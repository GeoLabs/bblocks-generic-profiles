
# Generic Profile: Terrain derivative (Schema)

`generic-profiles.generic-profile.terrain-derivative` *v0.1*

Derives one terrain attribute, as a single-band raster, from an elevation model. One elevation model input, one single-band raster output. Covers operations that differ only in the attribute computed (slope, aspect, curvature, terrain ruggedness, topographic position), not in signature.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Generic Profile: **Terrain derivative**.

> Derives one terrain attribute, as a single-band raster, from an elevation model. One elevation model input, one single-band raster output. Covers operations that differ only in the attribute computed (slope, aspect, curvature, terrain ruggedness, topographic position), not in signature.

## Signature

| | Name | Data type | Description |
|---|---|---|---|
| input | `elevation` | [`elevation-model`](../../data-type/) | the elevation model |
| output | `result` | [`raster-single-band`](../../data-type/) | the derived terrain attribute |

## Source

- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic Profile is.
- The operations below are each grounded in their own SAGA 7.3.0 tool documentation (see each
  Implementation Profile).

## Relations

- `broader`: [`generic-profiles.concept.terrain-analysis`](../../concept/terrain-analysis/)
- Refined by (3 Implementation Profiles): [`slope`](../../implementation-profile/slope/), [`terrain-ruggedness-index`](../../implementation-profile/terrain-ruggedness-index/), [`topographic-position-index`](../../implementation-profile/topographic-position-index/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).

## Examples

### Terrain derivative
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative",
  "type": "GenericProfile",
  "prefLabel": "Terrain derivative",
  "definition": "Derives one terrain attribute, as a single-band raster, from an elevation model. One elevation model input, one single-band raster output. Covers operations that differ only in the attribute computed (slope, aspect, curvature, terrain ruggedness, topographic position), not in signature.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile",
  "status": "submitted",
  "broader": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis"
  ],
  "keywords": [
    "terrain",
    "elevation",
    "raster",
    "derivative"
  ],
  "metadata": [
    {
      "title": "Process Concept: Terrain Analysis",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis"
    }
  ],
  "inputs": {
    "elevation": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative/inputs/elevation",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/elevation-model",
      "title": "Elevation model",
      "description": "the elevation model",
      "keywords": [
        "elevation"
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative/outputs/result",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster-single-band",
      "title": "Raster",
      "description": "the derived terrain attribute",
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
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/terrain-derivative/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative",
  "type": "GenericProfile",
  "prefLabel": "Terrain derivative",
  "definition": "Derives one terrain attribute, as a single-band raster, from an elevation model. One elevation model input, one single-band raster output. Covers operations that differ only in the attribute computed (slope, aspect, curvature, terrain ruggedness, topographic position), not in signature.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile",
  "status": "submitted",
  "broader": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis"
  ],
  "keywords": [
    "terrain",
    "elevation",
    "raster",
    "derivative"
  ],
  "metadata": [
    {
      "title": "Process Concept: Terrain Analysis",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis"
    }
  ],
  "inputs": {
    "elevation": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative/inputs/elevation",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/elevation-model",
      "title": "Elevation model",
      "description": "the elevation model",
      "keywords": [
        "elevation"
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative/outputs/result",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster-single-band",
      "title": "Raster",
      "description": "the derived terrain attribute",
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

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis> ;
    skos:definition "Derives one terrain attribute, as a single-band raster, from an elevation model. One elevation model input, one single-band raster output. Covers operations that differ only in the attribute computed (slope, aspect, curvature, terrain ruggedness, topographic position), not in signature." ;
    skos:inScheme gp:generic-profile ;
    skos:prefLabel "Terrain derivative" ;
    gp:inputs [ ns1:elevation <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative/inputs/elevation> ] ;
    gp:outputs [ ns2:result <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative/outputs/result> ] ;
    gp:status "submitted" ;
    proc:keywords "derivative",
        "elevation",
        "raster",
        "terrain" ;
    proc:metadata [ dcterms:title "Process Concept: Terrain Analysis" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative/inputs/elevation> dcterms:description "the elevation model" ;
    dcterms:title "Elevation model" ;
    dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/elevation-model> ;
    proc:keywords "elevation" .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative/outputs/result> dcterms:description "the derived terrain attribute" ;
    dcterms:title "Raster" ;
    dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster-single-band> ;
    proc:keywords "raster" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Generic Profile "Terrain derivative" -- see generic-profiles.generic-profile
  for the general shape every Generic Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative
      x-jsonld-id: '@id'
    type:
      const: GenericProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Terrain derivative
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis
      x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
    inputs:
      properties:
        elevation:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative/inputs/elevation
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type/elevation-model
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/inputs/
    outputs:
      properties:
        result:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative/outputs/result
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster-single-band
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

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/terrain-derivative/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/terrain-derivative/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/terrain-derivative/context.jsonld)

## Sources

* [ZOO-Project process-profiles: Concept / Generic Profile / Implementation Profile](https://zoo-project.github.io/docs/services/process-profiles.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/generic-profile/terrain-derivative`

