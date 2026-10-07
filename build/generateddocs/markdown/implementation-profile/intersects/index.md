
# Implementation Profile: Intersects (Schema)

`generic-profiles.implementation-profile.intersects` *v0.1*

Returns TRUE if this geometric object spatially intersects anotherGeometry (i.e. they share at least one point). Equivalent to the negation of Disjoint.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Implementation Profile: **Intersects**.

> Returns TRUE if this geometric object spatially intersects anotherGeometry (i.e. they share at least one point). Equivalent to the negation of Disjoint.

## Source

Two standards define this operation at different levels -- the abstract semantics, and the
concrete SQL binding an Implementation Profile is specifically meant to add (OGC 14-065 WPS 2.0.2
§7.5.3, "down to the supported data exchange formats"):

- [OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture](https://www.ogc.org/standards/sfa/), §6.1.15 -- the
  operation's abstract definition (this is what [its Concept](../../concept/vector-geometry-processing/)
  and [Generic Profile](../../generic-profile/binary-spatial-predicate/) are grounded in too).
- ISO/IEC 13249-3:2016 *SQL multimedia and application packages -- Part 3: Spatial*, §5.1.24 ST_Intersects
  -- the same operation bound to SQL: the `ST_Geometry` type and the `ST_Intersects` function name,
  of which this Implementation Profile's `prefLabel` (`Intersects`) is the SFA name without the `ST_`
  prefix SQL/MM adds. SQL/MM is why this tier exists at all: it is, precisely, an implementation
  profile of Simple Feature Access for SQL -- the same abstract operation, bound to one concrete
  language and type system, still not any one vendor's specific deployment of it.

## Illustration

![ST_Intersects](assets/st_intersects.png)

