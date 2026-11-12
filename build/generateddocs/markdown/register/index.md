
# Generic Process Profiles register (ISO 19135:2026) (Model)

`generic-profiles.register` *v0.1*

This register described with the Registered Item Model (ISO 19135:2026): one rim:Register, three rim:RegisterItemClasses (Process Concept, Generic Profile, Implementation Profile) and the three owl:Classes, each a sub-class of rim:RegisterItem, that every entry of the corresponding tier is typed with. A profile of ogc.rim.schemas.register-item-class, following the same pattern as that register's own activity-type profile.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

This register, described with the [Registered Item Model](https://ogcincubator.github.io/registered-item-model/)
(ISO 19135:2026) -- a profile of `ogc.rim.schemas.register-item-class`, built the
same way as that register's own `activity-type` profile.

## What it adds

Nothing to the register model, and nothing to the three tiers' own content: it names what was
already there in ISO 19135:2026 terms, so that this register's management metadata joins the
same graph as any other register mapped onto the model.

| ISO 19135:2026 | Here | IRI |
|---|---|---|
| `rim:Register` | this register | `https://geolabs.github.io/bblocks-generic-profiles/def/register` |
| `rim:RegisterItemClass` | Process Concept | `.../def/item-class/process-concept` |
| `rim:RegisterItemClass` | Generic Profile | `.../def/item-class/generic-profile` |
| `rim:RegisterItemClass` | Implementation Profile | `.../def/item-class/implementation-profile` |
| `rim:RegisterItem` sub-class | `gp:ProcessConcept` -- what a Concept entry's JSON `type: ProcessConcept` maps to | `.../def/ProcessConcept` |
| `rim:RegisterItem` sub-class | `gp:GenericProfile` -- JSON `type: GenericProfile` | `.../def/GenericProfile` |
| `rim:RegisterItem` sub-class | `gp:ImplementationProfile` -- JSON `type: ImplementationProfile` | `.../def/ImplementationProfile` |
| `rim:relatedItem` sub-property | `gp:refinesGenericProfile` (Implementation Profile -> Generic Profile) | |
| `rim:relatedItem` sub-property | `gp:activityType` (Implementation Profile -> activity type) | |
| (not a RIM relation) | `gp:representation` (Implementation Profile input/output -> `df:Representation` of `bblocks-data-formats`, decision D6) | |
| `acttype:ActivityType` (Activity Type Register) | the meaning of one operation, `generic-profiles.activity-type.*`, item class `acttype:activityTypeItemClass` | `.../def/activity-type/<operation>` |

The three item types remain `skos:Concept`s as well (that is what they were typed as before this
block existed, and what `prefLabel`/`definition`/`inScheme`/`broader` presuppose), so nothing
that consumed the SKOS view changes.

Every entry of the three tiers carries, in its JSON, the ISO 19135:2026 required core --
`objectIdentifier` (its own IRI), `itemClass`, `inRegister`, `validityStatus`,
`publicationStatus`. Each tier's base schema is an `allOf` of
`bblocks://ogc.rim.schemas.register-item` (which requires and types that core and
supplies the JSON-LD mapping of every `rim:*` term, including `"valid"` -> `rim:valid`) plus the
tier's own properties, of which only `itemClass` and `inRegister` are pinned per tier. This
register's contexts therefore declare no `rim:` term of their own. The base `rim:RegisterItemShape`
then applies to every entry through the ontology closure (`gp:ProcessConcept rdfs:subClassOf
rim:RegisterItem`, etc.), and `shapes.shacl` here only adds the per-tier item class / register
pins and the presence of the tier-to-tier link.

The Concept tier's JSON `type` is `ProcessConcept`, not `Concept`: the inherited context already
binds `Concept` to `rim:Concept` (the model's concept-plane class), and the assembled context
would otherwise carry two meanings for one term.

## Register specification

`gp:specification` (`ontology.ttl`), linked from `gp:register` by `rim:hasSpecification`, is this
register's `rim:RegisterSpecification`: scope, register type, roles, identifier and version rules,
eligibility, and what counts as a substantive change. GeoLabs SARL is the control body for now, with
the stated intention of delegating that role to the OGC or to an OSPD working group.

`rim:definesSubstantiveChange` reads:

> A change is substantive when a register user may have to change their data, profiles or processes because of it, or when it changes what an item means. Any other change to an existing item is clarifying.

The version rule (a substantive change creates a new item or version, a clarifying change keeps
them) is specific to this project's registers and does not come from ISO 19135. The rule for
proposals is what applies to every item today:

> While an item is a proposal, with no control-body decision recorded, it is amended in place, with a classified `rim:RegisterAction`. The substantive rule applies once it has been accepted.

The classified action of that rule has the type `gp:amendmentAction`, defined by this
specification: an in-place change to a proposal, with no control-body decision recorded, always
classified `clarifying` or `substantive`. The Registered Item Model has no such type and lets a
register specification define one; this type is specific to this register and will be replaced if
the model defines one. No shape enforces the classification of such an action: the model's
`rim:RegisterActionShape` only limits it to one.

The criteria for proposers other than GeoLabs have not been set.

## Activity types: the meaning of each operation

An Implementation Profile is not an activity type: `rim:RegisterItemShape` allows one item class per
item, and `gpic:implementation-profile` and `acttype:activityTypeItemClass` are two
(`docs/implementation-profile-vs-activity-type.md`). The meaning of an operation is therefore held by
a separate item of this register, one per operation (decision D3, 2026-11-05):
`generic-profiles.activity-type.*`, typed `acttype:ActivityType`, of the Activity Type Register's item
class, in `gp:register`. It carries the operation's definition, the standards that define it (Simple
Feature Access, SQL/MM `ST_*` names, WCPS, the literature of terrain indices) and its illustrations.

Each Implementation Profile links to it with `activityType` (`gp:activityType`, a sub-property of
`rim:relatedItem`, exactly one IRI). The Implementation Profile keeps the signature, the
representations and domain keywords (decision D4).

The process types of deployed processes (tier 4, `ospd.process-profiles.process-type` in
`bblocks-process-profiles`) are activity types too. How they relate to these items, and how a run is
typed, is not settled here: it waits for the answers of the model maintainers
(`docs/questions-for-rim-atr-maintainers.md`, decision D8).

## Entry into the register: a proposed addition, not a status

Entries used to carry a `status` from the ISO 19135-1:**2015** list (`submitted`, `valid`,
`invalid`, `superseded`, `retired`). It is gone: ISO 19135:2026 replaces that single list with two
independent concerns (validity, publication), makes supersession a relation, and records how an
item came to be in the register as a `rim:RegisterAction`. Every entry now carries:

- `hasAction`: one action of type `addition` (`rim:additionAction`), whose `proposer` is
  `https://geolabs.github.io/bblocks-generic-profiles/def/geolabs` (the register's owner and
  manager), `startedAtTime` the `dateTimeAddition` its building block declares, and `appliesTo` the
  entry itself. The action's own IRI is `<entry id>/actions/addition`;
- `validityStatus: invalid` and `publicationStatus: published`: no control-body decision has been
  recorded, so the entry is visible but not in force.

`gp:AdditionProposalShape` rejects an entry with no action at all
(`tests/item-without-addition-fail.ttl`) and one whose addition has no proposer
(`tests/addition-without-proposer-fail.ttl`; the plain count and the qualified count are both
needed, because pyshacl 0.21.0 does not raise `sh:qualifiedMinCount` on a path with no values). A later decision is a further `rim:RegisterAction`
(publish, invalidation, supersession) added next to the first, not an edit of it.

What is asserted and what is not: the date is the building block's own declared `dateTimeAddition`
(2026-09-30 to 2026-10-08), which does not match the date of the entry's first commit in this
repository (2026-10-07 to 2026-10-09, all 55 differ, some in each direction): the declared date is
kept, the git date is not claimed. `invalid` is a reading of "proposed, awaiting a decision", not
something the model states -- to settle with the model's authors.

## Two deliberate limits

- **Content register, no concept plane.** The Registered Item Model lets a register separate
  meaning (`rim:Concept`/`rim:ConceptVersion`) from representation (`rim:RegisterItem`). Here all
  three tiers are register items with their own `prefLabel`/`definition`. The specification records
  this choice, to be reviewed if a concept plane of operations is created later. The activity types
  live here pending decision D8; the register stays a content register meanwhile, to be reviewed
  with the maintainers' answers.
- **Depends on the model's JSON binding.** The `allOf` above needs the Registered Item Model's
  `register-item` schema not to pin `type` to `"rim:RegisterItem"` and its context to map the
  `rim:*` terms. Both were contributed by GeoLabs (2026-10-26) and are part of the published model
  at [ogcincubator/registered-item-model](https://github.com/ogcincubator/registered-item-model)
  since 2026-10-28; this register imports it by URL.

## Register position

Governance layer over all four tiers' first three (OGC 14-065 WPS 2.0.2 §7.5): Concept ->
Generic Profile -> Implementation Profile. Implementations (instance level) live in
`bblocks-process-profiles` and are not items of this register.

## Examples

### The register, its item classes and its specification
The ontology of this block as published, validated here as data: this is what checks
`gp:register` and `gp:specification` against the model's shapes.

#### turtle
```turtle
@prefix gp:   <https://geolabs.github.io/bblocks-generic-profiles/def/> .
@prefix gpic: <https://geolabs.github.io/bblocks-generic-profiles/def/item-class/> .
@prefix rim:  <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix dct:  <http://purl.org/dc/terms/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl:  <http://www.w3.org/2002/07/owl#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix prov: <http://www.w3.org/ns/prov#> .

#################################################################
# Ontology metadata
#
# A profile of the Registered Item Model (ISO 19135:2026) for this
# register. It adds nothing to the register model itself: it names the
# register, its three item classes, and the three classes of item --
# one per tier of OGC 14-065 WPS 2.0.2 §7.5 held here -- as sub-classes
# of rim:RegisterItem, so that the base rim:RegisterItemShape applies to
# every entry. Follows the pattern of the Registered Item Model's own
# activity-type profile.
#################################################################

gp: a owl:Ontology ;
    owl:imports rim: ;
    dct:title "Generic Process Profiles register" ;
    dct:description "Registered Item Model profile of the GeoLabs generic-profiles register: Process Concepts, Generic Profiles and Implementation Profiles (OGC 14-065 WPS 2.0.2 §7.5) as ISO 19135:2026 register items." ;
    dct:creator "GeoLabs SARL" ;
    dct:license <https://www.apache.org/licenses/LICENSE-2.0> .

#################################################################
# The register
#
# A content register, as the Registered Item Model uses the term: items
# carry their own name and definition (skos:prefLabel / skos:definition),
# there is no separate concept plane. gp:specification records that
# choice, to be reviewed if a concept plane of operations is created
# later (rim:Concept / rim:ConceptVersion realised by the items).
#################################################################

gp:register a rim:Register ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-generic-profiles/def/register"^^xsd:anyURI ;
    rim:functionalIdentifier "https://geolabs.github.io/bblocks-generic-profiles/"^^xsd:anyURI ;
    dct:title "Generic Process Profiles"@en ;
    dct:description "A general-purpose, provider-independent vocabulary of process Concepts, Generic Profiles and Implementation Profiles (OGC 14-065 WPS 2.0.2 §7.5), published as an OGC Building Blocks register."@en ;
    rim:registerOwner gp:geolabs ;
    rim:registerManager gp:geolabs ;
    rim:controlBody gp:geolabs ;
    rim:hasSpecification gp:specification ;
    rim:runsOn gp:registerSystem .

# The register specification. rim:definesSubstantiveChange is the text validated for all the
# registers of this project, word for word. The version rule below is specific to these registers
# and does not come from ISO 19135. tests/specification-without-title-fail.ttl proves that
# rim:RegisterSpecificationShape runs, and examples.yaml validates this file against it.
gp:specification a rim:RegisterSpecification ;
    dct:title "Generic Process Profiles register specification"@en ;
    dct:description
        "Scope. This register holds three item classes, the first three tiers of OGC 14-065 WPS 2.0.2 §7.5: Process Concept, Generic Profile and Implementation Profile. It also holds one activity type per operation (acttype:ActivityType, of the item class of the Activity Type Register): the meaning of the operation, to which its Implementation Profiles point with gp:activityType (decision D3): one or more per activity type. Real deployed or deployable processes, the Implementation (instance level), are not items of this register."@en ,
        "Register type. A content register, as the Registered Item Model uses the term: items carry their own name and definition, and there is no concept plane. To be reviewed if a concept plane of operations is created later. The activity types, one per operation, live in this register pending decision D8 on how the Activity Type Register is integrated; the register stays a content register meanwhile, to be reviewed with the answers of the Registered Item Model and Activity Type Register maintainers."@en ,
        "Roles. GeoLabs SARL is the register owner, the register manager and, for now, the control body. GeoLabs intends to delegate the control body role to the OGC or to an OSPD working group."@en ,
        "Identifiers. The object identifier of an item is its IRI, https://geolabs.github.io/bblocks-generic-profiles/def/<tier>/<name>, with <tier> one of concept, generic-profile, implementation-profile or activity-type. An object identifier never redirects; only a functional identifier may. The identifier of a published item changes only by an explicit decision."@en ,
        "Versions. An addition is an action of type addition, with no classification. A substantive change creates a new item or a new version, linked by rim:supersededBy, with an action classified substantive. A clarifying change keeps the item and its version, with an action classified clarifying. The classification correctional is not available. An item is retired by unpublishing it, not by deleting it."@en ,
        "What is substantive here. Substantive: a role added or removed, a change of dataType, cardinality or representation. Clarifying: description, keywords, documentary links. For an activity type: substantive, a change of its parent class or of an entity type; clarifying, its label, a rewording of its definition with the same meaning, its sources."@en ,
        "Proposals. While an item is a proposal, with no control-body decision recorded, it is amended in place, with a classified `rim:RegisterAction`. The substantive rule applies once it has been accepted."@en ,
        "Amendment. gp:amendmentAction is the action type of an in-place change to a proposal, an item with no control-body decision recorded. Such an action is always classified, clarifying or substantive: it is the classified rim:RegisterAction of the rule for proposals. This type is specific to this register and will be replaced if the Registered Item Model defines one."@en ,
        "Eligibility. An item is eligible for an item class if it carries what the class allows and nothing it excludes. Process Concept: the meaning of a group of operations, with no input, output, format or tool. Generic Profile: a signature in dataType concepts, with no format and no tool. Implementation Profile: a signature, representations, an activityType and domain keywords, with no tool, host or testbed. Existing items reach this state as amended proposals. Activity type: the meaning of one operation, its definition, the standards that define it and its illustrations, and the GeoSPARQL classes of the entities its activities use or generate, with no named role, format or tool; one per operation, of the item class of the Activity Type Register, a sub-class of geoproc:GeoprocessingActivityType with at least one GeoSPARQL spatial entity type. GeoLabs is the only proposer recorded so far; no criteria for other proposers have been set."@en ;
    rim:definesSubstantiveChange "A change is substantive when a register user may have to change their data, profiles or processes because of it, or when it changes what an item means. Any other change to an existing item is clarifying." .

# rim:actionType is required and the Registered Item Model has no type for an in-place change of a
# proposal; it lets a register specification define further action types. Defined by
# gp:specification, specific to this register.
gp:amendmentAction a rim:RegisterActionType , skos:Concept ;
    rdfs:isDefinedBy gp: ;
    skos:prefLabel "amendment"@en ;
    skos:definition "An in-place change to a proposal, an item with no control-body decision recorded. Always classified, clarifying or substantive."@en .

gp:geolabs a prov:Organization ;
    rdfs:label "GeoLabs SARL" ;
    rdfs:seeAlso <https://www.geolabs.fr/> .

# The register system is the OGC Building Blocks pipeline (bblocks-postprocess + GitHub
# Pages), kept distinct from the register itself as ISO 19135:2026 requires.
gp:registerSystem a rim:RegisterSystem ;
    rdfs:label "OGC Building Blocks register (bblocks-postprocess, GitHub Pages)" ;
    rdfs:seeAlso <https://github.com/GeoLabs/bblocks-generic-profiles/> .

#################################################################
# Item classes -- the unit validation rules attach to (ISO 19135:2026)
#################################################################

gpic:process-concept a rim:RegisterItemClass ;
    rdfs:isDefinedBy gp: ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/process-concept"^^xsd:anyURI ;
    dct:title "Process Concept"@en ;
    dct:description "WPS 2.0.2 §7.5.1: high-level documentation about a general group of processes; no input, output, format or implementation. Items of this class are gp:ProcessConcept instances."@en ;
    rim:definedIn gp:register ;
    rim:validatedBy gp:ProcessConceptShape .

gpic:generic-profile a rim:RegisterItemClass ;
    rdfs:isDefinedBy gp: ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/generic-profile"^^xsd:anyURI ;
    dct:title "Generic Profile"@en ;
    dct:description "WPS 2.0.2 §7.5.2: the abstract signature (named inputs/outputs, multiplicity, abstract data type) of one or more operations; no data format. Items of this class are gp:GenericProfile instances."@en ;
    rim:definedIn gp:register ;
    rim:validatedBy gp:GenericProfileShape .

gpic:implementation-profile a rim:RegisterItemClass ;
    rdfs:isDefinedBy gp: ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/implementation-profile"^^xsd:anyURI ;
    dct:title "Implementation Profile"@en ;
    dct:description "WPS 2.0.2 §7.5.3: a Generic Profile bound to standard data formats, implementable by multiple providers; not any one deployment. Items of this class are gp:ImplementationProfile instances."@en ;
    rim:definedIn gp:register ;
    rim:validatedBy gp:ImplementationProfileShape .

#################################################################
# Item types -- what the JSON `type` of each tier maps to
#
# Each is both a rim:RegisterItem (so the base shape applies) and a
# skos:Concept (what the three tiers were already typed as before this
# profile existed, and what skos:prefLabel / skos:definition /
# skos:inScheme / skos:broader on them presuppose).
#################################################################

gp:ProcessConcept a owl:Class ;
    rdfs:subClassOf rim:RegisterItem , skos:Concept ;
    rdfs:isDefinedBy gp: ;
    rdfs:label "Process Concept" ;
    rdfs:comment "A register item of item class gpic:process-concept (OGC 14-065 WPS 2.0.2 §7.5.1)." .

gp:GenericProfile a owl:Class ;
    rdfs:subClassOf rim:RegisterItem , skos:Concept ;
    rdfs:isDefinedBy gp: ;
    rdfs:label "Generic Profile" ;
    rdfs:comment "A register item of item class gpic:generic-profile (OGC 14-065 WPS 2.0.2 §7.5.2)." .

gp:ImplementationProfile a owl:Class ;
    rdfs:subClassOf rim:RegisterItem , skos:Concept ;
    rdfs:isDefinedBy gp: ;
    rdfs:label "Implementation Profile" ;
    rdfs:comment "A register item of item class gpic:implementation-profile (OGC 14-065 WPS 2.0.2 §7.5.3)." .

#################################################################
# Relations between items
#
# ISO 19135:2026 makes relations extensible as sub-properties of
# rim:relatedItem. The tier-to-tier links this register already had are
# declared as such; skos:broader (Generic Profile -> Process Concept) is
# left as is, since asserting a sub-property axiom on SKOS's own term is
# not this ontology's place -- the same link is also carried by the WPS
# Table 22 `metadata` reference on the item.
#################################################################

gp:refinesGenericProfile a owl:ObjectProperty ;
    rdfs:subPropertyOf rim:relatedItem ;
    rdfs:isDefinedBy gp: ;
    rdfs:label "refines Generic Profile" ;
    rdfs:comment "Relates an Implementation Profile to the Generic Profile whose signature it binds to formats (WPS 2.0.2 §7.5.3, Table 21)." ;
    rdfs:domain gp:ImplementationProfile ;
    rdfs:range gp:GenericProfile .

# Decisions D3 and D4 (2026-11-05): the meaning of the operation an Implementation Profile binds to
# formats is a separate acttype:ActivityType item of this register (generic-profiles.activity-type.*).
# An Implementation Profile cannot be that item itself: rim:RegisterItemShape allows one item class
# per item (docs/implementation-profile-vs-activity-type.md).
gp:activityType a owl:ObjectProperty ;
    rdfs:subPropertyOf rim:relatedItem ;
    rdfs:isDefinedBy gp: ;
    rdfs:label "activity type" ;
    rdfs:comment "Relates an Implementation Profile to the activity type that holds the meaning of its operation: definition, standards, illustrations." ;
    rdfs:domain gp:ImplementationProfile ;
    rdfs:range <https://w3id.org/ogc/rim/activity-type/ActivityType> .

# Decision D6 (2026-11-05): an Implementation Profile input or output names its exchange format by
# reference, not by a copied JSON Schema: one or more representations of the data-formats register,
# each realizing a version of the role's data type and pointing to one format. The schema itself
# stays at tier 4, as the deployed process serves it.
gp:representation a owl:ObjectProperty ;
    rdfs:isDefinedBy gp: ;
    rdfs:label "representation" ;
    rdfs:comment "Relates an input or output of an Implementation Profile to a representation (df:Representation) of the data-formats register in which it is exchanged: Table 21 Data format (D) of OGC 14-065 WPS 2.0.2, by IRI." ;
    rdfs:range <https://w3id.org/geolabs/ospd/data-formats/Representation> .


#################################################################
# Entry into the register: a proposed addition
#
# Every entry carries one rim:RegisterAction of type rim:additionAction,
# proposed (rim:proposer) by gp:geolabs, at the date the entry's building
# block declares as its addition (dateTimeAddition). No control-body
# decision has been recorded, so entries are rim:invalid (not in force)
# and rim:published (visible): the state of a proposed addition awaiting
# a decision, expressed with the ISO 19135:2026 pair rather than a
# status of our own. A later decision is a further rim:RegisterAction
# (publish / invalidation / supersession), not a change of this one.
# gp:AdditionProposalShape (shapes.shacl) requires the addition and its
# proposer on every entry.
#################################################################

```


### One chain of this register as ISO 19135:2026 register items
The register, its three item classes and one item per tier -- the real chain
*Vector Geometry Processing* (Process Concept) -> *Binary spatial predicate* (Generic
Profile) -> *Intersects* (Implementation Profile) -- reduced to the register-model
properties only. The full entries, with their WPS Table 21 `inputs`/`outputs`, are the JSON
examples of `generic-profiles.concept.vector-geometry-processing`,
`generic-profiles.generic-profile.binary-spatial-predicate` and
`generic-profiles.implementation-profile.intersects`; their JSON-LD context maps them onto
exactly these triples.

#### turtle
```turtle
gp:register a rim:Register ;
    dct:title "Generic Process Profiles"@en .

gpic:process-concept a rim:RegisterItemClass ;
    dct:title "Process Concept"@en ;
    rim:definedIn gp:register .

gpic:generic-profile a rim:RegisterItemClass ;
    dct:title "Generic Profile"@en ;
    rim:definedIn gp:register .

gpic:implementation-profile a rim:RegisterItemClass ;
    dct:title "Implementation Profile"@en ;
    rim:definedIn gp:register .

<https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing>
    a gp:ProcessConcept ;
    skos:prefLabel "Vector Geometry Processing" ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"^^xsd:anyURI ;
    rim:itemClass gpic:process-concept ;
    rim:inRegister gp:register ;
    rim:validityStatus rim:invalid ;
    rim:publicationStatus rim:published ;
    rim:hasAction <https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing/actions/addition> .

<https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing/actions/addition>
    a rim:RegisterAction ;
    rim:actionType rim:additionAction ;
    rim:proposer gp:geolabs ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing> ;
    prov:startedAtTime "2026-09-30T00:00:00Z"^^xsd:dateTime .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate>
    a gp:GenericProfile ;
    skos:prefLabel "Binary spatial predicate" ;
    skos:broader <https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing> ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate"^^xsd:anyURI ;
    rim:itemClass gpic:generic-profile ;
    rim:inRegister gp:register ;
    rim:validityStatus rim:invalid ;
    rim:publicationStatus rim:published ;
    rim:hasAction <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/actions/addition> .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/actions/addition>
    a rim:RegisterAction ;
    rim:actionType rim:additionAction ;
    rim:proposer gp:geolabs ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate> ;
    prov:startedAtTime "2026-09-30T00:00:00Z"^^xsd:dateTime .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersects>
    a gp:ImplementationProfile ;
    skos:prefLabel "Intersects" ;
    gp:refinesGenericProfile <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate> ;
    gp:activityType <https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/intersects> ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersects"^^xsd:anyURI ;
    rim:itemClass gpic:implementation-profile ;
    rim:inRegister gp:register ;
    rim:validityStatus rim:invalid ;
    rim:publicationStatus rim:published ;
    rim:hasAction <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersects/actions/addition> .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersects/actions/addition>
    a rim:RegisterAction ;
    rim:actionType rim:additionAction ;
    rim:proposer gp:geolabs ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersects> ;
    prov:startedAtTime "2026-09-30T00:00:00Z"^^xsd:dateTime .

```

## Sources

* [ISO 19135:2026, Geographic information — Registration and register governance](https://www.iso.org/standard/86261.html)
* [Registered Item Model (OGC Building Block)](https://ogcincubator.github.io/registered-item-model/)
* [OGC 14-065 WPS 2.0.2 Interface Standard Corrigendum 2, §7.5 Process profiles](https://docs.ogc.org/is/14-065/14-065.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/register`

