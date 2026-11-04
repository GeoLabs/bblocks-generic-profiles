
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

## Activity-type register is not this register's tier 3

This register contains provider-independent Implementation Profiles (tier 3). The process types
that classify real execution records belong with the deployable process profiles (tier 4), in
`bblocks-process-profiles`. There, `ospd.process-profiles.process-type` already supplies the IRI
that provenance `Activity` records carry as their `activityType`. It is the natural place to align
those process types with the Registered Item Model's `acttype:ActivityType`; this register does not
assert a speculative cross-link.

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

- **Content register, no concept plane.** ISO 19135:2026 lets a register separate meaning
  (`rim:Concept`/`rim:ConceptVersion`) from representation (`rim:RegisterItem`). Here all three
  tiers are register items with their own `prefLabel`/`definition` -- the lightest conformant
  register type. Whether Process Concepts should rather be the concept plane that Generic
  Profiles `rim:realizes` is left open; the current choice is the one that claims least.
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

