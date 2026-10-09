
# Implementation Profile: Analytical hillshading (Schema)

`generic-profiles.implementation-profile.analytical-hillshading` *v0.1*

For each cell, the angle at which light coming from the position of the light source hits the terrain surface (SAGA's standard method).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Implementation Profile: **Analytical hillshading**.

> For each cell, the angle at which light coming from the position of the light source hits the terrain surface (SAGA's standard method).

## Data

- input `elevation`: `elevation-model`, GeoTIFF
- input `azimuth`: `number`, no format to declare
- input `altitude`: `number`, no format to declare
- output `result`: `raster-single-band`, GeoTIFF

The declared format is a minimal default; a real implementation may support others (Table 21,
footnote d). For rasters, the Geonovum testbed's SAGA also serves ESRI ASCII grids, ENVI and PNG.

## Source

- [SAGA 7.3.0 -- Analytical Hillshading](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/ta_lighting_0.html)
- [ZOO-Project Geonovum testbed -- SAGA.ta_lighting.0: Analytical Hillshading](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_lighting.0)

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.analytical-hillshading`](../../generic-profile/analytical-hillshading/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.*` in `bblocks-process-profiles` -- a real process of
the ZOO-Project Geonovum testbed.

## Examples

### Analytical hillshading
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/analytical-hillshading",
  "type": "ImplementationProfile",
  "prefLabel": "Analytical hillshading",
  "definition": "For each cell, the angle at which light coming from the position of the light source hits the terrain surface (SAGA's standard method).",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading",
  "keywords": [
    "terrain",
    "elevation",
    "raster",
    "illumination",
    "hillshade",
    "Hillshade",
    "ta_lighting"
  ],
  "metadata": [
    {
      "title": "Process Concept: Terrain Analysis",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis"
    },
    {
      "title": "Generic Profile: Analytical hillshading",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading"
    }
  ],
  "inputs": {
    "elevation": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/analytical-hillshading/inputs/elevation",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/elevation-model",
      "schema": {
        "type": "string",
        "contentEncoding": "base64",
        "contentMediaType": "image/tiff",
        "description": "GeoTIFF"
      },
      "keywords": [
        "elevation",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Analytical hillshading -- input `elevation`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading/inputs/elevation"
        }
      ]
    },
    "azimuth": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/analytical-hillshading/inputs/azimuth",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/number",
      "keywords": [
        "azimuth"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Analytical hillshading -- input `azimuth`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading/inputs/azimuth"
        }
      ]
    },
    "altitude": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/analytical-hillshading/inputs/altitude",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/number",
      "keywords": [
        "altitude"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Analytical hillshading -- input `altitude`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading/inputs/altitude"
        }
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/analytical-hillshading/outputs/result",
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
          "title": "Generic Profile: Analytical hillshading -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading/outputs/result"
        }
      ]
    }
  },
  "source": [
    {
      "title": "SAGA 7.3.0 -- Analytical Hillshading",
      "link": "https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/ta_lighting_0.html"
    },
    {
      "title": "ZOO-Project Geonovum testbed -- SAGA.ta_lighting.0: Analytical Hillshading",
      "link": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_lighting.0"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/analytical-hillshading/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/analytical-hillshading",
  "type": "ImplementationProfile",
  "prefLabel": "Analytical hillshading",
  "definition": "For each cell, the angle at which light coming from the position of the light source hits the terrain surface (SAGA's standard method).",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading",
  "keywords": [
    "terrain",
    "elevation",
    "raster",
    "illumination",
    "hillshade",
    "Hillshade",
    "ta_lighting"
  ],
  "metadata": [
    {
      "title": "Process Concept: Terrain Analysis",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis"
    },
    {
      "title": "Generic Profile: Analytical hillshading",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading"
    }
  ],
  "inputs": {
    "elevation": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/analytical-hillshading/inputs/elevation",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/elevation-model",
      "schema": {
        "type": "string",
        "contentEncoding": "base64",
        "contentMediaType": "image/tiff",
        "description": "GeoTIFF"
      },
      "keywords": [
        "elevation",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Analytical hillshading -- input `elevation`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading/inputs/elevation"
        }
      ]
    },
    "azimuth": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/analytical-hillshading/inputs/azimuth",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/number",
      "keywords": [
        "azimuth"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Analytical hillshading -- input `azimuth`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading/inputs/azimuth"
        }
      ]
    },
    "altitude": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/analytical-hillshading/inputs/altitude",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/number",
      "keywords": [
        "altitude"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Analytical hillshading -- input `altitude`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading/inputs/altitude"
        }
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/analytical-hillshading/outputs/result",
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
          "title": "Generic Profile: Analytical hillshading -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading/outputs/result"
        }
      ]
    }
  },
  "source": [
    {
      "title": "SAGA 7.3.0 -- Analytical Hillshading",
      "link": "https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/ta_lighting_0.html"
    },
    {
      "title": "ZOO-Project Geonovum testbed -- SAGA.ta_lighting.0: Analytical Hillshading",
      "link": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_lighting.0"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix gp: <https://geolabs.github.io/bblocks-generic-profiles/def/> .
@prefix ns1: <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/> .
@prefix ns2: <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/> .
@prefix ns3: <https://w3id.org/ogc/api/schema/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/analytical-hillshading> a skos:Concept ;
    dcterms:source [ dcterms:references <https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/ta_lighting_0.html> ;
            dcterms:title "SAGA 7.3.0 -- Analytical Hillshading" ],
        [ dcterms:references <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_lighting.0> ;
            dcterms:title "ZOO-Project Geonovum testbed -- SAGA.ta_lighting.0: Analytical Hillshading" ] ;
    skos:definition "For each cell, the angle at which light coming from the position of the light source hits the terrain surface (SAGA's standard method)." ;
    skos:inScheme gp:implementation-profile ;
    skos:prefLabel "Analytical hillshading" ;
    gp:inputs [ ns2:altitude <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/analytical-hillshading/inputs/altitude> ;
            ns2:azimuth <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/analytical-hillshading/inputs/azimuth> ;
            ns2:elevation <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/analytical-hillshading/inputs/elevation> ] ;
    gp:outputs [ ns1:result <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/analytical-hillshading/outputs/result> ] ;
    gp:refinesGenericProfile <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading> ;
    gp:status "submitted" ;
    proc:keywords "Hillshade",
        "elevation",
        "hillshade",
        "illumination",
        "raster",
        "ta_lighting",
        "terrain" ;
    proc:metadata [ dcterms:title "Generic Profile: Analytical hillshading" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ],
        [ dcterms:title "Process Concept: Terrain Analysis" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/analytical-hillshading/inputs/altitude> dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/number> ;
    proc:keywords "altitude" ;
    proc:metadata [ dcterms:title "Generic Profile: Analytical hillshading -- input `altitude`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading/inputs/altitude> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/analytical-hillshading/inputs/azimuth> dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/number> ;
    proc:keywords "azimuth" ;
    proc:metadata [ dcterms:title "Generic Profile: Analytical hillshading -- input `azimuth`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading/inputs/azimuth> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/analytical-hillshading/inputs/elevation> dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/elevation-model> ;
    proc:keywords "GeoTIFF",
        "elevation" ;
    proc:metadata [ dcterms:title "Generic Profile: Analytical hillshading -- input `elevation`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading/inputs/elevation> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] ;
    proc:schema [ a ns3:string ;
            ns3:contentEncoding "base64" ;
            ns3:contentMediaType "image/tiff" ;
            ns3:description "GeoTIFF" ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/analytical-hillshading/outputs/result> dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster-single-band> ;
    proc:keywords "GeoTIFF",
        "raster" ;
    proc:metadata [ dcterms:title "Generic Profile: Analytical hillshading -- output `result`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading/outputs/result> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output> ] ;
    proc:schema [ a ns3:string ;
            ns3:contentEncoding "base64" ;
            ns3:contentMediaType "image/tiff" ;
            ns3:description "GeoTIFF" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Implementation Profile "Analytical hillshading" -- see generic-profiles.implementation-profile
  for the general shape every Implementation Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/analytical-hillshading
      x-jsonld-id: '@id'
    type:
      const: ImplementationProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Analytical hillshading
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
    refinesGenericProfile:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/refinesGenericProfile
      x-jsonld-type: '@id'
    keywords:
      allOf:
      - contains:
          const: terrain
      - contains:
          const: elevation
      - contains:
          const: raster
      - contains:
          const: illumination
      - contains:
          const: hillshade
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis
      - contains:
          type: object
          required:
          - role
          - href
          properties:
            role:
              const: http://www.opengis.net/spec/wps/2.0/def/process-profile/generic
            href:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading
      x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
    inputs:
      type: object
      required:
      - elevation
      - azimuth
      - altitude
      properties:
        elevation:
          properties:
            keywords:
              allOf:
              - contains:
                  const: elevation
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading/inputs/elevation
              x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
        azimuth:
          properties:
            keywords:
              allOf:
              - contains:
                  const: azimuth
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading/inputs/azimuth
              x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
        altitude:
          properties:
            keywords:
              allOf:
              - contains:
                  const: altitude
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading/inputs/altitude
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading/outputs/result
              x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/outputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/
- type: object
  properties:
    inputs:
      properties:
        elevation:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/analytical-hillshading/inputs/elevation
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type/elevation-model
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
        azimuth:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/analytical-hillshading/inputs/azimuth
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type/number
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
        altitude:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/analytical-hillshading/inputs/altitude
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/analytical-hillshading/outputs/result
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

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/analytical-hillshading/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/analytical-hillshading/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/analytical-hillshading/context.jsonld)

## Sources

* [SAGA 7.3.0 -- Analytical Hillshading](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/ta_lighting_0.html)
* [ZOO-Project Geonovum testbed -- SAGA.ta_lighting.0: Analytical Hillshading](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_lighting.0)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/implementation-profile/analytical-hillshading`

