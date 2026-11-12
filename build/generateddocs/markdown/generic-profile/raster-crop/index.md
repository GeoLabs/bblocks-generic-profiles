
# Generic Profile: Raster crop (Schema)

`generic-profiles.generic-profile.raster-crop` *v0.1*

Crops a raster coverage to a region of interest. One Raster input, a bounding box, one Raster output covering only that area.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Generic Profile: **Raster crop**.

> Crops a raster coverage to a region of interest. One Raster input, a bounding box, one Raster output covering only that area.

## Source

- ISO 19123-1:2023 *Geographic information -- Schema for coverage geometry and functions -- Part
  1: Fundamentals* -- the abstract coverage domain/range model this signature is grounded in (see
  [its Concept](../../concept/raster-coverage-processing/) for the full citation).
- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic
  Profile is.

## `areaOfInterest` is a concept at this tier, not a format

This tier carries a concept, `dataType`, and no format:
[Table 21](https://docs.ogc.org/is/14-065/14-065.html#32) gives Generic Profile no "Data format" row
at all. `areaOfInterest`'s `dataType` is `bounding-box`, a concept of the bblocks-data-types register.

Two earlier drafts took another route. The first used `Geometry`, the natural-seeming choice since a
region of interest reads like a geometric object. It did not match the real binding,
[`raster-crop`](../../implementation-profile/raster-crop/)'s own `OTB.ExtractROI`, whose "extent" mode
takes four plain numbers, `mode.extent.ulx`/`uly`/`lrx`/`lry`, not an encoded geometry: this is the
reason for `bounding-box` rather than `geometry`. The second was a `BoundingBox` type invented for
this register, which is no longer needed. The encoding lives at Implementation Profile, where
`areaOfInterest`'s `schema` `$ref`s
[`ogc.api.processes.part1.v1.schemas.bbox`](https://geolabs.github.io/bblocks-ogcapi-processes/)
directly -- OGC API - Processes - Part 1: Core's own bbox type (itself grounded in
[OGC 17-069r4](https://docs.ogc.org/is/17-069r4/17-069r4.html) §7.15.3's `bbox` parameter).

## Relations

- `broader`: [`generic-profiles.concept.raster-coverage-processing`](../../concept/raster-coverage-processing/)
- Refined by (1 Implementation Profile):
- [`raster-crop`](../../implementation-profile/raster-crop/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).

## Examples

### Raster crop
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop",
  "type": "GenericProfile",
  "prefLabel": "Raster crop",
  "definition": "Crops a raster coverage to a region of interest. One Raster input, an area of interest, one Raster output covering only that area.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile",
  "hasAction": [
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-09-30T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/actions/clarification-2026-11-06",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "clarifying",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-06T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop"
    }
  ],
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop",
  "itemClass": "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/generic-profile",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "broader": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
  ],
  "keywords": [
    "raster",
    "coverage",
    "crop"
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
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/inputs/raster",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/raster",
      "title": "Raster",
      "description": "the input raster coverage",
      "keywords": [
        "raster"
      ]
    },
    "areaOfInterest": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/inputs/areaOfInterest",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/bounding-box",
      "title": "Bounding box",
      "description": "the region of interest to crop to",
      "keywords": [
        "bounding box"
      ]
    }
  },
  "outputs": {
    "raster": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/outputs/raster",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/raster",
      "title": "Raster",
      "description": "the cropped raster coverage",
      "keywords": [
        "raster"
      ]
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/raster-crop/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop",
  "type": "GenericProfile",
  "prefLabel": "Raster crop",
  "definition": "Crops a raster coverage to a region of interest. One Raster input, an area of interest, one Raster output covering only that area.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile",
  "hasAction": [
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-09-30T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/actions/clarification-2026-11-06",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "clarifying",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-06T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop"
    }
  ],
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop",
  "itemClass": "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/generic-profile",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "broader": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
  ],
  "keywords": [
    "raster",
    "coverage",
    "crop"
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
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/inputs/raster",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/raster",
      "title": "Raster",
      "description": "the input raster coverage",
      "keywords": [
        "raster"
      ]
    },
    "areaOfInterest": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/inputs/areaOfInterest",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/bounding-box",
      "title": "Bounding box",
      "description": "the region of interest to crop to",
      "keywords": [
        "bounding box"
      ]
    }
  },
  "outputs": {
    "raster": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/outputs/raster",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/raster",
      "title": "Raster",
      "description": "the cropped raster coverage",
      "keywords": [
        "raster"
      ]
    }
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix gp: <https://geolabs.github.io/bblocks-generic-profiles/def/> .
@prefix ns1: <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/outputs/> .
@prefix ns2: <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/inputs/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/actions/addition> a rim:RegisterAction ;
    prov:startedAtTime "2026-09-30T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType rim:additionAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop> ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/actions/clarification-2026-11-06> a rim:RegisterAction ;
    prov:startedAtTime "2026-11-06T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType gp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop> ;
    rim:changeClassification rim:clarifyingChange ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/inputs/areaOfInterest> dcterms:description "the region of interest to crop to" ;
    dcterms:title "Bounding box" ;
    dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/bounding-box> ;
    proc:keywords "bounding box" .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/inputs/raster> dcterms:description "the input raster coverage" ;
    dcterms:title "Raster" ;
    dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/raster> ;
    proc:keywords "raster" .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/outputs/raster> dcterms:description "the cropped raster coverage" ;
    dcterms:title "Raster" ;
    dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/raster> ;
    proc:keywords "raster" .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop> a gp:GenericProfile ;
    skos:broader <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> ;
    skos:definition "Crops a raster coverage to a region of interest. One Raster input, an area of interest, one Raster output covering only that area." ;
    skos:inScheme gp:generic-profile ;
    skos:prefLabel "Raster crop" ;
    gp:inputs [ ns2:areaOfInterest <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/inputs/areaOfInterest> ;
            ns2:raster <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/inputs/raster> ] ;
    gp:outputs [ ns1:raster <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/outputs/raster> ] ;
    proc:keywords "coverage",
        "crop",
        "raster" ;
    proc:metadata [ dcterms:title "Process Concept: Raster Coverage Processing" ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] ;
    rim:hasAction <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/actions/addition>,
        <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/actions/clarification-2026-11-06> ;
    rim:inRegister gp:register ;
    rim:itemClass <https://geolabs.github.io/bblocks-generic-profiles/def/item-class/generic-profile> ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:invalid .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Generic Profile "Raster crop" -- see generic-profiles.generic-profile
  for the general shape every Generic Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop
      x-jsonld-id: '@id'
    type:
      const: GenericProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Raster crop
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
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/inputs/raster
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-data-types/def/data-type/raster
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
        areaOfInterest:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/inputs/areaOfInterest
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-data-types/def/data-type/bounding-box
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/inputs/
    outputs:
      properties:
        raster:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-crop/outputs/raster
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-data-types/def/data-type/raster
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/outputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/outputs/
x-jsonld-extra-terms:
  GenericProfile: https://geolabs.github.io/bblocks-generic-profiles/def/GenericProfile
  definition: http://www.w3.org/2004/02/skos/core#definition
  inScheme:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#inScheme
    x-jsonld-type: '@id'
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
  gp: https://geolabs.github.io/bblocks-generic-profiles/def/
  skos: http://www.w3.org/2004/02/skos/core#
  proc: https://w3id.org/ogc/api/processes/
  dct: http://purl.org/dc/terms/
