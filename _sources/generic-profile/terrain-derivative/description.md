Generic Profile: **Terrain derivative**.

> Derives one terrain attribute, as a single-band raster, from an elevation model. One elevation model input, one single-band raster output. Covers operations that differ only in the attribute computed (slope, aspect, curvature, terrain ruggedness, topographic position), not in signature.

## Signature

| | Name | Data type | Description |
|---|---|---|---|
| input | `elevation` | [`elevation-model`](../../data-type/) | the elevation model |
| output | `result` | [`raster-single-band`](../../data-type/) | the derived terrain attribute |

## Source

- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic Profile is.
- The operations below are each grounded in their own SAGA 7.3.0 tool documentation (see each
  Implementation Profile).

## Relations

- `broader`: [`generic-profiles.concept.terrain-analysis`](../../concept/terrain-analysis/)
- Refined by (3 Implementation Profiles): [`slope`](../../implementation-profile/slope/), [`terrain-ruggedness-index`](../../implementation-profile/terrain-ruggedness-index/), [`topographic-position-index`](../../implementation-profile/topographic-position-index/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).
