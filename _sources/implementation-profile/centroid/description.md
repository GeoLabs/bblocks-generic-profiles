Implementation Profile: **Centroid**.

> The mathematical centroid for this Surface as a Point. The result is not guaranteed to be on this Surface.

## Source

- [OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1, §2.1.9.1 Centroid()](https://www.ogc.org/standards/sfs/)
- ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_Centroid
- [ZOO-Project Geonovum testbed -- Centroid: Computes the centroid of a polygon.](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Centroid)

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.unary-geometry-operation`](../../generic-profile/unary-geometry-operation/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.vector.*` in `bblocks-process-profiles` -- a real
process of the ZOO-Project Geonovum testbed.
