# Questions for the Registered Item Model and Activity Type Register maintainers

Status: draft, 2026-11-05, question 12 added 2026-11-08, question 11 extended 2026-11-09. Not sent.

GeoLabs maintains `bblocks-generic-profiles`, a register of process profiles based on the WPS 2.0.2
tiers (OGC 14-065 §7.5). We want to integrate the Activity Type Register (ATR) without breaking the
one-item-class rule. These questions come from reading both repositories and testing against their
SHACL shapes.

Versions read: `registered-item-model` `98f6d6a`, `activity-type-register` `0c52c0e`, plus branch
`model-tweaks`. We have not read the text of ISO 19135:2026, so we cannot tell which rules come from
the standard and which come from the model.

## What we plan to do

An Implementation Profile cannot also be an `acttype:ActivityType`: the two shapes require different
values of `rim:itemClass`, and `rim:RegisterItemShape` allows only one. We confirmed this by test.

We therefore plan one separate activity type item per operation, in our own register:

```turtle
gpat:intersects a acttype:ActivityType , owl:Class ;
    rdfs:subClassOf geoproc:GeoprocessingActivityType ;
    rim:inRegister gp:register ;
    rim:itemClass acttype:activityTypeItemClass ;
    acttype:usedEntityType geo:Geometry ;
    acttype:associatedAgentType prov:SoftwareAgent .
```

This conforms to the RIM, ATR and GeoLabs shapes. We tested the pattern with pySHACL, not in a full
Building Blocks build.

## Questions that block our design

### 1. Must an execution record be a register item?

The `activity-types` example types a run with the registered class and gives it `rim:itemClass`,
`rim:objectIdentifier` and both statuses. In our test, a run typed with a registered class and carrying
no RIM fields fails with 5 violations. A run that uses `prov:type` instead of `rdf:type` conforms.

Is every run meant to be a governed item? If not, what is the recommended way to link a run to its
type? This matters because a workflow engine would otherwise need to mint register metadata per run.

### 2. Should `acttype:ActivityType` specialise `prov:Activity`?

The README says the item class "will be a profile of prov:Activity" and that execution records "will
be instances of prov:Activity". In `ontology.ttl`, `acttype:ActivityType` specialises only
`rim:RegisterItem`. Which statement is intended?

### 3. At what level should a type be registered?

The ATR `NdviComputation` example describes a kind of operation. In `ospd-dtaas-register`,
`convert_format` and `subsidence-analysis` use the URL of one deployed process as the item identifier.
Branch `model-tweaks` stresses that activity types are "types not instances".

We plan an operation-level type in `bblocks-generic-profiles` and deployment-level sub-classes in
`bblocks-process-profiles`. In our test, such a sub-class conforms only if it declares its own spatial
entity type: it does not inherit the one declared by its parent.

Are both levels valid? Should a deployment-level type be a sub-class of an operation-level type?

### 4. May a domain register hold items of `acttype:activityTypeItemClass`?

Our plan keeps the item in `gp:register` and reuses your item class. The core ontology says an item
class may be reused across registers. The ATR describes itself as a top-level register that federated
registers inherit from.

Is this reuse the intended mechanism? If not, should a domain register define its own item class as a
profile of yours?

### 5. How should concept vocabularies map to entity types?

`usedEntityType` expects classes, and `geoproc:` requires a GeoSPARQL spatial class. Our data types are
`rim:Concept` individuals, so using one directly fails validation. Declaring it as a class with
`rdfs:subClassOf geo:Feature` conforms, as in your NDVI example.

What we do now: every activity type of our register is a geoprocessing activity type, and declares a
GeoSPARQL class directly, chosen per kind of data, with no link to our data type concepts:
`geo:Geometry` for geometries and bounding boxes, `geo:Feature` for rasters and point clouds (a
coverage described as a feature, as `geoproc:GeoprocessingActivityType` says),
`geo:FeatureCollection` for feature collections.

Is a class bridge from a concept to a GeoSPARQL class the recommended way to be more precise? GeoSPARQL
has no raster class: is `geo:Feature` the right parent for a raster, and for a point cloud?

## Questions on the Registered Item Model

### 6. What is the cardinality of `rim:realizes`?

`sh:maxCount 1` limits an item to one concept version. Nothing limits the other direction.

- Does ISO 19135:2026 allow several items for one concept version? The governance note says "realised
  as a register item", in the singular.
