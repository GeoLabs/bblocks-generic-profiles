Generic Profile: **Band retrieval**.

> Retrieves one band of an Earth observation product as a raster, over the whole product or over an area of interest. A product, a band identifier and an optional bounding box in, one Raster out.

## Signature

| Role | Data type | Cardinality | Meaning |
|---|---|---|---|
| input `product` | [`eo-product`](https://geolabs.github.io/bblocks-data-types/def/data-type/eo-product) | exactly one | the product the band belongs to |
| input `band` | [`band-identifier`](https://geolabs.github.io/bblocks-data-types/def/data-type/band-identifier) | exactly one | the band to retrieve |
| input `areaOfInterest` | [`bounding-box`](https://geolabs.github.io/bblocks-data-types/def/data-type/bounding-box) | minOccurs 0 | the area to retrieve; the whole product when absent |
| output `raster` | [`raster`](https://geolabs.github.io/bblocks-data-types/def/data-type/raster) | exactly one | the retrieved band |

Each data type is a concept of the [`bblocks-data-types`](https://github.com/GeoLabs/bblocks-data-types) register; this tier names no format ([OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32) gives Generic Profile no Data format row). Outputs have no cardinality: Table 21 has no Output.Multiplicity row.

`areaOfInterest` is the first role of a Generic Profile of this register with minOccurs 0: band retrieval
is defined over the whole product as well as over an area (decision C14 of 2026-11-10).

## Source

- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic
  Profile is. The meaning of the operation, and the standards that define it, are its activity type (see the Implementation Profile).

## Relations

- `broader`: [`generic-profiles.concept.data-discovery-and-access`](../../concept/data-discovery-and-access/)
- Refined by (1 Implementation Profile):
- [`band-retrieval`](../../implementation-profile/band-retrieval/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level). A proposal added on 2026-11-10 (decision of 2026-11-10, six new process profiles).
