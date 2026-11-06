# Implementation Profile and Activity Type: relation, not sub-class

Status: design note, 2026-10-30. Records why the proposed tier-3 link was removed and why the process-type entries in `bblocks-process-profiles` are the natural integration point for `acttype:ActivityType`. Statements about other registers were checked against their published sources.

## The two notions

| | Implementation Profile (`bblocks-generic-profiles`) | Activity type (`activity-type-register`) |
|---|---|---|
| Model | OGC 14-065 WPS 2.0.2 §7.5.3 | Registered Item Model, activity-type profile (`acttype:`) |
| Describes | a **kind of process** by its signature bound to standard formats, implementable by several providers | a **kind of process** by the PROV relations its activities have: what they use and generate, who runs them, which plan they follow |
| Class | `gp:ProcessConcept` / `gp:GenericProfile` / `gp:ImplementationProfile`, each `rdfs:subClassOf rim:RegisterItem` and `skos:Concept` | `acttype:ActivityType rdfs:subClassOf rim:RegisterItem`; `geoproc:GeoprocessingActivityType rdfs:subClassOf acttype:ActivityType` |
| Item class | `gpic:implementation-profile` (`.../def/item-class/implementation-profile`) | `acttype:activityTypeItemClass` |
| Register | `https://geolabs.github.io/bblocks-generic-profiles/def/register`, owner/manager GeoLabs | the activity-type register (Geonovum-labs) |
| Namespace | `gp: https://geolabs.github.io/bblocks-generic-profiles/def/` | `acttype: https://w3id.org/ogc/rim/activity-type/`, `geoproc: https://w3id.org/ogc/rim/geoprocessing/` |

Both are `rim:RegisterItem`s of the same base model (ISO 19135:2026 via the Registered Item Model),
each governed by its own register. Seen from a process, they look like two descriptions of the same
kind of thing: the WPS one says *what goes in and out, in which formats*; the PROV one says *what
the run uses and produces, and who does it*.

## Why a direct tier-3 link was withdrawn

The proposed `gp:activityType` on `gp:ImplementationProfile` would have been:

- `rdfs:subPropertyOf rim:relatedItem` -- the Registered Item Model's extensible relation between
  two register items (both ends are `rim:RegisterItem`s);
- range `acttype:ActivityType`;
- optional, at most one, an IRI (`gp:ImplementationProfileShape`: `sh:nodeKind sh:IRI ;
  sh:maxCount 1`);
- carried in JSON as `activityType`, mapped by the Implementation Profile context.

It is set only where an activity type of the same harmonised operation has actually been
registered. On 2026-10-30 that is true of **none** of this register's Implementation Profiles: the
activity types registered so far -- e.g. `geonovum.dtaas.ogcapi.processes.3dgi.convert_format` in
`ospd-dtaas-register`, whose example is the deployed process
`https://processes.staging.roofer-online.nl/ogcapi/processes/roofer:convert_format:v1` -- describe
**specific deployed processes**, i.e. this project's Implementation (instance level) tier
(`bblocks-process-profiles`), not provider-independent operations. The property is therefore
declared and documented, and no entry carries it yet; the base block's clearly-labelled placeholder
example shows the shape of its use.

## Why a tier-3 Implementation Profile cannot be an ActivityType

A tempting alternative is to make `gp:ImplementationProfile rdfs:subClassOf acttype:ActivityType`:
an Implementation Profile *is* an activity type. Under the current SHACL contracts this is
mechanically impossible:

1. **Registered Item Model**, `rim:RegisterItemShape` (`core-ontology/shapes.shacl`):
   `rim:itemClass` has exactly one value.
2. **This register**, `gp:ImplementationProfileShape` (`_sources/register/shapes.shacl`):
   that value must be `gpic:implementation-profile`.
3. **Activity-type register**, `acttype:ActivityTypeShape` (`activity-types/shapes.shacl`):
   for an `acttype:ActivityType` the value must be `acttype:activityTypeItemClass`.

With the sub-class axiom, every Implementation Profile is also an `acttype:ActivityType`; rules 2
and 3 then require two different values for a property rule 1 limits to one. No value satisfies
all three. Each entry fails validation. The reason is the RIM's governance model: the item class
says which register governs the item, and one item belongs to one register.

The `geoproc:GeoprocessingActivityTypeShape` adds another constraint **only for geoprocessing
activity types**: at least one `acttype:usedEntityType` or `acttype:generatedEntityType` must be a
GeoSPARQL spatial class. This is not a requirement of the root `acttype:ActivityType`, and is not
why the tier-3 sub-class is impossible; the item-class conflict already rules it out.

## The better integration point: process-type at tier 4

`bblocks-process-profiles` already has `ospd.process-profiles.process-type`: its description says a
process type classifies PROV activities, and `scripts/generate.py` assigns that type IRI as the
`rdf:type` of each generated `prov:Activity`. This is the deployed-process (tier-4) level that
matches the activity types in `ospd-dtaas-register`. It is the appropriate place to align
`process-type` itself with `acttype:ActivityType`, rather than the provider-independent tier-3
Implementation Profile.

That alignment is now being developed in `bblocks-process-profiles`. It gives the process-type entry
the ActivityType item class, RIM core and addition action, while retaining its IRI as the class used
by provenance. The proposed `gp:activityType` relation on tier 3 has been removed. No other
repository is changed by this note.

## Pointers

- `bblocks-process-profiles`: `_sources/process-type/`, `scripts/generate.py` (`process_type_entry` and provenance `activityType`).
- Registered Item Model: <https://ogcincubator.github.io/registered-item-model/>
  (`_sources/core-ontology/shapes.shacl`).
- Activity-type register: <https://ogcincubator.github.io/activity-type-register/>
  (`_sources/activity-types/{ontology.ttl,shapes.shacl}`,
  `_sources/geoprocessing-activity-types/shapes.shacl`).
- Worked integration: <https://geonovum-labs.github.io/ospd-dtaas-register/>.
