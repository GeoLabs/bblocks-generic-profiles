
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
  "type": "ProcessConcept",
  "prefLabel": "Example Concept (placeholder, not a real vocabulary entry)",
  "definition": "Illustrates the shape of a Concept entry only. Real Concepts are each their own building block -- see generic-profiles.concept.vector-geometry-processing for actual vocabulary content.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/concept",
  "hasAction": {
    "id": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/example-concept/actions/addition",
    "type": "RegisterAction",
    "actionType": "addition",
    "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
    "startedAtTime": "2026-09-30T00:00:00Z",
    "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/example-concept"
  },
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/example-concept",
  "itemClass": "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/process-concept",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
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
  "type": "ProcessConcept",
  "prefLabel": "Example Concept (placeholder, not a real vocabulary entry)",
  "definition": "Illustrates the shape of a Concept entry only. Real Concepts are each their own building block -- see generic-profiles.concept.vector-geometry-processing for actual vocabulary content.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/concept",
  "hasAction": {
    "id": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/example-concept/actions/addition",
    "type": "RegisterAction",
    "actionType": "addition",
    "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
    "startedAtTime": "2026-09-30T00:00:00Z",
    "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/example-concept"
  },
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/example-concept",
  "itemClass": "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/process-concept",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
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
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/concept/example-concept> a gp:ProcessConcept ;
    dcterms:source [ dcterms:title "Placeholder -- not a real citation" ;
            gp:clause "n/a" ] ;
    skos:definition "Illustrates the shape of a Concept entry only. Real Concepts are each their own building block -- see generic-profiles.concept.vector-geometry-processing for actual vocabulary content." ;
    skos:inScheme gp:concept ;
    skos:prefLabel "Example Concept (placeholder, not a real vocabulary entry)" ;
    rim:hasAction <https://geolabs.github.io/bblocks-generic-profiles/def/concept/example-concept/actions/addition> ;
    rim:inRegister gp:register ;
    rim:itemClass <https://geolabs.github.io/bblocks-generic-profiles/def/item-class/process-concept> ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-generic-profiles/def/concept/example-concept"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:invalid .

<https://geolabs.github.io/bblocks-generic-profiles/def/concept/example-concept/actions/addition> a rim:RegisterAction ;
    prov:startedAtTime "2026-09-30T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType rim:additionAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/concept/example-concept> ;
    rim:proposer gp:geolabs .


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
allOf:
- $ref: https://ogcincubator.github.io/registered-item-model/build/annotated/rim/schemas/register-item/schema.yaml
- type: object
  required:
  - id
  - type
  - prefLabel
  - definition
  - inScheme
  - source
  - itemClass
  - inRegister
  - hasAction
  properties:
    id:
      type: string
      format: uri
      x-jsonld-id: '@id'
    type:
      const: ProcessConcept
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
    itemClass:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/item-class/process-concept
    inRegister:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/register
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
  ProcessConcept: https://geolabs.github.io/bblocks-generic-profiles/def/ProcessConcept
x-jsonld-prefixes:
  gp: https://geolabs.github.io/bblocks-generic-profiles/def/
  skos: http://www.w3.org/2004/02/skos/core#
  dct: http://purl.org/dc/terms/
