Implementation Profile: **Slope**.

> The slope gradient of an elevation model at each cell, from a local fit of the surface (SAGA's default method: the 9 parameter 2nd order polynom of Zevenbergen & Thorne 1987).

## Data

- input `elevation`: `elevation-model`, GeoTIFF
- output `result`: `raster-single-band`, GeoTIFF

The declared format is a minimal default; a real implementation may support others (Table 21,
footnote d). For rasters, the Geonovum testbed's SAGA also serves ESRI ASCII grids, ENVI and PNG.

## Source

- [SAGA 7.3.0 -- Slope, Aspect, Curvature](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/ta_morphometry_0.html)
- [ZOO-Project Geonovum testbed -- SAGA.ta_morphometry.0: Slope, Aspect, Curvature](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.0)
- Zevenbergen, L.W., Thorne, C.R. (1987): Quantitative analysis of land surface topography. Earth Surface Processes and Landforms, 12: 47-56

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.terrain-derivative`](../../generic-profile/terrain-derivative/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.*` in `bblocks-process-profiles` -- a real process of
the ZOO-Project Geonovum testbed.
