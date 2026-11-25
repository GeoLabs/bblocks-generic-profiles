Activity type: **Raster band math**.

> Evaluates a user-supplied, possibly vector-valued, mathematical expression per pixel across one or more input rasters, producing an output raster with one or more bands.

## The item

`https://w3id.org/geolabs/ospd/generic-profiles/activity-type/raster-band-math` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of the family [`generic-profiles.activity-type.band-algebra`](../band-algebra/) (decision of 2026-11-19), itself a sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate spatial data, declared with GeoSPARQL 1.1 classes: `usedEntityType` `geo:Feature`; `generatedEntityType` `geo:Feature`. The class is chosen per kind of role (see `scripts/activity-types.yaml`); how a data type of `bblocks-data-types` maps to an entity type is still open (decision D8, question 5).

The run of an activity of this type is not typed here (decision D8, open).

## Sources

- [OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard](https://www.ogc.org/standards/wcps/)
- [OGC 09-146r8 Coverage Implementation Schema (CIS) 1.1.1, §6.5 RangeType](https://docs.ogc.org/is/09-146r8/09-146r8.html)

## Profiles of this operation

The Implementation Profiles [`generic-profiles.implementation-profile.raster-band-math`](../../implementation-profile/raster-band-math/), [`generic-profiles.implementation-profile.raster-band-math-multiband`](../../implementation-profile/raster-band-math-multiband/) point here with `activityType`: the same operation, bound to different representations or cardinalities. They hold the signature and the representations; this item holds the meaning.
