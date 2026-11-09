---
layout: home
title: Home
---

<section class="hero">
  <img
    src="{{ '/assets/img/profile.jpg' | relative_url }}"
    alt="Seokhyun Moon"
    class="profile-avatar"
    width="560"
    height="560"
  />

  <div class="hero-copy">
    <h1 class="hero-name">Seokhyun Moon</h1>
    <p class="hero-role">
      InnoCORE Postdoctoral Researcher, KAIST
      <span class="hero-role-sep">·</span>
      <a href="https://wooyoun.kaist.ac.kr/" rel="noreferrer">Intelligent Chemistry Lab</a>
    </p>
    <p class="hero-lead">
      I am an InnoCORE postdoctoral researcher at KAIST working on AI-driven
      drug discovery. I build deep learning models for the structures and
      interactions of biomolecular complexes, and I am now working on agentic
      frameworks that go beyond single-target-based <em>in silico</em> drug
      discovery.
    </p>

      <div class="link-row" aria-label="contact and profile links">
        <a class="contact-pill" href="mailto:mshmjp@kaist.ac.kr">KAIST Email</a>
        <a class="contact-pill" href="mailto:mshmjp02@gmail.com">Gmail</a>
        <a class="contact-pill" href="https://scholar.google.com/citations?hl=ko&user=U1j8Ip8AAAAJ">Scholar</a>
        <a class="contact-pill" href="https://github.com/mseok">GitHub</a>
        <a class="contact-pill" href="https://www.linkedin.com/in/seokhyun-moon-a9229722b/">LinkedIn</a>
        <a class="contact-pill" href="{{ '/cv.pdf' | relative_url }}">CV</a>
      </div>
  </div>
</section>

<section id="research" class="home-section">
  <h2>Research</h2>
  <p>
    My research began with protein-ligand interaction prediction. In PIGNet
    and PIGNet2, I developed physics-informed models for binding affinity
    scoring and virtual screening, with a focus on generalization to unseen
    systems. I then moved from scoring given structures to predicting the
    structures themselves, working on co-folding and biomolecular complex
    structure prediction. I am one of the main developers of K-Fold, which
    models complex formation as a transition from the unbound components to
    the bound state.
  </p>
  <p>
    In parallel, I am interested in molecular generative models for lead
    optimization and <em>de novo</em> drug design.
  </p>
  <p>
    More recently, I have been working on agentic frameworks that aim to
    overcome the limitations of conventional single-target-based
    <em>in silico</em> drug discovery, and I am also interested in phenotypic
    drug discovery using virtual cells, where my previous work can be
    effectively leveraged. MoAgent, a hypothesis-driven multi-agent framework
    for drug mechanism-of-action discovery that I co-authored, is one example
    of the agentic direction.
  </p>
  <ul class="topic-list">
    <li>Biomolecular complex structure prediction</li>
    <li>Co-folding and molecular docking</li>
    <li>Physics-informed and equivariant deep learning</li>
    <li>Molecular generative models for lead optimization</li>
    <li>Agentic frameworks for drug discovery</li>
    <li>AI4Science infrastructure for reproducible research</li>
  </ul>
</section>

{%- assign pubs = site.data.scholar.publications -%}

<section id="publications" class="home-section">
  <div class="section-head">
    <h2>Publications</h2>
    <div class="pub-toggle" role="group" aria-label="Publication list">
      <button type="button" data-panel="selected" aria-pressed="true">Selected</button>
      <button type="button" data-panel="all" aria-pressed="false">All</button>
    </div>
  </div>
  <p class="pub-note"><sup>*</sup> Equal contribution &nbsp;·&nbsp; <sup>†</sup> Corresponding author</p>

  <div class="pub-panel sel-grid" data-panel="selected">
    {%- for n in (1..10) -%}
      {%- for p in pubs -%}
        {%- assign o = site.data.publications[p.id] -%}
        {%- if o.selected == n -%}
          {% include publication.html pub=p style="card" %}
        {%- endif -%}
      {%- endfor -%}
    {%- endfor -%}
  </div>

  <div class="pub-panel" data-panel="all" hidden>
  {%- comment -%} Year, then date (newest first); undated entries lead their year. {%- endcomment -%}
  {%- capture keys -%}
    {%- for p in pubs -%}
      {%- assign o = site.data.publications[p.id] -%}
      {%- unless o.hidden == true -%}
        {%- assign py = o.year | default: p.year | default: 0 -%}
        {%- assign pd = o.date | default: "9999-99-99" -%}
        {{ py | prepend: "0000" | slice: -4, 4 }}|{{ pd }}|{{ p.id }};
      {%- endunless -%}
    {%- endfor -%}
  {%- endcapture -%}
  {%- assign keys = keys | strip | split: ";" | sort | reverse -%}
  {%- assign current = "" -%}
  {%- for key in keys -%}
    {%- assign parts = key | strip | split: "|" -%}
    {%- assign y = parts[0] -%}
    {%- assign p = pubs | where: "id", parts[2] | first -%}
    {%- if y != current -%}
      {%- unless current == "" %}
    </ul>
  </div>
      {%- endunless %}
  <div class="pub-year">
    <h3>{% if y == "0000" %}Other{% else %}{{ y }}{% endif %}</h3>
    <ul class="pub-list">
      {%- assign current = y -%}
    {%- endif -%}
    {% include publication.html pub=p style="row" %}
  {%- endfor -%}
  {%- unless current == "" %}
    </ul>
  </div>
  {%- endunless %}
  </div>
</section>

<script>
  document.querySelectorAll(".pub-toggle button").forEach(function (button) {
    button.addEventListener("click", function () {
      document.querySelectorAll(".pub-toggle button").forEach(function (other) {
        other.setAttribute("aria-pressed", other === button ? "true" : "false");
      });
      document.querySelectorAll(".pub-panel").forEach(function (panel) {
        panel.hidden = panel.dataset.panel !== button.dataset.panel;
      });
    });
  });
</script>

<section class="home-section home-section-compact">
  <div class="home-meta-grid">
    <article>
      <h2>Invited Talks</h2>
      <ul class="meta-list">
        <li>
          <strong>Developing a generative model of protein-ligand complexations</strong><br />
          AI Star Fellowship Workshop, KAIST Graduate School of AI, Seoul, South Korea, November 2025
        </li>
        <li>
          <strong>Developing a generative model of protein-ligand complexations</strong><br />
          Symposium on AI New Drug Development Using Ultra-High Performance Supercomputing, MOGAM Institute for Biomedical Research, Seoul, South Korea, October 2025
        </li>
      </ul>
    </article>

    <article>
      <h2>Awards</h2>
      <ul class="meta-list">
        <li><strong>President's Award</strong>, Telecommunications Technology Association (AI-Champion), 2025</li>
        <li><strong>Recipient</strong>, 10th EDISON Computational Chemistry Software Application Competition, 2020</li>
        <li><strong>Recipient</strong>, KAIST Undergraduate Research Program Participation Prize, 2020</li>
        <li><strong>Recipient</strong>, Qualcomm-KAIST Innovation Awards, 2019</li>
      </ul>
    </article>
  </div>
</section>
