# FishCensus v3.0

## Context

Underwater visual census (UVC) methods are used worldwide to monitor shallow marine and freshwater habitats and support management and conservation decisions. However, several sources of bias still undermine the ability of these methods to accurately estimate abundances of some species.

## FishCensus Model

FishCensus is an agent-based model that simulates underwater visual census of fish populations. It can help estimate sampling bias, apply correction factors to field surveys, and decide on the best survey method for a particular species given its behavioural traits, detectability, or speed.

Fish move using a urge-based vector boids algorithm with drag-force physics. Complex behaviours such as schooling, diver avoidance/attraction, and bait scent following can be represented.

Four survey methods are supported:

- **Fixed-distance transect** — diver swims a fixed length, counting fish within a belt of defined width
- **Timed transect** — same as above but duration-based rather than distance-based
- **Stationary point count** — diver remains stationary and counts fish within a cylinder
- **Remote cameras** — static camera baited with a scent attractant; fish approach via a diffusing scent gradient

## How it works

FishCensus comes with two separate programs. The **Species Creator** is used to create new fish species or observe/edit existing ones; species parameters can be exported as a CSV file and imported into the main model.

In the main FishCensus program, a virtual diver (or camera) surveys a fish assemblage whose true density is known, allowing the direct quantification of bias — a measure that is unknowable in real field surveys.

Model code and documentation are maintained at [github.com/miguelppais/netlogo-fishcensus](https://github.com/miguelppais/netlogo-fishcensus). A full ODD protocol description is available in `docs/artifacts/odd/`.

## Related models

### Reefex model

Watson, R.A., Carlos, G.M., & Samoilys, M.A., 1995. Bias introduced by the non-random movement of fish in visual transect surveys. Ecological Modelling 77(2–3), 205–214. <http://doi.org/10.1016/0304-3800(93)E0085-H>

### AnimDens model

Ward-Paige, C.A., Flemming, J.M., Lotze, H.K., 2010. Overestimating fish counts by non-instantaneous visual censuses: Consequences for population and community descriptions. PLoS One 5, e11722. <http://doi.org/10.1371/journal.pone.0011722>

Pais, M.P., Ward-Paige, C.A. (2015). AnimDens NetLogo model. <http://modelingcommons.org/browse/one_model/4408>

### Vector-based swarming

Wilensky, U. (2005). NetLogo Flocking 3D Alternate model. <http://ccl.northwestern.edu/netlogo/models/Flocking3DAlternate>. Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.

## Credits and references

If you use this model in your research, please cite:

Pais, M.P., Cabral, H.N. 2018. Fish behaviour effects on the accuracy and precision of underwater visual census surveys. A virtual ecologist approach using an individual-based model. *PeerJ*. doi:10.7717/peerj.5378

To cite the model software itself:

Pais, M.P. 2026. FishCensus (version 3.0). CoMSES Computational Model Library. doi:10.25937/k5nn-1r14

## Acknowledgments

I thank everyone who tested the model and interface and helped find bugs, Christine Ward-Paige for clarifications and suggestions about the AnimDens model, Uri Wilensky for NetLogo and the base code for vector-based swarming, Kenneth Rose for valuable feedback and suggestions and J.P. Rosa for revising the calculation of drag forces. This study had the support of Fundação para a Ciência e Tecnologia (FCT), through the strategic project UID/MAR/04292/2013 granted to MARE and the grant awarded to Miguel P. Pais (SFRH/BPD/94638/2013).

## Contact the author

To report bugs, suggest features, or share work done with the model, please open an issue at [github.com/miguelppais/netlogo-fishcensus](https://github.com/miguelppais/netlogo-fishcensus) or email [mppais@fc.ul.pt](mailto:mppais@fc.ul.pt)

## COPYRIGHT AND LICENSE

Copyright 2016 Miguel Pessanha Pais

This model is released under the [MIT License](https://opensource.org/licenses/MIT). See the `LICENSE` file in the repository root for the full license text.
