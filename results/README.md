# Results

This directory holds BehaviorSpace output CSVs, sensitivity analysis outputs, and figures generated from `code/FishCensus_dev.nlogox`. Output files are not committed to git (see `.gitignore`) — they are either regenerated locally or downloaded from the published data archive.

## Published output data

The output data from the original validation and sensitivity analyses published in Pais & Cabral (2018) is archived as a supplementary file:

**Pais, M.P., Cabral, H.N. 2018.** Fish behaviour effects on the accuracy and precision of underwater visual census surveys. *PeerJ*. doi:[10.7717/peerj.5378](https://doi.org/10.7717/peerj.5378)

**Supplementary data (supp-6):** <https://doi.org/10.7717/peerj.5378/supp-6>

To populate this directory with the published outputs, download `supp-6` from the link above and place it here as `results/published/`.

## Regenerating outputs locally

All BehaviorSpace experiments used in the published analyses are stored in `code/FishCensus_dev.nlogox`. To regenerate:

1. Open `code/FishCensus_dev.nlogox` in NetLogo 7.0.3
2. Go to **Tools → BehaviorSpace**
3. Select the relevant experiment and run it
4. Save output CSVs to this directory

## Directory conventions

```text
results/
├── published/     # Downloaded outputs from the published supplementary data
└── [experiment]/  # Locally generated BehaviorSpace outputs, one folder per experiment
```

Do not commit files larger than 100 MB — archive large outputs on Zenodo or Dryad and link here instead.
