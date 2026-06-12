# FishCensus — Literature Review and Research Notes

Compiled by: Scientist agent
Date: 2026-06-13
Covers: Pais & Cabral (2017) and Pais & Cabral (2018)

---

## 1. Overview

FishCensus is an individual-based model (IBM) implemented in NetLogo that simulates underwater visual census (UVC) fish surveys using a virtual ecologist approach (Zurell et al., 2010). The model represents a spatially explicit 20 × 80 m arena in which a virtual diver performs one of two sampling methods — strip transects or stationary point counts — while simulated fish exhibit one of four behavioural archetypes. The programme addresses a longstanding but under-quantified problem in marine ecology: bias and imprecision in UVC density estimates arising from fish behaviour and non-instantaneous sampling. Prior computational work by Watson et al. (1995) (Reefex) and Ward-Paige et al. (2010) (AnimDens) established that non-instantaneous sampling inflates counts for mobile species, but neither model systematically explored how survey design parameters interact with fish behaviour across archetype space. FishCensus extended this by combining a Reynolds-boids movement engine (Reynolds, 1987; Spector et al., 2005) with an ODD-described diver agent (Grimm et al., 2006, 2010), enabling the first joint factorial analysis of fish behaviour and survey configuration. Two peer-reviewed papers have been published: Pais & Cabral (2017) established that behavioural archetype dominates over survey method choice in determining bias magnitude, and Pais & Cabral (2018) conducted a full parametric sweep of transect and point-count design parameters, providing evidence-based guidance for method selection per target assemblage.

---

## 2. Key Findings Table

| Paper | Method | Archetype | Inaccuracy / Bias (avg %) | Precision (CV avg %) | Main finding |
|---|---|---|---|---|---|
| Pais & Cabral (2017) | Stationary point count | Schooling | +400% (CF 0.20) | — | Schooling inflates counts via non-instantaneous sampling; correction factor derivable |
| Pais & Cabral (2017) | Stationary point count | Cryptic | −79% (CF 4.74) | — | Hidden fish cause severe underestimation; point counts worse than transects |
| Pais & Cabral (2017) | Stationary point count | Shy | +609% (CF 0.14) | — | Avoidance + non-instantaneous sampling compound positively |
| Pais & Cabral (2017) | Stationary point count | Bold | +974% (CF 0.09) | — | Diver attraction produces worst-case overestimation |
| Pais & Cabral (2017) | Strip transect | Schooling | +142% (CF 0.41) | — | Transects less biased than point counts for all archetypes |
| Pais & Cabral (2017) | Strip transect | Cryptic | −37% (CF 1.60) | — | Transect reduces hiding-time exposure; underestimation reduced |
| Pais & Cabral (2017) | Strip transect | Shy | +259% (CF 0.28) | — | Avoidance still inflates, but less than point count |
| Pais & Cabral (2017) | Strip transect | Bold | +504% (CF 0.17) | — | Attraction effect reduced with shorter dwell time |
| Pais & Cabral (2018) | Stationary (all configs) | Schooling | 1182% (range 131–2892%) | 318% (range 42–1014%) | Wide range across configurations; time × radius interaction key |
| Pais & Cabral (2018) | Stationary (all configs) | Cryptic | 83% (range 26–307%) | 63% (range 9–370%) | Lowest absolute bias of all archetypes; point counts preferred |
| Pais & Cabral (2018) | Stationary (all configs) | Shy | 758% (range 24–2170%) | 90% (range 34–203%) | High variability across configurations |
| Pais & Cabral (2018) | Stationary (all configs) | Bold | 2940% (range 479–9181%) | 283% (range 60–1083%) | Highest bias; diver-attracted species require fast transects |
| Pais & Cabral (2018) | Transect (all configs) | Schooling | 215% (range 41–871%) | 71% (range 15–245%) | Speed × width interaction important |
| Pais & Cabral (2018) | Transect (all configs) | Cryptic | 49% (range 14–80%) | 14% (range 4–67%) | Best-performing combination; slow narrow transect optimal |
| Pais & Cabral (2018) | Transect (all configs) | Shy | 387% (range 33–1730%) | 53% (range 15–198%) | Fast wide transect minimises bias |
| Pais & Cabral (2018) | Transect (all configs) | Bold | 858% (range 103–4201%) | 90% (range 18–305%) | Fast wide transect minimises bias |

