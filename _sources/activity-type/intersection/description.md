Activity type: **Intersection**.

> Returns a geometric object representing the point set intersection of this geometric object with anotherGeometry.

SQL/MM name: `ST_Intersection`.

## The item

`https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/intersection` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate geometries: `usedEntityType` `geo:Geometry`; `generatedEntityType` `geo:Geometry`.

The run of an activity of this type is not typed here (decision D8, open).

## Sources

- [OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture, §6.1.24](https://www.ogc.org/standards/sfa/)
- ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, §5.1.25 ST_Intersection

## Illustration

![ST_Intersection](assets/intersection.jpg)

Source: [PostGIS Workshop -- Geometry Returning Functions](https://postgis.net/workshops/postgis-intro/geometry_returning.html), © Paul Ramsey, Mark Leslie, PostGIS contributors, licensed [CC BY-SA 3.0 US](http://creativecommons.org/licenses/by-sa/3.0/us/).

## Profiles of this operation

The Implementation Profile [`generic-profiles.implementation-profile.intersection`](../../implementation-profile/intersection/) points here with `activityType`. It holds the signature and the representations; this item holds the meaning.
