
# Implementation Profile: Geometry extent (Schema)

`generic-profiles.implementation-profile.geometry-extent` *v0.1*

Computes the minimum bounding rectangle of a set of input geometries, as a geometry.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Implementation Profile: **Geometry extent**.

> Computes the minimum bounding rectangle of a set of input geometries, as a geometry.

## Source

Three sources, at different levels -- the abstract semantics, the SQL binding, and the concrete
tool this testbed actually runs:

- [OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture](https://www.ogc.org/standards/sfa/)
  -- `Geometry::Envelope()`, the abstract operation (this is what
  [its Concept](../../concept/vector-geometry-processing/) and
  [Generic Profile](../../generic-profile/geometry-extent/) are grounded in too).
- ISO/IEC 13249-3:2016 *SQL multimedia and application packages -- Part 3: Spatial*, `ST_Envelope`
  -- the same operation bound to SQL, the same way SQL/MM grounds every other vector Implementation
  Profile in this register.
- [SAGA GIS -- Get Shapes Extents](https://saga-gis.sourceforge.io/saga_tool_doc/9.4.0/shapes_tools_19.html)
  -- the concrete software binding the Geonovum testbed actually runs,
  [`SAGA.shapes_tools.19`](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.shapes_tools.19)
  ("Get Shapes Extents"): takes a shapes layer (`SHAPES`) and returns its extent (`EXTENTS`), both
  as `text/xml`/KML/`object` -- a vector geometry, not four plain numbers, the same shape this
  Implementation Profile declares. Unlike the vector predicates/operations above (SQL/MM-bound),
  this one is SAGA-bound: this testbed has no SQL/MM `ST_Envelope` process of its own, only this
  SAGA tool.

## Data formats

`geometry`, `result`: GML -- the register's minimal default (Table 21, D: Declare), consistent
with every other vector Implementation Profile in this register. `SAGA.shapes_tools.19`'s own
`SHAPES`/`EXTENTS` additionally expose KML and a generic `object` encoding; GML is kept as this
tier's minimal baseline (Per [OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32),
a specific deployment may *Extend* this default, footnote d).

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.geometry-extent`](../../generic-profile/geometry-extent/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.vector.extent` in `bblocks-process-profiles` -- a real
process of the ZOO-Project Geonovum testbed
(<https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.shapes_tools.19>).

## Examples

### Geometry extent
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/geometry-extent",
  "type": "ImplementationProfile",
  "prefLabel": "Geometry extent",
  "definition": "Computes the minimum bounding rectangle of a set of input geometries, as a geometry.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation",
  "keywords": [
    "vector",
    "geometry",
    "derived geometry",
    "Envelope",
    "SAGA GIS"
  ],
  "inputs": {
    "geometry": {
      "schema": {
        "type": "string",
        "contentMediaType": "text/xml",
        "description": "GML (minimal default; SAGA.shapes_tools.19 also accepts KML and a generic object encoding)"
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
          "title": "Generic Profile: Unary geometry operation",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation"
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
          "title": "Generic Profile: Unary geometry operation",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation"
        }
      ]
    }
  },
  "source": [
    {
      "title": "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture (Envelope)",
      "link": "https://www.ogc.org/standards/sfa/"
    },
    {
      "title": "ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_Envelope"
    },
    {
      "title": "SAGA GIS -- Get Shapes Extents (shapes_tools)",
      "link": "https://saga-gis.sourceforge.io/saga_tool_doc/9.4.0/shapes_tools_19.html"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/geometry-extent/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/geometry-extent",
  "type": "ImplementationProfile",
  "prefLabel": "Geometry extent",
  "definition": "Computes the minimum bounding rectangle of a set of input geometries, as a geometry.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation",
  "keywords": [
    "vector",
    "geometry",
    "derived geometry",
    "Envelope",
    "SAGA GIS"
  ],
  "inputs": {
    "geometry": {
      "schema": {
        "type": "string",
        "contentMediaType": "text/xml",
        "description": "GML (minimal default; SAGA.shapes_tools.19 also accepts KML and a generic object encoding)"
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
          "title": "Generic Profile: Unary geometry operation",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation"
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
          "title": "Generic Profile: Unary geometry operation",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation"
        }
      ]
    }
  },
  "source": [
    {
      "title": "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture (Envelope)",
      "link": "https://www.ogc.org/standards/sfa/"
    },
    {
      "title": "ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_Envelope"
    },
    {
      "title": "SAGA GIS -- Get Shapes Extents (shapes_tools)",
      "link": "https://saga-gis.sourceforge.io/saga_tool_doc/9.4.0/shapes_tools_19.html"
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

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/geometry-extent> a skos:Concept ;
    dcterms:source [ dcterms:references <https://saga-gis.sourceforge.io/saga_tool_doc/9.4.0/shapes_tools_19.html> ;
            dcterms:title "SAGA GIS -- Get Shapes Extents (shapes_tools)" ],
        [ dcterms:references <https://www.ogc.org/standards/sfa/> ;
            dcterms:title "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture (Envelope)" ],
        [ dcterms:title "ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_Envelope" ] ;
    skos:definition "Computes the minimum bounding rectangle of a set of input geometries, as a geometry." ;
    skos:inScheme gp:implementation-profile ;
    skos:prefLabel "Geometry extent" ;
    gp:inputs [ ns3:geometry [ proc:keywords "GML",
                        "geometry" ;
                    proc:metadata [ dcterms:title "Generic Profile: Unary geometry operation" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ],
                        [ dcterms:title "Process Concept: Vector Geometry Processing" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] ;
                    proc:schema [ a ns2:string ;
                            ns2:contentMediaType "text/xml" ;
                            ns2:description "GML (minimal default; SAGA.shapes_tools.19 also accepts KML and a generic object encoding)" ] ] ] ;
    gp:outputs [ ns1:result [ proc:keywords "GML",
                        "geometry" ;
                    proc:metadata [ dcterms:title "Generic Profile: Unary geometry operation" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ] ;
                    proc:schema [ a ns2:string ;
                            ns2:contentMediaType "text/xml" ;
                            ns2:description "GML" ] ] ] ;
    gp:refinesGenericProfile <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation> ;
    gp:status "submitted" ;
    proc:keywords "Envelope",
        "SAGA GIS",
        "derived geometry",
        "geometry",
        "vector" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Implementation Profile "Geometry extent" -- see generic-profiles.implementation-profile
  for the general shape every Implementation Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/geometry-extent
      x-jsonld-id: '@id'
    type:
      const: ImplementationProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Geometry extent
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation
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

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/geometry-extent/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/geometry-extent/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/geometry-extent/context.jsonld)

## Sources

* [OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture (Envelope)](https://www.ogc.org/standards/sfa/)
* ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_Envelope
* [SAGA GIS -- Get Shapes Extents (shapes_tools)](https://saga-gis.sourceforge.io/saga_tool_doc/9.4.0/shapes_tools_19.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/implementation-profile/geometry-extent`

