
# Implementation Profile: Equals (Schema)

`generic-profiles.implementation-profile.equals` *v0.1*

Returns TRUE if this geometric object is spatially equal to anotherGeometry (same point set), independent of vertex order or representation.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Implementation Profile: **Equals**.

> Returns TRUE if this geometric object is spatially equal to anotherGeometry (same point set), independent of vertex order or representation.

## Source

Two standards define this operation at different levels -- the abstract semantics, and the
concrete SQL binding an Implementation Profile is specifically meant to add (OGC 14-065 WPS 2.0.2
§7.5.3, "down to the supported data exchange formats"):

- [OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture](https://www.ogc.org/standards/sfa/), §6.1.14 -- the
  operation's abstract definition (this is what [its Concept](../../concept/vector-geometry-processing/)
  and [Generic Profile](../../generic-profile/binary-spatial-predicate/) are grounded in too).
- ISO/IEC 13249-3:2016 *SQL multimedia and application packages -- Part 3: Spatial*, §5.1.16 ST_Equals
  -- the same operation bound to SQL: the `ST_Geometry` type and the `ST_Equals` function name,
  of which this Implementation Profile's `prefLabel` (`Equals`) is the SFA name without the `ST_`
  prefix SQL/MM adds. SQL/MM is why this tier exists at all: it is, precisely, an implementation
  profile of Simple Feature Access for SQL -- the same abstract operation, bound to one concrete
  language and type system, still not any one vendor's specific deployment of it.

## Illustration

![ST_Equals](assets/st_equals.png)

