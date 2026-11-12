# Should `data-type` move to a separate `bblocks-data-types` register?

Status: **decided and applied -- Option A** (2026-11-04). The local `generic-profiles.data-type` block
is removed; `dataType` values are now the concept IRIs of the
[`bblocks-data-types`](https://geolabs.github.io/bblocks-data-types/) register
(`https://geolabs.github.io/bblocks-data-types/def/data-type/...`), imported in `bblocks-config.yaml`.
The analysis below is kept as the record of the decision (2026-10-26) and describes the situation
*before* the move.

## What `data-type` is today

- One building block, [`generic-profiles.data-type`](../_sources/data-type/), a SKOS
  `ConceptScheme` with **16 concepts**: `raster`, `raster-single-band`, `raster-multi-band`,
  `elevation-model`, `geometry`, `point`, `curve`, `surface`, `feature-collection`, `point-cloud`,
  `tin`, `table`, `bounding-box`, `number`, `string`, `boolean` (with `skos:broader` between them,
  e.g. `raster-single-band` → `raster`).
- `register: generic-profiles`, no `dependsOn`, nothing upstream.
- Its concepts' IRIs are under the register's own base URL:
  `https://geolabs.github.io/bblocks-generic-profiles/def/data-type/…`.

## How it is coupled to the rest of the register

The coupling is **nominal, not structural**, and that is the single most important fact for this
decision:

- The profile tiers point at a data type through the `dataType` **value** (an IRI, mapped to
  `dct:type` with `@type: @id`) — never through a `$ref bblocks://` and never via `dependsOn`.
- Because `dataType` is a *value* and not a schema position, it **cannot** become a `$ref`. The
  coupling stays "by IRI string" wherever the vocabulary physically lives.
- Measured across `_sources/`: **291 hard-coded `data-type` IRIs in 101 files** — 134 in
  `schema.yaml` files, 157 in example JSON. (Contexts carry none literally; they map the `dataType`
  term, not the individual type IRIs.)

## The crux: IRI stability, not file location

Moving the *files* is trivial. The real question is what happens to those 291 IRIs.

- **Option A — move the block and change the IRIs** to the new register's base URL
  (`…/bblocks-data-types/def/data-type/X`). This is a **breaking rename**: all 291 occurrences in
  101 files must be rewritten, and any consumer that already stored an old IRI breaks. One-off,
  doable, but must be coordinated.
- **Option B — move the block and keep the IRIs stable**, by publishing the terms under a
  **register-independent namespace** (e.g. `w3id.org/ogc/…`, or a dedicated `def/` host) so that
  the term's identity is decoupled from the register that happens to document and govern it. The
  physical move then changes no IRI and breaks nothing.

Option B is the clean, future-proof path, and it is exactly the Registered Item Model distinction
we already applied elsewhere: *the register* (its governance and location) is separate from *the
IRIs of its items*, and a `rim:objectIdentifier` never redirects. **Decide the permanent namespace
first; the move is cheap and non-breaking only once that is settled.** If the IRIs must stay under
`generic-profiles` for now, defer the whole move.

## Mechanics after a split

- `bblocks-generic-profiles` adds `imports: [ …/bblocks-data-types ]`. A `dependsOn` could be added
  for documentation / dependency-graph purposes, but **no `$ref`** is possible (see above).
- Build order: `bblocks-data-types` must build and publish first; `generic-profiles` imports its
  `register.json`. Until `bblocks-data-types` is published, building `generic-profiles` needs the
  **same local URL-mapping workaround** already used for the Registered Item Model
  (`bblocks-config-local.yml` + `.volumes`) — one more moving part in CI.
- An import makes the type IRIs resolvable and would, for the first time, let SHACL check that each
  `dataType` points at a real `DataType` — something nothing validates today.

## Alignment with the Registered Item Model work

`data-type` is already a `skos:ConceptScheme` with `skos:broader`, so it maps naturally onto the
RIM **concept plane** (`rim:ConceptSystem` + `rim:Concept`), or onto a content register of
`DataType` items. A `bblocks-data-types` register would therefore be a second, clean RIM example —
the concept-plane counterpart to `generic-profiles`'s content-plane register — if the team wants to
showcase the pattern on both sides.

## Costs vs benefits

| Benefits | Costs / risks |
|---|---|
| Reusable beyond generic-profiles (eoap-cct, process-profiles, any WPS-style profile) | 291 IRIs to rewrite unless the namespace is frozen (Option B) |
| Independent governance / versioning — the whole point of a register | One more repository to build, publish (Pages), maintain |
| Smaller, more focused generic-profiles | Build coupling (import + local mapping), more fragile CI |
| A natural RIM "concept plane" example | Over-fragmentation if nothing else ever uses it |

## Recommendation

Worth doing **iff** the vocabulary is meant to be shared beyond `generic-profiles` — which its
content and abstract suggest. The decisive prerequisite is **choosing a permanent, register-independent
IRI namespace before moving anything** (Option B). With that settled, the move is mechanical and
non-breaking; without it, defer.

## If/when the decision is "go" — migration checklist (not done here)

1. Fix the permanent IRI namespace for the 16 types (ideally register-independent).
2. In `bblocks-data-types`: replace the template placeholders with the `data-type` block (schema,
   context, `examples`), set `identifier-prefix` and `baseURL`, build and publish.
3. In `bblocks-generic-profiles`: add the import; if Option A was chosen, rewrite the 291 IRIs in
   the 101 files; remove the local `data-type` block.
4. Rebuild `generic-profiles` against the published (or locally mapped) `bblocks-data-types` and
   confirm the test report is unchanged.
5. Update both registers' READMEs.
