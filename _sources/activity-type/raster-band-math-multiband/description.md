Activity type: **Raster band math (multi-band output)**.

> Evaluates a user-supplied, possibly vector-valued mathematical expression per pixel across one or more input rasters, producing an output raster with one or more bands.

## The item

`https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-band-math-multiband` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate spatial data, declared with GeoSPARQL 1.1 classes: `usedEntityType` `geo:Feature`; `generatedEntityType` `geo:Feature`. The class is chosen per kind of role (see `scripts/activity-types.yaml`); how a data type of `bblocks-data-types` maps to an entity type is still open (decision D8, question 5).

The run of an activity of this type is not typed here (decision D8, open).

## Sources

- [OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard](https://www.ogc.org/standards/wcps/)
- [OGC 09-146r8 Coverage Implementation Schema (CIS) 1.1.1, §6.5 RangeType](https://docs.ogc.org/is/09-146r8/09-146r8.html)

## Profiles of this operation

The Implementation Profile [`generic-profiles.implementation-profile.raster-band-math-multiband`](../../implementation-profile/raster-band-math-multiband/) points here with `activityType`. It holds the signature and the representations; this item holds the meaning.