Notes: Pais & Cabral (2017) values at 0.2 fish/m², standard configurations (transect 40 × 2 m, 8 m/min; point count 5 m radius, 4°/s, 5 min). Pais & Cabral (2018) values at 0.3 fish/m², averaged across all parameter combinations. CF = correction factor (multiply raw count density by CF to obtain unbiased estimate). Precision not separately reported per archetype in 2017 (combined across methods).

---

## 3. Validated Patterns

The following patterns were confirmed by the model against prior field ecology literature.

- Cryptic fish (hidden/camouflaged) are underestimated in UVC surveys. FishCensus produces −37% (transect) to −79% (point count) at 0.2 fish/m², consistent with Willis (2001): 44–91% underestimation and Sale & Sharp (1983): −21% (Pais & Cabral, 2017).

- Shy (diver-avoidant) fish are underestimated relative to bold fish. The avoidance effect interacts with non-instantaneous sampling to produce net positive bias in absolute counts. This directional ordering is consistent with Kulbicki (1998), Bozec et al. (2011), and Edgar et al. (2004) (Pais & Cabral, 2017).

- Bold (diver-attracted) fish are overestimated. Gathering around the diver inflates recorded counts; the model reproduces +504–974% overestimation, consistent with expectations from Kulbicki et al. (2010) and Colton & Swearer (2010) (Pais & Cabral, 2017).

- Schooling fish show lower precision (higher CV) than solitary species. School encounter probability introduces high variance. This matches MacNeil et al. (2008b) and Cheal & Thompson (1997) (Pais & Cabral, 2017; Pais & Cabral, 2018).

- Non-instantaneous sampling inflates counts for mobile species. Fast-moving fish enter and re-enter the sampling area during a survey, producing positive bias. This was previously quantified by Ward-Paige et al. (2010) at 672–1100% for speeds of 0.4–0.6 m/s; the model reproduces the same direction and order of magnitude (Pais & Cabral, 2017; Pais & Cabral, 2018).

- Strip transects produce lower bias and higher precision than stationary point counts across all behavioural archetypes. The reduction in dwell time reduces the non-instantaneous effect. Consistent with Watson & Quinn (1997) and general practitioner experience (Pais & Cabral, 2017; Pais & Cabral, 2018).

- Bias is independent of true density within each fish type (F₁,₃ = 2.87, p > 0.05), supporting the use of a fixed correction factor per archetype. Precision degrades at lower densities (F₁,₃ = 10.62, p < 0.05), consistent with Sale & Sharp (1983) and Christensen & Winterbottom (1981) (Pais & Cabral, 2017).

- Increasing point count radius reduces bias for schooling, cryptic, and bold archetypes, but increases bias for shy (diver-avoidant) fish. This counter-intuitive interaction is a novel prediction not directly tested in prior field studies (Pais & Cabral, 2018).

- Faster transect swim speed reduces bias for schooling, shy, and bold fish, but increases bias for cryptic fish by reducing detection time. Consistent with Lincoln Smith (1988) for mobile species (Pais & Cabral, 2018).

---

## 4. Known Limitations from the Studies

- **Two-dimensional representation.** The model ignores depth. Vertical stratification of fish, depth-related visibility gradients, and the diver's approach angle are not represented.

- **Fixed visibility.** Maximum underwater visibility is set to a constant 6 m for all scenarios in the published analyses. Turbidity effects on detection probability are not modelled.

- **Homogeneous habitat.** The landscape is a featureless torus (wrap-around boundary). Habitat structure, substrate heterogeneity, shelter, and edge effects are absent. Fish home ranges and shelter-seeking behaviour are not modelled.

- **No trophic dynamics or population processes.** Fish do not feed, starve, grow, reproduce, or die within a simulation run. Population-level feedback on behaviour and spatial distribution is absent.

- **Single species per run.** The published analyses run one archetype at a time. Mixed-assemblage interactions (interspecific competition for space, predator avoidance cascades) are not captured.

- **No individual-level variability.** All fish of a given archetype share identical body size, speed, and behavioural repertoire. Size-related differences in detectability and evasion speed are not represented (explicitly acknowledged in both papers).

