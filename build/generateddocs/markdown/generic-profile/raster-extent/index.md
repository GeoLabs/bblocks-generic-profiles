
# Generic Profile: Raster extent (Schema)

`generic-profiles.generic-profile.raster-extent` *v0.1*

Computes the bounding envelope of a raster coverage, returned as a geometry (a rectangular polygon in the coverage's CRS). One Raster input, one Geometry output.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Generic Profile: **Raster extent**.

> Computes the bounding envelope of a raster coverage, returned as a geometry (a rectangular polygon in the coverage's CRS). One Raster input, one Geometry output.

## Source

- ISO 19123-1:2023 *Geographic information -- Schema for coverage geometry and functions -- Part
  1: Fundamentals* -- the abstract coverage domain/range model this signature is grounded in (see
  [its Concept](../../concept/raster-coverage-processing/) for the full citation).
- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic
  Profile is.

## Why the output is a Geometry, not a bounding box

The output is the coverage's bounding envelope -- conceptually "just" a bounding box -- but this
Generic Profile's real binding ([`OTB.ImageEnvelope`](../../implementation-profile/raster-extent/))
produces an actual vector polygon (GML/KML), not four plain numbers: *"Build a vector data
containing the image envelope polygon... you can set the polygon with more points with the `sr`
parameter"* -- `OTB.ImageEnvelope` can even densify the polygon's edges to follow a reprojection
curve, something four corner numbers cannot represent. This tier carries no type at all (see the
base schema's own note), but the Implementation Profile's `schema` reflects this: it declares
GML, not a `$ref` to `ogc.api.processes.v1.schemas.bbox` the way
[`raster-crop`](../raster-crop/)'s `areaOfInterest` does -- the two operations bind to genuinely
different real parameters, a polygon here, four plain numbers there.

## Relations

- `broader`: [`generic-profiles.concept.raster-coverage-processing`](../../concept/raster-coverage-processing/)
- Refined by (1 Implementation Profile):
- [`raster-extent`](../../implementation-profile/raster-extent/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).

## Examples

### Raster extent
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent",
  "type": "GenericProfile",
  "prefLabel": "Raster extent",
  "definition": "Computes the bounding envelope of a raster coverage, returned as a geometry (a rectangular polygon in the coverage's CRS). One Raster input, one Geometry output.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile",
  "status": "submitted",
  "broader": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
  ],
  "keywords": [
    "raster",
    "coverage",
    "extent"
  ],
  "metadata": [
    {
      "title": "Process Concept: Raster Coverage Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
    }
  ],
  "inputs": {
    "raster": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent/inputs/raster",
      "title": "Raster",
      "description": "the input raster coverage",
      "keywords": [
        "raster"
      ],
      "minOccurs": 1,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent/outputs/result",
      "title": "Geometry",
      "description": "the raster's bounding envelope",
      "keywords": [
        "geometry"
      ]
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/raster-extent/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent",
  "type": "GenericProfile",
  "prefLabel": "Raster extent",
  "definition": "Computes the bounding envelope of a raster coverage, returned as a geometry (a rectangular polygon in the coverage's CRS). One Raster input, one Geometry output.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile",
  "status": "submitted",
  "broader": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
  ],
  "keywords": [
    "raster",
    "coverage",
    "extent"
  ],
  "metadata": [
    {
      "title": "Process Concept: Raster Coverage Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
    }
  ],
  "inputs": {
    "raster": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent/inputs/raster",
      "title": "Raster",
      "description": "the input raster coverage",
      "keywords": [
        "raster"
      ],
      "minOccurs": 1,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent/outputs/result",
      "title": "Geometry",
      "description": "the raster's bounding envelope",
      "keywords": [
        "geometry"
      ]
    }
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix gp: <https://geolabs.github.io/bblocks-generic-profiles/def/> .
@prefix ns1: <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/inputs/> .
@prefix ns2: <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/outputs/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> ;
    skos:definition "Computes the bounding envelope of a raster coverage, returned as a geometry (a rectangular polygon in the coverage's CRS). One Raster input, one Geometry output." ;
    skos:inScheme gp:generic-profile ;
    skos:prefLabel "Raster extent" ;
    gp:inputs [ ns1:raster <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent/inputs/raster> ] ;
    gp:outputs [ ns2:result <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent/outputs/result> ] ;
    gp:status "submitted" ;
    proc:keywords "coverage",
        "extent",
        "raster" ;
    proc:metadata [ dcterms:title "Process Concept: Raster Coverage Processing" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent/inputs/raster> dcterms:description "the input raster coverage" ;
    dcterms:title "Raster" ;
    proc:keywords "raster" ;
    proc:maxOccurs 1 ;
    proc:minOccurs 1 .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent/outputs/result> dcterms:description "the raster's bounding envelope" ;
    dcterms:title "Geometry" ;
    proc:keywords "geometry" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Generic Profile "Raster extent" -- see generic-profiles.generic-profile
  for the general shape every Generic Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent
      x-jsonld-id: '@id'
    type:
      const: GenericProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Raster extent
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
- type: object
  properties:
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
      x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
    inputs:
      properties:
        raster:
          required:
          - id
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent/inputs/raster
              x-jsonld-id: '@id'
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/inputs/
    outputs:
      properties:
        result:
          required:
          - id
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-extent/outputs/result
              x-jsonld-id: '@id'
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/outputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/outputs/
x-jsonld-extra-terms:
  GenericProfile: http://www.w3.org/2004/02/skos/core#Concept
  definition: http://www.w3.org/2004/02/skos/core#definition
  inScheme:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#inScheme
    x-jsonld-type: '@id'
  status: https://geolabs.github.io/bblocks-generic-profiles/def/status
  broader:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#broader
    x-jsonld-type: '@id'
  keywords: https://w3id.org/ogc/api/processes/keywords
  source: http://purl.org/dc/terms/source
  title: http://purl.org/dc/terms/title
  link:
    x-jsonld-id: http://purl.org/dc/terms/references
    x-jsonld-type: '@id'
  clause: https://geolabs.github.io/bblocks-generic-profiles/def/clause
x-jsonld-prefixes:
  skos: http://www.w3.org/2004/02/skos/core#
  gp: https://geolabs.github.io/bblocks-generic-profiles/def/
  proc: https://w3id.org/ogc/api/processes/
  dct: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/raster-extent/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/raster-extent/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "GenericProfile": "skos:Concept",
    "id": "@id",
    "type": "@type",
    "prefLabel": "skos:prefLabel",
    "definition": "skos:definition",
    "inScheme": {
      "@id": "skos:inScheme",
      "@type": "@id"
    },
    "status": "gp:status",
    "broader": {
      "@id": "skos:broader",
      "@type": "@id"
    },
    "keywords": "proc:keywords",
    "metadata": {
      "@context": {
        "href": {
          "@id": "proc:href",
          "@type": "@id"
        },
        "role": {
          "@id": "proc:role",
          "@type": "@id"
        }
      },
      "@id": "proc:metadata"
    },
    "source": "dct:source",
    "inputs": {
      "@context": {
        "@vocab": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/inputs/",
        "description": "dct:description",
        "minOccurs": "proc:minOccurs",
        "maxOccurs": "proc:maxOccurs"
      },
      "@id": "gp:inputs"
    },
    "outputs": {
      "@context": {
        "@vocab": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/outputs/",
        "description": "dct:description"
      },
      "@id": "gp:outputs"
    },
    "title": "dct:title",
    "link": {
      "@id": "dct:references",
      "@type": "@id"
    },
    "clause": "gp:clause",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "gp": "https://geolabs.github.io/bblocks-generic-profiles/def/",
    "proc": "https://w3id.org/ogc/api/processes/",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/raster-extent/context.jsonld)

## Sources

* [ZOO-Project process-profiles: Concept / Generic Profile / Implementation Profile](https://zoo-project.github.io/docs/services/process-profiles.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/generic-profile/raster-extent`

