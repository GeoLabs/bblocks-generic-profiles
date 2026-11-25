Activity type family: **Spatial model conversion**.

> Converts spatial data from one spatial model to another, such as a point cloud to a grid coverage or to a collection of features.

## The item

`https://w3id.org/geolabs/ospd/generic-profiles/activity-type/spatial-model-conversion` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate spatial data, declared with GeoSPARQL 1.1 classes: `usedEntityType` `geo:Feature`. The class is chosen per kind of role (see `scripts/activity-types.yaml`); how a data type of `bblocks-data-types` maps to an entity type is still open (decision D8, question 5).

The run of an activity of this type is not typed here (decision D8, open).

## Members

A family groups operations by meaning (decision of 2026-11-19), proposed by GeoLabs: no source defines this grouping. Its members are its sub-classes; the Generic Profiles, which group operations by signature, are another axis. No Implementation Profile points to a family.

- [`generic-profiles.activity-type.point-cloud-to-grid`](../point-cloud-to-grid/)
- [`generic-profiles.activity-type.point-cloud-to-shapes`](../point-cloud-to-shapes/)
