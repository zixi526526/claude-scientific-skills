# Claude Scientific Skills (Curated Fork)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.md)
[![Skills](https://img.shields.io/badge/Skills-32-brightgreen.svg)](#whats-included)
[![Curated](https://img.shields.io/badge/Curated-Literature%20%7C%20scRNA--seq%20%7C%20Docs-blue.svg)](#whats-included)
[![Agent Skills](https://img.shields.io/badge/Standard-Agent_Skills-blueviolet.svg)](https://agentskills.io/)
[![Works with](https://img.shields.io/badge/Works_with-Cursor_|_Claude_Code_|_Codex-blue.svg)](#getting-started)
[![X](https://img.shields.io/badge/Follow_on_X-%40k__dense__ai-000000?logo=x)](https://x.com/k_dense_ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-K--Dense_Inc.-0A66C2?logo=linkedin)](https://www.linkedin.com/company/k-dense-inc)
[![YouTube](https://img.shields.io/badge/YouTube-K--Dense_Inc.-FF0000?logo=youtube)](https://www.youtube.com/@K-Dense-Inc)

A curated fork of [K-Dense](https://k-dense.ai)'s Claude Scientific Skills repository for the open [Agent Skills](https://agentskills.io/) standard. This fork keeps a focused set of **32 skills** for literature review, database and web search, single-cell analysis, scientific writing, visualization, document processing, and precision-medicine knowledge graph lookup across **Cursor, Claude Code, Codex, and more**.

Some retained folders, including `scientific-skills/docx`, `scientific-skills/pdf`, `scientific-skills/pptx`, and `scientific-skills/xlsx`, include their own folder-specific licenses that still apply.

<p align="center">
  <a href="https://k-dense.ai">
    <img src="docs/k-dense-web.gif" alt="K-Dense Web Demo" width="800"/>
  </a>
  <br/>
  <em>The demo above shows <a href="https://k-dense.ai">K-Dense Web</a> 閳?the hosted platform built on top of these skills. Claude Scientific Skills is the open-source skill collection; K-Dense Web is the full AI co-scientist platform with more power and zero setup.</em>
</p>

---

These skills enable your AI agent to seamlessly work with specialized scientific libraries, databases, and tools across multiple scientific domains. While the agent can use any Python package or API on its own, these explicitly defined skills provide curated documentation and examples that make it significantly stronger and more reliable for the workflows below:
- 棣冃?Bioinformatics & Genomics - Sequence analysis, single-cell RNA-seq, gene regulatory networks, variant annotation, phylogenetic analysis
- 棣冃?Cheminformatics & Drug Discovery - Molecular property prediction, virtual screening, ADMET analysis, molecular docking, lead optimization
- 棣冩暕 Proteomics & Mass Spectrometry - LC-MS/MS processing, peptide identification, spectral matching, protein quantification
- 棣冨綖 Clinical Research & Precision Medicine - Clinical trials, pharmacogenomics, variant interpretation, drug safety, clinical decision support, treatment planning
- 棣冾潵 Healthcare AI & Clinical ML - EHR analysis, physiological signal processing, medical imaging, clinical prediction models
- 棣冩煠閿?Medical Imaging & Digital Pathology - DICOM processing, whole slide image analysis, computational pathology, radiology workflows
- 棣冾樆 Machine Learning & AI - Deep learning, reinforcement learning, time series analysis, model interpretability, Bayesian methods
- 棣冩暛 Materials Science & Chemistry - Crystal structure analysis, phase diagrams, metabolic modeling, computational chemistry
- 棣冨 Physics & Astronomy - Astronomical data analysis, coordinate transformations, cosmological calculations, symbolic mathematics, physics computations
- 閳挎瑱绗?Engineering & Simulation - Discrete-event simulation, multi-objective optimization, metabolic engineering, systems modeling, process optimization
- 棣冩惓 Data Analysis & Visualization - Statistical analysis, network analysis, time series, publication-quality figures, large-scale data processing, EDA
- 棣冨 Geospatial Science & Remote Sensing - Satellite imagery processing, GIS analysis, spatial statistics, terrain analysis, machine learning for Earth observation
- 棣冃?Laboratory Automation - Liquid handling protocols, lab equipment control, workflow automation, LIMS integration
- 棣冩憥 Scientific Communication - Literature review, peer review, scientific writing, document processing, posters, slides, schematics, citation management
- 棣冩暕 Multi-omics & Systems Biology - Multi-modal data integration, pathway analysis, network biology, systems-level insights
- 棣冃?Protein Engineering & Design - Protein language models, structure prediction, sequence design, function annotation
- 棣冨笚 Research Methodology - Hypothesis generation, scientific brainstorming, critical thinking, grant writing, scholar evaluation

**Transform your AI coding agent into an 'AI Scientist' on your desktop!**

> 鐚?**If you find this repository useful**, please consider giving it a star! It helps others discover these tools and encourages us to continue maintaining and expanding this collection.

> 棣冨箑 **New to Claude Scientific Skills?** Watch our [Getting Started with Claude Scientific Skills](https://youtu.be/ZxbnDaD_FVg) video for a quick walkthrough.

---

## 棣冩憹 What's Included

This repository provides **32 curated skills** organized into the following areas:

- **9 literature, search, and citation skills** - BGPT Paper Search, bioRxiv, OpenAlex, PubMed, Google Scholar MCP, Perplexity Search, Research Lookup, Citation Management, and Literature Review
- **11 bioinformatics and single-cell skills** - AnnData, BioServices, Cellxgene Census, GEO, gget, NCBI Gene, PrimeKG, Scanpy, scVelo, scvi-tools, and STRING
- **7 writing, review, and presentation skills** - Humanizer, Peer Review, Scientific Brainstorming, Scientific Critical Thinking, Scientific Visualization, Scientific Writing, and Venue Templates
- **5 document processing skills** - DOCX, MarkItDown, PDF, PPTX, and XLSX

Each skill includes:
- 閴?Comprehensive documentation (`SKILL.md`)
- 閴?Practical code examples
- 閴?Use cases and best practices
- 閴?Integration guides
- 閴?Reference materials

---

## 棣冩惖 Table of Contents

- [What's Included](#whats-included)
- [Why Use This?](#why-use-this)
- [Getting Started](#getting-started)
- [Support Open Source](#-support-the-open-source-community)
- [Prerequisites](#prerequisites)
- [Quick Examples](#quick-examples)
- [Use Cases](#use-cases)
- [Available Skills](#available-skills)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
- [Support](#support)
- [Join Our Community](#join-our-community)
- [Citation](#citation)
- [License](#license)

---

## 棣冩畬 Why Use This?

### 閳?**Accelerate Your Research**
- **Save Days of Work** - Skip API documentation research and integration setup
- **Production-Ready Code** - Tested, validated examples following scientific best practices
- **Multi-Step Workflows** - Execute complex pipelines with a single prompt

### 棣冨箚 **Comprehensive Coverage**
- **32 Curated Skills** - Focused coverage for literature review, database lookup, web-grounded research, single-cell analysis, scientific writing, visualization, document workflows, and precision-medicine knowledge graph queries
- **Database & Search Coverage** - PubMed, GEO, OpenAlex, bioRxiv, Google Scholar MCP, Perplexity Search, Research Lookup, and multi-database access through BioServices and gget
- **Executable Workflows** - Scanpy QC, database query helpers, citation utilities, venue templates, and document-processing scripts for common research tasks

### 棣冩暋 **Easy Integration**
- **Simple Setup** - Copy skills to your skills directory and start working
- **Automatic Discovery** - Your agent automatically finds and uses relevant skills
- **Well Documented** - Each skill includes examples, use cases, and best practices

### 棣冨皞 **Maintained & Supported**
- **Regular Updates** - Continuously maintained and expanded by K-Dense team
- **Community Driven** - Open source with active community contributions
- **Enterprise Ready** - Commercial support available for advanced needs

---

## 棣冨箚 Getting Started

Claude Scientific Skills follows the open [Agent Skills](https://agentskills.io/) standard. Simply copy the skill folders into your skills directory and your AI agent will automatically discover and use them.

### Step 1: Clone the Repository

```bash
git clone https://github.com/K-Dense-AI/claude-scientific-skills.git
```

### Step 2: Copy Skills to Your Skills Directory

Copy the individual skill folders from `scientific-skills/` to one of the supported skill directories below. You can install skills **globally** (available across all projects) or **per-project** (available only in that project).

**Global installation** (recommended 閳?skills available everywhere):

| Tool | Directory |
|------|-----------|
| Cursor | `~/.cursor/skills/` |
| Claude Code | `~/.claude/skills/` |
| Codex | `~/.codex/skills/` |
| Gemini CLI | `~/.gemini/skills/` |

**Project-level installation** (skills scoped to a single project):

| Tool | Directory |
|------|-----------|
| Cursor | `.cursor/skills/` (in your project root) |
| Claude Code | `.claude/skills/` (in your project root) |
| Codex | `.codex/skills/` (in your project root) |
| Gemini CLI | `.gemini/skills/` (in your project root) |

> **Note:** Cursor also reads from `.claude/skills/`, `.codex/skills/`, and `.gemini/skills/` directories, and vice versa, so skills are cross-compatible between tools.

**Example 閳?global install for Cursor:**
```bash
cp -r claude-scientific-skills/scientific-skills/* ~/.cursor/skills/
```

**Example 閳?global install for Claude Code:**
```bash
cp -r claude-scientific-skills/scientific-skills/* ~/.claude/skills/
```

**Example 閳?global install for Gemini CLI:**
```bash
cp -r claude-scientific-skills/scientific-skills/* ~/.gemini/skills/
```

**Example 閳?project-level install:**
```bash
mkdir -p .cursor/skills
cp -r /path/to/claude-scientific-skills/scientific-skills/* .cursor/skills/
```

**That's it!** Your AI agent will automatically discover the skills and use them when relevant to your scientific tasks. You can also invoke any skill manually by mentioning the skill name in your prompt.

---

## 閴傘倧绗?Support the Open Source Community

Claude Scientific Skills is powered by **50+ incredible open source projects** maintained by dedicated developers and research communities worldwide. Projects like Biopython, Scanpy, RDKit, scikit-learn, PyTorch Lightning, and many others form the foundation of these skills.

**If you find value in this repository, please consider supporting the projects that make it possible:**

- 鐚?**Star their repositories** on GitHub
- 棣冩尩 **Sponsor maintainers** via GitHub Sponsors or NumFOCUS
- 棣冩憫 **Cite projects** in your publications
- 棣冩崌 **Contribute** code, docs, or bug reports

棣冩啝 **[View the full list of projects to support](docs/open-source-sponsors.md)**

---

## 閳挎瑱绗?Prerequisites

- **Python**: 3.9+ (3.12+ recommended for best compatibility)
- **uv**: Python package manager (required for installing skill dependencies)
- **Client**: Any agent that supports the [Agent Skills](https://agentskills.io/) standard (Cursor, Claude Code, Gemini CLI, Codex, etc.)
- **System**: macOS, Linux, or Windows with WSL2
- **Dependencies**: Automatically handled by individual skills (check `SKILL.md` files for specific requirements)

### Installing uv

The skills use `uv` as the package manager for installing Python dependencies. Install it using the instructions for your operating system:

**macOS and Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Alternative (via pip):**
```bash
pip install uv
```

After installation, verify it works by running:
```bash
uv --version
```

For more installation options and details, visit the [official uv documentation](https://docs.astral.sh/uv/).

---

## 棣冩寱 Quick Examples

Once you've installed the skills, you can ask your AI agent to execute complex multi-step scientific workflows. Here are some example prompts:

### 棣冃?Drug Discovery Pipeline
**Goal**: Find novel EGFR inhibitors for lung cancer treatment

**Prompt**:
```
Use available skills you have access to whenever possible. Query ChEMBL for EGFR inhibitors (IC50 < 50nM), analyze structure-activity relationships 
with RDKit, generate improved analogs with datamol, perform virtual screening with DiffDock 
against AlphaFold EGFR structure, search PubMed for resistance mechanisms, check COSMIC for 
mutations, and create visualizations and a comprehensive report.
```

**Skills Used**: ChEMBL, RDKit, datamol, DiffDock, AlphaFold DB, PubMed, COSMIC, scientific visualization

*Need cloud GPUs and a publication-ready report at the end? [Run this on K-Dense Web free.](https://k-dense.ai)*

---

### 棣冩暕 Single-Cell RNA-seq Analysis
**Goal**: Comprehensive analysis of 10X Genomics data with public data integration

**Prompt**:
```
Use available skills you have access to whenever possible. Load 10X dataset with Scanpy, perform QC and doublet removal, integrate with Cellxgene 
Census data, identify cell types using NCBI Gene markers, run differential expression with 
PyDESeq2, infer gene regulatory networks with Arboreto, enrich pathways via Reactome/KEGG, 
and identify therapeutic targets with Open Targets.
```

**Skills Used**: Scanpy, Cellxgene Census, NCBI Gene, PyDESeq2, Arboreto, Reactome, KEGG, Open Targets

*Want zero-setup cloud execution and shareable outputs? [Try K-Dense Web free.](https://k-dense.ai)*

---

### 棣冃?Multi-Omics Biomarker Discovery
**Goal**: Integrate RNA-seq, proteomics, and metabolomics to predict patient outcomes

**Prompt**:
```
Use available skills you have access to whenever possible. Analyze RNA-seq with PyDESeq2, process mass spec with pyOpenMS, integrate metabolites from 
HMDB/Metabolomics Workbench, map proteins to pathways (UniProt/KEGG), find interactions via 
STRING, correlate omics layers with statsmodels, build predictive model with scikit-learn, 
and search ClinicalTrials.gov for relevant trials.
```

**Skills Used**: PyDESeq2, pyOpenMS, HMDB, Metabolomics Workbench, UniProt, KEGG, STRING, statsmodels, scikit-learn, ClinicalTrials.gov

*This pipeline is heavy on compute. [Run it on K-Dense Web with cloud GPUs, free to start.](https://k-dense.ai)*

---

### 棣冨箚 Virtual Screening Campaign
**Goal**: Discover allosteric modulators for protein-protein interactions

**Prompt**:
```
Use available skills you have access to whenever possible. Retrieve AlphaFold structures, identify interaction interface with BioPython, search ZINC 
for allosteric candidates (MW 300-500, logP 2-4), filter with RDKit, dock with DiffDock, 
rank with DeepChem, check PubChem suppliers, search USPTO patents, and optimize leads with 
MedChem/molfeat.
```

**Skills Used**: AlphaFold DB, BioPython, ZINC, RDKit, DiffDock, DeepChem, PubChem, USPTO, MedChem, molfeat

*Skip the local GPU bottleneck. [Run virtual screening on K-Dense Web free.](https://k-dense.ai)*

---

### 棣冨綖 Clinical Variant Interpretation
**Goal**: Analyze VCF file for hereditary cancer risk assessment

**Prompt**:
```
Use available skills you have access to whenever possible. Parse VCF with pysam, annotate variants with Ensembl VEP, query ClinVar for pathogenicity, 
check COSMIC for cancer mutations, retrieve gene info from NCBI Gene, analyze protein impact 
with UniProt, search PubMed for case reports, check ClinPGx for pharmacogenomics, generate 
clinical report with document processing tools, and find matching trials on ClinicalTrials.gov.
```

**Skills Used**: pysam, Ensembl, ClinVar, COSMIC, NCBI Gene, UniProt, PubMed, ClinPGx, Document Skills, ClinicalTrials.gov

*Need a polished clinical report at the end, not just code? [K-Dense Web delivers publication-ready outputs. Try it free.](https://k-dense.ai)*

---

### 棣冨 Systems Biology Network Analysis
**Goal**: Analyze gene regulatory networks from RNA-seq data

**Prompt**:
```
Use available skills you have access to whenever possible. Query NCBI Gene for annotations, retrieve sequences from UniProt, identify interactions via 
STRING, map to Reactome/KEGG pathways, analyze topology with Torch Geometric, reconstruct 
GRNs with Arboreto, assess druggability with Open Targets, model with PyMC, visualize 
networks, and search GEO for similar patterns.
```

**Skills Used**: NCBI Gene, UniProt, STRING, Reactome, KEGG, Torch Geometric, Arboreto, Open Targets, PyMC, GEO

*Want end-to-end pipelines with shareable outputs and no setup? [Try K-Dense Web free.](https://k-dense.ai)*

> 棣冩憠 **Want more examples?** Check out [docs/examples.md](docs/examples.md) for comprehensive workflow examples and detailed use cases across all scientific domains.

---

## 棣冩畬 Want to Skip the Setup and Just Do the Science?

**Recognize any of these?**

- You spent more time configuring environments than running analyses
- Your workflow needs a GPU your local machine does not have
- You need a shareable, publication-ready figure or report, not just a script
- You want to run a complex multi-step pipeline right now, without reading package docs first

If so, **[K-Dense Web](https://k-dense.ai)** was built for you. It is the full AI co-scientist platform: everything in this repo plus cloud GPUs, 200+ skills, and outputs you can drop directly into a paper or presentation. Zero setup required.

| Feature | This Repo | K-Dense Web |
|---------|-----------|-------------|
| Scientific Skills | 32 skills | **200+ skills** (exclusive access) |
| Setup | Manual installation | **Zero setup, works instantly** |
| Compute | Your machine | **Cloud GPUs and HPC included** |
| Workflows | Prompt and code | **End-to-end research pipelines** |
| Outputs | Code and analysis | **Publication-ready figures, reports, and papers** |
| Integrations | Local tools | **Lab systems, ELNs, and cloud storage** |

> *"K-Dense Web took me from raw sequencing data to a draft figure in one afternoon. What used to take three days of environment setup and scripting now just works."*
> **Computational biologist, drug discovery**

> ### 棣冩尩 $50 in free credits, no credit card required
> Start running real scientific workflows in minutes.
>
> **[Try K-Dense Web free](https://k-dense.ai)**

*[k-dense.ai](https://k-dense.ai) | [Read the full comparison](https://k-dense.ai/blog/k-dense-web-vs-claude-scientific-skills)*

---

## 棣冩暕 Use Cases

### 棣冃?Drug Discovery & Medicinal Chemistry
- **Virtual Screening**: Screen millions of compounds from PubChem/ZINC against protein targets
- **Lead Optimization**: Analyze structure-activity relationships with RDKit, generate analogs with datamol
- **ADMET Prediction**: Predict absorption, distribution, metabolism, excretion, and toxicity with DeepChem
- **Molecular Docking**: Predict binding poses and affinities with DiffDock
- **Bioactivity Mining**: Query ChEMBL for known inhibitors and analyze SAR patterns

### 棣冃?Bioinformatics & Genomics
- **Sequence Analysis**: Process DNA/RNA/protein sequences with BioPython and pysam
- **Single-Cell Analysis**: Analyze 10X Genomics data with Scanpy, identify cell types, infer GRNs with Arboreto
- **Variant Annotation**: Annotate VCF files with Ensembl VEP, query ClinVar for pathogenicity
- **Variant Database Management**: Build scalable VCF databases with TileDB-VCF for incremental sample addition, efficient population-scale queries, and compressed storage of genomic variant data
- **Gene Discovery**: Query NCBI Gene, UniProt, and Ensembl for comprehensive gene information
- **Network Analysis**: Identify protein-protein interactions via STRING, map to pathways (KEGG, Reactome)

### 棣冨綖 Clinical Research & Precision Medicine
- **Clinical Trials**: Search ClinicalTrials.gov for relevant studies, analyze eligibility criteria
- **Variant Interpretation**: Annotate variants with ClinVar, COSMIC, and ClinPGx for pharmacogenomics
- **Drug Safety**: Query FDA databases for adverse events, drug interactions, and recalls
- **Precision Therapeutics**: Match patient variants to targeted therapies and clinical trials

### 棣冩暕 Multi-Omics & Systems Biology
- **Multi-Omics Integration**: Combine RNA-seq, proteomics, and metabolomics data
- **Pathway Analysis**: Enrich differentially expressed genes in KEGG/Reactome pathways
- **Network Biology**: Reconstruct gene regulatory networks, identify hub genes
- **Biomarker Discovery**: Integrate multi-omics layers to predict patient outcomes

### 棣冩惓 Data Analysis & Visualization
- **Statistical Analysis**: Perform hypothesis testing, power analysis, and experimental design
- **Publication Figures**: Create publication-quality visualizations with matplotlib and seaborn
- **Network Visualization**: Visualize biological networks with NetworkX
- **Report Generation**: Generate comprehensive PDF reports with Document Skills

### 棣冃?Laboratory Automation
- **Protocol Design**: Create Opentrons protocols for automated liquid handling
- **LIMS Integration**: Integrate with Benchling and LabArchives for data management
- **Workflow Automation**: Automate multi-step laboratory workflows

---

## 棣冩憥 Available Skills

This curated fork currently ships **32 skills**. The list below matches the local `scientific-skills/` directory and `.claude-plugin/marketplace.json`.

### Skill Categories

#### 棣冩憥 **Literature, Search & Citation** (9 skills)
- `bgpt-paper-search`
- `biorxiv-database`
- `citation-management`
- `google-scholar-mcp`
- `literature-review`
- `openalex-database`
- `perplexity-search`
- `pubmed-database`
- `research-lookup`

#### 棣冃?**Bioinformatics & Single-Cell** (11 skills)
- `anndata`
- `bioservices`
- `cellxgene-census`
- `gene-database`
- `geo-database`
- `gget`
- `primekg`
- `scanpy`
- `scvelo`
- `scvi-tools`
- `string-database`

#### 棣冩憹 **Writing, Review & Visualization** (7 skills)
- `humanizer`
- `peer-review`
- `scientific-brainstorming`
- `scientific-critical-thinking`
- `scientific-visualization`
- `scientific-writing`
- `venue-templates`

#### 棣冩惓 **Document Processing** (5 skills)
- `docx`
- `markitdown`
- `pdf`
- `pptx`
- `xlsx`

---

## 棣冾檪 Contributing

We welcome contributions to expand and improve this scientific skills repository!

### Ways to Contribute

閴?**Add New Skills**
- Create skills for additional scientific packages or databases
- Add integrations for scientific platforms and tools

棣冩憥 **Improve Existing Skills**
- Enhance documentation with more examples and use cases
- Add new workflows and reference materials
- Improve code examples and scripts
- Fix bugs or update outdated information

棣冩偘 **Report Issues**
- Submit bug reports with detailed reproduction steps
- Suggest improvements or new features

### How to Contribute

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-skill`)
3. **Follow** the existing directory structure and documentation patterns
4. **Ensure** all new skills include comprehensive `SKILL.md` files
5. **Test** your examples and workflows thoroughly
6. **Commit** your changes (`git commit -m 'Add amazing skill'`)
7. **Push** to your branch (`git push origin feature/amazing-skill`)
8. **Submit** a pull request with a clear description of your changes

### Contribution Guidelines

閴?**Adhere to the [Agent Skills Specification](https://agentskills.io/specification)** 閳?Every skill must follow the official spec (valid `SKILL.md` frontmatter, naming conventions, directory structure)  
閴?Maintain consistency with existing skill documentation format  
閴?Ensure all code examples are tested and functional  
閴?Follow scientific best practices in examples and workflows  
閴?Update relevant documentation when adding new capabilities  
閴?Provide clear comments and docstrings in code  
閴?Include references to official documentation

### Security Scanning

All skills in this repository are security-scanned using [Cisco AI Defense Skill Scanner](https://github.com/cisco-ai-defense/skill-scanner), an open-source tool that detects prompt injection, data exfiltration, and malicious code patterns in Agent Skills.

If you are contributing a new skill, we recommend running the scanner locally before submitting a pull request:

```bash
uv pip install cisco-ai-skill-scanner
skill-scanner scan /path/to/your/skill --use-behavioral
```

> **Note:** A clean scan result reduces noise in review, but does not guarantee a skill is free of all risk. Contributed skills are also reviewed manually before merging.

### Recognition

Contributors are recognized in our community and may be featured in:
- Repository contributors list
- Special mentions in release notes
- K-Dense community highlights

Your contributions help make scientific computing more accessible and enable researchers to leverage AI tools more effectively!

### Support Open Source

This project builds on 50+ amazing open source projects. If you find value in these skills, please consider [supporting the projects we depend on](docs/open-source-sponsors.md).

---

## 棣冩暋 Troubleshooting

### Common Issues

**Problem: Skills not loading**
- Verify skill folders are in the correct directory (see [Getting Started](#getting-started))
- Each skill folder must contain a `SKILL.md` file
- Restart your agent/IDE after copying skills
- In Cursor, check Settings 閳?Rules to confirm skills are discovered

**Problem: Missing Python dependencies**
- Solution: Check the specific `SKILL.md` file for required packages
- Install dependencies: `uv pip install package-name`

**Problem: API rate limits**
- Solution: Many databases have rate limits. Review the specific database documentation
- Consider implementing caching or batch requests

**Problem: Authentication errors**
- Solution: Some services require API keys. Check the `SKILL.md` for authentication setup
- Verify your credentials and permissions

**Problem: Outdated examples**
- Solution: Report the issue via GitHub Issues
- Check the official package documentation for updated syntax

---

## 閴?FAQ

### General Questions

**Q: Is this free to use?**  
A: Yes! This repository is MIT licensed. However, each individual skill has its own license specified in the `license` metadata field within its `SKILL.md` file閳ユ攤e sure to review and comply with those terms.

**Q: Why are all skills grouped together instead of separate packages?**  
A: We believe good science in the age of AI is inherently interdisciplinary. Bundling all skills together makes it trivial for you (and your agent) to bridge across fields閳ユ攨.g., combining genomics, cheminformatics, clinical data, and machine learning in one workflow閳ユ敋ithout worrying about which individual skills to install or wire together.

**Q: Can I use this for commercial projects?**  
A: The repository itself is MIT licensed, which allows commercial use. However, individual skills may have different licenses閳ユ攦heck the `license` field in each skill's `SKILL.md` file to ensure compliance with your intended use.

**Q: Do all skills have the same license?**  
A: No. Each skill has its own license specified in the `license` metadata field within its `SKILL.md` file. These licenses may differ from the repository's MIT License. Users are responsible for reviewing and adhering to the license terms of each individual skill they use.

**Q: How often is this updated?**  
A: We regularly update skills to reflect the latest versions of packages and APIs. Major updates are announced in release notes.

**Q: Can I use this with other AI models?**  
A: The skills follow the open [Agent Skills](https://agentskills.io/) standard and work with any compatible agent, including Cursor, Claude Code, and Codex.

### Installation & Setup

**Q: Do I need all the Python packages installed?**  
A: No! Only install the packages you need. Each skill specifies its requirements in its `SKILL.md` file.

**Q: What if a skill doesn't work?**  
A: First check the [Troubleshooting](#troubleshooting) section. If the issue persists, file an issue on GitHub with detailed reproduction steps.

**Q: Do the skills work offline?**  
A: Database skills require internet access to query APIs. Package skills work offline once Python dependencies are installed.

### Contributing

**Q: Can I contribute my own skills?**  
A: Absolutely! We welcome contributions. See the [Contributing](#contributing) section for guidelines and best practices.

**Q: How do I report bugs or suggest features?**  
A: Open an issue on GitHub with a clear description. For bugs, include reproduction steps and expected vs actual behavior.

---

## 棣冩尠 Support

Need help? Here's how to get support:

- 棣冩憠 **Documentation**: Check the relevant `SKILL.md` and `references/` folders
- 棣冩偘 **Bug Reports**: [Open an issue](https://github.com/K-Dense-AI/claude-scientific-skills/issues)
- 棣冩寱 **Feature Requests**: [Submit a feature request](https://github.com/K-Dense-AI/claude-scientific-skills/issues/new)
- 棣冩崍 **Enterprise Support**: Contact [K-Dense](https://k-dense.ai/) for commercial support
- 棣冨 **Community**: [Join our Slack](https://join.slack.com/t/k-densecommunity/shared_invite/zt-3iajtyls1-EwmkwIZk0g_o74311Tkf5g)

---

## 棣冨竴 Join Our Community!

**We'd love to have you join us!** 棣冩畬

Connect with other scientists, researchers, and AI enthusiasts using AI agents for scientific computing. Share your discoveries, ask questions, get help with your projects, and collaborate with the community!

棣冨皞 **[Join our Slack Community](https://join.slack.com/t/k-densecommunity/shared_invite/zt-3iajtyls1-EwmkwIZk0g_o74311Tkf5g)** 棣冨皞

Whether you're just getting started or you're a power user, our community is here to support you. We share tips, troubleshoot issues together, showcase cool projects, and discuss the latest developments in AI-powered scientific research.

**See you there!** 棣冩尠

---

## 棣冩憠 Citation

If you use Claude Scientific Skills in your research or project, please cite it as:

### BibTeX
```bibtex
@software{claude_scientific_skills_2026,
  author = {{K-Dense Inc.}},
  title = {Claude Scientific Skills: A Comprehensive Collection of Scientific Tools for Claude AI},
  year = {2026},
  url = {https://github.com/K-Dense-AI/claude-scientific-skills},
  note = {skills covering databases, packages, integrations, and analysis tools}
}
```

### APA
```
K-Dense Inc. (2026). Claude Scientific Skills: A comprehensive collection of scientific tools for Claude AI [Computer software]. https://github.com/K-Dense-AI/claude-scientific-skills
```

### MLA
```
K-Dense Inc. Claude Scientific Skills: A Comprehensive Collection of Scientific Tools for Claude AI. 2026, github.com/K-Dense-AI/claude-scientific-skills.
```

### Plain Text
```
Claude Scientific Skills by K-Dense Inc. (2026)
Available at: https://github.com/K-Dense-AI/claude-scientific-skills
```

We appreciate acknowledgment in publications, presentations, or projects that benefit from these skills!

---

## 棣冩惈 License

This project is licensed under the **MIT License**.

**Copyright 婕?2026 K-Dense Inc.** ([k-dense.ai](https://k-dense.ai/))

### Key Points:
- 閴?**Free for any use** (commercial and noncommercial)
- 閴?**Open source** - modify, distribute, and use freely
- 閴?**Permissive** - minimal restrictions on reuse
- 閳跨媴绗?**No warranty** - provided "as is" without warranty of any kind

See [LICENSE.md](LICENSE.md) for full terms.

### Individual Skill Licenses

> 閳跨媴绗?**Important**: Each skill has its own license specified in the `license` metadata field within its `SKILL.md` file. These licenses may differ from the repository's MIT License and may include additional terms or restrictions. **Users are responsible for reviewing and adhering to the license terms of each individual skill they use.**

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=K-Dense-AI/claude-scientific-skills&type=date&legend=top-left)](https://www.star-history.com/#K-Dense-AI/claude-scientific-skills&type=date&legend=top-left)


