Activity type: **Terrain ruggedness index**.

> The terrain ruggedness index (TRI) of Riley et al. (1999): how much the elevation of each cell differs from that of its neighbourhood.

## The item

`https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/terrain-ruggedness-index` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate spatial data, declared with GeoSPARQL 1.1 classes: `usedEntityType` `geo:Feature`; `generatedEntityType` `geo:Feature`. The class is chosen per kind of role (see `scripts/activity-types.yaml`); how a data type of `bblocks-data-types` maps to an entity type is still open (decision D8, question 5).

The run of an activity of this type is not typed here (decision D8, open).

## Sources

- Riley, S.J., De Gloria, S.D., Elliot, R. (1999): A Terrain Ruggedness that Quantifies Topographic Heterogeneity. Intermountain Journal of Science, Vol.5, No.1-4, pp.23-27

## Profiles of this operation

The Implementation Profile [`generic-profiles.implementation-profile.terrain-ruggedness-index`](../../implementation-profile/terrain-ruggedness-index/) points here with `activityType`. It holds the signature and the representations; this item holds the meaning.
