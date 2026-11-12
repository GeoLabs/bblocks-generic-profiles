Activity type: **Raster rendering**.

> Depicts a raster as an image for viewing, giving each cell a colour from a colour map that associates values, or classes of values, with colours.

## The item

`https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-rendering` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate spatial data, declared with GeoSPARQL 1.1 classes: `usedEntityType` `geo:Feature`. The class is chosen per kind of role (see `scripts/activity-types.yaml`); how a data type of `bblocks-data-types` maps to an entity type is still open (decision D8, question 5).

The run of an activity of this type is not typed here (decision D8, open).

## Sources

- [OGC 05-077r4 Symbology Encoding Implementation Specification 1.1.0, §11.5 Raster Symbolizer (ColorMap with the Categorize or Interpolate function)](https://portal.ogc.org/files/05-077r4)

## Notes

No generated entity type is declared. The image holds colours, not values, and is not georeferenced in general; no GeoSPARQL class applies to it.

## Profiles of this operation

The Implementation Profile [`generic-profiles.implementation-profile.raster-rendering`](../../implementation-profile/raster-rendering/) points here with `activityType`. It holds the signature and the representations; this item holds the meaning.
