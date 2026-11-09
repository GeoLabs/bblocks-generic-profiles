Implementation Profile: **Analytical hillshading**.

> Implementation Profile of the operation Analytical hillshading, whose meaning is its activity type (activityType): the signature of the Generic Profile Analytical hillshading, bound to data exchange formats.

## Activity type

The meaning of the operation -- its definition, the standards that define it and its illustration --
is the activity type [`generic-profiles.activity-type.analytical-hillshading`](../../activity-type/analytical-hillshading/), to which this
profile points with `activityType` (decisions D3 and D4).

## Signature and representations

The signature of the Generic Profile [Analytical hillshading](../../generic-profile/analytical-hillshading/), with each data-carrying
input and output bound to a representation of the
[`bblocks-data-formats`](https://github.com/GeoLabs/bblocks-data-formats) register (Table 21 Data
format, D; decision D6):

| Role | Data type | Representation |
|---|---|---|
| input `elevation` | `elevation-model` | [`elevation-model-geotiff`](https://w3id.org/geolabs-ospd/data-formats/representation/elevation-model-geotiff) (Elevation model as GeoTIFF) |
| input `azimuth` | `number` | -- |
| input `altitude` | `number` | -- |
| output `result` | `raster-single-band` | [`raster-single-band-geotiff`](https://w3id.org/geolabs-ospd/data-formats/representation/raster-single-band-geotiff) (Single-band raster as GeoTIFF) |

The representations are a minimal default: a deployment may support more formats (OGC 14-065 WPS
2.0.2 §7.5.4 Table 21, footnote d).

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
- `activityType`: [`generic-profiles.activity-type.analytical-hillshading`](../../activity-type/analytical-hillshading/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of this
register: deployed processes are profiled in `bblocks-process-profiles`, and name this profile with
`implementsProfile`. Tools, hosts and testbeds are recorded there; this item carries none as
keyword or source (decision D4). The sections above keep the tools and testbed that its defaults
were grounded in.

## Changes

A proposal, amended in place on 2026-11-09 (`gp:amendmentAction`):

- `meaning-2026-11-09`, substantive
- `representation-2026-11-09`, substantive
- `tools-2026-11-09`, clarifying
