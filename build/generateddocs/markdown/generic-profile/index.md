
# Generic Process Profile (Schema)

`generic-profiles.generic-profile` *v0.1*

The shape every Generic Profile shares: the abstract interface of one process, declaring a signature for its inputs and outputs (OGC 14-065 WPS 2.0.2 §7.5.2), linked to its Process Concept by `broader`. Each real Generic Profile (generic-profiles.generic-profile.*) is its own building block that allOf-references this one -- this block is not itself a catalogue, only the common shape plus one illustrative example.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Generic Process Profile -- the shape every Generic Profile in this register shares.

## What a Generic Profile is

OGC 14-065 WPS 2.0.2 §7.5.2: *"a generic profile is the abstract interface of a process. It
provides a detailed description of the process mechanics and declares a signature for process
inputs and outputs... similar to a process description... but does not provide a definition of
specific data formats."*

This block is not itself a catalogue: it carries one placeholder example only (`example1`, clearly
marked as illustrative, not a real signature). The real Generic Profiles are each their own
building block, `allOf`-referencing this one and adding their own `const`-pinned `id`/`prefLabel`:

Vector geometry (broader: [`vector-geometry-processing`](../concept/vector-geometry-processing/)):

- [`binary-spatial-predicate`](binary-spatial-predicate/) -- two Geometry in, one Boolean out
  (Intersects, Disjoint, Contains, Within, Touches, Crosses, Equals)
- [`binary-spatial-operation`](binary-spatial-operation/) -- two Geometry in, one Geometry out
  (Intersection, Union, Difference, Symmetric difference)
- [`geometry-buffer`](geometry-buffer/) -- one Geometry and one Number in, one Geometry out
  (Buffer)
- [`unary-geometry-operation`](unary-geometry-operation/) -- one Geometry in, one Geometry out
  (refined by 3 Implementation Profiles: Geometry extent/bounding envelope, Centroid, Convex
  hull)
- [`unary-spatial-predicate`](unary-spatial-predicate/) -- one Geometry in, one Boolean out
  (Is simple)
- [`geometry-measure`](geometry-measure/) -- one Geometry in, one Number out (Area)

Raster/coverage (broader: [`raster-coverage-processing`](../concept/raster-coverage-processing/)):

- [`raster-reprojection`](raster-reprojection/) -- one Raster and a target CRS in, one Raster out
- [`raster-band-math`](raster-band-math/) -- one-or-many Raster and an expression in, one Raster out
  (refined by 2 Implementation Profiles: fixed-one-band and possibly-multi-band -- see below)
- [`radiometric-index`](radiometric-index/) -- one-or-many Raster and index name(s) in, one Raster out
- [`raster-crop`](raster-crop/) -- one Raster and a bounding box in, one Raster out
- [`raster-format-conversion`](raster-format-conversion/) -- one Raster and a target format in, one Raster out
- [`raster-extent`](raster-extent/) -- one Raster in, one Geometry out (bounding envelope)

A Generic Profile declares a signature "for *a* process" (WPS's own wording, singular) -- but
several distinct operations sharing the identical shape are still modelled as **one** Generic
Profile when nothing in the signature itself distinguishes them: the seven vector predicates, and
also `raster-band-math`'s two Implementation Profiles (`OTB.BandMath`, fixed to one band, vs.
`OTB.BandMathX`, which may produce several). An earlier draft of this register modelled that
raster distinction as two Generic Profiles, using `cardinality: one-or-many` on the output to
tell them apart -- that was wrong: a multi-band raster is still **one** Raster output value, not
several (band count is a coverage's internal RangeType structure, OGC 09-146r8 CIS 1.1.1 §6.5,
not an output cardinality), and both variants have the identical Raster(s)+Expression->Raster
signature regardless. See [`raster-band-math`](raster-band-math/)'s own `description.md` ("Why
one Generic Profile, not two") and its multi-band Implementation Profile's "Open question"
section for the full account, including what a correct fix would need (a RangeType-like field
list, not yet modelled here).

