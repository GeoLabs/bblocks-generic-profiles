Generic Profile: **Raster resampling**.

> Changes the cell size of a raster coverage over the same extent and in the same coordinate reference system. One Raster input, a target grid resolution, one Raster output on the new grid.

## Signature

| Role | Data type | Cardinality | Meaning |
|---|---|---|---|
| input `raster` | [`raster`](https://geolabs.github.io/bblocks-data-types/def/data-type/raster) | exactly one | the input raster coverage |
| input `resolution` | [`grid-resolution`](https://geolabs.github.io/bblocks-data-types/def/data-type/grid-resolution) | exactly one | the cell size of the output grid, along each of its axes |
| output `raster` | [`raster`](https://geolabs.github.io/bblocks-data-types/def/data-type/raster) | exactly one | the resampled raster coverage |

Each data type is a concept of the [`bblocks-data-types`](https://github.com/GeoLabs/bblocks-data-types) register; this tier names no format ([OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32) gives Generic Profile no Data format row). Outputs have no cardinality: Table 21 has no Output.Multiplicity row.

## Source

- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic
  Profile is. The meaning of the operation, and the standards that define it, are its activity type (see the Implementation Profile).

## Relations

- `broader`: [`generic-profiles.concept.raster-coverage-processing`](../../concept/raster-coverage-processing/)
- Refined by (1 Implementation Profile):
- [`raster-resampling`](../../implementation-profile/raster-resampling/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level). A proposal added on 2026-11-10 (decision of 2026-11-10, six new process profiles).
