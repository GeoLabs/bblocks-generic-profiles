Activity type: **Slope**.

> The slope gradient of an elevation model at each cell, from a local fit of the surface by the 9 parameter 2nd order polynom of Zevenbergen & Thorne (1987).

## The item

`https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/slope` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `acttype:ActivityType`.

It declares no used or generated entity type, and is not a geoprocessing activity type yet: its data are rasters, point clouds, feature collections or bounding boxes, and how a data type of this project becomes an entity type waits for the answer of the model maintainers (`docs/questions-for-rim-atr-maintainers.md`, question 5; decision D8, open).

The run of an activity of this type is not typed here (decision D8, open).

## Sources

- Zevenbergen, L.W., Thorne, C.R. (1987): Quantitative analysis of land surface topography. Earth Surface Processes and Landforms, 12: 47-56

## Profiles of this operation

The Implementation Profile [`generic-profiles.implementation-profile.slope`](../../implementation-profile/slope/) points here with `activityType`. It holds the signature and the representations; this item holds the meaning.
