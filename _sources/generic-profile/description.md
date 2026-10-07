Generic Process Profile -- the shape every Generic Profile in this register shares.

## What a Generic Profile is

OGC 14-065 WPS 2.0.2 §7.5.2: *"a generic profile is the abstract interface of a process. It
provides a detailed description of the process mechanics and declares a signature for process
inputs and outputs... similar to a process description... but does not provide a definition of
specific data formats."*

This block is not itself a catalogue: it carries one placeholder example only (`example1`, clearly
marked as illustrative, not a real signature). The real Generic Profiles are each their own
building block, `allOf`-referencing this one and adding their own `const`-pinned `id`/`prefLabel`:

Vector geometry (broader: [`vector-geometry-processing`](../concept/vector-geometry-processing/)):

- [`binary-spatial-predicate`](binary-spatial-predicate/) -- two Geometry in, one Boolean out
  (Intersects, Disjoint, Contains, Within, Touches, Crosses, Equals)
- [`binary-spatial-operation`](binary-spatial-operation/) -- two Geometry in, one Geometry out
  (Intersection, Union, Difference, Symmetric difference)
- [`geometry-buffer`](geometry-buffer/) -- one Geometry and one Number in, one Geometry out
  (Buffer)
- [`unary-geometry-operation`](unary-geometry-operation/) -- one Geometry in, one Geometry out
  (refined by 3 Implementation Profiles: Geometry extent/bounding envelope, Centroid, Convex
  hull)
- [`unary-spatial-predicate`](unary-spatial-predicate/) -- one Geometry in, one Boolean out
  (Is simple)
- [`geometry-measure`](geometry-measure/) -- one Geometry in, one Number out (Area)

Raster/coverage (broader: [`raster-coverage-processing`](../concept/raster-coverage-processing/)):

- [`raster-reprojection`](raster-reprojection/) -- one Raster and a target CRS in, one Raster out
- [`raster-band-math`](raster-band-math/) -- one-or-many Raster and an expression in, one Raster out
  (refined by 2 Implementation Profiles: fixed-one-band and possibly-multi-band -- see below)
- [`radiometric-index`](radiometric-index/) -- one-or-many Raster and index name(s) in, one Raster out
- [`raster-crop`](raster-crop/) -- one Raster and a bounding box in, one Raster out
- [`raster-format-conversion`](raster-format-conversion/) -- one Raster and a target format in, one Raster out
- [`raster-extent`](raster-extent/) -- one Raster in, one Geometry out (bounding envelope)

A Generic Profile declares a signature "for *a* process" (WPS's own wording, singular) -- but
several distinct operations sharing the identical shape are still modelled as **one** Generic
Profile when nothing in the signature itself distinguishes them: the seven vector predicates, and
also `raster-band-math`'s two Implementation Profiles (`OTB.BandMath`, fixed to one band, vs.
`OTB.BandMathX`, which may produce several). An earlier draft of this register modelled that
raster distinction as two Generic Profiles, using `cardinality: one-or-many` on the output to
tell them apart -- that was wrong: a multi-band raster is still **one** Raster output value, not
several (band count is a coverage's internal RangeType structure, OGC 09-146r8 CIS 1.1.1 §6.5,
not an output cardinality), and both variants have the identical Raster(s)+Expression->Raster
signature regardless. See [`raster-band-math`](raster-band-math/)'s own `description.md` ("Why
one Generic Profile, not two") and its multi-band Implementation Profile's "Open question"
section for the full account, including what a correct fix would need (a RangeType-like field
list, not yet modelled here).

`raster-crop`'s `areaOfInterest` and `raster-extent`/`unary-geometry-operation`'s
[`geometry-extent`](../implementation-profile/geometry-extent/) Implementation Profile's outputs
look similar ("a bounding box") but bind to genuinely different real parameters:
`OTB.ExtractROI`'s "extent" mode takes four plain numbers, while
`OTB.ImageEnvelope`/`SAGA.shapes_tools.19` both return an actual vector polygon. Neither
distinction is carried at this tier any more (this tier has no type/format property at all, see
the base schema's own note); it lives entirely at Implementation Profile, in each one's `schema`
-- `areaOfInterest`'s `$ref`s `ogc.api.processes.v1.schemas.bbox`, the extent operations' outputs
declare GML -- see [`raster-crop`](raster-crop/)'s "`areaOfInterest` has no type at this tier"
and [`raster-extent`](raster-extent/)'s "Why the output is a Geometry, not a BoundingBox".

`unary-geometry-operation` is also where `geometry-extent` landed once it stopped being its own
Generic Profile: it shares the identical Geometry->Geometry signature with `centroid` and
`convex-hull` (OGC 99-049 Rev 1.1 §2.1.1.1 Envelope, §2.1.9.1 Centroid, §2.1.1.3 ConvexHull), the
same "one Generic Profile per signature, several Implementation Profiles per operation"
principle used everywhere else in this register -- there was never a reason for it to be
dedicated, that was simply how it was first added (2026-10-01) before the SFA operations below it
arrived (2026-10-06).

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).
