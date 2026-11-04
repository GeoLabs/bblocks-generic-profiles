
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

Narrower concept: [`terrain-analysis`](../terrain-analysis/) -- an elevation model is a single-band
raster (`data-types.data-type.elevation-model`).

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
  "type": "ProcessConcept",
  "prefLabel": "Raster Coverage Processing",
  "definition": "Operations on raster/coverage data: reprojecting a coverage to another coordinate reference system, deriving a new raster from one or more others via a mathematical expression or a named radiometric index, cropping a coverage to a region of interest, or converting a coverage to another encoding -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 \u00a77.5.1).",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/concept",
  "hasAction": {
    "id": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing/actions/addition",
    "type": "RegisterAction",
    "actionType": "addition",
    "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
    "startedAtTime": "2026-09-30T00:00:00Z",
    "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
  },
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing",
  "itemClass": "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/process-concept",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "source": [
    {
      "title": "ISO 19123-1:2023 Geographic information -- Schema for coverage geometry and functions -- Part 1: Fundamentals"
    },
    {
      "title": "OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard",
      "link": "https://www.ogc.org/standards/wcps/"
    }
  ],
  "narrower": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis"
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/concept/raster-coverage-processing/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing",
  "type": "ProcessConcept",
  "prefLabel": "Raster Coverage Processing",
  "definition": "Operations on raster/coverage data: reprojecting a coverage to another coordinate reference system, deriving a new raster from one or more others via a mathematical expression or a named radiometric index, cropping a coverage to a region of interest, or converting a coverage to another encoding -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 \u00a77.5.1).",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/concept",
  "hasAction": {
    "id": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing/actions/addition",
    "type": "RegisterAction",
    "actionType": "addition",
    "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
    "startedAtTime": "2026-09-30T00:00:00Z",
    "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
  },
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing",
  "itemClass": "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/process-concept",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "source": [
    {
      "title": "ISO 19123-1:2023 Geographic information -- Schema for coverage geometry and functions -- Part 1: Fundamentals"
    },
    {
      "title": "OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard",
      "link": "https://www.ogc.org/standards/wcps/"
    }
  ],
  "narrower": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis"
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

<https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> a gp:ProcessConcept ;
    dcterms:source [ dcterms:title "ISO 19123-1:2023 Geographic information -- Schema for coverage geometry and functions -- Part 1: Fundamentals" ],
        [ dcterms:references <https://www.ogc.org/standards/wcps/> ;
            dcterms:title "OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard" ] ;
    skos:definition "Operations on raster/coverage data: reprojecting a coverage to another coordinate reference system, deriving a new raster from one or more others via a mathematical expression or a named radiometric index, cropping a coverage to a region of interest, or converting a coverage to another encoding -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 §7.5.1)." ;
    skos:inScheme gp:concept ;
    skos:narrower <https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis> ;
    skos:prefLabel "Raster Coverage Processing" ;
    rim:hasAction <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing/actions/addition> ;
    rim:inRegister gp:register ;
    rim:itemClass <https://geolabs.github.io/bblocks-generic-profiles/def/item-class/process-concept> ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:invalid .

<https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing/actions/addition> a rim:RegisterAction ;
    prov:startedAtTime "2026-09-30T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType rim:additionAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> ;
    rim:proposer gp:geolabs .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Concept "Raster Coverage Processing" -- see generic-profiles.concept
  for the general shape every Concept shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/concept/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing
      x-jsonld-id: '@id'
    type:
      const: ProcessConcept
      x-jsonld-id: '@type'
    prefLabel:
      const: Raster Coverage Processing
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
x-jsonld-extra-terms:
  ProcessConcept: https://geolabs.github.io/bblocks-generic-profiles/def/ProcessConcept
  definition: http://www.w3.org/2004/02/skos/core#definition
  inScheme:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#inScheme
    x-jsonld-type: '@id'
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
  gp: https://geolabs.github.io/bblocks-generic-profiles/def/
  skos: http://www.w3.org/2004/02/skos/core#
  dct: http://purl.org/dc/terms/
x-bblocks-metadata:
  itemIdentifier: generic-profiles.concept.raster-coverage-processing
  register: https://geolabs.github.io/bblocks-generic-profiles/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-04'

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/concept/raster-coverage-processing/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/concept/raster-coverage-processing/schema.yaml)


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
    "source": "dct:source",
    "narrower": {
      "@id": "skos:narrower",
      "@type": "@id"
    },
    "ProcessConcept": "gp:ProcessConcept",
    "link": {
      "@id": "dct:references",
      "@type": "@id"
    },
    "clause": "gp:clause",
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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/concept/raster-coverage-processing/context.jsonld)

## Sources

* [ZOO-Project process-profiles: Concept / Generic Profile / Implementation Profile](https://zoo-project.github.io/docs/services/process-profiles.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/concept/raster-coverage-processing`

