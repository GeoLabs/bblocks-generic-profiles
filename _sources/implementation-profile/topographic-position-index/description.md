Implementation Profile: **Topographic position index**.

> Implementation Profile of the operation Topographic position index, whose meaning is its activity type (activityType): the signature of the Generic Profile Terrain derivative, bound to data exchange formats.

## Activity type

The meaning of the operation -- its definition, the standards that define it and its illustration -- is the activity type [`generic-profiles.activity-type.topographic-position-index`](../../activity-type/topographic-position-index/) (`activityType`), not this profile.

## Data

- input `elevation`: `elevation-model`, GeoTIFF
- output `result`: `raster-single-band`, GeoTIFF

The declared format is a minimal default; a real implementation may support others (Table 21,
footnote d). For rasters, the Geonovum testbed's SAGA also serves ESRI ASCII grids, ENVI and PNG.

## Source

- [SAGA 7.3.0 -- Topographic Position Index (TPI)](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/ta_morphometry_18.html)
- [ZOO-Project Geonovum testbed -- SAGA.ta_morphometry.18: Topographic Position Index (TPI)](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.18)
- Guisan, A., Weiss, S.B., Weiss, A.D. (1999): GLM versus CCA spatial modeling of plant species distribution. Plant Ecology 143: 107-122

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.terrain-derivative`](../../generic-profile/terrain-derivative/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.*` in `bblocks-process-profiles` -- a real process of
the ZOO-Project Geonovum testbed.
