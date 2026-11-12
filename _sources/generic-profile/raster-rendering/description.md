Generic Profile: **Raster rendering**.

> Depicts a raster as an image for viewing, by giving each cell a colour from a colour map. One Raster and a colour map in, one rendered image out.

## Signature

| Role | Data type | Cardinality | Meaning |
|---|---|---|---|
| input `raster` | [`raster`](https://geolabs.github.io/bblocks-data-types/def/data-type/raster) | exactly one | the raster to depict |
| input `colourMap` | [`colour-map`](https://geolabs.github.io/bblocks-data-types/def/data-type/colour-map) | exactly one | the colours given to the values of the raster |
| output `image` | [`rendered-image`](https://geolabs.github.io/bblocks-data-types/def/data-type/rendered-image) | exactly one | the rendering of the raster |

Each data type is a concept of the [`bblocks-data-types`](https://github.com/GeoLabs/bblocks-data-types) register; this tier names no format ([OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32) gives Generic Profile no Data format row). Outputs have no cardinality: Table 21 has no Output.Multiplicity row.

## Source

- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic
  Profile is. The meaning of the operation, and the standards that define it, are its activity type (see the Implementation Profile).

## Relations

- `broader`: [`generic-profiles.concept.raster-coverage-processing`](../../concept/raster-coverage-processing/)
- Refined by (1 Implementation Profile):
- [`raster-rendering`](../../implementation-profile/raster-rendering/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level). A proposal added on 2026-11-10 (decision of 2026-11-10, six new process profiles).
