# FishCensus

An agent-based model (ABM) that simulates underwater visual census (UVC) surveys of fish populations. Uses a virtual ecologist approach to quantify how fish behaviour — diver avoidance, attraction, and schooling — affects the accuracy and precision of density estimates obtained by different survey methods.

Built in [NetLogo 7](https://ccl.northwestern.edu/netlogo/) following the [ODD protocol](docs/artifacts/odd/ODD_PROTOCOL.md) and [CoMSES Guides to Good Practice](https://www.comses.net/resources/guides-to-good-practice/).

## What it does

- Simulates a virtual diver conducting a UVC survey over a fish assemblage with known true density
- Supports three survey methods: **fixed-distance transect**, **timed transect**, and **stationary point count**, with an experimental **remote camera** method
- Fish move using a urge-based boids algorithm with drag-force physics; behaviours include schooling, diver avoidance/attraction, and bait scent following
- Outputs a CSV with per-replicate count, density estimate, and bias relative to the true density

A companion program, **FishCensus Species Creator**, provides a GUI for editing species parameter sets and exporting them as `.csv` files for use in the main model.

## How to use it

1. Open `code/FishCensus.nlogox` in NetLogo 7.0.3
2. Load a species file via the **Import Species** button (example species are included in `data/`)
3. Select a survey method and set parameters using the interface sliders and choosers
4. Click **Setup** then **Go** to run a simulation
5. Results are printed to the output area and exported to `results/`

For BehaviorSpace batch runs, open `code/FishCensus_dev.nlogox` — this is the development file that contains all experiment definitions.

## Dependencies

| Dependency | Version | Notes |
| --- | --- | --- |
| NetLogo | 7.0.3 | [ccl.northwestern.edu/netlogo](https://ccl.northwestern.edu/netlogo/) |
| `csv` extension | bundled | Imports species parameter files |
| `rnd` extension | bundled | Weighted random behaviour selection |
| `time` extension | bundled | Output file timestamping |
| `profiler` extension | bundled | Debug and performance profiling |

## Project structure

```text
.
├── LICENSE                          # MIT
├── CITATION.cff                     # How to cite this model
├── code/
│   ├── FishCensus.nlogox            # Public release model (no experiments)
│   ├── FishCensus_dev.nlogox        # Development model (includes BehaviorSpace experiments)
│   └── FishCensus Species Creator.nlogox
├── data/                            # Species parameter CSV files
├── results/                         # BehaviorSpace output CSVs and figures
└── docs/
    ├── artifacts/odd/               # ODD Protocol and appendices
    └── artifacts/validation/        # Validation and sensitivity analysis reports
```

## Citation

If you use this model, please cite:

> Pais, M.P., Cabral, H.N. 2018. Fish behaviour effects on the accuracy and precision of underwater visual census surveys. A virtual ecologist approach using an individual-based model. *PeerJ*. doi:[10.7717/peerj.5378](https://doi.org/10.7717/peerj.5378)

To cite the model software itself:

> Pais, M.P. 2026. FishCensus (version 3.0). CoMSES Computational Model Library. doi:[10.25937/k5nn-1r14](https://doi.org/10.25937/k5nn-1r14)

## License

[MIT](LICENSE) © 2016 Miguel Pessanha Pais
