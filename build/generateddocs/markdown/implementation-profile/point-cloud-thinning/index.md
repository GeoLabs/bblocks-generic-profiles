
# Implementation Profile: Point cloud thinning (simple) (Schema)

`generic-profiles.implementation-profile.point-cloud-thinning` *v0.1*

Reduces the number of points to the given percentage by sequential point removal, which suits points stored in chronological order best.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Implementation Profile: **Point cloud thinning (simple)**.

> Reduces the number of points to the given percentage by sequential point removal, which suits points stored in chronological order best.

## Data

- input `points`: `point-cloud`, LAS (OGC 17-030r1); application/vnd.las is the IANA-registered media type
- input `percentage`: `number`, no format to declare
- output `result`: `point-cloud`, LAS (OGC 17-030r1); application/vnd.las is the IANA-registered media type

The declared format is a minimal default; a real implementation may support others (Table 21,
footnote d). For point clouds, it labels LAS `application/x-ogc-lasf`, not the IANA-registered `application/vnd.las` declared here.

## Source

- [SAGA 7.3.0 -- Point Cloud Thinning (Simple)](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/pointcloud_tools_9.html)
- [ZOO-Project Geonovum testbed -- SAGA.pointcloud_tools.9: Point Cloud Thinning (Simple)](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.9)

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.point-cloud-thinning`](../../generic-profile/point-cloud-thinning/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.*` in `bblocks-process-profiles` -- a real process of
the ZOO-Project Geonovum testbed.

## Examples

