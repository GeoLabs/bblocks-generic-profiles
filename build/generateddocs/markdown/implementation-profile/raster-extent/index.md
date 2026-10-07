
# Implementation Profile: Raster extent (Schema)

`generic-profiles.implementation-profile.raster-extent` *v0.1*

Computes the bounding envelope of a raster coverage, as a vector polygon.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Implementation Profile: **Raster extent**.

> Computes the bounding envelope of a raster coverage, as a vector polygon.

## Source

- [OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard](https://www.ogc.org/standards/wcps/)
  -- the OGC standards-track evidence that this kind of coverage operation is a recognised,
  harmonised processing concept (this is what [its Concept](../../concept/raster-coverage-processing/)
  and [Generic Profile](../../generic-profile/raster-extent/) are grounded in too).
- [OTB ImageEnvelope -- Build a vector data containing the image envelope polygon](https://www.orfeo-toolbox.org/CookBook/Applications/app_ImageEnvelope.html)
  -- the concrete software binding the Geonovum testbed actually runs,
  [`OTB.ImageEnvelope`](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.ImageEnvelope):
  takes a raster (`in`) and returns a vector polygon (`out`, GML/KML/`object`/zip) representing its
  envelope, in a requestable output projection (`proj`), optionally densified along the edges
  (`sr`, sampling rate) -- the real evidence that this operation's output is a vector polygon,
  not a plain four-number bounding box (see [its Generic Profile](../../generic-profile/raster-extent/)
  for why that distinction matters).

## Data format

`raster`: a `schema` of `{type: string, contentEncoding: base64, contentMediaType: image/tiff}`
(GeoTIFF) -- the register's minimal default (Table 21, D: Declare), consistent with every other
raster Implementation Profile in this register (not grounded in `OTB.ImageEnvelope`'s own `in`
the same way `OTB.BandMath`'s `il` is -- its schema was not individually re-checked here, GeoTIFF
follows this tier's general raster-input convention).

`result`: a `schema` of `{type: string, contentMediaType: text/xml}` (GML) -- grounded in
`OTB.ImageEnvelope`'s own `out`, which declares `text/xml` (GML),
`application/vnd.google-earth.kml+xml` (KML), `object` and `application/zip`; GML is kept as this
tier's minimal baseline, consistent with every vector-typed output elsewhere in this register.
Not a `$ref` to `ogc.api.processes.v1.schemas.bbox` the way
[`raster-crop`](../raster-crop/)'s `areaOfInterest` is -- this output is a real polygon, not a
plain numeric extent.

Per [OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32), a
specific deployment may *Extend* (E, footnote d) this minimal default -- this tier intentionally
does not pre-empt that.

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.raster-extent`](../../generic-profile/raster-extent/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.raster.extent` in `bblocks-process-profiles` -- a real
process of the ZOO-Project Geonovum testbed
(<https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.ImageEnvelope>).

## Examples

### Raster extent
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-extent",
  "type": "ImplementationProfile",
  "prefLabel": "Raster extent",
  "definition": "Computes the bounding envelope of a raster coverage, as a vector polygon.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent",
  "keywords": [
    "raster",
    "coverage",
    "extent",
    "OTB",
    "ImageEnvelope"
  ],
  "inputs": {
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
          "title": "Process Concept: Raster Coverage Processing",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
        },
        {
          "title": "Generic Profile: Raster extent",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent"
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
          "title": "Generic Profile: Raster extent",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent"
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
      "title": "OTB ImageEnvelope -- Build a vector data containing the image envelope polygon",
      "link": "https://www.orfeo-toolbox.org/CookBook/Applications/app_ImageEnvelope.html"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/raster-extent/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-extent",
  "type": "ImplementationProfile",
  "prefLabel": "Raster extent",
  "definition": "Computes the bounding envelope of a raster coverage, as a vector polygon.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent",
  "keywords": [
    "raster",
    "coverage",
    "extent",
    "OTB",
    "ImageEnvelope"
  ],
  "inputs": {
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
          "title": "Process Concept: Raster Coverage Processing",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
        },
        {
          "title": "Generic Profile: Raster extent",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent"
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
          "title": "Generic Profile: Raster extent",
          "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent"
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
      "title": "OTB ImageEnvelope -- Build a vector data containing the image envelope polygon",
      "link": "https://www.orfeo-toolbox.org/CookBook/Applications/app_ImageEnvelope.html"
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

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-extent> a skos:Concept ;
    dcterms:source [ dcterms:references <https://www.ogc.org/standards/wcps/> ;
            dcterms:title "OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard" ],
        [ dcterms:references <https://www.orfeo-toolbox.org/CookBook/Applications/app_ImageEnvelope.html> ;
            dcterms:title "OTB ImageEnvelope -- Build a vector data containing the image envelope polygon" ] ;
    skos:definition "Computes the bounding envelope of a raster coverage, as a vector polygon." ;
    skos:inScheme gp:implementation-profile ;
    skos:prefLabel "Raster extent" ;
    gp:inputs [ ns2:raster [ proc:keywords "GeoTIFF",
                        "raster" ;
                    proc:metadata [ dcterms:title "Process Concept: Raster Coverage Processing" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ],
                        [ dcterms:title "Generic Profile: Raster extent" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ] ;
                    proc:schema [ a ns1:string ;
                            ns1:contentEncoding "base64" ;
                            ns1:contentMediaType "image/tiff" ;
                            ns1:description "GeoTIFF" ] ] ] ;
    gp:outputs [ ns3:result [ proc:keywords "GML",
                        "geometry" ;
                    proc:metadata [ dcterms:title "Generic Profile: Raster extent" ;
                            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent> ;
                            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ] ;
                    proc:schema [ a ns1:string ;
                            ns1:contentMediaType "text/xml" ;
                            ns1:description "GML" ] ] ] ;
    gp:refinesGenericProfile <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent> ;
    gp:status "submitted" ;
    proc:keywords "ImageEnvelope",
        "OTB",
        "coverage",
        "extent",
        "raster" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Implementation Profile "Raster extent" -- see generic-profiles.implementation-profile
  for the general shape every Implementation Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-extent
      x-jsonld-id: '@id'
    type:
      const: ImplementationProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Raster extent
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
    refinesGenericProfile:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/refinesGenericProfile
      x-jsonld-type: '@id'
    keywords:
      allOf:
      - contains:
          const: raster
      - contains:
          const: coverage
      - contains:
          const: extent
      x-jsonld-id: https://w3id.org/ogc/api/processes/keywords
    inputs:
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent
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

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/raster-extent/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/raster-extent/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/raster-extent/context.jsonld)

## Sources

* [OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard](https://www.ogc.org/standards/wcps/)
* [OTB ImageEnvelope -- Build a vector data containing the image envelope polygon](https://www.orfeo-toolbox.org/CookBook/Applications/app_ImageEnvelope.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/implementation-profile/raster-extent`

