
# Implementation Profile: Terrain ruggedness index (Schema)

`generic-profiles.implementation-profile.terrain-ruggedness-index` *v0.1*

The terrain ruggedness index (TRI) of Riley et al. (1999): how much the elevation of each cell differs from that of its neighbourhood.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Implementation Profile: **Terrain ruggedness index**.

> The terrain ruggedness index (TRI) of Riley et al. (1999): how much the elevation of each cell differs from that of its neighbourhood.

## Data

- input `elevation`: `elevation-model`, GeoTIFF
- output `result`: `raster-single-band`, GeoTIFF

The declared format is a minimal default; a real implementation may support others (Table 21,
footnote d). For rasters, the Geonovum testbed's SAGA also serves ESRI ASCII grids, ENVI and PNG.

## Source

- [SAGA 7.3.0 -- Terrain Ruggedness Index (TRI)](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/ta_morphometry_16.html)
- [ZOO-Project Geonovum testbed -- SAGA.ta_morphometry.16: Terrain Ruggedness Index (TRI)](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.16)
- Riley, S.J., De Gloria, S.D., Elliot, R. (1999): A Terrain Ruggedness that Quantifies Topographic Heterogeneity. Intermountain Journal of Science, Vol.5, No.1-4, pp.23-27

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.terrain-derivative`](../../generic-profile/terrain-derivative/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.*` in `bblocks-process-profiles` -- a real process of
the ZOO-Project Geonovum testbed.

## Examples