- **Simplified memory model.** Fish are immediately removed from the diver's memory when they leave the field of view, allowing re-counting. The authors acknowledge this may slightly overestimate counts but treat it as negligible for small schools.

- **Transect edge and set-up effects not modelled.** The "first phase" effect — fish gathering near the diver during the setup period before counting begins, or counted at the end of a transect — is absent. This is expected to increase overestimation of mobile species.

- **Generic drag parameterisation.** Drag forces are calculated using *Gadus morhua* (cod) empirical coefficients as a generic approximation, because species-specific drag data are unavailable for most taxa. Error from this simplification is unquantified.

- **Urge weights as abstractions.** Behavioural urge weights cannot be measured directly in the field; they were set by pattern-oriented matching and OAT sensitivity analysis. Residual uncertainty in urge weights, particularly for rest and wander urges, affects absolute speed and therefore bias magnitude.

- **Local OAT sensitivity analysis only.** A formal global sensitivity analysis (e.g. Sobol indices, Morris screening) was not conducted. Parameter interactions are characterised only for survey configuration parameters (2018 study), not for all fish movement parameters simultaneously.

---

## 5. Open Questions and Future Work

The following directions were either explicitly suggested by the authors or are logically implied by the limitations above.

- **Multi-species assemblage simulations.** Both papers used single-archetype runs. Extending to mixed assemblages would allow evaluation of whether correction factors derived for single archetypes remain valid when behaviourally heterogeneous species are surveyed simultaneously.

- **Three-dimensional extension.** Adding depth as a third spatial dimension would allow modelling of vertical zonation, depth-stratified sampling designs, and the approach angle effect on fish detection.

- **Variable visibility and turbidity.** Replacing fixed visibility with a dynamic parameter would allow exploration of how turbid conditions interact with fish behaviour to alter UVC bias.

- **Habitat heterogeneity.** Incorporating substrate structure (reef, rock, sand patches) and shelter would allow testing how habitat complexity modifies the magnitude of behavioural bias. This is particularly relevant for cryptic species and for comparing results across reef complexity gradients.

- **Empirical archetype calibration.** The four behavioural archetypes are theoretical constructs. Mapping real species to archetypes via field experiments (e.g. diver-approach trials, video tracking) and re-parameterising accordingly would strengthen the practical utility of the correction factors.

- **Global sensitivity analysis.** A Sobol or Morris screening analysis across the full movement parameter space (particularly swim speed, rest urge weight, and school spacing) would quantify which parameter uncertainties most affect the bias estimates reported in the published papers.

- **Density-dependent correction factors.** While the 2017 study confirmed density independence of inaccuracy within the tested range (0.05–0.3 fish/m²), this range is relatively narrow. Testing at lower and higher densities relevant to depleted or aggregated populations may reveal density dependence not apparent in the published range.

- **Diver experience and detection probability.** The counting model assumes perfect detection of all eligible fish up to the count-saturation limit. Incorporating observer-specific detection probability (e.g. a distance-sampling detection function) would align the model with modern distance-sampling theory.

- **Validation of the Remote Cameras (BRUV) method (v3.0).** The bait-scent diffusion submodel added in version 3.0 has no published empirical validation. Comparison against empirical MaxN data from standardised BRUV deployments is the logical next step.

- **Optimal survey effort curves.** The 2018 study characterised bias and precision for a fixed number of replicates. Deriving power curves relating replicate number to achieved precision, conditional on archetype and method, would be directly actionable for survey design.

---

## 6. Calibration Sources

