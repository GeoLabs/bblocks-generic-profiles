Generic Profile: **Raster format conversion**.

> Converts a raster coverage from one encoding to another, without changing its content. One Raster input, a target format, one Raster output in the new encoding.

## Source

- ISO 19123-1:2023 *Geographic information -- Schema for coverage geometry and functions -- Part
  1: Fundamentals* -- the abstract coverage domain/range model this signature is grounded in (see
  [its Concept](../../concept/raster-coverage-processing/) for the full citation).
- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic
  Profile is.

## Relations

- `broader`: [`generic-profiles.concept.raster-coverage-processing`](../../concept/raster-coverage-processing/)
- Refined by (1 Implementation Profile):
- [`raster-format-conversion`](../../implementation-profile/raster-format-conversion/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).
