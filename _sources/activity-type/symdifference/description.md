Activity type: **Symmetric difference**.

> Returns a geometric object representing the point set symmetric difference of this geometric object with anotherGeometry.

SQL/MM name: `ST_SymDifference`.

## The item

`https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/symdifference` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate spatial data, declared with GeoSPARQL 1.1 classes: `usedEntityType` `geo:Geometry`; `generatedEntityType` `geo:Geometry`. The class is chosen per kind of role (see `scripts/activity-types.yaml`); how a data type of `bblocks-data-types` maps to an entity type is still open (decision D8, question 5).

The run of an activity of this type is not typed here (decision D8, open).

## Sources

- [OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture, §6.1.27](https://www.ogc.org/standards/sfa/)
- ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, §5.1.48 ST_SymDifference

## Illustration

No PostGIS workshop illustration exists for this operation. Same gap as `difference`: PostGIS's workshop chapter on geometry-returning functions does not cover `ST_SymDifference` at all, so there is no matching illustration to reuse here.

## Profiles of this operation

The Implementation Profile [`generic-profiles.implementation-profile.symdifference`](../../implementation-profile/symdifference/) points here with `activityType`. It holds the signature and the representations; this item holds the meaning.
