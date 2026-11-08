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

- **Content register, no concept plane.** The Registered Item Model lets a register separate
  meaning (`rim:Concept`/`rim:ConceptVersion`) from representation (`rim:RegisterItem`). Here all
  three tiers are register items with their own `prefLabel`/`definition`. The specification records
  this choice, to be reviewed if a concept plane of operations is created later.
- **Depends on the model's JSON binding.** The `allOf` above needs the Registered Item Model's
  `register-item` schema not to pin `type` to `"rim:RegisterItem"` and its context to map the
  `rim:*` terms. Both were contributed by GeoLabs (2026-10-26) and are part of the published model
  at [ogcincubator/registered-item-model](https://github.com/ogcincubator/registered-item-model)
  since 2026-10-28; this register imports it by URL.

## Register position

Governance layer over all four tiers' first three (OGC 14-065 WPS 2.0.2 §7.5): Concept ->
Generic Profile -> Implementation Profile. Implementations (instance level) live in
`bblocks-process-profiles` and are not items of this register.
