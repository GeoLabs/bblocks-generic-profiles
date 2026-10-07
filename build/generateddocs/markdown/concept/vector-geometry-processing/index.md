
# Process Concept: Vector Geometry Processing (Schema)

`generic-profiles.concept.vector-geometry-processing` *v0.1*

General group covering operations on vector geometries: testing spatial relationships between two geometries, deriving a new geometry from one or two others, and measuring a geometry's own properties -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 §7.5.1).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Process Concept: **Vector Geometry Processing**.

> Operations on vector geometries: testing a spatial relationship between two geometries, deriving
> a new geometry from one or two others, or measuring a property of a geometry.

## What a Process Concept is

OGC 14-065 WPS 2.0.2 §7.5.1: *"a process concept is an object that provides high-level
documentation about a general group of processes. It describes the purpose, methodology and
properties of a process but not the specific input and output parameters. It is rather a
documentation resource that may be referenced by refined process definitions to document their
relation to a common principle."*

This Concept deliberately carries no input, no output, no format, no CWL and no implementation --
that is what the two tiers below it are for. It exists so that several Generic Profiles with
different I/O shapes can still declare their kinship: [`binary-spatial-predicate`](../../generic-profile/binary-spatial-predicate/),
[`binary-spatial-operation`](../../generic-profile/binary-spatial-operation/),
[`geometry-buffer`](../../generic-profile/geometry-buffer/),
[`unary-geometry-operation`](../../generic-profile/unary-geometry-operation/),
[`unary-spatial-predicate`](../../generic-profile/unary-spatial-predicate/) and
[`geometry-measure`](../../generic-profile/geometry-measure/) each declare this Concept as their
`broader`.

## Source

- [OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture](https://www.ogc.org/standards/sfa/), §6.1 -- the 7
  predicates, 4 set operations and buffer are defined there.
- [OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1](https://www.ogc.org/standards/sfs/) --
  the harmonized-with-SQL predecessor to 06-103r4; Envelope (§2.1.1.1), Centroid/Area/PointOnSurface
  (§2.1.9.1) and ConvexHull/IsSimple (§2.1.1.1, §2.1.1.3) are defined there. Together the two
  standards ground the 17 operations this Concept groups (7 predicates, 4 set operations, buffer,
  envelope, centroid, convex hull, area, is-simple).

## Register position

Top tier of the four-tier model this register implements (OGC 14-065 WPS 2.0.2 §7.5): Concept ->
Generic Profile -> Implementation Profile -> Implementation (instance level). The fourth tier is
not part of this register -- see `ospd.process-profiles.sqlmm.*` in `bblocks-process-profiles`.

## Examples

### Vector Geometry Processing
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing",
  "type": "Concept",
  "prefLabel": "Vector Geometry Processing",
  "definition": "Operations on vector geometries: testing a spatial relationship between two geometries, deriving a new geometry from one or two others, or measuring a property of a geometry. Covers the spatial predicates, set operations and measures of OGC Simple Feature Access - Common Architecture (06-103r4) and its harmonized-with-SQL predecessor, Simple Features Specification For SQL Revision 1.1 (99-049), independent of any specific operation's own input/output signature.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/concept",
  "status": "submitted",
  "source": [
    {
      "title": "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture",
      "clause": "§6.1"
    },
    {
      "title": "OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://raw.githubusercontent.com/GeoLabs/bblocks-generic-profiles/undefined/build/annotated/concept/vector-geometry-processing/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing",
  "type": "Concept",
  "prefLabel": "Vector Geometry Processing",
  "definition": "Operations on vector geometries: testing a spatial relationship between two geometries, deriving a new geometry from one or two others, or measuring a property of a geometry. Covers the spatial predicates, set operations and measures of OGC Simple Feature Access - Common Architecture (06-103r4) and its harmonized-with-SQL predecessor, Simple Features Specification For SQL Revision 1.1 (99-049), independent of any specific operation's own input/output signature.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/concept",
  "status": "submitted",
  "source": [
    {
      "title": "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture",
      "clause": "\u00a76.1"
    },
    {
      "title": "OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix gp: <https://geolabs.github.io/bblocks-generic-profiles/def/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing> a skos:Concept ;
    dcterms:source [ dcterms:title "OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1" ],
        [ dcterms:title "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture" ;
            gp:clause "§6.1" ] ;
    skos:definition "Operations on vector geometries: testing a spatial relationship between two geometries, deriving a new geometry from one or two others, or measuring a property of a geometry. Covers the spatial predicates, set operations and measures of OGC Simple Feature Access - Common Architecture (06-103r4) and its harmonized-with-SQL predecessor, Simple Features Specification For SQL Revision 1.1 (99-049), independent of any specific operation's own input/output signature." ;
    skos:inScheme gp:concept ;
    skos:prefLabel "Vector Geometry Processing" ;
    gp:status "submitted" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Concept "Vector Geometry Processing" -- see generic-profiles.concept
  for the general shape every Concept shares.
allOf:
- $ref: https://raw.githubusercontent.com/GeoLabs/bblocks-generic-profiles/undefined/build/annotated/concept/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing
      x-jsonld-id: '@id'
    type:
      const: Concept
      x-jsonld-id: '@type'
    prefLabel:
      const: Vector Geometry Processing
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

* YAML version: [schema.yaml](https://raw.githubusercontent.com/GeoLabs/bblocks-generic-profiles/undefined/build/annotated/concept/vector-geometry-processing/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/GeoLabs/bblocks-generic-profiles/undefined/build/annotated/concept/vector-geometry-processing/schema.yaml)


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
[context.jsonld](https://raw.githubusercontent.com/GeoLabs/bblocks-generic-profiles/undefined/build/annotated/concept/vector-geometry-processing/context.jsonld)

## Sources

* [OGC 14-065 WPS 2.0.2 Interface Standard Corrigendum 2, §7.5.1 Process Concept](https://docs.ogc.org/is/14-065/14-065.html)
* [OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture](https://www.ogc.org/standards/sfa/)
* [OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1](https://www.ogc.org/standards/sfs/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/concept/vector-geometry-processing`

