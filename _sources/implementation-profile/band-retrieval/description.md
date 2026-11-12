Implementation Profile: **Band retrieval**.

> Implementation Profile of the operation Band retrieval, whose meaning is its activity type (activityType): the signature of the Generic Profile Band retrieval, bound to data exchange formats.

## Activity type

The meaning of the operation -- its definition, the standards that define it and its illustration --
is the activity type [`generic-profiles.activity-type.band-retrieval`](../../activity-type/band-retrieval/), to which this
profile points with `activityType` (decisions D3 and D4).

## Signature and representations

The signature of the Generic Profile [Band retrieval](../../generic-profile/band-retrieval/), with each data-carrying
input and output bound to a representation of the
[`bblocks-data-formats`](https://github.com/GeoLabs/bblocks-data-formats) register (Table 21 Data
format, D; decision D6):

| Role | Data type | Cardinality | Representation |
|---|---|---|---|
| input `product` | `eo-product` | exactly one | [`eo-product-stac-item`](https://w3id.org/geolabs/ospd/data-formats/representation/eo-product-stac-item) (Earth observation product as STAC Item) |
| input `band` | `band-identifier` | exactly one | none (a parameter) |
| input `areaOfInterest` | `bounding-box` | minOccurs 0 | [`bounding-box-ogcapi-processes-bbox`](https://w3id.org/geolabs/ospd/data-formats/representation/bounding-box-ogcapi-processes-bbox) (Bounding box as OGC API - Processes bbox) |
| output `raster` | `raster` | -- | [`raster-geotiff`](https://w3id.org/geolabs/ospd/data-formats/representation/raster-geotiff) (Raster as GeoTIFF) |

The representations are a minimal default: a deployment may support more formats (OGC 14-065 WPS
2.0.2 §7.5.4 Table 21, footnote d).

## Notes

`areaOfInterest` is optional (minOccurs 0, decision C14 of 2026-11-10): without it the whole band is
retrieved. The output is a `raster`, not a single-band raster: a band identifier may designate a composite
asset of the product, such as a true-colour image. No Implementation Profile is proposed for products
delivered as SAFE packages with JPEG 2000 bands: the SAFE format has no media type, and the rule that every
format has one is kept (decision C8 of 2026-11-10).

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.band-retrieval`](../../generic-profile/band-retrieval/)
- `activityType`: [`generic-profiles.activity-type.band-retrieval`](../../activity-type/band-retrieval/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). A proposal added on 2026-11-10 (decision of
2026-11-10, six new process profiles). The processes of `bblocks-process-profiles` that implement it are attached
there, with `implementsProfile`; this item carries no tool, host or testbed (decision D4).