| Parameter | Value used in published studies | Source |
|---|---|---|
| Drag coefficient (D, coasting cod 0.3 m TL) | 0.011 | Videler (1981) |
| Length-weight relationship (cod, kg and m) | W = 10.3 L^2.857 | Coull et al. (1989) |
| Length-surface area coefficient (c, in m) | 40 | O'Shea et al. (2006) |
| Maximum sustained and burst swim speeds | Calculated from caudal fin aspect ratio | Sambilay Jr (1990); FishBase |
| Count saturation (max fish counted per second) | 3 | Luck & Vogel (1997) |
| Diver swim speed (field reference) | 8 m/min | Pais et al. (2014) |
| Cryptic archetype detectability | 0.1–0.6 per behavioural state | MacNeil et al. (2008); field literature range 0.1–0.4 |
| Cryptic archetype behavioural frequencies | Derived from territorial male behaviour | Almada et al. (1987) |
| Schooling archetype school size | Perception distance set to produce 2–15 individuals | *Diplodus* spp. field observation (Pais, pers. obs.) |
| Diver field of view — transects | 180° | Ward-Paige et al. (2010) |
| Diver field of view — point counts | 160° | Ward-Paige et al. (2010) |
| Maximum visibility | 6 m | Fixed parameter; typical temperate reef conditions |
| Seawater density (for drag calculation) | 1027 kg/m³ | Standard physical oceanography value |
| Behaviour change interval | 10 s | Watson et al. (1995) |
| Movement sub-step | 0.1 s (10 cycles per model second) | Pais & Cabral (2017) |

---

## 7. Reference List

Almada, V.C., Gonçalves, E.J., Santos, A.J., Baptista, C., 1994. Breeding ecology and nest aggregations in a population of *Salaria pavo* (Pisces: Blenniidae) in an area where nest sites are very scarce. *Journal of Fish Biology* **45**, 819–830. doi:10.1111/j.1095-8649.1994.tb01052.x

Bozec, Y.-M., Kulbicki, M., Laloë, F., Mou-Tham, G., Gascuel, D., 2011. Factors affecting the detection distances of reef fish: implications for visual censuses. *Marine Biology* **158**, 969–981. doi:10.1007/s00227-011-1623-6

Cheal, A.J., Thompson, A.A., 1997. Comparing visual counts of coral reef fish: implications of transect width and species selection. *Marine Ecology Progress Series* **158**, 241–248. doi:10.3354/meps158241

Christensen, M.S., Winterbottom, R., 1981. A correction factor for, and its application to, visual censuses of littoral fish. *South African Journal of Zoology* **16**, 73–79.

Colton, M.A., Swearer, S.E., 2010. A comparison of two survey methods: differences between underwater visual census and baited remote underwater video. *Marine Ecology Progress Series* **400**, 19–36. doi:10.3354/meps08377

Coull, K.A., Jermyn, A.S., Newton, A.W., Henderson, G.I., Hall, W.B., 1989. *Length/Weight relationships for 88 species of fish encountered in the North East Atlantic*. Scottish Fisheries Research Report. Aberdeen, Scotland.

Edgar, G.J., Barrett, N.S., Morton, A.J., 2004. Biases associated with the use of underwater visual census techniques to quantify the density and size-structure of fish populations. *Journal of Experimental Marine Biology and Ecology* **308**, 269–290. doi:10.1016/j.jembe.2004.03.004

Grimm, V., Berger, U., Bastiansen, F., Eliassen, S., Ginot, V., Giske, J., Goss-Custard, J., Grand, T., Heinz, S.K., Huse, G., Huth, A., Jepsen, J.U., Jørgensen, C., Mooij, W.M., Müller, B., Pe'er, G., Piou, C., Railsback, S.F., Robbins, A.M., Robbins, M.M., Rossmanith, E., Rüger, N., Strand, E., Souissi, S., Stillman, R.A., Vabø, R., Visser, U., DeAngelis, D.L., 2006. A standard protocol for describing individual-based and agent-based models. *Ecological Modelling* **198**, 115–126. doi:10.1016/j.ecolmodel.2006.04.023

Grimm, V., Berger, U., DeAngelis, D.L., Polhill, J.G., Giske, J., Railsback, S.F., 2010. The ODD protocol: A review and first update. *Ecological Modelling* **221**, 2760–2768. doi:10.1016/j.ecolmodel.2010.08.019

Kulbicki, M., 1998. How the acquired behaviour of commercial reef fishes may influence the results obtained from visual censuses. *Journal of Experimental Marine Biology and Ecology* **222**, 11–30. doi:10.1016/S0022-0981(97)00133-0

Kulbicki, M., Cornuet, N., Vigliola, L., Wantiez, L., Hubert, N., Floeter, S., Fernandez-Parades, J.R., Beets, J., Friedlander, A., 2010. Counting coral reef fishes: interaction between methods and habitats. *Aquatic Living Resources* **23**, 65–77. doi:10.1051/alr/2009040

