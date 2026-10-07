Generic Profile: **Binary spatial predicate**.

> Tests a boolean spatial relationship between two geometries: two Geometry inputs, one Boolean output, no side effect.

## Source

- [OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture](https://www.ogc.org/standards/sfa/) -- the operations
  below are each defined there, at their own clause (see each Implementation Profile).
- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic Profile is.

## Relations

- `broader`: [`generic-profiles.concept.vector-geometry-processing`](../../concept/vector-geometry-processing/)
- Refined by (7 Implementation Profiles):
- [`intersects`](../../implementation-profile/intersects/)
- [`disjoint`](../../implementation-profile/disjoint/)
- [`contains`](../../implementation-profile/contains/)
- [`within`](../../implementation-profile/within/)
- [`touches`](../../implementation-profile/touches/)
- [`crosses`](../../implementation-profile/crosses/)
- [`equals`](../../implementation-profile/equals/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).
