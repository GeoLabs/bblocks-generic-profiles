Activity type: **Point cloud thinning (simple)**.

> Reduces the number of points to the given percentage by sequential point removal, which suits points stored in chronological order best.

## The item

`https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/point-cloud-thinning` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `acttype:ActivityType`.

It declares no used or generated entity type, and is not a geoprocessing activity type yet: its data are rasters, point clouds, feature collections or bounding boxes, and how a data type of this project becomes an entity type waits for the answer of the model maintainers (`docs/questions-for-rim-atr-maintainers.md`, question 5; decision D8, open).

The run of an activity of this type is not typed here (decision D8, open).

## Profiles of this operation

The Implementation Profile [`generic-profiles.implementation-profile.point-cloud-thinning`](../../implementation-profile/point-cloud-thinning/) points here with `activityType`. It holds the signature and the representations; this item holds the meaning.
