Generic Profile: **Product selection**.

> Selects, from a catalogue, the products of a collection whose footprint intersects an area of interest and whose acquisition time falls within a time interval. An area of interest, a time interval and a collection in, the selected products out.

## Signature

| Role | Data type | Cardinality | Meaning |
|---|---|---|---|
| input `areaOfInterest` | [`geometry`](https://geolabs.github.io/bblocks-data-types/def/data-type/geometry) | exactly one | the area the footprint of each product must intersect |
| input `timeInterval` | [`time-interval`](https://geolabs.github.io/bblocks-data-types/def/data-type/time-interval) | exactly one | the period in which each product was acquired |
| input `collection` | [`collection-identifier`](https://geolabs.github.io/bblocks-data-types/def/data-type/collection-identifier) | exactly one | the collection the products belong to |
| output `products` | [`eo-product`](https://geolabs.github.io/bblocks-data-types/def/data-type/eo-product) | exactly one | the selected products |

Each data type is a concept of the [`bblocks-data-types`](https://github.com/GeoLabs/bblocks-data-types) register; this tier names no format ([OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32) gives Generic Profile no Data format row). Outputs have no cardinality: Table 21 has no Output.Multiplicity row.

`areaOfInterest` is a `geometry`, not a `bounding-box`: a polygon is a valid search area, and a bounding
box, which data-types does not place under `geometry`, can be given as one.

## Source

- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic
  Profile is. The meaning of the operation, and the standards that define it, are its activity type (see the Implementation Profile).

## Relations

- `broader`: [`generic-profiles.concept.data-discovery-and-access`](../../concept/data-discovery-and-access/)
- Refined by (1 Implementation Profile):
- [`product-selection`](../../implementation-profile/product-selection/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level). A proposal added on 2026-11-10 (decision of 2026-11-10, six new process profiles).
