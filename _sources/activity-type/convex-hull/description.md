Activity type: **Convex hull**.

> Returns a geometry that represents the convex hull of this Geometry.

SQL/MM name: `ST_ConvexHull`.

## The item

`https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/convex-hull` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate spatial data, declared with GeoSPARQL 1.1 classes: `usedEntityType` `geo:Geometry`; `generatedEntityType` `geo:Geometry`. The class is chosen per kind of role (see `scripts/activity-types.yaml`); how a data type of `bblocks-data-types` maps to an entity type is still open (decision D8, question 5).

The run of an activity of this type is not typed here (decision D8, open).

## Sources

- [OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1, §2.1.1.3 ConvexHull()](https://www.ogc.org/standards/sfs/)
- ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_ConvexHull

## Profiles of this operation

The Implementation Profile [`generic-profiles.implementation-profile.convex-hull`](../../implementation-profile/convex-hull/) points here with `activityType`. It holds the signature and the representations; this item holds the meaning.