### Point cloud thinning (simple)
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning",
  "type": "ImplementationProfile",
  "prefLabel": "Point cloud thinning (simple)",
  "definition": "Reduces the number of points to the given percentage by sequential point removal, which suits points stored in chronological order best.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning",
  "keywords": [
    "point cloud",
    "thinning",
    "Point Cloud Thinning",
    "pointcloud_tools"
  ],
  "metadata": [
    {
      "title": "Process Concept: Point Cloud Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/point-cloud-processing"
    },
    {
      "title": "Generic Profile: Point cloud thinning",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning"
    }
  ],
  "inputs": {
    "points": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/inputs/points",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/point-cloud",
      "schema": {
        "type": "string",
        "contentEncoding": "base64",
        "contentMediaType": "application/vnd.las",
        "description": "LAS (OGC 17-030r1); application/vnd.las is the IANA-registered media type"
      },
      "keywords": [
        "point cloud",
        "LAS"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Point cloud thinning -- input `points`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/inputs/points"
        }
      ]
    },
    "percentage": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/inputs/percentage",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/number",
      "keywords": [
        "percentage"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Point cloud thinning -- input `percentage`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/inputs/percentage"
        }
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/outputs/result",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/point-cloud",
      "schema": {
        "type": "string",
        "contentEncoding": "base64",
        "contentMediaType": "application/vnd.las",
        "description": "LAS (OGC 17-030r1); application/vnd.las is the IANA-registered media type"
      },
      "keywords": [
        "point cloud",
        "LAS"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Point cloud thinning -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/outputs/result"
        }
      ]
    }
  },
  "source": [
    {
      "title": "SAGA 7.3.0 -- Point Cloud Thinning (Simple)",
      "link": "https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/pointcloud_tools_9.html"
    },
    {
      "title": "ZOO-Project Geonovum testbed -- SAGA.pointcloud_tools.9: Point Cloud Thinning (Simple)",
      "link": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.9"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/point-cloud-thinning/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning",
  "type": "ImplementationProfile",
  "prefLabel": "Point cloud thinning (simple)",
  "definition": "Reduces the number of points to the given percentage by sequential point removal, which suits points stored in chronological order best.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning",
  "keywords": [
    "point cloud",
    "thinning",
    "Point Cloud Thinning",
    "pointcloud_tools"
  ],
  "metadata": [
    {
      "title": "Process Concept: Point Cloud Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/point-cloud-processing"
    },
    {
      "title": "Generic Profile: Point cloud thinning",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning"
    }
  ],
  "inputs": {
    "points": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/inputs/points",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/point-cloud",
      "schema": {
        "type": "string",
        "contentEncoding": "base64",
        "contentMediaType": "application/vnd.las",
        "description": "LAS (OGC 17-030r1); application/vnd.las is the IANA-registered media type"
      },
      "keywords": [
        "point cloud",
        "LAS"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Point cloud thinning -- input `points`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/inputs/points"
        }
      ]
    },
    "percentage": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/inputs/percentage",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/number",
      "keywords": [
        "percentage"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Point cloud thinning -- input `percentage`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/inputs/percentage"
        }
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/outputs/result",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/point-cloud",
      "schema": {
        "type": "string",
        "contentEncoding": "base64",
        "contentMediaType": "application/vnd.las",
        "description": "LAS (OGC 17-030r1); application/vnd.las is the IANA-registered media type"
      },
      "keywords": [
        "point cloud",
        "LAS"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Point cloud thinning -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/outputs/result"
        }
      ]
    }
  },
  "source": [
    {
      "title": "SAGA 7.3.0 -- Point Cloud Thinning (Simple)",
      "link": "https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/pointcloud_tools_9.html"
    },
    {
      "title": "ZOO-Project Geonovum testbed -- SAGA.pointcloud_tools.9: Point Cloud Thinning (Simple)",
      "link": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.9"
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

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning> a skos:Concept ;
    dcterms:source [ dcterms:references <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.9> ;
            dcterms:title "ZOO-Project Geonovum testbed -- SAGA.pointcloud_tools.9: Point Cloud Thinning (Simple)" ],
        [ dcterms:references <https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/pointcloud_tools_9.html> ;
            dcterms:title "SAGA 7.3.0 -- Point Cloud Thinning (Simple)" ] ;
    skos:definition "Reduces the number of points to the given percentage by sequential point removal, which suits points stored in chronological order best." ;
    skos:inScheme gp:implementation-profile ;
    skos:prefLabel "Point cloud thinning (simple)" ;
    gp:inputs [ ns2:percentage <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/inputs/percentage> ;
            ns2:points <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/inputs/points> ] ;
    gp:outputs [ ns3:result <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/outputs/result> ] ;
    gp:refinesGenericProfile <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning> ;
    gp:status "submitted" ;
    proc:keywords "Point Cloud Thinning",
        "point cloud",
        "pointcloud_tools",
        "thinning" ;
    proc:metadata [ dcterms:title "Generic Profile: Point cloud thinning" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ],
        [ dcterms:title "Process Concept: Point Cloud Processing" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/point-cloud-processing> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/inputs/percentage> dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/number> ;
    proc:keywords "percentage" ;
    proc:metadata [ dcterms:title "Generic Profile: Point cloud thinning -- input `percentage`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/inputs/percentage> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/inputs/points> dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/point-cloud> ;
    proc:keywords "LAS",
        "point cloud" ;
    proc:metadata [ dcterms:title "Generic Profile: Point cloud thinning -- input `points`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/inputs/points> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] ;
    proc:schema [ a ns1:string ;
            ns1:contentEncoding "base64" ;
            ns1:contentMediaType "application/vnd.las" ;
            ns1:description "LAS (OGC 17-030r1); application/vnd.las is the IANA-registered media type" ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/outputs/result> dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/point-cloud> ;
    proc:keywords "LAS",
        "point cloud" ;
    proc:metadata [ dcterms:title "Generic Profile: Point cloud thinning -- output `result`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/outputs/result> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output> ] ;
    proc:schema [ a ns1:string ;
            ns1:contentEncoding "base64" ;
            ns1:contentMediaType "application/vnd.las" ;
            ns1:description "LAS (OGC 17-030r1); application/vnd.las is the IANA-registered media type" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Implementation Profile "Point cloud thinning (simple)" -- see generic-profiles.implementation-profile
  for the general shape every Implementation Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning
      x-jsonld-id: '@id'
    type:
      const: ImplementationProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Point cloud thinning (simple)
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
    refinesGenericProfile:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/refinesGenericProfile
      x-jsonld-type: '@id'
    keywords:
      allOf:
      - contains:
          const: point cloud
      - contains:
          const: thinning
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/concept/point-cloud-processing
      - contains:
          type: object
          required:
          - role
          - href
          properties:
            role:
              const: http://www.opengis.net/spec/wps/2.0/def/process-profile/generic
            href:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning
      x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
    inputs:
      type: object
      required:
      - points
      - percentage
      properties:
        points:
          properties:
            keywords:
              allOf:
              - contains:
                  const: point cloud
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/inputs/points
              x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
        percentage:
          properties:
            keywords:
              allOf:
              - contains:
                  const: percentage
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/inputs/percentage
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
                  const: point cloud
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-thinning/outputs/result
              x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/outputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/
- type: object
  properties:
    inputs:
      properties:
        points:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/inputs/points
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/inputs/percentage
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type/number
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-thinning/outputs/result
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type/point-cloud
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

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/point-cloud-thinning/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/point-cloud-thinning/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/point-cloud-thinning/context.jsonld)

## Sources

* [SAGA 7.3.0 -- Point Cloud Thinning (Simple)](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/pointcloud_tools_9.html)
* [ZOO-Project Geonovum testbed -- SAGA.pointcloud_tools.9: Point Cloud Thinning (Simple)](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.9)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/implementation-profile/point-cloud-thinning`

