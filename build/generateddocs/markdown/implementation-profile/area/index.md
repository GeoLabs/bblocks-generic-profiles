
# Implementation Profile: Area (Schema)

`generic-profiles.implementation-profile.area` *v0.1*

The area of this Surface, as measured in the spatial reference system of this Surface.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Implementation Profile: **Area**.

> The area of this Surface, as measured in the spatial reference system of this Surface.

## Source

- [OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1, §2.1.9.1 Area()](https://www.ogc.org/standards/sfs/)
- ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_Area
- [ZOO-Project Geonovum testbed -- GetArea: Computes the area of a geometry.](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/GetArea)

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.geometry-measure`](../../generic-profile/geometry-measure/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.vector.*` in `bblocks-process-profiles` -- a real
process of the ZOO-Project Geonovum testbed.

## Examples

### Area
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/area",
  "type": "ImplementationProfile",
  "prefLabel": "Area",
  "definition": "The area of this Surface, as measured in the spatial reference system of this Surface.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-measure",
  "keywords": [
    "vector",
    "geometry",
    "measure",
    "Area",
    "ST_Area"
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
          "title": "Generic Profile: Geometry measure",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-measure"
        }
      ]
    }
  },
  "outputs": {
    "result": {
      "schema": {
        "type": "number",
        "description": "a plain number"
      },
      "keywords": [
        "number"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Geometry measure",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-measure"
        }
      ]
    }
  },
  "source": [
    {
      "title": "OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1, \u00a72.1.9.1 Area()",
      "link": "https://www.ogc.org/standards/sfs/"
    },
    {
      "title": "ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_Area"
    },
    {
      "title": "ZOO-Project Geonovum testbed -- GetArea: Computes the area of a geometry.",
      "link": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/GetArea"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/area/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/area",
  "type": "ImplementationProfile",
  "prefLabel": "Area",
  "definition": "The area of this Surface, as measured in the spatial reference system of this Surface.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-measure",
  "keywords": [
    "vector",
    "geometry",
    "measure",
    "Area",
    "ST_Area"
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
          "title": "Generic Profile: Geometry measure",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-measure"
        }
      ]
    }
  },
  "outputs": {
    "result": {
      "schema": {
        "type": "number",
        "description": "a plain number"
      },
      "keywords": [
        "number"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Geometry measure",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-measure"
        }
      ]
    }
  },
  "source": [
    {
      "title": "OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1, \u00a72.1.9.1 Area()",
      "link": "https://www.ogc.org/standards/sfs/"
    },
    {
      "title": "ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_Area"
    },
    {
      "title": "ZOO-Project Geonovum testbed -- GetArea: Computes the area of a geometry.",
      "link": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/GetArea"
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

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/area> a skos:Concept ;
    dcterms:source [ dcterms:title "ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_Area" ],
        [ dcterms:references <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/GetArea> ;
            dcterms:title "ZOO-Project Geonovum testbed -- GetArea: Computes the area of a geometry." ],
        [ dcterms:references <https://www.ogc.org/standards/sfs/> ;
            dcterms:title "OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1, §2.1.9.1 Area()" ] ;
    skos:definition "The area of this Surface, as measured in the spatial reference system of this Surface." ;
    skos:inScheme gp:implementation-profile ;
    skos:prefLabel "Area" ;
    gp:inputs [ ns3:geometry [ proc:keywords "GML",
                        "geometry" ;
                    proc:metadata [ dcterms:title "Process Concept: Vector Geometry Processing" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ],
                        [ dcterms:title "Generic Profile: Geometry measure" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-measure> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ] ;
                    proc:schema [ a ns1:string ;
                            ns1:contentMediaType "text/xml" ;
                            ns1:description "GML" ] ] ] ;
    gp:outputs [ ns2:result [ proc:keywords "number" ;
                    proc:metadata [ dcterms:title "Generic Profile: Geometry measure" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-measure> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ] ;
                    proc:schema [ a ns1:number ;
                            ns1:description "a plain number" ] ] ] ;
    gp:refinesGenericProfile <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-measure> ;
    gp:status "submitted" ;
    proc:keywords "Area",
        "ST_Area",
        "geometry",
        "measure",
        "vector" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Implementation Profile "Area" -- see generic-profiles.implementation-profile
  for the general shape every Implementation Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/area
      x-jsonld-id: '@id'
    type:
      const: ImplementationProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Area
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
    refinesGenericProfile:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-measure
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/refinesGenericProfile
      x-jsonld-type: '@id'
    keywords:
      allOf:
      - contains:
          const: vector
      - contains:
          const: geometry
      - contains:
          const: measure
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/geometry-measure
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
                  const: number
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

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/area/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/area/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/area/context.jsonld)

## Sources

* [OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1, §2.1.9.1 Area()](https://www.ogc.org/standards/sfs/)
* ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_Area
* [ZOO-Project Geonovum testbed -- GetArea: Computes the area of a geometry.](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/GetArea)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/implementation-profile/area`

