
# Generic Profile: Band retrieval (Schema)

`generic-profiles.generic-profile.band-retrieval` *v0.1*

Retrieves one band of an Earth observation product as a raster, over the whole product or over an area of interest. A product, a band identifier and an optional bounding box in, one Raster out.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Generic Profile: **Band retrieval**.

> Retrieves one band of an Earth observation product as a raster, over the whole product or over an area of interest. A product, a band identifier and an optional bounding box in, one Raster out.

## Signature

| Role | Data type | Cardinality | Meaning |
|---|---|---|---|
| input `product` | [`eo-product`](https://geolabs.github.io/bblocks-data-types/def/data-type/eo-product) | exactly one | the product the band belongs to |
| input `band` | [`band-identifier`](https://geolabs.github.io/bblocks-data-types/def/data-type/band-identifier) | exactly one | the band to retrieve |
| input `areaOfInterest` | [`bounding-box`](https://geolabs.github.io/bblocks-data-types/def/data-type/bounding-box) | minOccurs 0 | the area to retrieve; the whole product when absent |
| output `raster` | [`raster`](https://geolabs.github.io/bblocks-data-types/def/data-type/raster) | exactly one | the retrieved band |

Each data type is a concept of the [`bblocks-data-types`](https://github.com/GeoLabs/bblocks-data-types) register; this tier names no format ([OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32) gives Generic Profile no Data format row). Outputs have no cardinality: Table 21 has no Output.Multiplicity row.

`areaOfInterest` is the first role of a Generic Profile of this register with minOccurs 0: band retrieval
is defined over the whole product as well as over an area (decision C14 of 2026-11-10).

## Source

- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic
  Profile is. The meaning of the operation, and the standards that define it, are its activity type (see the Implementation Profile).

## Relations

- `broader`: [`generic-profiles.concept.data-discovery-and-access`](../../concept/data-discovery-and-access/)
- Refined by (1 Implementation Profile):
- [`band-retrieval`](../../implementation-profile/band-retrieval/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level). A proposal added on 2026-11-10 (decision of 2026-11-10, six new process profiles).

## Examples

### Band retrieval
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval",
  "type": "GenericProfile",
  "prefLabel": "Band retrieval",
  "definition": "Retrieves one band of an Earth observation product as a raster, over the whole product or over an area of interest. A product, a band identifier and an optional bounding box in, one Raster out.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile",
  "hasAction": [
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval"
    }
  ],
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval",
  "itemClass": "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/generic-profile",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "broader": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/data-discovery-and-access"
  ],
  "keywords": [
    "product",
    "band",
    "retrieval"
  ],
  "metadata": [
    {
      "title": "Process Concept: Data Discovery and Access",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/data-discovery-and-access"
    }
  ],
  "inputs": {
    "product": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/inputs/product",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/eo-product",
      "title": "Earth observation product",
      "description": "the product the band belongs to",
      "keywords": [
        "product"
      ]
    },
    "band": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/inputs/band",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/band-identifier",
      "title": "Band identifier",
      "description": "the band to retrieve",
      "keywords": [
        "band"
      ]
    },
    "areaOfInterest": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/inputs/areaOfInterest",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/bounding-box",
      "title": "Bounding box",
      "description": "the area to retrieve; the whole product when absent",
      "keywords": [
        "bounding box"
      ],
      "minOccurs": 0
    }
  },
  "outputs": {
    "raster": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/outputs/raster",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/raster",
      "title": "Raster",
      "description": "the retrieved band",
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
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/band-retrieval/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval",
  "type": "GenericProfile",
  "prefLabel": "Band retrieval",
  "definition": "Retrieves one band of an Earth observation product as a raster, over the whole product or over an area of interest. A product, a band identifier and an optional bounding box in, one Raster out.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile",
  "hasAction": [
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval"
    }
  ],
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval",
  "itemClass": "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/generic-profile",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "broader": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/data-discovery-and-access"
  ],
  "keywords": [
    "product",
    "band",
    "retrieval"
  ],
  "metadata": [
    {
      "title": "Process Concept: Data Discovery and Access",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/data-discovery-and-access"
    }
  ],
  "inputs": {
    "product": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/inputs/product",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/eo-product",
      "title": "Earth observation product",
      "description": "the product the band belongs to",
      "keywords": [
        "product"
      ]
    },
    "band": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/inputs/band",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/band-identifier",
      "title": "Band identifier",
      "description": "the band to retrieve",
      "keywords": [
        "band"
      ]
    },
    "areaOfInterest": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/inputs/areaOfInterest",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/bounding-box",
      "title": "Bounding box",
      "description": "the area to retrieve; the whole product when absent",
      "keywords": [
        "bounding box"
      ],
      "minOccurs": 0
    }
  },
  "outputs": {
    "raster": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/outputs/raster",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/raster",
      "title": "Raster",
      "description": "the retrieved band",
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

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval> a gp:GenericProfile ;
    skos:broader <https://geolabs.github.io/bblocks-generic-profiles/def/concept/data-discovery-and-access> ;
    skos:definition "Retrieves one band of an Earth observation product as a raster, over the whole product or over an area of interest. A product, a band identifier and an optional bounding box in, one Raster out." ;
    skos:inScheme gp:generic-profile ;
    skos:prefLabel "Band retrieval" ;
    gp:inputs [ ns2:areaOfInterest <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/inputs/areaOfInterest> ;
            ns2:band <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/inputs/band> ;
            ns2:product <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/inputs/product> ] ;
    gp:outputs [ ns1:raster <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/outputs/raster> ] ;
    proc:keywords "band",
        "product",
        "retrieval" ;
    proc:metadata [ dcterms:title "Process Concept: Data Discovery and Access" ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] ;
    rim:hasAction <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/actions/addition> ;
    rim:inRegister gp:register ;
    rim:itemClass <https://geolabs.github.io/bblocks-generic-profiles/def/item-class/generic-profile> ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:invalid .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/actions/addition> a rim:RegisterAction ;
    prov:startedAtTime "2026-11-10T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType rim:additionAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval> ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/inputs/areaOfInterest> dcterms:description "the area to retrieve; the whole product when absent" ;
    dcterms:title "Bounding box" ;
    dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/bounding-box> ;
    proc:keywords "bounding box" ;
    proc:minOccurs 0 .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/inputs/band> dcterms:description "the band to retrieve" ;
    dcterms:title "Band identifier" ;
    dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/band-identifier> ;
    proc:keywords "band" .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/inputs/product> dcterms:description "the product the band belongs to" ;
    dcterms:title "Earth observation product" ;
    dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/eo-product> ;
    proc:keywords "product" .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/outputs/raster> dcterms:description "the retrieved band" ;
    dcterms:title "Raster" ;
    dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/raster> ;
    proc:keywords "raster" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Generic Profile "Band retrieval" -- see generic-profiles.generic-profile
  for the general shape every Generic Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval
      x-jsonld-id: '@id'
    type:
      const: GenericProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Band retrieval
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/concept/data-discovery-and-access
      x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
    inputs:
      required:
      - product
      - band
      - areaOfInterest
      properties:
        product:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/inputs/product
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-data-types/def/data-type/eo-product
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
        band:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/inputs/band
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-data-types/def/data-type/band-identifier
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
        areaOfInterest:
          required:
          - id
          - dataType
          - minOccurs
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/inputs/areaOfInterest
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-data-types/def/data-type/bounding-box
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
            minOccurs:
              const: 0
              x-jsonld-id: https://w3id.org/ogc/api/processes/minOccurs
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/inputs/
    outputs:
      required:
      - raster
      properties:
        raster:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/band-retrieval/outputs/raster
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
  itemIdentifier: generic-profiles.generic-profile.band-retrieval
  register: https://geolabs.github.io/bblocks-generic-profiles/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-12'

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/band-retrieval/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/band-retrieval/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/band-retrieval/context.jsonld)

## Sources

* [OGC 14-065 WPS 2.0.2 Interface Standard Corrigendum 2, §7.5.2 Generic Process Profile](https://docs.ogc.org/is/14-065/14-065.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/generic-profile/band-retrieval`

