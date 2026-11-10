Activity type: **Product selection**.

> Selects, from a catalogue of Earth observation products, those of a collection whose footprint intersects an area of interest and whose acquisition time falls within a time interval, possibly filtered further on their metadata, such as their cloud cover.

## The item

`https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/product-selection` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate spatial data, declared with GeoSPARQL 1.1 classes: `usedEntityType` `geo:Geometry`; `generatedEntityType` `geo:Feature`. The class is chosen per kind of role (see `scripts/activity-types.yaml`); how a data type of `bblocks-data-types` maps to an entity type is still open (decision D8, question 5).

The run of an activity of this type is not typed here (decision D8, open).

## Sources

- [OGC 13-026r9 OpenSearch Extension for Earth Observation 1.1, §1 Scope and the parameters for the discovery of products (parentIdentifier, cloudCover)](https://docs.ogc.org/is/13-026r9/13-026r9.html)
- [OGC 17-069r4 OGC API - Features - Part 1: Core, §7.15.3 Parameter bbox and §7.15.4 Parameter datetime](https://docs.ogc.org/is/17-069r4/17-069r4.html)
- [STAC API - Item Search 1.0.0 (community specification), parameters bbox, intersects, datetime and collections](https://github.com/radiantearth/stac-api-spec/blob/v1.0.0/item-search/README.md)

## Notes

It passes the geoprocessing shapes through its area of interest, and the search is a spatial query (a footprint intersects an area), but nothing geographic is computed or produced; the products may be returned as references. Whether a parent for discovery and access outside geoprocessing should be used is asked to the maintainers (question 5, decision C10 of 2026-11-10).

## Profiles of this operation

The Implementation Profile [`generic-profiles.implementation-profile.product-selection`](../../implementation-profile/product-selection/) points here with `activityType`. It holds the signature and the representations; this item holds the meaning.
