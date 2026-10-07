Implementation Profile: **Is simple**.

> Returns 1 (TRUE) if this Geometry has no anomalous geometric points, such as self intersection or self tangency.

## Source

- [OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1, §2.1.1.1 IsSimple()](https://www.ogc.org/standards/sfs/)
- ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_IsSimple
- [ZOO-Project Geonovum testbed -- IsSimple: IsSimple test.](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/IsSimple)

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.unary-spatial-predicate`](../../generic-profile/unary-spatial-predicate/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.vector.*` in `bblocks-process-profiles` -- a real
process of the ZOO-Project Geonovum testbed.
