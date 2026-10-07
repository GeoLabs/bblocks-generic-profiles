# bblocks-generic-profiles

OGC Building Blocks register holding a general-purpose, engine- and format-agnostic vocabulary of
process Concepts, Generic Profiles and Implementation Profiles, independent of any one project.
Identifier prefix: `generic-profiles.`

Built with the [OGC Building Blocks template](https://github.com/opengeospatial/bblocks-template)
tooling (`ghcr.io/opengeospatial/bblocks-postprocess`); see
[the Building Blocks documentation](https://ogcincubator.github.io/bblocks-docs/) for what a
register is and how the pipeline works. This README replaces the template's own, per its
instructions, and adds what is specific to this register below.

## The model: Concept -> Generic Profile -> Implementation Profile -> Implementation

This register follows the four-tier profile hierarchy of
[OGC 14-065, WPS 2.0.2 §7.5](https://docs.ogc.org/is/14-065/14-065.html) (also described, less
formally, by [ZOO-Project's own process-profiles registry](https://zoo-project.github.io/docs/services/process-profiles.html)).
Each tier answers a different question, and each is deliberately kept out of the tiers around it:

| Tier | Question it answers | What it must *not* carry | In this register |
|---|---|---|---|
| **Process Concept** | What is this, in general? | Any input, output, format or implementation (WPS §7.5.1: *"high-level documentation about a general group of processes... not the specific input and output parameters"*) | `generic-profiles.concept.*` |
| **Generic Profile** | What is this operation's abstract signature? | Any data format or size limit (WPS §7.5.2: *"declares a signature for process inputs and outputs"*) | `generic-profiles.generic-profile.*` |
| **Implementation Profile** | What standard formats does it support? | Any one deployment's specific choice (WPS §7.5.3: *"cover all descriptive elements of a process down to the supported data exchange formats... may be implemented by multiple service providers"*) | `generic-profiles.implementation-profile.*` |
| **Implementation (instance level)** | Which real, running process is this? | — this is the concrete thing itself | Not in this register — see below |

The fourth tier, real deployed or deployable processes, is intentionally **not** part of this
register: it lives wherever that implementation itself is profiled. For the worked example below,
that is [`GeoLabs/bblocks-process-profiles`](https://github.com/GeoLabs/bblocks-process-profiles)'s
`ospd.process-profiles.sqlmm.*` (12 real processes of a ZOO-Project testbed deployment), which
link back here through their own `implementsProfile` property (on `ospd.process-profiles.process-type`)
rather than this register cross-referencing them.

A Generic Profile may cover **several** distinct operations when they share the same I/O shape —
WPS's own wording is "a signature for *a* process" (singular), but nothing in a signature alone
distinguishes, say, `Intersects` from `Contains`: both take two geometries and return a boolean.
That distinction is what the Implementation Profile tier is for. Concretely, six Generic
Profiles cover seventeen Implementation Profiles here:

| Generic Profile | Signature | Implementation Profiles |
|---|---|---|
| [`binary-spatial-predicate`](_sources/generic-profile/binary-spatial-predicate/) | Geometry, Geometry -> Boolean | `intersects`, `disjoint`, `contains`, `within`, `touches`, `crosses`, `equals` |
| [`binary-spatial-operation`](_sources/generic-profile/binary-spatial-operation/) | Geometry, Geometry -> Geometry | `intersection`, `union`, `difference`, `symdifference` |
| [`geometry-buffer`](_sources/generic-profile/geometry-buffer/) | Geometry, Number -> Geometry | `buffer` |
| [`unary-geometry-operation`](_sources/generic-profile/unary-geometry-operation/) | Geometry -> Geometry | `geometry-extent` (SAGA GIS `Get Shapes Extents` -- no SQL/MM `ST_Envelope` process exists on this testbed), `centroid` (SQL/MM `ST_Centroid`), `convex-hull` (SQL/MM `ST_ConvexHull`) |
| [`unary-spatial-predicate`](_sources/generic-profile/unary-spatial-predicate/) | Geometry -> Boolean | `is-simple` (SQL/MM `ST_IsSimple`) |
| [`geometry-measure`](_sources/generic-profile/geometry-measure/) | Geometry -> Number | `area` (SQL/MM `ST_Area`) |

All seventeen `broader`/refine back to one Process Concept, **Vector Geometry Processing**.
`centroid`, `convex-hull`, `is-simple` and `area` (2026-10-06) are grounded in
[OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1](https://www.ogc.org/standards/sfs/),
the harmonized-with-SQL predecessor to 06-103r4 that the other SQL/MM-bound operations above
already cite; `geometry-extent` was merged into `unary-geometry-operation` at the same time,
having never had a real reason to be its own Generic Profile once two more operations shared its
exact signature.

A second family covers raster/coverage operations, grounded in the same four-tier pattern. Five of
the six Generic Profiles have their own distinct signature and refine to exactly one
Implementation Profile; `raster-band-math` refines to **two**, the same way the vector predicates
do — same relation (`broader`, `refinesGenericProfile`, `isProfileOf`) throughout:

| Generic Profile | Signature | Implementation Profile(s) |
|---|---|---|
| [`raster-reprojection`](_sources/generic-profile/raster-reprojection/) | Raster, CRS -> Raster | `raster-reprojection` (GDAL `gdalwarp`) |
| [`raster-band-math`](_sources/generic-profile/raster-band-math/) | Raster+, Expression -> Raster | `raster-band-math` (OTB `BandMath`, muParser, fixed to one band), `raster-band-math-multiband` (OTB `BandMathX`, muParserX, may produce several bands) |
| [`radiometric-index`](_sources/generic-profile/radiometric-index/) | Raster+, IndexName+ -> Raster | `radiometric-index` (OTB `RadiometricIndices`) |
| [`raster-crop`](_sources/generic-profile/raster-crop/) | Raster, BoundingBox -> Raster | `raster-crop` (OTB `ExtractROI`) |
| [`raster-format-conversion`](_sources/generic-profile/raster-format-conversion/) | Raster, Format -> Raster | `raster-format-conversion` (GDAL `gdal_translate`) |
| [`raster-extent`](_sources/generic-profile/raster-extent/) | Raster -> Geometry | `raster-extent` (OTB `ImageEnvelope`) |

All six `broader`/refine back to one Process Concept, **Raster Coverage Processing**. Note that
`raster-band-math`'s two Implementation Profiles have the *identical* signature above (band count
is not part of it) — an earlier draft of this register modelled band count as two separate
Generic Profiles using `cardinality: one-or-many` on the output, which was wrong: a multi-band
raster is still one Raster output value, not several. See
[`raster-band-math`](_sources/generic-profile/raster-band-math/)'s own `description.md` ("Why one
Generic Profile, not two") and the "Known limitation" section below.

## Why SQL/MM (and GDAL/OTB) matter here

Each Implementation Profile is grounded in *two* standards, not one, because they answer different
questions (see each one's own `description.md` for the full citation):

- For vector operations: [OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture](https://www.ogc.org/standards/sfa/)
  defines the operation abstractly (a UML method with no binding) — this is what the Concept and
  Generic Profile are grounded in. **ISO/IEC 13249-3:2016 SQL/MM Spatial** binds the *same*
  operation to SQL: a concrete type (`ST_Geometry`) and a concrete function name (`ST_Intersects`,
  `ST_Buffer`, ...). SQL/MM is not a fifth tier and not a Concept — it is, precisely, *an*
  Implementation Profile of Simple Feature Access, for one language and type system, and it is
  exactly why this tier exists at all: a harmonised, well-defined computing process "that may be
  implemented by multiple service providers" (WPS §7.5.3), not yet any one provider's actual
  deployment.
- For raster operations: ISO 19123-1:2023 *Schema for coverage geometry and functions* is the
  abstract analogue of Simple Feature Access, and [OGC 08-068r2 WCPS](https://www.ogc.org/standards/wcps/)
  is the OGC standards-track evidence that coverage processing operations (reprojection, band
  math, cropping) are recognised, harmonised concepts. Unlike SQL/MM, **GDAL and OTB are not
  themselves ISO/OGC standards** — they are the de facto, widely-deployed software bindings the
  Geonovum testbed actually runs (`Gdal_Warp`, `OTB.BandMath`, `OTB.BandMathX`,
  `OTB.RadiometricIndices`, `OTB.ExtractROI`, `Gdal_Translate`). Each raster Implementation
  Profile's `description.md` states this asymmetry explicitly rather than overstating GDAL/OTB's
  standards status to match SQL/MM's.

## OGC API - Processes alignment: why `inputs`/`outputs` look the way they do

[OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32)
("Inheritance and override rules for process profiles") is the precise contract `inputs`/
`outputs` follow at every tier, not just §7.5.3's prose. Rather than inventing a vocabulary from
scratch to express it, both tiers reuse a subset of [OGC API - Processes - Part 1: Core](https://geolabs.github.io/bblocks-ogcapi-processes/)'s
own `InputDescription`/`OutputDescription`/`schema` structure -- the same structure this
project's Implementation (instance level) tier already uses (`ogc.api.processes.v1.schemas.*`),
so all four tiers are now structurally, not just conceptually, consistent:

- **Generic Profile** `inputs`/`outputs` carry `title`, `description`, `keywords`, `metadata`
  and (inputs only) `minOccurs`/`maxOccurs` -- and *nothing else*. Table 21 gives Generic Profile no "Data format"
  row at all (only Implementation Profile does, "D"), so there is no type/format property at
  this tier either, regardless of what WPS §7.5.2's "signature" evokes informally; what WPS calls
  a signature is conveyed here in `title`/`description` prose plus `minOccurs`/`maxOccurs`
  (Table 21: Input.Multiplicity, D), not a machine-checked abstract type.
- **Implementation Profile** `inputs`/`outputs` carry a real `schema` (OGC API - Processes' own
  `schema` property: a full JSON Schema / OpenAPI Schema Object) for Table 21's Data format (D),
  and `maxOccurs` (a real Restrict of the Generic Profile's own value, footnote c: *"Implementation
  profiles may restrict the maximum cardinality of a superior generic profile... They shall not
  modify the minimum cardinality"*) instead of free text. A `schema` may `$ref` a real shared
  type's own published schema directly -- `raster-crop`'s `areaOfInterest` `$ref`s
  [`ogc.api.processes.v1.schemas.bbox`](https://geolabs.github.io/bblocks-ogcapi-processes/)
  (OGC API - Processes - Part 1: Core's own bbox type, itself grounded in
  [OGC 17-069r4](https://docs.ogc.org/is/17-069r4/17-069r4.html) §7.15.3's `bbox` parameter)
  rather than naming a format with a bespoke string. `eoap.cct.*` types (bblocks-eoap-cct) are a
  *different* vocabulary, for CWL inputs/outputs crossing into OGC API - Processes - Part 2:
  Deploy, Replace, Undeploy -- not used here, since `schema` already models an OGC API - Processes
  processDescription directly.
- **Keywords and Metadata** follow the rest of Table 21, also with OGC API - Processes' own
  `descriptionType` properties: `keywords` on the process and on every input/output (Declared by
  the Generic Profile, Extended by the Implementation Profile, whose schema requires it to
  contain every Generic Profile keyword), and `metadata` as WPS Table 5 Metadata structures
  (`title`/`role`/`href`, i.e. `ogc.api.processes.v1.schemas.metadata`). Footnote a ("the list
  of metadata references to superior process profiles shall be extended") is applied at the level
  each reference is about. On the process, references to whole profiles with the
  [Table 22](https://docs.ogc.org/is/14-065/14-065r1.html) roles: a Generic Profile references
  its Process Concept (`.../process-profile/concept`), an Implementation Profile keeps that and
  adds its Generic Profile (`.../process-profile/generic`). On an input/output, only references
  to the corresponding input/output of a superior profile, with this register's roles
  `role/generic-input`/`-output` (and `role/implementation-input`/`-output` at the instance level,
  in `bblocks-process-profiles`). Every Generic Profile input and output is listed on its
  Implementation Profiles, not only those that declare a `schema`.
- **Every input/output description has its own IRI**, `<profile id>/inputs/<name>`
  (`/outputs/<name>`), carried as `id` and pinned by each building block's schema, so that a lower
  tier's metadata `href` -- e.g. a live process's `implementation` reference in
  `bblocks-process-profiles` -- names a node of this register's graph rather than nothing.

The declared default is kept deliberately minimal -- **GML** for every vector geometry role,
**GeoTIFF** for every raster role, not an exhaustive list. Table 21's own rule for this is `E`
(Extend) at Implementation (instance level) (footnote d: *"Implementations may... support
additional data exchange formats"*): a real deployment is free to go beyond this tier's default,
so this tier should not try to guess every format a future deployment might add. Where grounded
in a real processDescription this is stated (the SQL/MM testbed exposes geometries as
`text/xml`=GML only; `OTB.BandMath`/`BandMathX`/`RadiometricIndices`/`ExtractROI` each expose
exactly `image/tiff`, `image/jpeg`, `image/png`, of which GeoTIFF is the one georeferencing-capable
member); where it is not (`Gdal_Warp`/`Gdal_Translate`'s DSN-typed inputs carry no format
structurally at all on this testbed), that is stated too, rather than implied. `OTB.BandMath`/
`BandMathX`'s own `il` input (`maxOccurs: 1024`) and `OTB.RadiometricIndices`' own `in` input (a
single image, not a list) are the real evidence behind `raster-band-math`/
`raster-band-math-multiband`/`radiometric-index`'s `maxOccurs` values. See
[`implementation-profile/description.md`](_sources/implementation-profile/description.md) for the
full Table 21 account, and each Implementation Profile's own `description.md` for its specific
grounding. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for how this design was reached --
checked first on `geometry-extent`/`raster-crop` alone, then rolled out register-wide once
confirmed.

## Building blocks

| Identifier | Tier |
|---|---|
| `generic-profiles.concept` | Concept (shared shape only, illustrative example) |
| `generic-profiles.concept.vector-geometry-processing` | Concept |
| `generic-profiles.generic-profile` | Generic Profile (shared shape only, illustrative example) |
| `generic-profiles.generic-profile.binary-spatial-predicate` | Generic Profile |
| `generic-profiles.generic-profile.binary-spatial-operation` | Generic Profile |
| `generic-profiles.generic-profile.geometry-buffer` | Generic Profile |
| `generic-profiles.generic-profile.unary-geometry-operation` | Generic Profile |
| `generic-profiles.generic-profile.unary-spatial-predicate` | Generic Profile |
| `generic-profiles.generic-profile.geometry-measure` | Generic Profile |
| `generic-profiles.implementation-profile` | Implementation Profile (shared shape only, illustrative example) |
| `generic-profiles.implementation-profile.intersects` | Implementation Profile |
| `generic-profiles.implementation-profile.disjoint` | Implementation Profile |
| `generic-profiles.implementation-profile.contains` | Implementation Profile |
| `generic-profiles.implementation-profile.within` | Implementation Profile |
| `generic-profiles.implementation-profile.touches` | Implementation Profile |
| `generic-profiles.implementation-profile.crosses` | Implementation Profile |
| `generic-profiles.implementation-profile.equals` | Implementation Profile |
| `generic-profiles.implementation-profile.intersection` | Implementation Profile |
| `generic-profiles.implementation-profile.union` | Implementation Profile |
| `generic-profiles.implementation-profile.difference` | Implementation Profile |
| `generic-profiles.implementation-profile.symdifference` | Implementation Profile |
| `generic-profiles.implementation-profile.buffer` | Implementation Profile |
| `generic-profiles.implementation-profile.geometry-extent` | Implementation Profile |
| `generic-profiles.implementation-profile.centroid` | Implementation Profile |
| `generic-profiles.implementation-profile.convex-hull` | Implementation Profile |
| `generic-profiles.implementation-profile.is-simple` | Implementation Profile |
| `generic-profiles.implementation-profile.area` | Implementation Profile |
| `generic-profiles.concept.raster-coverage-processing` | Concept |
| `generic-profiles.generic-profile.raster-reprojection` | Generic Profile |
| `generic-profiles.generic-profile.raster-band-math` | Generic Profile |
| `generic-profiles.generic-profile.radiometric-index` | Generic Profile |
| `generic-profiles.generic-profile.raster-crop` | Generic Profile |
| `generic-profiles.generic-profile.raster-format-conversion` | Generic Profile |
| `generic-profiles.generic-profile.raster-extent` | Generic Profile |
| `generic-profiles.implementation-profile.raster-reprojection` | Implementation Profile |
| `generic-profiles.implementation-profile.raster-band-math` | Implementation Profile |
| `generic-profiles.implementation-profile.raster-band-math-multiband` | Implementation Profile |
| `generic-profiles.implementation-profile.radiometric-index` | Implementation Profile |
| `generic-profiles.implementation-profile.raster-crop` | Implementation Profile |
| `generic-profiles.implementation-profile.raster-format-conversion` | Implementation Profile |
| `generic-profiles.implementation-profile.raster-extent` | Implementation Profile |

The three base blocks (`generic-profiles.concept`, `generic-profiles.generic-profile`,
`generic-profiles.implementation-profile`) are the shape every real entry of that tier shares —
each real entry `allOf`-references its base
and pins its own `id`/`prefLabel` (and, for Implementation Profiles, `refinesGenericProfile`) with
`const`. They are not a catalogue themselves: each carries exactly one clearly-labelled
placeholder example, never a real operation — see [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for
why that distinction matters (an earlier draft of this register got it wrong, using real SQL/MM
operations as "examples" of the shared schema instead of giving each its own building block).

## Known limitation: band count is not formally modelled

`raster-band-math`'s two Implementation Profiles differ in whether the output raster is fixed to
one band or may have several (`OTB.BandMath`/muParser vs. `OTB.BandMathX`/muParserX). The
standards-correct way to express that is a coverage's **RangeType**
([OGC 09-146r8 Coverage Implementation Schema (CIS) 1.1.1](https://docs.ogc.org/is/09-146r8/09-146r8.html)
§6.5: a `SWE Common::DataRecord` with one named field per band, attached to the coverage — also
surfaced operationally by OGC API - Coverages as "field selection"), not an output cardinality —
a multi-band raster is still one Raster value. This register does not yet model a RangeType-like
field list; the distinction is documented in prose only (each Implementation Profile's
`description.md`), not enforced by a schema property. See
[`raster-band-math-multiband`](_sources/implementation-profile/raster-band-math-multiband/)'s
`description.md` ("Open question") for the full account — left for a future revision rather than
added provisionally.

## History: from a custom `BoundingBox` type to reusing OGC API - Processes' own `bbox`

`raster-crop`'s `areaOfInterest` went through two abstract types before landing on today's
design. First `Geometry` (the natural-seeming choice for "a region of interest"), which did not
match its real binding (`OTB.ExtractROI`'s "extent" mode takes four plain numbers, not an encoded
geometry) -- a mismatch an earlier draft left visible rather than papered over. Then a dedicated
`BoundingBox` abstract type (grounded in [OGC 17-069r4](https://docs.ogc.org/is/17-069r4/17-069r4.html)
§7.15.3's `bbox` parameter) plus a `"BBOX"` `dataFormats` string, invented from scratch for this
register. Once the register moved to reusing OGC API - Processes' own `InputDescription`/`schema`
structure (above), both were superseded: `areaOfInterest`'s `schema` now `$ref`s
`ogc.api.processes.v1.schemas.bbox` directly -- OGC API - Processes - Part 1: Core's own,
already-published bbox type, not a custom one. See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
for the full account, including why `eoap.cct.bbox` (bblocks-eoap-cct) was considered and set
aside -- a type for CWL inputs/outputs crossing into OGC API - Processes - Part 2, a different
vocabulary layer from the `schema` property this tier's Implementation Profile actually models.

## Not limited to spatial operations

The worked example here is OGC 06-103r4 / SQL/MM because it is a clean, standardised case with a
small number of Generic Profiles covering many named operations. Any domain with standardised
abstract operations and several independent bindings is a candidate for the same pattern — the
raster/coverage family above is the second such domain in this register.

## Regenerating

```bash
./build.sh     # authoritative: bblocks-postprocess in Docker, results in build-local/tests/report.json
./view.sh      # http://localhost:9090
```

`build.sh` passes `-it` to Docker; drop it when running from a script or CI. On macOS the
container's `--clean` can occasionally race the bind mount and die with a `FileNotFoundError` or
`ENOENT` on a random building block's `context.jsonld` — rerun; it is not a register error, the
same intermittent issue `bblocks-process-profiles` documents.

All content under `_sources/` is hand-written (there is no CWL, no run record, nothing to
generate from) — edit it directly.

## License

Apache-2.0, with one exception: the `assets/*.png`/`*.jpg` illustrations in the 10 vector
Implementation Profiles that have one (`equals`, `intersects`, `disjoint`, `crosses`, `touches`,
`within`, `contains`, `buffer`, `intersection`, `union`) are third-party content, reused from the
[PostGIS Workshop](https://postgis.net/workshops/postgis-intro/) (© Paul Ramsey, Mark Leslie,
PostGIS contributors) under [CC BY-SA 3.0 US](http://creativecommons.org/licenses/by-sa/3.0/us/),
**not** Apache-2.0 -- any reuse of those specific files must keep that attribution and license,
independent of the rest of this register. Each image's own `description.md` ("Illustration"
section) carries the same attribution next to it.
