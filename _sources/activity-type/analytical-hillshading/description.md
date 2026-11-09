Activity type: **Analytical hillshading**.

> For each cell, the angle at which light coming from the position of the light source hits the terrain surface.

## The item

`https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/analytical-hillshading` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate spatial data, declared with GeoSPARQL 1.1 classes: `usedEntityType` `geo:Feature`; `generatedEntityType` `geo:Feature`. The class is chosen per kind of role (see `scripts/activity-types.yaml`); how a data type of `bblocks-data-types` maps to an entity type is still open (decision D8, question 5).

The run of an activity of this type is not typed here (decision D8, open).

## Profiles of this operation

The Implementation Profile [`generic-profiles.implementation-profile.analytical-hillshading`](../../implementation-profile/analytical-hillshading/) points here with `activityType`. It holds the signature and the representations; this item holds the meaning.