x-bblocks-metadata:
  itemIdentifier: generic-profiles.generic-profile.raster-crop
  register: https://geolabs.github.io/bblocks-generic-profiles/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-12'

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/raster-crop/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/raster-crop/schema.yaml)


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
    "broader": {
      "@id": "skos:broader",
      "@type": "@id"
    },
    "keywords": "proc:keywords",
    "metadata": {
      "@context": {
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
        "dataType": {
          "@id": "dct:type",
          "@type": "@id"
        },
        "minOccurs": "proc:minOccurs",
        "maxOccurs": "proc:maxOccurs"
      },
      "@id": "gp:inputs"
    },
    "outputs": {
      "@context": {
        "@vocab": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/outputs/",
        "dataType": {
          "@id": "dct:type",
          "@type": "@id"
        }
      },
      "@id": "gp:outputs"
    },
    "GenericProfile": "gp:GenericProfile",
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
    "proc": "https://w3id.org/ogc/api/processes/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/raster-crop/context.jsonld)

## Sources

* [ZOO-Project process-profiles: Concept / Generic Profile / Implementation Profile](https://zoo-project.github.io/docs/services/process-profiles.html)
* [OGC API - Processes - Part 1: Core, InputDescription/OutputDescription](https://geolabs.github.io/bblocks-ogcapi-processes/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/generic-profile/raster-crop`

