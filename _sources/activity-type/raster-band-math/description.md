Activity type: **Raster band math**.

> Evaluates a user-supplied mathematical expression per pixel across one or more input rasters, producing a monoband output raster.

## The item

`https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-band-math` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate spatial data, declared with GeoSPARQL 1.1 classes: `usedEntityType` `geo:Feature`; `generatedEntityType` `geo:Feature`. The class is chosen per kind of role (see `scripts/activity-types.yaml`); how a data type of `bblocks-data-types` maps to an entity type is still open (decision D8, question 5).

The run of an activity of this type is not typed here (decision D8, open).

## Sources

- [OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard](https://www.ogc.org/standards/wcps/)

## Profiles of this operation

The Implementation Profile [`generic-profiles.implementation-profile.raster-band-math`](../../implementation-profile/raster-band-math/) points here with `activityType`. It holds the signature and the representations; this item holds the meaning.
