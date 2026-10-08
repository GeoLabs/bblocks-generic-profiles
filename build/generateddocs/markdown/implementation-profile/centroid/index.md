
# Implementation Profile: Centroid (Schema)

`generic-profiles.implementation-profile.centroid` *v0.1*

The mathematical centroid for this Surface as a Point. The result is not guaranteed to be on this Surface.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Implementation Profile: **Centroid**.

> The mathematical centroid for this Surface as a Point. The result is not guaranteed to be on this Surface.

## Source

- [OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1, §2.1.9.1 Centroid()](https://www.ogc.org/standards/sfs/)
- ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_Centroid
- [ZOO-Project Geonovum testbed -- Centroid: Computes the centroid of a polygon.](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Centroid)

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.unary-geometry-operation`](../../generic-profile/unary-geometry-operation/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.vector.*` in `bblocks-process-profiles` -- a real
process of the ZOO-Project Geonovum testbed.

## Examples

### Centroid
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/centroid",
  "type": "ImplementationProfile",
  "prefLabel": "Centroid",
  "definition": "The mathematical centroid for this Surface as a Point. The result is not guaranteed to be on this Surface.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation",
  "keywords": [
    "vector",
    "geometry",
    "derived geometry",
    "Centroid",
    "ST_Centroid"
  ],
  "metadata": [
    {
      "title": "Process Concept: Vector Geometry Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"
    },
    {
      "title": "Generic Profile: Unary geometry operation",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation"
    }
  ],
  "inputs": {
    "geometry": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/centroid/inputs/geometry",
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
          "title": "Generic Profile: Unary geometry operation -- input `geometry`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation/inputs/geometry"
        }
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/centroid/outputs/result",
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
          "title": "Generic Profile: Unary geometry operation -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation/outputs/result"
        }
      ]
    }
  },
  "source": [
    {
      "title": "OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1, \u00a72.1.9.1 Centroid()",
      "link": "https://www.ogc.org/standards/sfs/"
    },
    {
      "title": "ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_Centroid"
    },
    {
      "title": "ZOO-Project Geonovum testbed -- Centroid: Computes the centroid of a polygon.",
      "link": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Centroid"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/centroid/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/centroid",
  "type": "ImplementationProfile",
  "prefLabel": "Centroid",
  "definition": "The mathematical centroid for this Surface as a Point. The result is not guaranteed to be on this Surface.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation",
  "keywords": [
    "vector",
    "geometry",
    "derived geometry",
    "Centroid",
    "ST_Centroid"
  ],
  "metadata": [
    {
      "title": "Process Concept: Vector Geometry Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"
    },
    {
      "title": "Generic Profile: Unary geometry operation",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation"
    }
  ],
  "inputs": {
    "geometry": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/centroid/inputs/geometry",
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
          "title": "Generic Profile: Unary geometry operation -- input `geometry`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation/inputs/geometry"
        }
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/centroid/outputs/result",
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
          "title": "Generic Profile: Unary geometry operation -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation/outputs/result"
        }
      ]
    }
  },
  "source": [
    {
      "title": "OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1, \u00a72.1.9.1 Centroid()",
      "link": "https://www.ogc.org/standards/sfs/"
    },
    {
      "title": "ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_Centroid"
    },
    {
      "title": "ZOO-Project Geonovum testbed -- Centroid: Computes the centroid of a polygon.",
      "link": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Centroid"
    }
  ]
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

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/centroid> a skos:Concept ;
    dcterms:source [ dcterms:references <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Centroid> ;
            dcterms:title "ZOO-Project Geonovum testbed -- Centroid: Computes the centroid of a polygon." ],
        [ dcterms:references <https://www.ogc.org/standards/sfs/> ;
            dcterms:title "OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1, §2.1.9.1 Centroid()" ],
        [ dcterms:title "ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_Centroid" ] ;
    skos:definition "The mathematical centroid for this Surface as a Point. The result is not guaranteed to be on this Surface." ;
    skos:inScheme gp:implementation-profile ;
    skos:prefLabel "Centroid" ;
    gp:inputs [ ns3:geometry <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/centroid/inputs/geometry> ] ;
    gp:outputs [ ns2:result <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/centroid/outputs/result> ] ;
    gp:refinesGenericProfile <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation> ;
    gp:status "submitted" ;
    proc:keywords "Centroid",
        "ST_Centroid",
        "derived geometry",
        "geometry",
        "vector" ;
    proc:metadata [ dcterms:title "Process Concept: Vector Geometry Processing" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ],
        [ dcterms:title "Generic Profile: Unary geometry operation" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/centroid/inputs/geometry> proc:keywords "GML",
        "geometry" ;
    proc:metadata [ dcterms:title "Generic Profile: Unary geometry operation -- input `geometry`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation/inputs/geometry> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] ;
    proc:schema [ a ns1:string ;
            ns1:contentMediaType "text/xml" ;
            ns1:description "GML" ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/centroid/outputs/result> proc:keywords "GML",
        "geometry" ;
    proc:metadata [ dcterms:title "Generic Profile: Unary geometry operation -- output `result`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation/outputs/result> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output> ] ;
    proc:schema [ a ns1:string ;
            ns1:contentMediaType "text/xml" ;
            ns1:description "GML" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Implementation Profile "Centroid" -- see generic-profiles.implementation-profile
  for the general shape every Implementation Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/centroid
      x-jsonld-id: '@id'
    type:
      const: ImplementationProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Centroid
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
    refinesGenericProfile:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/refinesGenericProfile
      x-jsonld-type: '@id'
    keywords:
      allOf:
      - contains:
          const: vector
      - contains:
          const: geometry
      - contains:
          const: derived geometry
      x-jsonld-id: https://w3id.org/ogc/api/processes/keywords
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
      - contains:
          type: object
          required:
          - role
          - href
          properties:
            role:
              const: http://www.opengis.net/spec/wps/2.0/def/process-profile/generic
            href:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation
      x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
    inputs:
      type: object
      required:
      - geometry
      properties:
        geometry:
          properties:
            keywords:
              allOf:
              - contains:
                  const: geometry
              x-jsonld-id: https://w3id.org/ogc/api/processes/keywords
            metadata:
              allOf:
              - contains:
                  type: object
                  required:
                  - role
                  - href
                  properties:
                    role:
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input
                    href:
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation/inputs/geometry
              x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
            maxOccurs:
              type: integer
              maximum: 1
              x-jsonld-id: https://w3id.org/ogc/api/processes/maxOccurs
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/
    outputs:
      type: object
      required:
      - result
      properties:
        result:
          properties:
            keywords:
              allOf:
              - contains:
                  const: geometry
              x-jsonld-id: https://w3id.org/ogc/api/processes/keywords
            metadata:
              allOf:
              - contains:
                  type: object
                  required:
                  - role
                  - href
                  properties:
                    role:
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output
                    href:
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation/outputs/result
              x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/outputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/
- type: object
  properties:
    inputs:
      properties:
        geometry:
          required:
          - id
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/centroid/inputs/geometry
              x-jsonld-id: '@id'
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/
    outputs:
      properties:
        result:
          required:
          - id
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/centroid/outputs/result
              x-jsonld-id: '@id'
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/outputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/
x-jsonld-extra-terms:
  ImplementationProfile: http://www.w3.org/2004/02/skos/core#Concept
  definition: http://www.w3.org/2004/02/skos/core#definition
  inScheme:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#inScheme
    x-jsonld-type: '@id'
  status: https://geolabs.github.io/bblocks-generic-profiles/def/status
  source: http://purl.org/dc/terms/source
  title: http://purl.org/dc/terms/title
  link:
    x-jsonld-id: http://purl.org/dc/terms/references
    x-jsonld-type: '@id'
x-jsonld-prefixes:
  skos: http://www.w3.org/2004/02/skos/core#
  gp: https://geolabs.github.io/bblocks-generic-profiles/def/
  proc: https://w3id.org/ogc/api/processes/
  dct: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/centroid/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/centroid/schema.yaml)


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
    "source": "dct:source",
    "title": "dct:title",
    "link": {
      "@id": "dct:references",
      "@type": "@id"
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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/centroid/context.jsonld)

## Sources

* [OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1, §2.1.9.1 Centroid()](https://www.ogc.org/standards/sfs/)
* ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_Centroid
* [ZOO-Project Geonovum testbed -- Centroid: Computes the centroid of a polygon.](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Centroid)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/implementation-profile/centroid`

