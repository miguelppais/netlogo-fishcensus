# Model Validation & Sensitivity Analysis

> Reference: [CoMSES Guides to Good Practice — ABM Development](https://www.comses.net/resources/guides-to-good-practice/)

---

## 1. Model Identity

| Field | Value |
| --- | --- |
| **Model name** | FishCensus |
| **Version** | 3.0 (analyses conducted on v1.0 and v2.0) |
| **NetLogo version** | 7.0.3 (v1.0 used NetLogo 5.3.1; v2.0 used NetLogo 6) |
| **Date** | 2026-06-13 |
| **Author(s)** | Miguel Pessanha Pais |

---

## 2. Verification

*Verification answers: "Did we build the model right?" — does the code do what the ODD says?*

| Check | Status | Notes |
| --- | --- | --- |
| All ODD submodels implemented | ✅ | Movement, perception, survey, drag-force, scent diffusion — all present |
| Info Tab synchronized with ODD | ✅ | Synced as of 2026-06-13; see `README.md` |
| No runtime errors across parameter space | ✅ | Confirmed through BehaviorSpace sweeps in published analyses |
| Extreme-value tests pass (min/max sliders) | ✅ | OAT analysis covers boundary-adjacent values |
| Unit-level behavior matches ODD description | ✅ | Published in two peer-reviewed journals |

---

## 3. Validation

*Validation answers: "Did we build the right model?" — does model output match real-world patterns?*

### Primary publications

| Publication | Model version | Focus |
| --- | --- | --- |
| Pais, M.P. & Cabral, H.N. (2017). Fish behaviour effects on the accuracy and precision of underwater visual census surveys. A virtual ecologist approach using an individual-based model. *Ecological Modelling* **346**, 58–69. doi:[10.1016/j.ecolmodel.2016.12.011](https://doi.org/10.1016/j.ecolmodel.2016.12.011) | v1.0 | Introduces the model; validates that behavioural archetypes produce directionally correct bias patterns against field literature |
| Pais, M.P. & Cabral, H.N. (2018). Effect of underwater visual survey methodology on bias and precision of fish counts: a simulation approach. *PeerJ* **6**:e5378. doi:[10.7717/peerj.5378](https://doi.org/10.7717/peerj.5378) | v2.0 | Parametric sweep of transect and point count configurations across all four behavioural archetypes |

### 3.1 Pattern-Oriented Validation (POV)

The model was validated using the virtual ecologist approach (Zurell et al. 2010). Known fish behavioural archetypes were simulated and the resulting bias patterns compared against expected directions from the field ecology literature.

| Empirical Pattern | Literature source | FishCensus result |
| --- | --- | --- |
| Cryptic fish are underestimated in UVC | Willis (2001): 44–91% underestimation; Sale & Sharp (1983): −21% | ✅ Cryptic type: −37% (transect), −79% (point count) at 0.2 fish/m² — within literature range |
| Shy (avoidant) fish are underestimated relative to bold fish | Bozec et al. (2011); Kulbicki (1998); Edgar et al. (2004): up to 40–90% underestimation vs control | ✅ Shy vs bold effect size ~200%; shy control comparison shows underestimation consistent with Christensen & Winterbottom (1981) |
| Bold (attracted) fish are overestimated | Kulbicki et al. (2010); Colton & Swearer (2010): gathering around diver inflates counts | ✅ Bold type: +504% (transect), +974% (point count); bold vs control ~200% positive bias |
| Schooling fish show lower precision than solitary species | MacNeil et al. (2008b); Cheal & Thompson (1997): high variability due to school encounter probability | ✅ Schooling CV ≈ 130–400% depending on method, consistently among the highest |
| Mobile fish are overestimated due to non-instantaneous sampling | Ward-Paige et al. (2010): 672–1100% positive bias at 0.4–0.6 m/s | ✅ Shy type (0.4 m/s cruise): +259–609% positive overall bias; bold (fast) even higher |
| Transects have less bias and more precision than point counts | Watson & Quinn (1997); Pais & Cabral (2017) prior expectations | ✅ Confirmed across all four behavioural traits; point counts had higher bias and lower precision on average |
| Increasing point count radius reduces bias for most traits | Field observations: larger area dilutes diver-aggregation effect | ✅ Radius increase reduces bias for schooling, cryptic and bold; exception: shy fish (diver-avoidant) — larger radius increases bias |
| Faster transect swim speed reduces bias for mobile species | Lincoln Smith (1988); field inference | ✅ Faster speed reduces bias for schooling, shy and bold types; increases bias for cryptic (reduces detection time) |

### 3.2 Quantitative Validation Results

**Pais & Cabral (2017) — v1.0 at 0.2 fish/m², strip transects (40 × 2 m, 8 m/min) and stationary point counts (5 m radius, 4°/s, 5 min):**

| Fish type | Method | Inaccuracy (% true density) | Correction factor |
| --- | --- | --- | --- |
| Schooling | Stationary | +400% | 0.20 |
| Cryptic | Stationary | −79% | 4.74 |
| Shy | Stationary | +609% | 0.14 |
| Bold | Stationary | +974% | 0.09 |
| Schooling | Transect | +142% | 0.41 |
| Cryptic | Transect | −37% | 1.60 |
| Shy | Transect | +259% | 0.28 |
| Bold | Transect | +504% | 0.17 |

Inaccuracy was not significantly affected by true density within fish types (F₁,₃ = 2.87, p > 0.05), supporting the application of a density-independent correction factor. Precision was significantly affected by decreasing density (F₁,₃ = 10.62, p < 0.05).

**Pais & Cabral (2018) — v2.0, average bias and CV across all sampling parameter combinations at 0.3 fish/m²:**

| Fish type | Method | Bias avg (%) | Bias range (%) | CV avg (%) | CV range (%) |
| --- | --- | --- | --- | --- | --- |
| Schooling | Stationary | 1182.3 | 130.8–2892.1 | 317.7 | 41.8–1014.1 |
| Cryptic | Stationary | 83.0 | 25.6–307.3 | 62.5 | 9.0–370.1 |
| Shy | Stationary | 758.0 | 23.6–2170.2 | 89.7 | 33.5–202.9 |
| Bold | Stationary | 2940.2 | 478.5–9181.4 | 282.5 | 60.0–1082.8 |
| Schooling | Transect | 215.2 | 41.0–871.3 | 71.3 | 14.7–244.6 |
| Cryptic | Transect | 49.2 | 14.3–79.7 | 14.2 | 4.0–67.2 |
| Shy | Transect | 387.3 | 32.7–1730.0 | 52.6 | 14.7–198.2 |
| Bold | Transect | 857.7 | 102.7–4200.7 | 90.3 | 17.5–305.1 |

Statistical analysis: multiple linear regression on all main effects and interactions, R² > 0.6 for most traits (cryptic R² ≈ 0.4 transect, 0.2 point count).

### 3.3 Face Validity

The model's emergent behaviour is qualitatively consistent with practitioner experience from >250 UVC dives in temperate reefs and with the field ecology literature:

- Cryptic fish underestimation (−37 to −79%) is within the range of field studies using rotenone or enclosed-area methods (Willis 2001: 44–91%; Sale & Sharp 1983: −21%).
- Bold fish overestimation (~500–1000%) is consistent with the expected non-instantaneous sampling effect for fast-moving, diver-attracted species (Ward-Paige et al. 2010).
- The finding that stationary point counts produce systematically higher bias and lower precision than transects replicates well-known field observations, and provides a mechanistic explanation via the non-instantaneous sampling component.
- Bias independence from true density (verified statistically) supports the practical use of correction factors, consistent with Sale & Sharp (1983) and Christensen & Winterbottom (1981).

The model has been accepted for publication in two peer-reviewed international journals (Ecological Modelling, PeerJ), providing independent expert validation of face validity.

---

## 4. Sensitivity Analysis

### 4.1 Local (One-at-a-Time) Structural Parameter Sensitivity

Conducted in Pais & Cabral (2017), §2.4. Setup: 30 × 2 m transects, 8 m/min, 6 m visibility, 0.2 fish/m², 15 replicates per parameter value.

| Parameter | Change | Effect on estimated density | Interpretation |
| --- | --- | --- | --- |
| Behaviour change interval | +1 s (+10%) | +15.2% | Moderate sensitivity; output robust to small changes |
| Behaviour change interval | −1 s (−10%) | +4.1% | Asymmetric — longer interval has more effect |
| Count saturation | −1 fish/s | +0.4% | Low sensitivity |
| Count saturation | +1 fish/s | +1.6% | Low sensitivity |
| School spacing distance | +20% | +20% estimated density | High sensitivity — school compactness directly affects counts |
| School spacing distance | −20% | −20% estimated density | Centre urge increase has analogous effect |
| Perception angle (non-schooling) | −1° | +2.0% estimated density | Low-moderate sensitivity |
| Perception angle (non-schooling) | +1° | +1.8% estimated density | Low-moderate sensitivity |
| Maximum swim speed | (see notes) | **Highest sensitivity parameter** | Requires careful parameterisation from measurements or caudal fin aspect ratio formula |
| Rest urge weight | (see notes) | **Highest sensitivity parameter** | Adds drag to movement; small changes drastically alter average speed |

Full sensitivity results including all OAT species parameter variants are in supplementary material S3 of Pais & Cabral (2017). The species-level OAT files (14 parameter pairs) are available in `data/` and correspond to the 2018 study's method-sensitivity sweep.

### 4.2 Method-Parameter Sensitivity

Conducted in Pais & Cabral (2018). Key significant effects on bias (multiple linear regression):

**Stationary point counts:**

- Increasing survey time → significant positive effect on bias for all traits
- Increasing radius → attenuates time effect for schooling, cryptic, bold; **increases** bias for shy
- Rotation speed → significant positive effect only for shy fish

**Strip transects:**

- Faster swim speed → reduces bias for schooling, shy, bold; **increases** bias for cryptic
- Wider transect → reduces bias for mobile species; increases bias for cryptic
- Transect length → weak effect except at slow speeds (increases bias for mobile species)

**Optimal configurations per trait (from 2018 study conclusions):**

- Mobile species (schooling, bold, shy): fast + wide transect, OR large radius + short time point count
- Cryptic species: slow + narrow transect, OR any point count configuration

### 4.3 Global Sensitivity Analysis

A formal global sensitivity analysis (e.g. Sobol indices, Morris screening) was not conducted in the published studies. The 2017 study applied local OAT analysis. The 2018 study performed a full factorial parametric sweep across all combinations of three method parameters × four behavioural traits, which provides near-global coverage of the sampling methodology parameter space.

---

## 5. Uncertainty Quantification

| Source of uncertainty | How handled | Remaining risk |
| --- | --- | --- |
| Stochasticity (random seed) | 10 replicates per parameter set (fish reshuffled, new random seed each replicate) | Low — bias estimates are stable across densities |
| Parameter uncertainty (movement) | OAT analysis; parameterisation from caudal fin aspect ratio (Sambilay 1990) and field observation; fish speed identified as highest-sensitivity parameter | Moderate — urge weights are abstractions not directly measurable |
| Parameter uncertainty (behaviour frequencies) | Pattern-oriented matching against field observations; schooling type matched to *Diplodus* spp. school sizes (~2–15 individuals) | Moderate for schooling/shy/bold types; lower for cryptic (based on literature) |
| Structural uncertainty | 2D simplification; fixed visibility; wrap-around boundary | Moderate — see Known Limitations |
| Remote cameras (v3.0) | Not yet formally validated against empirical BRUV data | High — new method, no published validation |

---

## 6. BehaviorSpace Experiments

All BehaviorSpace experiment definitions are stored in `code/FishCensus_dev.nlogox`. Published output data from the 2018 study is archived at doi:[10.7717/peerj.5378/supp-6](https://doi.org/10.7717/peerj.5378/supp-6).

**2017 study (v1.0):** 2 methods × 4 fish types × 3 controls × 4 densities × 10 surveys × 10 replicates each.

**2018 study (v2.0):** Full factorial sweep — transects: 5 lengths × 5 widths × 5 speeds × 4 traits = 500 combinations; point counts: 4 radii × 5 times × 5 rotation speeds × 4 traits = 400 combinations. 10 replicates each. Analysis in R 3.4.3.

---

## 7. Calibration Record

| Parameter | Value | Method | Source |
| --- | --- | --- | --- |
| Drag coefficient (D) | 0.011 | Literature — coasting cod (*Gadus morhua*, 0.3 m TL) | Videler (1981) |
| Length-weight (cod) | W = 10.3 L^2.857 (kg, m) | Literature | Coull et al. (1989) |
| Length-surface area coefficient (c) | 40 (m) | Literature | O'Shea et al. (2006) |
| Max swim speeds (all types) | Calculated from caudal fin aspect ratio | Sambilay Jr (1990); FishBase species data | Pais & Cabral (2017, 2018) |
| Cryptic type detectability | 0.1–0.6 per behavioural state | Literature range 0.1–0.4 adjusted for model-specific factors | MacNeil et al. (2008) |
| Cryptic behavioural frequencies | Derived from territorial male behaviour data | Literature | Almada et al. (1987) |
| Schooling type school size | Perception distance set to match ~2–15 individuals | Field observation — *Diplodus* spp. | Pais personal obs. |
| Diver swim speed | 8 m/min | Field measurements on temperate reefs | Pais et al. (2014) |
| Count saturation | 3 fish/s | Visual working memory capacity | Luck & Vogel (1997) |

---

## 8. Known Limitations

1. **2D only** — Depth and vertical stratification are not modelled. Depth-related detection biases absent.
2. **Fixed visibility** — Visibility is a constant (6 m in published analyses). Turbidity gradients not modelled.
3. **Wrap-around world** — Torus boundary; no habitat heterogeneity, edges, or shelter.
4. **No trophic dynamics** — Fish do not feed, starve, or interact as predator/prey. No population dynamics within a run.
5. **No multi-diver effects** — Single diver or camera per simulation run.
6. **No individual variability** — All fish of a type share identical size, speed, and behaviour repertoire. Size classes not differentiated (acknowledged by authors as a simplification).
7. **Unforgiving memory model** — Fish are immediately forgotten when they leave the field of view. May slightly overestimate counts; assumed negligible for small schools.
8. **Transect edge/setup effect not modelled** — The "first phase" effect (fish gathering around diver during setup, or counted at transect end) is absent. Would increase overestimation of mobile species in transects.
9. **Remote cameras (v3.0) not validated** — The bait scent diffusion submodel has no published validation against empirical BRUV data. Results for this method should be interpreted with caution.
