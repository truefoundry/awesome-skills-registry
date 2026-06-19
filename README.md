<h1 align="center">TrueFoundry Skills Registry</h1>

![TrueFoundry Skills Registry — the open agent skills ecosystem](images/tf_banner.svg)

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome" /></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome" /></a>
  <a href="#license"><img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=flat-square" alt="License: Apache-2.0" /></a>
</p>

<p align="center">
  <!-- skills-count-start -->
  <img src="https://img.shields.io/badge/skills-1023-6E56CF?style=flat-square" alt="1023 skills" />
  <!-- skills-count-end -->
  <img src="https://img.shields.io/badge/official-91-22C55E?style=flat-square" alt="91 official skills" />
  <img src="https://img.shields.io/badge/sources-71_repos-3B82F6?style=flat-square" alt="71 source repos" />
</p>

<p align="center">
  <a href="https://x.com/truefoundry"><img src="https://img.shields.io/badge/Follow%20on%20X-000000?style=for-the-badge&logo=x&logoColor=white" alt="Follow on X" /></a>
  <a href="https://www.linkedin.com/company/truefoundry"><img src="https://img.shields.io/badge/Follow%20on%20LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Follow on LinkedIn" /></a>
  <a href="https://discord.gg/truefoundry"><img src="https://img.shields.io/badge/Join%20our%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Join our Discord" /></a>
</p>

---

## Contents

