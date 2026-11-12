Implementation Profile: **Radiometric index (single-band rasters)**.

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

| Role | Data type | Cardinality | Representation |
|---|---|---|---|
| input `rasters` | `raster-single-band` | maxOccurs unbounded | [`raster-single-band-geotiff`](https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff) (Single-band raster as GeoTIFF) |
| input `index` | `radiometric-index` | minOccurs 0, maxOccurs unbounded | none (a parameter) |
| output `raster` | `raster-single-band` | -- | [`raster-single-band-geotiff`](https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff) (Single-band raster as GeoTIFF) |

The representations are a minimal default: a deployment may support more formats (OGC 14-065 WPS
2.0.2 §7.5.4 Table 21, footnote d).

## How this profile differs from radiometric-index

The Implementation Profile [`radiometric-index`](../radiometric-index/) takes one multi-band image (`rasters`,
maxOccurs 1) and returns one raster with a band per index. This one takes the bands as separate single-band
rasters (`rasters`, maxOccurs unbounded) and returns one single-band raster per index: a deployment may bind
several of its outputs to `raster`, one per index. Both narrow the data types of the Generic Profile
(`raster` to `raster-single-band`); no shape checks such a narrowing, the `const` pins of `schema.yaml` do.

`index` has minOccurs 0 (decision C3 of 2026-11-10): a deployment may fix the index it computes instead of
exposing it, and records the fixed value where it is profiled, in `bblocks-process-profiles`. Which input raster
holds which band is not expressed by this profile.

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.radiometric-index`](../../generic-profile/radiometric-index/)
- `activityType`: [`generic-profiles.activity-type.radiometric-index`](../../activity-type/radiometric-index/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). A proposal added on 2026-11-10 (decision of
2026-11-10, six new process profiles). The processes of `bblocks-process-profiles` that implement it are attached
there, with `implementsProfile`; this item carries no tool, host or testbed (decision D4).
