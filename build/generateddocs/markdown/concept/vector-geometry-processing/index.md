
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
  "type": "ProcessConcept",
  "prefLabel": "Vector Geometry Processing",
  "definition": "Operations on vector geometries: testing a spatial relationship between two geometries, deriving a new geometry from one or two others, or measuring a property of a geometry. Covers the spatial predicates, set operations and measures of OGC Simple Feature Access - Common Architecture (06-103r4) and its harmonized-with-SQL predecessor, Simple Features Specification For SQL Revision 1.1 (99-049), independent of any specific operation's own input/output signature.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/concept",
  "hasAction": {
    "id": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing/actions/addition",
    "type": "RegisterAction",
    "actionType": "addition",
    "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
    "startedAtTime": "2026-09-30T00:00:00Z",
    "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"
  },
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing",
  "itemClass": "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/process-concept",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
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
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/concept/vector-geometry-processing/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing",
  "type": "ProcessConcept",
  "prefLabel": "Vector Geometry Processing",
  "definition": "Operations on vector geometries: testing a spatial relationship between two geometries, deriving a new geometry from one or two others, or measuring a property of a geometry. Covers the spatial predicates, set operations and measures of OGC Simple Feature Access - Common Architecture (06-103r4) and its harmonized-with-SQL predecessor, Simple Features Specification For SQL Revision 1.1 (99-049), independent of any specific operation's own input/output signature.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/concept",
  "hasAction": {
    "id": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing/actions/addition",
    "type": "RegisterAction",
    "actionType": "addition",
    "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
    "startedAtTime": "2026-09-30T00:00:00Z",
    "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"
  },
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing",
  "itemClass": "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/process-concept",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
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
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing> a gp:ProcessConcept ;
    dcterms:source [ dcterms:title "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture" ;
            gp:clause "§6.1" ],
        [ dcterms:title "OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1" ] ;
    skos:definition "Operations on vector geometries: testing a spatial relationship between two geometries, deriving a new geometry from one or two others, or measuring a property of a geometry. Covers the spatial predicates, set operations and measures of OGC Simple Feature Access - Common Architecture (06-103r4) and its harmonized-with-SQL predecessor, Simple Features Specification For SQL Revision 1.1 (99-049), independent of any specific operation's own input/output signature." ;
    skos:inScheme gp:concept ;
    skos:prefLabel "Vector Geometry Processing" ;
    rim:hasAction <https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing/actions/addition> ;
    rim:inRegister gp:register ;
    rim:itemClass <https://geolabs.github.io/bblocks-generic-profiles/def/item-class/process-concept> ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:invalid .

<https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing/actions/addition> a rim:RegisterAction ;
    prov:startedAtTime "2026-09-30T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType rim:additionAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing> ;
    rim:proposer gp:geolabs .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Concept "Vector Geometry Processing" -- see generic-profiles.concept
  for the general shape every Concept shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/concept/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing
      x-jsonld-id: '@id'
    type:
      const: ProcessConcept
      x-jsonld-id: '@type'
    prefLabel:
      const: Vector Geometry Processing
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
  itemIdentifier: generic-profiles.concept.vector-geometry-processing
  register: https://geolabs.github.io/bblocks-generic-profiles/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-04'

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/concept/vector-geometry-processing/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/concept/vector-geometry-processing/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/concept/vector-geometry-processing/context.jsonld)

## Sources

* [OGC 14-065 WPS 2.0.2 Interface Standard Corrigendum 2, §7.5.1 Process Concept](https://docs.ogc.org/is/14-065/14-065.html)
* [OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture](https://www.ogc.org/standards/sfa/)
* [OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1](https://www.ogc.org/standards/sfs/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/concept/vector-geometry-processing`

