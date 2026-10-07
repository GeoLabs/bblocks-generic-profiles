Process Implementation Profile -- the shape every Implementation Profile in this register shares.

## What an Implementation Profile is

OGC 14-065 WPS 2.0.2 §7.5.3: *"Implementation profiles cover all descriptive elements of a
process down to the supported data exchange formats. Technically they are process descriptions,
but with the scope of a process profile, i.e., a harmonized and well-defined computing process
that may be implemented by multiple service providers."*

This block is not itself a catalogue: it carries one placeholder example only, clearly marked as
illustrative. The real Implementation Profiles are each their own building block: one per named
operation, each `allOf`-referencing this one and adding its own `const`-pinned
`id`/`prefLabel`/`refinesGenericProfile` --

- 17 vector operations: 15 bound to SQL/MM (Intersects, Contains, Buffer, Centroid, Convex hull,
  Area, Is simple, ...), plus Geometry extent, bound to SAGA GIS (`SAGA.shapes_tools.19`, no
  SQL/MM `ST_Envelope` process exists on this testbed);
- 7 raster/coverage operations bound to GDAL/OTB (Raster reprojection, Raster band math, Raster
  band math (multi-band output), Radiometric index, Raster crop, Raster format conversion,
  Raster extent).

Three of the vector operations (Centroid, Convex hull, Geometry extent) share one Generic
Profile, `unary-geometry-operation` (Geometry -> Geometry); Is simple refines
`unary-spatial-predicate` (Geometry -> Boolean); Area refines `geometry-measure`
(Geometry -> Number). Centroid, Convex hull, Is simple and Area (2026-10-06) are grounded in
[OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1](https://www.ogc.org/standards/sfs/),
the harmonized-with-SQL predecessor to 06-103r4 that the other SQL/MM-bound operations below
already use.

## What Table 21 asks this tier to carry, and how each row is enforced

[OGC 14-065r1 WPS 2.0 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065r1.html#figure_14)
("Inheritance and override rules for process profiles") is the precise contract, not just the
§7.5.3 prose above. D = Declare, I = Inherit (unchanged), O = Override, E = Extend, R = Restrict.
The "how" column is what each real Implementation Profile's own `schema.yaml` checks against its
Generic Profile (generated from it by `scripts/apply_table21_keywords_metadata.py`):

| Row | GP | **IP** | Instance | How, at this tier |
|---|---|---|---|---|
| Process Identifier, Title, Abstract | D | **O** | O | `id`/`prefLabel`/`definition`, `const`-pinned per operation |
| Process Keywords | D | **E** | E | `keywords` must `contain` every Generic Profile keyword |
| Process Metadata | D | **E/O** ᵃ | E/O ᵃ | `metadata` must keep the Generic Profile's Table 22 `concept` reference and add a `generic` one; `source` (citations) stays free |
| Input (the set itself) | | | E ᵇ | every Generic Profile input must be listed (`required`) |
| Input Identifier, Title, Abstract | D | **I** | I | the input's key; Title/Abstract not repeated (unchanged) |
| Input Keywords | D | **E** | E | `keywords` must `contain` the Generic Profile input's |
| Input Metadata | D | **E/O** ᵃ | E/O ᵃ | `metadata` must reference the corresponding Generic Profile input (`generic-input`, below) |
| Input Multiplicity | D | **R** ᶜ | E ᵈ | `maxOccurs` ≤ the Generic Profile's; no `minOccurs` at all |
| Input Data format | -- | **D** | E ᵈ | `schema` |
| Output (the set itself) | | | E ᵇ | every Generic Profile output must be listed (`required`) |
| Output Identifier, Title, Abstract | D | **I** | I | as for inputs |
| Output Keywords | D | **E** | E | `keywords` must `contain` the Generic Profile output's |
| Output Metadata | D | **O** | O | `metadata` references the corresponding Generic Profile output (`generic-output`): a register choice, Table 21 leaves it free |
| Output Data format | -- | **D** | E ᵈ | `schema` |

ᵃ *"The list of metadata references to superior process profiles shall be extended.
Documentation metadata may be overridden."* The references are Table 5 Metadata structures
(`title`, `role`, `href` -- OGC API - Processes' own `ogc.api.processes.v1.schemas.metadata`)
whose `role` is a Table 22 identifier: `http://www.opengis.net/spec/wps/2.0/def/process-profile/`
`concept`, `generic` or `implementation`. ᵇ additional optional inputs or supplementary outputs.
ᶜ maximum only, never the minimum. ᵈ more or larger inputs, additional formats.

Each input/output here has its own IRI, `<Implementation Profile id>/inputs/<name>`
(`/outputs/<name>`), so that an implementation can reference one input rather than the whole
profile. References are made at the level they are about:

- **on the process**, references to whole superior profiles, with the Table 22 roles (`concept`,
  `generic`, `implementation`) -- made once, never repeated on inputs/outputs;
- **on an input/output**, references to the corresponding input/output of each superior profile,
  with roles this register defines, since Table 22 only names profile *levels*:

| Role | Meaning |
|---|---|
| `https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input` | the `href` is the Generic Profile input this input refines |
| `https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output` | the same, for an output |
| `https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input` | the `href` is one input of an Implementation Profile, which the referencing input implements |
| `https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output` | the same, for an output |

They are this register's own identifiers, not OGC ones: nothing is minted under
`http://www.opengis.net/spec/wps/2.0/def/`, where OGC 14-065r1 defines only the three Table 22
roles and `process/description/documentation`.

Footnote a thus becomes a real chain at each level. For an input of `area`: nothing at Generic
Profile (a Process Concept has no inputs), `generic-input` here, and `generic-input` plus
`implementation-input` at the Implementation (instance level) -- see
`ospd.process-profiles.sqlmm.area`'s `processDescription.inherited.json`. On the process: `concept`
at Generic Profile, `concept` + `generic` here, all three at the instance level.

`schema` -- OGC API - Processes Part 1 Core's own property, a full JSON Schema / OpenAPI Schema
Object, able to `$ref` a real shared type's own published schema (e.g.
`ogc.api.processes.v1.schemas.bbox`) -- is Table 21's Data format. Every input/output is listed,
but only those that carry spatial/raster/bbox data have a `schema`; a plain `String`/`Number`/
`Boolean` parameter (an expression, a CRS code, a distance) has no format to declare.

**The declared default is kept deliberately minimal** -- one format per data-carrying role (GML
for vector geometry, GeoTIFF for raster), not an exhaustive list of everything a deployment might
ever support. Table 21's own inheritance rule for this tier is `E` (Extend) at Implementation
(instance level): *"Implementations may allow more or larger input datasets than the
implementation profile, or support additional data exchange formats"* (footnote d) -- a
deployment is free to go beyond this tier's minimal default, so this tier should not try to
pre-empt every format a future deployment might add. Where this minimal default happens to be
grounded in a real deployment's own processDescription (the vector operations' GML, most of the
raster operations' GeoTIFF), that grounding is cited in each Implementation Profile's own
`description.md` -- where it is not (`Gdal_Warp`/`Gdal_Translate`'s DSN-typed inputs expose no
format structurally at all), that is also stated explicitly rather than implied.

`maxOccurs`, when present, Restricts (footnote c: *"Implementation profiles may restrict the
maximum cardinality of a superior generic profile... They shall not modify the minimum
cardinality"*) the Generic Profile's own `maxOccurs` for one input -- a real integer (or
`unbounded`), the same property OGC API - Processes' own `InputDescription` uses, not free text.
E.g. `OTB.BandMath`/`OTB.BandMathX`'s own `il` input caps at `maxOccurs: 1024`, and
`OTB.RadiometricIndices`' own `in` input is a single image, restricting the Generic Profile's
`maxOccurs: unbounded` all the way down to `1`.

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level).
