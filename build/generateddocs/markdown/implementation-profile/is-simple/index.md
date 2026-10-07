
# Implementation Profile: Is simple (Schema)

`generic-profiles.implementation-profile.is-simple` *v0.1*

Returns 1 (TRUE) if this Geometry has no anomalous geometric points, such as self intersection or self tangency.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Implementation Profile: **Is simple**.

> Returns 1 (TRUE) if this Geometry has no anomalous geometric points, such as self intersection or self tangency.

## Source

- [OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1, §2.1.1.1 IsSimple()](https://www.ogc.org/standards/sfs/)
- ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_IsSimple
- [ZOO-Project Geonovum testbed -- IsSimple: IsSimple test.](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/IsSimple)

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.unary-spatial-predicate`](../../generic-profile/unary-spatial-predicate/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.vector.*` in `bblocks-process-profiles` -- a real
process of the ZOO-Project Geonovum testbed.

## Examples

### Is simple
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/is-simple",
  "type": "ImplementationProfile",
  "prefLabel": "Is simple",
  "definition": "Returns 1 (TRUE) if this Geometry has no anomalous geometric points, such as self intersection or self tangency.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-spatial-predicate",
  "keywords": [
    "vector",
    "geometry",
    "predicate",
    "IsSimple",
    "ST_IsSimple"
  ],
  "inputs": {
    "geometry": {
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
          "title": "Process Concept: Vector Geometry Processing",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"
        },
        {
          "title": "Generic Profile: Unary spatial predicate",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-spatial-predicate"
        }
      ]
    }
  },
  "outputs": {
    "result": {
      "keywords": [
        "boolean"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Unary spatial predicate",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-spatial-predicate"
        }
      ]
    }
  },
  "source": [
    {
      "title": "OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1, \u00a72.1.1.1 IsSimple()",
      "link": "https://www.ogc.org/standards/sfs/"
    },
    {
      "title": "ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_IsSimple"
    },
    {
      "title": "ZOO-Project Geonovum testbed -- IsSimple: IsSimple test.",
      "link": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/IsSimple"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://raw.githubusercontent.com/GeoLabs/bblocks-generic-profiles/undefined/build/annotated/implementation-profile/is-simple/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/is-simple",
  "type": "ImplementationProfile",
  "prefLabel": "Is simple",
  "definition": "Returns 1 (TRUE) if this Geometry has no anomalous geometric points, such as self intersection or self tangency.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-spatial-predicate",
  "keywords": [
    "vector",
    "geometry",
    "predicate",
    "IsSimple",
    "ST_IsSimple"
  ],
  "inputs": {
    "geometry": {
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
          "title": "Process Concept: Vector Geometry Processing",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"
        },
        {
          "title": "Generic Profile: Unary spatial predicate",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-spatial-predicate"
        }
      ]
    }
  },
  "outputs": {
    "result": {
      "keywords": [
        "boolean"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Unary spatial predicate",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-spatial-predicate"
        }
      ]
    }
  },
  "source": [
    {
      "title": "OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1, \u00a72.1.1.1 IsSimple()",
      "link": "https://www.ogc.org/standards/sfs/"
    },
    {
      "title": "ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_IsSimple"
    },
    {
      "title": "ZOO-Project Geonovum testbed -- IsSimple: IsSimple test.",
      "link": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/IsSimple"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix gp: <https://geolabs.github.io/bblocks-generic-profiles/def/> .
@prefix ns1: <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/> .
@prefix ns2: <https://w3id.org/ogc/api/schema/> .
@prefix ns3: <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/is-simple> a skos:Concept ;
    dcterms:source [ dcterms:references <https://www.ogc.org/standards/sfs/> ;
            dcterms:title "OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1, §2.1.1.1 IsSimple()" ],
        [ dcterms:title "ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_IsSimple" ],
        [ dcterms:references <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/IsSimple> ;
            dcterms:title "ZOO-Project Geonovum testbed -- IsSimple: IsSimple test." ] ;
    skos:definition "Returns 1 (TRUE) if this Geometry has no anomalous geometric points, such as self intersection or self tangency." ;
    skos:inScheme gp:implementation-profile ;
    skos:prefLabel "Is simple" ;
    gp:inputs [ ns1:geometry [ proc:keywords "GML",
                        "geometry" ;
                    proc:metadata [ dcterms:title "Generic Profile: Unary spatial predicate" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-spatial-predicate> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ],
                        [ dcterms:title "Process Concept: Vector Geometry Processing" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] ;
                    proc:schema [ a ns2:string ;
                            ns2:contentMediaType "text/xml" ;
                            ns2:description "GML" ] ] ] ;
    gp:outputs [ ns3:result [ proc:keywords "boolean" ;
                    proc:metadata [ dcterms:title "Generic Profile: Unary spatial predicate" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-spatial-predicate> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ] ] ] ;
    gp:refinesGenericProfile <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-spatial-predicate> ;
    gp:status "submitted" ;
    proc:keywords "IsSimple",
        "ST_IsSimple",
        "geometry",
        "predicate",
        "vector" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Implementation Profile "Is simple" -- see generic-profiles.implementation-profile
  for the general shape every Implementation Profile shares.
allOf:
- $ref: https://raw.githubusercontent.com/GeoLabs/bblocks-generic-profiles/undefined/build/annotated/implementation-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/is-simple
      x-jsonld-id: '@id'
    type:
      const: ImplementationProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Is simple
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
    refinesGenericProfile:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-spatial-predicate
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/refinesGenericProfile
      x-jsonld-type: '@id'
    keywords:
      allOf:
      - contains:
          const: vector
      - contains:
          const: geometry
      - contains:
          const: predicate
      x-jsonld-id: https://w3id.org/ogc/api/processes/keywords
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-spatial-predicate
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
                  const: boolean
              x-jsonld-id: https://w3id.org/ogc/api/processes/keywords
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

* YAML version: [schema.yaml](https://raw.githubusercontent.com/GeoLabs/bblocks-generic-profiles/undefined/build/annotated/implementation-profile/is-simple/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/GeoLabs/bblocks-generic-profiles/undefined/build/annotated/implementation-profile/is-simple/schema.yaml)


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
    "inputs": {
      "@context": {
        "@vocab": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/",
        "schema": {
          "@context": {
            "@vocab": "https://w3id.org/ogc/api/schema/"
          },
          "@id": "proc:schema"
        },
        "maxOccurs": "proc:maxOccurs",
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
        },
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
[context.jsonld](https://raw.githubusercontent.com/GeoLabs/bblocks-generic-profiles/undefined/build/annotated/implementation-profile/is-simple/context.jsonld)

## Sources

* [OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1, §2.1.1.1 IsSimple()](https://www.ogc.org/standards/sfs/)
* ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_IsSimple
* [ZOO-Project Geonovum testbed -- IsSimple: IsSimple test.](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/IsSimple)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/implementation-profile/is-simple`

