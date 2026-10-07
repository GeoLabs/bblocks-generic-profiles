
# Process Concept: Raster Coverage Processing (Schema)

`generic-profiles.concept.raster-coverage-processing` *v0.1*

Operations on raster/coverage data: reprojecting a coverage to another coordinate reference system, deriving a new raster from one or more others via a mathematical expression or a named radiometric index, cropping a coverage to a region of interest, or converting a coverage to another encoding -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 §7.5.1).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Process Concept: **Raster Coverage Processing**.

> Operations on raster/coverage data: reprojecting a coverage to another coordinate reference
> system, deriving a new raster from one or more others via a mathematical expression or a named
> radiometric index, cropping a coverage to a region of interest, or converting a coverage to
> another encoding.

## What a Process Concept is

OGC 14-065 WPS 2.0.2 §7.5.1: *"a process concept is an object that provides high-level
documentation about a general group of processes. It describes the purpose, methodology and
properties of a process but not the specific input and output parameters. It is rather a
documentation resource that may be referenced by refined process definitions to document their
relation to a common principle."*

This Concept deliberately carries no input, no output, no format, no CWL and no implementation --
that is what the two tiers below it are for. It exists so that several Generic Profiles with
different I/O shapes can still declare their kinship:
[`raster-reprojection`](../../generic-profile/raster-reprojection/),
[`raster-band-math`](../../generic-profile/raster-band-math/),
[`radiometric-index`](../../generic-profile/radiometric-index/),
[`raster-crop`](../../generic-profile/raster-crop/),
[`raster-format-conversion`](../../generic-profile/raster-format-conversion/) and
[`raster-extent`](../../generic-profile/raster-extent/) each declare this
Concept as their `broader`.

## Source

Two standards, at different levels, the same way [`vector-geometry-processing`](../vector-geometry-processing/)
is grounded in Simple Feature Access and SQL/MM:

- ISO 19123-1:2023 *Geographic information -- Schema for coverage geometry and functions -- Part 1:
  Fundamentals* -- the abstract domain/range model of a coverage (a raster is one kind of coverage),
  with no processing language attached. This is the raster/coverage analogue of what OGC 06-103r4
  Simple Feature Access is for vector geometry.
- [OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard](https://www.ogc.org/standards/wcps/)
  -- an OGC standard that *does* bind coverage operations (subsetting, band math, reprojection) to
  a concrete query language. It is not cited as any one Implementation Profile's format binding
  below (GDAL and OTB, not WCPS, are what the Geonovum testbed actually runs), only as the
  standards-track evidence that these operations are recognised, harmonised processing concepts
  and not implementation-specific inventions.

## Register position

Top tier of the four-tier model this register implements (OGC 14-065 WPS 2.0.2 §7.5): Concept ->
Generic Profile -> Implementation Profile -> Implementation (instance level). The fourth tier is
not part of this register -- see `ospd.process-profiles.*` in `bblocks-process-profiles`.

## Examples

### Raster Coverage Processing
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing",
  "type": "Concept",
  "prefLabel": "Raster Coverage Processing",
  "definition": "Operations on raster/coverage data: reprojecting a coverage to another coordinate reference system, deriving a new raster from one or more others via a mathematical expression or a named radiometric index, cropping a coverage to a region of interest, or converting a coverage to another encoding -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 \u00a77.5.1).",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/concept",
  "status": "submitted",
  "source": [
    {
      "title": "ISO 19123-1:2023 Geographic information -- Schema for coverage geometry and functions -- Part 1: Fundamentals"
    },
    {
      "title": "OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard",
      "link": "https://www.ogc.org/standards/wcps/"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://raw.githubusercontent.com/GeoLabs/bblocks-generic-profiles/undefined/build/annotated/concept/raster-coverage-processing/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing",
  "type": "Concept",
  "prefLabel": "Raster Coverage Processing",
  "definition": "Operations on raster/coverage data: reprojecting a coverage to another coordinate reference system, deriving a new raster from one or more others via a mathematical expression or a named radiometric index, cropping a coverage to a region of interest, or converting a coverage to another encoding -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 \u00a77.5.1).",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/concept",
  "status": "submitted",
  "source": [
    {
      "title": "ISO 19123-1:2023 Geographic information -- Schema for coverage geometry and functions -- Part 1: Fundamentals"
    },
    {
      "title": "OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard",
      "link": "https://www.ogc.org/standards/wcps/"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix gp: <https://geolabs.github.io/bblocks-generic-profiles/def/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> a skos:Concept ;
    dcterms:source [ dcterms:references <https://www.ogc.org/standards/wcps/> ;
            dcterms:title "OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard" ],
        [ dcterms:title "ISO 19123-1:2023 Geographic information -- Schema for coverage geometry and functions -- Part 1: Fundamentals" ] ;
    skos:definition "Operations on raster/coverage data: reprojecting a coverage to another coordinate reference system, deriving a new raster from one or more others via a mathematical expression or a named radiometric index, cropping a coverage to a region of interest, or converting a coverage to another encoding -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 §7.5.1)." ;
    skos:inScheme gp:concept ;
    skos:prefLabel "Raster Coverage Processing" ;
    gp:status "submitted" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Concept "Raster Coverage Processing" -- see generic-profiles.concept
  for the general shape every Concept shares.
allOf:
- $ref: https://raw.githubusercontent.com/GeoLabs/bblocks-generic-profiles/undefined/build/annotated/concept/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing
      x-jsonld-id: '@id'
    type:
      const: Concept
      x-jsonld-id: '@type'
    prefLabel:
      const: Raster Coverage Processing
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
x-jsonld-extra-terms:
  Concept: http://www.w3.org/2004/02/skos/core#Concept
  definition: http://www.w3.org/2004/02/skos/core#definition
  inScheme:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#inScheme
    x-jsonld-type: '@id'
  status: https://geolabs.github.io/bblocks-generic-profiles/def/status
  narrower:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#narrower
    x-jsonld-type: '@id'
  source: http://purl.org/dc/terms/source
  title: http://purl.org/dc/terms/title
  link:
    x-jsonld-id: http://purl.org/dc/terms/references
    x-jsonld-type: '@id'
  clause: https://geolabs.github.io/bblocks-generic-profiles/def/clause
x-jsonld-prefixes:
  skos: http://www.w3.org/2004/02/skos/core#
  gp: https://geolabs.github.io/bblocks-generic-profiles/def/
  dct: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://raw.githubusercontent.com/GeoLabs/bblocks-generic-profiles/undefined/build/annotated/concept/raster-coverage-processing/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/GeoLabs/bblocks-generic-profiles/undefined/build/annotated/concept/raster-coverage-processing/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "Concept": "skos:Concept",
    "id": "@id",
    "type": "@type",
    "prefLabel": "skos:prefLabel",
    "definition": "skos:definition",
    "inScheme": {
      "@id": "skos:inScheme",
      "@type": "@id"
    },
    "status": "gp:status",
    "source": "dct:source",
    "narrower": {
      "@id": "skos:narrower",
      "@type": "@id"
    },
    "title": "dct:title",
    "link": {
      "@id": "dct:references",
      "@type": "@id"
    },
    "clause": "gp:clause",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "gp": "https://geolabs.github.io/bblocks-generic-profiles/def/",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://raw.githubusercontent.com/GeoLabs/bblocks-generic-profiles/undefined/build/annotated/concept/raster-coverage-processing/context.jsonld)

## Sources

* [ZOO-Project process-profiles: Concept / Generic Profile / Implementation Profile](https://zoo-project.github.io/docs/services/process-profiles.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/concept/raster-coverage-processing`

