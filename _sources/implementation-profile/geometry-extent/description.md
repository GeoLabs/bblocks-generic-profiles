Implementation Profile: **Geometry extent**.

> Computes the minimum bounding rectangle of a set of input geometries, as a geometry.

## Source

Three sources, at different levels -- the abstract semantics, the SQL binding, and the concrete
tool this testbed actually runs:

- [OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture](https://www.ogc.org/standards/sfa/)
  -- `Geometry::Envelope()`, the abstract operation (this is what
  [its Concept](../../concept/vector-geometry-processing/) and
  [Generic Profile](../../generic-profile/geometry-extent/) are grounded in too).
- ISO/IEC 13249-3:2016 *SQL multimedia and application packages -- Part 3: Spatial*, `ST_Envelope`
  -- the same operation bound to SQL, the same way SQL/MM grounds every other vector Implementation
  Profile in this register.
- [SAGA GIS -- Get Shapes Extents](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/shapes_tools_19.html)
  -- the concrete software binding the Geonovum testbed actually runs,
  [`SAGA.shapes_tools.19`](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.shapes_tools.19)
  ("Get Shapes Extents"): takes a shapes layer (`SHAPES`) and returns its extent (`EXTENTS`), both
  as `text/xml`/KML/`object` -- a vector geometry, not four plain numbers, the same shape this
  Implementation Profile declares. Unlike the vector predicates/operations above (SQL/MM-bound),
  this one is SAGA-bound: this testbed has no SQL/MM `ST_Envelope` process of its own, only this
  SAGA tool.

## Data formats

`geometry`, `result`: GML -- the register's minimal default (Table 21, D: Declare), consistent
with every other vector Implementation Profile in this register. `SAGA.shapes_tools.19`'s own
`SHAPES`/`EXTENTS` additionally expose KML and a generic `object` encoding; GML is kept as this
tier's minimal baseline (Per [OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32),
a specific deployment may *Extend* this default, footnote d).

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.geometry-extent`](../../generic-profile/geometry-extent/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.vector.extent` in `bblocks-process-profiles` -- a real
process of the ZOO-Project Geonovum testbed
(<https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.shapes_tools.19>).
