# Session Outline (Schedule)

**PUBH 6854 / PUBH 4201 — Applied / Practical Computing in Health Data Science, Fall 2026**
MW, 12:45 – 2:00 p.m., SPH 300

Schedule is identical for the graduate (PUBH 6854) and undergraduate (PUBH 4201) sections; grading and deliverable differences are noted in [`GRADING_AND_POLICIES.md`](GRADING_AND_POLICIES.md).

---

## Module 1: Computing Environments, Reproducibility, and Data Wrangling

*Focus: Foundational computing workflows, reproducible environments, and practical data cleaning using both classical tools and generative AI assistance.*

### Week 1 — Computing Environments
- **Lecture:** Aug 24 · **Practical:** Aug 26
- Topics: Review of UNIX shell and scripting; remote development and analysis; overview of R and Python; coding environments (RStudio, JetBrains, VS Code)
- Learning objectives: Best practices for remote and local computing environments; essential tools for data scientists

### Week 2 — Reproducible Research Fundamentals
- **Lecture:** Aug 31 · **Practical:** Sep 2
- Topics: Dependency management; virtual environments (conda, uv, renv); containers (Docker, Singularity); containers in cloud computing; using generative AI for setup and troubleshooting
- Required readings: PCB Chapters 1, 4–6; [Introduction to renv](https://rstudio.github.io/renv/articles/renv.html)
- Deliverable: **Lab 1 — Reproducible Computing Setup**
- Learning objectives: Implement virtual environments; concepts of containerization and containerization tools

### Week 3 — Reproducible Research Notebooks
- **No class:** Sep 7 · **Lecture:** Sep 9
- Topics: Computational notebooks (Jupyter, Colab, R Markdown); using generative AI for setup and troubleshooting
- Required readings: DSF Chapter 1; [R for Reproducible Scientific Analysis](https://swcarpentry.github.io/r-novice-gapminder/)
- Deliverable: **Lab 2 — Analysis Notebook**
- Learning objectives: Create and compile a research notebook in R and Python

### Week 4 — Text Processing
- **Lecture:** Sep 14 · **Practical:** Sep 16
- Topics: Regular expressions for biological and health data; parsing semi-structured files (FASTA, metadata, logs); AI-assisted text extraction vs. regex-based methods
- Required readings: PCB Chapters 2–3; DSF Chapter 5
- Recommended readings: Python `re` documentation; prompting guides for structured data extraction
- Hands-on exercise: Extract structured fields using regex and AI tools
- Learning objectives: Clean real-world health data; compare classical and AI-based parsing approaches; identify failure modes in automated tools

### Week 5 — Data Wrangling
- **Lecture:** Sep 21 · **Lecture:** Sep 23
- Topics: Data frame ecosystems (R/tidyverse, pandas, polars); constructing samples × features × metadata tables; introduction to analytic data readiness
- Required readings: PCB Chapters 10–11; DSF Chapters 3–7
- Hands-on exercise: Build a small feature table from raw inputs
- Deliverable: **Lab 3 — Parsing Messy Health or Genomic Data**
- Learning objectives: Transform raw data into structured analytic formats; understand data readiness for modeling and inference

---

## Module 2: Programming, Databases, and Scientific Visualization

*Focus: Writing maintainable code, managing structured data, and communicating results through effective visualization.*

### Week 6 — Software Design
- **Lecture:** Sep 28 · **Practical:** Sep 30
- Topics: Software design paradigms (procedural, object-oriented, functional); modular programming; version control
- Required readings: [Python modules documentation](https://docs.python.org/3/tutorial/modules.html); [Git Tutorial](https://git-scm.com/docs/gittutorial)

### Week 7 — Advanced Software Design
- **Lecture:** Oct 5 · **Practical:** Oct 7
- Topics: Distributing software — packaging in R and Python; debugging workflows in software IDEs (PyCharm, VS Code); using generative AI assistance for developing, debugging, refactoring
- Required readings: [R Packages](https://r-pkgs.org/)
- Learning objectives: Build and debug code that is modular, reusable, and efficiently uses generative AI; fundamental concepts and key implementation details for R and Python packages
- **Final Project Proposals due Oct 7**

### Week 8 — Relational Databases
- **No class:** Oct 12 · **Lecture:** Oct 14
- Topics: Relational databases and SQL fundamentals; joining heterogeneous health datasets; genomic databases (UCSC, NCBI); AI-assisted query formulation and validation
- Required readings: PCB Chapters 14–15
- Hands-on exercise: Query and merge multiple data tables into one analytic dataset
- Learning objectives: Understand relational data concepts; integrate multiple data sources; prepare data for downstream analysis

### Week 9 — Advanced Data Architectures
- **Lecture:** Oct 19 · **Practical:** Oct 21
- Topics: Common data formats in HDS — flat file, hierarchical (H5), columnar (parquet/Apache Arrow); HDS-specific semi-structured formats (FASTQ, BED, GFF/GTF, VCF, BAM); accessing APIs (JSON)
- Deliverable: **Lab 4 — Database-Driven Feature Table**

### Week 10 — Workflow Management
- **Lecture:** Oct 26 · **Practical:** Oct 28
- Topics: Workflow fundamentals — inputs and outputs as dependencies; workflow management systems (Snakemake, Nextflow, Cromwell)
- Deliverable: **Lab 5 — Scalable Analysis Workflow**
- Learning objectives: Fundamentals of workflow management tools; implement loose collections of analysis scripts as reproducible workflows

---

## Module 3: Generative AI, Prompt Engineering, and Advanced Workflows

*Focus: Responsible use of generative AI, prompt engineering, and integration of AI into end-to-end health data science workflows.*

### Week 11 — Prompt Engineering and Generative AI
- **Lecture:** Nov 2 · **Practical:** Nov 4
- Topics: Prompt engineering fundamentals; task decomposition and prompt iteration; using Copilot, ChatGPT, Claude, and Gemini for analysis tasks
- Required readings: Instructor-provided notes on prompt engineering
- Recommended readings: Responsible AI guidelines; AI evaluation case studies
- Ongoing: Final Project

### Week 12 — Advanced Prompt Engineering and Generative AI
- **Lecture:** Nov 9 · **Practical:** Nov 11
- Topics: Integrating AI tools into development environments; hallucination detection and validation
- Required readings: Instructor-provided notes
- Ongoing: Final Project

### Week 13 — Human-in-the-Loop Analytics
- **Lecture:** Nov 16 · **Practical:** Nov 18
- Topics: Human-in-the-loop systems; integrating AI into analytical workflows; transparency and validation in AI-assisted analysis
- Hands-on exercise: Add validation checkpoints to an AI-assisted workflow
- Ongoing: Final Project
- Learning objectives: Design human-centered AI workflows; apply oversight to AI-assisted analysis

### Thanksgiving Break
- **No class:** Nov 23–27

### Week 14 — AI-Assisted Pipelines
- **Practical:** Nov 30 · **Practical:** Dec 2
- Ongoing: Final Project

### Week 15 — Capstone Integration Project
- **Practical:** Dec 7 · **Presentations:** Dec 9
- Students present final projects

---

*Source of truth: `AppliedComputing PUBH6854 Fall2026 Syllabus.docx` and `PracticalComputing PUBH4201 Fall2026 Syllabus.docx` (Dropbox `Teaching/Applied_Computing/Fall2026/`). If this schedule and the syllabus ever diverge, the syllabus governs.*