- [Skills](#skills)
- [Getting Started](#getting-started)
- [Using the Catalog](#using-the-catalog)
- [Creating Skills](#creating-skills)
- [Registry Entry Format](#registry-entry-format)
- [Contributing](#contributing)
- [Resources](#resources)
- [License](#license)

## Skills

Browse the full catalog grouped by publisher. The most popular publishers are
expanded by default — click any collapsed section to reveal its skills. This
section is generated from the registry by
[`scripts/build_readme_skills.py`](scripts/build_readme_skills.py); run it after
new skills land to refresh the listing.

<!-- skills-list-start -->

<details open>
<summary><strong>Official Claude Skills</strong> &nbsp;·&nbsp; 17 skills &nbsp;·&nbsp; ⭐ 149,805 &nbsp;·&nbsp; official</summary>

- [anthropics/algorithmic-art](https://github.com/anthropics/skills/tree/HEAD/skills/algorithmic-art) — Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration.
- [anthropics/brand-guidelines](https://github.com/anthropics/skills/tree/HEAD/skills/brand-guidelines) — Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic…
- [anthropics/canvas-design](https://github.com/anthropics/skills/tree/HEAD/skills/canvas-design) — Create beautiful visual art in .png and .pdf documents using design philosophy.
- [anthropics/claude-api](https://github.com/anthropics/skills/tree/HEAD/skills/claude-api) — Build, debug, and optimize Claude API / Anthropic SDK apps.
- [anthropics/doc-coauthoring](https://github.com/anthropics/skills/tree/HEAD/skills/doc-coauthoring) — Guide users through a structured workflow for co-authoring documentation.
- [anthropics/frontend-design](https://github.com/anthropics/skills/tree/HEAD/skills/frontend-design) — Create distinctive, production-grade frontend interfaces with high design quality.
- [anthropics/internal-comms](https://github.com/anthropics/skills/tree/HEAD/skills/internal-comms) — A set of resources to help me write all kinds of internal communications, using the formats that my company likes to us…
- [anthropics/mcp-builder](https://github.com/anthropics/skills/tree/HEAD/skills/mcp-builder) — Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external service…
- [anthropics/pdf](https://github.com/anthropics/skills/tree/HEAD/skills/pdf) — Use this skill whenever the user wants to do anything with PDF files.
- [anthropics/pptx](https://github.com/anthropics/skills/tree/HEAD/skills/pptx) — Use this skill any time a .pptx file is involved in any way — as input, output, or both.
- [anthropics/skill-creator](https://github.com/anthropics/skills/tree/HEAD/skills/skill-creator) — Create new skills, modify and improve existing skills, and measure skill performance.
- [anthropics/slack-gif-creator](https://github.com/anthropics/skills/tree/HEAD/skills/slack-gif-creator) — Knowledge and utilities for creating animated GIFs optimized for Slack.
- [anthropics/theme-factory](https://github.com/anthropics/skills/tree/HEAD/skills/theme-factory) — Toolkit for styling artifacts with a theme.
- [anthropics/webapp-testing](https://github.com/anthropics/skills/tree/HEAD/skills/webapp-testing) — Toolkit for interacting with and testing local web applications using Playwright.
- [anthropics/web-artifacts-builder](https://github.com/anthropics/skills/tree/HEAD/skills/web-artifacts-builder) — Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies…
- [anthropics/docx](https://github.com/anthropics/skills/tree/HEAD/skills/docx) — Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files).
- [anthropics/xlsx](https://github.com/anthropics/skills/tree/HEAD/skills/xlsx) — Use this skill any time a spreadsheet file is the primary input or output.

</details>

<details open>
<summary><strong>Mattpocock</strong> &nbsp;·&nbsp; 29 skills &nbsp;·&nbsp; ⭐ 126,573</summary>

- [mattpocock/handoff](https://github.com/mattpocock/skills/tree/HEAD/skills/productivity/handoff) — Compact the current conversation into a handoff document for another agent to pick up.
- [mattpocock/caveman](https://github.com/mattpocock/skills/tree/HEAD/skills/productivity/caveman) — Ultra-compressed communication mode.
- [mattpocock/review](https://github.com/mattpocock/skills/tree/HEAD/skills/in-progress/review) — Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes — Standards (does the code f…
- [mattpocock/to-prd](https://github.com/mattpocock/skills/tree/HEAD/skills/engineering/to-prd) — Turn the current conversation context into a PRD and publish it to the project issue tracker.
- [mattpocock/design-an-interface](https://github.com/mattpocock/skills/tree/HEAD/skills/deprecated/design-an-interface) — Generate multiple radically different interface designs for a module using parallel sub-agents.
- [mattpocock/diagnose](https://github.com/mattpocock/skills/tree/HEAD/skills/engineering/diagnose) — Disciplined diagnosis loop for hard bugs and performance regressions.
- [mattpocock/edit-article](https://github.com/mattpocock/skills/tree/HEAD/skills/personal/edit-article) — Edit and improve articles by restructuring sections, improving clarity, and tightening prose.
- [mattpocock/git-guardrails-claude-code](https://github.com/mattpocock/skills/tree/HEAD/skills/misc/git-guardrails-claude-code) — Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execu…
- [mattpocock/grill-me](https://github.com/mattpocock/skills/tree/HEAD/skills/productivity/grill-me) — Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of th…
- [mattpocock/grill-with-docs](https://github.com/mattpocock/skills/tree/HEAD/skills/engineering/grill-with-docs) — Grilling session that challenges your plan against the existing domain model, sharpens terminology, and updates documen…
- [mattpocock/improve-codebase-architecture](https://github.com/mattpocock/skills/tree/HEAD/skills/engineering/improve-codebase-architecture) — Find deepening opportunities in a codebase, informed by the domain language in CONTEXT.md and the decisions in docs/adr…
- [mattpocock/triage](https://github.com/mattpocock/skills/tree/HEAD/skills/engineering/triage) — Triage issues through a state machine driven by triage roles.
- [mattpocock/migrate-to-shoehorn](https://github.com/mattpocock/skills/tree/HEAD/skills/misc/migrate-to-shoehorn) — Migrate test files from `as` type assertions to @total-typescript/shoehorn.
- [mattpocock/obsidian-vault](https://github.com/mattpocock/skills/tree/HEAD/skills/personal/obsidian-vault) — Search, create, and manage notes in the Obsidian vault with wikilinks and index notes.
- [mattpocock/to-issues](https://github.com/mattpocock/skills/tree/HEAD/skills/engineering/to-issues) — Break a plan, spec, or PRD into independently-grabbable issues on the project issue tracker using tracer-bullet vertica…
- [mattpocock/qa](https://github.com/mattpocock/skills/tree/HEAD/skills/deprecated/qa) — Interactive QA session where user reports bugs or issues conversationally, and the agent files GitHub issues.
- [mattpocock/prototype](https://github.com/mattpocock/skills/tree/HEAD/skills/engineering/prototype) — Build a throwaway prototype to flesh out a design before committing to it.
- [mattpocock/request-refactor-plan](https://github.com/mattpocock/skills/tree/HEAD/skills/deprecated/request-refactor-plan) — Create a detailed refactor plan with tiny commits via user interview, then file it as a GitHub issue.
- [mattpocock/scaffold-exercises](https://github.com/mattpocock/skills/tree/HEAD/skills/misc/scaffold-exercises) — Create exercise directory structures with sections, problems, solutions, and explainers that pass linting.
- [mattpocock/setup-matt-pocock-skills](https://github.com/mattpocock/skills/tree/HEAD/skills/engineering/setup-matt-pocock-skills) — Sets up an `## Agent skills` block in AGENTS.md/CLAUDE.md and `docs/agents/` so the engineering skills know this repo's…
- [mattpocock/setup-pre-commit](https://github.com/mattpocock/skills/tree/HEAD/skills/misc/setup-pre-commit) — Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo.
- [mattpocock/tdd](https://github.com/mattpocock/skills/tree/HEAD/skills/engineering/tdd) — Test-driven development with red-green-refactor loop.
- [mattpocock/teach](https://github.com/mattpocock/skills/tree/HEAD/skills/in-progress/teach) — Teach the user a new skill or concept, within this workspace.
- [mattpocock/ubiquitous-language](https://github.com/mattpocock/skills/tree/HEAD/skills/deprecated/ubiquitous-language) — Extract a DDD-style ubiquitous language glossary from the current conversation, flagging ambiguities and proposing cano…
- [mattpocock/write-a-skill](https://github.com/mattpocock/skills/tree/HEAD/skills/productivity/write-a-skill) — Create new agent skills with proper structure, progressive disclosure, and bundled resources.
- [mattpocock/writing-beats](https://github.com/mattpocock/skills/tree/HEAD/skills/in-progress/writing-beats) — Shape an article as a journey of beats, choose-your-own-adventure style.
- [mattpocock/writing-fragments](https://github.com/mattpocock/skills/tree/HEAD/skills/in-progress/writing-fragments) — Grilling session that mines the user for fragments — heterogeneous nuggets of writing (claims, vignettes, sharp sentenc…
- [mattpocock/writing-shape](https://github.com/mattpocock/skills/tree/HEAD/skills/in-progress/writing-shape) — Take a markdown file of raw material and shape it into an article through a conversational session — drafting candidate…
- [mattpocock/zoom-out](https://github.com/mattpocock/skills/tree/HEAD/skills/engineering/zoom-out) — Tell the agent to zoom out and give broader context or a higher-level perspective.

</details>

<details open>
<summary><strong>Leonxlnx</strong> &nbsp;·&nbsp; 13 skills &nbsp;·&nbsp; ⭐ 42,062</summary>

- [Leonxlnx/brandkit](https://github.com/Leonxlnx/taste-skill/tree/HEAD/skills/brandkit) — Premium brand-kit image generation skill for creating high-end brand-guidelines boards, logo systems, identity decks, a…
- [Leonxlnx/brutalist-skill](https://github.com/Leonxlnx/taste-skill/tree/HEAD/skills/brutalist-skill) — Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics.
- [Leonxlnx/output-skill](https://github.com/Leonxlnx/taste-skill/tree/HEAD/skills/output-skill) — Overrides default LLM truncation behavior.
- [Leonxlnx/gpt-tasteskill](https://github.com/Leonxlnx/taste-skill/tree/HEAD/skills/gpt-tasteskill) — Elite UX/UI & Advanced GSAP Motion Engineer.
- [Leonxlnx/soft-skill](https://github.com/Leonxlnx/taste-skill/tree/HEAD/skills/soft-skill) — Teaches the AI to design like a high-end agency.
- [Leonxlnx/image-to-code-skill](https://github.com/Leonxlnx/taste-skill/tree/HEAD/skills/image-to-code-skill) — Elite website image-to-code skill for Codex.
- [Leonxlnx/minimalist-skill](https://github.com/Leonxlnx/taste-skill/tree/HEAD/skills/minimalist-skill) — Clean editorial-style interfaces.
- [Leonxlnx/imagegen-frontend-mobile](https://github.com/Leonxlnx/taste-skill/tree/HEAD/skills/imagegen-frontend-mobile) — Elite mobile app image-generation skill for creating premium, app-native screen concepts and flows.
- [Leonxlnx/stitch-skill](https://github.com/Leonxlnx/taste-skill/tree/HEAD/skills/stitch-skill) — Semantic Design System Skill for Google Stitch.
- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill/tree/HEAD/skills/taste-skill) — Anti-slop frontend skill for landing pages, portfolios, and redesigns.
- [Leonxlnx/taste-skill-v1](https://github.com/Leonxlnx/taste-skill/tree/HEAD/skills/taste-skill-v1) — The original v1 taste-skill, preserved for projects depending on its exact behavior.
- [Leonxlnx/imagegen-frontend-web](https://github.com/Leonxlnx/taste-skill/tree/HEAD/skills/imagegen-frontend-web) — Elite frontend image-direction skill for generating premium, conversion-aware website design references.
- [Leonxlnx/redesign-skill](https://github.com/Leonxlnx/taste-skill/tree/HEAD/skills/redesign-skill) — Upgrades existing websites and apps to premium quality.

</details>

<details open>
<summary><strong>Coreyhaines31</strong> &nbsp;·&nbsp; 43 skills &nbsp;·&nbsp; ⭐ 33,005</summary>

- [coreyhaines31/ab-testing](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/ab-testing) — When the user wants to plan, design, or implement an A/B test or experiment, or build a growth experimentation program.
- [coreyhaines31/ad-creative](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/ad-creative) — When the user wants to generate, iterate, or scale ad creative — headlines, descriptions, primary text, or full ad vari…
- [coreyhaines31/ads](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/ads) — When the user wants help with paid advertising campaigns on Google Ads, Meta (Facebook/Instagram), LinkedIn, Twitter/X,…
- [coreyhaines31/ai-seo](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/ai-seo) — When the user wants to optimize content for AI search engines, get cited by LLMs, or appear in AI-generated answers.
- [coreyhaines31/video](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/video) — When the user wants to create, generate, or produce video content using AI tools or programmatic frameworks.
- [coreyhaines31/analytics](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/analytics) — When the user wants to set up, improve, or audit analytics tracking and measurement.
- [coreyhaines31/aso](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/aso) — When the user wants to audit or optimize an App Store or Google Play listing.
- [coreyhaines31/churn-prevention](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/churn-prevention) — When the user wants to reduce churn, build cancellation flows, set up save offers, recover failed payments, or implemen…
- [coreyhaines31/co-marketing](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/co-marketing) — When the user wants to find co-marketing partners, plan joint campaigns, or brainstorm partnership opportunities.
- [coreyhaines31/cold-email](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/cold-email) — Write B2B cold emails and follow-up sequences that get replies.
- [coreyhaines31/community-marketing](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/community-marketing) — Build and leverage online communities to drive product growth and brand loyalty.
- [coreyhaines31/competitors](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/competitors) — When the user wants to create competitor comparison or alternative pages for SEO and sales enablement.
- [coreyhaines31/competitor-profiling](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/competitor-profiling) — When the user wants to research, profile, or analyze competitors from their URLs.
- [coreyhaines31/content-strategy](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/content-strategy) — When the user wants to plan a content strategy, decide what content to create, or figure out what topics to cover.
- [coreyhaines31/cro](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/cro) — When the user wants to optimize, improve, or increase conversions on any marketing page or form — including homepage, l…
- [coreyhaines31/copy-editing](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/copy-editing) — When the user wants to edit, review, or improve existing marketing copy, or refresh outdated content.
- [coreyhaines31/copywriting](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/copywriting) — When the user wants to write, rewrite, or improve marketing copy for any page — including homepage, landing pages, pric…
- [coreyhaines31/customer-research](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/customer-research) — When the user wants to conduct, analyze, or synthesize customer research.
- [coreyhaines31/directory-submissions](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/directory-submissions) — When the user wants to submit their product to startup, SaaS, AI, agent, MCP, no-code, or review directories for backli…
- [coreyhaines31/emails](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/emails) — When the user wants to create or optimize an email sequence, drip campaign, automated email flow, or lifecycle email pr…
- [coreyhaines31/free-tools](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/free-tools) — When the user wants to plan, evaluate, or build a free tool for marketing purposes — lead generation, SEO value, or bra…
- [coreyhaines31/lead-magnets](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/lead-magnets) — When the user wants to create, plan, or optimize a lead magnet for email capture or lead generation.
- [coreyhaines31/marketing-ideas](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/marketing-ideas) — When the user needs marketing ideas, inspiration, or strategies for their SaaS or software product.
- [coreyhaines31/image](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/image) — When the user wants to create, generate, edit, or optimize images for marketing — blog heroes, social graphics, product…
- [coreyhaines31/marketing-plan](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/marketing-plan) — When the user needs a comprehensive marketing plan for a client, a company they advise, or their own product.
- [coreyhaines31/marketing-psychology](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/marketing-psychology) — When the user wants to apply psychological principles, mental models, or behavioral science to marketing.
- [coreyhaines31/paywalls](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/paywalls) — When the user wants to create or optimize in-app paywalls, upgrade screens, upsell modals, or feature gates.
- [coreyhaines31/popups](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/popups) — When the user wants to create or optimize popups, modals, overlays, slide-ins, or banners for conversion purposes.
- [coreyhaines31/pricing](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/pricing) — When the user wants help with pricing decisions, packaging, or monetization strategy.
- [coreyhaines31/launch](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/launch) — When the user wants to plan a product launch, feature announcement, or release strategy.
- [coreyhaines31/product-marketing](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/product-marketing) — When the user wants to create or update their product marketing context document.
- [coreyhaines31/programmatic-seo](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/programmatic-seo) — When the user wants to create SEO-driven pages at scale using templates and data.
- [coreyhaines31/referrals](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/referrals) — When the user wants to create, optimize, or analyze a referral program, affiliate program, or word-of-mouth strategy.
- [coreyhaines31/revops](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/revops) — When the user wants help with revenue operations, lead lifecycle management, or marketing-to-sales handoff processes.
- [coreyhaines31/sales-enablement](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/sales-enablement) — When the user wants to create sales collateral, pitch decks, one-pagers, objection handling docs, or demo scripts.
- [coreyhaines31/prospecting](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/prospecting) — When the user wants to find, qualify, and build a list of prospects to reach out to — across B2B SaaS, general B2B, or…
- [coreyhaines31/schema](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/schema) — When the user wants to add, fix, or optimize schema markup and structured data on their site.
- [coreyhaines31/seo-audit](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/seo-audit) — When the user wants to audit, review, or diagnose SEO issues on their site.
- [coreyhaines31/signup](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/signup) — When the user wants to optimize signup, registration, account creation, or trial activation flows.
- [coreyhaines31/site-architecture](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/site-architecture) — When the user wants to plan, map, or restructure their website's page hierarchy, navigation, URL structure, or internal…
- [coreyhaines31/sms](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/sms) — When the user wants to plan, build, or optimize SMS or MMS marketing — including welcome flows, abandoned cart texts, p…
- [coreyhaines31/social](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/social) — When the user wants help creating, scheduling, or optimizing social media content for LinkedIn, Twitter/X, Instagram, T…
- [coreyhaines31/onboarding](https://github.com/coreyhaines31/marketingskills/tree/HEAD/skills/onboarding) — When the user wants to optimize post-signup onboarding, user activation, first-run experience, or time-to-value.

</details>

<details open>
<summary><strong>K Dense AI</strong> &nbsp;·&nbsp; 143 skills &nbsp;·&nbsp; ⭐ 28,042</summary>

- [K-Dense-AI/adaptyv](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/adaptyv) — How to use the Adaptyv Bio Foundry API and Python SDK for protein experiment design, submission, and results retrieval.
- [K-Dense-AI/aeon](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/aeon) — This skill should be used for time series machine learning tasks including classification, regression, clustering, fore…
- [K-Dense-AI/anndata](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/anndata) — Data structure for annotated matrices in single-cell analysis.
- [K-Dense-AI/arboreto](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/arboreto) — Infer gene regulatory networks (GRNs) from gene expression data using scalable algorithms (GRNBoost2, GENIE3).
- [K-Dense-AI/astropy](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/astropy) — Core Python library for astronomy and astrophysics workflows that need Astropy APIs, including units/quantities, coordi…
- [K-Dense-AI/autoskill](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/autoskill) — Observe the user's screen via screenpipe, detect repeated research workflows, match them against existing scientific-ag…
- [K-Dense-AI/benchling-integration](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/benchling-integration) — Benchling Python SDK and REST API integration for registry entities, inventory, ELN entries, workflows, Benchling Apps,…
- [K-Dense-AI/bgpt-paper-search](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/bgpt-paper-search) — Search scientific papers and retrieve structured experimental data extracted from full-text studies via the BGPT MCP se…
- [K-Dense-AI/bids](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/bids) — Use this skill when working with Brain Imaging Data Structure (BIDS) datasets: organizing neuroscience and biomedical d…
- [K-Dense-AI/biopython](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/biopython) — Comprehensive molecular biology toolkit.
- [K-Dense-AI/bioservices](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/bioservices) — Unified Python interface to 40+ bioinformatics services.
- [K-Dense-AI/bulk-rnaseq](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/bulk-rnaseq) — End-to-end bulk RNA-seq orchestrator — takes raw FASTQ reads through QC and trimming (FastQC, fastp/Trim Galore), align…
- [K-Dense-AI/cellxgene-census](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/cellxgene-census) — Query the CELLxGENE Census (61M+ cells) programmatically.
- [K-Dense-AI/cirq](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/cirq) — Google quantum computing framework.
- [K-Dense-AI/citation-management](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/citation-management) — Comprehensive citation management for academic research.
- [K-Dense-AI/clinical-decision-support](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/clinical-decision-support) — Generate professional clinical decision support (CDS) documents for pharmaceutical and clinical research settings, incl…
- [K-Dense-AI/clinical-reports](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/clinical-reports) — Write comprehensive clinical reports including case reports (CARE guidelines), diagnostic reports (radiology/pathology/…
- [K-Dense-AI/cobrapy](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/cobrapy) — Constraint-based metabolic modeling (COBRA).
- [K-Dense-AI/consciousness-council](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/consciousness-council) — Run a multi-perspective Mind Council deliberation on any question, decision, or creative challenge.
- [K-Dense-AI/dask](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/dask) — Distributed computing for larger-than-RAM pandas/NumPy workflows.
- [K-Dense-AI/database-lookup](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/database-lookup) — Search 78 public scientific, biomedical, materials science, and economic databases via REST APIs.
- [K-Dense-AI/datamol](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/datamol) — Pythonic wrapper around RDKit with simplified interface and sensible defaults.
- [K-Dense-AI/deepchem](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/deepchem) — Molecular ML with diverse featurizers and pre-built datasets.
- [K-Dense-AI/deeptools](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/deeptools) — NGS analysis toolkit.
- [K-Dense-AI/depmap](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/depmap) — Query the Cancer Dependency Map (DepMap) for cancer cell line gene dependency scores (CRISPR Chronos), drug sensitivity…
- [K-Dense-AI/dhdna-profiler](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/dhdna-profiler) — Extract cognitive patterns and thinking fingerprints from any text.
- [K-Dense-AI/diffdock](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/diffdock) — Diffusion-based molecular docking.
- [K-Dense-AI/dnanexus-integration](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/dnanexus-integration) — DNAnexus cloud genomics platform.
- [K-Dense-AI/esm](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/esm) — Comprehensive toolkit for EvolutionaryScale protein language models including ESM3 (generative multimodal design across…
- [K-Dense-AI/etetoolkit](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/etetoolkit) — Phylogenetic tree toolkit (ETE).
- [K-Dense-AI/exa-search](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/exa-search) — Web toolkit powered by Exa, tuned for scientific and technical content.
- [K-Dense-AI/exploratory-data-analysis](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/exploratory-data-analysis) — Perform comprehensive exploratory data analysis on scientific data files across 200+ file formats.
- [K-Dense-AI/flowio](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/flowio) — Parse FCS (Flow Cytometry Standard) files v2.0-3.1.
- [K-Dense-AI/fluidsim](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/fluidsim) — Framework for computational fluid dynamics simulations using Python.
- [K-Dense-AI/generate-image](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/generate-image) — Generate or edit images using AI models (FLUX, Nano Banana 2).
- [K-Dense-AI/geniml](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/geniml) — This skill should be used when working with genomic interval data (BED files) for machine learning tasks.
- [K-Dense-AI/geomaster](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/geomaster) — Comprehensive geospatial science skill covering remote sensing, GIS, spatial analysis, machine learning for earth obser…
- [K-Dense-AI/geopandas](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/geopandas) — Python library for working with geospatial vector data including shapefiles, GeoJSON, and GeoPackage files.
- [K-Dense-AI/get-available-resources](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/get-available-resources) — This skill should be used at the start of any computationally intensive scientific task to detect and report available…
- [K-Dense-AI/gget](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/gget) — Fast CLI/Python queries to 20+ bioinformatics databases.
- [K-Dense-AI/ginkgo-cloud-lab](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/ginkgo-cloud-lab) — Submit and manage protocols on Ginkgo Bioworks Cloud Lab (cloud.ginkgo.bio), a web-based interface for autonomous lab e…
- [K-Dense-AI/glycoengineering](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/glycoengineering) — Analyze and engineer protein glycosylation.
- [K-Dense-AI/gtars](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/gtars) — High-performance toolkit for genomic interval analysis in Rust with Python bindings.
- [K-Dense-AI/histolab](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/histolab) — Lightweight WSI tile extraction and preprocessing.
- [K-Dense-AI/hugging-science](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/hugging-science) — Use when the user is doing AI/ML work in a scientific domain such as biology, chemistry, physics, astronomy, climate, g…
- [K-Dense-AI/transformers](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/transformers) — Hugging Face Transformers for loading Hub models, running pipeline inference, text generation, and Trainer fine-tuning…
- [K-Dense-AI/hypogenic](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/hypogenic) — Automated LLM-driven hypothesis generation and testing on tabular datasets.
- [K-Dense-AI/hypothesis-generation](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/hypothesis-generation) — Structured hypothesis formulation from observations.
- [K-Dense-AI/imaging-data-commons](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/imaging-data-commons) — Query and download public cancer imaging data from NCI Imaging Data Commons using idc-index.
- [K-Dense-AI/infographics](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/infographics) — Create professional infographics using Nano Banana Pro AI with smart iterative refinement.
- [K-Dense-AI/iso-13485-certification](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/iso-13485-certification) — Comprehensive toolkit for preparing ISO 13485 certification documentation for medical device Quality Management Systems.
- [K-Dense-AI/labarchive-integration](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/labarchive-integration) — Electronic lab notebook API integration.
- [K-Dense-AI/lamindb](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/lamindb) — Use when working with LaminDB, the open-source lineage-native lakehouse for biological datasets and models.
- [K-Dense-AI/latchbio-integration](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/latchbio-integration) — Latch platform for bioinformatics workflows.
- [K-Dense-AI/latex-posters](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/latex-posters) — Create professional research posters in LaTeX using beamerposter, tikzposter, or baposter.
- [K-Dense-AI/liteparse](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/liteparse) — Local document and PDF parsing with spatial text and bounding boxes.
- [K-Dense-AI/literature-review](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/literature-review) — Conduct comprehensive, systematic literature reviews using multiple academic databases (PubMed, arXiv, bioRxiv, Semanti…
- [K-Dense-AI/markdown-mermaid-writing](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/markdown-mermaid-writing) — Comprehensive markdown and Mermaid diagram writing skill.
- [K-Dense-AI/market-research-reports](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/market-research-reports) — Generate comprehensive market research reports (50+ pages) in the style of top consulting firms (McKinsey, BCG, Gartner…
- [K-Dense-AI/markitdown](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/markitdown) — Convert files and office documents to Markdown.
- [K-Dense-AI/matchms](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/matchms) — Spectral similarity and compound identification for metabolomics.
- [K-Dense-AI/matlab](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/matlab) — MATLAB and GNU Octave numerical computing for matrix operations, data analysis, visualization, and scientific computing.
- [K-Dense-AI/matplotlib](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/matplotlib) — Low-level plotting library for full customization.
- [K-Dense-AI/medchem](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/medchem) — Medicinal chemistry filters for compound triage.
- [K-Dense-AI/treatment-plans](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/treatment-plans) — Generate concise (3-4 page), focused medical treatment plans in LaTeX/PDF format for all clinical specialties.
- [K-Dense-AI/modal](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/modal) — Modal is a serverless cloud platform for running Python on demand, including on-demand GPUs.
- [K-Dense-AI/molecular-dynamics](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/molecular-dynamics) — Run and analyze molecular dynamics simulations with OpenMM and MDAnalysis.
- [K-Dense-AI/molfeat](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/molfeat) — Molecular featurization for ML (100+ featurizers).
- [K-Dense-AI/networkx](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/networkx) — Comprehensive toolkit for creating, analyzing, and visualizing complex networks and graphs in Python.
- [K-Dense-AI/neurokit2](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/neurokit2) — Comprehensive biosignal processing toolkit for analyzing physiological data including ECG, EEG, EDA, RSP, PPG, EMG, and…
- [K-Dense-AI/neuropixels-analysis](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/neuropixels-analysis) — Analyze Neuropixels extracellular recordings end-to-end with SpikeInterface.
- [K-Dense-AI/nextflow](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/nextflow) — Build, run, and debug Nextflow data pipelines and nf-core workflows end to end.
- [K-Dense-AI/omero-integration](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/omero-integration) — Microscopy data management platform.
- [K-Dense-AI/open-notebook](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/open-notebook) — Self-hosted, open-source alternative to Google NotebookLM for AI-powered research and document analysis.
- [K-Dense-AI/opentrons-integration](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/opentrons-integration) — Official Opentrons Protocol API for OT-2 and Flex robots.
- [K-Dense-AI/optimize-for-gpu](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/optimize-for-gpu) — GPU-accelerate Python code using CuPy, Numba CUDA, Warp, cuDF, cuML, cuGraph, KvikIO, cuCIM, cuxfilter, cuVS, cuSpatial…
- [K-Dense-AI/pacsomatic](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/pacsomatic) — Operator toolkit for nf-core/pacsomatic matched tumor-normal workflows from BAM inputs.
- [K-Dense-AI/paper-lookup](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/paper-lookup) — Search 10 academic paper databases via REST APIs for research papers, preprints, and scholarly articles.
- [K-Dense-AI/paperzilla](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/paperzilla) — Chat with your agent about projects, recommendations, and canonical papers in Paperzilla.
- [K-Dense-AI/parallel-web](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/parallel-web) — All-in-one web toolkit powered by parallel-cli, with a strong emphasis on academic and scientific sources.
- [K-Dense-AI/pathml](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/pathml) — Full-featured computational pathology toolkit.
- [K-Dense-AI/pathway-enrichment](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/pathway-enrichment) — Run pathway and gene-set enrichment analysis on gene lists or ranked gene data, then interpret the results.
- [K-Dense-AI/pdf](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/pdf) — Use this skill whenever the user wants to do anything with PDF files.
- [K-Dense-AI/peer-review](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/peer-review) — Structured manuscript/grant review with checklist-based evaluation.
- [K-Dense-AI/pennylane](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/pennylane) — Hardware-agnostic quantum ML framework with automatic differentiation.
- [K-Dense-AI/phylogenetics](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/phylogenetics) — Build and analyze phylogenetic trees using MAFFT (multiple alignment), IQ-TREE 2 (maximum likelihood), and FastTree (fa…
- [K-Dense-AI/polars-bio](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/polars-bio) — High-performance genomic interval operations and bioinformatics file I/O on Polars DataFrames.
- [K-Dense-AI/polars](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/polars) — Fast in-memory DataFrame library for datasets that fit in RAM.
- [K-Dense-AI/pptx](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/pptx) — Use this skill any time a .pptx file is involved in any way — as input, output, or both.
- [K-Dense-AI/pptx-posters](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/pptx-posters) — Create research posters using HTML/CSS that can be exported to PDF or PPTX.
- [K-Dense-AI/primekg](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/primekg) — Query the Precision Medicine Knowledge Graph (PrimeKG) for multiscale biological data including genes, drugs, diseases,…
- [K-Dense-AI/protocolsio-integration](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/protocolsio-integration) — Integration with protocols.io API for managing scientific protocols.
- [K-Dense-AI/pufferlib](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/pufferlib) — High-performance reinforcement learning framework optimized for speed and scale.
- [K-Dense-AI/pydeseq2](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/pydeseq2) — Differential gene expression analysis (Python DESeq2).
- [K-Dense-AI/pydicom](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/pydicom) — Python library for working with DICOM (Digital Imaging and Communications in Medicine) files.
- [K-Dense-AI/pyhealth](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/pyhealth) — Build clinical/healthcare deep-learning pipelines with PyHealth — loading EHR/signal/imaging datasets (MIMIC-III/IV, eI…
- [K-Dense-AI/pylabrobot](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/pylabrobot) — Vendor-agnostic lab automation framework.
- [K-Dense-AI/pymatgen](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/pymatgen) — Materials science toolkit.
- [K-Dense-AI/pymc](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/pymc) — Bayesian modeling with PyMC.
- [K-Dense-AI/pymoo](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/pymoo) — Multi-objective optimization framework.
- [K-Dense-AI/pyopenms](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/pyopenms) — Complete mass spectrometry analysis platform.
- [K-Dense-AI/pysam](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/pysam) — Genomic file toolkit.
- [K-Dense-AI/pytdc](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/pytdc) — Therapeutics Data Commons.
- [K-Dense-AI/pytorch-lightning](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/pytorch-lightning) — Deep learning framework (PyTorch Lightning / lightning package).
- [K-Dense-AI/pyzotero](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/pyzotero) — Interact with Zotero reference management libraries using the pyzotero Python client.
- [K-Dense-AI/qiskit](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/qiskit) — IBM quantum computing framework.
- [K-Dense-AI/qutip](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/qutip) — Quantum physics simulation library for open quantum systems.
- [K-Dense-AI/rdkit](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/rdkit) — Cheminformatics toolkit for fine-grained molecular control.
- [K-Dense-AI/research-grants](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/research-grants) — Write competitive research proposals for NSF, NIH, DOE, DARPA, and Taiwan NSTC.
- [K-Dense-AI/research-lookup](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/research-lookup) — Look up current research information using parallel-cli search (primary, fast web search), the Parallel Chat API (deep…
- [K-Dense-AI/rowan](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/rowan) — Rowan is a cloud-native molecular modeling and medicinal-chemistry workflow platform with a Python API.
- [K-Dense-AI/scanpy](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/scanpy) — Standard single-cell RNA-seq analysis pipeline.
- [K-Dense-AI/scholar-evaluation](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/scholar-evaluation) — Systematically evaluate scholarly work using the ScholarEval framework, providing structured assessment across research…
- [K-Dense-AI/scientific-brainstorming](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/scientific-brainstorming) — Creative research ideation and exploration.
- [K-Dense-AI/scientific-critical-thinking](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/scientific-critical-thinking) — Evaluate scientific claims and evidence quality.
- [K-Dense-AI/scientific-schematics](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/scientific-schematics) — Create publication-quality scientific diagrams using Nano Banana 2 AI with smart iterative refinement.
- [K-Dense-AI/scientific-slides](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/scientific-slides) — Build slide decks and presentations for research talks.
- [K-Dense-AI/venue-templates](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/venue-templates) — Access comprehensive LaTeX templates, formatting requirements, and submission guidelines for major scientific publicati…
- [K-Dense-AI/scientific-visualization](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/scientific-visualization) — Meta-skill for publication-ready figures.
- [K-Dense-AI/scientific-writing](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/scientific-writing) — Core skill for the deep research and writing tool.
- [K-Dense-AI/scikit-bio](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/scikit-bio) — Biological data toolkit.
- [K-Dense-AI/scikit-learn](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/scikit-learn) — Machine learning in Python with scikit-learn.
- [K-Dense-AI/scikit-survival](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/scikit-survival) — Comprehensive toolkit for survival analysis and time-to-event modeling in Python using scikit-survival.
- [K-Dense-AI/scvelo](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/scvelo) — RNA velocity analysis with scVelo.
- [K-Dense-AI/scvi-tools](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/scvi-tools) — Deep generative models for single-cell omics.
- [K-Dense-AI/seaborn](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/seaborn) — Statistical visualization with pandas integration.
- [K-Dense-AI/shap](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/shap) — Model interpretability and explainability using SHAP (SHapley Additive exPlanations).
- [K-Dense-AI/simpy](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/simpy) — Process-based discrete-event simulation framework in Python.
- [K-Dense-AI/stable-baselines3](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/stable-baselines3) — Production-ready reinforcement learning algorithms (PPO, SAC, DQN, TD3, DDPG, A2C) with scikit-learn-like API.
- [K-Dense-AI/statistical-analysis](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/statistical-analysis) — Guided statistical analysis with test selection and reporting.
- [K-Dense-AI/statsmodels](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/statsmodels) — Statistical models library for Python.
- [K-Dense-AI/sympy](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/sympy) — Use when you need exact symbolic math in Python — algebra, calculus, equation solving, symbolic linear algebra, or code…
- [K-Dense-AI/tiledbvcf](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/tiledbvcf) — Efficient storage and retrieval of genomic variant data using TileDB.
- [K-Dense-AI/timesfm-forecasting](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/timesfm-forecasting) — Zero-shot time series forecasting with Google's TimesFM foundation model.
- [K-Dense-AI/torch-geometric](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/torch-geometric) — PyTorch Geometric (PyG) for graph neural networks — node/link/graph classification, message passing (GCN, GAT, GraphSAG…
- [K-Dense-AI/torchdrug](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/torchdrug) — PyTorch-native graph neural networks for molecules and proteins.
- [K-Dense-AI/umap-learn](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/umap-learn) — UMAP dimensionality reduction.
- [K-Dense-AI/usfiscaldata](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/usfiscaldata) — Query the U.S.
- [K-Dense-AI/vaex](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/vaex) — Use this skill for processing and analyzing large tabular datasets (billions of rows) that exceed available RAM.
- [K-Dense-AI/what-if-oracle](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/what-if-oracle) — Run structured What-If scenario analysis with 4–6 branch possibility exploration (best, likely, worst, wild card, contr…
- [K-Dense-AI/docx](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/docx) — Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files).
- [K-Dense-AI/xlsx](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/xlsx) — Create, edit, analyze, or convert Excel spreadsheets (.xlsx, .xlsm) where the workbook file is the primary deliverable.
- [K-Dense-AI/zarr-python](https://github.com/K-Dense-AI/claude-scientific-skills/tree/HEAD/skills/zarr-python) — Chunked N-D arrays for cloud storage (Zarr-Python 3).

</details>

<details open>
<summary><strong>Vercel Labs</strong> &nbsp;·&nbsp; 9 skills &nbsp;·&nbsp; ⭐ 27,842 &nbsp;·&nbsp; official</summary>

- [vercel-labs/deploy-to-vercel](https://github.com/vercel-labs/agent-skills/tree/HEAD/skills/deploy-to-vercel) — Deploy applications and websites to Vercel.
- [vercel-labs/react-best-practices](https://github.com/vercel-labs/agent-skills/tree/HEAD/skills/react-best-practices) — React and Next.js performance optimization guidelines from Vercel Engineering.
- [vercel-labs/composition-patterns](https://github.com/vercel-labs/agent-skills/tree/HEAD/skills/composition-patterns) — React composition patterns that scale.
- [vercel-labs/react-native-skills](https://github.com/vercel-labs/agent-skills/tree/HEAD/skills/react-native-skills) — React Native and Expo best practices for building performant mobile apps.
- [vercel-labs/react-view-transitions](https://github.com/vercel-labs/agent-skills/tree/HEAD/skills/react-view-transitions) — Guide for implementing smooth, native-feeling animations using React's View Transition API (`<ViewTransition>` componen…
- [vercel-labs/vercel-cli-with-tokens](https://github.com/vercel-labs/agent-skills/tree/HEAD/skills/vercel-cli-with-tokens) — Deploy and manage projects on Vercel using token-based authentication.
- [vercel-labs/vercel-optimize](https://github.com/vercel-labs/agent-skills/tree/HEAD/skills/vercel-optimize) — Use for Vercel cost and performance optimization on deployed projects, especially Next.js, SvelteKit, Nuxt, and limited…
- [vercel-labs/web-design-guidelines](https://github.com/vercel-labs/agent-skills/tree/HEAD/skills/web-design-guidelines) — Review UI code for Web Interface Guidelines compliance.
- [vercel-labs/writing-guidelines](https://github.com/vercel-labs/agent-skills/tree/HEAD/skills/writing-guidelines) — Review docs/prose for Writing Guidelines compliance.

</details>

<details open>
<summary><strong>Blader</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 23,869</summary>

- [blader/humanizer](https://github.com/blader/humanizer) — Remove signs of AI-generated writing from text.

</details>

<details open>
<summary><strong>Garrytan</strong> &nbsp;·&nbsp; 51 skills &nbsp;·&nbsp; ⭐ 22,403</summary>

- [garrytan/academic-verify](https://github.com/garrytan/gbrain/tree/HEAD/skills/academic-verify) — Verify a research claim or academic citation by tracing it through publication → methodology → raw data → independent r…
- [garrytan/archive-crawler](https://github.com/garrytan/gbrain/tree/HEAD/skills/archive-crawler) — Universal archivist for personal file archives (Dropbox/B2/Gmail-takeout/local-mount/hard-drive-dump).
- [garrytan/article-enrichment](https://github.com/garrytan/gbrain/tree/HEAD/skills/article-enrichment) — Transform raw article text dumps in the brain into structured pages with executive summary, verbatim quotes, key insigh…
- [garrytan/ask-user](https://github.com/garrytan/gbrain/tree/HEAD/skills/ask-user) — Reusable pattern for presenting the user with explicit choices and gating execution until they respond.
- [garrytan/book-mirror](https://github.com/garrytan/gbrain/tree/HEAD/skills/book-mirror) — Take any book (EPUB/PDF), produce a personalized chapter-by-chapter analysis with two-column tables.
- [garrytan/maintain](https://github.com/garrytan/gbrain/tree/HEAD/skills/maintain) — Brain health checks: back-link enforcement, citation audit, filing validation, stale info detection, orphan pages, and…
- [garrytan/brain-ops](https://github.com/garrytan/gbrain/tree/HEAD/skills/brain-ops) — Brain knowledge base operations.
- [garrytan/enrich](https://github.com/garrytan/gbrain/tree/HEAD/skills/enrich) — Enrich brain pages with tiered enrichment protocol.
- [garrytan/publish](https://github.com/garrytan/gbrain/tree/HEAD/skills/publish) — Share brain pages as beautiful password-protected HTML with zero LLM calls
- [garrytan/brain-pdf](https://github.com/garrytan/gbrain/tree/HEAD/skills/brain-pdf) — Generate a publication-quality PDF from any brain page via the gstack make-pdf binary.
- [garrytan/query](https://github.com/garrytan/gbrain/tree/HEAD/skills/query) — Answer questions using the brain's knowledge with 3-layer search, synthesis, and citation propagation.
- [garrytan/brain-taxonomist](https://github.com/garrytan/gbrain/tree/HEAD/skills/brain-taxonomist) — Filing gate for ALL brain writes.
- [garrytan/capture](https://github.com/garrytan/gbrain/tree/HEAD/skills/capture) — Save any thought or content into the brain via one CLI command.
- [garrytan/citation-fixer](https://github.com/garrytan/gbrain/tree/HEAD/skills/citation-fixer) — Audit and fix citation formatting across brain pages.
- [garrytan/cold-start](https://github.com/garrytan/gbrain/tree/HEAD/skills/cold-start) — Day-one data bootstrapping for a new brain.
- [garrytan/concept-synthesis](https://github.com/garrytan/gbrain/tree/HEAD/skills/concept-synthesis) — Deduplicate and synthesize raw concept stubs into a tiered intellectual map (T1 Canon to T4 Riff), tracing idea evoluti…
- [garrytan/ingest](https://github.com/garrytan/gbrain/tree/HEAD/skills/ingest) — Route content to specialized ingestion skills.
- [garrytan/cron-scheduler](https://github.com/garrytan/gbrain/tree/HEAD/skills/cron-scheduler) — Schedule management with staggering, quiet hours, and wake-up override.
- [garrytan/cross-modal-review](https://github.com/garrytan/gbrain/tree/HEAD/skills/cross-modal-review) — Quality gate via second model.
- [garrytan/briefing](https://github.com/garrytan/gbrain/tree/HEAD/skills/briefing) — Compile daily briefing with meeting context, active deals, and citation tracking
- [garrytan/daily-task-manager](https://github.com/garrytan/gbrain/tree/HEAD/skills/daily-task-manager) — Task lifecycle management.
- [garrytan/daily-task-prep](https://github.com/garrytan/gbrain/tree/HEAD/skills/daily-task-prep) — Morning preparation.
- [garrytan/data-research](https://github.com/garrytan/gbrain/tree/HEAD/skills/data-research) — Structured data research: search sources, extract structured data, archive raw sources, maintain canonical tracker page…
- [garrytan/eiirp](https://github.com/garrytan/gbrain/tree/HEAD/skills/eiirp) — Everything In Its Right Place.
- [garrytan/frontmatter-guard](https://github.com/garrytan/gbrain/tree/HEAD/skills/frontmatter-guard) — Validate and auto-repair YAML frontmatter on brain pages.
- [garrytan/functional-area-resolver](https://github.com/garrytan/gbrain/tree/HEAD/skills/functional-area-resolver) — Compress an agent's routing file (RESOLVER.md or AGENTS.md) by converting granular skill-per-row tables into functional…
- [garrytan/setup](https://github.com/garrytan/gbrain/tree/HEAD/skills/setup) — Set up GBrain with auto-provision Supabase or PGLite, AGENTS.md injection, first import
- [garrytan/gbrain-upgrade](https://github.com/garrytan/gbrain/tree/HEAD/skills/gbrain-upgrade) — Keep gbrain current.
- [garrytan/idea-ingest](https://github.com/garrytan/gbrain/tree/HEAD/skills/idea-ingest) — Ingest links, articles, tweets, and ideas into the brain.
- [garrytan/install](https://github.com/garrytan/gbrain/tree/HEAD/skills/install) — This skill has been replaced by the **setup** skill.
- [garrytan/media-ingest](https://github.com/garrytan/gbrain/tree/HEAD/skills/media-ingest) — Ingest video, audio, PDF, book, screenshot, and GitHub repo content into the brain.
- [garrytan/meeting-ingestion](https://github.com/garrytan/gbrain/tree/HEAD/skills/meeting-ingestion) — Ingest meeting transcripts into brain pages with attendee enrichment, entity propagation, and timeline merge.
- [garrytan/migrate](https://github.com/garrytan/gbrain/tree/HEAD/skills/migrate) — Universal migration from Obsidian, Notion, Logseq, markdown, CSV, JSON, Roam
- [garrytan/minion-orchestrator](https://github.com/garrytan/gbrain/tree/HEAD/skills/minion-orchestrator) — Unified Minions skill for both deterministic shell jobs and LLM subagent orchestration.
- [garrytan/perplexity-research](https://github.com/garrytan/gbrain/tree/HEAD/skills/perplexity-research) — Brain-augmented web research.
- [garrytan/repo-architecture](https://github.com/garrytan/gbrain/tree/HEAD/skills/repo-architecture) — Where new brain files go.
- [garrytan/reports](https://github.com/garrytan/gbrain/tree/HEAD/skills/reports) — Save and load timestamped reports.
- [garrytan/schema-author](https://github.com/garrytan/gbrain/tree/HEAD/skills/schema-author) — Evolve your brain's schema pack.
- [garrytan/schema-unify](https://github.com/garrytan/gbrain/tree/HEAD/skills/schema-unify) — Migrate a brain from gbrain-base (or any pack) to gbrain-base-v2's 14-canonical-type taxonomy via gbrain onboard --chec…
- [garrytan/signal-detector](https://github.com/garrytan/gbrain/tree/HEAD/skills/signal-detector) — Always-on ambient signal capture.
- [garrytan/skill-creator](https://github.com/garrytan/gbrain/tree/HEAD/skills/skill-creator) — Create new skills following the GBrain conformance standard.
- [garrytan/skill-optimizer](https://github.com/garrytan/gbrain/tree/HEAD/skills/skill-optimizer) — Self-evolving skill optimization via SkillOpt-paper-grounded text-space optimizer.
- [garrytan/skillify](https://github.com/garrytan/gbrain/tree/HEAD/skills/skillify) — The meta skill.
- [garrytan/skillpack-check](https://github.com/garrytan/gbrain/tree/HEAD/skills/skillpack-check) — Run `gbrain skillpack-check` to produce an agent-readable JSON health report for the gbrain install.
- [garrytan/skillpack-harvest](https://github.com/garrytan/gbrain/tree/HEAD/skills/skillpack-harvest) — Lift a proven skill from a host repo (e.g.
- [garrytan/smoke-test](https://github.com/garrytan/gbrain/tree/HEAD/skills/smoke-test) — Post-restart smoke tests + auto-fix for gbrain and OpenClaw environments.
- [garrytan/soul-audit](https://github.com/garrytan/gbrain/tree/HEAD/skills/soul-audit) — 6-phase interactive interview that generates the agent's identity (SOUL.md), user profile (USER.md), access control (AC…
- [garrytan/strategic-reading](https://github.com/garrytan/gbrain/tree/HEAD/skills/strategic-reading) — Read a book, article, transcript, or case study through the lens of a specific strategic problem you're facing.
- [garrytan/testing](https://github.com/garrytan/gbrain/tree/HEAD/skills/testing) — Skill validation framework PLUS daily test-suite health and regression intelligence.
- [garrytan/voice-note-ingest](https://github.com/garrytan/gbrain/tree/HEAD/skills/voice-note-ingest) — Ingest a voice note with exact-phrasing preservation (never paraphrased).
- [garrytan/webhook-transforms](https://github.com/garrytan/gbrain/tree/HEAD/skills/webhook-transforms) — Generic framework for converting external events (SMS, meetings, social mentions) into brain-ingestible signals.

</details>

<details>
<summary><strong>Zarazhangrui</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 21,383</summary>

- [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) — Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files.

</details>

<details>
<summary><strong>Hugging Face</strong> &nbsp;·&nbsp; 17 skills &nbsp;·&nbsp; ⭐ 10,656 &nbsp;·&nbsp; official</summary>

- [huggingface/hf-cli](https://github.com/huggingface/skills/tree/HEAD/skills/hf-cli) — Hugging Face Hub CLI (`hf`) for downloading, uploading, and managing models, datasets, spaces, buckets, repos, papers,…
- [huggingface/hf-mcp](https://github.com/huggingface/skills/tree/HEAD/hf-mcp/skills/hf-mcp) — Use Hugging Face Hub via MCP server tools.
- [huggingface/huggingface-community-evals](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-community-evals) — Run evaluations for Hugging Face Hub models using inspect-ai and lighteval on local hardware.
- [huggingface/huggingface-datasets](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-datasets) — Use this skill for Hugging Face Dataset Viewer API workflows that fetch subset/split metadata, paginate rows, search te…
- [huggingface/huggingface-gradio](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-gradio) — Build Gradio web UIs and demos in Python.
- [huggingface/huggingface-llm-trainer](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-llm-trainer) — Train or fine-tune language and vision models using TRL (Transformer Reinforcement Learning) or Unsloth with Hugging Fa…
- [huggingface/huggingface-local-models](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-local-models) — Use to select models to run locally with llama.cpp and GGUF on CPU, Mac Metal, CUDA, or ROCm.
- [huggingface/huggingface-best](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-best) — Use when the user asks about finding the best, top, or recommended model for a task, wants to know what AI model to use…
- [huggingface/huggingface-paper-publisher](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-paper-publisher) — Publish and manage research papers on Hugging Face Hub.
- [huggingface/huggingface-papers](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-papers) — Look up and read Hugging Face paper pages in markdown, and use the papers API for structured metadata such as authors,…
- [huggingface/huggingface-spaces](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-spaces) — Build, deploy, and maintain applications on Hugging Face Spaces — Gradio / Docker / Static SDKs, ZeroGPU and dedicated…
- [huggingface/huggingface-tool-builder](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-tool-builder) — Use this skill when the user wants to build tool/scripts or achieve a task where using data from the Hugging Face API w…
- [huggingface/huggingface-trackio](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-trackio) — Track and visualize ML training experiments with Trackio.
- [huggingface/huggingface-vision-trainer](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-vision-trainer) — Trains and fine-tunes vision models for object detection (D-FINE, RT-DETR v2, DETR, YOLOS), image classification (timm…
- [huggingface/huggingface-zerogpu](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-zerogpu) — AI demos and GPU compute with Gradio Spaces and Hugging Face Spaces ZeroGPU.
- [huggingface/train-sentence-transformers](https://github.com/huggingface/skills/tree/HEAD/skills/train-sentence-transformers) — Train or fine-tune sentence-transformers models across `SentenceTransformer` (bi-encoder; dense or static embedding mod…
- [huggingface/transformers-js](https://github.com/huggingface/skills/tree/HEAD/skills/transformers-js) — Use Transformers.js to run state-of-the-art machine learning models directly in JavaScript/TypeScript.

</details>

<details>
<summary><strong>Kreuzberg Dev</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 8,483 &nbsp;·&nbsp; official</summary>

- [kreuzberg-dev/kreuzberg](https://github.com/kreuzberg-dev/kreuzberg/tree/HEAD/skills/kreuzberg) — Extract text, tables, metadata, and images from 91+ document formats (PDF, Office, images, HTML, email, archives, acade…

</details>

<details>
<summary><strong>PleasePrompto</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 6,999</summary>

- [PleasePrompto/notebooklm-skill](https://github.com/PleasePrompto/notebooklm-skill) — Use this skill to query your Google NotebookLM notebooks directly from Claude Code for source-grounded, citation-backed…

</details>

<details>
<summary><strong>Czlonkowski</strong> &nbsp;·&nbsp; 7 skills &nbsp;·&nbsp; ⭐ 5,393</summary>

- [czlonkowski/n8n-expression-syntax](https://github.com/czlonkowski/n8n-skills/tree/HEAD/skills/n8n-expression-syntax) — Validate n8n expression syntax and fix common errors.
- [czlonkowski/n8n-code-javascript](https://github.com/czlonkowski/n8n-skills/tree/HEAD/skills/n8n-code-javascript) — Write JavaScript code in n8n Code nodes.
- [czlonkowski/n8n-mcp-tools-expert](https://github.com/czlonkowski/n8n-skills/tree/HEAD/skills/n8n-mcp-tools-expert) — Expert guide for using n8n-mcp MCP tools effectively.
- [czlonkowski/n8n-node-configuration](https://github.com/czlonkowski/n8n-skills/tree/HEAD/skills/n8n-node-configuration) — Operation-aware node configuration guidance.
- [czlonkowski/n8n-code-python](https://github.com/czlonkowski/n8n-skills/tree/HEAD/skills/n8n-code-python) — Write Python code in n8n Code nodes.
- [czlonkowski/n8n-validation-expert](https://github.com/czlonkowski/n8n-skills/tree/HEAD/skills/n8n-validation-expert) — Interpret validation errors and guide fixing them.
- [czlonkowski/n8n-workflow-patterns](https://github.com/czlonkowski/n8n-skills/tree/HEAD/skills/n8n-workflow-patterns) — Proven workflow architectural patterns from real n8n workflows.

</details>

<details>
<summary><strong>Deanpeters</strong> &nbsp;·&nbsp; 49 skills &nbsp;·&nbsp; ⭐ 5,080</summary>

- [deanpeters/acquisition-channel-advisor](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/acquisition-channel-advisor) — Evaluate acquisition channels using unit economics, customer quality, and scalability.
- [deanpeters/ai-shaped-readiness-advisor](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/ai-shaped-readiness-advisor) — Assess whether your product work is AI-first or AI-shaped.
- [deanpeters/altitude-horizon-framework](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/altitude-horizon-framework) — Understand the PM-to-Director transition through altitude and horizon thinking.
- [deanpeters/business-health-diagnostic](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/business-health-diagnostic) — Diagnose SaaS business health across growth, retention, efficiency, and capital.
- [deanpeters/company-research](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/company-research) — Create a company research brief with executive quotes, product strategy, and org context.
- [deanpeters/context-engineering-advisor](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/context-engineering-advisor) — Diagnose context stuffing vs.
- [deanpeters/customer-journey-map](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/customer-journey-map) — Create a customer journey map across stages, touchpoints, actions, emotions, and metrics.
- [deanpeters/customer-journey-mapping-workshop](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/customer-journey-mapping-workshop) — Run a customer journey mapping workshop with adaptive questions and outputs.
- [deanpeters/director-readiness-advisor](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/director-readiness-advisor) — Guide the PM-to-Director transition across preparing, interviewing, landing, and recalibrating.
- [deanpeters/discovery-interview-prep](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/discovery-interview-prep) — Plan customer discovery interviews with the right goal, segment, constraints, and method.
- [deanpeters/discovery-process](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/discovery-process) — Run a full discovery cycle from problem hypothesis to validated solution.
- [deanpeters/eol-message](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/eol-message) — Write a clear, empathetic EOL announcement with rationale, customer impact, and next steps.
- [deanpeters/epic-breakdown-advisor](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/epic-breakdown-advisor) — Break down epics into user stories with Humanizing Work split patterns.
- [deanpeters/epic-hypothesis](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/epic-hypothesis) — Frame an epic as a testable hypothesis with target user, expected outcome, and validation method.
- [deanpeters/executive-onboarding-playbook](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/executive-onboarding-playbook) — Plan a VP or CPO 30-60-90 day diagnostic onboarding path.
- [deanpeters/feature-investment-advisor](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/feature-investment-advisor) — Evaluate feature investments using revenue impact, cost structure, ROI, and strategy.
- [deanpeters/finance-metrics-quickref](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/finance-metrics-quickref) — Look up SaaS finance metrics, formulas, and benchmarks fast.
- [deanpeters/finance-based-pricing-advisor](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/finance-based-pricing-advisor) — Evaluate pricing changes using ARPU, conversion, churn risk, NRR, and payback.
- [deanpeters/jobs-to-be-done](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/jobs-to-be-done) — Uncover customer jobs, pains, and gains in a structured JTBD format.
- [deanpeters/lean-ux-canvas](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/lean-ux-canvas) — Guide teams through Lean UX Canvas v2.
- [deanpeters/opportunity-solution-tree](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/opportunity-solution-tree) — Build an Opportunity Solution Tree from outcomes to opportunities, solutions, and tests.
- [deanpeters/organic-growth-advisor](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/organic-growth-advisor) — Identify which organic growth path to pursue — new segments, geographies, channels, or products.
- [deanpeters/pestel-analysis](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/pestel-analysis) — Analyze political, economic, social, technological, environmental, and legal forces.
- [deanpeters/pm-skill-creator](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/pm-skill-creator) — Design a new PM skill through guided conversation.
- [deanpeters/pol-probe](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/pol-probe) — Define a Proof of Life probe to test a risky hypothesis cheaply.
- [deanpeters/pol-probe-advisor](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/pol-probe-advisor) — Select the right Proof of Life (PoL) probe based on hypothesis, risk, and resources.
- [deanpeters/positioning-statement](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/positioning-statement) — Create a Geoffrey Moore-style positioning statement.
- [deanpeters/positioning-workshop](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/positioning-workshop) — Run a positioning workshop that surfaces target customer, unmet need, category, benefits, and differentiation.
- [deanpeters/prd-development](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/prd-development) — Build a structured PRD that connects problem, users, solution, and success criteria.
- [deanpeters/press-release](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/press-release) — Write an Amazon-style press release that defines customer value before building.
- [deanpeters/prioritization-advisor](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/prioritization-advisor) — Choose a prioritization framework based on stage, team context, and stakeholder needs.
- [deanpeters/problem-framing-canvas](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/problem-framing-canvas) — Guide teams through MITRE's Problem Framing Canvas.
- [deanpeters/problem-statement](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/problem-statement) — Write a user-centered problem statement with who is blocked, what they are trying to do, why it matters, and how it fee…
- [deanpeters/product-sense-interview-answer](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/product-sense-interview-answer) — Structure a spoken PM product-sense answer with assumptions, segmentation, pain-point prioritization, and MVP tradeoffs.
- [deanpeters/product-strategy-session](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/product-strategy-session) — Run an end-to-end product strategy session across positioning, discovery, and roadmap planning.
- [deanpeters/proto-persona](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/proto-persona) — Create a proto-persona from current research, market signals, and team knowledge.
- [deanpeters/recommendation-canvas](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/recommendation-canvas) — Evaluate an AI product idea across outcomes, hypotheses, risks, and positioning.
- [deanpeters/roadmap-planning](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/roadmap-planning) — Plan a strategic roadmap across prioritization, epic definition, stakeholder alignment, and sequencing.
- [deanpeters/saas-economics-efficiency-metrics](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/saas-economics-efficiency-metrics) — Evaluate SaaS unit economics and capital efficiency.
- [deanpeters/saas-revenue-growth-metrics](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/saas-revenue-growth-metrics) — Calculate SaaS revenue, retention, and growth metrics.
- [deanpeters/skill-authoring-workflow](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/skill-authoring-workflow) — Turn raw PM content into a compliant, publish-ready skill.
- [deanpeters/storyboard](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/storyboard) — Create a six-frame storyboard that shows a user's journey from problem to solution.
- [deanpeters/tam-sam-som-calculator](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/tam-sam-som-calculator) — Calculate TAM, SAM, and SOM with explicit assumptions, methods, and caveats.
- [deanpeters/user-story](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/user-story) — Create user stories with Mike Cohn format and Gherkin acceptance criteria.
- [deanpeters/user-story-mapping](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/user-story-mapping) — Create a user story map that lays out activities, steps, tasks, and release slices.
- [deanpeters/user-story-mapping-workshop](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/user-story-mapping-workshop) — Run a user story mapping workshop with adaptive questions and a structured map output.
- [deanpeters/user-story-splitting](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/user-story-splitting) — Break a large story or epic into smaller deliverable stories using proven split patterns.
- [deanpeters/vp-cpo-readiness-advisor](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/vp-cpo-readiness-advisor) — Guide the transition to VP or CPO across preparing, interviewing, landing, and recalibrating.
- [deanpeters/workshop-facilitation](https://github.com/deanpeters/Product-Manager-Skills/tree/HEAD/skills/workshop-facilitation) — Facilitate workshop sessions in a one-step, multi-turn flow.

</details>

<details>
<summary><strong>Tech Leads Club</strong> &nbsp;·&nbsp; 80 skills &nbsp;·&nbsp; ⭐ 4,578</summary>

- [tech-leads-club/ai-cold-outreach](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(gtm)/ai-cold-outreach) — When the user wants to build an AI-powered outreach system, write cold emails, improve deliverability, or scale persona…
- [tech-leads-club/ai-pricing](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(gtm)/ai-pricing) — When the user wants to price an AI product, choose a charge metric, design pricing tiers, or optimize margins.
- [tech-leads-club/ai-sdr](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(gtm)/ai-sdr) — When the user wants to deploy AI sales development reps, automate sales qualification, build signal-to-action routing,…
- [tech-leads-club/ai-ugc-ads](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(gtm)/ai-ugc-ads) — When the user wants to create UGC ad campaigns, recruit UGC creators, generate AI UGC content, or scale with user-gener…
- [tech-leads-club/ai-seo](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(gtm)/ai-seo) — When the user wants to build programmatic SEO with AI, create competitor alternative pages, optimize for AI Overviews,…
- [tech-leads-club/perf-astro](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(performance)/perf-astro) — Astro-specific performance optimizations for 95+ Lighthouse scores.
- [tech-leads-club/aws-advisor](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(cloud)/aws-advisor) — Expert AWS Cloud Advisor for architecture design, security review, and implementation guidance.
- [tech-leads-club/chrome-devtools](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(tooling)/chrome-devtools) — Browser debugging, performance profiling, and automation via Chrome DevTools MCP.
- [tech-leads-club/cloudflare-deploy](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(cloud)/cloudflare-deploy) — Deploy applications and infrastructure to Cloudflare using Workers, Pages, and related platform services.
- [tech-leads-club/codenavi](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(development)/codenavi) — Your pathfinder for navigating unknown codebases.
- [tech-leads-club/coding-guidelines](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(development)/coding-guidelines) — Behavioral guidelines to reduce common LLM coding mistakes.
- [tech-leads-club/component-common-domain-detection](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(architecture)/component-common-domain-detection) — Finds duplicate business logic spread across multiple components and suggests consolidation.
- [tech-leads-club/component-flattening-analysis](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(architecture)/component-flattening-analysis) — Detects misplaced classes and fixes component hierarchy problems — finds code that should belong inside a component but…
- [tech-leads-club/component-identification-sizing](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(architecture)/component-identification-sizing) — Maps architectural components in a codebase and measures their size to identify what should be extracted first.
- [tech-leads-club/confluence-assistant](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(development)/confluence-assistant) — Expert in Confluence operations using Atlassian MCP.
- [tech-leads-club/content-to-pipeline](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(gtm)/content-to-pipeline) — When the user wants to turn content into revenue, build a content-led GTM motion, reverse engineer distribution, or rep…
- [tech-leads-club/core-web-vitals](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(performance)/core-web-vitals) — Optimize Core Web Vitals (LCP, INP, CLS) for better page experience and search ranking.
- [tech-leads-club/coupling-analysis](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(architecture)/coupling-analysis) — Analyzes coupling between modules using the three-dimensional model (strength, distance, volatility) from "Balancing Co…
- [tech-leads-club/create-adr](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(creation)/create-adr) — Creates Architecture Decision Records (ADRs) to document significant architectural choices and their rationale for futu…
- [tech-leads-club/create-rfc](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(creation)/create-rfc) — Creates structured Request for Comments (RFC) documents for proposing and deciding on significant changes.
- [tech-leads-club/create-technical-design-doc](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(creation)/create-technical-design-doc) — Creates comprehensive Technical Design Documents (TDD) with mandatory and optional sections through interactive discove…
- [tech-leads-club/cursor-subagent-creator](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(creation)/cursor-subagent-creator) — Creates Cursor-specific AI subagents with isolated context for complex multi-step workflows.
- [tech-leads-club/decomposition-planning-roadmap](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(architecture)/decomposition-planning-roadmap) — Creates step-by-step decomposition plans and migration roadmaps for breaking apart monolithic applications.
- [tech-leads-club/docs-writer](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(development)/docs-writer) — Write, review, and edit documentation files with consistent structure, tone, and technical accuracy.
- [tech-leads-club/domain-analysis](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(architecture)/domain-analysis) — Maps business domains and suggests service boundaries in any codebase using DDD Strategic Design.
- [tech-leads-club/domain-identification-grouping](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(architecture)/domain-identification-grouping) — Groups existing components into logical business domains to plan service-based architecture.
- [tech-leads-club/excalidraw-studio](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(tooling)/excalidraw-studio) — Generate Excalidraw diagrams from natural language descriptions.
- [tech-leads-club/expansion-retention](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(gtm)/expansion-retention) — When the user wants to reduce churn, build expansion revenue, automate customer success, or optimize net revenue retent…
- [tech-leads-club/figma](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(design)/figma) — Use the Figma MCP server to fetch design context, screenshots, variables, and assets from Figma, and to translate Figma…
- [tech-leads-club/figma-implement-design](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(design)/figma-implement-design) — Translate Figma nodes into production-ready code with 1:1 visual fidelity using the Figma MCP workflow (design context,…
- [tech-leads-club/frontend-blueprint](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(architecture)/frontend-blueprint) — AI frontend specialist and design consultant that guides users through a structured discovery process before generating…
- [tech-leads-club/frontend-design](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(design)/frontend-design) — Create distinctive, production-grade frontend interfaces with high design quality.
- [tech-leads-club/gh-address-comments](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(development)/gh-address-comments) — Address review and issue comments on the open GitHub PR for the current branch using gh CLI.
- [tech-leads-club/gh-fix-ci](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(tooling)/gh-fix-ci) — Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions.
- [tech-leads-club/gtm-engineering](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(gtm)/gtm-engineering) — When the user wants to build GTM automation with code, design workflow architectures, use AI agents for GTM tasks, or i…
- [tech-leads-club/gtm-metrics](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(gtm)/gtm-metrics) — When the user wants to define GTM metrics, build a metrics dashboard, measure pipeline efficiency, or track AI product…
- [tech-leads-club/jira-assistant](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(development)/jira-assistant) — Manage Jira issues via Atlassian MCP — search, create, update, transition status, and handle sprint tasks.
- [tech-leads-club/lead-enrichment](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(gtm)/lead-enrichment) — When the user wants to build data enrichment workflows, score leads against ICP, set up Clay waterfalls, or improve con…
- [tech-leads-club/learning-opportunities](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(learning)/learning-opportunities) — Facilitates deliberate skill development during AI-assisted coding.
- [tech-leads-club/legacy-migration-planner](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(architecture)/legacy-migration-planner) — Use when planning legacy system migrations, codebase modernization, monolith decomposition, microservices consolidation…
- [tech-leads-club/perf-lighthouse](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(performance)/perf-lighthouse) — Run Lighthouse audits locally via CLI or Node API, parse and interpret reports, and set performance budgets.
- [tech-leads-club/mermaid-studio](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(tooling)/mermaid-studio) — Expert Mermaid diagram creation, validation, and rendering with dual-engine output (SVG/PNG/ASCII).
- [tech-leads-club/modular-decomposition](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(architecture)/modular-decomposition) — Runs a sequenced monolith-to-modular pipeline that sizes and inventories components, finds shared domain duplication, a…
- [tech-leads-club/modular-design-principles](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(architecture)/modular-design-principles) — Technology-agnostic guidance for modular systems: bounded contexts, clear boundaries, composability, state isolation, e…
- [tech-leads-club/multi-platform-launch](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(gtm)/multi-platform-launch) — When the user wants to launch a product across multiple platforms, plan a Product Hunt launch, build a waitlist, or exe…
- [tech-leads-club/nestjs-modular-monolith](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(development)/nestjs-modular-monolith) — Specialist in designing and implementing scalable modular monolith architectures using NestJS with DDD, Clean Architect…
- [tech-leads-club/netlify-deploy](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(cloud)/netlify-deploy) — Deploy web projects to Netlify using the Netlify CLI (`npx netlify`).
- [tech-leads-club/nx-ci-monitor](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(tooling)/nx-ci-monitor) — Monitor Nx Cloud CI pipeline status and handle self-healing fixes automatically.
- [tech-leads-club/nx-generate](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(tooling)/nx-generate) — Generate code using Nx generators — scaffold projects, libraries, features, or run workspace-specific generators with p…
- [tech-leads-club/nx-run-tasks](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(tooling)/nx-run-tasks) — Execute build, test, lint, serve, and other tasks in an Nx workspace using single runs, run-many, and affected commands.
- [tech-leads-club/nx-workspace](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(tooling)/nx-workspace) — Configure, explore, and optimize Nx monorepo workspaces.
- [tech-leads-club/paid-creative-ai](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(gtm)/paid-creative-ai) — When the user wants to create AI-generated ad creative, test performance creative, manage creative fatigue, or optimize…
- [tech-leads-club/partner-affiliate](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(gtm)/partner-affiliate) — When the user wants to build a partner program, launch an affiliate program, design integration partnerships, or create…
- [tech-leads-club/playwright-skill](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(web-automation)/playwright-skill) — Complete browser automation with Playwright.
- [tech-leads-club/positioning-icp](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(gtm)/positioning-icp) — When the user wants to define their ideal customer profile, position an AI product, build messaging architecture, or va…
- [tech-leads-club/react-best-practices](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(quality)/react-best-practices) — React and Next.js performance optimization guidelines from Vercel Engineering.
- [tech-leads-club/react-composition-patterns](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(architecture)/react-composition-patterns) — React composition patterns that scale.
- [tech-leads-club/react-native-expert](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(development)/react-native-expert) — Senior React Native and Expo engineer for building production-ready cross-platform mobile apps.
- [tech-leads-club/render-deploy](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(cloud)/render-deploy) — Deploy applications to Render by analyzing codebases, generating render.yaml Blueprints, and providing Dashboard deepli…
- [tech-leads-club/sales-motion-design](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(gtm)/sales-motion-design) — When the user wants to choose between PLG and sales-led, design a sales motion, optimize time-to-first-value, or build…
- [tech-leads-club/security-best-practices](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(security)/security-best-practices) — Perform language and framework specific security best-practice reviews and suggest improvements.
- [tech-leads-club/security-ownership-map](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(security)/security-ownership-map) — Analyze git repositories to build a security ownership topology (people-to-file), compute bus factor and sensitive-code…
- [tech-leads-club/security-threat-model](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(security)/security-threat-model) — Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities, abuse paths, and m…
- [tech-leads-club/sentry](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(monitoring)/sentry) — Inspect Sentry issues, summarize production errors, and pull health data via the Sentry API (read-only).
- [tech-leads-club/seo](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(quality)/seo) — Optimize for search engine visibility and ranking.
- [tech-leads-club/shopify-developer](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(development)/shopify-developer) — Complete Shopify development reference covering Liquid templating, OS 2.0 themes, GraphQL APIs, Hydrogen, Functions, an…
- [tech-leads-club/skill-architect](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(creation)/skill-architect) — Expert guide for designing and building high-quality skills from scratch through structured conversation.
- [tech-leads-club/social-selling](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(gtm)/social-selling) — When the user wants to sell through social media, optimize LinkedIn for sales, build DM sequences, or convert content e…
- [tech-leads-club/solo-founder-gtm](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(gtm)/solo-founder-gtm) — When the user is a solo founder building their GTM motion, wants to scale without hiring, or needs to design an AI agen…
- [tech-leads-club/tlc-spec-driven](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(development)/tlc-spec-driven) — Project and feature planning with 4 adaptive phases - Specify, Design, Tasks, Execute.
- [tech-leads-club/subagent-creator](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(creation)/subagent-creator) — Guide for creating AI subagents with isolated context for complex multi-step workflows.
- [tech-leads-club/tactical-ddd](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(architecture)/tactical-ddd) — Detects anemic domain models, validates and refactors them into rich domain models, and enforces tactical DDD patterns…
- [tech-leads-club/the-fool](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(decision-making)/the-fool) — Use when challenging ideas, plans, decisions, or proposals.
- [tech-leads-club/vercel-deploy](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(cloud)/vercel-deploy) — Deploy applications and websites to Vercel.
- [tech-leads-club/video-outreach](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(gtm)/video-outreach) — When the user wants to build video-first cold outreach, create personalized video at scale, implement async selling, or…
- [tech-leads-club/web-accessibility](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(quality)/web-accessibility) — Audit and improve web accessibility following WCAG 2.1 guidelines.
- [tech-leads-club/web-best-practices](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(quality)/web-best-practices) — Apply modern web development best practices for security, compatibility, and code quality.
- [tech-leads-club/web-design-guidelines](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(design)/web-design-guidelines) — Review UI code for Web Interface Guidelines compliance.
- [tech-leads-club/perf-web-optimization](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(performance)/perf-web-optimization) — Optimize web performance: bundle size, images, caching, lazy loading, and overall page speed.
- [tech-leads-club/web-quality-audit](https://github.com/tech-leads-club/agent-skills/tree/HEAD/packages/skills-catalog/skills/(quality)/web-quality-audit) — Comprehensive web quality audit covering performance, accessibility, SEO, and best practices in a single review.

</details>

<details>
<summary><strong>Op7418</strong> &nbsp;·&nbsp; 2 skills &nbsp;·&nbsp; ⭐ 2,964</summary>

- [op7418/NanoBanana-PPT-Skills](https://github.com/op7418/NanoBanana-PPT-Skills) — - **Skill 名称**: ppt-generator-pro
- [op7418/Youtube-clipper-skill](https://github.com/op7418/Youtube-clipper-skill) — YouTube 视频智能剪辑工具。下载视频和字幕，AI 分析生成精细章节（几分钟级别）， 用户选择片段后自动剪辑、翻译字幕为中英双语、烧录字幕到视频，并生成总结文案。 使用场景：当用户需要剪辑 YouTube 视频、生成短视频片段、制作双…

</details>

<details>
<summary><strong>Lackeyjb</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 2,758</summary>

- [lackeyjb/playwright-skill](https://github.com/lackeyjb/playwright-skill/tree/HEAD/skills/playwright-skill) — Complete browser automation with Playwright.

</details>

<details>
<summary><strong>Ibelick</strong> &nbsp;·&nbsp; 4 skills &nbsp;·&nbsp; ⭐ 2,696</summary>

- [ibelick/baseline-ui](https://github.com/ibelick/ui-skills/tree/HEAD/skills/baseline-ui) — Validates animation durations, enforces typography scale, checks component accessibility, and prevents layout anti-patt…
- [ibelick/fixing-accessibility](https://github.com/ibelick/ui-skills/tree/HEAD/skills/fixing-accessibility) — Audit and fix HTML accessibility issues including ARIA labels, keyboard navigation, focus management, color contrast, a…
- [ibelick/fixing-metadata](https://github.com/ibelick/ui-skills/tree/HEAD/skills/fixing-metadata) — Audit and fix HTML metadata including page titles, meta descriptions, canonical URLs, Open Graph tags, Twitter cards, f…
- [ibelick/fixing-motion-performance](https://github.com/ibelick/ui-skills/tree/HEAD/skills/fixing-motion-performance) — Audit and fix animation performance issues including layout thrashing, compositor properties, scroll-linked motion, and…

</details>

<details>
<summary><strong>CloudAI X</strong> &nbsp;·&nbsp; 10 skills &nbsp;·&nbsp; ⭐ 2,385</summary>

- [CloudAI-X/threejs-animation](https://github.com/CloudAI-X/threejs-skills/tree/HEAD/skills/threejs-animation) — Three.js animation - keyframe animation, skeletal animation, morph targets, animation mixing.
- [CloudAI-X/threejs-fundamentals](https://github.com/CloudAI-X/threejs-skills/tree/HEAD/skills/threejs-fundamentals) — Three.js scene setup, cameras, renderer, Object3D hierarchy, coordinate systems.
- [CloudAI-X/threejs-geometry](https://github.com/CloudAI-X/threejs-skills/tree/HEAD/skills/threejs-geometry) — Three.js geometry creation - built-in shapes, BufferGeometry, custom geometry, instancing.
- [CloudAI-X/threejs-interaction](https://github.com/CloudAI-X/threejs-skills/tree/HEAD/skills/threejs-interaction) — Three.js interaction - raycasting, controls, mouse/touch input, object selection.
- [CloudAI-X/threejs-lighting](https://github.com/CloudAI-X/threejs-skills/tree/HEAD/skills/threejs-lighting) — Three.js lighting - light types, shadows, environment lighting.
- [CloudAI-X/threejs-loaders](https://github.com/CloudAI-X/threejs-skills/tree/HEAD/skills/threejs-loaders) — Three.js asset loading - GLTF, textures, images, models, async patterns.
- [CloudAI-X/threejs-materials](https://github.com/CloudAI-X/threejs-skills/tree/HEAD/skills/threejs-materials) — Three.js materials - PBR, basic, phong, shader materials, material properties.
- [CloudAI-X/threejs-postprocessing](https://github.com/CloudAI-X/threejs-skills/tree/HEAD/skills/threejs-postprocessing) — Three.js post-processing - EffectComposer, bloom, DOF, screen effects.
- [CloudAI-X/threejs-shaders](https://github.com/CloudAI-X/threejs-skills/tree/HEAD/skills/threejs-shaders) — Three.js shaders - GLSL, ShaderMaterial, uniforms, custom effects.
- [CloudAI-X/threejs-textures](https://github.com/CloudAI-X/threejs-skills/tree/HEAD/skills/threejs-textures) — Three.js textures - texture types, UV mapping, environment maps, texture settings.

</details>

<details>
<summary><strong>Foryourhealth111 Pixel</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 2,279</summary>

- [foryourhealth111-pixel/Vibe-Skills](https://github.com/foryourhealth111-pixel/Vibe-Skills) — Vibe Code Orchestrator (VCO) is a governed runtime entry that freezes requirements, plans XL-first execution, and enfor…

</details>

<details>
<summary><strong>Supabase</strong> &nbsp;·&nbsp; 2 skills &nbsp;·&nbsp; ⭐ 2,231 &nbsp;·&nbsp; official</summary>

- [supabase/supabase](https://github.com/supabase/agent-skills/tree/HEAD/skills/supabase) — Use when doing ANY task involving Supabase.
- [supabase/supabase-postgres-best-practices](https://github.com/supabase/agent-skills/tree/HEAD/skills/supabase-postgres-best-practices) — Postgres performance optimization and best practices from Supabase.

</details>

<details>
<summary><strong>Mcollina</strong> &nbsp;·&nbsp; 11 skills &nbsp;·&nbsp; ⭐ 1,835</summary>

- [mcollina/documentation](https://github.com/mcollina/skills/tree/HEAD/skills/documentation) — Creates, structures, and reviews technical documentation following the Diátaxis framework (tutorials, how-to guides, re…
- [mcollina/fastify](https://github.com/mcollina/skills/tree/HEAD/skills/fastify) — Guides development of Fastify Node.js backend servers and REST APIs using TypeScript or JavaScript.
- [mcollina/init](https://github.com/mcollina/skills/tree/HEAD/skills/init) — Creates, updates, or optimizes an AGENTS.md file for a repository with minimal, high-signal instructions covering non-d…
- [mcollina/linting-neostandard-eslint9](https://github.com/mcollina/skills/tree/HEAD/skills/linting-neostandard-eslint9) — Configures ESLint v9 flat config and neostandard for JavaScript and TypeScript projects, including migrating from legac…
- [mcollina/nodejs-core](https://github.com/mcollina/skills/tree/HEAD/skills/nodejs-core) — Debugs native module crashes, optimizes V8 performance, configures node-gyp builds, writes N-API/node-addon-api binding…
- [mcollina/node](https://github.com/mcollina/skills/tree/HEAD/skills/node) — Provides domain-specific best practices for Node.js development with TypeScript, covering type stripping, async pattern…
- [mcollina/oauth](https://github.com/mcollina/skills/tree/HEAD/skills/oauth) — Implements OAuth 2.0/2.1 authorization flows in Fastify applications — configures authorization code with PKCE, client…
- [mcollina/octocat](https://github.com/mcollina/skills/tree/HEAD/skills/octocat) — Use this skill whenever the prompt contains any `github.com` URL, even if the user only pastes a link and gives no GitH…
- [mcollina/skill-optimizer](https://github.com/mcollina/skills/tree/HEAD/skills/skill-optimizer) — Optimizes AI skills for activation, clarity, and cross-model reliability.
- [mcollina/snipgrapher](https://github.com/mcollina/skills/tree/HEAD/skills/snipgrapher) — Configures and uses snipgrapher to generate polished code snippet images, including syntax-highlighted PNGs, SVGs, and…
- [mcollina/typescript-magician](https://github.com/mcollina/skills/tree/HEAD/skills/typescript-magician) — Designs complex generic types, refactors `any` types to strict alternatives, creates type guards and utility types, and…

</details>

<details>
<summary><strong>Cloudflare</strong> &nbsp;·&nbsp; 9 skills &nbsp;·&nbsp; ⭐ 1,759 &nbsp;·&nbsp; official</summary>

- [cloudflare/agents-sdk](https://github.com/cloudflare/skills/tree/HEAD/skills/agents-sdk) — Build AI agents on Cloudflare Workers using the Agents SDK.
- [cloudflare/durable-objects](https://github.com/cloudflare/skills/tree/HEAD/skills/durable-objects) — Create and review Cloudflare Durable Objects.
- [cloudflare/cloudflare-email-service](https://github.com/cloudflare/skills/tree/HEAD/skills/cloudflare-email-service) — Send and receive transactional emails with Cloudflare Email Service (Email Sending + Email Routing).
- [cloudflare/cloudflare](https://github.com/cloudflare/skills/tree/HEAD/skills/cloudflare) — Comprehensive Cloudflare platform skill covering Workers, Pages, storage (KV, D1, R2), AI (Workers AI, Vectorize, Agent…
- [cloudflare/turnstile-spin](https://github.com/cloudflare/skills/tree/HEAD/skills/turnstile-spin) — Set up Cloudflare Turnstile end-to-end in a project — scan the codebase, create the widget via the Cloudflare API, depl…
- [cloudflare/sandbox-sdk](https://github.com/cloudflare/skills/tree/HEAD/skills/sandbox-sdk) — Build sandboxed applications for secure code execution.
- [cloudflare/web-perf](https://github.com/cloudflare/skills/tree/HEAD/skills/web-perf) — Analyzes web performance using Chrome DevTools MCP.
- [cloudflare/workers-best-practices](https://github.com/cloudflare/skills/tree/HEAD/skills/workers-best-practices) — Reviews and authors Cloudflare Workers code against production best practices.
- [cloudflare/wrangler](https://github.com/cloudflare/skills/tree/HEAD/skills/wrangler) — Cloudflare Workers CLI for deploying, developing, and managing Workers, KV, R2, D1, Vectorize, Hyperdrive, Workers AI,…

</details>

<details>
<summary><strong>Stripe</strong> &nbsp;·&nbsp; 3 skills &nbsp;·&nbsp; ⭐ 1,603 &nbsp;·&nbsp; official</summary>

- [stripe/stripe-best-practices](https://github.com/stripe/ai/tree/HEAD/skills/stripe-best-practices) — Guides Stripe integration decisions — API selection (Checkout Sessions vs PaymentIntents), Connect platform setup (Acco…
- [stripe/stripe-projects](https://github.com/stripe/ai/tree/HEAD/skills/stripe-projects) — Use when the user wants to provision infrastructure or third-party services using Stripe Projects.
- [stripe/upgrade-stripe](https://github.com/stripe/ai/tree/HEAD/skills/upgrade-stripe) — Guide for upgrading Stripe API versions and SDKs

</details>

<details>
<summary><strong>Eronred</strong> &nbsp;·&nbsp; 40 skills &nbsp;·&nbsp; ⭐ 1,482</summary>

- [Eronred/ab-test-store-listing](https://github.com/Eronred/aso-skills/tree/HEAD/skills/ab-test-store-listing) — When the user wants to A/B test App Store product page elements to improve conversion rate.
- [Eronred/android-aso](https://github.com/Eronred/aso-skills/tree/HEAD/skills/android-aso) — When the user wants to optimize their Google Play Store listing — title, short description, full description, keywords,…
- [Eronred/app-analytics](https://github.com/Eronred/aso-skills/tree/HEAD/skills/app-analytics) — When the user wants to set up, interpret, or improve their app analytics and tracking.
- [Eronred/app-clips](https://github.com/Eronred/aso-skills/tree/HEAD/skills/app-clips) — When the user wants to implement, optimize, or use App Clips for app discovery and conversion.
- [Eronred/app-icon-optimization](https://github.com/Eronred/aso-skills/tree/HEAD/skills/app-icon-optimization) — When the user wants to design, test, or improve their app icon to increase tap-through rate and conversions in App Stor…
- [Eronred/app-launch](https://github.com/Eronred/aso-skills/tree/HEAD/skills/app-launch) — When the user wants to plan a launch strategy for a new app or major update.
- [Eronred/app-marketing-context](https://github.com/Eronred/aso-skills/tree/HEAD/skills/app-marketing-context) — When the user wants to create or update their app marketing context document.
- [Eronred/app-preview-video](https://github.com/Eronred/aso-skills/tree/HEAD/skills/app-preview-video) — When the user wants to plan, script, produce, or optimize App Store Preview videos or Google Play promo videos — the au…
- [Eronred/app-rejection-recovery](https://github.com/Eronred/aso-skills/tree/HEAD/skills/app-rejection-recovery) — When the user's app or update was rejected by Apple App Review or Google Play Review and they need to diagnose why, fix…
- [Eronred/category-positioning](https://github.com/Eronred/aso-skills/tree/HEAD/skills/category-positioning) — When the user wants to choose, change, or evaluate their App Store / Google Play category and subcategory — including p…
- [Eronred/asc-metrics](https://github.com/Eronred/aso-skills/tree/HEAD/skills/asc-metrics) — When the user wants to analyze their own app's actual performance data from App Store Connect — real downloads, revenue…
- [Eronred/app-store-featured](https://github.com/Eronred/aso-skills/tree/HEAD/skills/app-store-featured) — When the user wants to get featured on the App Store or understand the editorial process.
- [Eronred/localization](https://github.com/Eronred/aso-skills/tree/HEAD/skills/localization) — When the user wants to localize their App Store listing for international markets.
- [Eronred/market-movers](https://github.com/Eronred/aso-skills/tree/HEAD/skills/market-movers) — When the user wants to track App Store chart rank changes, find top gainers and losers, detect breakout apps entering t…
- [Eronred/market-pulse](https://github.com/Eronred/aso-skills/tree/HEAD/skills/market-pulse) — When the user wants a comprehensive App Store market overview, daily/weekly market briefing, or combined view of chart…
- [Eronred/apple-search-ads](https://github.com/Eronred/aso-skills/tree/HEAD/skills/apple-search-ads) — When the user wants to set up, optimize, or scale Apple Search Ads (ASA) campaigns — including keyword bidding, match t…
- [Eronred/aso-audit](https://github.com/Eronred/aso-skills/tree/HEAD/skills/aso-audit) — When the user wants a full ASO health audit, review their App Store listing quality, or diagnose why their app isn't ra…
- [Eronred/competitor-analysis](https://github.com/Eronred/aso-skills/tree/HEAD/skills/competitor-analysis) — When the user wants to analyze competitors' App Store strategy, find keyword gaps, or understand competitive positionin…
- [Eronred/competitor-tracking](https://github.com/Eronred/aso-skills/tree/HEAD/skills/competitor-tracking) — When the user wants to monitor competitor apps on an ongoing basis — tracking metadata changes, keyword shifts, screens…
- [Eronred/keyword-research](https://github.com/Eronred/aso-skills/tree/HEAD/skills/keyword-research) — When the user wants to discover, evaluate, or prioritize App Store keywords.
- [Eronred/aso-router](https://github.com/Eronred/aso-skills/tree/HEAD/skills/aso-router) — ---
- [Eronred/attribution-setup](https://github.com/Eronred/aso-skills/tree/HEAD/skills/attribution-setup) — When the user wants to set up, debug, or interpret app install attribution — including SKAdNetwork (SKAN), Apple's AdAt…
- [Eronred/crash-analytics](https://github.com/Eronred/aso-skills/tree/HEAD/skills/crash-analytics) — When the user wants to monitor, triage, or reduce their app's crash rate — including setting up Crashlytics, prioritizi…
- [Eronred/creator-ugc-marketing](https://github.com/Eronred/aso-skills/tree/HEAD/skills/creator-ugc-marketing) — When the user wants to plan, brief, source, or measure organic creator / influencer / UGC marketing for their app — inc…
- [Eronred/custom-product-pages](https://github.com/Eronred/aso-skills/tree/HEAD/skills/custom-product-pages) — When the user wants to design, deploy, or measure Apple Custom Product Pages (CPP) — the alternate App Store product pa…
- [Eronred/in-app-events](https://github.com/Eronred/aso-skills/tree/HEAD/skills/in-app-events) — When the user wants to create, plan, or optimize App Store In-App Events — the event cards that appear on the Today tab…
- [Eronred/metadata-optimization](https://github.com/Eronred/aso-skills/tree/HEAD/skills/metadata-optimization) — When the user wants to optimize App Store metadata — title, subtitle, keyword field, or description.
- [Eronred/monetization-strategy](https://github.com/Eronred/aso-skills/tree/HEAD/skills/monetization-strategy) — When the user wants to design or optimize their app's monetization — pricing, paywalls, subscriptions, or in-app purcha…
- [Eronred/onboarding-optimization](https://github.com/Eronred/aso-skills/tree/HEAD/skills/onboarding-optimization) — When the user wants to improve their app's onboarding experience, increase activation rate, reduce Day 1 drop-off, or o…
- [Eronred/paywall-optimization](https://github.com/Eronred/aso-skills/tree/HEAD/skills/paywall-optimization) — When the user wants to design, test, or optimize their app's paywall — layout, copy, pricing display, trial offers, pla…
- [Eronred/press-and-pr](https://github.com/Eronred/aso-skills/tree/HEAD/skills/press-and-pr) — When the user wants to get press coverage, media mentions, or editorial features for their app — including writing pres…
- [Eronred/rating-prompt-strategy](https://github.com/Eronred/aso-skills/tree/HEAD/skills/rating-prompt-strategy) — When the user wants to improve their app's star rating, increase ratings volume, optimize when and how they prompt user…
- [Eronred/referral-program](https://github.com/Eronred/aso-skills/tree/HEAD/skills/referral-program) — When the user wants to design, launch, or optimize an in-app referral / invite / share-to-earn program — including rewa…
- [Eronred/retention-optimization](https://github.com/Eronred/aso-skills/tree/HEAD/skills/retention-optimization) — When the user wants to reduce churn, improve user engagement, or increase lifetime value.
- [Eronred/review-management](https://github.com/Eronred/aso-skills/tree/HEAD/skills/review-management) — When the user wants to analyze, respond to, or improve their app reviews and ratings.
- [Eronred/screenshot-optimization](https://github.com/Eronred/aso-skills/tree/HEAD/skills/screenshot-optimization) — When the user wants to design, optimize, or evaluate App Store screenshots and preview videos.
- [Eronred/seasonal-aso](https://github.com/Eronred/aso-skills/tree/HEAD/skills/seasonal-aso) — When the user wants to optimize their App Store listing for seasonal events, holidays, or trending moments — including…
- [Eronred/subscription-lifecycle](https://github.com/Eronred/aso-skills/tree/HEAD/skills/subscription-lifecycle) — When the user wants to optimize their subscription business end-to-end — from trial start through renewal, cancellation…
- [Eronred/ua-campaign](https://github.com/Eronred/aso-skills/tree/HEAD/skills/ua-campaign) — When the user wants to plan or optimize paid user acquisition campaigns.
- [Eronred/web-to-app-funnel](https://github.com/Eronred/aso-skills/tree/HEAD/skills/web-to-app-funnel) — When the user wants to design or optimize the funnel that takes web visitors into installing and onboarding the app — i…

</details>

<details>
<summary><strong>Truongduy2611</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 1,240</summary>

- [truongduy2611/app-store-preflight-skills](https://github.com/truongduy2611/app-store-preflight-skills) — Scan an iOS/macOS Xcode project for common App Store rejection patterns before submission.

</details>

<details>
<summary><strong>BehiSecc</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 944</summary>

- [BehiSecc/VibeSec-Skill](https://github.com/BehiSecc/VibeSec-Skill) — This skill helps Claude write secure web applications.

</details>

<details>
<summary><strong>Huifer</strong> &nbsp;·&nbsp; 19 skills &nbsp;·&nbsp; ⭐ 876</summary>

- [huifer/ai-analyzer](https://github.com/huifer/Claude-Ally-Health/tree/HEAD/skills/ai-analyzer) — AI驱动的综合健康分析系统，整合多维度健康数据、识别异常模式、预测健康风险、提供个性化建议。支持智能问答和AI健康报告生成。
- [huifer/emergency-card](https://github.com/huifer/Claude-Ally-Health/tree/HEAD/skills/emergency-card) — 生成紧急情况下快速访问的医疗信息摘要卡片。当用户需要旅行、就诊准备、紧急情况或询问"紧急信息"、"医疗卡片"、"急救信息"时使用此技能。提取关键信息（过敏、用药、急症、植入物），支持多格式输出（JSON、文本、二维码），用于急救或快速就医。
- [huifer/family-health-analyzer](https://github.com/huifer/Claude-Ally-Health/tree/HEAD/skills/family-health-analyzer) — 分析家族病史、评估遗传风险、识别家庭健康模式、提供个性化预防建议
- [huifer/fitness-analyzer](https://github.com/huifer/Claude-Ally-Health/tree/HEAD/skills/fitness-analyzer) — 分析运动数据、识别运动模式、评估健身进展，并提供个性化训练建议。支持与慢性病数据的关联分析。
- [huifer/food-database-query](https://github.com/huifer/Claude-Ally-Health/tree/HEAD/skills/food-database-query) — **技能名称**: Food Database Query
- [huifer/goal-analyzer](https://github.com/huifer/Claude-Ally-Health/tree/HEAD/skills/goal-analyzer) — 分析健康目标数据、识别目标模式、评估目标进度,并提供个性化目标管理建议。支持与营养、运动、睡眠等健康数据的关联分析。
- [huifer/health-trend-analyzer](https://github.com/huifer/Claude-Ally-Health/tree/HEAD/skills/health-trend-analyzer) — 分析一段时间内健康数据的趋势和模式。关联药物、症状、生命体征、化验结果和其他健康指标的变化。识别令人担忧的趋势、改善情况，并提供数据驱动的洞察。当用户询问健康趋势、模式、随时间的变化或"我的健康状况有什么变化？"时使用。支持多维度分析（体…
- [huifer/mental-health-analyzer](https://github.com/huifer/Claude-Ally-Health/tree/HEAD/skills/mental-health-analyzer) — 分析心理健康数据、识别心理模式、评估心理健康状况、提供个性化心理健康建议。支持与睡眠、运动、营养等其他健康数据的关联分析。
- [huifer/nutrition-analyzer](https://github.com/huifer/Claude-Ally-Health/tree/HEAD/skills/nutrition-analyzer) — 分析营养数据、识别营养模式、评估营养状况，并提供个性化营养建议。支持与运动、睡眠、慢性病数据的关联分析。
- [huifer/occupational-health-analyzer](https://github.com/huifer/Claude-Ally-Health/tree/HEAD/skills/occupational-health-analyzer) — 分析职业健康数据、识别工作相关健康风险、评估职业健康状况、提供个性化职业健康建议。支持与睡眠、运动、心理健康等其他健康数据的关联分析。
- [huifer/oral-health-analyzer](https://github.com/huifer/Claude-Ally-Health/tree/HEAD/skills/oral-health-analyzer) — 分析口腔健康数据、识别口腔问题模式、评估口腔健康状况、提供个性化口腔健康建议。支持与营养、慢性病、用药等其他健康数据的关联分析。
- [huifer/rehabilitation-analyzer](https://github.com/huifer/Claude-Ally-Health/tree/HEAD/skills/rehabilitation-analyzer) — 分析康复训练数据、识别康复模式、评估康复进展，并提供个性化康复建议
- [huifer/sexual-health-analyzer](https://github.com/huifer/Claude-Ally-Health/tree/HEAD/skills/sexual-health-analyzer) — 本技能提供全面的性健康数据分析功能,包括IIEF-5评分分析、STD筛查管理、避孕效果评估、性活动统计以及与用药、慢性病、心理、营养、运动等模块的深度关联分析。
- [huifer/skin-health-analyzer](https://github.com/huifer/Claude-Ally-Health/tree/HEAD/skills/skin-health-analyzer) — 分析皮肤健康数据、识别皮肤问题模式、评估皮肤健康状况、提供个性化皮肤健康建议。支持与营养、慢性病、用药等其他健康数据的关联分析。
- [huifer/sleep-analyzer](https://github.com/huifer/Claude-Ally-Health/tree/HEAD/skills/sleep-analyzer) — 分析睡眠数据、识别睡眠模式、评估睡眠质量，并提供个性化睡眠改善建议。支持与其他健康数据的关联分析。
- [huifer/tcm-constitution-analyzer](https://github.com/huifer/Claude-Ally-Health/tree/HEAD/skills/tcm-constitution-analyzer) — 分析中医体质数据、识别体质类型、评估体质特征,并提供个性化养生建议。支持与营养、运动、睡眠等健康数据的关联分析。
- [huifer/travel-health-analyzer](https://github.com/huifer/Claude-Ally-Health/tree/HEAD/skills/travel-health-analyzer) — 分析旅行健康数据、评估目的地健康风险、提供疫苗接种建议、生成多语言紧急医疗信息卡片。支持WHO/CDC数据集成的专业级旅行健康风险评估。
- [huifer/weightloss-analyzer](https://github.com/huifer/Claude-Ally-Health/tree/HEAD/skills/weightloss-analyzer) — 分析减肥数据、计算代谢率、追踪能量缺口、管理减肥阶段
- [huifer/wellally-tech](https://github.com/huifer/Claude-Ally-Health/tree/HEAD/skills/wellally-tech) — Integrate digital health data sources (Apple Health, Fitbit, Oura Ring) and connect to WellAlly.tech knowledge base.

</details>

<details>
<summary><strong>Deusyu</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 766</summary>

- [deusyu/translate-book](https://github.com/deusyu/translate-book) — Translate books (PDF/DOCX/EPUB) into any language using parallel sub-agents.

</details>

<details>
<summary><strong>Alinaqi</strong> &nbsp;·&nbsp; 68 skills &nbsp;·&nbsp; ⭐ 694</summary>

- [alinaqi/aeo-optimization](https://github.com/alinaqi/maggy/tree/HEAD/skills/aeo-optimization) — AI Engine Optimization - semantic triples, page templates, content clusters for AI citations
- [alinaqi/agent-teams](https://github.com/alinaqi/maggy/tree/HEAD/skills/agent-teams) — Claude Code Agent Teams - default team-based development with strict TDD pipeline enforcement
- [alinaqi/agentic-development](https://github.com/alinaqi/maggy/tree/HEAD/skills/agentic-development) — Build AI agents with Pydantic AI (Python) and Claude SDK (Node.js)
- [alinaqi/ai-models](https://github.com/alinaqi/maggy/tree/HEAD/skills/ai-models) — Latest AI models reference - Claude, OpenAI, Gemini, Eleven Labs, Replicate
- [alinaqi/android-java](https://github.com/alinaqi/maggy/tree/HEAD/skills/android-java) — Android Java development with MVVM, ViewBinding, and Espresso testing
- [alinaqi/android-kotlin](https://github.com/alinaqi/maggy/tree/HEAD/skills/android-kotlin) — Android Kotlin development with Coroutines, Jetpack Compose, Hilt, and MockK testing
- [alinaqi/autonomous-testing](https://github.com/alinaqi/maggy/tree/HEAD/skills/autonomous-testing) — An AI-driven testing agent that auto-discovers, generates, executes, evaluates, and fixes tests for any project type.
- [alinaqi/aws-aurora](https://github.com/alinaqi/maggy/tree/HEAD/skills/aws-aurora) — AWS Aurora Serverless v2, RDS Proxy, Data API, connection pooling
- [alinaqi/aws-dynamodb](https://github.com/alinaqi/maggy/tree/HEAD/skills/aws-dynamodb) — AWS DynamoDB single-table design, GSI patterns, SDK v3 TypeScript/Python
- [alinaqi/azure-cosmosdb](https://github.com/alinaqi/maggy/tree/HEAD/skills/azure-cosmosdb) — Azure Cosmos DB partition keys, consistency levels, change feed, SDK patterns
- [alinaqi/base](https://github.com/alinaqi/maggy/tree/HEAD/skills/base) — Universal coding patterns, constraints, TDD workflow, atomic todos
- [alinaqi/build-in-public](https://github.com/alinaqi/maggy/tree/HEAD/skills/build-in-public) — Build in public isn't marketing.
- [alinaqi/cloudflare-d1](https://github.com/alinaqi/maggy/tree/HEAD/skills/cloudflare-d1) — Cloudflare D1 SQLite database with Workers, Drizzle ORM, migrations
- [alinaqi/code-deduplication](https://github.com/alinaqi/maggy/tree/HEAD/skills/code-deduplication) — Prevent semantic code duplication with capability index and check-before-write
- [alinaqi/code-graph](https://github.com/alinaqi/maggy/tree/HEAD/skills/code-graph) — AST-based code graph for fast symbol lookup, dependency analysis, and blast radius via codebase-memory-mcp MCP server
- [alinaqi/code-review](https://github.com/alinaqi/maggy/tree/HEAD/skills/code-review) — Mandatory code reviews via /code-review before commits and deploys
- [alinaqi/codex-review](https://github.com/alinaqi/maggy/tree/HEAD/skills/codex-review) — OpenAI Codex CLI code review with GPT-5.2-Codex, CI/CD integration
- [alinaqi/commit-hygiene](https://github.com/alinaqi/maggy/tree/HEAD/skills/commit-hygiene) — Atomic commits, PR size limits, commit thresholds, stacked PRs
- [alinaqi/council-review](https://github.com/alinaqi/maggy/tree/HEAD/skills/council-review) — Multi-model validation council — auto-validate plans, architecture changes, and PRs via validate-plan/review before exe…
- [alinaqi/cpg-analysis](https://github.com/alinaqi/maggy/tree/HEAD/skills/cpg-analysis) — Deep code property graph analysis with Joern CPG (AST+CFG+PDG) and CodeQL for control flow, data flow, taint analysis,…
- [alinaqi/credentials](https://github.com/alinaqi/maggy/tree/HEAD/skills/credentials) — Centralized API key management from Access.txt
- [alinaqi/cross-agent-delegation](https://github.com/alinaqi/maggy/tree/HEAD/skills/cross-agent-delegation) — Cross-agent task routing — Codex auto-review, Kimi delegation by complexity score (iCPG + Claude reasoning), iCPG + Mne…
- [alinaqi/database-schema](https://github.com/alinaqi/maggy/tree/HEAD/skills/database-schema) — Schema awareness - read before coding, type generation, prevent column errors
- [alinaqi/existing-repo](https://github.com/alinaqi/maggy/tree/HEAD/skills/existing-repo) — Analyze existing repositories, maintain structure, setup guardrails and best practices
- [alinaqi/external-model-delegation](https://github.com/alinaqi/maggy/tree/HEAD/skills/external-model-delegation) — A `UserPromptSubmit` hook classifies every user prompt into one of six cost/performance tiers.
- [alinaqi/firebase](https://github.com/alinaqi/maggy/tree/HEAD/skills/firebase) — Firebase Firestore, Auth, Storage, real-time listeners, security rules
- [alinaqi/flutter](https://github.com/alinaqi/maggy/tree/HEAD/skills/flutter) — Flutter development with Riverpod state management, Freezed, go_router, and mocktail testing
- [alinaqi/gemini-review](https://github.com/alinaqi/maggy/tree/HEAD/skills/gemini-review) — Google Gemini CLI code review with Gemini 2.5 Pro, 1M token context, CI/CD integration
- [alinaqi/icpg](https://github.com/alinaqi/maggy/tree/HEAD/skills/icpg) — Intent-Augmented Code Property Graph — tracks WHY code exists via ReasonNodes with formal contracts, 6-dimension drift…
- [alinaqi/iterative-development](https://github.com/alinaqi/maggy/tree/HEAD/skills/iterative-development) — TDD iteration loops using Claude Code Stop hooks - runs tests after each response, feeds failures back automatically
- [alinaqi/klaviyo](https://github.com/alinaqi/maggy/tree/HEAD/skills/klaviyo) — Klaviyo email/SMS marketing - profiles, events, flows, segmentation
- [alinaqi/llm-patterns](https://github.com/alinaqi/maggy/tree/HEAD/skills/llm-patterns) — AI-first application patterns, LLM testing, prompt management
- [alinaqi/maggy](https://github.com/alinaqi/maggy/tree/HEAD/skills/maggy) — Maggy is a local AI engineering command center.
- [alinaqi/medusa](https://github.com/alinaqi/maggy/tree/HEAD/skills/medusa) — Medusa headless commerce - modules, workflows, API routes, admin UI
- [alinaqi/mnemos](https://github.com/alinaqi/maggy/tree/HEAD/skills/mnemos) — Task-scoped memory lifecycle — typed MnemoGraph prevents lossy context compaction by treating facts/decisions/code-refs…
- [alinaqi/ui-mobile](https://github.com/alinaqi/maggy/tree/HEAD/skills/ui-mobile) — Mobile UI patterns - React Native, iOS/Android, touch targets
- [alinaqi/model-routing](https://github.com/alinaqi/maggy/tree/HEAD/skills/model-routing) — Every user prompt goes through a 9-tier classification pipeline before any AI model processes it.
- [alinaqi/ms-teams-apps](https://github.com/alinaqi/maggy/tree/HEAD/skills/ms-teams-apps) — Microsoft Teams bots and AI agents - Claude/OpenAI, Adaptive Cards, Graph API
- [alinaqi/nodejs-backend](https://github.com/alinaqi/maggy/tree/HEAD/skills/nodejs-backend) — Node.js backend patterns with Express/Fastify, repositories
- [alinaqi/playwright-testing](https://github.com/alinaqi/maggy/tree/HEAD/skills/playwright-testing) — E2E testing with Playwright - Page Objects, cross-browser, CI/CD
- [alinaqi/polyphony](https://github.com/alinaqi/maggy/tree/HEAD/skills/polyphony) — Multi-agent orchestration with container-isolated workspaces — each agent session runs in its own Docker container with…
- [alinaqi/posthog-analytics](https://github.com/alinaqi/maggy/tree/HEAD/skills/posthog-analytics) — PostHog analytics, event tracking, feature flags, dashboards
- [alinaqi/project-tooling](https://github.com/alinaqi/maggy/tree/HEAD/skills/project-tooling) — gh, vercel, supabase, render CLI and deployment platform setup
- [alinaqi/pwa-development](https://github.com/alinaqi/maggy/tree/HEAD/skills/pwa-development) — Progressive Web Apps - service workers, caching strategies, offline, Workbox
- [alinaqi/python](https://github.com/alinaqi/maggy/tree/HEAD/skills/python) — Python development with ruff, mypy, pytest - TDD and type safety
- [alinaqi/react-native](https://github.com/alinaqi/maggy/tree/HEAD/skills/react-native) — React Native mobile patterns, platform-specific code
- [alinaqi/react-web](https://github.com/alinaqi/maggy/tree/HEAD/skills/react-web) — React web development with hooks, React Query, Zustand
- [alinaqi/reddit-ads](https://github.com/alinaqi/maggy/tree/HEAD/skills/reddit-ads) — Reddit Ads API - campaigns, targeting, conversions, agentic optimization
- [alinaqi/reddit-api](https://github.com/alinaqi/maggy/tree/HEAD/skills/reddit-api) — Reddit API with PRAW (Python) and Snoowrap (Node.js)
- [alinaqi/security](https://github.com/alinaqi/maggy/tree/HEAD/skills/security) — OWASP security patterns, secrets management, security testing
- [alinaqi/session-management](https://github.com/alinaqi/maggy/tree/HEAD/skills/session-management) — Context preservation, tiered summarization, resumability
- [alinaqi/shopify-apps](https://github.com/alinaqi/maggy/tree/HEAD/skills/shopify-apps) — Shopify app development - Remix, Admin API, checkout extensions
- [alinaqi/site-architecture](https://github.com/alinaqi/maggy/tree/HEAD/skills/site-architecture) — Technical SEO - robots.txt, sitemap, meta tags, Core Web Vitals
- [alinaqi/supabase](https://github.com/alinaqi/maggy/tree/HEAD/skills/supabase) — Core Supabase CLI, migrations, RLS, Edge Functions
- [alinaqi/supabase-nextjs](https://github.com/alinaqi/maggy/tree/HEAD/skills/supabase-nextjs) — Next.js with Supabase and Drizzle ORM
- [alinaqi/supabase-node](https://github.com/alinaqi/maggy/tree/HEAD/skills/supabase-node) — Express/Hono with Supabase and Drizzle ORM
- [alinaqi/supabase-python](https://github.com/alinaqi/maggy/tree/HEAD/skills/supabase-python) — FastAPI with Supabase and SQLAlchemy/SQLModel
- [alinaqi/team-coordination](https://github.com/alinaqi/maggy/tree/HEAD/skills/team-coordination) — Multi-person projects - shared state, todo claiming, handoffs
- [alinaqi/ticket-craft](https://github.com/alinaqi/maggy/tree/HEAD/skills/ticket-craft) — Create Jira/Asana/Linear tickets optimized for Claude Code execution - AI-native ticket writing
- [alinaqi/typescript](https://github.com/alinaqi/maggy/tree/HEAD/skills/typescript) — TypeScript strict mode with eslint and jest
- [alinaqi/ui-testing](https://github.com/alinaqi/maggy/tree/HEAD/skills/ui-testing) — Visual testing - catch invisible buttons, broken layouts, contrast
- [alinaqi/ui-web](https://github.com/alinaqi/maggy/tree/HEAD/skills/ui-web) — Web UI - glassmorphism, Tailwind, dark mode, accessibility
- [alinaqi/user-journeys](https://github.com/alinaqi/maggy/tree/HEAD/skills/user-journeys) — User experience flows - journey mapping, UX validation, error recovery
- [alinaqi/visual-validation](https://github.com/alinaqi/maggy/tree/HEAD/skills/visual-validation) — Every UI change should be visually verified before it ships.
- [alinaqi/web-content](https://github.com/alinaqi/maggy/tree/HEAD/skills/web-content) — SEO and AI discovery (GEO) - schema, ChatGPT/Perplexity optimization
- [alinaqi/web-payments](https://github.com/alinaqi/maggy/tree/HEAD/skills/web-payments) — Stripe Checkout, subscriptions, webhooks, customer portal
- [alinaqi/woocommerce](https://github.com/alinaqi/maggy/tree/HEAD/skills/woocommerce) — WooCommerce REST API - products, orders, customers, webhooks
- [alinaqi/workspace](https://github.com/alinaqi/maggy/tree/HEAD/skills/workspace) — Dynamic multi-repo and monorepo awareness for Claude Code.

</details>

<details>
<summary><strong>Aklofas</strong> &nbsp;·&nbsp; 12 skills &nbsp;·&nbsp; ⭐ 530</summary>

- [aklofas/datasheets](https://github.com/aklofas/kicad-happy/tree/HEAD/skills/datasheets) — Extract structured specifications from electronic component datasheet PDFs — pinouts, electrical characteristics, perip…
- [aklofas/digikey](https://github.com/aklofas/kicad-happy/tree/HEAD/skills/digikey) — Search DigiKey for electronic components and download datasheets — primary source for prototype orders and the preferre…
- [aklofas/bom](https://github.com/aklofas/kicad-happy/tree/HEAD/skills/bom) — BOM (Bill of Materials) management for electronics projects — the primary orchestrator skill that coordinates DigiKey,…
- [aklofas/element14](https://github.com/aklofas/kicad-happy/tree/HEAD/skills/element14) — Search Newark, Farnell, and element14 for electronic components — find parts by MPN or distributor part number, check p…
- [aklofas/jlcpcb](https://github.com/aklofas/kicad-happy/tree/HEAD/skills/jlcpcb) — JLCPCB PCB fabrication and assembly — BOM/CPL generation, basic vs extended parts, assembly constraints, design rules,…
- [aklofas/kicad](https://github.com/aklofas/kicad-happy/tree/HEAD/skills/kicad) — Analyze KiCad projects and PDF schematics: schematics, PCB layouts, Gerbers, footprints, symbols, netlists, and design…
- [aklofas/emc](https://github.com/aklofas/kicad-happy/tree/HEAD/skills/emc) — EMC pre-compliance risk analysis for KiCad PCB designs — 18 check categories, 44 rule IDs covering ground planes, decou…
- [aklofas/kidoc](https://github.com/aklofas/kicad-happy/tree/HEAD/skills/kidoc) — Generate professional engineering documentation from KiCad projects — Hardware Design Descriptions (HDD), CE Technical…
- [aklofas/lcsc](https://github.com/aklofas/kicad-happy/tree/HEAD/skills/lcsc) — Search LCSC Electronics for electronic components — find parts by LCSC number (Cxxxxx) or MPN, check stock/pricing, dow…
- [aklofas/mouser](https://github.com/aklofas/kicad-happy/tree/HEAD/skills/mouser) — Search Mouser Electronics for electronic components — secondary source for prototype orders.
- [aklofas/pcbway](https://github.com/aklofas/kicad-happy/tree/HEAD/skills/pcbway) — PCBWay PCB fabrication and assembly — turnkey/consigned assembly, design rules, ordering workflow.
- [aklofas/spice](https://github.com/aklofas/kicad-happy/tree/HEAD/skills/spice) — Run automatic SPICE simulations on subcircuits detected from KiCad schematic analysis — validates filter frequencies, d…

</details>

<details>
<summary><strong>Meodai</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 486</summary>

- [meodai/skill.color-expert](https://github.com/meodai/skill.color-expert) — Use when working with color naming, color theory, color spaces, color definitions, or any task involving color knowledg…

</details>

<details>
<summary><strong>Komal SkyNET</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 424</summary>

- [komal-SkyNET/claude-skill-homeassistant](https://github.com/komal-SkyNET/claude-skill-homeassistant) — Expert-level Home Assistant configuration management with efficient deployment workflows (git and rapid scp iteration),…

</details>

<details>
<summary><strong>Lawvable</strong> &nbsp;·&nbsp; 42 skills &nbsp;·&nbsp; ⭐ 415</summary>

- [lawvable/assignation-refere-communication-associe-selim-brihi](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/assignation-refere-communication-associe-selim-brihi) — Rédaction d'assignations en référé devant le tribunal de commerce ou des activités économiques pour le droit de communi…
- [lawvable/assignation-refere-recouvrement-creance-selim-brihi](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/assignation-refere-recouvrement-creance-selim-brihi) — Rédaction d'assignations en référé devant le tribunal de commerce ou des activités économiques pour le recouvrement de…
- [lawvable/contract-review-anthropic](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/contract-review-anthropic) — Review contracts against your organization's negotiation playbook, flagging deviations and generating redline suggestio…
- [lawvable/politique-cookies-malik-taiar](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/politique-cookies-malik-taiar) — Guide for drafting cookie policies compliant with GDPR and the ePrivacy Directive.
- [lawvable/docx-processing-anthropic](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/docx-processing-anthropic) — Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files).
- [lawvable/docx-processing-openai](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/docx-processing-openai) — Toolkit for comprehensive document reading, editing, and creation with visual quality control.
- [lawvable/docx-processing-superdoc](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/docx-processing-superdoc) — Searches, replaces, and reads text in Word documents.
- [lawvable/docx-processing-lawvable](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/docx-processing-lawvable) — Programmatically edit Word documents (.docx) with live preview and track changes via SuperDoc VS Code extension.
- [lawvable/gdpr-breach-sentinel-oliver-schmidt-prietz](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/gdpr-breach-sentinel-oliver-schmidt-prietz) — Elite incident response and legal compliance guidance for data breaches under GDPR Articles 33 & 34.
- [lawvable/dpia-sentinel-oliver-schmidt-prietz](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/dpia-sentinel-oliver-schmidt-prietz) — GDPR Data Protection Impact Assessment (DPIA) guidance under Article 35 GDPR, EDPB Guidelines WP 248 rev.01, EDPB Opini…
- [lawvable/gdpr-privacy-notice-eu-oliver-schmidt-prietz](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/gdpr-privacy-notice-eu-oliver-schmidt-prietz) — Draft GDPR/DSGVO-compliant privacy notices as .docx for any EU/EEA jurisdiction and audience.
- [lawvable/canned-responses-anthropic](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/canned-responses-anthropic) — Generate templated responses for common legal inquiries and identify when situations require individualized attention.
- [lawvable/legal-risk-assessment-anthropic](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/legal-risk-assessment-anthropic) — Assess and classify legal risks using a severity-by-likelihood framework with escalation criteria.
- [lawvable/legal-risk-assessment-zacharie-laik](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/legal-risk-assessment-zacharie-laik) — Conduct legal research and risk analysis using GoodLegal MCP tools.
- [lawvable/legal-simulation-patrick-munro](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/legal-simulation-patrick-munro) — Framework for demonstrating AI capabilities in legal contexts.
- [lawvable/mediation-dispute-analysis-jinzhe-tan](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/mediation-dispute-analysis-jinzhe-tan) — Use this skill whenever a lawyer or mediator needs help analyzing a dispute for mediation purposes.
- [lawvable/meeting-briefing-anthropic](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/meeting-briefing-anthropic) — Prepare structured briefings for meetings with legal relevance and track resulting action items.
- [lawvable/nda-review-jamie-tso](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/nda-review-jamie-tso) — Guide to review incoming one-way (unilateral) commercial NDAs in a jurisdiction-agnostic way, from either a Recipient o…
- [lawvable/nda-triage-anthropic](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/nda-triage-anthropic) — Screen incoming NDAs and classify them as GREEN (standard), YELLOW (needs review), or RED (significant issues).
- [lawvable/nil-contract-analysis-samir-patel](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/nil-contract-analysis-samir-patel) — NIL (Name, Image, and Likeness) contract analysis for NCAA student-athletes from the athlete's perspective.
- [lawvable/notification-licenciement-selim-brihi](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/notification-licenciement-selim-brihi) — Guide pour la rédaction de notifications de licenciement conformes au droit du travail français.
- [lawvable/outlook-emails-lawvable](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/outlook-emails-lawvable) — Read, search, and download emails and attachments from Microsoft Outlook via OAuth2.
- [lawvable/pdf-processing-anthropic](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/pdf-processing-anthropic) — Use this skill whenever the user wants to do anything with PDF files.
- [lawvable/pdf-processing-openai](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/pdf-processing-openai) — Toolkit for comprehensive PDF reading, reviwing, and creation with visual quality control.
- [lawvable/pptx-processing-anthropic](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/pptx-processing-anthropic) — Use this skill any time a .pptx file is involved in any way — as input, output, or both.
- [lawvable/compliance-anthropic](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/compliance-anthropic) — Navigate privacy regulations (GDPR, CCPA), review DPAs, and handle data subject requests.
- [lawvable/politique-confidentialite-malik-taiar](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/politique-confidentialite-malik-taiar) — Guide for drafting privacy policies compliant with GDPR.
- [lawvable/red-team-verifier-patrick-munro](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/red-team-verifier-patrick-munro) — Adversarial verification for AI-generated legal content with systematic fact-checking, source validation, and quality c…
- [lawvable/requete-cph-licenciement-faute-grave-selim-brihi](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/requete-cph-licenciement-faute-grave-selim-brihi) — Rédaction de requêtes devant le Conseil de prud'hommes pour contester un licenciement pour faute grave.
- [lawvable/security-review-openai](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/security-review-openai) — Perform language and framework specific security best-practice reviews and suggest improvements.
- [lawvable/skill-creator-anthropic](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/skill-creator-anthropic) — Guide for creating effective skills.
- [lawvable/skill-creator-openai](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/skill-creator-openai) — Guide for creating effective skills.
- [lawvable/skill-optimizer-lawvable](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/skill-optimizer-lawvable) — Guide to analyze a current work session and propose improvements to skills.
- [lawvable/statute-analysis-rafal-fryc](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/statute-analysis-rafal-fryc) — Guide for reading, interpreting, and applying statutes, regulations, and rules in legal and compliance contexts.
- [lawvable/tabular-review-lawvable](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/tabular-review-lawvable) — Guide to analyze multiple documents (PDF, DOCX) against user-defined columns and produce a structured Excel output with…
- [lawvable/tech-contract-negotiation-patrick-munro](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/tech-contract-negotiation-patrick-munro) — Guide to negotiating technology services agreements, professional services contracts, and commercial B2B transactions.
- [lawvable/vendor-due-diligence-patrick-munro](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/vendor-due-diligence-patrick-munro) — Framework for assessing IT service providers, technology vendors, and third-party partners.
- [lawvable/vscode-extension-builder-lawvable](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/vscode-extension-builder-lawvable) — Build VS Code extensions from scratch or convert existing JS/React/Vue apps.
- [lawvable/politique-lanceur-alerte-malik-taiar](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/politique-lanceur-alerte-malik-taiar) — Guide for (a) auditing an existing whistleblower system or (b) drafting a compliant reporting policy from a provided te…
- [lawvable/xlsx-processing-anthropic](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/xlsx-processing-anthropic) — Use this skill any time a spreadsheet file is the primary input or output.
- [lawvable/xlsx-processing-manus](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/xlsx-processing-manus) — Professional Excel spreadsheet creation with a focus on aesthetics and data analysis.
- [lawvable/xlsx-processing-openai](https://github.com/lawvable/awesome-legal-skills/tree/HEAD/skills/xlsx-processing-openai) — Toolkit for comprehensive Spreadsheet reading, creation, editing, and analysis with visual quality control.

</details>

<details>
<summary><strong>Makenotion</strong> &nbsp;·&nbsp; 8 skills &nbsp;·&nbsp; ⭐ 412 &nbsp;·&nbsp; official</summary>

- [makenotion/knowledge-capture](https://github.com/makenotion/claude-code-notion-plugin/tree/HEAD/skills/notion/knowledge-capture) — Transforms conversations and discussions into structured documentation pages in Notion.
- [makenotion/knowledge-capture](https://github.com/makenotion/notion-cookbook/tree/HEAD/skills/claude/knowledge-capture) — Transforms conversations and discussions into structured documentation pages in Notion.
- [makenotion/meeting-intelligence](https://github.com/makenotion/claude-code-notion-plugin/tree/HEAD/skills/notion/meeting-intelligence) — Prepares meeting materials by gathering context from Notion, enriching with Claude research, and creating both an inter…
- [makenotion/meeting-intelligence](https://github.com/makenotion/notion-cookbook/tree/HEAD/skills/claude/meeting-intelligence) — Prepares meeting materials by gathering context from Notion, enriching with Claude research, and creating both an inter…
- [makenotion/research-documentation](https://github.com/makenotion/claude-code-notion-plugin/tree/HEAD/skills/notion/research-documentation) — Searches across your Notion workspace, synthesizes findings from multiple pages, and creates comprehensive research doc…
- [makenotion/research-documentation](https://github.com/makenotion/notion-cookbook/tree/HEAD/skills/claude/research-documentation) — Searches across your Notion workspace, synthesizes findings from multiple pages, and creates comprehensive research doc…
- [makenotion/spec-to-implementation](https://github.com/makenotion/claude-code-notion-plugin/tree/HEAD/skills/notion/spec-to-implementation) — Turns product or tech specs into concrete Notion tasks that Claude code can implement.
- [makenotion/spec-to-implementation](https://github.com/makenotion/notion-cookbook/tree/HEAD/skills/claude/spec-to-implementation) — Turns product or tech specs into concrete Notion tasks that Claude code can implement.

</details>

<details>
<summary><strong>Zscole</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 339</summary>

- [zscole/model-hierarchy-skill](https://github.com/zscole/model-hierarchy-skill) — Cost-optimize AI agent operations by routing tasks to appropriate models based on complexity.

</details>

<details>
<summary><strong>Charlie85270</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 303</summary>

- [Charlie85270/world-builder](https://github.com/Charlie85270/Dorothy/tree/HEAD/skills/world-builder) — Create and manage generative game zones for Dorothy's Pokemon-style world.

</details>

<details>
<summary><strong>Gitroomhq</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 289</summary>

- [gitroomhq/postiz](https://github.com/gitroomhq/postiz-agent/tree/HEAD/skills/postiz) — Postiz is a tool to schedule social media and chat posts to 28+ channels X, LinkedIn, LinkedIn Page, Reddit, Instagram,…

</details>

<details>
<summary><strong>Testdino Hq</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 276 &nbsp;·&nbsp; official</summary>

- [testdino-hq/playwright-skill](https://github.com/testdino-hq/playwright-skill) — Battle-tested Playwright patterns for writing, debugging, and scaling reliable test suites.

</details>

<details>
<summary><strong>Bitwize Music Studio</strong> &nbsp;·&nbsp; 53 skills &nbsp;·&nbsp; ⭐ 251</summary>

- [bitwize-music-studio/album-art-director](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/album-art-director) — Creates visual concepts for album artwork and generates AI art prompts.
- [bitwize-music-studio/album-conceptualizer](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/album-conceptualizer) — Designs album concepts, tracklist architecture, and thematic planning through 7 structured phases.
- [bitwize-music-studio/tutorial](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/tutorial) — Provides interactive guided album creation for new users.
- [bitwize-music-studio/album-dashboard](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/album-dashboard) — Shows a structured progress dashboard for an album with percentage complete per phase, blocking items, and status break…
- [bitwize-music-studio/album-ideas](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/album-ideas) — Tracks and manages album ideas including brainstorming, planning, and status updates.
- [bitwize-music-studio/resume](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/resume) — Finds an album by name and shows detailed status with next steps.
- [bitwize-music-studio/researchers-biographical](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/researchers-biographical) — Researches personal backgrounds, interviews, motivations, and humanizing details.
- [bitwize-music-studio/about](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/about) — Provides information about the bitwize-music plugin, its version, and its creator.
- [bitwize-music-studio/document-hunter](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/document-hunter) — Searches and retrieves documents from free public sources using automated browser navigation.
- [bitwize-music-studio/explicit-checker](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/explicit-checker) — Scans lyrics for explicit content and verifies that explicit flags match actual content.
- [bitwize-music-studio/researchers-financial](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/researchers-financial) — Researches SEC filings, earnings calls, analyst reports, and market data.
- [bitwize-music-studio/genre-creator](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/genre-creator) — Create new genre documentation files for the bitwize-music genre library.
- [bitwize-music-studio/researchers-gov](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/researchers-gov) — Researches DOJ/FBI/SEC press releases, agency statements, and government sources.
- [bitwize-music-studio/researchers-historical](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/researchers-historical) — Researches archives, contemporary accounts, and timeline reconstruction.
- [bitwize-music-studio/import-art](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/import-art) — Places album art files in the correct audio and content directory locations.
- [bitwize-music-studio/import-audio](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/import-audio) — Moves audio files to the correct album location with proper path structure.
- [bitwize-music-studio/import-track](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/import-track) — Moves track markdown files to the correct album location.
- [bitwize-music-studio/researchers-journalism](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/researchers-journalism) — Researches investigative articles, interviews, and news coverage.
- [bitwize-music-studio/researchers-legal](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/researchers-legal) — Researches court documents, indictments, plea agreements, and sentencing records.
- [bitwize-music-studio/lyric-refiner](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/lyric-refiner) — Autonomous multi-pass lyric refinement for tightening, cohesion, and album unity.
- [bitwize-music-studio/lyric-reviewer](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/lyric-reviewer) — Reviews lyrics against a quality checklist before Suno generation.
- [bitwize-music-studio/voice-checker](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/voice-checker) — Reviews lyrics and prose for AI-written patterns (abstract noun stacking, over-explained metaphors, cliche escalation,…
- [bitwize-music-studio/lyric-writer](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/lyric-writer) — Writes or reviews lyrics with professional prosody, rhyme craft, and quality checks.
- [bitwize-music-studio/pronunciation-specialist](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/pronunciation-specialist) — Scans lyrics for pronunciation risks and prevents Suno mispronunciations.
- [bitwize-music-studio/mastering-engineer](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/mastering-engineer) — Guides audio mastering for streaming platforms including loudness optimization and tonal balance.
- [bitwize-music-studio/mix-engineer](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/mix-engineer) — Polishes raw Suno audio by processing per-stem WAVs (vocals, backing_vocals, drums, bass, guitar, keyboard, strings, br…
- [bitwize-music-studio/clipboard](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/clipboard) — Copies track content (lyrics, style prompts, streaming lyrics) to the system clipboard.
- [bitwize-music-studio/cloud-uploader](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/cloud-uploader) — Uploads promo videos and content to Cloudflare R2 or AWS S3.
- [bitwize-music-studio/plagiarism-checker](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/plagiarism-checker) — Scans lyrics for phrases that may match existing songs using web search and LLM knowledge.
- [bitwize-music-studio/next-step](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/next-step) — Analyzes album state and recommends the optimal next action.
- [bitwize-music-studio/researcher](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/researcher) — Conducts investigative-grade research with primary source analysis, cross-verification, and trial-level depth.
- [bitwize-music-studio/verify-sources](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/verify-sources) — Captures human source verification for tracks, timestamps it, and updates track files.
- [bitwize-music-studio/help](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/help) — Shows available skills, common workflows, and quick reference for the plugin.
- [bitwize-music-studio/new-album](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/new-album) — Creates a new album with the correct directory structure and templates.
- [bitwize-music-studio/configure](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/configure) — Sets up or edits the plugin configuration file interactively.
- [bitwize-music-studio/health-check](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/health-check) — Runs plugin health checks (venv packages and skill registration).
- [bitwize-music-studio/pre-generation-check](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/pre-generation-check) — Validates all pre-generation gates before sending tracks to Suno.
- [bitwize-music-studio/researchers-primary-source](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/researchers-primary-source) — Researches the subject's own words from tweets, blogs, forums, and chat logs.
- [bitwize-music-studio/promo-reviewer](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/promo-reviewer) — Reviews and iterates on social media copy in album promo/ files.
- [bitwize-music-studio/promo-writer](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/promo-writer) — Generates platform-specific social media copy from album themes, track concepts, and lyrics.
- [bitwize-music-studio/promo-director](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/promo-director) — Generates 15-second vertical promo videos for social media from mastered audio.
- [bitwize-music-studio/promote-idea](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/promote-idea) — Converts an album idea from IDEAS.md into an actual album project in one step.
- [bitwize-music-studio/release-director](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/release-director) — Coordinates album release including QA, distribution prep, and platform uploads.
- [bitwize-music-studio/researchers-verifier](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/researchers-verifier) — Performs quality control, citation validation, and fact-checking before human review.
- [bitwize-music-studio/researchers-security](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/researchers-security) — Researches malware analysis, CVEs, attribution reports, and hacker community sources.
- [bitwize-music-studio/session-start](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/session-start) — Runs the session startup procedure - verifies setup, loads config and state, checks skill models, and reports project s…
- [bitwize-music-studio/setup](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/setup) — Detects your Python environment and guides you through installing plugin dependencies.
- [bitwize-music-studio/sheet-music-publisher](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/sheet-music-publisher) — Converts mastered audio to sheet music and creates printable songbooks.
- [bitwize-music-studio/suno-engineer](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/suno-engineer) — Constructs technical Suno V5/V5.5 style prompts, selects genres, and optimizes generation settings.
- [bitwize-music-studio/researchers-tech](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/researchers-tech) — Researches project histories, changelogs, developer interviews, and open source documentation.
- [bitwize-music-studio/test](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/test) — Runs automated tests to validate plugin integrity across 14 categories.
- [bitwize-music-studio/rename](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/rename) — Renames an album or track, updating slugs, titles, and all mirrored paths.
- [bitwize-music-studio/validate-album](https://github.com/bitwize-music-studio/claude-ai-music-skills/tree/HEAD/skills/validate-album) — Validates album directory structure, file locations, and content integrity.

</details>

<details>
<summary><strong>EveryInc</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 250</summary>

- [EveryInc/charlie-cfo-skill](https://github.com/EveryInc/charlie-cfo-skill) — Your AI CFO for bootstrapped startups, named after Charlie Munger who embodied the principle that capital discipline is…

</details>

<details>
<summary><strong>CosmoBlk</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 213</summary>

- [CosmoBlk/email-marketing-bible](https://github.com/CosmoBlk/email-marketing-bible) — Comprehensive, data-backed email marketing knowledge base.

</details>

<details>
<summary><strong>Indranilbanerjee</strong> &nbsp;·&nbsp; 154 skills &nbsp;·&nbsp; ⭐ 136</summary>

- [indranilbanerjee/ab-test-plan](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/ab-test-plan) — Design A/B and multivariate tests.
- [indranilbanerjee/ad-creative](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/ad-creative) — Generate platform-specific ad copy.
- [indranilbanerjee/add-integration](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/add-integration) — Add MCP server integrations.
- [indranilbanerjee/aeo-audit](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/aeo-audit) — Audit AI search visibility.
- [indranilbanerjee/aeo-geo](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/aeo-geo) — Optimize AI engine visibility.
- [indranilbanerjee/agency-dashboard](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/agency-dashboard) — Portfolio-level agency dashboard aggregating health metrics across all client brands — campaign status, budget pacing,…
- [indranilbanerjee/analytics-insights](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/analytics-insights) — Analyze marketing performance.
- [indranilbanerjee/attribution-model](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/attribution-model) — Set up attribution models.
- [indranilbanerjee/attribution-report](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/attribution-report) — Run multi-touch attribution analysis.
- [indranilbanerjee/audience-intelligence](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/audience-intelligence) — Research target audiences.
- [indranilbanerjee/audience-profile](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/audience-profile) — Build detailed buyer personas.
- [indranilbanerjee/autopilot-status](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/autopilot-status) — Check campaign autopilot status.
- [indranilbanerjee/publish-blog](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/publish-blog) — Publish blog posts.
- [indranilbanerjee/entity-audit](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/entity-audit) — Audit brand entity consistency.
- [indranilbanerjee/brand-setup](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/brand-setup) — Set up or update a brand profile.
- [indranilbanerjee/status](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/status) — Show a unified status snapshot of the active brand: profile, active engagements with current part, recent insights, rec…
- [indranilbanerjee/budget-optimizer](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/budget-optimizer) — Optimize budget allocation.
- [indranilbanerjee/budget-tracker](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/budget-tracker) — Track budget pacing in real time.
- [indranilbanerjee/what-if](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/what-if) — Compare budget scenarios side-by-side.
- [indranilbanerjee/c2pa-metadata](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/c2pa-metadata) — Embed C2PA (Content Authenticity Initiative) provenance manifests in AI-generated marketing assets (image/video/audio/P…
- [indranilbanerjee/campaign-audit](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/campaign-audit) — Audit a brand's existing live campaigns across every active channel — paid, organic, email, social, content, SEO.
- [indranilbanerjee/campaign-orchestrator](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/campaign-orchestrator) — Orchestrate full campaign lifecycle.
- [indranilbanerjee/campaign-plan](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/campaign-plan) — Build multi-channel campaign plans.
- [indranilbanerjee/campaign-status](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/campaign-status) — Check active campaign status.
- [indranilbanerjee/case-study-plan](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/case-study-plan) — Create case studies and success stories.
- [indranilbanerjee/churn-risk](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/churn-risk) — Assess customer churn risk.
- [indranilbanerjee/client-onboarding](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/client-onboarding) — Plan client onboarding.
- [indranilbanerjee/client-proposal](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/client-proposal) — Draft agency proposals.
- [indranilbanerjee/client-report](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/client-report) — Generate client-facing reports.
- [indranilbanerjee/client-validation-document](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/client-validation-document) — Produce the Part 5 Client Validation Document — the one true stop where unbiased v1 findings meet the client.
- [indranilbanerjee/cohort-analysis](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/cohort-analysis) — Analyze customer cohorts.
- [indranilbanerjee/competitor-alerts](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/competitor-alerts) — Configure competitor alerts.
- [indranilbanerjee/competitor-analysis](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/competitor-analysis) — Run competitive analysis.
- [indranilbanerjee/competitor-pages](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/competitor-pages) — Create competitor comparison pages.
- [indranilbanerjee/competitor-monitor](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/competitor-monitor) — Set up ongoing competitor monitoring.
- [indranilbanerjee/content-brief](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/content-brief) — Create detailed content briefs.
- [indranilbanerjee/content-calendar](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/content-calendar) — Plan content calendars.
- [indranilbanerjee/content-decay-scan](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/content-decay-scan) — Scan content library for decay signals: declining traffic, falling rankings, outdated stats, dropped AI citations.
- [indranilbanerjee/content-engine](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/content-engine) — Create or optimize marketing content.
- [indranilbanerjee/eval-config](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/eval-config) — Configure content eval settings.
- [indranilbanerjee/eval-suite](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/eval-suite) — Batch evaluate multiple content pieces.
- [indranilbanerjee/eval-content](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/eval-content) — Evaluate content quality.
- [indranilbanerjee/content-repurpose](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/content-repurpose) — Repurpose content across channels.
- [indranilbanerjee/context-engine](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/context-engine) — Load brand context for marketing tasks.
- [indranilbanerjee/continuous-improvement-loop](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/continuous-improvement-loop) — Run Part 12 — the continuous improvement loop.
- [indranilbanerjee/counter-narrative](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/counter-narrative) — Build counter-narrative playbooks.
- [indranilbanerjee/creative-health](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/creative-health) — Assess ad creative fatigue.
- [indranilbanerjee/creative-testing-framework](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/creative-testing-framework) — Design structured ad creative tests with A/B test plans, multivariate creative strategies, sample size calculations, an…
- [indranilbanerjee/credential-switch](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/credential-switch) — Switch brand credentials.
- [indranilbanerjee/crisis-response](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/crisis-response) — Manage PR crises.
- [indranilbanerjee/pipeline-update](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/pipeline-update) — Update CRM pipeline.
- [indranilbanerjee/crm-sync](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/crm-sync) — Sync data to CRM platforms.
- [indranilbanerjee/cro](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/cro) — Optimize conversion rates.
- [indranilbanerjee/dark-funnel](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/dark-funnel) — Map invisible buyer journeys.
- [indranilbanerjee/data-export](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/data-export) — Export marketing data.
- [indranilbanerjee/data-import](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/data-import) — Import data from external sources.
- [indranilbanerjee/help](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/help) — Show the getting started guide, available commands, examples, and help for Digital Marketing Pro
- [indranilbanerjee/digital-pr](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/digital-pr) — Plan digital PR campaigns.
- [indranilbanerjee/email-sequence](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/email-sequence) — Design email sequences.
- [indranilbanerjee/emerging-channels](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/emerging-channels) — Explore emerging marketing channels.
- [indranilbanerjee/executive-dashboard](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/executive-dashboard) — Design executive marketing dashboards.
- [indranilbanerjee/exec-summary](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/exec-summary) — Generate C-suite executive summaries.
- [indranilbanerjee/four-core-documents](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/four-core-documents) — Produce the Four Core Documents at strategic depth (61 total steps): Business & SBU Analysis, Segmentation Framework, B…
- [indranilbanerjee/funnel-architect](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/funnel-architect) — Design marketing funnels.
- [indranilbanerjee/funnel-audit](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/funnel-audit) — Audit funnel performance.
- [indranilbanerjee/geo-monitor](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/geo-monitor) — Monitor brand AI visibility.
- [indranilbanerjee/growth-engineering](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/growth-engineering) — Engineer growth loops.
- [indranilbanerjee/loop-detect](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/loop-detect) — Identify and model growth loops.
- [indranilbanerjee/growth-plan](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/growth-plan) — Produce the 11-section Growth Plan — the flagship Part 8 client-facing deliverable that synthesises the entire engageme…
- [indranilbanerjee/gsc-ai-performance](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/gsc-ai-performance) — Query and interpret the new Google Search Console AI Performance Report (AI Overviews + AI Mode impressions/pages/count…
- [indranilbanerjee/hreflang-check](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/hreflang-check) — Audit hreflang tags.
- [indranilbanerjee/image-seo-audit](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/image-seo-audit) — Audit image SEO.
- [indranilbanerjee/import-sop](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/import-sop) — Import agency SOPs.
- [indranilbanerjee/import-guidelines](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/import-guidelines) — Import brand guidelines.
- [indranilbanerjee/import-template](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/import-template) — Import deliverable templates.
- [indranilbanerjee/influencer-creator](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/influencer-creator) — Plan influencer and creator partnerships.
- [indranilbanerjee/influencer-brief](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/influencer-brief) — Create influencer campaign briefs.
- [indranilbanerjee/integrations](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/integrations) — Show MCP integration status.
- [indranilbanerjee/intelligence-report](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/intelligence-report) — Generate marketing intelligence briefings from compound intelligence across agents — surfaces learnings, cross-agent pa…
- [indranilbanerjee/journey-design](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/journey-design) — Design cross-channel customer journeys.
- [indranilbanerjee/keyword-research](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/keyword-research) — Research and cluster keywords.
- [indranilbanerjee/landing-page-audit](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/landing-page-audit) — Audit landing pages.
- [indranilbanerjee/language-audit](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/language-audit) — Audit multilingual content consistency.
- [indranilbanerjee/language-config](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/language-config) — Configure language settings.
- [indranilbanerjee/launch-ad-campaign](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/launch-ad-campaign) — Launch paid ad campaigns.
- [indranilbanerjee/launch-campaign](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/launch-campaign) — Orchestrate the full multi-channel launch of an approved campaign plan — pre-launch checklist, asset readiness gate, ch…
- [indranilbanerjee/launch-plan](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/launch-plan) — Build product launch playbooks.
- [indranilbanerjee/lead-import](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/lead-import) — Import leads into CRM.
- [indranilbanerjee/live-dashboard](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/live-dashboard) — Create live Looker Studio dashboards.
- [indranilbanerjee/local-seo](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/local-seo) — Build local SEO strategy.
- [indranilbanerjee/local-seo-audit](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/local-seo-audit) — Audit local SEO health.
- [indranilbanerjee/localize-campaign](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/localize-campaign) — Localize campaigns for multiple markets.
- [indranilbanerjee/market-weather](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/market-weather) — Assess current market conditions.
- [indranilbanerjee/anomaly-scan](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/anomaly-scan) — Detect marketing anomalies.
- [indranilbanerjee/marketing-automation](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/marketing-automation) — Design marketing automation workflows.
- [indranilbanerjee/check](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/check) — Run the unified pre-publish quality gate on marketing content — hallucination detection, claim verification, brand voic…
- [indranilbanerjee/engagement-workflow](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/engagement-workflow) — Run a full marketing engagement using the 12-Part methodology.
- [indranilbanerjee/learn](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/learn) — Save a marketing learning or insight.
- [indranilbanerjee/performance-check](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/performance-check) — Pull live marketing metrics for a performance snapshot: KPIs vs targets, trend comparison, and cross-platform overview.
- [indranilbanerjee/performance-report](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/performance-report) — Generate performance reports.
- [indranilbanerjee/recall](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/recall) — Recall marketing learnings.
- [indranilbanerjee/connect](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/connect) — Set up an MCP connector.
- [indranilbanerjee/martech-audit](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/martech-audit) — Audit the martech stack.
- [indranilbanerjee/media-plan](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/media-plan) — Create a paid media plan.
- [indranilbanerjee/message-test](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/message-test) — Test message variants on synthetic audiences.
- [indranilbanerjee/multilingual-score](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/multilingual-score) — Score localized content quality.
- [indranilbanerjee/narrative-landscape](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/narrative-landscape) — Map the competitive narrative landscape.
- [indranilbanerjee/narrative-tracker](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/narrative-tracker) — Track AI engine brand narratives.
- [indranilbanerjee/page-seo-analysis](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/page-seo-analysis) — Analyze SEO for a single page.
- [indranilbanerjee/paid-advertising](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/paid-advertising) — Plan paid advertising campaigns.
- [indranilbanerjee/pdf-report](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/pdf-report) — Generate branded PDF reports.
- [indranilbanerjee/pr-pitch](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/pr-pitch) — Create media pitch packages.
- [indranilbanerjee/pricing-test](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/pricing-test) — Test pricing strategies with synthetic data.
- [indranilbanerjee/programmatic-seo](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/programmatic-seo) — Plan programmatic SEO pages.
- [indranilbanerjee/prompt-test](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/prompt-test) — A/B test content variations.
- [indranilbanerjee/qbr-plan](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/qbr-plan) — Prepare a Quarterly Business Review.
- [indranilbanerjee/quality-report](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/quality-report) — Generate quality trends report.
- [indranilbanerjee/rank-monitor](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/rank-monitor) — Monitor keyword rankings.
- [indranilbanerjee/redirect-manager](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/redirect-manager) — Manage URL redirects.
- [indranilbanerjee/region-config](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/region-config) — Configure regional settings.
- [indranilbanerjee/reputation-management](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/reputation-management) — Manage brand reputation.
- [indranilbanerjee/retargeting-strategy](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/retargeting-strategy) — Design retargeting strategy.
- [indranilbanerjee/simulate](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/simulate) — Simulate revenue impact via Monte Carlo.
- [indranilbanerjee/review-response](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/review-response) — Respond to online reviews.
- [indranilbanerjee/roi-calculator](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/roi-calculator) — Calculate marketing ROI.
- [indranilbanerjee/save-knowledge](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/save-knowledge) — Save brand knowledge to memory.
- [indranilbanerjee/schedule-social](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/schedule-social) — Schedule social media posts.
- [indranilbanerjee/search-knowledge](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/search-knowledge) — Search stored brand knowledge.
- [indranilbanerjee/segment-audience](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/segment-audience) — Create audience segments.
- [indranilbanerjee/send-email-campaign](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/send-email-campaign) — Send email campaigns.
- [indranilbanerjee/send-notification](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/send-notification) — Send team notifications.
- [indranilbanerjee/send-report](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/send-report) — Deliver performance reports.
- [indranilbanerjee/send-sms](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/send-sms) — Send SMS or WhatsApp messages.
- [indranilbanerjee/seo-audit](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/seo-audit) — Run comprehensive SEO audit.
- [indranilbanerjee/seo-implement](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/seo-implement) — Execute SEO changes.
- [indranilbanerjee/seo-plan](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/seo-plan) — Build SEO strategy and roadmap.
- [indranilbanerjee/serp-tracker](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/serp-tracker) — Track SERP feature changes.
- [indranilbanerjee/share-of-voice](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/share-of-voice) — Measure share of voice.
- [indranilbanerjee/sitemap-manager](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/sitemap-manager) — Manage XML sitemaps.
- [indranilbanerjee/social-strategy](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/social-strategy) — Build social media strategy.
- [indranilbanerjee/sop-library](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/sop-library) — Manage agency SOPs.
- [indranilbanerjee/switch-brand](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/switch-brand) — Switch active brand profile.
- [indranilbanerjee/sync-memory](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/sync-memory) — Batch sync session learnings to memory.
- [indranilbanerjee/focus-group](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/focus-group) — Run synthetic focus groups.
- [indranilbanerjee/team-assign](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/team-assign) — Assign tasks to team members.
- [indranilbanerjee/tech-seo-audit](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/tech-seo-audit) — Run technical SEO audit.
- [indranilbanerjee/technical-seo](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/technical-seo) — Deep technical SEO analysis.
- [indranilbanerjee/translate-content](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/translate-content) — Translate marketing content.
- [indranilbanerjee/validate-output](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/validate-output) — Validate content structure.
- [indranilbanerjee/validate-profile](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/validate-profile) — Validate a brand profile end-to-end — required fields, voice/audience completeness, connector reachability, credentials…
- [indranilbanerjee/verify-claims](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/verify-claims) — Verify marketing claims.
- [indranilbanerjee/video-script](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/video-script) — Write video scripts.
- [indranilbanerjee/webinar-plan](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/webinar-plan) — Plan webinars and virtual events.
- [indranilbanerjee/yearly-planner](https://github.com/indranilbanerjee/digital-marketing-pro/tree/HEAD/skills/yearly-planner) — Produce the 12-month operational Yearly Planner — the calendar companion to the Growth Plan in Part 8.

</details>

<details>
<summary><strong>Gokapso</strong> &nbsp;·&nbsp; 3 skills &nbsp;·&nbsp; ⭐ 129</summary>

- [gokapso/automate-whatsapp](https://github.com/gokapso/agent-skills/tree/HEAD/skills/automate-whatsapp) — Build WhatsApp automations with Kapso workflows: configure WhatsApp triggers, edit workflow graphs, manage executions,…
- [gokapso/integrate-whatsapp](https://github.com/gokapso/agent-skills/tree/HEAD/skills/integrate-whatsapp) — Connect WhatsApp to your product with Kapso: onboard customers with setup links, detect connections, receive events via…
- [gokapso/observe-whatsapp](https://github.com/gokapso/agent-skills/tree/HEAD/skills/observe-whatsapp) — Observe and troubleshoot WhatsApp in Kapso: debug message delivery, inspect webhook deliveries/retries, triage API erro…

</details>

<details>
<summary><strong>Degausai</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 124</summary>

- [degausai/wonda-cli](https://github.com/degausai/wonda/tree/HEAD/skills/wonda-cli) — Using the Wonda CLI to generate images, videos, music, and audio from the terminal — plus LinkedIn, Reddit, and X/Twitt…

</details>

<details>
<summary><strong>Talkstream</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 113</summary>

- [talkstream/ru-text](https://github.com/talkstream/ru-text) — Use when writing, editing, or reviewing Russian-language text, or when user mentions ru-text.

</details>

<details>
<summary><strong>CodeRabbit</strong> &nbsp;·&nbsp; 2 skills &nbsp;·&nbsp; ⭐ 112 &nbsp;·&nbsp; official</summary>

- [coderabbitai/code-review](https://github.com/coderabbitai/skills/tree/HEAD/skills/code-review) — AI-powered code review using CodeRabbit.
- [coderabbitai/autofix](https://github.com/coderabbitai/skills/tree/HEAD/skills/autofix) — Safely review and apply CodeRabbit PR review-thread feedback from GitHub with per-change approval; never execute review…

</details>

<details>
<summary><strong>Wrsmith108</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 110</summary>

- [wrsmith108/linear-claude-skill](https://github.com/wrsmith108/linear-claude-skill) — Managing Linear issues, projects, and teams.

</details>

<details>
<summary><strong>Digidai</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 105</summary>

- [Digidai/product-manager-skills](https://github.com/Digidai/product-manager-skills) — PM skill for Claude Code, Codex, Cursor, and Windsurf.

</details>

<details>
<summary><strong>Kevin7Qi</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 84</summary>

- [Kevin7Qi/codex-collab](https://github.com/Kevin7Qi/codex-collab) — Use when the user asks to invoke, delegate to, or collaborate with Codex on any task.

</details>

<details>
<summary><strong>Omkamal</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 84</summary>

- [omkamal/pypict-claude-skill](https://github.com/omkamal/pypict-claude-skill) — Design comprehensive test cases using PICT (Pairwise Independent Combinatorial Testing) for any piece of requirements o…

</details>

<details>
<summary><strong>MohamedAbdallah 14</strong> &nbsp;·&nbsp; 6 skills &nbsp;·&nbsp; ⭐ 57</summary>

- [MohamedAbdallah-14/unslop](https://github.com/MohamedAbdallah-14/unslop/tree/HEAD/skills/unslop) — Humanize LLM output so it reads like a careful human wrote it.
- [MohamedAbdallah-14/unslop-commit](https://github.com/MohamedAbdallah-14/unslop/tree/HEAD/skills/unslop-commit) — Rewrites commit messages so they sound like a careful human engineer wrote them.
- [MohamedAbdallah-14/unslop-file](https://github.com/MohamedAbdallah-14/unslop/tree/HEAD/skills/unslop-file) — Humanize natural-language memory files (CLAUDE.md, todos, preferences, docs) by removing AI-isms and adding burstiness…
- [MohamedAbdallah-14/unslop-help](https://github.com/MohamedAbdallah-14/unslop/tree/HEAD/skills/unslop-help) — Quick-reference card for unslop modes, sub-skills, and slash commands.
- [MohamedAbdallah-14/unslop-reasoning](https://github.com/MohamedAbdallah-14/unslop/tree/HEAD/skills/unslop-reasoning) — Strip AI-slop patterns from reasoning traces (chain-of-thought, extended thinking, agent decomposition) — not final pro…
- [MohamedAbdallah-14/unslop-review](https://github.com/MohamedAbdallah-14/unslop/tree/HEAD/skills/unslop-review) — Rewrites code review comments so they read like a human teammate wrote them.

</details>

<details>
<summary><strong>Uucz</strong> &nbsp;·&nbsp; 7 skills &nbsp;·&nbsp; ⭐ 57</summary>

- [uucz/moyu](https://github.com/uucz/moyu/tree/HEAD/skills/moyu) — Automatically activates when over-engineering patterns are detected: (1) Modifying code or files the user did not expli…
- [uucz/moyu-en](https://github.com/uucz/moyu/tree/HEAD/skills/moyu-en) — Automatically activates when over-engineering patterns are detected: (1) Modifying code or files the user did not expli…
- [uucz/moyu-fr](https://github.com/uucz/moyu/tree/HEAD/skills/moyu-fr) — S'active automatiquement lorsque des patterns de sur-ingénierie sont détectés : (1) Modifier du code ou des fichiers qu…
- [uucz/moyu-ja](https://github.com/uucz/moyu/tree/HEAD/skills/moyu-ja) — 過剰エンジニアリングのパターンが検出された場合に自動的に発動します： (1) ユーザーが明示的に変更を求めていないコードやファイルを修正する (2) 要求されていない新しい抽象レイヤー（class、interface、factory、wr…
- [uucz/moyu-ko](https://github.com/uucz/moyu/tree/HEAD/skills/moyu-ko) — 과잉 엔지니어링 패턴이 감지되면 자동으로 활성화됩니다: (1) 사용자가 명시적으로 변경을 요청하지 않은 코드나 파일을 수정하는 경우 (2) 요청되지 않은 새로운 추상화 레이어(class, interface, fac…
- [uucz/moyu-lite](https://github.com/uucz/moyu/tree/HEAD/skills/moyu-lite) — Lightweight anti-over-engineering guard.
- [uucz/moyu-strict](https://github.com/uucz/moyu/tree/HEAD/skills/moyu-strict) — Strict anti-over-engineering enforcement.

</details>

<details>
<summary><strong>K Kolomeitsev</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 52</summary>

- [k-kolomeitsev/data-structure-protocol](https://github.com/k-kolomeitsev/data-structure-protocol/tree/HEAD/skills/data-structure-protocol) — Build and navigate DSP (Data Structure Protocol) — graph-based long-term structural memory of codebases for LLM agents.

</details>

<details>
<summary><strong>Robzolkos</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 52</summary>

- [robzolkos/skill-rails-upgrade](https://github.com/robzolkos/skill-rails-upgrade) — Analyze Rails application upgrade path.

</details>

<details>
<summary><strong>SHADOWPR0</strong> &nbsp;·&nbsp; 2 skills &nbsp;·&nbsp; ⭐ 43</summary>

- [SHADOWPR0/beautiful_prose](https://github.com/SHADOWPR0/beautiful_prose) — A hard-edged writing style contract for timeless, forceful English prose without modern AI tics.
- [SHADOWPR0/security-bluebook-builder](https://github.com/SHADOWPR0/security-bluebook-builder) — Create or refine a concise, normative security policy ("Blue Book") for sensitive applications.

</details>

<details>
<summary><strong>HeshamFS</strong> &nbsp;·&nbsp; 23 skills &nbsp;·&nbsp; ⭐ 41</summary>

- [HeshamFS/benchmark-and-mms-planner](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/verification-validation/benchmark-and-mms-planner) — Plan verification and validation campaigns for simulation codes using manufactured solutions, canonical benchmark probl…
- [HeshamFS/convergence-study](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/core-numerical/convergence-study) — Perform spatial and temporal convergence analysis for solution verification — compute observed convergence orders from…
- [HeshamFS/differentiation-schemes](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/core-numerical/differentiation-schemes) — Select and apply numerical differentiation schemes for PDE and ODE discretization — generate finite-difference stencils…
- [HeshamFS/fair-simulation-packager](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/data-management/fair-simulation-packager) — Create FAIR-minded reproducibility bundles for materials simulations by collecting input/output file inventories, hashe…
- [HeshamFS/hpc-runtime-doctor](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/hpc-deployment/hpc-runtime-doctor) — Diagnose HPC runtime and scheduler problems for materials simulations, including MPI/OpenMP/GPU layout, modules, CUDA/K…
- [HeshamFS/linear-solvers](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/core-numerical/linear-solvers) — Select and configure linear solvers for Ax=b systems arising in numerical simulations — choose between direct (LU, Chol…
- [HeshamFS/md-analysis-planner](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/simulation-workflow/md-analysis-planner) — Plan molecular dynamics post-processing for materials simulations, including RDF, MSD and diffusion, VACF/VDOS, coordin…
- [HeshamFS/mesh-generation](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/core-numerical/mesh-generation) — Plan and evaluate mesh generation for numerical simulations — estimate grid resolution from physics scales (interface w…
- [HeshamFS/nonlinear-solvers](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/core-numerical/nonlinear-solvers) — Select and configure nonlinear solvers for root-finding f(x)=0, optimization min F(x), and least-squares problems — cho…
- [HeshamFS/numerical-integration](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/core-numerical/numerical-integration) — Select and configure time integration methods for ODE and PDE simulations — choose among explicit Runge-Kutta, BDF, Ros…
- [HeshamFS/numerical-stability](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/core-numerical/numerical-stability) — Analyze numerical stability for time-dependent PDE simulations — check CFL and Fourier criteria, perform von Neumann st…
- [HeshamFS/ontology-explorer](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/ontology/ontology-explorer) — Parse, navigate, and query materials science ontology structures — browse class hierarchies, inspect individual classes…
- [HeshamFS/ontology-mapper](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/ontology/ontology-mapper) — Map materials science terms, crystal structures, and sample descriptions to standardized ontology classes and propertie…
- [HeshamFS/ontology-validator](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/ontology/ontology-validator) — Validate material sample annotations against ontology constraints — check that class names and property names exist in…
- [HeshamFS/parameter-optimization](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/simulation-workflow/parameter-optimization) — Explore and optimize simulation parameters via design of experiments (DOE), sensitivity analysis, and optimizer selecti…
- [HeshamFS/simulation-failure-triage](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/robustness/simulation-failure-triage) — Triage cross-code simulation failures and propose safe retry ladders for nonconvergence, NaN/Inf, exploding energies, u…
- [HeshamFS/simulation-orchestrator](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/simulation-workflow/simulation-orchestrator) — Orchestrate multi-simulation campaigns — generate parameter sweep configurations (grid, linspace, or Latin Hypercube sa…
- [HeshamFS/performance-profiling](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/simulation-workflow/performance-profiling) — Identify computational bottlenecks, analyze parallel scaling, estimate memory requirements, and generate optimization r…
- [HeshamFS/post-processing](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/simulation-workflow/post-processing) — Extract, analyze, and summarize simulation output data — pull spatial fields at specific timesteps, compute time-series…
- [HeshamFS/simulation-validator](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/simulation-workflow/simulation-validator) — Validate simulations across three stages — run pre-flight checks on configuration files (parameter ranges, required fie…
- [HeshamFS/slurm-job-script-generator](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/hpc-deployment/slurm-job-script-generator) — Generate correct, copy-pasteable SLURM sbatch job scripts and sanity-check HPC resource requests — configure nodes, MPI…
- [HeshamFS/time-stepping](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/core-numerical/time-stepping) — Plan and control time-step policies for transient simulations — couple CFL and physics-based stability limits with adap…
- [HeshamFS/workflow-engine-mapper](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/simulation-workflow/workflow-engine-mapper) — Map computational materials tasks onto workflow engines such as atomate2, jobflow, AiiDA, pyiron, or a simple one-off s…

</details>

<details>
<summary><strong>Muthuishere</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 39</summary>

- [muthuishere/hand-drawn-diagrams](https://github.com/muthuishere/hand-drawn-diagrams) — Create hand-drawn Excalidraw diagrams, flows, explainers, wireframes, and page mockups.

</details>

<details>
<summary><strong>Takechanman1228</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 36</summary>

- [takechanman1228/ecom](https://github.com/takechanman1228/claude-ecom/tree/HEAD/skills/ecom) — Claude-powered ecommerce business review toolkit for D2C stores.

</details>

<details>
<summary><strong>Honeydew Ai</strong> &nbsp;·&nbsp; 12 skills &nbsp;·&nbsp; ⭐ 35 &nbsp;·&nbsp; official</summary>

- [honeydew-ai/attribute-creation](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/tree/HEAD/skills/attribute-creation) — Guides you step-by-step through defining a calculated attribute (dimension) on a Honeydew entity.
- [honeydew-ai/context-item-creation](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/tree/HEAD/skills/context-item-creation) — Guides you through creating context items — instructions, skills, knowledge pointers, and memory events — that give the…
- [honeydew-ai/conversation-review](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/tree/HEAD/skills/conversation-review) — Use when a semantic/context layer curator wants to review past analysis conversations in bulk, categorize user feedback…
- [honeydew-ai/filtering](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/tree/HEAD/skills/filtering) — Use when the user needs to filter data — whether in a structured query, a metric aggregation, or an attribute expressio…
- [honeydew-ai/domain-creation](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/tree/HEAD/skills/domain-creation) — Guides you through creating a Honeydew domain — a governance object that scopes entity/field visibility and applies man…
- [honeydew-ai/entity-creation](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/tree/HEAD/skills/entity-creation) — Guides you through defining a new Honeydew entity from a data warehouse source — covering source type, granularity key,…
- [honeydew-ai/validation](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/tree/HEAD/skills/validation) — Use after creating or modifying ANY Honeydew object (metric, attribute, entity, domain).
- [honeydew-ai/query](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/tree/HEAD/skills/query) — Use when the user wants to query or analyze data through the Honeydew semantic layer — including natural language analy…
- [honeydew-ai/metric-creation](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/tree/HEAD/skills/metric-creation) — Guides you step-by-step through defining a business metric (aggregation) on a Honeydew entity.
- [honeydew-ai/model-exploration](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/tree/HEAD/skills/model-exploration) — Use when exploring Honeydew semantic layer, discovering entities/fields, setting up workspace and branch context, or ru…
- [honeydew-ai/relation-creation](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/tree/HEAD/skills/relation-creation) — Guides you through defining a relationship between two Honeydew entities — covering join type, direction, cross-filteri…
- [honeydew-ai/workspace-branch](https://github.com/honeydew-ai/honeydew-ai-coding-agents-plugins/tree/HEAD/skills/workspace-branch) — Use when setting up workspace and branch context, switching workspaces or branches, creating or deleting branches, revi…

</details>

<details>
<summary><strong>Frmoretto</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 30</summary>

- [frmoretto/clarity-gate](https://github.com/frmoretto/clarity-gate/tree/HEAD/skills/clarity-gate) — Pre-ingestion verification for epistemic quality in RAG systems.

</details>

<details>
<summary><strong>Cypress Io</strong> &nbsp;·&nbsp; 3 skills &nbsp;·&nbsp; ⭐ 27 &nbsp;·&nbsp; official</summary>

- [cypress-io/cypress-author](https://github.com/cypress-io/ai-toolkit/tree/HEAD/skills/cypress-author) — Creates, updates, and fixes Cypress tests (E2E/end-to-end and component tests).
- [cypress-io/cypress-docs](https://github.com/cypress-io/ai-toolkit/tree/HEAD/skills/cypress-docs) — Search and extract Cypress information from official documentation (docs.cypress.io, cypress.io); prefer LLM markdown u…
- [cypress-io/cypress-explain](https://github.com/cypress-io/ai-toolkit/tree/HEAD/skills/cypress-explain) — Explains Cypress tests (E2E and component tests), and answers questions about Cypress use and behavior.

</details>

<details>
<summary><strong>More Io</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 24</summary>

- [more-io/apple-bridges](https://github.com/more-io/claude-apple-bridges/tree/HEAD/skills/apple-bridges) — Use this skill whenever the user asks about Apple apps — Reminders, Calendar, Contacts, Notes, Mail, or tmux sessions.

</details>

<details>
<summary><strong>Awrshift</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 21</summary>

- [awrshift/claude-memory-kit](https://github.com/awrshift/claude-memory-kit) — Persistent memory for Claude Code agents with an agent-audit-ritual architecture.

</details>

<details>
<summary><strong>Metalbear Co</strong> &nbsp;·&nbsp; 6 skills &nbsp;·&nbsp; ⭐ 20 &nbsp;·&nbsp; official</summary>

- [metalbear-co/mirrord-ci](https://github.com/metalbear-co/skills/tree/HEAD/skills/mirrord-ci) — Help users set up mirrord in CI pipelines for testing against real Kubernetes environments.
- [metalbear-co/mirrord-config](https://github.com/metalbear-co/skills/tree/HEAD/skills/mirrord-config) — Helps users generate, edit, and validate mirrord.json configuration files for mirrord (MetalBear).
- [metalbear-co/mirrord-db-branching](https://github.com/metalbear-co/skills/tree/HEAD/skills/mirrord-db-branching) — Helps users configure mirrord.json for database branching, enabling isolated database copies for safe development and t…
- [metalbear-co/mirrord-kafka](https://github.com/metalbear-co/skills/tree/HEAD/skills/mirrord-kafka) — Helps DevOps engineers configure mirrord Operator's Kafka queue splitting feature end-to-end.
- [metalbear-co/mirrord-operator](https://github.com/metalbear-co/skills/tree/HEAD/skills/mirrord-operator) — Help users install and configure the mirrord operator for team environments.
- [metalbear-co/mirrord-quickstart](https://github.com/metalbear-co/skills/tree/HEAD/skills/mirrord-quickstart) — Guide users from zero to their first working mirrord session.

</details>

<details>
<summary><strong>Ethos Link</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 16</summary>

- [ethos-link/rails-conventions](https://github.com/ethos-link/rails-conventions) — Rails 8.x application architecture, implementation, and review guidance for production codebases.

</details>

<details>
<summary><strong>Dembrandt</strong> &nbsp;·&nbsp; 32 skills &nbsp;·&nbsp; ⭐ 14</summary>

- [dembrandt/algorithmic-color-palette](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/algorithmic-color-palette) — Derive a full UI colour palette algorithmically from one or two brand colours.
- [dembrandt/brand-visual-language](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/brand-visual-language) — A brand's visual tone — playful or serious, rounded or angular — should be consistent across all UI elements.
- [dembrandt/button-states](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/button-states) — Every interactive element needs a complete set of visual states — rest, hover, active/pressed, focus, disabled, and loa…
- [dembrandt/color-mode-and-theme](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/color-mode-and-theme) — Choose light, dark, or combined color mode deliberately based on brand tone and user context.
- [dembrandt/component-family-consistency](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/component-family-consistency) — Buttons, inputs, pills, badges, calendars, and other interactive components form a visual family — they share the same…
- [dembrandt/data-display-and-selection](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/data-display-and-selection) — Complex data deserves multiple view modes — grid, list, table — chosen by the user based on their task.
- [dembrandt/dembrandt](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/dembrandt) — Orchestrator for the full dembrandt UX pipeline.
- [dembrandt/elevation-and-depth](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/elevation-and-depth) — Elevation — subtle shadows and layering — communicates visual hierarchy by lifting elements above the surface.
- [dembrandt/extract-design](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/extract-design) — Extract a complete design system — colors, typography, spacing, components, shadows, and W3C design tokens — from any l…
- [dembrandt/form-design](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/form-design) — Forms have three layers of guidance: helper text below the input explains what to enter, placeholder shows the expected…
- [dembrandt/generate-ui-from-brand](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/generate-ui-from-brand) — Pipeline skill — turns a URL or DESIGN.md into a concrete UI structure with decisions already made.
- [dembrandt/gestalt-ui-organisation](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/gestalt-ui-organisation) — UI layout and grouping should follow Gestalt principles so users immediately understand which controls, commands, and e…
- [dembrandt/global-toolbar-controls](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/global-toolbar-controls) — Quick global settings — currency, language, region, units — belong in a persistent, low-profile location such as a head…
- [dembrandt/information-architecture](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/information-architecture) — In large applications, information architecture determines whether users can find, understand, and act on data.
- [dembrandt/loading-states-and-perceived-performance](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/loading-states-and-perceived-performance) — Manage user expectations during wait times with appropriate loading states — from simple spinners to complex skeleton s…
- [dembrandt/micro-interactions](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/micro-interactions) — Micro-interactions are small, purposeful animations and responses that reward the user and make the interface feel aliv…
- [dembrandt/modular-scale-typography](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/modular-scale-typography) — Typography feels cohesive and intentional when font sizes follow a modular scale — a ratio-based sequence where every s…
- [dembrandt/motion-and-storytelling](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/motion-and-storytelling) — Disney's 12 animation principles, cinematic storytelling techniques, and comic book conventions apply to web UI — used…
- [dembrandt/nielsen-usability-heuristics](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/nielsen-usability-heuristics) — UI design and review should apply Nielsen's 10 Usability Heuristics — the foundational principles for evaluating and im…
- [dembrandt/notifications-and-recovery](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/notifications-and-recovery) — When something goes wrong, the user must be able to recover or try again.
- [dembrandt/performance-and-web-vitals](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/performance-and-web-vitals) — Audit UI performance with Lighthouse and fix Core Web Vitals — LCP, CLS, INP.
- [dembrandt/real-world-metaphors](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/real-world-metaphors) — UI patterns borrowed from the physical world feel immediately intuitive — cards feel graspable, carousels feel scrollab…
- [dembrandt/responsive-paradigms](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/responsive-paradigms) — Mobile, tablet, and desktop are different interaction paradigms — not the same layout scaled up or down.
- [dembrandt/scroll-areas](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/scroll-areas) — Scroll areas inside a layout should be avoided wherever possible.
- [dembrandt/semantic-html-and-seo](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/semantic-html-and-seo) — Semantic HTML5, SEO fundamentals, alt texts, progressive enhancement, SPA considerations, device capability detection,…
- [dembrandt/status-colors-and-errors](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/status-colors-and-errors) — Keep status and error colours minimal and consistent — too many semantic colours confuse users.
- [dembrandt/sticky-and-fixed-elements](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/sticky-and-fixed-elements) — Sticky and fixed positioning keeps critical UI persistent as the user scrolls — headers at the top, toolbars at the bot…
- [dembrandt/ui-context-and-scope](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/ui-context-and-scope) — UI should make it immediately clear where the user is, what context they are operating in, and what their actions will…
- [dembrandt/ui-density](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/ui-density) — UI density — how much information and how many features appear at once — should match the primary platform and user typ…
- [dembrandt/user-flows-and-guided-paths](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/user-flows-and-guided-paths) — Related features and tasks — such as purchase flows, onboarding, or multi-step configuration — should be designed as na…
- [dembrandt/visual-emphasis-and-hierarchy](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/visual-emphasis-and-hierarchy) — The most important actions and content in a UI should be visually prominent — through size, colour, weight, and positio…
- [dembrandt/wcag-accessibility](https://github.com/dembrandt/dembrandt-skills/tree/HEAD/skills/wcag-accessibility) — UI must comply with WCAG 2.2 Level AA, as required by the European Accessibility Act (EN 301 549).

</details>

<details>
<summary><strong>Trycourier</strong> &nbsp;·&nbsp; 1 skill &nbsp;·&nbsp; ⭐ 9 &nbsp;·&nbsp; official</summary>

- [trycourier/courier-skills](https://github.com/trycourier/courier-skills) — Use when building notifications with Courier across email, SMS, push, in-app inbox, Slack, Teams, or WhatsApp.

</details>

<!-- skills-list-end -->

## Getting Started

### Use a skill in your agent

Most agents read skills from a local directory. For example, with Claude Code:

```bash
mkdir -p ~/.config/claude-code/skills/
cp -r skill-name ~/.config/claude-code/skills/
head ~/.config/claude-code/skills/skill-name/SKILL.md
```

The agent loads the skill automatically and activates it when relevant. Cursor,
Windsurf, Cline, Codex, Gemini CLI, and other agents follow the same open
`SKILL.md` convention — drop the folder where your agent expects skills.

### Find skills programmatically

The catalog is a single JSON file you can fetch and filter:

```bash
# Top coding skills in the catalog
jq '[.[] | select(.category == "coding")][:10] | .[].display_name' dist/ai-skills.json
```

## Using the Catalog

[`dist/ai-skills.json`](dist/ai-skills.json) is the canonical export. Each entry
carries the skill's `id`, `display_name`, `description`, `authors`, `tags`,
`category`, `source` (repo + path), `metadata.stars`, and `added_at`. Entries are
ordered by source-repo stars (descending) so the most popular sources lead and
each source's skills stay grouped together — ideal for powering a search UI, an
agent's skill picker, or a recommendations API.

## Creating Skills

Each skill is a folder with a `SKILL.md` file and optional supporting files:

```
skill-name/
├── SKILL.md          # Required: instructions + YAML frontmatter
├── scripts/          # Optional: helper scripts
├── references/       # Optional: reference docs
└── assets/           # Optional: templates / assets
```

Minimal template:

```markdown
---
name: my-skill-name
description: A clear description of what this skill does and when to use it.
---

# My Skill Name

Detailed description of the skill's purpose and capabilities.

## When to Use This Skill

- Use case 1
- Use case 2

## Instructions

[Detailed instructions for the agent on how to execute this skill]

## Examples

[Real-world examples showing the skill in action]
```

**Best practices:** focus on specific, repeatable tasks; write instructions for
the agent, not the end user; include clear examples and edge cases; confirm
before destructive operations; and document prerequisites. The full guide,
including a richer template, lives in [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Registry Entry Format

Each skill is generated as `registry/{owner}-{repo}/{owner}-{repo}-{skill-dir}.yaml`:

```yaml
id: anthropics-skills-algorithmic-art
display_name: Algorithmic Art
description: Creating algorithmic art using p5.js with seeded randomness ...
authors:
  - anthropics
is_official: true
tags:
  - generative-art
  - p5js
  - creative-coding
category: creative
source:
  path: /skills/algorithmic-art
  repo: anthropics/skills
metadata:
  stars: 149805
added_at: "2026-06-05"
```

- **Filename** `{owner}-{repo}-{skill_dir}.yaml` is globally unique; it's also the
  dedupe key, so a skill is "known" if that stem exists in any folder.
- **One folder per source repo** keeps every source's skills together.
- **`metadata.stars`** records the source repo's GitHub star count and drives the
  ordering of `dist/ai-skills.json`.

## Contributing

Contributing is simple: **add a GitHub repo to [`sources.yaml`](sources.yaml)** and
open a PR. A GitHub Action scans the repo for `SKILL.md` files, classifies each
skill, and adds it to the catalog automatically — you never hand-write entries.

- Found a repo with skills? Add its URL.
- Wrote your own skill? Push the `SKILL.md` to a public repo and add that URL.

Add a source by picking the line that matches where the `SKILL.md` files live:

```yaml
sources:
  # SKILL.md at the repo root
  - url: https://github.com/owner/my-skill

  # Skills inside a folder (each subfolder with a SKILL.md becomes an entry)
  - url: https://github.com/owner/my-skills
    skills_path: skills/

  # Multiple scan roots with no shared parent
  - url: https://github.com/huggingface/skills
    skills_paths:
      - skills/
      - hf-mcp/skills/
```

Add `is_official: true` for first-party/vendor repos. Then open a PR titled
something like `chore(sources): add owner/repo`.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the full guide.

## Resources

- [Anthropic Skills Repository](https://github.com/anthropics/skills) — the open `SKILL.md` standard and example skills
- [Agent Skills (engineering deep dive)](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Skills Overview](https://www.anthropic.com/news/skills)
- [`sources.yaml`](sources.yaml) · [`scripts/`](scripts/) · [`dist/ai-skills.json`](dist/ai-skills.json)

## License

This repository's tooling is maintained by TrueFoundry and licensed under the
**Apache License 2.0**. Individual skills remain under the licenses of their
**source repositories** — always check the original repo (linked via each entry's
`source.repo`) before using a skill.

---

<p align="center">
  Built by <a href="https://truefoundry.com">TrueFoundry</a> · Skills are portable across agents — write once, use everywhere.
</p>
