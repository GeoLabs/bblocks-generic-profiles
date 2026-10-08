
# Process Implementation Profile (Schema)

`generic-profiles.implementation-profile` *v0.1*

The shape every Implementation Profile shares: a specific named operation refining one Generic Profile, adding the standard data exchange formats it is commonly expressed in (OGC 14-065 WPS 2.0.2 §7.5.3). Each real Implementation Profile (generic-profiles.implementation-profile.*) is its own building block that allOf-references this one.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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

## Examples

### Example Implementation Profile (illustrative shape only, not a real operation)
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile",
  "type": "ImplementationProfile",
  "prefLabel": "Example Implementation Profile (placeholder, not a real operation)",
  "definition": "Illustrates the shape of an Implementation Profile entry only. Real ones are each their own building block -- see generic-profiles.implementation-profile.intersects, .buffer and the other siblings.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate",
  "keywords": [
    "vector",
    "geometry",
    "spatial relation",
    "predicate",
    "example"
  ],
  "metadata": [
    {
      "title": "Process Concept: Vector Geometry Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"
    },
    {
      "title": "Generic Profile: Binary spatial predicate",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate"
    }
  ],
  "inputs": {
    "geometry1": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/inputs/geometry1",
      "schema": {
        "type": "string",
        "contentMediaType": "text/xml",
        "description": "GML"
      },
      "keywords": [
        "geometry",
        "GML"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Binary spatial predicate -- input `geometry1`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/inputs/geometry1"
        }
      ]
    },
    "geometry2": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/inputs/geometry2",
      "schema": {
        "type": "string",
        "contentMediaType": "text/xml",
        "description": "GML"
      },
      "keywords": [
        "geometry",
        "GML"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Binary spatial predicate -- input `geometry2`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/inputs/geometry2"
        }
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/outputs/result",
      "keywords": [
        "boolean"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Binary spatial predicate -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/outputs/result"
        }
      ]
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile",
  "type": "ImplementationProfile",
  "prefLabel": "Example Implementation Profile (placeholder, not a real operation)",
  "definition": "Illustrates the shape of an Implementation Profile entry only. Real ones are each their own building block -- see generic-profiles.implementation-profile.intersects, .buffer and the other siblings.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate",
  "keywords": [
    "vector",
    "geometry",
    "spatial relation",
    "predicate",
    "example"
  ],
  "metadata": [
    {
      "title": "Process Concept: Vector Geometry Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"
    },
    {
      "title": "Generic Profile: Binary spatial predicate",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate"
    }
  ],
  "inputs": {
    "geometry1": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/inputs/geometry1",
      "schema": {
        "type": "string",
        "contentMediaType": "text/xml",
        "description": "GML"
      },
      "keywords": [
        "geometry",
        "GML"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Binary spatial predicate -- input `geometry1`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/inputs/geometry1"
        }
      ]
    },
    "geometry2": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/inputs/geometry2",
      "schema": {
        "type": "string",
        "contentMediaType": "text/xml",
        "description": "GML"
      },
      "keywords": [
        "geometry",
        "GML"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Binary spatial predicate -- input `geometry2`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/inputs/geometry2"
        }
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/outputs/result",
      "keywords": [
        "boolean"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Binary spatial predicate -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/outputs/result"
        }
      ]
    }
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix gp: <https://geolabs.github.io/bblocks-generic-profiles/def/> .
@prefix ns1: <https://w3id.org/ogc/api/schema/> .
@prefix ns2: <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/> .
@prefix ns3: <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile> a skos:Concept ;
    skos:definition "Illustrates the shape of an Implementation Profile entry only. Real ones are each their own building block -- see generic-profiles.implementation-profile.intersects, .buffer and the other siblings." ;
    skos:inScheme gp:implementation-profile ;
    skos:prefLabel "Example Implementation Profile (placeholder, not a real operation)" ;
    gp:inputs [ ns3:geometry1 <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/inputs/geometry1> ;
            ns3:geometry2 <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/inputs/geometry2> ] ;
    gp:outputs [ ns2:result <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/outputs/result> ] ;
    gp:refinesGenericProfile <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate> ;
    gp:status "submitted" ;
    proc:keywords "example",
        "geometry",
        "predicate",
        "spatial relation",
        "vector" ;
    proc:metadata [ dcterms:title "Process Concept: Vector Geometry Processing" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ],
        [ dcterms:title "Generic Profile: Binary spatial predicate" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/inputs/geometry1> proc:keywords "GML",
        "geometry" ;
    proc:metadata [ dcterms:title "Generic Profile: Binary spatial predicate -- input `geometry1`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/inputs/geometry1> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] ;
    proc:schema [ a ns1:string ;
            ns1:contentMediaType "text/xml" ;
            ns1:description "GML" ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/inputs/geometry2> proc:keywords "GML",
        "geometry" ;
    proc:metadata [ dcterms:title "Generic Profile: Binary spatial predicate -- input `geometry2`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/inputs/geometry2> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] ;
    proc:schema [ a ns1:string ;
            ns1:contentMediaType "text/xml" ;
            ns1:description "GML" ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/outputs/result> proc:keywords "boolean" ;
    proc:metadata [ dcterms:title "Generic Profile: Binary spatial predicate -- output `result`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/outputs/result> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output> ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: "Process Implementation Profile (OGC 14-065 WPS 2.0.2 \xA77.5.3): \"Implementation
  profiles cover all descriptive elements of a process down to the supported data
  exchange formats.\" One per specific named operation (Intersects, Buffer, ...),
  `refinesGenericProfile` to exactly one Generic Profile (the shared abstract I/O
  shape).\n`inputs`/`outputs` use OGC API - Processes - Part 1: Core's own `schema`
  property (a full JSON Schema / OpenAPI Schema Object) for Table 21's Data format
  (D), instead of a custom format vocabulary: this project already imports and uses
  the same `schema` property at Implementation (instance level), so a real deployment's
  processDescription and this tier's declared default are now directly comparable
  JSON, not a bespoke string next to real JSON. `maxOccurs`, when present, Restricts
  (R, footnote c: \"Implementation profiles may restrict the maximum cardinality of
  a superior generic profile... They shall not modify the minimum cardinality\") the
  Generic Profile's own value -- a real integer (or `unbounded`), not free text. Only
  inputs/outputs that carry spatial/raster/bbox data need a `schema` entry; a plain
  parameter (an expression, a CRS code, a distance) has none to declare.\nKeep the
  declared `schema` minimal and deliberately not exhaustive (one format is often enough:
  GML for vector geometry data, GeoTIFF for raster, OGC API - Processes' own `bbox`
  schema for a bounding box). Per Table 21, Implementation (instance level) may *Extend*
  this (footnote d: \"Implementations may... support additional data exchange formats\")
  -- a specific deployment is free to support more than this tier's minimal default,
  so this tier should not try to pre-empt every format a future deployment might add.
  See each Implementation Profile's own `description.md` for whether its default is
  grounded in a real deployment's processDescription or left as the vocabulary's own
  minimal baseline.\nA `schema` may `$ref` a real shared type's own published schema
  directly -- e.g. `ogc.api.processes.v1.schemas.bbox` for a bounding box, the same
  OGC API - Processes - Part 1: Core type this register's Implementation (instance
  level) processDescriptions already use. `eoap.cct.*` types (bblocks-eoap-cct) are
  a *different* vocabulary, for typing CWL inputs/outputs passed to OGC API - Processes
  - Part 2: Deploy, Replace, Undeploy, not for describing an OGC API - Processes processDescription's
  own `schema` -- not used here.\nThe rest of Table 21 at this tier, as each real
  Implementation Profile's own `schema.yaml` enforces it against its Generic Profile:
  - Process: `keywords` Extend (E) -- must contain every Generic Profile keyword;\n
  \ `id`/`prefLabel`/`definition` Override (O); `metadata` Extends (E, footnote a:
  \"the list of\n  metadata references to superior process profiles shall be extended\")
  the Generic Profile's\n  list -- its Table 22 `concept` reference -- with a `generic`
  one to the Generic Profile\n  itself. Profile-level references are made here only,
  never repeated on inputs/outputs.\n- Input: every Generic Profile input is listed.
  Its `metadata` references the corresponding\n  Generic Profile input (`<Generic
  Profile id>/inputs/<name>`) with this register's role\n  `https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input`
  -- footnote a, at the level of the input; `keywords` Extend (E);\n  Identifier/Title/Abstract
  Inherit (I), so not repeated; `maxOccurs` Restrict (R); `schema`\n  Declare (D).\n-
  Output: every Generic Profile output is listed too; `metadata` references the corresponding\n
  \ Generic Profile output with the role `https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output`
  (Table 21 allows any value here,\n  O; the register keeps outputs symmetric with
  inputs); `keywords` Extend (E); `schema`\n  Declare (D)."
type: object
required:
- id
- type
- prefLabel
- definition
- inScheme
- status
- refinesGenericProfile
- keywords
- metadata
- inputs
- outputs
properties:
  id:
    type: string
    format: uri
    x-jsonld-id: '@id'
  type:
    const: ImplementationProfile
    x-jsonld-id: '@type'
  prefLabel:
    type: string
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
  definition:
    type: string
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#definition
  inScheme:
    type: string
    format: uri
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#inScheme
    x-jsonld-type: '@id'
  status:
    type: string
    enum:
    - submitted
    - valid
    - invalid
    - superseded
    - retired
    x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/status
  refinesGenericProfile:
    description: The single Generic Profile (generic-profiles.generic-profile.*) this
      Implementation Profile refines.
    type: string
    format: uri
    x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/refinesGenericProfile
    x-jsonld-type: '@id'
  keywords:
    description: Table 21 Process.Keywords (E) -- the Generic Profile's keywords plus
      this operation's own.
    type: array
    minItems: 1
    items:
      type: string
    x-jsonld-id: https://w3id.org/ogc/api/processes/keywords
  metadata:
    description: 'Table 21 Process.Metadata (E, footnote a): the Generic Profile''s
      references (Table 22 `concept`) plus a Table 22 `generic` reference to the Generic
      Profile.'
    type: array
    items:
      $ref: https://geolabs.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/v1/schemas/metadata/schema.yaml
    allOf:
    - contains:
        type: object
        required:
        - role
        - href
        properties:
          role:
            const: http://www.opengis.net/spec/wps/2.0/def/process-profile/concept
    - contains:
        type: object
        required:
        - role
        - href
        properties:
          role:
            const: http://www.opengis.net/spec/wps/2.0/def/process-profile/generic
    x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
    x-jsonld-extra-terms:
      title: http://purl.org/dc/terms/title
      role:
        x-jsonld-id: https://w3id.org/ogc/api/processes/role
        x-jsonld-type: '@id'
      href:
        x-jsonld-id: https://w3id.org/ogc/api/processes/href
        x-jsonld-type: '@id'
  inputs:
    description: Keyed by the same input names as the Generic Profile's own `inputs`
      (Identifier/Title/ Abstract Inherited, not repeated). `schema` is Table 21's
      Data format (D); `maxOccurs`, when present, Restricts (R, footnote c) the Generic
      Profile's own value; `keywords` Extend (E) the Generic Profile's; `metadata`
      Extends (E, footnote a) its superior-profile references.
    type: object
    additionalProperties:
      type: object
      required:
      - id
      - keywords
      - metadata
      properties:
        id:
          description: This input's own IRI, `<profile id>/inputs/<name>` -- what
            a lower tier's metadata `href` points at.
          type: string
          format: uri
          x-jsonld-id: '@id'
        schema:
          x-jsonld-id: https://w3id.org/ogc/api/processes/schema
          x-jsonld-vocab: https://w3id.org/ogc/api/schema/
        maxOccurs:
          oneOf:
          - type: integer
          - const: unbounded
          x-jsonld-id: https://w3id.org/ogc/api/processes/maxOccurs
        keywords:
          type: array
          minItems: 1
          items:
            type: string
          x-jsonld-id: https://w3id.org/ogc/api/processes/keywords
        metadata:
          type: array
          items:
            $ref: https://geolabs.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/v1/schemas/metadata/schema.yaml
          contains:
            type: object
            required:
            - role
            - href
            properties:
              role:
                const: https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input
                x-jsonld-id: https://w3id.org/ogc/api/processes/role
                x-jsonld-type: '@id'
          x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
          x-jsonld-extra-terms:
            title: http://purl.org/dc/terms/title
            href:
              x-jsonld-id: https://w3id.org/ogc/api/processes/href
              x-jsonld-type: '@id'
    x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/inputs
    x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/
  outputs:
    description: Keyed by the same output names as the Generic Profile's own `outputs`.
    type: object
    additionalProperties:
      type: object
      required:
      - id
      - keywords
      - metadata
      properties:
        id:
          description: This output's own IRI, `<profile id>/outputs/<name>` -- what
            a lower tier's metadata `href` points at.
          type: string
          format: uri
          x-jsonld-id: '@id'
        schema:
          x-jsonld-id: https://w3id.org/ogc/api/processes/schema
          x-jsonld-vocab: https://w3id.org/ogc/api/schema/
        keywords:
          type: array
          minItems: 1
          items:
            type: string
          x-jsonld-id: https://w3id.org/ogc/api/processes/keywords
        metadata:
          type: array
          items:
            $ref: https://geolabs.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/v1/schemas/metadata/schema.yaml
          contains:
            type: object
            required:
            - role
            - href
            properties:
              role:
                const: https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output
                x-jsonld-id: https://w3id.org/ogc/api/processes/role
                x-jsonld-type: '@id'
          x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
          x-jsonld-extra-terms:
            title: http://purl.org/dc/terms/title
            href:
              x-jsonld-id: https://w3id.org/ogc/api/processes/href
              x-jsonld-type: '@id'
    x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/outputs
    x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/
  source:
    type: array
    items:
      type: object
      required:
      - title
      properties:
        title:
          type: string
          x-jsonld-id: http://purl.org/dc/terms/title
        link:
          type: string
          format: uri
          x-jsonld-id: http://purl.org/dc/terms/references
          x-jsonld-type: '@id'
    x-jsonld-id: http://purl.org/dc/terms/source
x-jsonld-extra-terms:
  ImplementationProfile: http://www.w3.org/2004/02/skos/core#Concept
x-jsonld-prefixes:
  skos: http://www.w3.org/2004/02/skos/core#
  gp: https://geolabs.github.io/bblocks-generic-profiles/def/
  proc: https://w3id.org/ogc/api/processes/
  dct: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "ImplementationProfile": "skos:Concept",
    "id": "@id",
    "type": "@type",
    "prefLabel": "skos:prefLabel",
    "definition": "skos:definition",
    "inScheme": {
      "@id": "skos:inScheme",
      "@type": "@id"
    },
    "status": "gp:status",
    "refinesGenericProfile": {
      "@id": "gp:refinesGenericProfile",
      "@type": "@id"
    },
    "keywords": "proc:keywords",
    "metadata": {
      "@context": {
        "href": {
          "@id": "proc:href",
          "@type": "@id"
        },
        "role": {
          "@id": "proc:role",
          "@type": "@id"
        },
        "title": "dct:title"
      },
      "@id": "proc:metadata"
    },
    "inputs": {
      "@context": {
        "@vocab": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/",
        "schema": {
          "@context": {
            "@vocab": "https://w3id.org/ogc/api/schema/"
          },
          "@id": "proc:schema"
        },
        "maxOccurs": "proc:maxOccurs"
      },
      "@id": "gp:inputs"
    },
    "outputs": {
      "@context": {
        "@vocab": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/",
        "schema": {
          "@context": {
            "@vocab": "https://w3id.org/ogc/api/schema/"
          },
          "@id": "proc:schema"
        }
      },
      "@id": "gp:outputs"
    },
    "source": {
      "@context": {
        "title": "dct:title",
        "link": {
          "@id": "dct:references",
          "@type": "@id"
        }
      },
      "@id": "dct:source"
    },
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "gp": "https://geolabs.github.io/bblocks-generic-profiles/def/",
    "proc": "https://w3id.org/ogc/api/processes/",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/context.jsonld)

## Sources

* [OGC 14-065 WPS 2.0.2 Interface Standard Corrigendum 2, §7.5.3 Process Implementation Profile](https://docs.ogc.org/is/14-065/14-065.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/implementation-profile`

