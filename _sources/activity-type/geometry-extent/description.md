Activity type: **Geometry extent**.

> Computes the minimum bounding rectangle of a set of input geometries, as a geometry.

## The item

`https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/geometry-extent` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate spatial data, declared with GeoSPARQL 1.1 classes: `usedEntityType` `geo:Geometry`; `generatedEntityType` `geo:Geometry`. The class is chosen per kind of role (see `scripts/activity-types.yaml`); how a data type of `bblocks-data-types` maps to an entity type is still open (decision D8, question 5).

The run of an activity of this type is not typed here (decision D8, open).

## Sources

- [OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture (Envelope)](https://www.ogc.org/standards/sfa/)
- ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_Envelope

## Profiles of this operation

The Implementation Profile [`generic-profiles.implementation-profile.geometry-extent`](../../implementation-profile/geometry-extent/) points here with `activityType`. It holds the signature and the representations; this item holds the meaning.
