Generic Profile: **Raster crop**.

> Crops a raster coverage to a region of interest. One Raster input, a bounding box, one Raster output covering only that area.

## Source

- ISO 19123-1:2023 *Geographic information -- Schema for coverage geometry and functions -- Part
  1: Fundamentals* -- the abstract coverage domain/range model this signature is grounded in (see
  [its Concept](../../concept/raster-coverage-processing/) for the full citation).
- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic
  Profile is.

## `areaOfInterest` is a concept at this tier, not a format

This tier carries a concept, `dataType`, and no format:
[Table 21](https://docs.ogc.org/is/14-065/14-065.html#32) gives Generic Profile no "Data format" row
at all. `areaOfInterest`'s `dataType` is `bounding-box`, a concept of the bblocks-data-types register.

Two earlier drafts took another route. The first used `Geometry`, the natural-seeming choice since a
region of interest reads like a geometric object. It did not match the real binding,
[`raster-crop`](../../implementation-profile/raster-crop/)'s own `OTB.ExtractROI`, whose "extent" mode
takes four plain numbers, `mode.extent.ulx`/`uly`/`lrx`/`lry`, not an encoded geometry: this is the
reason for `bounding-box` rather than `geometry`. The second was a `BoundingBox` type invented for
this register, which is no longer needed. The encoding lives at Implementation Profile, where
`areaOfInterest`'s `schema` `$ref`s
[`ogc.api.processes.part1.v1.schemas.bbox`](https://geolabs.github.io/bblocks-ogcapi-processes/)
directly -- OGC API - Processes - Part 1: Core's own bbox type (itself grounded in
[OGC 17-069r4](https://docs.ogc.org/is/17-069r4/17-069r4.html) §7.15.3's `bbox` parameter).

## Relations

- `broader`: [`generic-profiles.concept.raster-coverage-processing`](../../concept/raster-coverage-processing/)
- Refined by (1 Implementation Profile):
- [`raster-crop`](../../implementation-profile/raster-crop/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).
