
# Generic Profile: Raster band math (Schema)

`generic-profiles.generic-profile.raster-band-math` *v0.1*

Derives a new raster from one or more input rasters via a user-supplied mathematical expression evaluated per pixel. One or more Raster inputs, an expression, one Raster output -- the output's band structure (one band or several) is not part of this signature, see its Implementation Profiles.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Generic Profile: **Raster band math**.

> Derives a new raster from one or more input rasters via a user-supplied mathematical expression
> evaluated per pixel. One or more Raster inputs, an expression, one Raster output.

## Source

- ISO 19123-1:2023 *Geographic information -- Schema for coverage geometry and functions -- Part
  1: Fundamentals* -- the abstract coverage domain/range model this signature is grounded in (see
  [its Concept](../../concept/raster-coverage-processing/) for the full citation).
- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic
  Profile is.

## Why one Generic Profile, not two

An earlier draft of this register split this into two Generic Profiles -- one for a
fixed-one-band output (`OTB.BandMath`/muParser), one for a possibly-multi-band output
(`OTB.BandMathX`/muParserX) -- and tried to express the difference with `cardinality: one-or-many`
on the output. That was wrong on two counts: first, a multi-band raster is still exactly **one**
Raster output value, not several -- `cardinality` describes how many separate output values a
process returns, not the internal band structure of one of them (see the base
`generic-profile.schema.yaml`'s own note on this). Second, and more fundamentally, WPS §7.5.2's
"signature for process inputs and outputs" is about which *parameters* exist, at what abstract
type -- both variants have the identical signature: Raster(s), Expression -> Raster. What
distinguishes them (how many bands the result happens to have) is exactly WPS §7.5.3's territory,
"down to the supported data exchange formats" -- Implementation Profile, not Generic Profile. See
[`raster-band-math-multiband`](../../implementation-profile/raster-band-math-multiband/)'s own
`description.md` for where that distinction now lives, and for the still-open question of how to
express it formally.

## Relations

- `broader`: [`generic-profiles.concept.raster-coverage-processing`](../../concept/raster-coverage-processing/)
- Refined by (2 Implementation Profiles):
- [`raster-band-math`](../../implementation-profile/raster-band-math/) -- fixed to one band (`OTB.BandMath`/muParser)
- [`raster-band-math-multiband`](../../implementation-profile/raster-band-math-multiband/) -- may produce several bands (`OTB.BandMathX`/muParserX)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).

## Examples

