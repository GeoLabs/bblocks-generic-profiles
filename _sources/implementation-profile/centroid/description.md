Implementation Profile: **Centroid**.

> Implementation Profile of the operation Centroid, whose meaning is its activity type (activityType): the signature of the Generic Profile Unary geometry operation, bound to data exchange formats.

## Activity type

The meaning of the operation -- its definition, the standards that define it and its illustration --
is the activity type [`generic-profiles.activity-type.centroid`](../../activity-type/centroid/), to which this
profile points with `activityType` (decisions D3 and D4).

## Signature and representations

The signature of the Generic Profile [Unary geometry operation](../../generic-profile/unary-geometry-operation/), with each data-carrying
input and output bound to a representation of the
[`bblocks-data-formats`](https://github.com/GeoLabs/bblocks-data-formats) register (Table 21 Data
format, D; decision D6):

| Role | Data type | Representation |
|---|---|---|
| input `geometry` | `surface` | [`surface-gml`](https://w3id.org/geolabs/ospd/data-formats/representation/surface-gml) (Surface as GML) |
| output `result` | `point` | [`point-gml`](https://w3id.org/geolabs/ospd/data-formats/representation/point-gml) (Point as GML) |

The representations are a minimal default: a deployment may support more formats (OGC 14-065 WPS
2.0.2 §7.5.4 Table 21, footnote d).

## Source

- [OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1, §2.1.9.1 Centroid()](https://www.ogc.org/standards/sfs/)
- ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_Centroid
- [ZOO-Project Geonovum testbed -- Centroid: Computes the centroid of a polygon.](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Centroid)

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.unary-geometry-operation`](../../generic-profile/unary-geometry-operation/)
- `activityType`: [`generic-profiles.activity-type.centroid`](../../activity-type/centroid/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see [`ospd.process-profiles.sqlmm.centroid`](https://github.com/GeoLabs/bblocks-process-profiles/tree/master/_sources/sqlmm/centroid)
in `bblocks-process-profiles` -- a real process of the ZOO-Project Geonovum testbed
(<https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Centroid>).

That process names this profile with `implementsProfile`. Tools, hosts and testbeds are
recorded there; this item carries none as keyword or source (decision D4). The sections
above keep the tools and testbed that its defaults were grounded in.

## Changes

A proposal, amended in place on 2026-11-09 (`gp:amendmentAction`):

- `meaning-2026-11-09`, substantive
- `operation-sources-2026-11-09`, clarifying
- `representation-2026-11-09`, substantive
- `tools-2026-11-09`, clarifying
- `sections-restored-2026-11-09`, clarifying
