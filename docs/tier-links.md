# Links between tiers: one canonical relation, the rest derived

Status: proposal (action A3.5 of the tier separation, 2026-11-09). Nothing in the model changes with
this note. It asks for a decision.

## What links the tiers today

The same parent-child link between two tiers is written up to five times, in four forms. Measured on
branch `planes/phase-3` (2026-11-09):

| Form | Where | Generic Profile -> Process Concept | Implementation Profile -> Generic Profile |
|---|---|---|---|
| `broader` (`skos:broader`) | item JSON, RDF | 17 | -- |
| `refinesGenericProfile` (`gp:refinesGenericProfile`, sub-property of `rim:relatedItem`) | item JSON, RDF | -- | 31 |
| `metadata` with a Table 22 `role` (`.../process-profile/concept`, `generic`) | item JSON, RDF (`proc:metadata`) | 17 `concept` | 31 `concept` + 31 `generic` |
| `metadata` with a role of this register (`role/generic-input`, `generic-output`) | each input and output | -- | 84 |
| `isProfileOf` | `bblock.json`, register metadata, not RDF of the item | 17 | 31 (plus the base block of each tier: 96 values in total) |
| `const` pins of the same values | each block's `schema.yaml` | 17 | 31, and the role references |

No copy disagrees with another today: for every Generic Profile the `concept` reference equals
`broader`, and for every Implementation Profile the `generic` reference equals
`refinesGenericProfile` and its `concept` reference equals the `broader` of that Generic Profile.
They agree because they were written together, and nothing checks it: a change to one copy would not
be caught.

The tier-4 link, `implementsProfile` on `ospd.process-profiles.process-type` and `isProfileOf` on the
process profile block, lives in `bblocks-process-profiles` and follows the same pattern.

`activityType` (decisions D3 and D4) is not a tier link: it relates a profile to the meaning of its
operation, outside the chain. It is left out of this proposal.

## Proposal

### One canonical relation per pair of adjacent tiers

Each is an RDF property, sub-property of `rim:relatedItem`, written once, in the item's JSON:

| Child -> parent | Canonical relation | Today |
|---|---|---|
| Generic Profile -> Process Concept | `gp:refinesProcessConcept` (new, one or more) | `broader` |
| Implementation Profile -> Generic Profile | `gp:refinesGenericProfile` (exactly one) | unchanged |
| Implementation (tier 4) -> Implementation Profile | `implementsProfile` | unchanged, in `bblocks-process-profiles`; its declaration as a sub-property of `rim:relatedItem` waits for phase 4 and D8 |

`skos:broader` cannot be the canonical relation: this register does not assert axioms on SKOS terms
(`register/ontology.ttl`), so it cannot be declared a sub-property of `rim:relatedItem`.

### Derivation rules

Everything else is derived from the canonical relations and never written by hand:

1. `broader` (`skos:broader`) of a Generic Profile = its `gp:refinesProcessConcept`. It stays in the
   JSON for SKOS consumers.
2. Table 22 `metadata` on an item = one reference per ancestor, the role named after the ancestor's
   tier: `concept` for each Process Concept reached through the chain, `generic` for the Generic
   Profile, `implementation` for the Implementation Profile (tier 4 only). The `title` is
   "<tier>: <prefLabel of the ancestor>".
3. Role references on an input or output named `n` = `<parent id>/inputs/n` (or `/outputs/n`) with
   `role/generic-input` (`-output`) at tier 3, and `role/implementation-input` (`-output`) at tier 4,
   for each role the parent declares. A role of the child with no counterpart in the parent is an
   addition (Table 21 footnote b) and gets none.
4. `isProfileOf` of a block = [the base block of its tier, the block of its canonical parent]. The
   block identifier follows from the parent's IRI (`generic-profiles.<tier>.<name>`).
5. The `const` pins of each `schema.yaml` are generated from the same values.

### How to keep it so

Two options, not exclusive:

- **Generate** rules 1 to 5, as `bblocks-process-profiles` already does for tier 4
  (`scripts/generate.py`, `inherited_process_description`): a script reads the canonical relation of
  each item and writes the derived fields. A hand edit of a derived field is overwritten.
- **Check** them in the build: a SHACL-SPARQL constraint per rule on the uplifted graph, e.g. "every
  `proc:metadata` of role `generic` on an Implementation Profile has the `href` of its
  `gp:refinesGenericProfile`", with a failing fixture each. `isProfileOf` is not in the item graph
  and can only be checked by a script.

### What it would change

- `gp:refinesProcessConcept` is a new property on the 17 Generic Profiles: an addition to a
  proposal, recorded as a `gp:amendmentAction`. Whether it is substantive or clarifying is for the
  control body: it changes no meaning, but consumers of the RDF see a new triple.
- The derived fields keep their values; only how they are produced changes.
- No identifier changes.

## Not settled here

- The tier-4 relation and how a run is typed (D8, phase 4).
- Whether a Generic Profile may refine several Process Concepts (today `broader` allows it, and the
  Terrain Analysis concept is itself `narrower` than Raster Coverage Processing).
