
# Implementation Profile: Symmetric difference (Schema)

`generic-profiles.implementation-profile.symdifference` *v0.1*

Returns a geometric object representing the point set symmetric difference of this geometric object with anotherGeometry.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Implementation Profile: **Symmetric difference**.

> Returns a geometric object representing the point set symmetric difference of this geometric object with anotherGeometry.

## Source

Two standards define this operation at different levels -- the abstract semantics, and the
concrete SQL binding an Implementation Profile is specifically meant to add (OGC 14-065 WPS 2.0.2
§7.5.3, "down to the supported data exchange formats"):

- [OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture](https://www.ogc.org/standards/sfa/), §6.1.27 -- the
  operation's abstract definition (this is what [its Concept](../../concept/vector-geometry-processing/)
  and [Generic Profile](../../generic-profile/binary-spatial-operation/) are grounded in too).
- ISO/IEC 13249-3:2016 *SQL multimedia and application packages -- Part 3: Spatial*, §5.1.48 ST_SymDifference
  -- the same operation bound to SQL: the `ST_Geometry` type and the `ST_SymDifference` function name,
  of which this Implementation Profile's `prefLabel` (`Symmetric difference`) is the SFA name without the `ST_`
  prefix SQL/MM adds. SQL/MM is why this tier exists at all: it is, precisely, an implementation
  profile of Simple Feature Access for SQL -- the same abstract operation, bound to one concrete
  language and type system, still not any one vendor's specific deployment of it.

## Illustration

No PostGIS workshop illustration exists for this operation. Same gap as `difference`: PostGIS's workshop chapter on geometry-returning functions does not cover `ST_SymDifference` at all, so there is no matching illustration to reuse here.

## Data formats

`geometry1`, `geometry2`, `result`: GML -- the register's minimal default (Table 21, D: Declare), grounded in the real ZOO-Project Geonovum testbed, whose SQL/MM processes expose geometries as `text/xml` (GML) only, never WKT or GeoJSON (checked across `Intersects`, `Buffer`, `Intersection`).

