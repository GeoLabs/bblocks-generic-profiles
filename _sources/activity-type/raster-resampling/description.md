Activity type: **Raster resampling**.

> Changes the cell size of a raster coverage, or its number of cells along each axis, over the same extent and in the same coordinate reference system, computing each new cell value from the input cells by an interpolation method.

## The item

`https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-resampling` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate spatial data, declared with GeoSPARQL 1.1 classes: `usedEntityType` `geo:Feature`; `generatedEntityType` `geo:Feature`. The class is chosen per kind of role (see `scripts/activity-types.yaml`); how a data type of `bblocks-data-types` maps to an entity type is still open (decision D8, question 5).

The run of an activity of this type is not typed here (decision D8, open).

## Sources

- [OGC 12-039 Web Coverage Service Interface Standard - Scaling Extension 1.0, §4.1 Scaling (of a grid coverage)](https://portal.ogc.org/files/12-039)

## Profiles of this operation

The Implementation Profile [`generic-profiles.implementation-profile.raster-resampling`](../../implementation-profile/raster-resampling/) points here with `activityType`. It holds the signature and the representations; this item holds the meaning.
