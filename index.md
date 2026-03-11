---
layout: home
title: Home
---

<section class="hero-shell">
  <div class="hero-main">
    <img
      src="{{ '/Profile.jpg' | relative_url }}"
      alt="Seokhyun Moon"
      class="profile-avatar"
    />

    <div class="hero-copy">
      <h1 class="hero-name">Seokhyun Moon</h1>
      <p class="hero-role">
        Ph.D. Candidate, KAIST Chemistry
        <span class="hero-role-sep">·</span>
        <a href="https://wooyoun.kaist.ac.kr/" rel="noreferrer">
          Intelligent Chemistry Lab
        </a>
      </p>
      <p class="eyebrow">aidd / molecular docking / molecular generative models</p>
      <p class="hero-lead">
        I am a Ph.D. Candidate in KAIST Chemistry working on AI-driven drug
        discovery. My recent work focuses on co-folding, molecular docking, and
        molecular generative models, with an emphasis on reliable structure and
        interaction modeling.
      </p>
      <p class="hero-note">
        This site collects research notes, technical posts, and project logs.
        Outside my core research, I am also increasingly interested in
        AI agent-driven automation and productivity workflows.
      </p>

      <div class="link-row" aria-label="contact and profile links">
        <a class="contact-pill" href="mailto:mshmjp@kaist.ac.kr">KAIST Email</a>
        <a class="contact-pill" href="mailto:mshmjp02@gmail.com">Gmail</a>
        <a class="contact-pill" href="https://scholar.google.com/citations?hl=ko&user=U1j8Ip8AAAAJ">Scholar</a>
        <a class="contact-pill" href="https://github.com/mseok">GitHub</a>
        <a class="contact-pill" href="https://www.linkedin.com/in/seokhyun-moon-a9229722b/">LinkedIn</a>
        <a class="contact-pill" href="https://drive.google.com/file/d/12OB_B7QWBLEFqM1p2qBWAxqZsP5dQxw3/view?usp=sharing">CV</a>
      </div>
    </div>
  </div>
</section>

<section id="research" class="home-section">
  <h2>Research</h2>
  <p>
    My research focuses on developing computational frameworks for understanding
    and predicting molecular interactions. Building on PIGNet, a
    physics-informed graph neural network for binding affinity estimation, I
    have worked on structure and binding affinity prediction for diverse
    biomolecular complexes. I am currently developing next-generation
    foundation models for biomolecular complex structure prediction.
  </p>
  <p>
    In parallel, I am interested in molecular generative models for lead
    optimization and <em>de novo</em> drug design, and more recently in
    phenotypic drug discovery using virtual cells, where my previous work can be
    effectively leveraged.
  </p>
  <ul class="research-list">
    <li>Biomolecular complex structure prediction</li>
    <li>Co-folding and molecular docking</li>
    <li>Physics-informed and equivariant deep learning</li>
    <li>Molecular generative models for lead optimization</li>
    <li>AI4Science infrastructure for reproducible research</li>
  </ul>
</section>

