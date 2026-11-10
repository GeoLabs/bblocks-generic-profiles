Implementation Profile: **Raster rendering**.

> Implementation Profile of the operation Raster rendering, whose meaning is its activity type (activityType): the signature of the Generic Profile Raster rendering, bound to data exchange formats.

## Activity type

The meaning of the operation -- its definition, the standards that define it and its illustration --
is the activity type [`generic-profiles.activity-type.raster-rendering`](../../activity-type/raster-rendering/), to which this
profile points with `activityType` (decisions D3 and D4).

## Signature and representations

The signature of the Generic Profile [Raster rendering](../../generic-profile/raster-rendering/), with each data-carrying
input and output bound to a representation of the
[`bblocks-data-formats`](https://github.com/GeoLabs/bblocks-data-formats) register (Table 21 Data
format, D; decision D6):

| Role | Data type | Cardinality | Representation |
|---|---|---|---|
| input `raster` | `raster` | exactly one | [`raster-geotiff`](https://w3id.org/geolabs-ospd/data-formats/representation/raster-geotiff) (Raster as GeoTIFF) |
| input `colourMap` | `colour-map` | exactly one | none (a parameter) |
| output `image` | `rendered-image` | -- | [`rendered-image-png`](https://w3id.org/geolabs-ospd/data-formats/representation/rendered-image-png) (Rendered image as PNG) |

The representations are a minimal default: a deployment may support more formats (OGC 14-065 WPS
2.0.2 §7.5.4 Table 21, footnote d).

## Notes

`colourMap` is a parameter: how a colour map is written is not registered as a format (decision C7
of 2026-11-10). The rendered image holds colours, not values, and need not be georeferenced.

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.raster-rendering`](../../generic-profile/raster-rendering/)
- `activityType`: [`generic-profiles.activity-type.raster-rendering`](../../activity-type/raster-rendering/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). A proposal added on 2026-11-10 (decision of
2026-11-10, six new process profiles). The processes of `bblocks-process-profiles` that implement it are attached
there, with `implementsProfile`; this item carries no tool, host or testbed (decision D4).
