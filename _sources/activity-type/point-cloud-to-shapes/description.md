Activity type: **Point cloud to shapes**.

> Converts a point cloud to a feature collection of points.

## The item

`https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/point-cloud-to-shapes` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate spatial data, declared with GeoSPARQL 1.1 classes: `usedEntityType` `geo:Feature`; `generatedEntityType` `geo:FeatureCollection`. The class is chosen per kind of role (see `scripts/activity-types.yaml`); how a data type of `bblocks-data-types` maps to an entity type is still open (decision D8, question 5).

The run of an activity of this type is not typed here (decision D8, open).

## Profiles of this operation

The Implementation Profile [`generic-profiles.implementation-profile.point-cloud-to-shapes`](../../implementation-profile/point-cloud-to-shapes/) points here with `activityType`. It holds the signature and the representations; this item holds the meaning.