`raster-crop`'s `areaOfInterest` and `raster-extent`/`unary-geometry-operation`'s
[`geometry-extent`](../implementation-profile/geometry-extent/) Implementation Profile's outputs
look similar ("a bounding box") but bind to genuinely different real parameters:
`OTB.ExtractROI`'s "extent" mode takes four plain numbers, while
`OTB.ImageEnvelope`/`SAGA.shapes_tools.19` both return an actual vector polygon. Neither
distinction is carried at this tier any more (this tier has no type/format property at all, see
the base schema's own note); it lives entirely at Implementation Profile, in each one's `schema`
-- `areaOfInterest`'s `$ref`s `ogc.api.processes.v1.schemas.bbox`, the extent operations' outputs
declare GML -- see [`raster-crop`](raster-crop/)'s "`areaOfInterest` has no type at this tier"
and [`raster-extent`](raster-extent/)'s "Why the output is a Geometry, not a BoundingBox".

`unary-geometry-operation` is also where `geometry-extent` landed once it stopped being its own
Generic Profile: it shares the identical Geometry->Geometry signature with `centroid` and
`convex-hull` (OGC 99-049 Rev 1.1 §2.1.1.1 Envelope, §2.1.9.1 Centroid, §2.1.1.3 ConvexHull), the
same "one Generic Profile per signature, several Implementation Profiles per operation"
principle used everywhere else in this register -- there was never a reason for it to be
dedicated, that was simply how it was first added (2026-10-01) before the SFA operations below it
arrived (2026-10-06).

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).

## Examples

