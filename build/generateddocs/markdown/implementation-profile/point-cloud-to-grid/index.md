
# Implementation Profile: Point cloud to grid (Schema)

`generic-profiles.implementation-profile.point-cloud-to-grid` *v0.1*

Writes one value per grid cell from the points falling in it -- by default the z value of the first point -- as a single-band raster.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Implementation Profile: **Point cloud to grid**.

> Writes one value per grid cell from the points falling in it -- by default the z value of the first point -- as a single-band raster.

## Data

- input `points`: `point-cloud`, LAS (OGC 17-030r1); application/vnd.las is the IANA-registered media type
- input `cellSize`: `number`, no format to declare
- output `result`: `raster-single-band`, GeoTIFF

Narrowed data types: `result` (output): `raster-single-band`, narrower than the Generic Profile's `raster`.

The declared format is a minimal default; a real implementation may support others (Table 21,
footnote d). For rasters, the Geonovum testbed's SAGA also serves ESRI ASCII grids, ENVI and PNG. For point clouds, it labels LAS `application/x-ogc-lasf`, not the IANA-registered `application/vnd.las` declared here.

## Source

- [SAGA 7.3.0 -- Point Cloud to Grid](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/pointcloud_tools_4.html)
- [ZOO-Project Geonovum testbed -- SAGA.pointcloud_tools.4: Point Cloud to Grid](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.4)

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.point-cloud-rasterization`](../../generic-profile/point-cloud-rasterization/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.*` in `bblocks-process-profiles` -- a real process of
the ZOO-Project Geonovum testbed.

## Examples

