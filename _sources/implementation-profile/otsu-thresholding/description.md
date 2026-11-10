Implementation Profile: **Otsu thresholding**.

> Implementation Profile of the operation Otsu thresholding, whose meaning is its activity type (activityType): the signature of the Generic Profile Raster thresholding, bound to data exchange formats.

## Activity type

The meaning of the operation -- its definition, the standards that define it and its illustration --
is the activity type [`generic-profiles.activity-type.otsu-thresholding`](../../activity-type/otsu-thresholding/), to which this
profile points with `activityType` (decisions D3 and D4).

## Signature and representations

The signature of the Generic Profile [Raster thresholding](../../generic-profile/raster-thresholding/), with each data-carrying
input and output bound to a representation of the
[`bblocks-data-formats`](https://github.com/GeoLabs/bblocks-data-formats) register (Table 21 Data
format, D; decision D6):

| Role | Data type | Cardinality | Representation |
|---|---|---|---|
| input `raster` | `raster-single-band` | exactly one | [`raster-single-band-geotiff`](https://w3id.org/geolabs-ospd/data-formats/representation/raster-single-band-geotiff) (Single-band raster as GeoTIFF) |
| output `mask` | `binary-mask` | -- | [`raster-single-band-geotiff`](https://w3id.org/geolabs-ospd/data-formats/representation/raster-single-band-geotiff) (Single-band raster as GeoTIFF) |

The representations are a minimal default: a deployment may support more formats (OGC 14-065 WPS
2.0.2 §7.5.4 Table 21, footnote d).

## Notes

The threshold is not an input: Otsu's method computes it from the histogram of the raster's values.
A thresholding at a value given by the caller would need another Generic Profile. The output `mask` is a
`binary-mask`; its representation is the one of `raster-single-band`, its broader data type, which
`gp:RepresentationReferenceShape` accepts.

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.raster-thresholding`](../../generic-profile/raster-thresholding/)
- `activityType`: [`generic-profiles.activity-type.otsu-thresholding`](../../activity-type/otsu-thresholding/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). A proposal added on 2026-11-10 (decision of
2026-11-10, six new process profiles). The processes of `bblocks-process-profiles` that implement it are attached
there, with `implementsProfile`; this item carries no tool, host or testbed (decision D4).
