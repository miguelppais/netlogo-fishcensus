# Multiagent NetLogo Template

A foundational workspace for complex Agent-Based Modeling using a Multiagent LLM workflow, following the [CoMSES Guides to Good Practice](https://www.comses.net/resources/guides-to-good-practice/).

## Getting Started

1. **License** — Fill in `LICENSE` with your name and year. Use MIT, BSD, or Apache for software ([choosealicense.com](https://choosealicense.com)). Data and manuscripts should use CC-BY or CC-0.

2. **Research** — Use the **Scientist** to review literature and document behavioral rules in `docs/research/`.

3. **ODD Protocol** — Use the **Architect** to draft the ODD Protocol in `docs/artifacts/odd/` using the provided template.

4. **Data Management** — Document all empirical inputs and their provenance in `data/README.md` before using them in the model. Preserve raw data in `data/raw/` (treat as read-only).

5. **Implementation** — Use the **NetLogo Engineer** and **UI Designer** to write `.nlogox` code in `code/`. Any logic change **must** be synced back to the ODD and the model's Info Tab.

6. **Validation & Sensitivity Analysis** — Use the **Data Scientist** to run BehaviorSpace sweeps, conduct one-at-a-time and global sensitivity analyses, and validate emergent patterns against empirical data. Document all results in `docs/artifacts/validation/` and store output files in `results/`.

7. **Archive & Publish** — When the model is ready, publish it to the [CoMSES Computational Model Library](https://www.comses.net/codebases/) or [Zenodo](https://zenodo.org/) to obtain a DOI. Update `CITATION.cff` with the DOI and release URL. Archive input datasets separately in a data repository (e.g., [Dryad](https://datadryad.org/)).

For agent roles, workflow rules, and skill definitions, see [AGENTS.md](AGENTS.md).

## Dependencies

| Dependency | Version | Notes |
| --- | --- | --- |
| NetLogo | 7.0.3 | [ccl.northwestern.edu/netlogo](https://ccl.northwestern.edu/netlogo/) |
| `csv` extension | bundled | Imports species parameter CSV files |
| `rnd` extension | bundled | Weighted random behaviour selection |
| `time` extension | bundled | Output file timestamping |
| `profiler` extension | bundled | Debug and performance profiling |

## Project Structure

```text
.
├── LICENSE                          # Open source license
├── CITATION.cff                     # How to cite this model
├── code/                            # .nlogox model files and .nls scripts
├── data/
│   ├── README.md                    # Data provenance registry
│   ├── raw/                         # Original unmodified input data (read-only)
│   └── processed/                   # Cleaned inputs ready for the model
├── results/                         # BehaviorSpace output CSVs and analysis figures
├── docs/
│   └── artifacts/
│       ├── odd/                     # ODD Protocol documents
│       ├── validation/              # Validation and sensitivity analysis reports
│       ├── prd/                     # Product Requirements Documents
│       ├── backlog/                 # Epics and User Stories (task pool)
│       ├── adr/                     # Architecture Decision Records
│       ├── specs/                   # Technical specifications
│       └── learnings/               # Compound capture of reusable engineering takeaways
│   ├── research/                    # Literature reviews and behavioral reports
│   └── brainstorms/                 # Unstructured ideas, feature concepts, and sprint planning
└── References/
    └── models/                      # Legacy .nlogo reference models and snippets
```
