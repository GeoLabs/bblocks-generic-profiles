Generic Profile: **Raster thresholding**.

> Divides the cells of a single-band raster into two classes at a threshold that the operation determines from the raster's values, and returns the upper class as a binary mask. One single-band Raster input, one Binary mask output.

## Signature

| Role | Data type | Cardinality | Meaning |
|---|---|---|---|
| input `raster` | [`raster-single-band`](https://geolabs.github.io/bblocks-data-types/def/data-type/raster-single-band) | exactly one | the single-band raster to threshold |
| output `mask` | [`binary-mask`](https://geolabs.github.io/bblocks-data-types/def/data-type/binary-mask) | exactly one | the cells of the upper class |

Each data type is a concept of the [`bblocks-data-types`](https://github.com/GeoLabs/bblocks-data-types) register; this tier names no format ([OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32) gives Generic Profile no Data format row). Outputs have no cardinality: Table 21 has no Output.Multiplicity row.

## Source

- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic
  Profile is. The meaning of the operation, and the standards that define it, are its activity type (see the Implementation Profile).

## Relations

- `broader`: [`generic-profiles.concept.raster-coverage-processing`](../../concept/raster-coverage-processing/)
- Refined by (1 Implementation Profile):
- [`otsu-thresholding`](../../implementation-profile/otsu-thresholding/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level). A proposal added on 2026-11-10 (decision of 2026-11-10, six new process profiles).