Source: [PostGIS Workshop -- Spatial Relationships](https://postgis.net/workshops/postgis-intro/spatial_relationships.html), © Paul Ramsey, Mark Leslie, PostGIS contributors, licensed [CC BY-SA 3.0 US](http://creativecommons.org/licenses/by-sa/3.0/us/).

## Data formats

`geometry1`, `geometry2`: GML -- the register's minimal default (Table 21, D: Declare), grounded in the real ZOO-Project Geonovum testbed, whose SQL/MM processes expose geometries as `text/xml` (GML) only, never WKT or GeoJSON (checked across `Intersects`, `Buffer`, `Intersection`). `result` (Boolean) carries no data format.

Per [OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32), a specific deployment may *Extend* (E, footnote d) this minimal default with additional formats it happens to support -- this tier intentionally does not pre-empt that.

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.binary-spatial-predicate`](../../generic-profile/binary-spatial-predicate/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see [`ospd.process-profiles.sqlmm.equals`](https://github.com/GeoLabs/bblocks-process-profiles/tree/master/_sources/sqlmm/equals)
in `bblocks-process-profiles` -- a real process of the ZOO-Project Geonovum testbed
(<https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Equals>), which matches this tier's own minimal default (GML), specialised to one concrete version and root element, GML 3.1.0 Polygon.

## Examples

### Equals
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/equals",
  "type": "ImplementationProfile",
  "prefLabel": "Equals",
  "definition": "Returns TRUE if this geometric object is spatially equal to anotherGeometry (same point set), independent of vertex order or representation.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate",
  "keywords": [
    "vector",
    "geometry",
    "spatial relation",
    "predicate",
    "Equals",
    "ST_Equals"
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
  ],
  "inputs": {
    "geometry1": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/equals/inputs/geometry1",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/geometry",
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
          "title": "Generic Profile: Binary spatial predicate -- input `geometry1`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/inputs/geometry1"
        }
      ]
    },
    "geometry2": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/equals/inputs/geometry2",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/geometry",
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
          "title": "Generic Profile: Binary spatial predicate -- input `geometry2`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/inputs/geometry2"
        }
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/equals/outputs/result",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/boolean",
      "keywords": [
        "boolean"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Binary spatial predicate -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/outputs/result"
        }
      ]
    }
  },
  "source": [
    {
      "title": "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture, \u00a76.1.14",
      "link": "https://www.ogc.org/standards/sfa/"
    },
    {
      "title": "ISO/IEC 13249-3:2016 Information technology -- Database languages -- SQL multimedia and application packages -- Part 3: Spatial, \u00a75.1.16 ST_Equals"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/equals/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/equals",
  "type": "ImplementationProfile",
  "prefLabel": "Equals",
  "definition": "Returns TRUE if this geometric object is spatially equal to anotherGeometry (same point set), independent of vertex order or representation.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate",
  "keywords": [
    "vector",
    "geometry",
    "spatial relation",
    "predicate",
    "Equals",
    "ST_Equals"
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
  ],
  "inputs": {
    "geometry1": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/equals/inputs/geometry1",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/geometry",
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
          "title": "Generic Profile: Binary spatial predicate -- input `geometry1`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/inputs/geometry1"
        }
      ]
    },
    "geometry2": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/equals/inputs/geometry2",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/geometry",
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
          "title": "Generic Profile: Binary spatial predicate -- input `geometry2`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/inputs/geometry2"
        }
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/equals/outputs/result",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/boolean",
      "keywords": [
        "boolean"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Binary spatial predicate -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/outputs/result"
        }
      ]
    }
  },
  "source": [
    {
      "title": "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture, \u00a76.1.14",
      "link": "https://www.ogc.org/standards/sfa/"
    },
    {
      "title": "ISO/IEC 13249-3:2016 Information technology -- Database languages -- SQL multimedia and application packages -- Part 3: Spatial, \u00a75.1.16 ST_Equals"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix gp: <https://geolabs.github.io/bblocks-generic-profiles/def/> .
@prefix ns1: <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/> .
@prefix ns2: <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/> .
@prefix ns3: <https://w3id.org/ogc/api/schema/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/equals> a skos:Concept ;
    dcterms:source [ dcterms:title "ISO/IEC 13249-3:2016 Information technology -- Database languages -- SQL multimedia and application packages -- Part 3: Spatial, §5.1.16 ST_Equals" ],
        [ dcterms:references <https://www.ogc.org/standards/sfa/> ;
            dcterms:title "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture, §6.1.14" ] ;
    skos:definition "Returns TRUE if this geometric object is spatially equal to anotherGeometry (same point set), independent of vertex order or representation." ;
    skos:inScheme gp:implementation-profile ;
    skos:prefLabel "Equals" ;
    gp:inputs [ ns1:geometry1 <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/equals/inputs/geometry1> ;
            ns1:geometry2 <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/equals/inputs/geometry2> ] ;
    gp:outputs [ ns2:result <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/equals/outputs/result> ] ;
    gp:refinesGenericProfile <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate> ;
    gp:status "submitted" ;
    proc:keywords "Equals",
        "ST_Equals",
        "geometry",
        "predicate",
        "spatial relation",
        "vector" ;
    proc:metadata [ dcterms:title "Process Concept: Vector Geometry Processing" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ],
        [ dcterms:title "Generic Profile: Binary spatial predicate" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/equals/inputs/geometry1> dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/geometry> ;
    proc:keywords "GML",
        "geometry" ;
    proc:metadata [ dcterms:title "Generic Profile: Binary spatial predicate -- input `geometry1`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/inputs/geometry1> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] ;
    proc:schema [ a ns3:string ;
            ns3:contentMediaType "text/xml" ;
            ns3:description "GML" ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/equals/inputs/geometry2> dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/geometry> ;
    proc:keywords "GML",
        "geometry" ;
    proc:metadata [ dcterms:title "Generic Profile: Binary spatial predicate -- input `geometry2`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/inputs/geometry2> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] ;
    proc:schema [ a ns3:string ;
            ns3:contentMediaType "text/xml" ;
            ns3:description "GML" ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/equals/outputs/result> dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/boolean> ;
    proc:keywords "boolean" ;
    proc:metadata [ dcterms:title "Generic Profile: Binary spatial predicate -- output `result`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/outputs/result> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output> ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Implementation Profile "Equals" -- see generic-profiles.implementation-profile
  for the general shape every Implementation Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/equals
      x-jsonld-id: '@id'
    type:
      const: ImplementationProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Equals
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input
                    href:
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/inputs/geometry1
              x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input
                    href:
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/inputs/geometry2
              x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/outputs/result
              x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/outputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/
- type: object
  properties:
    inputs:
      properties:
        geometry1:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/equals/inputs/geometry1
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type/geometry
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
        geometry2:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/equals/inputs/geometry2
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type/geometry
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/
    outputs:
      properties:
        result:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/equals/outputs/result
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type/boolean
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
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

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/equals/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/equals/schema.yaml)


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
        "dataType": {
          "@id": "dct:type",
          "@type": "@id"
        },
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
        "dataType": {
          "@id": "dct:type",
          "@type": "@id"
        },
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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/equals/context.jsonld)

## Sources

* [OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture, §6.1.14](https://www.ogc.org/standards/sfa/)
* ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, §5.1.16 ST_Equals

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/implementation-profile/equals`

