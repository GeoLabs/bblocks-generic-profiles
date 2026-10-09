
# Implementation Profile: Radiometric index (Schema)

`generic-profiles.implementation-profile.radiometric-index` *v0.1*

Computes one or more named radiometric indices (e.g. NDVI, NDWI, SAVI) from the relevant spectral channels of the input raster(s).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Implementation Profile: **Radiometric index**.

> Computes one or more named radiometric indices (e.g. NDVI, NDWI, SAVI) from the relevant spectral channels of the input raster(s).

## Source

Two standards define this operation at different levels -- the abstract semantics, and the
concrete tool binding an Implementation Profile is specifically meant to add (OGC 14-065 WPS
2.0.2 §7.5.3, "down to the supported data exchange formats"):

- [OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard](https://www.ogc.org/standards/wcps/)
  -- the OGC standards-track evidence that this kind of coverage operation is a recognised,
  harmonised processing concept (this is what [its Concept](../../concept/raster-coverage-processing/)
  and [Generic Profile](../../generic-profile/radiometric-index/) are grounded in too). Unlike
  SQL/MM for the vector Implementation Profiles, WCPS is not the language this operation is
  actually bound to below -- GDAL/OTB, not WCPS, is what the Geonovum testbed runs.
- [OTB RadiometricIndices -- Computes radiometric indices from the relevant channels of the input image](https://www.orfeo-toolbox.org/CookBook/Applications/app_RadiometricIndices.html) -- the concrete software binding: a
  widely deployed, de facto standard implementation (not itself an ISO/OGC standard, unlike
  SQL/MM's formal status for the vector operations) that the Geonovum testbed's own
  [`OTB.RadiometricIndices`](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.RadiometricIndices)
  process wraps directly.

## Data formats

`rasters`, `raster` (output): GeoTIFF -- grounded the same way as `raster-band-math`: OTB's own
`in`/`out` declare exactly `image/tiff`, `image/jpeg`, `image/png`; GeoTIFF is the
georeferencing-capable member kept as the default.

## Multiplicity

`rasters`: restricted (Table 21, R, footnote c) to exactly one -- unlike `OTB.BandMath`/
`OTB.BandMathX`'s `il` (an image list), `OTB.RadiometricIndices`' own `in` input is a *single*
pre-stacked multi-band image (the red/nir/green/mir channels are selected from within it via
`channels.red`/`channels.nir`/...); the Generic Profile's abstract "one-or-many" is narrowed all
the way down to one here.

Per [OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32), a specific deployment may *Extend* (E, footnote d) this minimal default with additional formats it happens to support -- this tier intentionally does not pre-empt that.

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.radiometric-index`](../../generic-profile/radiometric-index/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.*` in `bblocks-process-profiles` -- real processes of
the ZOO-Project Geonovum testbed
(<https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.RadiometricIndices>).

## Examples

### Radiometric index
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index",
  "type": "ImplementationProfile",
  "prefLabel": "Radiometric index",
  "definition": "Computes one or more named radiometric indices (e.g. NDVI, NDWI, SAVI) from the relevant spectral channels of the input raster(s).",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index",
  "keywords": [
    "raster",
    "coverage",
    "radiometric index",
    "OTB",
    "RadiometricIndices"
  ],
  "metadata": [
    {
      "title": "Process Concept: Raster Coverage Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
    },
    {
      "title": "Generic Profile: Radiometric index",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index"
    }
  ],
  "inputs": {
    "rasters": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index/inputs/rasters",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster",
      "schema": {
        "type": "string",
        "contentEncoding": "base64",
        "contentMediaType": "image/tiff",
        "description": "GeoTIFF"
      },
      "maxOccurs": 1,
      "keywords": [
        "raster",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Radiometric index -- input `rasters`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index/inputs/rasters"
        }
      ]
    },
    "index": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index/inputs/index",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/string",
      "keywords": [
        "radiometric index"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Radiometric index -- input `index`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index/inputs/index"
        }
      ]
    }
  },
  "outputs": {
    "raster": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index/outputs/raster",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster",
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
          "title": "Generic Profile: Radiometric index -- output `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index/outputs/raster"
        }
      ]
    }
  },
  "source": [
    {
      "title": "OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard",
      "link": "https://www.ogc.org/standards/wcps/"
    },
    {
      "title": "OTB RadiometricIndices -- Computes radiometric indices from the relevant channels of the input image",
      "link": "https://www.orfeo-toolbox.org/CookBook/Applications/app_RadiometricIndices.html"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/radiometric-index/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index",
  "type": "ImplementationProfile",
  "prefLabel": "Radiometric index",
  "definition": "Computes one or more named radiometric indices (e.g. NDVI, NDWI, SAVI) from the relevant spectral channels of the input raster(s).",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index",
  "keywords": [
    "raster",
    "coverage",
    "radiometric index",
    "OTB",
    "RadiometricIndices"
  ],
  "metadata": [
    {
      "title": "Process Concept: Raster Coverage Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
    },
    {
      "title": "Generic Profile: Radiometric index",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index"
    }
  ],
  "inputs": {
    "rasters": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index/inputs/rasters",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster",
      "schema": {
        "type": "string",
        "contentEncoding": "base64",
        "contentMediaType": "image/tiff",
        "description": "GeoTIFF"
      },
      "maxOccurs": 1,
      "keywords": [
        "raster",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Radiometric index -- input `rasters`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index/inputs/rasters"
        }
      ]
    },
    "index": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index/inputs/index",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/string",
      "keywords": [
        "radiometric index"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Radiometric index -- input `index`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index/inputs/index"
        }
      ]
    }
  },
  "outputs": {
    "raster": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index/outputs/raster",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster",
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
          "title": "Generic Profile: Radiometric index -- output `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index/outputs/raster"
        }
      ]
    }
  },
  "source": [
    {
      "title": "OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard",
      "link": "https://www.ogc.org/standards/wcps/"
    },
    {
      "title": "OTB RadiometricIndices -- Computes radiometric indices from the relevant channels of the input image",
      "link": "https://www.orfeo-toolbox.org/CookBook/Applications/app_RadiometricIndices.html"
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
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index> a skos:Concept ;
    dcterms:source [ dcterms:references <https://www.ogc.org/standards/wcps/> ;
            dcterms:title "OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard" ],
        [ dcterms:references <https://www.orfeo-toolbox.org/CookBook/Applications/app_RadiometricIndices.html> ;
            dcterms:title "OTB RadiometricIndices -- Computes radiometric indices from the relevant channels of the input image" ] ;
    skos:definition "Computes one or more named radiometric indices (e.g. NDVI, NDWI, SAVI) from the relevant spectral channels of the input raster(s)." ;
    skos:inScheme gp:implementation-profile ;
    skos:prefLabel "Radiometric index" ;
    gp:inputs [ ns1:index <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index/inputs/index> ;
            ns1:rasters <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index/inputs/rasters> ] ;
    gp:outputs [ ns3:raster <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index/outputs/raster> ] ;
    gp:refinesGenericProfile <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index> ;
    gp:status "submitted" ;
    proc:keywords "OTB",
        "RadiometricIndices",
        "coverage",
        "radiometric index",
        "raster" ;
    proc:metadata [ dcterms:title "Process Concept: Raster Coverage Processing" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ],
        [ dcterms:title "Generic Profile: Radiometric index" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index/inputs/index> dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/string> ;
    proc:keywords "radiometric index" ;
    proc:metadata [ dcterms:title "Generic Profile: Radiometric index -- input `index`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index/inputs/index> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index/inputs/rasters> dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster> ;
    proc:keywords "GeoTIFF",
        "raster" ;
    proc:maxOccurs 1 ;
    proc:metadata [ dcterms:title "Generic Profile: Radiometric index -- input `rasters`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index/inputs/rasters> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] ;
    proc:schema [ a ns2:string ;
            ns2:contentEncoding "base64" ;
            ns2:contentMediaType "image/tiff" ;
            ns2:description "GeoTIFF" ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index/outputs/raster> dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster> ;
    proc:keywords "GeoTIFF",
        "raster" ;
    proc:metadata [ dcterms:title "Generic Profile: Radiometric index -- output `raster`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index/outputs/raster> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output> ] ;
    proc:schema [ a ns2:string ;
            ns2:contentEncoding "base64" ;
            ns2:contentMediaType "image/tiff" ;
            ns2:description "GeoTIFF" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Implementation Profile "Radiometric index" -- see generic-profiles.implementation-profile
  for the general shape every Implementation Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index
      x-jsonld-id: '@id'
    type:
      const: ImplementationProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Radiometric index
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
    refinesGenericProfile:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/refinesGenericProfile
      x-jsonld-type: '@id'
    keywords:
      allOf:
      - contains:
          const: raster
      - contains:
          const: coverage
      - contains:
          const: radiometric index
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing
      - contains:
          type: object
          required:
          - role
          - href
          properties:
            role:
              const: http://www.opengis.net/spec/wps/2.0/def/process-profile/generic
            href:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index
      x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
    inputs:
      type: object
      required:
      - rasters
      - index
      properties:
        rasters:
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input
                    href:
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index/inputs/rasters
              x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
        index:
          properties:
            keywords:
              allOf:
              - contains:
                  const: radiometric index
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index/inputs/index
              x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/
    outputs:
      type: object
      required:
      - raster
      properties:
        raster:
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index/outputs/raster
              x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/outputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/
- type: object
  properties:
    inputs:
      properties:
        rasters:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index/inputs/rasters
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
        index:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index/inputs/index
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type/string
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/
    outputs:
      properties:
        raster:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index/outputs/raster
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster
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

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/radiometric-index/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/radiometric-index/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/radiometric-index/context.jsonld)

## Sources

* [OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard](https://www.ogc.org/standards/wcps/)
* [OTB RadiometricIndices -- Computes radiometric indices from the relevant channels of the input image](https://www.orfeo-toolbox.org/CookBook/Applications/app_RadiometricIndices.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/implementation-profile/radiometric-index`