- Does the limit of one version per item come from the standard or from the model? In our register,
  GML represents 4 data types and GeoTIFF 3.
- Should a format that serves several concepts be a standalone item with no `realizes`?

### 7. Were these terms meant to be dropped?

Commits on 2026-10-21 added `rim:isRealizedBy`, a concept version domain for `rim:inRegister`, and
`altLabel`s matching ISO 19135. They edited `build/annotated`, and none of them is in the current
sources. The `rim:isRealizedBy` note said it allows items "to appear in multiple registers".

Are these terms still wanted? Should they move to `_sources`?

### 8. How should actions on concept versions be recorded?

`rim:hasAction` and `rim:appliesTo` apply only to `rim:RegisterItem`, while concept versions carry the
statuses. `bblocks-data-types` had to add its own `dt:hasVersionAction`. Should the model cover this?

### 9. Does `rim:invalid` fit a proposal awaiting a decision?

We record proposed items as `rim:invalid` and `rim:published`, with one addition action. The model does
not state this reading. Is it acceptable, or should a register define a status such as `draft` in its
specification?

## Stability

### 10. When will `model-tweaks` merge?

It renames `acttype:activityTypeItemClass` to `acttype:ActivityTypeItemClass`. Published examples and
`ospd-dtaas-register` use the current form. Will the old IRI remain valid?

### 11. Which URLs are canonical?

The ATR and RIM `register.json` files respond on both `geonovum-labs.github.io` and
`ogcincubator.github.io`. Will the first stay available? Is `ogcincubator` the one to import?

The ATR sources (`0c52c0e`: `bblocks-config.yaml` and `build/register.json`) import the model from
`ogcincubator.github.io`. The `register.json` served on `ogcincubator.github.io/activity-type-register`
on 2026-11-09 (last modified 2026-11-04 10:27 GMT) still imports it from `geonovum-labs.github.io`: the
deployment looks older than the sources. In a build, that transitive import is loaded last and
replaces our direct `ogcincubator` import for every `ogc.rim.*` block; we map it back locally for
now. Could the published ATR be redeployed from current master?

`https://w3id.org/ogc/rim/` and `https://w3id.org/ogc/rim/activity-type/ActivityType` returned 404 on
2026-11-05. Is that redirect planned?

## Register actions

### 12. Which action type amends a proposal in place?

The model has no action type for amending a proposal in place, before any control-body decision. We
therefore define `gp:amendmentAction` in our register specification, as `core-ontology/skos.ttl`
line 47 allows ("a register may define further action types in its register specification"), and
always classify such an action `clarifying` or `substantive`. Will the model provide a common type
for this, and under which IRI? We would replace ours with it.

### 13. In which direction does `rim:supersedes` point?

`rim:supersedes` and `rim:supersededBy` both go from `rim:RegisterItem` to `rim:RegisterItem`, with no
comment and no `owl:inverseOf`. We read `A rim:supersedes B` as "A replaces B", from the label.

We need it across registers. Our data types register withdraws 19 string formats that now live as
format items in a separate formats register, which depends on it. `rim:supersededBy` from the withdrawn
item fails `rim:RegisterItemShape`, because the target is not typed in the data types graph, and that
register must not depend on the formats one. We therefore put `rim:supersedes` on the new format item.

Is our reading of the direction right? Could the two properties be declared inverse of each other?

## Possible defects

No answer is needed unless you disagree.

- `rim:affectedProperty` has range `rdf:property`; `rdf:Property` looks intended.
- `activity-types-schema/context.jsonld` declares `rim` as `https://w3id.org/ogc/rim#`, while the
  ontology uses `https://w3id.org/ogc/rim/`.
- The ATR JSON examples pass SHACL with an empty focus list for `rim:RegisterItemShape`. We found that list
  unreliable, so we cannot say whether the shape ran. Those examples also use `itemClass: rim:RegisterItemClass`, and `buffer.json`
  uses plain strings such as `point` for entity types.
- The ATR `abstract` in `bblocks-config.yaml` describes "Generic Profiles". That text comes from our
  register and may not be intended.
- `core-ontology` links to `iso.org/standard/86261`, while search results point to `87753` for
  ISO 19135:2026. We could not open either page.
- The RIM README still mentions `_sources/rim`, `registered-item` and `_sources/activity-type`, which
  have moved or been renamed.
