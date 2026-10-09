
# Implementation Profile: Raster crop (Schema)

`generic-profiles.implementation-profile.raster-crop` *v0.1*

Extracts the pixels of a raster coverage that fall within a region of interest. `areaOfInterest`'s `schema` $refs `ogc.api.processes.v1.schemas.bbox` directly (OGC API - Processes Part 1 Core's own bbox type), not a bespoke format string.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Implementation Profile: **Raster crop**.

> Extracts the pixels of a raster coverage that fall within a region of interest.

## Source

Two standards define this operation at different levels -- the abstract semantics, and the
concrete tool binding an Implementation Profile is specifically meant to add (OGC 14-065 WPS
2.0.2 §7.5.3, "down to the supported data exchange formats"):

- [OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard](https://www.ogc.org/standards/wcps/)
  -- the OGC standards-track evidence that this kind of coverage operation is a recognised,
  harmonised processing concept (this is what [its Concept](../../concept/raster-coverage-processing/)
  and [Generic Profile](../../generic-profile/raster-crop/) are grounded in too). Unlike
  SQL/MM for the vector Implementation Profiles, WCPS is not the language this operation is
  actually bound to below -- GDAL/OTB, not WCPS, is what the Geonovum testbed runs.
- [OTB ExtractROI -- Extracts a region of interest defined by the user](https://www.orfeo-toolbox.org/CookBook/Applications/app_ExtractROI.html) -- the concrete software binding: a
  widely deployed, de facto standard implementation (not itself an ISO/OGC standard, unlike
  SQL/MM's formal status for the vector operations) that the Geonovum testbed's own
  [`OTB.ExtractROI`](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.ExtractROI)
  process wraps directly.
- [OGC 17-069r4 OGC API - Features - Part 1: Core](https://docs.ogc.org/is/17-069r4/17-069r4.html),
  §7.15.3 -- defines the `bbox` parameter (an array of 4 or 6 numbers) that
  `ogc.api.processes.v1.schemas.bbox` (below) itself cites as its own source.

## Data format

`raster` (input and output): a `schema` of `{type: string, contentEncoding: base64,
contentMediaType: image/tiff}` (GeoTIFF) -- grounded in `OTB.ExtractROI`'s own processDescription
(`in`/`out` both declare `image/tiff`, `image/jpeg`, `image/png`; GeoTIFF kept as the
georeferencing-capable default).

`areaOfInterest`: a `schema` that `$ref`s
[`ogc.api.processes.v1.schemas.bbox`](https://geolabs.github.io/bblocks-ogcapi-processes/)'s own
published schema directly (`{bbox: [4 or 6 numbers], crs: CRS84|CRS84h}`) -- OGC API - Processes
- Part 1: Core's own bbox type, not a bespoke format string, and grounded directly in
`OTB.ExtractROI`'s own "extent" mode (`mode.extent.ulx`/`uly`/`lrx`/`lry`, four plain numbers).
This Implementation Profile's Generic Profile originally typed `areaOfInterest` as `Geometry`,
which did not match -- see [`raster-crop`](../../generic-profile/raster-crop/)'s own "Why
`areaOfInterest` is `BoundingBox`, not `Geometry`" for that fix, now superseded in turn by
reusing `ogc.api.processes.v1.schemas.bbox` directly rather than inventing a `BoundingBox`
abstract type and a `"BBOX"` format string (see the repository README, "OGC API - Processes
alignment"). `eoap.cct.bbox` (bblocks-eoap-cct) is a *different* type, for CWL inputs/outputs
crossing into OGC API - Processes - Part 2: Deploy, Replace, Undeploy, not used here.
`OTB.ExtractROI`'s other three modes (`standard`, `radius`, `fit`) each use a different parameter
shape again (pixel offset/size, a circle, a reference image/vector) -- none of them a bbox or an
encoded geometry either, and not modelled here.

Per [OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32), a specific deployment may *Extend* (E, footnote d) this minimal default with additional formats it happens to support -- this tier intentionally does not pre-empt that.

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.raster-crop`](../../generic-profile/raster-crop/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.*` in `bblocks-process-profiles` -- real processes of
the ZOO-Project Geonovum testbed
(<https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.ExtractROI>).

## Examples

### Raster crop
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-crop",
  "type": "ImplementationProfile",
  "prefLabel": "Raster crop",
  "definition": "Extracts the pixels of a raster coverage that fall within a region of interest.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop",
  "keywords": [
    "raster",
    "coverage",
    "crop",
    "OTB",
    "ExtractROI"
  ],
  "metadata": [
    {
      "title": "Process Concept: Raster Coverage Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
    },
    {
      "title": "Generic Profile: Raster crop",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop"
    }
  ],
  "inputs": {
    "raster": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-crop/inputs/raster",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster",
      "schema": {
        "type": "string",
        "contentEncoding": "base64",
        "contentMediaType": "image/tiff"
      },
      "keywords": [
        "raster",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster crop -- input `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/inputs/raster"
        }
      ]
    },
    "areaOfInterest": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-crop/inputs/areaOfInterest",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/bounding-box",
      "schema": {
        "$ref": "https://geolabs.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/v1/schemas/bbox/schema.json"
      },
      "keywords": [
        "bounding box",
        "bbox"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster crop -- input `areaOfInterest`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/inputs/areaOfInterest"
        }
      ]
    }
  },
  "outputs": {
    "raster": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-crop/outputs/raster",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster",
      "schema": {
        "type": "string",
        "contentEncoding": "base64",
        "contentMediaType": "image/tiff"
      },
      "keywords": [
        "raster",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster crop -- output `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/outputs/raster"
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
      "title": "OTB ExtractROI -- Extracts a region of interest defined by the user",
      "link": "https://www.orfeo-toolbox.org/CookBook/Applications/app_ExtractROI.html"
    },
    {
      "title": "ogc.api.processes.v1.schemas.bbox -- bbox schema (OGC API - Processes - Part 1: Core)",
      "link": "https://geolabs.github.io/bblocks-ogcapi-processes/"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/raster-crop/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-crop",
  "type": "ImplementationProfile",
  "prefLabel": "Raster crop",
  "definition": "Extracts the pixels of a raster coverage that fall within a region of interest.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop",
  "keywords": [
    "raster",
    "coverage",
    "crop",
    "OTB",
    "ExtractROI"
  ],
  "metadata": [
    {
      "title": "Process Concept: Raster Coverage Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
    },
    {
      "title": "Generic Profile: Raster crop",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop"
    }
  ],
  "inputs": {
    "raster": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-crop/inputs/raster",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster",
      "schema": {
        "type": "string",
        "contentEncoding": "base64",
        "contentMediaType": "image/tiff"
      },
      "keywords": [
        "raster",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster crop -- input `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/inputs/raster"
        }
      ]
    },
    "areaOfInterest": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-crop/inputs/areaOfInterest",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/bounding-box",
      "schema": {
        "$ref": "https://geolabs.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/v1/schemas/bbox/schema.json"
      },
      "keywords": [
        "bounding box",
        "bbox"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster crop -- input `areaOfInterest`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/inputs/areaOfInterest"
        }
      ]
    }
  },
  "outputs": {
    "raster": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-crop/outputs/raster",
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster",
      "schema": {
        "type": "string",
        "contentEncoding": "base64",
        "contentMediaType": "image/tiff"
      },
      "keywords": [
        "raster",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster crop -- output `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/outputs/raster"
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
      "title": "OTB ExtractROI -- Extracts a region of interest defined by the user",
      "link": "https://www.orfeo-toolbox.org/CookBook/Applications/app_ExtractROI.html"
    },
    {
      "title": "ogc.api.processes.v1.schemas.bbox -- bbox schema (OGC API - Processes - Part 1: Core)",
      "link": "https://geolabs.github.io/bblocks-ogcapi-processes/"
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
@prefix ns3: <https://w3id.org/ogc/api/schema/$> .
@prefix ns4: <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-crop> a skos:Concept ;
    dcterms:source [ dcterms:references <https://geolabs.github.io/bblocks-ogcapi-processes/> ;
            dcterms:title "ogc.api.processes.v1.schemas.bbox -- bbox schema (OGC API - Processes - Part 1: Core)" ],
        [ dcterms:references <https://www.ogc.org/standards/wcps/> ;
            dcterms:title "OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard" ],
        [ dcterms:references <https://www.orfeo-toolbox.org/CookBook/Applications/app_ExtractROI.html> ;
            dcterms:title "OTB ExtractROI -- Extracts a region of interest defined by the user" ] ;
    skos:definition "Extracts the pixels of a raster coverage that fall within a region of interest." ;
    skos:inScheme gp:implementation-profile ;
    skos:prefLabel "Raster crop" ;
    gp:inputs [ ns2:areaOfInterest <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-crop/inputs/areaOfInterest> ;
            ns2:raster <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-crop/inputs/raster> ] ;
    gp:outputs [ ns4:raster <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-crop/outputs/raster> ] ;
    gp:refinesGenericProfile <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop> ;
    gp:status "submitted" ;
    proc:keywords "ExtractROI",
        "OTB",
        "coverage",
        "crop",
        "raster" ;
    proc:metadata [ dcterms:title "Process Concept: Raster Coverage Processing" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ],
        [ dcterms:title "Generic Profile: Raster crop" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-crop/inputs/areaOfInterest> dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/bounding-box> ;
    proc:keywords "bbox",
        "bounding box" ;
    proc:metadata [ dcterms:title "Generic Profile: Raster crop -- input `areaOfInterest`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/inputs/areaOfInterest> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] ;
    proc:schema [ ns3:ref "https://geolabs.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/v1/schemas/bbox/schema.json" ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-crop/inputs/raster> dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster> ;
    proc:keywords "GeoTIFF",
        "raster" ;
    proc:metadata [ dcterms:title "Generic Profile: Raster crop -- input `raster`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/inputs/raster> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] ;
    proc:schema [ a ns1:string ;
            ns1:contentEncoding "base64" ;
            ns1:contentMediaType "image/tiff" ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-crop/outputs/raster> dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster> ;
    proc:keywords "GeoTIFF",
        "raster" ;
    proc:metadata [ dcterms:title "Generic Profile: Raster crop -- output `raster`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/outputs/raster> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output> ] ;
    proc:schema [ a ns1:string ;
            ns1:contentEncoding "base64" ;
            ns1:contentMediaType "image/tiff" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Implementation Profile "Raster crop" -- see generic-profiles.implementation-profile
  for the general shape every Implementation Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-crop
      x-jsonld-id: '@id'
    type:
      const: ImplementationProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Raster crop
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
    refinesGenericProfile:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/refinesGenericProfile
      x-jsonld-type: '@id'
    keywords:
      allOf:
      - contains:
          const: raster
      - contains:
          const: coverage
      - contains:
          const: crop
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop
      x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
    inputs:
      type: object
      required:
      - raster
      - areaOfInterest
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input
                    href:
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/inputs/raster
              x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
        areaOfInterest:
          properties:
            keywords:
              allOf:
              - contains:
                  const: bounding box
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/inputs/areaOfInterest
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/outputs/raster
              x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/outputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/
- type: object
  properties:
    inputs:
      properties:
        raster:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-crop/inputs/raster
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
        areaOfInterest:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-crop/inputs/areaOfInterest
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type/bounding-box
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-crop/outputs/raster
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

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/raster-crop/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/raster-crop/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/raster-crop/context.jsonld)

## Sources

* [OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard](https://www.ogc.org/standards/wcps/)
* [OTB ExtractROI -- Extracts a region of interest defined by the user](https://www.orfeo-toolbox.org/CookBook/Applications/app_ExtractROI.html)
* [OGC 17-069r4 OGC API - Features - Part 1: Core, §7.15.3 Parameter bbox](https://docs.ogc.org/is/17-069r4/17-069r4.html)
* [ogc.api.processes.v1.schemas.bbox -- bbox schema (OGC API - Processes - Part 1: Core)](https://geolabs.github.io/bblocks-ogcapi-processes/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/implementation-profile/raster-crop`

