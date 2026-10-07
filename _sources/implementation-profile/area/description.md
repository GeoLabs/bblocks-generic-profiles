Implementation Profile: **Area**.

> The area of this Surface, as measured in the spatial reference system of this Surface.

## Source

- [OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1, §2.1.9.1 Area()](https://www.ogc.org/standards/sfs/)
- ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_Area
- [ZOO-Project Geonovum testbed -- GetArea: Computes the area of a geometry.](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/GetArea)

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.geometry-measure`](../../generic-profile/geometry-measure/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.vector.*` in `bblocks-process-profiles` -- a real
process of the ZOO-Project Geonovum testbed.
