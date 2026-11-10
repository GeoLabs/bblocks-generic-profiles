Implementation Profile: **Raster resampling**.

> Implementation Profile of the operation Raster resampling, whose meaning is its activity type (activityType): the signature of the Generic Profile Raster resampling, bound to data exchange formats.

## Activity type

The meaning of the operation -- its definition, the standards that define it and its illustration --
is the activity type [`generic-profiles.activity-type.raster-resampling`](../../activity-type/raster-resampling/), to which this
profile points with `activityType` (decisions D3 and D4).

## Signature and representations

The signature of the Generic Profile [Raster resampling](../../generic-profile/raster-resampling/), with each data-carrying
input and output bound to a representation of the
[`bblocks-data-formats`](https://github.com/GeoLabs/bblocks-data-formats) register (Table 21 Data
format, D; decision D6):

| Role | Data type | Cardinality | Representation |
|---|---|---|---|
| input `raster` | `raster` | exactly one | [`raster-geotiff`](https://w3id.org/geolabs-ospd/data-formats/representation/raster-geotiff) (Raster as GeoTIFF) |
| input `resolution` | `grid-resolution` | exactly one | none (a parameter) |
| output `raster` | `raster` | -- | [`raster-geotiff`](https://w3id.org/geolabs-ospd/data-formats/representation/raster-geotiff) (Raster as GeoTIFF) |

The representations are a minimal default: a deployment may support more formats (OGC 14-065 WPS
2.0.2 §7.5.4 Table 21, footnote d).

## Notes

`resolution` is the target cell size. A target number of cells is another way to define the new
grid; it is not a role of this profile, and a deployment may take it as an input of its own (Table 21,
footnote b). The interpolation method is not a role either.

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.raster-resampling`](../../generic-profile/raster-resampling/)
- `activityType`: [`generic-profiles.activity-type.raster-resampling`](../../activity-type/raster-resampling/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). A proposal added on 2026-11-10 (decision of
2026-11-10, six new process profiles). The processes of `bblocks-process-profiles` that implement it are attached
there, with `implementsProfile`; this item carries no tool, host or testbed (decision D4).