x-bblocks-metadata:
  itemIdentifier: generic-profiles.concept
  register: https://geolabs.github.io/bblocks-generic-profiles/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-12'

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/concept/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/concept/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "Register": "rim:Register",
    "RegisterSystem": "rim:RegisterSystem",
    "RegisterSpecification": "rim:RegisterSpecification",
    "RegisterItemClass": "rim:RegisterItemClass",
    "RegisterItem": "rim:RegisterItem",
    "RegisterAction": "rim:RegisterAction",
    "Concept": "rim:Concept",
    "ConceptVersion": "rim:ConceptVersion",
    "ConceptSystem": "rim:ConceptSystem",
    "Commitment": "rim:Commitment",
    "Agent": "prov:Agent",
    "Organization": "prov:Organization",
    "Person": "prov:Person",
    "label": "rdfs:label",
    "prefLabel": "skos:prefLabel",
    "definition": "skos:definition",
    "inScheme": {
      "@id": "skos:inScheme",
      "@type": "@id"
    },
    "runsOn": {
      "@id": "rim:runsOn",
      "@type": "@id"
    },
    "hasSpecification": {
      "@id": "rim:hasSpecification",
      "@type": "@id"
    },
    "definesSubstantiveChange": "rim:definesSubstantiveChange",
    "registerOwner": {
      "@id": "rim:registerOwner",
      "@type": "@id"
    },
    "registerManager": {
      "@id": "rim:registerManager",
      "@type": "@id"
    },
    "controlBody": {
      "@id": "rim:controlBody",
      "@type": "@id"
    },
    "registerSystemManager": {
      "@id": "rim:registerSystemManager",
      "@type": "@id"
    },
    "registerUser": {
      "@id": "rim:registerUser",
      "@type": "@id"
    },
    "hasCommitment": {
      "@id": "rim:hasCommitment",
      "@type": "@id"
    },
    "commitmentCategory": {
      "@id": "rim:commitmentCategory",
      "@type": "@vocab"
    },
    "access": "rim:accessCommitment",
    "persistence": "rim:persistenceCommitment",
    "transparency": "rim:transparencyCommitment",
    "definedIn": {
      "@id": "rim:definedIn",
      "@type": "@id"
    },
    "validatedBy": {
      "@id": "rim:validatedBy",
      "@type": "@id"
    },
    "versionOf": {
      "@id": "rim:versionOf",
      "@type": "@id"
    },
    "version": "rim:version",
    "valid": "rim:valid",
    "invalid": "rim:invalid",
    "published": "rim:published",
    "unpublished": "rim:unpublished",
    "appliesTo": {
      "@id": "rim:appliesTo",
      "@type": "@id"
    },
    "proposer": {
      "@id": "rim:proposer",
      "@type": "@id"
    },
    "actionType": {
      "@id": "rim:actionType",
      "@type": "@vocab"
    },
    "addition": "rim:additionAction",
    "publish": "rim:publishAction",
    "unpublish": "rim:unpublishAction",
    "invalidation": "rim:invalidationAction",
    "supersession": "rim:supersessionAction",
    "redaction": "rim:redactionAction",
    "deletion": "rim:deletionAction",
    "changeClassification": {
      "@id": "rim:changeClassification",
      "@type": "@vocab"
    },
    "substantive": "rim:substantiveChange",
    "clarifying": "rim:clarifyingChange",
    "correctional": "rim:correctionalChange",
    "startedAtTime": {
      "@id": "prov:startedAtTime",
      "@type": "xsd:dateTime"
    },
    "endedAtTime": {
      "@id": "prov:endedAtTime",
      "@type": "xsd:dateTime"
    },
    "wasAssociatedWith": {
      "@id": "prov:wasAssociatedWith",
      "@type": "@id"
    },
    "id": "@id",
    "type": "@type",
    "objectIdentifier": {
      "@id": "rim:objectIdentifier",
      "@type": "xsd:anyURI"
    },
    "functionalIdentifier": {
      "@id": "rim:functionalIdentifier",
      "@type": "xsd:anyURI"
    },
    "itemClass": {
      "@id": "rim:itemClass",
      "@type": "@id"
    },
    "inRegister": {
      "@id": "rim:inRegister",
      "@type": "@id"
    },
    "realizes": {
      "@id": "rim:realizes",
      "@type": "@id"
    },
    "validityStatus": {
      "@id": "rim:validityStatus",
      "@type": "@vocab"
    },
    "publicationStatus": {
      "@id": "rim:publicationStatus",
      "@type": "@vocab"
    },
    "isRedacted": {
      "@id": "rim:isRedacted",
      "@type": "xsd:boolean"
    },
    "isDeleted": {
      "@id": "rim:isDeleted",
      "@type": "xsd:boolean"
    },
    "title": "dct:title",
    "description": "dct:description",
    "relatedItem": {
      "@id": "rim:relatedItem",
      "@type": "@id"
    },
    "supersededBy": {
      "@id": "rim:supersededBy",
      "@type": "@id"
    },
    "supersedes": {
      "@id": "rim:supersedes",
      "@type": "@id"
    },
    "hasAction": {
      "@id": "rim:hasAction",
      "@type": "@id"
    },
    "source": {
      "@context": {
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
    "ProcessConcept": "gp:ProcessConcept",
    "rim": "https://w3id.org/ogc/rim/",
    "prov": "http://www.w3.org/ns/prov#",
    "dct": "http://purl.org/dc/terms/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "gp": "https://geolabs.github.io/bblocks-generic-profiles/def/",
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

