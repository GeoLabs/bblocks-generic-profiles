
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
  "inputs": {
    "rasters": {
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
          "title": "Process Concept: Raster Coverage Processing",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
        },
        {
          "title": "Generic Profile: Radiometric index",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index"
        }
      ]
    },
    "index": {
      "keywords": [
        "radiometric index"
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
      ]
    }
  },
  "outputs": {
    "raster": {
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
          "title": "Generic Profile: Radiometric index",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index"
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
  "inputs": {
    "rasters": {
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
          "title": "Process Concept: Raster Coverage Processing",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
        },
        {
          "title": "Generic Profile: Radiometric index",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index"
        }
      ]
    },
    "index": {
      "keywords": [
        "radiometric index"
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
      ]
    }
  },
  "outputs": {
    "raster": {
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
          "title": "Generic Profile: Radiometric index",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index"
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
@prefix ns1: <https://w3id.org/ogc/api/schema/> .
@prefix ns2: <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/> .
@prefix ns3: <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/radiometric-index> a skos:Concept ;
    dcterms:source [ dcterms:references <https://www.orfeo-toolbox.org/CookBook/Applications/app_RadiometricIndices.html> ;
            dcterms:title "OTB RadiometricIndices -- Computes radiometric indices from the relevant channels of the input image" ],
        [ dcterms:references <https://www.ogc.org/standards/wcps/> ;
            dcterms:title "OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard" ] ;
    skos:definition "Computes one or more named radiometric indices (e.g. NDVI, NDWI, SAVI) from the relevant spectral channels of the input raster(s)." ;
    skos:inScheme gp:implementation-profile ;
    skos:prefLabel "Radiometric index" ;
    gp:inputs [ ns2:index [ proc:keywords "radiometric index" ;
                    proc:metadata [ dcterms:title "Generic Profile: Radiometric index" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ],
                        [ dcterms:title "Process Concept: Raster Coverage Processing" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] ] ;
            ns2:rasters [ proc:keywords "GeoTIFF",
                        "raster" ;
                    proc:maxOccurs 1 ;
                    proc:metadata [ dcterms:title "Generic Profile: Radiometric index" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ],
                        [ dcterms:title "Process Concept: Raster Coverage Processing" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] ;
                    proc:schema [ a ns1:string ;
                            ns1:contentEncoding "base64" ;
                            ns1:contentMediaType "image/tiff" ;
                            ns1:description "GeoTIFF" ] ] ] ;
    gp:outputs [ ns3:raster [ proc:keywords "GeoTIFF",
                        "raster" ;
                    proc:metadata [ dcterms:title "Generic Profile: Radiometric index" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ] ;
                    proc:schema [ a ns1:string ;
                            ns1:contentEncoding "base64" ;
                            ns1:contentMediaType "image/tiff" ;
                            ns1:description "GeoTIFF" ] ] ] ;
    gp:refinesGenericProfile <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/radiometric-index> ;
    gp:status "submitted" ;
    proc:keywords "OTB",
        "RadiometricIndices",
        "coverage",
        "radiometric index",
        "raster" .


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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/radiometric-index/context.jsonld)

## Sources

* [OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard](https://www.ogc.org/standards/wcps/)
* [OTB RadiometricIndices -- Computes radiometric indices from the relevant channels of the input image](https://www.orfeo-toolbox.org/CookBook/Applications/app_RadiometricIndices.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/implementation-profile/radiometric-index`

