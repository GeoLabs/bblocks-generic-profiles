Activity type: **Band retrieval**.

> Retrieves one band, one range component, of an Earth observation product as a raster, over the whole product or over an area of interest, with the values the product provides, possibly converted to physical units by the scale and offset the product declares.

## The item

`https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/band-retrieval` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate spatial data, declared with GeoSPARQL 1.1 classes: `usedEntityType` `geo:Feature`; `generatedEntityType` `geo:Feature`. The class is chosen per kind of role (see `scripts/activity-types.yaml`); how a data type of `bblocks-data-types` maps to an entity type is still open (decision D8, question 5).

The run of an activity of this type is not typed here (decision D8, open).

## Sources

- [OGC 12-040 Web Coverage Service Interface Standard - Range Subsetting Extension 1.0, §1 Scope (retrieval of selected range components of a coverage)](https://portal.ogc.org/files/12-040)
- [OGC 09-110r4 WCS 2.0 Interface Standard - Core, version 2.0.1, §4.5 (coverage) trimming and §8.4.1 GetCoverage request (domain subsetting)](https://portal.ogc.org/files/09-110r4)

## Profiles of this operation

The Implementation Profile [`generic-profiles.implementation-profile.band-retrieval`](../../implementation-profile/band-retrieval/) points here with `activityType`. It holds the signature and the representations; this item holds the meaning.
