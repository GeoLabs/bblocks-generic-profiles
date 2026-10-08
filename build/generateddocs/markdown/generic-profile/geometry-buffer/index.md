
# Generic Profile: Geometry buffer (Schema)

`generic-profiles.generic-profile.geometry-buffer` *v0.1*

Computes a new geometry from one input geometry and a scalar distance. A different shape from binary-spatial-operation: one Geometry, one Number, not two Geometries.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Generic Profile: **Geometry buffer**.

> Computes a new geometry from one input geometry and a scalar distance: one Geometry, one Number, one Geometry output.

## Source

- [OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture](https://www.ogc.org/standards/sfa/) -- the operations
  below are each defined there, at their own clause (see each Implementation Profile).
- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic Profile is.

## Relations

- `broader`: [`generic-profiles.concept.vector-geometry-processing`](../../concept/vector-geometry-processing/)
- Refined by (1 Implementation Profile):
- [`buffer`](../../implementation-profile/buffer/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).

## Examples

### Geometry buffer
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-buffer",
  "type": "GenericProfile",
  "prefLabel": "Geometry buffer",
  "definition": "Computes a new geometry from one input geometry and a scalar distance. A different shape from binary-spatial-operation: one Geometry, one Number, not two Geometries.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile",
  "status": "submitted",
  "broader": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"
  ],
  "keywords": [
    "vector",
    "geometry",
    "spatial analysis",
    "buffer"
  ],
  "metadata": [
    {
      "title": "Process Concept: Vector Geometry Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"
    }
  ],
  "inputs": {
    "geometry": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-buffer/inputs/geometry",
      "title": "Geometry",
      "description": "the input geometry",
      "keywords": [
        "geometry"
      ],
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "distance": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-buffer/inputs/distance",
      "title": "Number",
      "description": "the buffer distance",
      "keywords": [
        "distance"
      ],
      "minOccurs": 1,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-buffer/outputs/result",
      "title": "Geometry",
      "description": "the buffered geometry",
      "keywords": [
        "geometry"
      ]
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/geometry-buffer/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-buffer",
  "type": "GenericProfile",
  "prefLabel": "Geometry buffer",
  "definition": "Computes a new geometry from one input geometry and a scalar distance. A different shape from binary-spatial-operation: one Geometry, one Number, not two Geometries.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile",
  "status": "submitted",
  "broader": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"
  ],
  "keywords": [
    "vector",
    "geometry",
    "spatial analysis",
    "buffer"
  ],
  "metadata": [
    {
      "title": "Process Concept: Vector Geometry Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"
    }
  ],
  "inputs": {
    "geometry": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-buffer/inputs/geometry",
      "title": "Geometry",
      "description": "the input geometry",
      "keywords": [
        "geometry"
      ],
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "distance": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-buffer/inputs/distance",
      "title": "Number",
      "description": "the buffer distance",
      "keywords": [
        "distance"
      ],
      "minOccurs": 1,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-buffer/outputs/result",
      "title": "Geometry",
      "description": "the buffered geometry",
      "keywords": [
        "geometry"
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

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-buffer> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing> ;
    skos:definition "Computes a new geometry from one input geometry and a scalar distance. A different shape from binary-spatial-operation: one Geometry, one Number, not two Geometries." ;
    skos:inScheme gp:generic-profile ;
    skos:prefLabel "Geometry buffer" ;
    gp:inputs [ ns2:distance <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-buffer/inputs/distance> ;
            ns2:geometry <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-buffer/inputs/geometry> ] ;
    gp:outputs [ ns1:result <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-buffer/outputs/result> ] ;
    gp:status "submitted" ;
    proc:keywords "buffer",
        "geometry",
        "spatial analysis",
        "vector" ;
    proc:metadata [ dcterms:title "Process Concept: Vector Geometry Processing" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-buffer/inputs/distance> dcterms:description "the buffer distance" ;
    dcterms:title "Number" ;
    proc:keywords "distance" ;
    proc:maxOccurs 1 ;
    proc:minOccurs 1 .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-buffer/inputs/geometry> dcterms:description "the input geometry" ;
    dcterms:title "Geometry" ;
    proc:keywords "geometry" ;
    proc:maxOccurs 1 ;
    proc:minOccurs 1 .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-buffer/outputs/result> dcterms:description "the buffered geometry" ;
    dcterms:title "Geometry" ;
    proc:keywords "geometry" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Generic Profile "Geometry buffer" -- see generic-profiles.generic-profile
  for the general shape every Generic Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-buffer
      x-jsonld-id: '@id'
    type:
      const: GenericProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Geometry buffer
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing
      x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
    inputs:
      properties:
        geometry:
          required:
          - id
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-buffer/inputs/geometry
              x-jsonld-id: '@id'
        distance:
          required:
          - id
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-buffer/inputs/distance
              x-jsonld-id: '@id'
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/inputs/
    outputs:
      properties:
        result:
          required:
          - id
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-buffer/outputs/result
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

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/geometry-buffer/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/geometry-buffer/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/geometry-buffer/context.jsonld)

## Sources

* [ZOO-Project process-profiles: Concept / Generic Profile / Implementation Profile](https://zoo-project.github.io/docs/services/process-profiles.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/generic-profile/geometry-buffer`

