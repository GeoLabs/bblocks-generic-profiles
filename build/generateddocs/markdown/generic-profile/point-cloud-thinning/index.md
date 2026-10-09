
# Generic Profile: Point cloud thinning (Schema)

`generic-profiles.generic-profile.point-cloud-thinning` *v0.1*

Reduces the number of points of a point cloud. One point cloud and the share of points to keep in, one point cloud out.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Generic Profile: **Point cloud thinning**.

> Reduces the number of points of a point cloud. One point cloud and the share of points to keep in, one point cloud out.

## Signature

| | Name | Data type | Description |
|---|---|---|---|
| input | `points` | [`point-cloud`](../../data-type/) | the input point cloud |
| input | `percentage` | [`number`](../../data-type/) | the share of points to keep, in percent |
| output | `result` | [`point-cloud`](../../data-type/) | the thinned point cloud |

## Source

- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic Profile is.
- The operations below are each grounded in their own SAGA 7.3.0 tool documentation (see each
  Implementation Profile).

## Relations

- `broader`: [`generic-profiles.concept.point-cloud-processing`](../../concept/point-cloud-processing/)
- Refined by (1 Implementation Profile): [`point-cloud-thinning`](../../implementation-profile/point-cloud-thinning/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).

## Examples

### Point cloud thinning
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning",
  "type": "GenericProfile",
  "prefLabel": "Point cloud thinning",
  "definition": "Reduces the number of points of a point cloud. One point cloud and the share of points to keep in, one point cloud out.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile",
  "status": "submitted",
  "broader": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/point-cloud-processing"
  ],
  "keywords": [
    "point cloud",
    "thinning"
  ],
  "metadata": [
    {
      "title": "Process Concept: Point Cloud Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/point-cloud-processing"
    }
  ],
  "inputs": {
    "points": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/inputs/points",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/point-cloud",
      "title": "Point cloud",
      "description": "the input point cloud",
      "keywords": [
        "point cloud"
      ]
    },
    "percentage": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/inputs/percentage",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/number",
      "title": "Number",
      "description": "the share of points to keep, in percent",
      "keywords": [
        "percentage"
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/outputs/result",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/point-cloud",
      "title": "Point cloud",
      "description": "the thinned point cloud",
      "keywords": [
        "point cloud"
      ]
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/point-cloud-thinning/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning",
  "type": "GenericProfile",
  "prefLabel": "Point cloud thinning",
  "definition": "Reduces the number of points of a point cloud. One point cloud and the share of points to keep in, one point cloud out.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile",
  "status": "submitted",
  "broader": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/point-cloud-processing"
  ],
  "keywords": [
    "point cloud",
    "thinning"
  ],
  "metadata": [
    {
      "title": "Process Concept: Point Cloud Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/point-cloud-processing"
    }
  ],
  "inputs": {
    "points": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/inputs/points",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/point-cloud",
      "title": "Point cloud",
      "description": "the input point cloud",
      "keywords": [
        "point cloud"
      ]
    },
    "percentage": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/inputs/percentage",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/number",
      "title": "Number",
      "description": "the share of points to keep, in percent",
      "keywords": [
        "percentage"
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/outputs/result",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/point-cloud",
      "title": "Point cloud",
      "description": "the thinned point cloud",
      "keywords": [
        "point cloud"
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

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-generic-profiles/def/concept/point-cloud-processing> ;
    skos:definition "Reduces the number of points of a point cloud. One point cloud and the share of points to keep in, one point cloud out." ;
    skos:inScheme gp:generic-profile ;
    skos:prefLabel "Point cloud thinning" ;
    gp:inputs [ ns2:percentage <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/inputs/percentage> ;
            ns2:points <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/inputs/points> ] ;
    gp:outputs [ ns1:result <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/outputs/result> ] ;
    gp:status "submitted" ;
    proc:keywords "point cloud",
        "thinning" ;
    proc:metadata [ dcterms:title "Process Concept: Point Cloud Processing" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/point-cloud-processing> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/inputs/percentage> dcterms:description "the share of points to keep, in percent" ;
    dcterms:title "Number" ;
    dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/number> ;
    proc:keywords "percentage" .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/inputs/points> dcterms:description "the input point cloud" ;
    dcterms:title "Point cloud" ;
    dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/point-cloud> ;
    proc:keywords "point cloud" .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/outputs/result> dcterms:description "the thinned point cloud" ;
    dcterms:title "Point cloud" ;
    dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/point-cloud> ;
    proc:keywords "point cloud" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Generic Profile "Point cloud thinning" -- see generic-profiles.generic-profile
  for the general shape every Generic Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning
      x-jsonld-id: '@id'
    type:
      const: GenericProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Point cloud thinning
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/concept/point-cloud-processing
      x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
    inputs:
      properties:
        points:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/inputs/points
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type/point-cloud
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
        percentage:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/inputs/percentage
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type/number
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/outputs/result
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type/point-cloud
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

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/point-cloud-thinning/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/point-cloud-thinning/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/point-cloud-thinning/context.jsonld)

## Sources

* [ZOO-Project process-profiles: Concept / Generic Profile / Implementation Profile](https://zoo-project.github.io/docs/services/process-profiles.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/generic-profile/point-cloud-thinning`

