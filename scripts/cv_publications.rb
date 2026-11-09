# Write the CV publication entries (LaTeX for mseok/AcademicCV) from the
# site's publication data. Ruby standard library only; no model calls.
#
#   ruby cv_publications.rb <site repo> <output publications.tex>

require "json"
require "yaml"

site, out = ARGV
abort "usage: cv_publications.rb SITE_REPO OUTPUT_TEX" unless site && out

scholar = JSON.parse(File.read(File.join(site, "_data/scholar.json")))
overrides = YAML.safe_load(File.read(File.join(site, "_data/publications.yml"))) || {}

def tex(text)
  text.to_s
      .gsub(/[\u2010\u2011]/, "-")
      .gsub("\u00a0", " ")
      .gsub(/[\\{}&%$#_^~]/) { |c| { "\\" => "\\textbackslash{}", "^" => "\\^{}", "~" => "\\~{}" }.fetch(c, "\\#{c}") }
      .gsub("\u2026", "\\ldots{}")
end

def url(link)
  link.to_s.gsub(/[%#]/) { |c| "\\#{c}" }
end

def author(name)
  marks = name[/[*\u2020]+\z/].to_s
  base = name.chomp(marks).strip
  return "\\ldots" if base == "\u2026"
  body = base =~ /\A(Seokhyun Moon|S Moon)\z/ ? "\\textbf{#{tex(base)}}" : tex(base)
  "\\mbox{#{body}#{marks.gsub("\u2020", '$\\dagger$')}}"
end

def authors(list)
  names = list.split(/,\s*/).map { |n| author(n) }
  return names.join if names.size < 2
  names[0..-2].join(", ") + ", and " + names[-1]
end

entries = scholar["publications"].each_with_index.map do |pub, index|
  o = overrides[pub["id"]] || {}
  next if o["hidden"]
  links = o["links"] || []
  scholar_url = "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=#{scholar['profile']}" \
                "&citation_for_view=#{scholar['profile']}:#{pub['id']}"
  venues = (o["cv"] || {})["venues"] || [{ "text" => o["venue"] || pub["venue"], "url" => (links.first || {})["url"] || scholar_url }]
  labelled, plain = venues.partition { |v| v["label"] }
  parts = [labelled.map { |v| "#{v['label']} \\href{#{url(v['url'])}}{#{tex(v['text'])}}" }.join(", ")]
  parts += plain.map { |v| "\\href{#{url(v['url'])}}{#{tex(v['text'])}}" }
  code = links.find { |l| l["label"] == "Code" }
  parts << "\\href{#{url(code['url'])}}{Code}" if code
  { year: o["year"] || pub["year"], date: o["date"] || pub["date"], index: index, title: o["title"] || pub["title"],
    authors: o["authors"] || pub["authors"], note: (o["cv"] || {})["note"],
    venue_line: parts.reject(&:empty?).join(" | ") }
end.compact

# Year, then date (newest first); undated entries lead their year.
undated = "9999-99-99"
entries.sort! do |a, b|
  [b[:year] || 0, b[:date] || undated, a[:index]] <=> [a[:year] || 0, a[:date] || undated, b[:index]]
end

body = entries.map do |e|
  note = e[:note] ? "\n\n                \\vspace{0.10 cm}\n                #{tex(e[:note])}" : ""
  <<~TEX
    \\begin{twocolentry}{
        #{e[:year]}
    }
        \\textbf{#{tex(e[:title])}}
    \\end{twocolentry}

    \\vspace{0.10 cm}

    \\begin{onecolentry}
        #{authors(e[:authors])}#{note}

        \\vspace{0.10 cm}
        #{e[:venue_line]}
    \\end{onecolentry}

    \\vspace{0.20 cm}
  TEX
end

header = "% Generated from mseok/mseok.github.io (_data/scholar.json, _data/publications.yml).\n" \
         "% Edit _data/publications.yml there, not this file; the weekly job rewrites it.\n\n"
File.write(out, header + body.join("\n"))
