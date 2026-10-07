Generic Profile: **Unary geometry operation**.

> Derives a new geometry from a single input geometry. One Geometry input, one Geometry output. Covers operations that differ only in what they compute (bounding envelope, centroid, convex hull), not in signature -- the same principle `binary-spatial-predicate` and `binary-spatial-operation` already use for their own several operations.

## Source

- [OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture](https://www.ogc.org/standards/sfa/)
  -- the operations below are each defined there, at their own clause (see each Implementation
  Profile).
- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic
  Profile is.

## Relations

- `broader`: [`generic-profiles.concept.vector-geometry-processing`](../../concept/vector-geometry-processing/)
- Refined by (3 Implementation Profiles):
- [`geometry-extent`](../../implementation-profile/geometry-extent/)
- [`centroid`](../../implementation-profile/centroid/)
- [`convex-hull`](../../implementation-profile/convex-hull/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).