Source: [PostGIS Workshop -- Spatial Relationships](https://postgis.net/workshops/postgis-intro/spatial_relationships.html), © Paul Ramsey, Mark Leslie, PostGIS contributors, licensed [CC BY-SA 3.0 US](http://creativecommons.org/licenses/by-sa/3.0/us/).

## Data formats

`geometry1`, `geometry2`: GML -- the register's minimal default (Table 21, D: Declare), grounded in the real ZOO-Project Geonovum testbed, whose SQL/MM processes expose geometries as `text/xml` (GML) only, never WKT or GeoJSON (checked across `Intersects`, `Buffer`, `Intersection`). `result` (Boolean) carries no data format.

Per [OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32), a specific deployment may *Extend* (E, footnote d) this minimal default with additional formats it happens to support -- this tier intentionally does not pre-empt that.

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.binary-spatial-predicate`](../../generic-profile/binary-spatial-predicate/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see [`ospd.process-profiles.sqlmm.intersects`](https://github.com/GeoLabs/bblocks-process-profiles/tree/master/_sources/sqlmm/intersects)
in `bblocks-process-profiles` -- a real process of the ZOO-Project Geonovum testbed
(<https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Intersects>), which matches this tier's own minimal default (GML), specialised to one concrete version and root element, GML 3.1.0 Polygon.

## Examples

### Intersects
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersects",
  "type": "ImplementationProfile",
  "prefLabel": "Intersects",
  "definition": "Returns TRUE if this geometric object spatially intersects anotherGeometry (i.e. they share at least one point). Equivalent to the negation of Disjoint.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate",
  "keywords": [
    "vector",
    "geometry",
    "spatial relation",
    "predicate",
    "Intersects",
    "ST_Intersects"
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
          "title": "Generic Profile: Binary spatial predicate",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate"
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
          "title": "Generic Profile: Binary spatial predicate",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate"
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
          "title": "Generic Profile: Binary spatial predicate",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate"
        }
      ]
    }
  },
  "source": [
    {
      "title": "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture, \u00a76.1.15",
      "link": "https://www.ogc.org/standards/sfa/"
    },
    {
      "title": "ISO/IEC 13249-3:2016 Information technology -- Database languages -- SQL multimedia and application packages -- Part 3: Spatial, \u00a75.1.24 ST_Intersects"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://raw.githubusercontent.com/GeoLabs/bblocks-generic-profiles/undefined/build/annotated/implementation-profile/intersects/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersects",
  "type": "ImplementationProfile",
  "prefLabel": "Intersects",
  "definition": "Returns TRUE if this geometric object spatially intersects anotherGeometry (i.e. they share at least one point). Equivalent to the negation of Disjoint.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate",
  "keywords": [
    "vector",
    "geometry",
    "spatial relation",
    "predicate",
    "Intersects",
    "ST_Intersects"
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
          "title": "Generic Profile: Binary spatial predicate",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate"
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
          "title": "Generic Profile: Binary spatial predicate",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate"
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
          "title": "Generic Profile: Binary spatial predicate",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate"
        }
      ]
    }
  },
  "source": [
    {
      "title": "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture, \u00a76.1.15",
      "link": "https://www.ogc.org/standards/sfa/"
    },
    {
      "title": "ISO/IEC 13249-3:2016 Information technology -- Database languages -- SQL multimedia and application packages -- Part 3: Spatial, \u00a75.1.24 ST_Intersects"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix gp: <https://geolabs.github.io/bblocks-generic-profiles/def/> .
@prefix ns1: <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/> .
@prefix ns2: <https://w3id.org/ogc/api/schema/> .
@prefix ns3: <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersects> a skos:Concept ;
    dcterms:source [ dcterms:references <https://www.ogc.org/standards/sfa/> ;
            dcterms:title "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture, §6.1.15" ],
        [ dcterms:title "ISO/IEC 13249-3:2016 Information technology -- Database languages -- SQL multimedia and application packages -- Part 3: Spatial, §5.1.24 ST_Intersects" ] ;
    skos:definition "Returns TRUE if this geometric object spatially intersects anotherGeometry (i.e. they share at least one point). Equivalent to the negation of Disjoint." ;
    skos:inScheme gp:implementation-profile ;
    skos:prefLabel "Intersects" ;
    gp:inputs [ ns3:geometry1 [ proc:keywords "GML",
                        "geometry" ;
                    proc:metadata [ dcterms:title "Generic Profile: Binary spatial predicate" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ],
                        [ dcterms:title "Process Concept: Vector Geometry Processing" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] ;
                    proc:schema [ a ns2:string ;
                            ns2:contentMediaType "text/xml" ;
                            ns2:description "GML" ] ] ;
            ns3:geometry2 [ proc:keywords "GML",
                        "geometry" ;
                    proc:metadata [ dcterms:title "Process Concept: Vector Geometry Processing" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ],
                        [ dcterms:title "Generic Profile: Binary spatial predicate" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ] ;
                    proc:schema [ a ns2:string ;
                            ns2:contentMediaType "text/xml" ;
                            ns2:description "GML" ] ] ] ;
    gp:outputs [ ns1:result [ proc:keywords "boolean" ;
                    proc:metadata [ dcterms:title "Generic Profile: Binary spatial predicate" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ] ] ] ;
    gp:refinesGenericProfile <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate> ;
    gp:status "submitted" ;
    proc:keywords "Intersects",
        "ST_Intersects",
        "geometry",
        "predicate",
        "spatial relation",
        "vector" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Implementation Profile "Intersects" -- see generic-profiles.implementation-profile
  for the general shape every Implementation Profile shares.
allOf:
- $ref: https://raw.githubusercontent.com/GeoLabs/bblocks-generic-profiles/undefined/build/annotated/implementation-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/intersects
      x-jsonld-id: '@id'
    type:
      const: ImplementationProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Intersects
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
    refinesGenericProfile:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/refinesGenericProfile
      x-jsonld-type: '@id'
    keywords:
      allOf:
      - contains:
          const: vector
      - contains:
          const: geometry
      - contains:
          const: spatial relation
      - contains:
          const: predicate
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate
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

* YAML version: [schema.yaml](https://raw.githubusercontent.com/GeoLabs/bblocks-generic-profiles/undefined/build/annotated/implementation-profile/intersects/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/GeoLabs/bblocks-generic-profiles/undefined/build/annotated/implementation-profile/intersects/schema.yaml)


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
[context.jsonld](https://raw.githubusercontent.com/GeoLabs/bblocks-generic-profiles/undefined/build/annotated/implementation-profile/intersects/context.jsonld)

## Sources

* [OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture, §6.1.15](https://www.ogc.org/standards/sfa/)
* ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, §5.1.24 ST_Intersects

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/implementation-profile/intersects`