### Raster band math
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math",
  "type": "GenericProfile",
  "prefLabel": "Raster band math",
  "definition": "Derives a new raster from one or more input rasters via a user-supplied mathematical expression evaluated per pixel. One or more Raster inputs, an expression, one Raster output -- the output's band structure (one band or several) is not part of this signature, see its Implementation Profiles.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile",
  "status": "submitted",
  "broader": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
  ],
  "keywords": [
    "raster",
    "coverage",
    "band math"
  ],
  "metadata": [
    {
      "title": "Process Concept: Raster Coverage Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
    }
  ],
  "inputs": {
    "rasters": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/rasters",
      "title": "Raster",
      "description": "the input raster band(s)/image(s)",
      "keywords": [
        "raster"
      ],
      "minOccurs": 1,
      "maxOccurs": "unbounded"
    },
    "expression": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/expression",
      "title": "String",
      "description": "the per-pixel mathematical expression",
      "keywords": [
        "expression"
      ],
      "minOccurs": 1,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "raster": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/outputs/raster",
      "title": "Raster",
      "description": "the resulting raster",
      "keywords": [
        "raster"
      ]
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/raster-band-math/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math",
  "type": "GenericProfile",
  "prefLabel": "Raster band math",
  "definition": "Derives a new raster from one or more input rasters via a user-supplied mathematical expression evaluated per pixel. One or more Raster inputs, an expression, one Raster output -- the output's band structure (one band or several) is not part of this signature, see its Implementation Profiles.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile",
  "status": "submitted",
  "broader": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
  ],
  "keywords": [
    "raster",
    "coverage",
    "band math"
  ],
  "metadata": [
    {
      "title": "Process Concept: Raster Coverage Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
    }
  ],
  "inputs": {
    "rasters": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/rasters",
      "title": "Raster",
      "description": "the input raster band(s)/image(s)",
      "keywords": [
        "raster"
      ],
      "minOccurs": 1,
      "maxOccurs": "unbounded"
    },
    "expression": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/expression",
      "title": "String",
      "description": "the per-pixel mathematical expression",
      "keywords": [
        "expression"
      ],
      "minOccurs": 1,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "raster": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/outputs/raster",
      "title": "Raster",
      "description": "the resulting raster",
      "keywords": [
        "raster"
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

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> ;
    skos:definition "Derives a new raster from one or more input rasters via a user-supplied mathematical expression evaluated per pixel. One or more Raster inputs, an expression, one Raster output -- the output's band structure (one band or several) is not part of this signature, see its Implementation Profiles." ;
    skos:inScheme gp:generic-profile ;
    skos:prefLabel "Raster band math" ;
    gp:inputs [ ns2:expression <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/expression> ;
            ns2:rasters <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/rasters> ] ;
    gp:outputs [ ns1:raster <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/outputs/raster> ] ;
    gp:status "submitted" ;
    proc:keywords "band math",
        "coverage",
        "raster" ;
    proc:metadata [ dcterms:title "Process Concept: Raster Coverage Processing" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/expression> dcterms:description "the per-pixel mathematical expression" ;
    dcterms:title "String" ;
    proc:keywords "expression" ;
    proc:maxOccurs 1 ;
    proc:minOccurs 1 .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/rasters> dcterms:description "the input raster band(s)/image(s)" ;
    dcterms:title "Raster" ;
    proc:keywords "raster" ;
    proc:maxOccurs "unbounded" ;
    proc:minOccurs 1 .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/outputs/raster> dcterms:description "the resulting raster" ;
    dcterms:title "Raster" ;
    proc:keywords "raster" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Generic Profile "Raster band math" -- see generic-profiles.generic-profile
  for the general shape every Generic Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math
      x-jsonld-id: '@id'
    type:
      const: GenericProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Raster band math
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
- type: object
  properties:
    metadata:
      allOf:
      - contains:
          type: object
          required:
          - role
          - href
          properties:
            role:
              const: http://www.opengis.net/spec/wps/2.0/def/process-profile/concept
            href:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing
      x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
    inputs:
      properties:
        rasters:
          required:
          - id
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/rasters
              x-jsonld-id: '@id'
        expression:
          required:
          - id
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/expression
              x-jsonld-id: '@id'
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/inputs/
    outputs:
      properties:
        raster:
          required:
          - id
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/outputs/raster
              x-jsonld-id: '@id'
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/outputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/outputs/
x-jsonld-extra-terms:
  GenericProfile: http://www.w3.org/2004/02/skos/core#Concept
  definition: http://www.w3.org/2004/02/skos/core#definition
  inScheme:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#inScheme
    x-jsonld-type: '@id'
  status: https://geolabs.github.io/bblocks-generic-profiles/def/status
  broader:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#broader
    x-jsonld-type: '@id'
  keywords: https://w3id.org/ogc/api/processes/keywords
  source: http://purl.org/dc/terms/source
  title: http://purl.org/dc/terms/title
  link:
    x-jsonld-id: http://purl.org/dc/terms/references
    x-jsonld-type: '@id'
  clause: https://geolabs.github.io/bblocks-generic-profiles/def/clause
x-jsonld-prefixes:
  skos: http://www.w3.org/2004/02/skos/core#
  gp: https://geolabs.github.io/bblocks-generic-profiles/def/
  proc: https://w3id.org/ogc/api/processes/
  dct: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/raster-band-math/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/raster-band-math/schema.yaml)


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
    "metadata": {
      "@context": {
        "href": {
          "@id": "proc:href",
          "@type": "@id"
        },
        "role": {
          "@id": "proc:role",
          "@type": "@id"
        }
      },
      "@id": "proc:metadata"
    },
    "source": "dct:source",
    "inputs": {
      "@context": {
        "@vocab": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/inputs/",
        "description": "dct:description",
        "minOccurs": "proc:minOccurs",
        "maxOccurs": "proc:maxOccurs"
      },
      "@id": "gp:inputs"
    },
    "outputs": {
      "@context": {
        "@vocab": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/outputs/",
        "description": "dct:description"
      },
      "@id": "gp:outputs"
    },
    "title": "dct:title",
    "link": {
      "@id": "dct:references",
      "@type": "@id"
    },
    "clause": "gp:clause",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "gp": "https://geolabs.github.io/bblocks-generic-profiles/def/",
    "proc": "https://w3id.org/ogc/api/processes/",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/raster-band-math/context.jsonld)

## Sources

* [ZOO-Project process-profiles: Concept / Generic Profile / Implementation Profile](https://zoo-project.github.io/docs/services/process-profiles.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/generic-profile/raster-band-math`

