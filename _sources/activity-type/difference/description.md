Activity type: **Difference**.

> Returns a geometric object representing the point set difference of this geometric object with anotherGeometry.

SQL/MM name: `ST_Difference`.

## The item

`https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/difference` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate spatial data, declared with GeoSPARQL 1.1 classes: `usedEntityType` `geo:Geometry`; `generatedEntityType` `geo:Geometry`. The class is chosen per kind of role (see `scripts/activity-types.yaml`); how a data type of `bblocks-data-types` maps to an entity type is still open (decision D8, question 5).

The run of an activity of this type is not typed here (decision D8, open).

## Sources

- [OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture, §6.1.26](https://www.ogc.org/standards/sfa/)
- ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, §5.1.13 ST_Difference

## Illustration

No PostGIS workshop illustration exists for this operation. PostGIS's own workshop chapter on geometry-returning functions (<https://postgis.net/workshops/postgis-intro/geometry_returning.html>) covers `ST_Centroid`, `ST_Buffer`, `ST_Intersection` and `ST_Union` with a diagram each, but not `ST_Difference` -- there is no matching illustration to reuse here.

## Profiles of this operation

The Implementation Profile [`generic-profiles.implementation-profile.difference`](../../implementation-profile/difference/) points here with `activityType`. It holds the signature and the representations; this item holds the meaning.