### Example Generic Profile (illustrative shape only, not a real signature)
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/example-generic-profile",
  "type": "GenericProfile",
  "prefLabel": "Example Generic Profile (placeholder, not a real signature)",
  "definition": "Illustrates the shape of a Generic Profile entry only. Real Generic Profiles are each their own building block -- see generic-profiles.generic-profile.binary-spatial-predicate, .geometry-buffer and the other siblings for actual signatures.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile",
  "status": "submitted",
  "broader": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"
  ],
  "keywords": ["example"],
  "inputs": {
    "input1": {
      "title": "Geometry",
      "description": "an input role",
      "keywords": ["geometry"],
      "metadata": [
        {
          "title": "Process Concept: Vector Geometry Processing",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"
        }
      ],
      "minOccurs": 1,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "result": {"title": "Boolean", "description": "an output role", "keywords": ["boolean"]}
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/example-generic-profile",
  "type": "GenericProfile",
  "prefLabel": "Example Generic Profile (placeholder, not a real signature)",
  "definition": "Illustrates the shape of a Generic Profile entry only. Real Generic Profiles are each their own building block -- see generic-profiles.generic-profile.binary-spatial-predicate, .geometry-buffer and the other siblings for actual signatures.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile",
  "status": "submitted",
  "broader": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"
  ],
  "keywords": [
    "example"
  ],
  "inputs": {
    "input1": {
      "title": "Geometry",
      "description": "an input role",
      "keywords": [
        "geometry"
      ],
      "metadata": [
        {
          "title": "Process Concept: Vector Geometry Processing",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"
        }
      ],
      "minOccurs": 1,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "result": {
      "title": "Boolean",
      "description": "an output role",
      "keywords": [
        "boolean"
      ]
    }
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix gp: <https://geolabs.github.io/bblocks-generic-profiles/def/> .
@prefix ns1: <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/outputs/> .
@prefix ns2: <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/inputs/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/example-generic-profile> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing> ;
    skos:definition "Illustrates the shape of a Generic Profile entry only. Real Generic Profiles are each their own building block -- see generic-profiles.generic-profile.binary-spatial-predicate, .geometry-buffer and the other siblings for actual signatures." ;
    skos:inScheme gp:generic-profile ;
    skos:prefLabel "Example Generic Profile (placeholder, not a real signature)" ;
    gp:inputs [ ns2:input1 [ dcterms:description "an input role" ;
                    dcterms:title "Geometry" ;
                    proc:keywords "geometry" ;
                    proc:maxOccurs 1 ;
                    proc:metadata [ dcterms:title "Process Concept: Vector Geometry Processing" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] ;
                    proc:minOccurs 1 ] ] ;
    gp:outputs [ ns1:result [ dcterms:description "an output role" ;
                    dcterms:title "Boolean" ;
                    proc:keywords "boolean" ] ] ;
    gp:status "submitted" ;
    proc:keywords "example" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: "Generic Process Profile (OGC 14-065 WPS 2.0.2 \xA77.5.2): \"the abstract
  interface of a process... declares a signature for process inputs and outputs.\"
  One Generic Profile per signature: several operations sharing the identical I/O
  shape (the seven binary spatial predicates, for instance) share one Generic Profile
  and differ only at Implementation Profile; `broader` links it to the Process Concept
  (generic-profiles.concept.*) documenting the general group it belongs to.\nImplementation
  Profiles and Implementations (instance level) -- concrete, deployable processes
  binding a Generic Profile to real formats -- are not part of this register; they
  live wherever the implementation itself is profiled (e.g. `ospd.process-profiles.sqlmm.*`)
  and link back here via their own `implementsProfile` property. This register does
  not cross-reference them.\n`inputs`/`outputs` use a subset of OGC API - Processes
  - Part 1: Core's own `InputDescription`/`OutputDescription` structure (`title`,
  `description`, `keywords`, `minOccurs`/`maxOccurs`) rather than a custom vocabulary
  invented for this register: this project already imports and uses that structure
  at Implementation (instance level) (`ogc.api.processes.v1.schemas.*`), so reusing
  it here makes all four tiers structurally, not just conceptually, consistent. There
  is deliberately no type/format property at this tier: [OGC 14-065 WPS 2.0.2 \xA77.5.4
  Table 21](https://docs.ogc.org/is/14-065/14-065.html#32) gives Generic Profile no
  \"Data format\" row at all (only Implementation Profile does, \"D\") -- what WPS
  \xA77.5.2 calls a \"signature\" is the existence, naming and multiplicity of inputs/outputs,
  conveyed here in `title`/`description` prose, not a machine-checked abstract type.\nThis
  tier is where Table 21 Declares (D) every property it lists for the Process, its
  Inputs and its Outputs -- including `keywords` (Process, Input, Output) and `metadata`
  (Input, Output), both taken from OGC API - Processes' own `descriptionType` (whose
  `metadata` item, `ogc.api.processes.v1.schemas.metadata`, is WPS Table 5's Metadata
  structure: `title`, `role`, `href`). Every input's `metadata` must reference this
  Generic Profile's superior, its Process Concept, with the Table 22 role `http://www.opengis.net/spec/wps/2.0/def/process-profile/concept`:
  that is the list Table 21 footnote a requires the Implementation Profile to extend."
type: object
required:
- id
- type
- prefLabel
- definition
- inScheme
- status
- broader
- keywords
- inputs
- outputs
properties:
  id:
    type: string
    format: uri
    x-jsonld-id: '@id'
  type:
    const: GenericProfile
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
  broader:
    description: The Process Concept(s) (generic-profiles.concept.*) documenting the
      general group this operation belongs to.
    type: array
    minItems: 1
    items:
      type: string
      format: uri
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#broader
    x-jsonld-type: '@id'
  keywords:
    description: Table 21 Process.Keywords (D). Each Implementation Profile must keep
      all of them (E).
    type: array
    minItems: 1
    items:
      type: string
    x-jsonld-id: https://w3id.org/ogc/api/processes/keywords
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
        clause:
          type: string
          x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/clause
    x-jsonld-id: http://purl.org/dc/terms/source
  inputs:
    description: 'Keyed by role name. A subset of OGC API - Processes Part 1 Core''s
      own InputDescription: `title`/`description` carry the "signature" informally,
      `minOccurs`/`maxOccurs` are the one machine-checkable property this tier actually
      has (Table 21: Input.Multiplicity, D).'
    type: object
    minProperties: 1
    additionalProperties:
      type: object
      required:
      - title
      - keywords
      - metadata
      properties:
        title:
          type: string
          x-jsonld-id: http://purl.org/dc/terms/title
        description:
          type: string
          x-jsonld-id: http://purl.org/dc/terms/description
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
                const: http://www.opengis.net/spec/wps/2.0/def/process-profile/concept
                x-jsonld-id: https://w3id.org/ogc/api/processes/role
                x-jsonld-type: '@id'
          x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
          x-jsonld-extra-terms:
            title: http://purl.org/dc/terms/title
            href:
              x-jsonld-id: https://w3id.org/ogc/api/processes/href
              x-jsonld-type: '@id'
        minOccurs:
          type: integer
          default: 1
          x-jsonld-id: https://w3id.org/ogc/api/processes/minOccurs
        maxOccurs:
          default: 1
          oneOf:
          - type: integer
          - const: unbounded
          x-jsonld-id: https://w3id.org/ogc/api/processes/maxOccurs
    x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/inputs
    x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/inputs/
  outputs:
    description: Keyed by role name. No `minOccurs`/`maxOccurs` -- Table 21 has no
      Output.Multiplicity row (and, per the same reasoning as the earlier `cardinality`-on-outputs
      mistake this replaces, an output's internal structure, e.g. a raster's band
      count, is not an output cardinality either way; see generic-profiles.implementation-profile.raster-band-math-multiband's
      `description.md`).
    type: object
    minProperties: 1
    additionalProperties:
      type: object
      required:
      - title
      - keywords
      properties:
        title:
          type: string
          x-jsonld-id: http://purl.org/dc/terms/title
        description:
          type: string
          x-jsonld-id: http://purl.org/dc/terms/description
        keywords:
          type: array
          minItems: 1
          items:
            type: string
          x-jsonld-id: https://w3id.org/ogc/api/processes/keywords
        metadata:
          description: 'Table 21 Output.Metadata is D here then plain O below (no
            footnote a): unlike an input''s, an output''s metadata carries no obligation
            to be kept by lower tiers.'
          type: array
          items:
            $ref: https://geolabs.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/v1/schemas/metadata/schema.yaml
          x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
          x-jsonld-extra-terms:
            title: http://purl.org/dc/terms/title
            role:
              x-jsonld-id: https://w3id.org/ogc/api/processes/role
              x-jsonld-type: '@id'
            href:
              x-jsonld-id: https://w3id.org/ogc/api/processes/href
              x-jsonld-type: '@id'
    x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/outputs
    x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/outputs/
x-jsonld-extra-terms:
  GenericProfile: http://www.w3.org/2004/02/skos/core#Concept
x-jsonld-prefixes:
  skos: http://www.w3.org/2004/02/skos/core#
  gp: https://geolabs.github.io/bblocks-generic-profiles/def/
  proc: https://w3id.org/ogc/api/processes/
  dct: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "GenericProfile": "skos:Concept",
    "id": "@id",
    "type": "@type",
    "prefLabel": "skos:prefLabel",
    "definition": "skos:definition",
    "inScheme": {
      "@id": "skos:inScheme",
      "@type": "@id"
    },
    "status": "gp:status",
    "broader": {
      "@id": "skos:broader",
      "@type": "@id"
    },
    "keywords": "proc:keywords",
    "source": {
      "@context": {
        "title": "dct:title",
        "link": {
          "@id": "dct:references",
          "@type": "@id"
        },
        "clause": "gp:clause"
      },
      "@id": "dct:source"
    },
    "inputs": {
      "@context": {
        "@vocab": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/inputs/",
        "title": "dct:title",
        "description": "dct:description",
        "metadata": {
          "@context": {
            "role": {
              "@id": "proc:role",
              "@type": "@id"
            },
            "href": {
              "@id": "proc:href",
              "@type": "@id"
            }
          },
          "@id": "proc:metadata"
        },
        "minOccurs": "proc:minOccurs",
        "maxOccurs": "proc:maxOccurs"
      },
      "@id": "gp:inputs"
    },
    "outputs": {
      "@context": {
        "@vocab": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/outputs/",
        "title": "dct:title",
        "description": "dct:description",
        "metadata": {
          "@context": {
            "role": {
              "@id": "proc:role",
              "@type": "@id"
            },
            "href": {
              "@id": "proc:href",
              "@type": "@id"
            }
          },
          "@id": "proc:metadata"
        }
      },
      "@id": "gp:outputs"
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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/context.jsonld)

## Sources

* [OGC 14-065 WPS 2.0.2 Interface Standard Corrigendum 2, §7.5.2 Generic Process Profile](https://docs.ogc.org/is/14-065/14-065.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/generic-profile`

