
# Generic Profile: Binary spatial set operation (Schema)

`generic-profiles.generic-profile.binary-spatial-operation` *v0.1*

Computes a new geometry from the point-set relationship of two input geometries. Shared I/O shape of the SQL/MM set-operation family: two Geometry inputs, one Geometry output.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Generic Profile: **Binary spatial set operation**.

> Computes a new geometry from the point-set relationship of two input geometries: two Geometry inputs, one Geometry output.

## Source

- [OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture](https://www.ogc.org/standards/sfa/) -- the operations
  below are each defined there, at their own clause (see each Implementation Profile).
- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic Profile is.

## Relations

- `broader`: [`generic-profiles.concept.vector-geometry-processing`](../../concept/vector-geometry-processing/)
- Refined by (4 Implementation Profiles):
- [`intersection`](../../implementation-profile/intersection/)
- [`union`](../../implementation-profile/union/)
- [`difference`](../../implementation-profile/difference/)
- [`symdifference`](../../implementation-profile/symdifference/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).

## Examples

### Binary spatial set operation
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation",
  "type": "GenericProfile",
  "prefLabel": "Binary spatial set operation",
  "definition": "Computes a new geometry from the point-set relationship of two input geometries. Shared I/O shape of the SQL/MM set-operation family: two Geometry inputs, one Geometry output.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile",
  "status": "submitted",
  "broader": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"
  ],
  "keywords": [
    "vector",
    "geometry",
    "spatial analysis",
    "set operation"
  ],
  "inputs": {
    "geometry1": {
      "title": "Geometry",
      "description": "the first geometry",
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
    },
    "geometry2": {
      "title": "Geometry",
      "description": "the second geometry",
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
      "title": "Geometry",
      "description": "the resulting geometry",
      "keywords": [
        "geometry"
      ],
      "metadata": [
        {
          "title": "Process Concept: Vector Geometry Processing",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"
        }
      ]
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/binary-spatial-operation/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation",
  "type": "GenericProfile",
  "prefLabel": "Binary spatial set operation",
  "definition": "Computes a new geometry from the point-set relationship of two input geometries. Shared I/O shape of the SQL/MM set-operation family: two Geometry inputs, one Geometry output.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile",
  "status": "submitted",
  "broader": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"
  ],
  "keywords": [
    "vector",
    "geometry",
    "spatial analysis",
    "set operation"
  ],
  "inputs": {
    "geometry1": {
      "title": "Geometry",
      "description": "the first geometry",
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
    },
    "geometry2": {
      "title": "Geometry",
      "description": "the second geometry",
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
      "title": "Geometry",
      "description": "the resulting geometry",
      "keywords": [
        "geometry"
      ],
      "metadata": [
        {
          "title": "Process Concept: Vector Geometry Processing",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"
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

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing> ;
    skos:definition "Computes a new geometry from the point-set relationship of two input geometries. Shared I/O shape of the SQL/MM set-operation family: two Geometry inputs, one Geometry output." ;
    skos:inScheme gp:generic-profile ;
    skos:prefLabel "Binary spatial set operation" ;
    gp:inputs [ ns1:geometry1 [ dcterms:description "the first geometry" ;
                    dcterms:title "Geometry" ;
                    proc:keywords "geometry" ;
                    proc:maxOccurs 1 ;
                    proc:metadata [ dcterms:title "Process Concept: Vector Geometry Processing" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] ;
                    proc:minOccurs 1 ] ;
            ns1:geometry2 [ dcterms:description "the second geometry" ;
                    dcterms:title "Geometry" ;
                    proc:keywords "geometry" ;
                    proc:maxOccurs 1 ;
                    proc:metadata [ dcterms:title "Process Concept: Vector Geometry Processing" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] ;
                    proc:minOccurs 1 ] ] ;
    gp:outputs [ ns2:result [ dcterms:description "the resulting geometry" ;
                    dcterms:title "Geometry" ;
                    proc:keywords "geometry" ;
                    proc:metadata [ dcterms:title "Process Concept: Vector Geometry Processing" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] ] ] ;
    gp:status "submitted" ;
    proc:keywords "geometry",
        "set operation",
        "spatial analysis",
        "vector" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Generic Profile "Binary spatial set operation" -- see generic-profiles.generic-profile
  for the general shape every Generic Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation
      x-jsonld-id: '@id'
    type:
      const: GenericProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Binary spatial set operation
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

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/binary-spatial-operation/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/binary-spatial-operation/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/binary-spatial-operation/context.jsonld)

## Sources

* [ZOO-Project process-profiles: Concept / Generic Profile / Implementation Profile](https://zoo-project.github.io/docs/services/process-profiles.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/generic-profile/binary-spatial-operation`

