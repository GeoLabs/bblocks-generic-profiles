Activity type: **Topographic position index**.

> The topographic position index (TPI) of Guisan et al. (1999): the difference between the elevation of each cell and the mean elevation of its neighbourhood.

## The item

`https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/topographic-position-index` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate spatial data, declared with GeoSPARQL 1.1 classes: `usedEntityType` `geo:Feature`; `generatedEntityType` `geo:Feature`. The class is chosen per kind of role (see `scripts/activity-types.yaml`); how a data type of `bblocks-data-types` maps to an entity type is still open (decision D8, question 5).

The run of an activity of this type is not typed here (decision D8, open).

## Sources

- Guisan, A., Weiss, S.B., Weiss, A.D. (1999): GLM versus CCA spatial modeling of plant species distribution. Plant Ecology 143: 107-122

## Profiles of this operation

The Implementation Profile [`generic-profiles.implementation-profile.topographic-position-index`](../../implementation-profile/topographic-position-index/) points here with `activityType`. It holds the signature and the representations; this item holds the meaning.
