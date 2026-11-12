Activity type: **Slope**.

> The slope gradient of an elevation model at each cell, from a local fit of the surface by the 9 parameter 2nd order polynom of Zevenbergen & Thorne (1987).

## The item

`https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/slope` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate spatial data, declared with GeoSPARQL 1.1 classes: `usedEntityType` `geo:Feature`; `generatedEntityType` `geo:Feature`. The class is chosen per kind of role (see `scripts/activity-types.yaml`); how a data type of `bblocks-data-types` maps to an entity type is still open (decision D8, question 5).

The run of an activity of this type is not typed here (decision D8, open).

## Sources

- Zevenbergen, L.W., Thorne, C.R. (1987): Quantitative analysis of land surface topography. Earth Surface Processes and Landforms, 12: 47-56

## Profiles of this operation

The Implementation Profile [`generic-profiles.implementation-profile.slope`](../../implementation-profile/slope/) points here with `activityType`. It holds the signature and the representations; this item holds the meaning.