Per [OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32), a specific deployment may *Extend* (E, footnote d) this minimal default with additional formats it happens to support -- this tier intentionally does not pre-empt that.

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.binary-spatial-operation`](../../generic-profile/binary-spatial-operation/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see [`ospd.process-profiles.sqlmm.symdifference`](https://github.com/GeoLabs/bblocks-process-profiles/tree/master/_sources/sqlmm/symdifference)
in `bblocks-process-profiles` -- a real process of the ZOO-Project Geonovum testbed
(<https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Symmetric difference>), which matches this tier's own minimal default (GML), specialised to one concrete version and root element, GML 3.1.0 Polygon.

## Examples

### Symmetric difference
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/symdifference",
  "type": "ImplementationProfile",
  "prefLabel": "Symmetric difference",
  "definition": "Returns a geometric object representing the point set symmetric difference of this geometric object with anotherGeometry.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation",
  "keywords": [
    "vector",
    "geometry",
    "spatial analysis",
    "set operation",
    "SymDifference",
    "ST_SymDifference"
  ],
  "inputs": {
    "geometry1": {
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
          "title": "Generic Profile: Binary spatial set operation",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation"
        }
      ]
    },
    "geometry2": {
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
          "title": "Generic Profile: Binary spatial set operation",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation"
        }
      ]
    }
  },
  "outputs": {
    "result": {
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
          "title": "Generic Profile: Binary spatial set operation",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation"
        }
      ]
    }
  },
  "source": [
    {
      "title": "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture, \u00a76.1.27",
      "link": "https://www.ogc.org/standards/sfa/"
    },
    {
      "title": "ISO/IEC 13249-3:2016 Information technology -- Database languages -- SQL multimedia and application packages -- Part 3: Spatial, \u00a75.1.48 ST_SymDifference"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://raw.githubusercontent.com/GeoLabs/bblocks-generic-profiles/undefined/build/annotated/implementation-profile/symdifference/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/symdifference",
  "type": "ImplementationProfile",
  "prefLabel": "Symmetric difference",
  "definition": "Returns a geometric object representing the point set symmetric difference of this geometric object with anotherGeometry.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation",
  "keywords": [
    "vector",
    "geometry",
    "spatial analysis",
    "set operation",
    "SymDifference",
    "ST_SymDifference"
  ],
  "inputs": {
    "geometry1": {
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
          "title": "Generic Profile: Binary spatial set operation",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation"
        }
      ]
    },
    "geometry2": {
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
          "title": "Generic Profile: Binary spatial set operation",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation"
        }
      ]
    }
  },
  "outputs": {
    "result": {
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
          "title": "Generic Profile: Binary spatial set operation",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation"
        }
      ]
    }
  },
  "source": [
    {
      "title": "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture, \u00a76.1.27",
      "link": "https://www.ogc.org/standards/sfa/"
    },
    {
      "title": "ISO/IEC 13249-3:2016 Information technology -- Database languages -- SQL multimedia and application packages -- Part 3: Spatial, \u00a75.1.48 ST_SymDifference"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix gp: <https://geolabs.github.io/bblocks-generic-profiles/def/> .
@prefix ns1: <https://w3id.org/ogc/api/schema/> .
@prefix ns2: <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/> .
@prefix ns3: <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/symdifference> a skos:Concept ;
    dcterms:source [ dcterms:title "ISO/IEC 13249-3:2016 Information technology -- Database languages -- SQL multimedia and application packages -- Part 3: Spatial, §5.1.48 ST_SymDifference" ],
        [ dcterms:references <https://www.ogc.org/standards/sfa/> ;
            dcterms:title "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture, §6.1.27" ] ;
    skos:definition "Returns a geometric object representing the point set symmetric difference of this geometric object with anotherGeometry." ;
    skos:inScheme gp:implementation-profile ;
    skos:prefLabel "Symmetric difference" ;
    gp:inputs [ ns2:geometry1 [ proc:keywords "GML",
                        "geometry" ;
                    proc:metadata [ dcterms:title "Process Concept: Vector Geometry Processing" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ],
                        [ dcterms:title "Generic Profile: Binary spatial set operation" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ] ;
                    proc:schema [ a ns1:string ;
                            ns1:contentMediaType "text/xml" ;
                            ns1:description "GML" ] ] ;
            ns2:geometry2 [ proc:keywords "GML",
                        "geometry" ;
                    proc:metadata [ dcterms:title "Process Concept: Vector Geometry Processing" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ],
                        [ dcterms:title "Generic Profile: Binary spatial set operation" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ] ;
                    proc:schema [ a ns1:string ;
                            ns1:contentMediaType "text/xml" ;
                            ns1:description "GML" ] ] ] ;
    gp:outputs [ ns3:result [ proc:keywords "GML",
                        "geometry" ;
                    proc:metadata [ dcterms:title "Generic Profile: Binary spatial set operation" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ] ;
                    proc:schema [ a ns1:string ;
                            ns1:contentMediaType "text/xml" ;
                            ns1:description "GML" ] ] ] ;
    gp:refinesGenericProfile <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation> ;
    gp:status "submitted" ;
    proc:keywords "ST_SymDifference",
        "SymDifference",
        "geometry",
        "set operation",
        "spatial analysis",
        "vector" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Implementation Profile "Symmetric difference" -- see generic-profiles.implementation-profile
  for the general shape every Implementation Profile shares.
allOf:
- $ref: https://raw.githubusercontent.com/GeoLabs/bblocks-generic-profiles/undefined/build/annotated/implementation-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/symdifference
      x-jsonld-id: '@id'
    type:
      const: ImplementationProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Symmetric difference
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
    refinesGenericProfile:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/refinesGenericProfile
      x-jsonld-type: '@id'
    keywords:
      allOf:
      - contains:
          const: vector
      - contains:
          const: geometry
      - contains:
          const: spatial analysis
      - contains:
          const: set operation
      x-jsonld-id: https://w3id.org/ogc/api/processes/keywords
    inputs:
      type: object
      required:
      - geometry1
      - geometry2
      properties:
        geometry1:
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation
              x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
            maxOccurs:
              type: integer
              maximum: 1
              x-jsonld-id: https://w3id.org/ogc/api/processes/maxOccurs
        geometry2:
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-operation
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

* YAML version: [schema.yaml](https://raw.githubusercontent.com/GeoLabs/bblocks-generic-profiles/undefined/build/annotated/implementation-profile/symdifference/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/GeoLabs/bblocks-generic-profiles/undefined/build/annotated/implementation-profile/symdifference/schema.yaml)


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
[context.jsonld](https://raw.githubusercontent.com/GeoLabs/bblocks-generic-profiles/undefined/build/annotated/implementation-profile/symdifference/context.jsonld)

## Sources

* [OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture, §6.1.27](https://www.ogc.org/standards/sfa/)
* ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, §5.1.48 ST_SymDifference

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/implementation-profile/symdifference`

