Generic Profile: **Raster crop**.

> Crops a raster coverage to a region of interest. One Raster input, a bounding box, one Raster output covering only that area.

## Source

- ISO 19123-1:2023 *Geographic information -- Schema for coverage geometry and functions -- Part
  1: Fundamentals* -- the abstract coverage domain/range model this signature is grounded in (see
  [its Concept](../../concept/raster-coverage-processing/) for the full citation).
- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic
  Profile is.

## `areaOfInterest` has no type at this tier

Two earlier drafts tried to give `areaOfInterest` a machine-checked abstract type at this tier --
first `Geometry` (the natural-seeming choice, since a region of interest reads like a geometric
object), then a dedicated `BoundingBox` type when `Geometry` turned out not to match its real
binding ([`raster-crop`](../../implementation-profile/raster-crop/)'s own `OTB.ExtractROI`, whose
"extent" mode takes four plain numbers, `mode.extent.ulx`/`uly`/`lrx`/`lry`, not an encoded
geometry). Both were unnecessary: [Table 21](https://docs.ogc.org/is/14-065/14-065.html#32) gives
Generic Profile no "Data format" row at all, so there is nothing to type here regardless of which
vocabulary is used. The distinction now lives entirely at Implementation Profile, where
`areaOfInterest`'s `schema` `$ref`s
[`ogc.api.processes.v1.schemas.bbox`](https://geolabs.github.io/bblocks-ogcapi-processes/)
directly -- OGC API - Processes - Part 1: Core's own bbox type (itself grounded in
[OGC 17-069r4](https://docs.ogc.org/is/17-069r4/17-069r4.html) §7.15.3's `bbox` parameter), not a
custom abstract type.

## Relations

- `broader`: [`generic-profiles.concept.raster-coverage-processing`](../../concept/raster-coverage-processing/)
- Refined by (1 Implementation Profile):
- [`raster-crop`](../../implementation-profile/raster-crop/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).
