Activity type: **Raster reprojection**.

> Reprojects a raster coverage to another coordinate reference system, resampling pixel values as needed, preserving the coverage's content.

## The item

`https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-reprojection` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `acttype:ActivityType`.

It declares no used or generated entity type, and is not a geoprocessing activity type yet: its data are rasters, point clouds, feature collections or bounding boxes, and how a data type of this project becomes an entity type waits for the answer of the model maintainers (`docs/questions-for-rim-atr-maintainers.md`, question 5; decision D8, open).

The run of an activity of this type is not typed here (decision D8, open).

## Sources

- [OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard](https://www.ogc.org/standards/wcps/)

## Profiles of this operation

The Implementation Profile [`generic-profiles.implementation-profile.raster-reprojection`](../../implementation-profile/raster-reprojection/) points here with `activityType`. It holds the signature and the representations; this item holds the meaning.
