Implementation Profile: **Topographic position index**.

> Implementation Profile of the operation Topographic position index, whose meaning is its activity type (activityType): the signature of the Generic Profile Terrain derivative, bound to data exchange formats.

## Activity type

The meaning of the operation -- its definition, the standards that define it and its illustration --
is the activity type [`generic-profiles.activity-type.topographic-position-index`](../../activity-type/topographic-position-index/), to which this
profile points with `activityType` (decisions D3 and D4).

## Signature and representations

The signature of the Generic Profile [Terrain derivative](../../generic-profile/terrain-derivative/), with each data-carrying
input and output bound to a representation of the
[`bblocks-data-formats`](https://github.com/GeoLabs/bblocks-data-formats) register (Table 21 Data
format, D; decision D6):

| Role | Data type | Representation |
|---|---|---|
| input `elevation` | `elevation-model` | [`elevation-model-geotiff`](https://w3id.org/geolabs/ospd/data-formats/representation/elevation-model-geotiff) (Elevation model as GeoTIFF) |
| output `result` | `raster-single-band` | [`raster-single-band-geotiff`](https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff) (Single-band raster as GeoTIFF) |

The representations are a minimal default: a deployment may support more formats (OGC 14-065 WPS
2.0.2 §7.5.4 Table 21, footnote d).

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
- `activityType`: [`generic-profiles.activity-type.topographic-position-index`](../../activity-type/topographic-position-index/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see [`ospd.process-profiles.terrain.topographic-position-index`](https://github.com/GeoLabs/bblocks-process-profiles/tree/master/_sources/terrain/topographic-position-index)
in `bblocks-process-profiles` -- a real process of the ZOO-Project Geonovum testbed
(<https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.18>).

That process names this profile with `implementsProfile`. Tools, hosts and testbeds are
recorded there; this item carries none as keyword or source (decision D4). The sections
above keep the tools and testbed that its defaults were grounded in.

## Changes

A proposal, amended in place on 2026-11-09 (`gp:amendmentAction`):

- `meaning-2026-11-09`, substantive
- `operation-sources-2026-11-09`, clarifying
- `representation-2026-11-09`, substantive
- `tools-2026-11-09`, clarifying
- `sections-restored-2026-11-09`, clarifying
