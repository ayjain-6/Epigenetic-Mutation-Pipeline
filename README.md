# Epigenetic-Mutation-Pipeline: Multi-Database Chromatin Integrator

[![CI/CD Pipeline](https://github.com/ayjain-6/Epigenetic-Mutation-Pipeline/actions/workflows/test.yml/badge.svg)](https://github.com/ayjain-6/Epigenetic-Mutation-Pipeline/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An automated, config-driven bioinformatics pipeline designed for multi-database precision oncology integration across the **H3.3 / ATRX / DAXX chromatin remodeling axis** (implicated in pediatric high-grade gliomas, osteosarcomas, and pancreatic neuroendocrine tumors).

---

## Integrated Databases & Framework
* **AlphaMissense (Google DeepMind):** Evaluates structural missense pathogenicity to predict protein destabilization.
* **gnomAD v4:** Filters out common population germline polymorphisms (Minor Allele Frequency threshold <= 0.001) to isolate rare somatic/driver mutations.
* **COSMIC v101:** Aggregates tumor sample recurrence counts to flag recurrent cancer hotspots.
* **DepMap (Achilles):** Integrates CRISPR knockout dependency Z-scores to identify selective cancer cell line vulnerabilities and synthetic lethality targets.
* **ClinVar:** Incorporates clinical assertions and interpretive consensus.

---

## Reproducible Output Summary (`results/cross_db_summary_daxx_expanded.csv`)
The pipeline ingests raw variant sets, filters population noise, and outputs a version-controlled multi-omics matrix containing over 100 high-confidence variants across `H3F3A`, `ATRX`, and `DAXX`.

---

## Quick Start
```bash
# Clone Repository
git clone [https://github.com/ayjain-6/Epigenetic-Mutation-Pipeline.git](https://github.com/ayjain-6/Epigenetic-Mutation-Pipeline.git)
cd Epigenetic-Mutation-Pipeline

# Install Dependencies
pip install -r requirements.txt

# Run Multi-Database Integration Engine
python src/integration_engine.py
```
