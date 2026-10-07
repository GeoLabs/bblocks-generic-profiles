
# Process Concept (Schema)

`generic-profiles.concept` *v0.1*

The shape every Process Concept shares: high-level documentation about a general group of processes, no input, no output, no format, no implementation (OGC 14-065 WPS 2.0.2 §7.5.1). Each real Concept (generic-profiles.concept.*) is its own building block that allOf-references this one -- this block is not itself a catalogue, only the common shape plus one illustrative example.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Process Concept -- the shape every Concept in this register shares.

## What a Process Concept is

OGC 14-065 WPS 2.0.2 §7.5.1: *"a process concept is an object that provides high-level
documentation about a general group of processes. It describes the purpose, methodology and
properties of a process but not the specific input and output parameters. It is rather a
documentation resource that may be referenced by refined process definitions to document their
relation to a common principle."*

This block is not itself a catalogue: it carries one placeholder example only, clearly marked as
illustrative, not a real vocabulary entry. The real Concepts in this register are each their own
building block, `allOf`-referencing this one and adding their own `const`-pinned `id`/`prefLabel`:

- [`vector-geometry-processing`](vector-geometry-processing/) -- operations on vector geometries.
- [`raster-coverage-processing`](raster-coverage-processing/) -- operations on raster/coverage data.

## Register position

Top tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): **Concept** -> Generic Profile ->
Implementation Profile -> Implementation (instance level).

## Examples

### Example Concept (illustrative shape only, not a real vocabulary entry)
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/example-concept",
  "type": "Concept",
  "prefLabel": "Example Concept (placeholder, not a real vocabulary entry)",
  "definition": "Illustrates the shape of a Concept entry only. Real Concepts are each their own building block -- see generic-profiles.concept.vector-geometry-processing for actual vocabulary content.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/concept",
  "status": "submitted",
  "source": [
    {
      "title": "Placeholder -- not a real citation",
      "clause": "n/a"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/concept/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/example-concept",
  "type": "Concept",
  "prefLabel": "Example Concept (placeholder, not a real vocabulary entry)",
  "definition": "Illustrates the shape of a Concept entry only. Real Concepts are each their own building block -- see generic-profiles.concept.vector-geometry-processing for actual vocabulary content.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/concept",
  "status": "submitted",
  "source": [
    {
      "title": "Placeholder -- not a real citation",
      "clause": "n/a"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix gp: <https://geolabs.github.io/bblocks-generic-profiles/def/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/concept/example-concept> a skos:Concept ;
    dcterms:source [ dcterms:title "Placeholder -- not a real citation" ;
            gp:clause "n/a" ] ;
    skos:definition "Illustrates the shape of a Concept entry only. Real Concepts are each their own building block -- see generic-profiles.concept.vector-geometry-processing for actual vocabulary content." ;
    skos:inScheme gp:concept ;
    skos:prefLabel "Example Concept (placeholder, not a real vocabulary entry)" ;
    gp:status "submitted" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: "Process Concept (OGC 14-065 WPS 2.0.2 \xA77.5.1): \"high-level documentation
  about a general group of processes... the purpose, methodology and properties of
  a process but not the specific input and output parameters... a documentation resource
  that may be referenced by refined process definitions to document their relation
  to a common principle.\" Deliberately carries no I/O, no format, no CWL: each generic-profiles.generic-profile.*
  entry declares the Concept(s) it belongs to (e.g. vector geometry processing, raster
  coverage processing) as its `broader` concept."
type: object
required:
- id
- type
- prefLabel
- definition
- inScheme
- status
- source
properties:
  id:
    type: string
    format: uri
    x-jsonld-id: '@id'
  type:
    const: Concept
    x-jsonld-id: '@type'
  prefLabel:
    type: string
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
  definition:
    type: string
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#definition
  inScheme:
    type: string
    format: uri
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#inScheme
    x-jsonld-type: '@id'
  status:
    type: string
    enum:
    - submitted
    - valid
    - invalid
    - superseded
    - retired
    x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/status
  source:
    type: array
    minItems: 1
    items:
      type: object
      required:
      - title
      properties:
        title:
          type: string
          x-jsonld-id: http://purl.org/dc/terms/title
        link:
          type: string
          format: uri
          x-jsonld-id: http://purl.org/dc/terms/references
          x-jsonld-type: '@id'
        clause:
          type: string
          x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/clause
    x-jsonld-id: http://purl.org/dc/terms/source
  narrower:
    type: array
    items:
      type: string
      format: uri
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#narrower
    x-jsonld-type: '@id'
x-jsonld-extra-terms:
  Concept: http://www.w3.org/2004/02/skos/core#Concept
x-jsonld-prefixes:
  skos: http://www.w3.org/2004/02/skos/core#
  gp: https://geolabs.github.io/bblocks-generic-profiles/def/
  dct: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/concept/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/concept/schema.yaml)


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
    "source": {
      "@context": {
        "title": "dct:title",
        "link": {
          "@id": "dct:references",
          "@type": "@id"
        },
        "clause": "gp:clause"
      },
      "@id": "dct:source"
    },
    "narrower": {
      "@id": "skos:narrower",
      "@type": "@id"
    },
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "gp": "https://geolabs.github.io/bblocks-generic-profiles/def/",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/concept/context.jsonld)

## Sources

* [OGC 14-065 WPS 2.0.2 Interface Standard Corrigendum 2, §7.5.1 Process Concept](https://docs.ogc.org/is/14-065/14-065.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/concept`

