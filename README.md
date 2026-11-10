# bblocks-generic-profiles

OGC Building Blocks register holding a general-purpose, provider-independent vocabulary of process
Concepts, Generic Profiles and Implementation Profiles, independent of any one project. Formats
appear at the Implementation Profile tier only.
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
| [`raster-resampling`](_sources/generic-profile/raster-resampling/) | Raster, GridResolution -> Raster | `raster-resampling` (added 2026-11-10) |
| [`raster-thresholding`](_sources/generic-profile/raster-thresholding/) | Raster (single band) -> BinaryMask | `otsu-thresholding` (added 2026-11-10) |
| [`raster-rendering`](_sources/generic-profile/raster-rendering/) | Raster, ColourMap -> RenderedImage | `raster-rendering` (added 2026-11-10) |

All nine `broader`/refine back to one Process Concept, **Raster Coverage Processing**, whose
definition was extended on 2026-11-10 (an amendment classified substantive) to resampling,
thresholding and rendering. `radiometric-index` also refines to a second Implementation Profile,
`radiometric-index-single-band` (separate single-band rasters in, one single-band raster per index
out, the index optional; added 2026-11-10); both point to the same activity type. Note that
`raster-band-math`'s two Implementation Profiles have the *identical* signature above (band count
is not part of it) — an earlier draft of this register modelled band count as two separate
Generic Profiles using `cardinality: one-or-many` on the output, which was wrong: a multi-band
raster is still one Raster output value, not several. See
[`raster-band-math`](_sources/generic-profile/raster-band-math/)'s own `description.md` ("Why one
Generic Profile, not two") and the "Known limitation" section below.

Two more families come from SAGA GIS 7.3.0 tools exposed by the Geonovum testbed, with data the
register did not have before: **elevation models** and **point clouds** (2026-10-08).

| Generic Profile | Signature (data types) | Implementation Profile(s) |
|---|---|---|
| [`terrain-derivative`](_sources/generic-profile/terrain-derivative/) | elevation-model -> raster-single-band | `slope` (SAGA `ta_morphometry 0`), `terrain-ruggedness-index` (`ta_morphometry 16`), `topographic-position-index` (`ta_morphometry 18`) |
| [`analytical-hillshading`](_sources/generic-profile/analytical-hillshading/) | elevation-model, number (azimuth), number (altitude) -> raster-single-band | `analytical-hillshading` (`ta_lighting 0`) |
| [`point-cloud-rasterization`](_sources/generic-profile/point-cloud-rasterization/) | point-cloud, number (cell size) -> raster | `point-cloud-to-grid` (`pointcloud_tools 4`, output narrowed to raster-single-band) |
| [`point-cloud-thinning`](_sources/generic-profile/point-cloud-thinning/) | point-cloud, number (percentage) -> point-cloud | `point-cloud-thinning` (`pointcloud_tools 9`) |
| [`point-cloud-to-features`](_sources/generic-profile/point-cloud-to-features/) | point-cloud -> feature-collection | `point-cloud-to-shapes` (`pointcloud_tools 5`) |

