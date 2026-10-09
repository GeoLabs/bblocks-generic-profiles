
# Generic Profile: Raster format conversion (Schema)

`generic-profiles.generic-profile.raster-format-conversion` *v0.1*

Converts a raster coverage from one encoding to another, without changing its content. One Raster input, a target format, one Raster output in the new encoding.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Generic Profile: **Raster format conversion**.

> Converts a raster coverage from one encoding to another, without changing its content. One Raster input, a target format, one Raster output in the new encoding.

## Source

- ISO 19123-1:2023 *Geographic information -- Schema for coverage geometry and functions -- Part
  1: Fundamentals* -- the abstract coverage domain/range model this signature is grounded in (see
  [its Concept](../../concept/raster-coverage-processing/) for the full citation).
- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic
  Profile is.

## Relations

- `broader`: [`generic-profiles.concept.raster-coverage-processing`](../../concept/raster-coverage-processing/)
- Refined by (1 Implementation Profile):
- [`raster-format-conversion`](../../implementation-profile/raster-format-conversion/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).

## Examples

### Raster format conversion
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion",
  "type": "GenericProfile",
  "prefLabel": "Raster format conversion",
  "definition": "Converts a raster coverage from one encoding to another, without changing its content. One Raster input, a target format, one Raster output in the new encoding.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile",
  "status": "submitted",
  "broader": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
  ],
  "keywords": [
    "raster",
    "coverage",
    "format conversion"
  ],
  "metadata": [
    {
      "title": "Process Concept: Raster Coverage Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
    }
  ],
  "inputs": {
    "raster": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/inputs/raster",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster",
      "title": "Raster",
      "description": "the input raster coverage",
      "keywords": [
        "raster"
      ]
    },
    "targetFormat": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/inputs/targetFormat",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/string",
      "title": "String",
      "description": "the target raster encoding",
      "keywords": [
        "format"
      ]
    }
  },
  "outputs": {
    "raster": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/outputs/raster",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster",
      "title": "Raster",
      "description": "the converted raster coverage",
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
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/raster-format-conversion/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion",
  "type": "GenericProfile",
  "prefLabel": "Raster format conversion",
  "definition": "Converts a raster coverage from one encoding to another, without changing its content. One Raster input, a target format, one Raster output in the new encoding.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile",
  "status": "submitted",
  "broader": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
  ],
  "keywords": [
    "raster",
    "coverage",
    "format conversion"
  ],
  "metadata": [
    {
      "title": "Process Concept: Raster Coverage Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
    }
  ],
  "inputs": {
    "raster": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/inputs/raster",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster",
      "title": "Raster",
      "description": "the input raster coverage",
      "keywords": [
        "raster"
      ]
    },
    "targetFormat": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/inputs/targetFormat",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/string",
      "title": "String",
      "description": "the target raster encoding",
      "keywords": [
        "format"
      ]
    }
  },
  "outputs": {
    "raster": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/outputs/raster",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster",
      "title": "Raster",
      "description": "the converted raster coverage",
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
@prefix ns1: <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/inputs/> .
@prefix ns2: <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/outputs/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> ;
    skos:definition "Converts a raster coverage from one encoding to another, without changing its content. One Raster input, a target format, one Raster output in the new encoding." ;
    skos:inScheme gp:generic-profile ;
    skos:prefLabel "Raster format conversion" ;
    gp:inputs [ ns1:raster <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/inputs/raster> ;
            ns1:targetFormat <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/inputs/targetFormat> ] ;
    gp:outputs [ ns2:raster <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/outputs/raster> ] ;
    gp:status "submitted" ;
    proc:keywords "coverage",
        "format conversion",
        "raster" ;
    proc:metadata [ dcterms:title "Process Concept: Raster Coverage Processing" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/inputs/raster> dcterms:description "the input raster coverage" ;
    dcterms:title "Raster" ;
    dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster> ;
    proc:keywords "raster" .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/inputs/targetFormat> dcterms:description "the target raster encoding" ;
    dcterms:title "String" ;
    dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/string> ;
    proc:keywords "format" .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/outputs/raster> dcterms:description "the converted raster coverage" ;
    dcterms:title "Raster" ;
    dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster> ;
    proc:keywords "raster" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Generic Profile "Raster format conversion" -- see generic-profiles.generic-profile
  for the general shape every Generic Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion
      x-jsonld-id: '@id'
    type:
      const: GenericProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Raster format conversion
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
        raster:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/inputs/raster
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
        targetFormat:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/inputs/targetFormat
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type/string
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/inputs/
    outputs:
      properties:
        raster:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-format-conversion/outputs/raster
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
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

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/raster-format-conversion/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/raster-format-conversion/schema.yaml)


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
        "dataType": {
          "@id": "dct:type",
          "@type": "@id"
        },
        "description": "dct:description",
        "minOccurs": "proc:minOccurs",
        "maxOccurs": "proc:maxOccurs"
      },
      "@id": "gp:inputs"
    },
    "outputs": {
      "@context": {
        "@vocab": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/outputs/",
        "dataType": {
          "@id": "dct:type",
          "@type": "@id"
        },
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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/raster-format-conversion/context.jsonld)

## Sources

* [ZOO-Project process-profiles: Concept / Generic Profile / Implementation Profile](https://zoo-project.github.io/docs/services/process-profiles.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/generic-profile/raster-format-conversion`

