Implementation Profile: **Product selection**.

> Implementation Profile of the operation Product selection, whose meaning is its activity type (activityType): the signature of the Generic Profile Product selection, bound to data exchange formats.

## Activity type

The meaning of the operation -- its definition, the standards that define it and its illustration --
is the activity type [`generic-profiles.activity-type.product-selection`](../../activity-type/product-selection/), to which this
profile points with `activityType` (decisions D3 and D4).

## Signature and representations

The signature of the Generic Profile [Product selection](../../generic-profile/product-selection/), with each data-carrying
input and output bound to a representation of the
[`bblocks-data-formats`](https://github.com/GeoLabs/bblocks-data-formats) register (Table 21 Data
format, D; decision D6):

| Role | Data type | Cardinality | Representation |
|---|---|---|---|
| input `areaOfInterest` | `geometry` | exactly one | [`geometry-geojson`](https://w3id.org/geolabs/ospd/data-formats/representation/geometry-geojson) (Geometry as GeoJSON) |
| input `timeInterval` | `time-interval` | exactly one | none (a parameter) |
| input `collection` | `collection-identifier` | exactly one | none (a parameter) |
| output `products` | `eo-product` | -- | [`eo-product-stac-item`](https://w3id.org/geolabs/ospd/data-formats/representation/eo-product-stac-item) (Earth observation product as STAC Item) |

The representations are a minimal default: a deployment may support more formats (OGC 14-065 WPS
2.0.2 §7.5.4 Table 21, footnote d).

## Notes

The catalogue in which the search runs, and filters such as a maximum cloud cover or a product level,
are not roles: they designate where the search runs or filter for one kind of sensor. A deployment takes them
as inputs of its own (decision C12 of 2026-11-10). `products` may hold several products or one: outputs have
no cardinality, and the structure of the value is the deployment's. A product given by URL, rather than as its
record, is declared at tier 4.

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.product-selection`](../../generic-profile/product-selection/)
- `activityType`: [`generic-profiles.activity-type.product-selection`](../../activity-type/product-selection/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). A proposal added on 2026-11-10 (decision of
2026-11-10, six new process profiles). The processes of `bblocks-process-profiles` that implement it are attached
there, with `implementsProfile`; this item carries no tool, host or testbed (decision D4).