The terrain ones `broader` to a new Concept, **Terrain Analysis**, itself listed as `narrower`
than Raster Coverage Processing -- an elevation model is a single-band raster; the point cloud ones
to **Point Cloud Processing**. Point clouds are declared as LAS
([OGC 17-030r1](https://www.ogc.org/standards/las/), media type `application/vnd.las`).

A fourth Process Concept, **Data Discovery and Access** (2026-11-10), groups operations that find
or deliver data rather than compute from it, for the OSPD processes that search a catalogue or
download a band:

| Generic Profile | Signature (data types) | Implementation Profile(s) |
|---|---|---|
| [`product-selection`](_sources/generic-profile/product-selection/) | geometry, time-interval, collection-identifier -> eo-product | `product-selection` (area as GeoJSON, products as STAC Items) |
| [`band-retrieval`](_sources/generic-profile/band-retrieval/) | eo-product, band-identifier, bounding-box (optional) -> raster | `band-retrieval` (product as STAC Item, raster as GeoTIFF) |

No Implementation Profile binds band retrieval to SAFE packages and JPEG 2000 bands: the SAFE format
has no media type, and the rule that every format has one is kept (decision C8 of 2026-11-10).

## Data types

Every Generic and Implementation Profile input/output carries a `dataType`, a concept of the
[data types register](https://geolabs.github.io/bblocks-data-types/) (`data-types.vocabulary`): raster, single- or
multi-band, elevation model, geometry and its point/curve/surface kinds, feature collection, point
cloud, TIN, table, bounding box, number, string, boolean. It is the kind of data, not its encoding
(an Implementation Profile's `representation`), so it is not the "Data format" Table 21 denies the Generic
Profile. An Implementation Profile may narrow it along `broader`, and its schema pins the result --
e.g. `centroid` takes a `surface` and returns a `point` (OGC 99-049 §2.1.9.1: Area and Centroid are
Surface methods), `raster-band-math` returns a `raster-single-band`.

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

## Where the meaning of an operation lives: activity types

Since 2026-11-09 (decisions D3 and D4), the meaning of each operation is not carried by its
Implementation Profile but by a separate item of this register, an activity type
(`generic-profiles.activity-type.*`, `acttype:ActivityType` of the
[Activity Type Register](https://ogcincubator.github.io/activity-type-register/)), one per operation.
The Implementation Profile points to it with `activityType`. The activity type holds the definition,
the standards that define the operation -- [OGC 06-103r4 Simple Feature Access](https://www.ogc.org/standards/sfa/)
or [OGC 99-049](https://www.ogc.org/standards/sfs/) for vector operations, with the
ISO/IEC 13249-3 SQL/MM name (`ST_Intersects`, ...) as `altLabel`;
[OGC 08-068r2 WCPS](https://www.ogc.org/standards/wcps/) for raster operations; the literature of
the terrain indices -- and the illustrations. An Implementation Profile cannot be its own activity
type: `rim:RegisterItemShape` allows one item class per item
([`docs/implementation-profile-vs-activity-type.md`](docs/implementation-profile-vs-activity-type.md)).

An Implementation Profile item carries no tool, host or testbed keyword or source (decision D4);
the descriptions above and in each profile's `description.md` still name the tools their defaults
were grounded in. The processes that implement a profile, and the tools behind them, are profiled in
[`bblocks-process-profiles`](https://github.com/GeoLabs/bblocks-process-profiles), which links each
of them to its Implementation Profile with `implementsProfile`.

## OGC API - Processes alignment: why `inputs`/`outputs` look the way they do

[OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32)
("Inheritance and override rules for process profiles") is the precise contract `inputs`/
`outputs` follow at every tier, not just §7.5.3's prose. Rather than inventing a vocabulary from
scratch to express it, both tiers reuse a subset of [OGC API - Processes - Part 1: Core](https://geolabs.github.io/bblocks-ogcapi-processes/)'s
own `InputDescription`/`OutputDescription`/`schema` structure (since 2026-11-09, `schema` only at
the Implementation (instance level); tier 3 names a `representation`) -- the same structure this
project's Implementation (instance level) tier already uses (`ogc.api.processes.v1.schemas.*`),
so all four tiers are now structurally, not just conceptually, consistent:

- **Generic Profile** `inputs`/`outputs` carry `dataType`, `title`, `description`, `keywords`,
  `metadata` and (inputs only) `minOccurs`/`maxOccurs` -- and *nothing else*. Table 21 gives Generic
  Profile no "Data format" row at all (only Implementation Profile does, "D"), so a format stays
  forbidden at this tier, regardless of what WPS §7.5.2's "signature" evokes informally. `dataType`
  is not a format: it is a concept, the kind of data a role takes (see "Data types" above). What
  WPS calls a signature is conveyed here by the named roles, their `dataType` and
  `minOccurs`/`maxOccurs` (Table 21: Input.Multiplicity, D), which the build checks, with
  `title`/`description` explaining them in prose.
- **Implementation Profile** `inputs`/`outputs` name Table 21's Data format (D) by reference:
  `representation`, one or more IRIs of representations of
  [`bblocks-data-formats`](https://github.com/GeoLabs/bblocks-data-formats) (decision D6). A
  representation realizes a version of the role's data type and points to a format; the JSON
  Schema stays at the Implementation (instance level), as served. `raster-crop`'s `areaOfInterest`,
  which `$ref`ed [`ogc.api.processes.v1.schemas.bbox`](https://geolabs.github.io/bblocks-ogcapi-processes/)
  until 2026-11-09, now points to the representation `bounding-box-ogcapi-processes-bbox`, whose
  format carries that `$ref`. `maxOccurs` is a real Restrict of the Generic Profile's own value
  (footnote c: *"Implementation profiles may restrict the maximum cardinality of a superior generic
  profile... They shall not modify the minimum cardinality"*), not free text. `eoap.cct.*` types
  (bblocks-eoap-cct) are a *different* vocabulary, for CWL inputs/outputs crossing into OGC API -
  Processes - Part 2: Deploy, Replace, Undeploy -- not used here.
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
  Implementation Profiles, not only those that declare a `representation`.
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
`BandMathX`'s own `il` input (a list) and `OTB.RadiometricIndices`' own `in` input (a single image, not a list) are the real
evidence behind `raster-band-math`/`raster-band-math-multiband`'s `maxOccurs: unbounded` and
`radiometric-index`'s `maxOccurs: 1`. A cardinality is written only where there is one: an input
without `minOccurs`/`maxOccurs` has the OGC API - Processes default, exactly one. See
[`implementation-profile/description.md`](_sources/implementation-profile/description.md) for the
full Table 21 account, and each Implementation Profile's own `description.md` for its specific
grounding.

## Building blocks

| Identifier | Tier |
|---|---|
| `generic-profiles.register` | The register itself as an ISO 19135:2026 `rim:Register`, with its three item classes |
| `generic-profiles.concept` | Concept (shared shape only, illustrative example) |
| `generic-profiles.concept.vector-geometry-processing` | Concept |
| `generic-profiles.generic-profile` | Generic Profile (shared shape only, illustrative example) |
| `generic-profiles.generic-profile.binary-spatial-predicate` | Generic Profile |
| `generic-profiles.generic-profile.binary-spatial-operation` | Generic Profile |
| `generic-profiles.generic-profile.geometry-buffer` | Generic Profile |
| `generic-profiles.generic-profile.unary-geometry-operation` | Generic Profile |
| `generic-profiles.generic-profile.unary-spatial-predicate` | Generic Profile |
| `generic-profiles.generic-profile.geometry-measure` | Generic Profile |
| `generic-profiles.activity-type` | Activity type: the meaning of one operation (shared shape, shapes and tests) |
| `generic-profiles.activity-type.<operation>` | Activity type, one per operation (36); 37 Implementation Profiles point to them, two to `radiometric-index` |
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
| `generic-profiles.generic-profile.raster-resampling` | Generic Profile |
| `generic-profiles.generic-profile.raster-thresholding` | Generic Profile |
| `generic-profiles.generic-profile.raster-rendering` | Generic Profile |
| `generic-profiles.implementation-profile.radiometric-index-single-band` | Implementation Profile |
| `generic-profiles.implementation-profile.raster-resampling` | Implementation Profile |
| `generic-profiles.implementation-profile.otsu-thresholding` | Implementation Profile |
| `generic-profiles.implementation-profile.raster-rendering` | Implementation Profile |
| `generic-profiles.concept.terrain-analysis` | Concept |
| `generic-profiles.concept.point-cloud-processing` | Concept |
| `generic-profiles.generic-profile.terrain-derivative` | Generic Profile |
| `generic-profiles.generic-profile.analytical-hillshading` | Generic Profile |
| `generic-profiles.generic-profile.point-cloud-rasterization` | Generic Profile |
| `generic-profiles.generic-profile.point-cloud-thinning` | Generic Profile |
| `generic-profiles.generic-profile.point-cloud-to-features` | Generic Profile |
| `generic-profiles.implementation-profile.slope` | Implementation Profile |
| `generic-profiles.implementation-profile.terrain-ruggedness-index` | Implementation Profile |
| `generic-profiles.implementation-profile.topographic-position-index` | Implementation Profile |
| `generic-profiles.implementation-profile.analytical-hillshading` | Implementation Profile |
| `generic-profiles.implementation-profile.point-cloud-to-grid` | Implementation Profile |
| `generic-profiles.implementation-profile.point-cloud-thinning` | Implementation Profile |
| `generic-profiles.implementation-profile.point-cloud-to-shapes` | Implementation Profile |
| `generic-profiles.concept.data-discovery-and-access` | Concept |
| `generic-profiles.generic-profile.product-selection` | Generic Profile |
| `generic-profiles.generic-profile.band-retrieval` | Generic Profile |
| `generic-profiles.implementation-profile.product-selection` | Implementation Profile |
| `generic-profiles.implementation-profile.band-retrieval` | Implementation Profile |

The three base blocks (`generic-profiles.concept`, `generic-profiles.generic-profile`,
`generic-profiles.implementation-profile`) are the shape every real entry of that tier shares —
each real entry `allOf`-references its base
and pins its own `id`/`prefLabel` (and, for Implementation Profiles, `refinesGenericProfile`) with
`const`. They are not a catalogue themselves: each carries exactly one clearly-labelled
placeholder example, never a real operation.

## This register as an ISO 19135:2026 register

The register also describes itself with the
[Registered Item Model](https://ogcincubator.github.io/registered-item-model/) (ISO 19135:2026,
*Registration and register governance*), through one extra block,
[`generic-profiles.register`](_sources/register/) -- a profile of
`ogc.rim.schemas.register-item-class`, built like that register's own `activity-type`
profile. It adds no content to the three tiers; it names them in the model's terms:

- one `rim:Register` (`.../def/register`) and three `rim:RegisterItemClass`es
  (`.../def/item-class/process-concept`, `generic-profile`, `implementation-profile`);
- three `owl:Class`es, `gp:ProcessConcept` / `gp:GenericProfile` / `gp:ImplementationProfile`,
  each `rdfs:subClassOf rim:RegisterItem` **and** `skos:Concept` -- what the JSON `type` of each
  tier (`ProcessConcept`, `GenericProfile`, `ImplementationProfile`) maps to; the Concept tier's
  `type` was renamed from `Concept`, which the model's own context already binds to `rim:Concept`;
- `gp:refinesGenericProfile rdfs:subPropertyOf rim:relatedItem`;
- on every entry, the ISO 19135:2026 required core: `objectIdentifier` (its own `id`),
  `itemClass`, `inRegister`, `validityStatus`, `publicationStatus`, and one `hasAction` recording
  the entry's *addition* (below). Each tier's base schema is an `allOf` of
  `bblocks://ogc.rim.schemas.register-item` plus the tier's own properties: the
  model's schema requires and types the core, the model's JSON-LD context maps it onto `rim:*`
  (`"valid"` -> `rim:valid`), and this register's contexts declare no `rim:` term of their own --
  only `itemClass` and `inRegister` are pinned per tier.

`gp:specification`, the register's `rim:RegisterSpecification`, states its scope, roles, identifier
and version rules, eligibility and definition of a substantive change. GeoLabs SARL is the control
body for now, and intends to delegate that role to the OGC or to an OSPD working group.

### How each entry enters the register

There is no `status` field. ISO 19135:2026 drops the 2015 edition's single lifecycle list
(`submitted`/`valid`/`invalid`/`superseded`/`retired`) in favour of two independent concerns plus
actions, so every entry instead records:

- one `hasAction` of type `addition` (`rim:additionAction`), whose `proposer` is GeoLabs
  (`.../def/geolabs`, the register's owner and manager), `startedAtTime` the building block's own
  `dateTimeAddition`, and `appliesTo` the entry -- a proposed addition, not yet decided;
- `validityStatus: invalid` + `publicationStatus: published` -- visible here, not in force, since
  no control-body decision has been recorded. A later decision is a further `rim:RegisterAction`
  (publish, invalidation, supersession) added beside the first, never an edit of it.

`gp:AdditionProposalShape` enforces this: `_sources/register/tests/item-without-addition-fail.ttl`
(no action) and `addition-without-proposer-fail.ttl` (addition without a proposer) are both
rejected (both an unqualified and a qualified count are needed, because pyshacl 0.21.0 does not
raise `sh:qualifiedMinCount` on a path with no values). `invalid` as the reading of "proposed,
awaiting a decision", and whether a proposal should be modelled further, are open questions for
the model's authors.

What the build checks, per entry (`build-local/tests/report.json`, 57/57): `generic-profiles.register`'s
own shapes (item class and register pinned per tier, tier-to-tier link present, the addition
recorded) **and** the model's base `rim:RegisterItemShape`, which applies to our items through the
ontology closure.

Two things are deliberately not claimed, and one is open -- see the block's
[`description.md`](_sources/register/description.md):

- it is a *content register* (no concept plane: each item carries its own `prefLabel`/
  `definition`), as `gp:specification` records, to be reviewed if a concept plane of operations is
  created later;
- the `allOf` needs the model's JSON binding -- a `register-item` schema that does not pin `type`
  to `"rim:RegisterItem"`, and a context that maps the `rim:*` terms. Both were contributed by
  GeoLabs and are now part of the published model
  ([ogcincubator/registered-item-model](https://github.com/ogcincubator/registered-item-model),
  imported here by URL), so `./build.sh` needs no local mapping.

## Band count: modelled by data type, not by field list

`raster-band-math`'s two Implementation Profiles differ in whether the output raster is fixed to
one band or may have several (`OTB.BandMath`/muParser vs. `OTB.BandMathX`/muParserX). Since
2026-10-08 that is stated, and checked, with the [data types register](https://geolabs.github.io/bblocks-data-types/):
`raster-band-math`'s output is `raster-single-band`, a narrower type than the Generic Profile's
`raster`, while `raster-band-math-multiband`'s stays `raster` (BandMathX may output one band or
several). An elevation model is likewise `elevation-model`, a narrower `raster-single-band`.

What is still not modelled is the band *structure*: which bands, what they mean -- a coverage's
**RangeType** ([OGC 09-146r8 Coverage Implementation Schema (CIS) 1.1.1](https://docs.ogc.org/is/09-146r8/09-146r8.html)
§6.5: a `SWE Common::DataRecord` with one named field per band). The data type says "one band" or
"several", not "red, green, near-infrared". See
[`raster-band-math-multiband`](_sources/implementation-profile/raster-band-math-multiband/)'s
`description.md` ("Open question").

## History: from a custom `BoundingBox` type to reusing OGC API - Processes' own `bbox`

`raster-crop`'s `areaOfInterest` went through two abstract types before landing on today's
design. First `Geometry` (the natural-seeming choice for "a region of interest"), which did not
match its real binding (`OTB.ExtractROI`'s "extent" mode takes four plain numbers, not an encoded
geometry) -- a mismatch an earlier draft left visible rather than papered over. Then a dedicated
`BoundingBox` abstract type (grounded in [OGC 17-069r4](https://docs.ogc.org/is/17-069r4/17-069r4.html)
§7.15.3's `bbox` parameter) plus a `"BBOX"` `dataFormats` string, invented from scratch for this
register. Once the register moved to reusing OGC API - Processes' own `InputDescription`/`schema`
structure (above), both were superseded: `areaOfInterest`'s `schema` `$ref`ed
`ogc.api.processes.v1.schemas.bbox` directly -- OGC API - Processes - Part 1: Core's own,
already-published bbox type, not a custom one. Since 2026-11-09 (decision D6) the role points to
the representation `bounding-box-ogcapi-processes-bbox` of `bblocks-data-formats`, whose format
carries that `$ref`. `eoap.cct.bbox` (bblocks-eoap-cct) was considered
and set aside: it is a type for CWL inputs/outputs crossing into OGC API - Processes - Part 2, a
different vocabulary layer from the `representation` this tier's Implementation Profile now
carries (until 2026-11-09, the `schema` property it modelled).

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

Until `bblocks-data-types` and `bblocks-data-formats` are published, the build needs local
url-mappings: see [`docs/LOCAL-BUILD.md`](docs/LOCAL-BUILD.md) and
`bblocks-config-local.yml.example` (including the temporary mapping of the Registered Item Model).

All content under `_sources/` is hand-written (there is no CWL, no run record, nothing to
generate from) — edit it directly — except the activity type items `_sources/activity-type/<operation>/`
and the item class constant of `_sources/activity-type/schema.yaml`, generated by
`scripts/activity_types.py` from `scripts/activity-types.yaml`.

## License

Apache-2.0, with one exception: the `assets/*.png`/`*.jpg` illustrations in the 10 vector
Implementation Profiles that have one (`equals`, `intersects`, `disjoint`, `crosses`, `touches`,
`within`, `contains`, `buffer`, `intersection`, `union`) are third-party content, reused from the
[PostGIS Workshop](https://postgis.net/workshops/postgis-intro/) (© Paul Ramsey, Mark Leslie,
PostGIS contributors) under [CC BY-SA 3.0 US](http://creativecommons.org/licenses/by-sa/3.0/us/),
**not** Apache-2.0 -- any reuse of those specific files must keep that attribution and license,
independent of the rest of this register. Each image's own `description.md` ("Illustration"
section) carries the same attribution next to it.
