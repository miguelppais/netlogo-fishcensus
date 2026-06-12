# Appendix I

## Calculation of acceleration due to drag on the FishCensus fish movement sub-model

This is an appendix to the full description of the model that can be found on openABM.

Miguel Pessanha Pais (mppais@fc.ul.pt)

---

This is a summary of the calculations. For references and details on how these calculations fit in the model, see the [full ODD description](ODD_PROTOCOL.md).

Since the observed acceleration of an actively swimming fish already considers drag forces, it is the coasting phase that is of interest for the movement model. The drag force (F_d) acting over a coasting fish is calculated as:

$$F_d = \frac{1}{2} \times D \times d \times A_s \times v^2 \tag{1}$$

, where D is the drag coefficient, d is the density of the fluid (1027 kg/m³ for surface seawater), v is the speed and A_s is the wetted surface area.

In order to calculate acceleration from the drag force, the fish body mass must be taken into account. Since length is an attribute of fish in the model, the weight (W) in kilograms can be estimated from a length-weight relationship:

$$W = a \, L^b \tag{2}$$

, where L is the total length in metres.

For simplicity, the surface area of a fish can be roughly estimated as a function of total length squared, multiplied by a coefficient that varies with body shape:

$$A_s = c \, L^2 \tag{3}$$

Given that F_d = W a_d, and substituting W by the length-weight relationship, the magnitude of the acceleration due to drag (a_d) in a movement cycle can be written in the form:

$$a_d = k \, v^2 \tag{4}$$

, with v being the speed on the previous cycle. The constant k is calculated from the total length (L) in meters using equations 1, 2 and 3:

$$k = \left(\frac{1}{2} \times D \times d \times cL^2\right) \big/ \left(aL^b\right) \tag{5}$$

, where D is the drag coefficient, d is the density of the fluid, c is the coefficient for the length - surface area relationship and a and b are coefficients for the length - weight relationship. The coefficients a, b and c must be converted so the formulas reflect relationships in meters and kilograms.
