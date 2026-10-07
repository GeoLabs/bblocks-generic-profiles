
# Generic Profile: Radiometric index (Schema)

`generic-profiles.generic-profile.radiometric-index` *v0.1*

Computes one or more named radiometric indices (e.g. NDVI, NDWI, SAVI) from the relevant spectral bands of one or more input rasters. One or more Raster inputs, the name(s) of the index/indices to compute, one Raster output (one band per selected index).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Generic Profile: **Radiometric index**.

> Computes one or more named radiometric indices (e.g. NDVI, NDWI, SAVI) from the relevant spectral bands of one or more input rasters. One or more Raster inputs, the name(s) of the index/indices to compute, one Raster output (one band per selected index).

## Source

- ISO 19123-1:2023 *Geographic information -- Schema for coverage geometry and functions -- Part
  1: Fundamentals* -- the abstract coverage domain/range model this signature is grounded in (see
  [its Concept](../../concept/raster-coverage-processing/) for the full citation).
- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic
  Profile is.

## Relations

- `broader`: [`generic-profiles.concept.raster-coverage-processing`](../../concept/raster-coverage-processing/)
- Refined by (1 Implementation Profile):
- [`radiometric-index`](../../implementation-profile/radiometric-index/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).

## Examples

### Radiometric index
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index",
  "type": "GenericProfile",
  "prefLabel": "Radiometric index",
  "definition": "Computes one or more named radiometric indices (e.g. NDVI, NDWI, SAVI) from the relevant spectral bands of one or more input rasters. One or more Raster inputs, the name(s) of the index/indices to compute, one Raster output (one band per selected index).",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile",
  "status": "submitted",
  "broader": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
  ],
  "keywords": [
    "raster",
    "coverage",
    "radiometric index"
  ],
  "inputs": {
    "rasters": {
      "title": "Raster",
      "description": "the input spectral band(s)",
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
      "maxOccurs": "unbounded"
    },
    "index": {
      "title": "String",
      "description": "the name of the radiometric index (or indices) to compute",
      "keywords": [
        "radiometric index"
      ],
      "metadata": [
        {
          "title": "Process Concept: Raster Coverage Processing",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
        }
      ],
      "minOccurs": 1,
      "maxOccurs": "unbounded"
    }
  },
  "outputs": {
    "raster": {
      "title": "Raster",
      "description": "the resulting raster (one band per selected index)",
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
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/radiometric-index/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index",
  "type": "GenericProfile",
  "prefLabel": "Radiometric index",
  "definition": "Computes one or more named radiometric indices (e.g. NDVI, NDWI, SAVI) from the relevant spectral bands of one or more input rasters. One or more Raster inputs, the name(s) of the index/indices to compute, one Raster output (one band per selected index).",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile",
  "status": "submitted",
  "broader": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
  ],
  "keywords": [
    "raster",
    "coverage",
    "radiometric index"
  ],
  "inputs": {
    "rasters": {
      "title": "Raster",
      "description": "the input spectral band(s)",
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
      "maxOccurs": "unbounded"
    },
    "index": {
      "title": "String",
      "description": "the name of the radiometric index (or indices) to compute",
      "keywords": [
        "radiometric index"
      ],
      "metadata": [
        {
          "title": "Process Concept: Raster Coverage Processing",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
        }
      ],
      "minOccurs": 1,
      "maxOccurs": "unbounded"
    }
  },
  "outputs": {
    "raster": {
      "title": "Raster",
      "description": "the resulting raster (one band per selected index)",
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

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> ;
    skos:definition "Computes one or more named radiometric indices (e.g. NDVI, NDWI, SAVI) from the relevant spectral bands of one or more input rasters. One or more Raster inputs, the name(s) of the index/indices to compute, one Raster output (one band per selected index)." ;
    skos:inScheme gp:generic-profile ;
    skos:prefLabel "Radiometric index" ;
    gp:inputs [ ns1:index [ dcterms:description "the name of the radiometric index (or indices) to compute" ;
                    dcterms:title "String" ;
                    proc:keywords "radiometric index" ;
                    proc:maxOccurs "unbounded" ;
                    proc:metadata [ dcterms:title "Process Concept: Raster Coverage Processing" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] ;
                    proc:minOccurs 1 ] ;
            ns1:rasters [ dcterms:description "the input spectral band(s)" ;
                    dcterms:title "Raster" ;
                    proc:keywords "raster" ;
                    proc:maxOccurs "unbounded" ;
                    proc:metadata [ dcterms:title "Process Concept: Raster Coverage Processing" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] ;
                    proc:minOccurs 1 ] ] ;
    gp:outputs [ ns2:raster [ dcterms:description "the resulting raster (one band per selected index)" ;
                    dcterms:title "Raster" ;
                    proc:keywords "raster" ;
                    proc:metadata [ dcterms:title "Process Concept: Raster Coverage Processing" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] ] ] ;
    gp:status "submitted" ;
    proc:keywords "coverage",
        "radiometric index",
        "raster" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Generic Profile "Radiometric index" -- see generic-profiles.generic-profile
  for the general shape every Generic Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index
      x-jsonld-id: '@id'
    type:
      const: GenericProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Radiometric index
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

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/radiometric-index/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/radiometric-index/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/radiometric-index/context.jsonld)

## Sources

* [ZOO-Project process-profiles: Concept / Generic Profile / Implementation Profile](https://zoo-project.github.io/docs/services/process-profiles.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/generic-profile/radiometric-index`

