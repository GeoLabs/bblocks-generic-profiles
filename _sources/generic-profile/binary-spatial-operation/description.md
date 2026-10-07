Generic Profile: **Binary spatial set operation**.

> Computes a new geometry from the point-set relationship of two input geometries: two Geometry inputs, one Geometry output.

## Source

- [OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture](https://www.ogc.org/standards/sfa/) -- the operations
  below are each defined there, at their own clause (see each Implementation Profile).
- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic Profile is.

## Relations

- `broader`: [`generic-profiles.concept.vector-geometry-processing`](../../concept/vector-geometry-processing/)
- Refined by (4 Implementation Profiles):
- [`intersection`](../../implementation-profile/intersection/)
- [`union`](../../implementation-profile/union/)
- [`difference`](../../implementation-profile/difference/)
- [`symdifference`](../../implementation-profile/symdifference/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).