### Point cloud to grid
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-grid",
  "type": "ImplementationProfile",
  "prefLabel": "Point cloud to grid",
  "definition": "Writes one value per grid cell from the points falling in it -- by default the z value of the first point -- as a single-band raster.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-rasterization",
  "keywords": [
    "point cloud",
    "raster",
    "rasterization",
    "Point Cloud to Grid",
    "pointcloud_tools"
  ],
  "metadata": [
    {
      "title": "Process Concept: Point Cloud Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/point-cloud-processing"
    },
    {
      "title": "Generic Profile: Point cloud rasterization",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-rasterization"
    }
  ],
  "inputs": {
    "points": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-grid/inputs/points",
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
          "title": "Generic Profile: Point cloud rasterization -- input `points`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-rasterization/inputs/points"
        }
      ]
    },
    "cellSize": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-grid/inputs/cellSize",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/number",
      "keywords": [
        "cell size"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Point cloud rasterization -- input `cellSize`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-rasterization/inputs/cellSize"
        }
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-grid/outputs/result",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster-single-band",
      "schema": {
        "type": "string",
        "contentEncoding": "base64",
        "contentMediaType": "image/tiff",
        "description": "GeoTIFF"
      },
      "keywords": [
        "raster",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Point cloud rasterization -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-rasterization/outputs/result"
        }
      ]
    }
  },
  "source": [
    {
      "title": "SAGA 7.3.0 -- Point Cloud to Grid",
      "link": "https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/pointcloud_tools_4.html"
    },
    {
      "title": "ZOO-Project Geonovum testbed -- SAGA.pointcloud_tools.4: Point Cloud to Grid",
      "link": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.4"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/point-cloud-to-grid/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-grid",
  "type": "ImplementationProfile",
  "prefLabel": "Point cloud to grid",
  "definition": "Writes one value per grid cell from the points falling in it -- by default the z value of the first point -- as a single-band raster.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-rasterization",
  "keywords": [
    "point cloud",
    "raster",
    "rasterization",
    "Point Cloud to Grid",
    "pointcloud_tools"
  ],
  "metadata": [
    {
      "title": "Process Concept: Point Cloud Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/point-cloud-processing"
    },
    {
      "title": "Generic Profile: Point cloud rasterization",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-rasterization"
    }
  ],
  "inputs": {
    "points": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-grid/inputs/points",
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
          "title": "Generic Profile: Point cloud rasterization -- input `points`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-rasterization/inputs/points"
        }
      ]
    },
    "cellSize": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-grid/inputs/cellSize",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/number",
      "keywords": [
        "cell size"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Point cloud rasterization -- input `cellSize`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-rasterization/inputs/cellSize"
        }
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-grid/outputs/result",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster-single-band",
      "schema": {
        "type": "string",
        "contentEncoding": "base64",
        "contentMediaType": "image/tiff",
        "description": "GeoTIFF"
      },
      "keywords": [
        "raster",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Point cloud rasterization -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-rasterization/outputs/result"
        }
      ]
    }
  },
  "source": [
    {
      "title": "SAGA 7.3.0 -- Point Cloud to Grid",
      "link": "https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/pointcloud_tools_4.html"
    },
    {
      "title": "ZOO-Project Geonovum testbed -- SAGA.pointcloud_tools.4: Point Cloud to Grid",
      "link": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.4"
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

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-grid> a skos:Concept ;
    dcterms:source [ dcterms:references <https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/pointcloud_tools_4.html> ;
            dcterms:title "SAGA 7.3.0 -- Point Cloud to Grid" ],
        [ dcterms:references <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.4> ;
            dcterms:title "ZOO-Project Geonovum testbed -- SAGA.pointcloud_tools.4: Point Cloud to Grid" ] ;
    skos:definition "Writes one value per grid cell from the points falling in it -- by default the z value of the first point -- as a single-band raster." ;
    skos:inScheme gp:implementation-profile ;
    skos:prefLabel "Point cloud to grid" ;
    gp:inputs [ ns1:cellSize <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-grid/inputs/cellSize> ;
            ns1:points <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-grid/inputs/points> ] ;
    gp:outputs [ ns3:result <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-grid/outputs/result> ] ;
    gp:refinesGenericProfile <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-rasterization> ;
    gp:status "submitted" ;
    proc:keywords "Point Cloud to Grid",
        "point cloud",
        "pointcloud_tools",
        "raster",
        "rasterization" ;
    proc:metadata [ dcterms:title "Generic Profile: Point cloud rasterization" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-rasterization> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ],
        [ dcterms:title "Process Concept: Point Cloud Processing" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/point-cloud-processing> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-grid/inputs/cellSize> dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/number> ;
    proc:keywords "cell size" ;
    proc:metadata [ dcterms:title "Generic Profile: Point cloud rasterization -- input `cellSize`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-rasterization/inputs/cellSize> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-grid/inputs/points> dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/point-cloud> ;
    proc:keywords "LAS",
        "point cloud" ;
    proc:metadata [ dcterms:title "Generic Profile: Point cloud rasterization -- input `points`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-rasterization/inputs/points> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] ;
    proc:schema [ a ns2:string ;
            ns2:contentEncoding "base64" ;
            ns2:contentMediaType "application/vnd.las" ;
            ns2:description "LAS (OGC 17-030r1); application/vnd.las is the IANA-registered media type" ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-grid/outputs/result> dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster-single-band> ;
    proc:keywords "GeoTIFF",
        "raster" ;
    proc:metadata [ dcterms:title "Generic Profile: Point cloud rasterization -- output `result`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-rasterization/outputs/result> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output> ] ;
    proc:schema [ a ns2:string ;
            ns2:contentEncoding "base64" ;
            ns2:contentMediaType "image/tiff" ;
            ns2:description "GeoTIFF" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Implementation Profile "Point cloud to grid" -- see generic-profiles.implementation-profile
  for the general shape every Implementation Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-grid
      x-jsonld-id: '@id'
    type:
      const: ImplementationProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Point cloud to grid
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
    refinesGenericProfile:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-rasterization
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/refinesGenericProfile
      x-jsonld-type: '@id'
    keywords:
      allOf:
      - contains:
          const: point cloud
      - contains:
          const: raster
      - contains:
          const: rasterization
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-rasterization
      x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
    inputs:
      type: object
      required:
      - points
      - cellSize
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-rasterization/inputs/points
              x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
        cellSize:
          properties:
            keywords:
              allOf:
              - contains:
                  const: cell size
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-rasterization/inputs/cellSize
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
                  const: raster
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-rasterization/outputs/result
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-grid/inputs/points
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type/point-cloud
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
        cellSize:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-grid/inputs/cellSize
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-grid/outputs/result
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster-single-band
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

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/point-cloud-to-grid/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/point-cloud-to-grid/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/point-cloud-to-grid/context.jsonld)

## Sources

* [SAGA 7.3.0 -- Point Cloud to Grid](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/pointcloud_tools_4.html)
* [ZOO-Project Geonovum testbed -- SAGA.pointcloud_tools.4: Point Cloud to Grid](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.4)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/implementation-profile/point-cloud-to-grid`