### Terrain ruggedness index
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/terrain-ruggedness-index",
  "type": "ImplementationProfile",
  "prefLabel": "Terrain ruggedness index",
  "definition": "The terrain ruggedness index (TRI) of Riley et al. (1999): how much the elevation of each cell differs from that of its neighbourhood.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative",
  "keywords": [
    "terrain",
    "elevation",
    "raster",
    "derivative",
    "TRI",
    "ta_morphometry"
  ],
  "metadata": [
    {
      "title": "Process Concept: Terrain Analysis",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis"
    },
    {
      "title": "Generic Profile: Terrain derivative",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative"
    }
  ],
  "inputs": {
    "elevation": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/terrain-ruggedness-index/inputs/elevation",
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
          "title": "Generic Profile: Terrain derivative -- input `elevation`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative/inputs/elevation"
        }
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/terrain-ruggedness-index/outputs/result",
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
          "title": "Generic Profile: Terrain derivative -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative/outputs/result"
        }
      ]
    }
  },
  "source": [
    {
      "title": "SAGA 7.3.0 -- Terrain Ruggedness Index (TRI)",
      "link": "https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/ta_morphometry_16.html"
    },
    {
      "title": "ZOO-Project Geonovum testbed -- SAGA.ta_morphometry.16: Terrain Ruggedness Index (TRI)",
      "link": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.16"
    },
    {
      "title": "Riley, S.J., De Gloria, S.D., Elliot, R. (1999): A Terrain Ruggedness that Quantifies Topographic Heterogeneity. Intermountain Journal of Science, Vol.5, No.1-4, pp.23-27"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/terrain-ruggedness-index/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/terrain-ruggedness-index",
  "type": "ImplementationProfile",
  "prefLabel": "Terrain ruggedness index",
  "definition": "The terrain ruggedness index (TRI) of Riley et al. (1999): how much the elevation of each cell differs from that of its neighbourhood.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative",
  "keywords": [
    "terrain",
    "elevation",
    "raster",
    "derivative",
    "TRI",
    "ta_morphometry"
  ],
  "metadata": [
    {
      "title": "Process Concept: Terrain Analysis",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis"
    },
    {
      "title": "Generic Profile: Terrain derivative",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative"
    }
  ],
  "inputs": {
    "elevation": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/terrain-ruggedness-index/inputs/elevation",
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
          "title": "Generic Profile: Terrain derivative -- input `elevation`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative/inputs/elevation"
        }
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/terrain-ruggedness-index/outputs/result",
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
          "title": "Generic Profile: Terrain derivative -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative/outputs/result"
        }
      ]
    }
  },
  "source": [
    {
      "title": "SAGA 7.3.0 -- Terrain Ruggedness Index (TRI)",
      "link": "https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/ta_morphometry_16.html"
    },
    {
      "title": "ZOO-Project Geonovum testbed -- SAGA.ta_morphometry.16: Terrain Ruggedness Index (TRI)",
      "link": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.16"
    },
    {
      "title": "Riley, S.J., De Gloria, S.D., Elliot, R. (1999): A Terrain Ruggedness that Quantifies Topographic Heterogeneity. Intermountain Journal of Science, Vol.5, No.1-4, pp.23-27"
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

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/terrain-ruggedness-index> a skos:Concept ;
    dcterms:source [ dcterms:references <https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/ta_morphometry_16.html> ;
            dcterms:title "SAGA 7.3.0 -- Terrain Ruggedness Index (TRI)" ],
        [ dcterms:references <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.16> ;
            dcterms:title "ZOO-Project Geonovum testbed -- SAGA.ta_morphometry.16: Terrain Ruggedness Index (TRI)" ],
        [ dcterms:title "Riley, S.J., De Gloria, S.D., Elliot, R. (1999): A Terrain Ruggedness that Quantifies Topographic Heterogeneity. Intermountain Journal of Science, Vol.5, No.1-4, pp.23-27" ] ;
    skos:definition "The terrain ruggedness index (TRI) of Riley et al. (1999): how much the elevation of each cell differs from that of its neighbourhood." ;
    skos:inScheme gp:implementation-profile ;
    skos:prefLabel "Terrain ruggedness index" ;
    gp:inputs [ ns2:elevation <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/terrain-ruggedness-index/inputs/elevation> ] ;
    gp:outputs [ ns3:result <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/terrain-ruggedness-index/outputs/result> ] ;
    gp:refinesGenericProfile <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative> ;
    gp:status "submitted" ;
    proc:keywords "TRI",
        "derivative",
        "elevation",
        "raster",
        "ta_morphometry",
        "terrain" ;
    proc:metadata [ dcterms:title "Process Concept: Terrain Analysis" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ],
        [ dcterms:title "Generic Profile: Terrain derivative" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/terrain-ruggedness-index/inputs/elevation> dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/elevation-model> ;
    proc:keywords "GeoTIFF",
        "elevation" ;
    proc:metadata [ dcterms:title "Generic Profile: Terrain derivative -- input `elevation`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative/inputs/elevation> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] ;
    proc:schema [ a ns1:string ;
            ns1:contentEncoding "base64" ;
            ns1:contentMediaType "image/tiff" ;
            ns1:description "GeoTIFF" ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/terrain-ruggedness-index/outputs/result> dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster-single-band> ;
    proc:keywords "GeoTIFF",
        "raster" ;
    proc:metadata [ dcterms:title "Generic Profile: Terrain derivative -- output `result`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative/outputs/result> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output> ] ;
    proc:schema [ a ns1:string ;
            ns1:contentEncoding "base64" ;
            ns1:contentMediaType "image/tiff" ;
            ns1:description "GeoTIFF" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Implementation Profile "Terrain ruggedness index" -- see generic-profiles.implementation-profile
  for the general shape every Implementation Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/terrain-ruggedness-index
      x-jsonld-id: '@id'
    type:
      const: ImplementationProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Terrain ruggedness index
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
    refinesGenericProfile:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative
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
          const: derivative
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative
      x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
    inputs:
      type: object
      required:
      - elevation
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative/inputs/elevation
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/terrain-derivative/outputs/result
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/terrain-ruggedness-index/inputs/elevation
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type/elevation-model
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/terrain-ruggedness-index/outputs/result
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

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/terrain-ruggedness-index/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/terrain-ruggedness-index/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/terrain-ruggedness-index/context.jsonld)

## Sources

* [SAGA 7.3.0 -- Terrain Ruggedness Index (TRI)](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/ta_morphometry_16.html)
* [ZOO-Project Geonovum testbed -- SAGA.ta_morphometry.16: Terrain Ruggedness Index (TRI)](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.ta_morphometry.16)
* Riley, S.J., De Gloria, S.D., Elliot, R. (1999): A Terrain Ruggedness that Quantifies Topographic Heterogeneity. Intermountain Journal of Science, Vol.5, No.1-4, pp.23-27

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/implementation-profile/terrain-ruggedness-index`

