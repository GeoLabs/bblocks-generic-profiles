Activity type family: **Geometry construction**.

> Derives a new geometry from one input geometry and, possibly, parameters such as a distance.

## The item

`https://w3id.org/geolabs/ospd/generic-profiles/activity-type/geometry-construction` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate spatial data, declared with GeoSPARQL 1.1 classes: `usedEntityType` `geo:Geometry`; `generatedEntityType` `geo:Geometry`. The class is chosen per kind of role (see `scripts/activity-types.yaml`); how a data type of `bblocks-data-types` maps to an entity type is still open (decision D8, question 5).

The run of an activity of this type is not typed here (decision D8, open).

## Members

A family groups operations by meaning (decision of 2026-11-19), proposed by GeoLabs: no source defines this grouping. Its members are its sub-classes; the Generic Profiles, which group operations by signature, are another axis. No Implementation Profile points to a family.

- [`generic-profiles.activity-type.buffer`](../buffer/)
- [`generic-profiles.activity-type.centroid`](../centroid/)
- [`generic-profiles.activity-type.convex-hull`](../convex-hull/)
