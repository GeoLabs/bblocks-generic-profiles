Implementation Profile: **Analytical hillshading**.

> For each cell, the angle at which light coming from the position of the light source hits the terrain surface (SAGA's standard method).

## Data

- input `elevation`: `elevation-model`, GeoTIFF
- input `azimuth`: `number`, no format to declare
- input `altitude`: `number`, no format to declare
- output `result`: `raster-single-band`, GeoTIFF

The declared format is a minimal default; a real implementation may support others (Table 21,
footnote d). For rasters, the Geonovum testbed's SAGA also serves ESRI ASCII grids, ENVI and PNG.

## Source

- [SAGA 7.3.0 -- Analytical Hillshading](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/ta_lighting_0.html)
- [ZOO-Project Geonovum testbed -- SAGA.ta_lighting.0: Analytical Hillshading](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_lighting.0)

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.analytical-hillshading`](../../generic-profile/analytical-hillshading/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.*` in `bblocks-process-profiles` -- a real process of
the ZOO-Project Geonovum testbed.
