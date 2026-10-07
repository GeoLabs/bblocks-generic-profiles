
# Generic Profile: Raster crop (Schema)

`generic-profiles.generic-profile.raster-crop` *v0.1*

Crops a raster coverage to a region of interest. One Raster input, a bounding box, one Raster output covering only that area.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Generic Profile: **Raster crop**.

> Crops a raster coverage to a region of interest. One Raster input, a bounding box, one Raster output covering only that area.

## Source

- ISO 19123-1:2023 *Geographic information -- Schema for coverage geometry and functions -- Part
  1: Fundamentals* -- the abstract coverage domain/range model this signature is grounded in (see
  [its Concept](../../concept/raster-coverage-processing/) for the full citation).
- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic
  Profile is.

## `areaOfInterest` has no type at this tier

Two earlier drafts tried to give `areaOfInterest` a machine-checked abstract type at this tier --
first `Geometry` (the natural-seeming choice, since a region of interest reads like a geometric
object), then a dedicated `BoundingBox` type when `Geometry` turned out not to match its real
binding ([`raster-crop`](../../implementation-profile/raster-crop/)'s own `OTB.ExtractROI`, whose
"extent" mode takes four plain numbers, `mode.extent.ulx`/`uly`/`lrx`/`lry`, not an encoded
geometry). Both were unnecessary: [Table 21](https://docs.ogc.org/is/14-065/14-065.html#32) gives
Generic Profile no "Data format" row at all, so there is nothing to type here regardless of which
vocabulary is used. The distinction now lives entirely at Implementation Profile, where
`areaOfInterest`'s `schema` `$ref`s
[`ogc.api.processes.v1.schemas.bbox`](https://geolabs.github.io/bblocks-ogcapi-processes/)
directly -- OGC API - Processes - Part 1: Core's own bbox type (itself grounded in
[OGC 17-069r4](https://docs.ogc.org/is/17-069r4/17-069r4.html) §7.15.3's `bbox` parameter), not a
custom abstract type.

## Relations

- `broader`: [`generic-profiles.concept.raster-coverage-processing`](../../concept/raster-coverage-processing/)
- Refined by (1 Implementation Profile):
- [`raster-crop`](../../implementation-profile/raster-crop/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).

## Examples

### Raster crop
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop",
  "type": "GenericProfile",
  "prefLabel": "Raster crop",
  "definition": "Crops a raster coverage to a region of interest. One Raster input, an area of interest, one Raster output covering only that area.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile",
  "status": "submitted",
  "broader": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
  ],
  "keywords": [
    "raster",
    "coverage",
    "crop"
  ],
  "inputs": {
    "raster": {
      "title": "Raster",
      "description": "the input raster coverage",
      "keywords": [
        "raster"
      ],
      "metadata": [
        {
          "title": "Process Concept: Raster Coverage Processing",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
        }
      ],
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "areaOfInterest": {
      "title": "Bounding box",
      "description": "the region of interest to crop to",
      "keywords": [
        "bounding box"
      ],
      "metadata": [
        {
          "title": "Process Concept: Raster Coverage Processing",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
        }
      ],
      "minOccurs": 1,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "raster": {
      "title": "Raster",
      "description": "the cropped raster coverage",
      "keywords": [
        "raster"
      ],
      "metadata": [
        {
          "title": "Process Concept: Raster Coverage Processing",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
        }
      ]
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/raster-crop/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop",
  "type": "GenericProfile",
  "prefLabel": "Raster crop",
  "definition": "Crops a raster coverage to a region of interest. One Raster input, an area of interest, one Raster output covering only that area.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile",
  "status": "submitted",
  "broader": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
  ],
  "keywords": [
    "raster",
    "coverage",
    "crop"
  ],
  "inputs": {
    "raster": {
      "title": "Raster",
      "description": "the input raster coverage",
      "keywords": [
        "raster"
      ],
      "metadata": [
        {
          "title": "Process Concept: Raster Coverage Processing",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
        }
      ],
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "areaOfInterest": {
      "title": "Bounding box",
      "description": "the region of interest to crop to",
      "keywords": [
        "bounding box"
      ],
      "metadata": [
        {
          "title": "Process Concept: Raster Coverage Processing",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
        }
      ],
      "minOccurs": 1,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "raster": {
      "title": "Raster",
      "description": "the cropped raster coverage",
      "keywords": [
        "raster"
      ],
      "metadata": [
        {
          "title": "Process Concept: Raster Coverage Processing",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
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
@prefix ns1: <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/inputs/> .
@prefix ns2: <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/outputs/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> ;
    skos:definition "Crops a raster coverage to a region of interest. One Raster input, an area of interest, one Raster output covering only that area." ;
    skos:inScheme gp:generic-profile ;
    skos:prefLabel "Raster crop" ;
    gp:inputs [ ns1:areaOfInterest [ dcterms:description "the region of interest to crop to" ;
                    dcterms:title "Bounding box" ;
                    proc:keywords "bounding box" ;
                    proc:maxOccurs 1 ;
                    proc:metadata [ dcterms:title "Process Concept: Raster Coverage Processing" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] ;
                    proc:minOccurs 1 ] ;
            ns1:raster [ dcterms:description "the input raster coverage" ;
                    dcterms:title "Raster" ;
                    proc:keywords "raster" ;
                    proc:maxOccurs 1 ;
                    proc:metadata [ dcterms:title "Process Concept: Raster Coverage Processing" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] ;
                    proc:minOccurs 1 ] ] ;
    gp:outputs [ ns2:raster [ dcterms:description "the cropped raster coverage" ;
                    dcterms:title "Raster" ;
                    proc:keywords "raster" ;
                    proc:metadata [ dcterms:title "Process Concept: Raster Coverage Processing" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] ] ] ;
    gp:status "submitted" ;
    proc:keywords "coverage",
        "crop",
        "raster" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Generic Profile "Raster crop" -- see generic-profiles.generic-profile
  for the general shape every Generic Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop
      x-jsonld-id: '@id'
    type:
      const: GenericProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Raster crop
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
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
  inputs:
    x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/inputs
    x-jsonld-context:
      '@vocab': https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/inputs/
      title: http://purl.org/dc/terms/title
      description: http://purl.org/dc/terms/description
      keywords: https://w3id.org/ogc/api/processes/keywords
      metadata:
        '@id': https://w3id.org/ogc/api/processes/metadata
        '@context':
          title: http://purl.org/dc/terms/title
          role:
            '@id': https://w3id.org/ogc/api/processes/role
            '@type': '@id'
          href:
            '@id': https://w3id.org/ogc/api/processes/href
            '@type': '@id'
      minOccurs: https://w3id.org/ogc/api/processes/minOccurs
      maxOccurs: https://w3id.org/ogc/api/processes/maxOccurs
  outputs:
    x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/outputs
    x-jsonld-context:
      '@vocab': https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/outputs/
      title: http://purl.org/dc/terms/title
      description: http://purl.org/dc/terms/description
      keywords: https://w3id.org/ogc/api/processes/keywords
      metadata:
        '@id': https://w3id.org/ogc/api/processes/metadata
        '@context':
          title: http://purl.org/dc/terms/title
          role:
            '@id': https://w3id.org/ogc/api/processes/role
            '@type': '@id'
          href:
            '@id': https://w3id.org/ogc/api/processes/href
            '@type': '@id'
x-jsonld-prefixes:
  skos: http://www.w3.org/2004/02/skos/core#
  gp: https://geolabs.github.io/bblocks-generic-profiles/def/
  proc: https://w3id.org/ogc/api/processes/
  dct: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/raster-crop/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/raster-crop/schema.yaml)


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
    "source": "dct:source",
    "inputs": {
      "@context": {
        "@vocab": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/inputs/",
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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/raster-crop/context.jsonld)

## Sources

* [ZOO-Project process-profiles: Concept / Generic Profile / Implementation Profile](https://zoo-project.github.io/docs/services/process-profiles.html)
* [OGC API - Processes - Part 1: Core, InputDescription/OutputDescription](https://geolabs.github.io/bblocks-ogcapi-processes/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/generic-profile/raster-crop`

