Process Concept: **Terrain Analysis**.

> Operations deriving terrain attributes from an elevation model: local surface derivatives (slope, aspect, curvature), neighbourhood indices (terrain ruggedness, topographic position) and illumination (hillshading) -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 §7.5.1). A kind of raster coverage processing: an elevation model is a single-band raster whose values are elevations.

## Source

- [SAGA 7.3.0 tool libraries, category Terrain Analysis](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/index.html)
- Wilson, J.P., Gallant, J.C. (2000): Terrain Analysis: Principles and Applications (cited by SAGA's Topographic Position Index tool)

## Relations

- Broader concept of (`broader`): [`terrain-derivative`](../../generic-profile/terrain-derivative/), [`analytical-hillshading`](../../generic-profile/analytical-hillshading/)
- Narrower than [`raster-coverage-processing`](../raster-coverage-processing/) (listed in its `narrower`)

## Register position

Top tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): **Concept** -> Generic Profile ->
Implementation Profile -> Implementation (instance level).