<section id="publications" class="home-section">
  <h2>Publications</h2>
  <div class="publication-list">
    <article class="publication-item">
      <h3>FragFM: Hierarchical Framework for Efficient Molecule Generation via Fragment-Level Discrete Flow Matching</h3>
      <p>Joongwon Lee, Seonghwan Kim, Seokhyun Moon, Hyunwoo Kim, and Woo Youn Kim</p>
      <p>ICLR 2026</p>
      <p><a href="https://arxiv.org/abs/2502.15805">Paper</a></p>
    </article>

    <article class="publication-item">
      <h3>MoAgent: A Hypothesis-Driven Multi-Agent Framework for Drug Mechanism of Action Discovery</h3>
      <p>Jun Hyeong Kim, Seokhyun Moon, Seonghwan Kim, Junhyeok Jeon, Taein Kim, Jisu Seo, Songmi Kim, and Woo Youn Kim</p>
      <p>NeurIPS 2025 Workshop: AI4D3, FM4LS</p>
      <p>
        <a href="https://openreview.net/forum?id=XY9yFyi4GF">Paper (AI4D3)</a>
        /
        <a href="https://openreview.net/forum?id=1fkPh6XTVe">Paper (FM4LS)</a>
      </p>
    </article>

    <article class="publication-item">
      <h3>Discrete Diffusion Schrodinger Bridge Matching for Graph Transformation</h3>
      <p>Jun Hyeong Kim, Seonghwan Kim, Seokhyun Moon, Hyeongwoo Kim, Jeheon Woo, and Woo Youn Kim</p>
      <p>ICLR 2025, NeurIPS 2024 Workshop: AI for New Drug Modalities</p>
      <p>
        <a href="https://arxiv.org/abs/2410.01500">Paper</a>
        /
        <a href="https://github.com/junhkim1226/DDSBM.git">Code</a>
      </p>
    </article>

    <article class="publication-item">
      <h3>DeepBioisostere: Discovering Bioisosteres with Deep Learning for a Fine Control of Multiple Molecular Properties</h3>
      <p>Hyeongwoo Kim, Seokhyun Moon, Wonho Zhung, and Woo Youn Kim</p>
      <p>Under Review</p>
      <p>
        <a href="https://arxiv.org/abs/2403.02706">Paper</a>
        /
        <a href="https://github.com/Hwoo-Kim/DeepBioisostere.git">Code</a>
      </p>
    </article>

    <article class="publication-item">
      <h3>Toward Generalizable Structure-Based Deep Learning Models for Protein-Ligand Interaction Prediction: Challenges and Strategies</h3>
      <p>Seokhyun Moon, Wonho Zhung, and Woo Youn Kim</p>
      <p><em>WIREs Computational Molecular Science</em>, 2024</p>
      <p><a href="https://doi.org/10.1002/wcms.1705">Paper</a></p>
    </article>

    <article class="publication-item">
      <h3>PIGNet2: A Versatile Deep Learning-based Protein-Ligand Interaction Prediction Model for Binding Affinity Scoring and Virtual Screening</h3>
      <p>Seokhyun Moon, Sang-Yeon Hwang, Jaechang Lim, and Woo Youn Kim</p>
      <p><em>Digital Discovery</em>, 2024</p>
      <p>
        <a href="https://doi.org/10.1039/D3DD00149K">Paper</a>
        /
        <a href="https://github.com/mseok/pignet2">Code</a>
      </p>
    </article>

    <article class="publication-item">
      <h3>GeoTMI: Predicting Quantum Chemical Property with Easy-to-Obtain Geometry via Positional Denoising</h3>
      <p>Hyeonsu Kim, Jeheon Woo, Seonghwan Kim, Seokhyun Moon, Jun Hyeong Kim, and Woo Youn Kim</p>
      <p>NeurIPS, 2023</p>
      <p>
        <a href="https://openreview.net/forum?id=5JcKKRX2iH">Paper</a>
        /
        <a href="https://github.com/Imfinethankyou1/GeoTMI">Code</a>
      </p>
    </article>

    <article class="publication-item">
      <h3>PIGNet: a physics-informed deep learning model toward generalized drug-target interaction prediction</h3>
      <p>Seokhyun Moon, Wonho Zhung, Soojung Yang, Jaechang Lim, and Woo Youn Kim</p>
      <p><em>Chemical Science</em>, 2022</p>
      <p>
        <a href="https://doi.org/10.1039/D1SC06946B">Paper</a>
        /
        <a href="https://github.com/ace-kaist/pignet">Code</a>
      </p>
    </article>

    <article class="publication-item">
      <h3>Scaffold-based molecular design with a graph generative model</h3>
      <p>Jaechang Lim, Sang-Yeon Hwang, Seokhyun Moon, Seungsu Kim, and Woo Youn Kim</p>
      <p><em>Chemical Science</em>, 2020</p>
      <p>
        <a href="https://pubs.rsc.org/en/content/articlelanding/2020/sc/c9sc04503a">Paper</a>
        /
        <a href="https://github.com/jaechanglim/GGM">Code</a>
      </p>
    </article>
  </div>
</section>

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
