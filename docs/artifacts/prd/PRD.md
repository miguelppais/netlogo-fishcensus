# Product Requirements Document — FishCensus

**Version:** 3.0
**Status:** Approved (retroactive)
**Date:** 2026-06-12
**Author:** Miguel Pessanha Pais
**Target Audience:** Marine ecologists, fisheries scientists, UVC survey practitioners

---

## 1. Research Question / Phenomenon

**Primary question:** How do fish behavioural traits — particularly diver avoidance, diver attraction, schooling, and cryptic behaviour — affect the accuracy and precision of population density estimates produced by underwater visual census (UVC) surveys?

**Secondary question:** Can a single modelling framework quantify the sampling bias introduced by non-instantaneous observation across four operationally distinct survey methods, and thereby provide correction factors applicable to real field data?

UVC methods are used worldwide to monitor shallow marine and freshwater habitats for conservation and fisheries management. Despite their widespread use, known sources of bias (reactive fish behaviour, observer saturation, limited visibility, non-instantaneous sampling) remain impossible to quantify directly from field data because the true population density is never known in the field. FishCensus solves this by operating as a **virtual ecologist**: the simulated survey is conducted over a population of known true density, making bias directly observable and quantifiable.

The model builds upon two predecessor models — the Reefex model (Watson et al., 1995) and the AnimDens model (Ward-Paige et al., 2010) — with substantially greater spatial and temporal resolution, a more realistic urge-based fish movement model with drag-force physics (Reynolds boids framework), and the addition of a remote camera survey method.

---

## 2. Acceptance Criteria

The model is considered valid and fit for publication when all of the following are satisfied:

| # | Criterion | How to verify |
|---|---|---|
| AC-1 | For a species with avoidance weight = 0, estimated density converges on true density as sample replicates increase | BehaviorSpace sweep over replicate count; SE of estimate decreases monotonically |
| AC-2 | Fish with diver.avoidance.w > 0 produce underestimates; fish with diver.avoidance.w < 0 (attraction) produce overestimates | Directional bias confirmed across parameter sweep |
| AC-3 | Schooling species exhibit higher variance in density estimates than non-schooling species at equal density | Coefficient of variation comparison in BehaviorSpace output |
| AC-4 | Bias due to non-instantaneous sampling increases with fish speed relative to diver speed | Positive correlation confirmed in OAT sensitivity sweep |
| AC-5 | Output from fixed-distance transect, timed transect, stationary point count, and remote camera methods are each logically consistent with their respective sampling formulae | Manual verification and extreme-parameter tests |
| AC-6 | Results from the published paper (Pais & Cabral, 2018, doi:10.7717/peerj.5378) are reproducible using the species parameter CSV files and BehaviorSpace experiments included in `code/FishCensus_dev.nlogox` | Numerical match within stochastic tolerance |
| AC-7 | Info Tab in `code/FishCensus.nlogox` is identical to `README.md` | Diff check confirms zero discrepancy |
| AC-8 | ODD protocol in `docs/artifacts/odd/ODD_PROTOCOL.md` covers all seven ODD elements (Purpose, Entities, Process, Design concepts, Initialization, Input, Sub-models) | Section-by-section checklist in validation report |

---

## 3. Survey Methods in Scope

All four methods simulate a single survey replicate. The virtual diver (or camera) operates over a fish assemblage with known true density so that bias is directly computable.

### 3.1 Fixed-Distance Transect
- Diver swims a straight path of fixed length at a pre-defined constant speed.
- Fish are counted within a belt of defined width on either side of the diver's path.
- Finishing condition: diver reaches the target distance (y-coordinate check).
- Key parameters: `transect-distance` (m), `transect-width` (m), `diver-speed` (m/min).

### 3.2 Timed Transect
- Same geometry and counting rules as the fixed-distance transect.
- Finishing condition: elapsed model time reaches a user-defined duration.
- Key parameters: `transect-time` (min), `transect-width` (m), `diver-speed` (m/min).

### 3.3 Stationary Point Count (SPC)
- Diver remains at a fixed position and rotates clockwise at a constant angular speed.
- Fish are counted within a cylinder of defined radius.
- Field of view is set to 160 degrees for this method (vs 180 for transects).
- Key parameters: `point-count-radius` (m), `point-count-time` (min), `turning-speed` (deg/s).

### 3.4 Remote Cameras (with Bait Scent)
- A static camera is deployed at a fixed location; no diver is present.
- A chemical scent attractant diffuses outward from the camera following a gradient.
- Fish detect and follow the scent gradient, generating approach behaviour not present in diver-based methods.
- Fish are counted within a defined detection radius of the camera.
- Key parameters: scent diffusion rate, detection radius, bait attraction weight in fish urge system.

---

## 4. Out of Scope

The following are **explicitly not modelled** in FishCensus v3.0:

| Excluded element | Rationale |
|---|---|
| Depth / 3D space | Depth is assumed constant; model is 2D to reduce complexity and computation time |
| Variable water visibility | Maximum visibility is fixed at 6 m and constant in space and time |
| Predator–prey trophic dynamics | Fish predation interactions are represented only as a behavioural urge (prey-chasing weight), not as a full trophic model |
| Population dynamics (birth, death, growth) | Each run simulates a single survey event; no demographic processes occur within a run |
| Multi-diver counting competition | The buddy diver triggers fish avoidance but does not count fish; only one virtual ecologist counts |
| Environmental heterogeneity | The landscape grid has no variables affecting agents; patches are inert |
| Time-varying environmental drivers | No tidal, current, or light cycle processes |
| Genetic or evolutionary processes | Fish attributes are fixed within a run and between runs for a given species CSV |
| Actual species identification error | The model assumes perfect species identification within ID distance; only detectability (visibility) is uncertain |

---

## 5. Key Species Parameters

Fish species are defined by a set of attributes loaded from a CSV file exported by the **Species Creator** companion program (`code/SpeciesCreator.nlogox`). Each row in the CSV defines one species. The parameters that most strongly determine survey bias are:

| Parameter | Units | Role in bias |
|---|---|---|
| `diver.avoidance.w` | dimensionless weight | Positive → undercount (evasion); negative → overcount (attraction) |
| `max.sustained.speed` | m/s | Faster fish cross transect borders more readily, inflating non-instantaneous bias |
| `burst.speed` | m/s | Sets escape speed when diver enters approach distance |
| `approach.dist` | m | Radius at which evasion is triggered; larger values increase undercount |
| `id.distance` | m | Maximum range for species identification; limits effective detection zone |
| `detectability` | 0–1 probability | Values < 1 introduce stochastic visibility loss (cryptic species) |
| `perception.dist` | m | Fish sensory range for schoolmates and divers |
| `perception.angle` | degrees | Directional scope of fish sensing (0–360) |
| Schooling on/off | Boolean | Schooling increases count variance due to clustering |
| `schooling.dist` | body lengths | Preferred inter-individual distance within schools |
| Up to 4 behaviours × urge weights | dimensionless | Define behavioural repertoire; each behaviour is a vector of 8 urge weights with an associated frequency |

The CSV format is defined implicitly by the Species Creator. Representative species parameter files are stored in `data/` (e.g., `data/calibration.csv`, `data/schooling.csv`, `data/shy.csv`, `data/cryptic.csv`, `data/bold.csv`).

---

## 6. Success Metrics

| Metric | Definition | Target |
|---|---|---|
| Bias quantification | `(estimated density - instantaneous density) / instantaneous density` per replicate | Directionally correct and consistent with empirical expectations from literature |
| Estimate precision | Coefficient of variation across N replicates for a given parameter set | Documented across the full behavioural parameter space in the validation report |
| Sensitivity rank order | Ranking of parameters by effect size on bias (OAT analysis) | Avoidance weight and speed rank highest, consistent with Reefex and AnimDens findings |
| Method comparison | Relative bias across the four survey methods for identical species parameter sets | Remote camera produces positive bias for avoidance species; diver methods produce negative bias |
| Computational performance | Time to complete one BehaviorSpace sweep of N replicates | Acceptable for interactive use; current vector-math optimisation yields ~22% speedup over pre-v3.0 baseline |
| Reproducibility | Re-running published BehaviorSpace experiments reproduces figures from Pais & Cabral (2018) within stochastic error | Documented in validation report |

---

## 7. Dependencies and Data Sources

| Dependency | Location | Notes |
|---|---|---|
| Species parameter CSVs | `data/*.csv` | Input data for all model runs; provenance to be documented in `data/README.md` |
| ODD protocol | `docs/artifacts/odd/ODD_PROTOCOL.md` | Authoritative behavioural specification; this PRD is derived from it |
| Drag-force appendix | `docs/artifacts/odd/ODD_APPENDIX_I_drag_forces.md` | Physics basis for the deceleration sub-model |
| Peer-reviewed paper | doi:10.7717/peerj.5378 | Empirical validation targets and published parameter values |
| Published output data | doi:10.7717/peerj.5378/supp-6 | Supplementary dataset for quantitative reproduction tests |
| NetLogo 7.0.3 | External | Runtime environment; extensions: `csv`, `rnd`, `profiler`, `time` |
| Vector math optimisation notes | `docs/research/Vector math optimization walkthrough.md` | Engineering background for the ~22% speed improvement in v3.0 |

---

## 8. References

- Pais, M.P., Cabral, H.N. 2018. Fish behaviour effects on the accuracy and precision of underwater visual census surveys. A virtual ecologist approach using an individual-based model. *PeerJ*. doi:10.7717/peerj.5378
- Ward-Paige, C.A., Flemming, J.M., Lotze, H.K., 2010. Overestimating fish counts by non-instantaneous visual censuses. *PLoS One* 5, e11722. doi:10.1371/journal.pone.0011722
- Watson, R.A., Carlos, G.M., Samoilys, M.A., 1995. Bias introduced by the non-random movement of fish in visual transect surveys. *Ecol. Modell.* 77, 205–214. doi:10.1016/0304-3800(93)E0085-H
- Zurell, D. et al., 2010. The virtual ecologist approach: Simulating data and observers. *Oikos* 119, 622–635. doi:10.1111/j.1600-0706.2009.18284.x
