Process Concept: **Vector Geometry Processing**.

> Operations on vector geometries: testing a spatial relationship between two geometries, deriving
> a new geometry from one or two others, or measuring a property of a geometry.

## What a Process Concept is

OGC 14-065 WPS 2.0.2 §7.5.1: *"a process concept is an object that provides high-level
documentation about a general group of processes. It describes the purpose, methodology and
properties of a process but not the specific input and output parameters. It is rather a
documentation resource that may be referenced by refined process definitions to document their
relation to a common principle."*

This Concept deliberately carries no input, no output, no format, no CWL and no implementation --
that is what the two tiers below it are for. It exists so that several Generic Profiles with
different I/O shapes can still declare their kinship: [`binary-spatial-predicate`](../../generic-profile/binary-spatial-predicate/),
[`binary-spatial-operation`](../../generic-profile/binary-spatial-operation/),
[`geometry-buffer`](../../generic-profile/geometry-buffer/),
[`unary-geometry-operation`](../../generic-profile/unary-geometry-operation/),
[`unary-spatial-predicate`](../../generic-profile/unary-spatial-predicate/) and
[`geometry-measure`](../../generic-profile/geometry-measure/) each declare this Concept as their
`broader`.

## Source

- [OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture](https://www.ogc.org/standards/sfa/), §6.1 -- the 7
  predicates, 4 set operations and buffer are defined there.
- [OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1](https://www.ogc.org/standards/sfs/) --
  the harmonized-with-SQL predecessor to 06-103r4; Envelope (§2.1.1.1), Centroid/Area/PointOnSurface
  (§2.1.9.1) and ConvexHull/IsSimple (§2.1.1.1, §2.1.1.3) are defined there. Together the two
  standards ground the 17 operations this Concept groups (7 predicates, 4 set operations, buffer,
  envelope, centroid, convex hull, area, is-simple).

## Register position

Top tier of the four-tier model this register implements (OGC 14-065 WPS 2.0.2 §7.5): Concept ->
Generic Profile -> Implementation Profile -> Implementation (instance level). The fourth tier is
not part of this register -- see `ospd.process-profiles.sqlmm.*` in `bblocks-process-profiles`.
