Implementation Profile: **Radiometric index**.

> Implementation Profile of the operation Radiometric index, whose meaning is its activity type (activityType): the signature of the Generic Profile Radiometric index, bound to data exchange formats.

## Activity type

The meaning of the operation -- its definition, the standards that define it and its illustration --
is the activity type [`generic-profiles.activity-type.radiometric-index`](../../activity-type/radiometric-index/), to which this
profile points with `activityType` (decisions D3 and D4).

## Signature and representations

The signature of the Generic Profile [Radiometric index](../../generic-profile/radiometric-index/), with each data-carrying
input and output bound to a representation of the
[`bblocks-data-formats`](https://github.com/GeoLabs/bblocks-data-formats) register (Table 21 Data
format, D; decision D6):

| Role | Data type | Representation |
|---|---|---|
| input `rasters` (minOccurs 1, maxOccurs 1) | `raster` | [`raster-geotiff`](https://w3id.org/geolabs-ospd/data-formats/representation/raster-geotiff) (Raster as GeoTIFF) |
| input `index` | `radiometric-index` | -- |
| output `raster` | `raster` | [`raster-geotiff`](https://w3id.org/geolabs-ospd/data-formats/representation/raster-geotiff) (Raster as GeoTIFF) |

The representations are a minimal default: a deployment may support more formats (OGC 14-065 WPS
2.0.2 §7.5.4 Table 21, footnote d).

## Multiplicity

`rasters`: restricted (Table 21, R, footnote c) to exactly one: the indices are computed from the
channels of one multi-band raster, where the Generic Profile accepts one or more rasters.

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.radiometric-index`](../../generic-profile/radiometric-index/)
- `activityType`: [`generic-profiles.activity-type.radiometric-index`](../../activity-type/radiometric-index/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of this
register: deployed processes are profiled in `bblocks-process-profiles`, and name this profile with
`implementsProfile`. Tools, hosts and testbeds are recorded there, not here.

## Changes

A proposal, amended in place on 2026-11-09 (`gp:amendmentAction`):

- `meaning-2026-11-09`, substantive
- `operation-sources-2026-11-09`, clarifying
- `representation-2026-11-09`, substantive
- `tools-2026-11-09`, clarifying
- `data-type-2026-11-09`, substantive
