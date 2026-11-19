Activity type: **Point cloud to grid**.

> Writes one value per grid cell from the points falling in it -- by default the z value of the first point -- as a single-band raster.

## The item

`https://w3id.org/geolabs/ospd/generic-profiles/activity-type/point-cloud-to-grid` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of the family [`generic-profiles.activity-type.spatial-model-conversion`](../spatial-model-conversion/) (decision of 2026-11-19), itself a sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate spatial data, declared with GeoSPARQL 1.1 classes: `usedEntityType` `geo:Feature`; `generatedEntityType` `geo:Feature`. The class is chosen per kind of role (see `scripts/activity-types.yaml`); how a data type of `bblocks-data-types` maps to an entity type is still open (decision D8, question 5).

The run of an activity of this type is not typed here (decision D8, open).

## Profiles of this operation

The Implementation Profile [`generic-profiles.implementation-profile.point-cloud-to-grid`](../../implementation-profile/point-cloud-to-grid/) points here with `activityType`. It holds the signature and the representations; this item holds the meaning.
