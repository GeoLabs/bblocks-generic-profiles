Activity type: **Raster format conversion**.

> Re-encodes a raster coverage into another raster format, without altering its content.

## The item

`https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-format-conversion` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate spatial data, declared with GeoSPARQL 1.1 classes: `usedEntityType` `geo:Feature`; `generatedEntityType` `geo:Feature`. The class is chosen per kind of role (see `scripts/activity-types.yaml`); how a data type of `bblocks-data-types` maps to an entity type is still open (decision D8, question 5).

The run of an activity of this type is not typed here (decision D8, open).

## Sources

- [OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard](https://www.ogc.org/standards/wcps/)

## Profiles of this operation

The Implementation Profile [`generic-profiles.implementation-profile.raster-format-conversion`](../../implementation-profile/raster-format-conversion/) points here with `activityType`. It holds the signature and the representations; this item holds the meaning.
