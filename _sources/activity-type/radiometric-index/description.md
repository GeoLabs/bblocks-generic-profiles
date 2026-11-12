Activity type: **Radiometric index**.

> Computes one or more named radiometric indices (e.g. NDVI, NDWI, SAVI) from the relevant spectral channels of the input raster(s).

## The item

`https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/radiometric-index` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate spatial data, declared with GeoSPARQL 1.1 classes: `usedEntityType` `geo:Feature`; `generatedEntityType` `geo:Feature`. The class is chosen per kind of role (see `scripts/activity-types.yaml`); how a data type of `bblocks-data-types` maps to an entity type is still open (decision D8, question 5).

The run of an activity of this type is not typed here (decision D8, open).

## Sources

- [OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard](https://www.ogc.org/standards/wcps/)

## Profiles of this operation

The Implementation Profiles [`generic-profiles.implementation-profile.radiometric-index`](../../implementation-profile/radiometric-index/), [`generic-profiles.implementation-profile.radiometric-index-single-band`](../../implementation-profile/radiometric-index-single-band/) point here with `activityType`: the same operation, bound to different representations or cardinalities. They hold the signature and the representations; this item holds the meaning.
