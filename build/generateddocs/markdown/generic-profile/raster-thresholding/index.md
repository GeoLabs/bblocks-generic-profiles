
# Generic Profile: Raster thresholding (Schema)

`generic-profiles.generic-profile.raster-thresholding` *v0.1*

Divides the cells of a single-band raster into two classes at a threshold that the operation determines from the raster's values, and returns the upper class as a binary mask. One single-band Raster input, one Binary mask output.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Generic Profile: **Raster thresholding**.

> Divides the cells of a single-band raster into two classes at a threshold that the operation determines from the raster's values, and returns the upper class as a binary mask. One single-band Raster input, one Binary mask output.

## Signature

| Role | Data type | Cardinality | Meaning |
|---|---|---|---|
| input `raster` | [`raster-single-band`](https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band) | exactly one | the single-band raster to threshold |
| output `mask` | [`binary-mask`](https://w3id.org/geolabs/ospd/data-types/data-type/binary-mask) | exactly one | the cells of the upper class |

Each data type is a concept of the [`bblocks-data-types`](https://github.com/GeoLabs/bblocks-data-types) register; this tier names no format ([OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32) gives Generic Profile no Data format row). Outputs have no cardinality: Table 21 has no Output.Multiplicity row.

## Source

- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic
  Profile is. The meaning of the operation, and the standards that define it, are its activity type (see the Implementation Profile).

## Relations

- `broader`: [`generic-profiles.concept.raster-coverage-processing`](../../concept/raster-coverage-processing/)
- Refined by (1 Implementation Profile):
- [`otsu-thresholding`](../../implementation-profile/otsu-thresholding/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level). A proposal added on 2026-11-10 (decision of 2026-11-10, six new process profiles).

## Examples

### Raster thresholding
#### json
```json
{
  "id": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding",
  "type": "GenericProfile",
  "prefLabel": "Raster thresholding",
  "definition": "Divides the cells of a single-band raster into two classes at a threshold that the operation determines from the raster's values, and returns the upper class as a binary mask. One single-band Raster input, one Binary mask output.",
  "inScheme": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile",
  "hasAction": [
    {
      "id": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://w3id.org/geolabs/ospd/generic-profiles/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding"
    },
    {
      "id": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding/actions/identifier-2026-11-17",
      "type": "RegisterAction",
      "actionType": "https://w3id.org/geolabs/ospd/generic-profiles/amendmentAction",
      "changeClassification": "clarifying",
      "affectedProperty": "https://w3id.org/ogc/rim/objectIdentifier",
      "description": "The object identifier of this item moves from https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-thresholding to https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding, which resolves through w3id.org (decision of 2026-11-17); the register actions of the item move with it, under https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding/actions/. The old IRI is kept as owl:sameAs. The content of the item is unchanged. Classified clarifying: the item is the same, only its identifier changes.",
      "proposer": "https://w3id.org/geolabs/ospd/generic-profiles/geolabs",
      "startedAtTime": "2026-11-17T00:00:00Z",
      "appliesTo": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding"
    }
  ],
  "objectIdentifier": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding",
  "sameAs": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-thresholding",
  "itemClass": "https://w3id.org/geolabs/ospd/generic-profiles/item-class/generic-profile",
  "inRegister": "https://w3id.org/geolabs/ospd/generic-profiles/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "broader": [
    "https://w3id.org/geolabs/ospd/generic-profiles/concept/raster-coverage-processing"
  ],
  "keywords": [
    "raster",
    "coverage",
    "thresholding"
  ],
  "metadata": [
    {
      "title": "Process Concept: Raster Coverage Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://w3id.org/geolabs/ospd/generic-profiles/concept/raster-coverage-processing"
    }
  ],
  "inputs": {
    "raster": {
      "id": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding/inputs/raster",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "title": "Raster (single band)",
      "description": "the single-band raster to threshold",
      "keywords": [
        "raster"
      ]
    }
  },
  "outputs": {
    "mask": {
      "id": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding/outputs/mask",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/binary-mask",
      "title": "Binary mask",
      "description": "the cells of the upper class",
      "keywords": [
        "mask"
      ]
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/raster-thresholding/context.jsonld",
  "id": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding",
  "type": "GenericProfile",
  "prefLabel": "Raster thresholding",
  "definition": "Divides the cells of a single-band raster into two classes at a threshold that the operation determines from the raster's values, and returns the upper class as a binary mask. One single-band Raster input, one Binary mask output.",
  "inScheme": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile",
  "hasAction": [
    {
      "id": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://w3id.org/geolabs/ospd/generic-profiles/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding"
    },
    {
      "id": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding/actions/identifier-2026-11-17",
      "type": "RegisterAction",
      "actionType": "https://w3id.org/geolabs/ospd/generic-profiles/amendmentAction",
      "changeClassification": "clarifying",
      "affectedProperty": "https://w3id.org/ogc/rim/objectIdentifier",
      "description": "The object identifier of this item moves from https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-thresholding to https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding, which resolves through w3id.org (decision of 2026-11-17); the register actions of the item move with it, under https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding/actions/. The old IRI is kept as owl:sameAs. The content of the item is unchanged. Classified clarifying: the item is the same, only its identifier changes.",
      "proposer": "https://w3id.org/geolabs/ospd/generic-profiles/geolabs",
      "startedAtTime": "2026-11-17T00:00:00Z",
      "appliesTo": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding"
    }
  ],
  "objectIdentifier": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding",
  "sameAs": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-thresholding",
  "itemClass": "https://w3id.org/geolabs/ospd/generic-profiles/item-class/generic-profile",
  "inRegister": "https://w3id.org/geolabs/ospd/generic-profiles/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "broader": [
    "https://w3id.org/geolabs/ospd/generic-profiles/concept/raster-coverage-processing"
  ],
  "keywords": [
    "raster",
    "coverage",
    "thresholding"
  ],
  "metadata": [
    {
      "title": "Process Concept: Raster Coverage Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://w3id.org/geolabs/ospd/generic-profiles/concept/raster-coverage-processing"
    }
  ],
  "inputs": {
    "raster": {
      "id": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding/inputs/raster",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "title": "Raster (single band)",
      "description": "the single-band raster to threshold",
      "keywords": [
        "raster"
      ]
    }
  },
  "outputs": {
    "mask": {
      "id": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding/outputs/mask",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/binary-mask",
      "title": "Binary mask",
      "description": "the cells of the upper class",
      "keywords": [
        "mask"
      ]
    }
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix gp: <https://w3id.org/geolabs/ospd/generic-profiles/> .
@prefix ns1: <https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/outputs/> .
@prefix ns2: <https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/inputs/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding/actions/addition> a rim:RegisterAction ;
    prov:startedAtTime "2026-11-10T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType rim:additionAction ;
    rim:appliesTo <https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding> ;
    rim:proposer gp:geolabs .

<https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding/actions/identifier-2026-11-17> a rim:RegisterAction ;
    dcterms:description "The object identifier of this item moves from https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-thresholding to https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding, which resolves through w3id.org (decision of 2026-11-17); the register actions of the item move with it, under https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding/actions/. The old IRI is kept as owl:sameAs. The content of the item is unchanged. Classified clarifying: the item is the same, only its identifier changes." ;
    prov:startedAtTime "2026-11-17T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType gp:amendmentAction ;
    rim:affectedProperty rim:objectIdentifier ;
    rim:appliesTo <https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding> ;
    rim:changeClassification rim:clarifyingChange ;
    rim:proposer gp:geolabs .

<https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding/inputs/raster> dcterms:description "the single-band raster to threshold" ;
    dcterms:title "Raster (single band)" ;
    dcterms:type <https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band> ;
    proc:keywords "raster" .

<https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding/outputs/mask> dcterms:description "the cells of the upper class" ;
    dcterms:title "Binary mask" ;
    dcterms:type <https://w3id.org/geolabs/ospd/data-types/data-type/binary-mask> ;
    proc:keywords "mask" .

<https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding> a gp:GenericProfile ;
    owl:sameAs <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-thresholding> ;
    skos:broader <https://w3id.org/geolabs/ospd/generic-profiles/concept/raster-coverage-processing> ;
    skos:definition "Divides the cells of a single-band raster into two classes at a threshold that the operation determines from the raster's values, and returns the upper class as a binary mask. One single-band Raster input, one Binary mask output." ;
    skos:inScheme gp:generic-profile ;
    skos:prefLabel "Raster thresholding" ;
    gp:inputs [ ns2:raster <https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding/inputs/raster> ] ;
    gp:outputs [ ns1:mask <https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding/outputs/mask> ] ;
    proc:keywords "coverage",
        "raster",
        "thresholding" ;
    proc:metadata [ dcterms:title "Process Concept: Raster Coverage Processing" ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] ;
    rim:hasAction <https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding/actions/addition>,
        <https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding/actions/identifier-2026-11-17> ;
    rim:inRegister gp:register ;
    rim:itemClass <https://w3id.org/geolabs/ospd/generic-profiles/item-class/generic-profile> ;
    rim:objectIdentifier "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:invalid .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Generic Profile "Raster thresholding" -- see generic-profiles.generic-profile
  for the general shape every Generic Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding
      x-jsonld-id: '@id'
    type:
      const: GenericProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Raster thresholding
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
              const: https://w3id.org/geolabs/ospd/generic-profiles/concept/raster-coverage-processing
      x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
    inputs:
      required:
      - raster
      properties:
        raster:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding/inputs/raster
              x-jsonld-id: '@id'
            dataType:
              const: https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
      x-jsonld-id: https://w3id.org/geolabs/ospd/generic-profiles/inputs
      x-jsonld-vocab: https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/inputs/
    outputs:
      required:
      - mask
      properties:
        mask:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/raster-thresholding/outputs/mask
              x-jsonld-id: '@id'
            dataType:
              const: https://w3id.org/geolabs/ospd/data-types/data-type/binary-mask
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
      x-jsonld-id: https://w3id.org/geolabs/ospd/generic-profiles/outputs
      x-jsonld-vocab: https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/outputs/
x-jsonld-extra-terms:
  GenericProfile: https://w3id.org/geolabs/ospd/generic-profiles/GenericProfile
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
  clause: https://w3id.org/geolabs/ospd/generic-profiles/clause
  sameAs:
    x-jsonld-id: http://www.w3.org/2002/07/owl#sameAs
    x-jsonld-type: '@id'
  affectedProperty:
    x-jsonld-id: https://w3id.org/ogc/rim/affectedProperty
    x-jsonld-type: '@id'
x-jsonld-prefixes:
  gp: https://w3id.org/geolabs/ospd/generic-profiles/
  skos: http://www.w3.org/2004/02/skos/core#
  proc: https://w3id.org/ogc/api/processes/
  dct: http://purl.org/dc/terms/
x-bblocks-metadata:
  itemIdentifier: generic-profiles.generic-profile.raster-thresholding
  register: https://geolabs.github.io/bblocks-generic-profiles/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-19'

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/raster-thresholding/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/raster-thresholding/schema.yaml)


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
        "@vocab": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/inputs/",
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
        "@vocab": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/outputs/",
        "dataType": {
          "@id": "dct:type",
          "@type": "@id"
        }
      },
      "@id": "gp:outputs"
    },
    "GenericProfile": "gp:GenericProfile",
    "sameAs": {
      "@id": "http://www.w3.org/2002/07/owl#sameAs",
      "@type": "@id"
    },
    "affectedProperty": {
      "@id": "rim:affectedProperty",
      "@type": "@id"
    },
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
    "gp": "https://w3id.org/geolabs/ospd/generic-profiles/",
    "proc": "https://w3id.org/ogc/api/processes/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/raster-thresholding/context.jsonld)

## Sources

* [OGC 14-065 WPS 2.0.2 Interface Standard Corrigendum 2, §7.5.2 Generic Process Profile](https://docs.ogc.org/is/14-065/14-065.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/generic-profile/raster-thresholding`