Lincoln Smith, M.P., 1988. Effects of observer swimming speed on sample counts of temperate rocky reef fish assemblages. *Marine Ecology Progress Series* **43**, 223–231. doi:10.3354/meps043223

Luck, S.J., Vogel, E.K., 1997. The capacity of visual working memory for features and conjunctions. *Nature* **390**, 279–281. doi:10.1038/36846

MacNeil, M.A., Graham, N.A.J., Conroy, M.J., Fonnesbeck, C.J., Polunin, N.V.C., Rushton, S.P., Chabanet, P., McClanahan, T.R., 2008. Detection heterogeneity in underwater visual-census data. *Journal of Fish Biology* **73**, 1748–1763. doi:10.1111/j.1095-8649.2008.02067.x

O'Shea, B., Mordue-Luntz, A.J., Fryer, R.J., Pert, C.C., Bricknell, I.R., 2006. Determination of the surface area of a fish. *Journal of Fish Diseases* **29**, 437–440. doi:10.1111/j.1365-2761.2006.00728.x

Pais, M.P., Cabral, H.N., 2017. Fish behaviour effects on the accuracy and precision of underwater visual census surveys. A virtual ecologist approach using an individual-based model. *Ecological Modelling* **346**, 58–69. doi:10.1016/j.ecolmodel.2016.12.011

Pais, M.P., Cabral, H.N., 2018. Effect of underwater visual survey methodology on bias and precision of fish counts: a simulation approach. *PeerJ* **6**:e5378. doi:10.7717/peerj.5378

Pais, M.P., Henriques, S., Costa, M.J., Cabral, H.N., 2014. Topographic complexity and the power to detect structural and functional changes in temperate reef fish assemblages: The need for habitat-independent sample sizes. *Ecological Indicators* **45**, 18–27. doi:10.1016/j.ecolind.2014.03.018

Reynolds, C.W., 1987. Flocks, herds, and schools: A distributed behavioral model. *Computer Graphics (ACM)* **21**, 25–34. doi:10.1145/37402.37406

Sale, P.F., Sharp, B.J., 1983. Correction for bias in visual transect censuses of coral reef fishes. *Coral Reefs* **2**, 37–42. doi:10.1007/BF00304729

Sambilay Jr, V.C., 1990. Interrelationships between swimming speed, caudal fin aspect ratio and body length of fishes. *Fishbyte* **8**, 16–20.

Spector, L., Klein, J., Perry, C., Feinstein, M., 2005. Emergence of collective behavior in evolving populations of flying agents. *Genetic Programming and Evolvable Machines* **6**, 111–125. doi:10.1007/s10710-005-7620-3

Videler, J.J., 1981. Swimming movements, body structure and propulsion in cod *Gadus morhua*. *Symposia of the Zoological Society of London* **48**, 1–27.

Ward-Paige, C.A., Flemming, J.M., Lotze, H.K., 2010. Overestimating fish counts by non-instantaneous visual censuses: Consequences for population and community descriptions. *PLoS One* **5**, e11722. doi:10.1371/journal.pone.0011722

Watson, R.A., Carlos, G.M., Samoilys, M.A., 1995. Bias introduced by the non-random movement of fish in visual transect surveys. *Ecological Modelling* **77**, 205–214. doi:10.1016/0304-3800(93)E0085-H

Watson, M., Quinn, N.J., 1997. Comparative performance of methods for estimating the abundance of reef fish. *Proceedings of the 8th International Coral Reef Symposium* **2**, 1987–1992.

Willis, T.J., 2001. Visual census methods underestimate density and diversity of cryptic reef fishes. *Journal of Fish Biology* **59**, 1408–1411. doi:10.1111/j.1095-8649.2001.tb00202.x

Zurell, D., Berger, U., Cabral, J.S., Jeltsch, F., Meynard, C.N., Münkemüller, T., Nehrbass, N., Pagel, J., Reineking, B., Schröder, B., Grimm, V., 2010. The virtual ecologist approach: Simulating data and observers. *Oikos* **119**, 622–635. doi:10.1111/j.1600-0706.2009.18284.x
