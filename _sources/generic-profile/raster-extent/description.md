Generic Profile: **Raster extent**.

> Computes the bounding envelope of a raster coverage, returned as a geometry (a rectangular polygon in the coverage's CRS). One Raster input, one Geometry output.

## Source

- ISO 19123-1:2023 *Geographic information -- Schema for coverage geometry and functions -- Part
  1: Fundamentals* -- the abstract coverage domain/range model this signature is grounded in (see
  [its Concept](../../concept/raster-coverage-processing/) for the full citation).
- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic
  Profile is.

## Why the output is a Geometry, not a bounding box

The output is the coverage's bounding envelope -- conceptually "just" a bounding box -- but this
Generic Profile's real binding ([`OTB.ImageEnvelope`](../../implementation-profile/raster-extent/))
produces an actual vector polygon (GML/KML), not four plain numbers: *"Build a vector data
containing the image envelope polygon... you can set the polygon with more points with the `sr`
parameter"* -- `OTB.ImageEnvelope` can even densify the polygon's edges to follow a reprojection
curve, something four corner numbers cannot represent. This tier carries no type at all (see the
base schema's own note), but the Implementation Profile's `schema` reflects this: it declares
GML, not a `$ref` to `ogc.api.processes.v1.schemas.bbox` the way
[`raster-crop`](../raster-crop/)'s `areaOfInterest` does -- the two operations bind to genuinely
different real parameters, a polygon here, four plain numbers there.

## Relations

- `broader`: [`generic-profiles.concept.raster-coverage-processing`](../../concept/raster-coverage-processing/)
- Refined by (1 Implementation Profile):
- [`raster-extent`](../../implementation-profile/raster-extent/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).
