
# Generic Profile: Point cloud to features (Schema)

`generic-profiles.generic-profile.point-cloud-to-features` *v0.1*

Converts a point cloud to a feature collection. One point cloud in, one feature collection out.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Generic Profile: **Point cloud to features**.

> Converts a point cloud to a feature collection. One point cloud in, one feature collection out.

## Signature

| | Name | Data type | Description |
|---|---|---|---|
| input | `points` | [`point-cloud`](../../data-type/) | the input point cloud |
| output | `result` | [`feature-collection`](../../data-type/) | one feature per point, its attributes as feature attributes |

## Source

- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic Profile is.
- The operations below are each grounded in their own SAGA 7.3.0 tool documentation (see each
  Implementation Profile).

## Relations

- `broader`: [`generic-profiles.concept.point-cloud-processing`](../../concept/point-cloud-processing/)
- Refined by (1 Implementation Profile): [`point-cloud-to-shapes`](../../implementation-profile/point-cloud-to-shapes/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).

## Examples

### Point cloud to features
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features",
  "type": "GenericProfile",
  "prefLabel": "Point cloud to features",
  "definition": "Converts a point cloud to a feature collection. One point cloud in, one feature collection out.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile",
  "hasAction": {
    "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features/actions/addition",
    "type": "RegisterAction",
    "actionType": "addition",
    "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
    "startedAtTime": "2026-10-08T00:00:00Z",
    "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features"
  },
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features",
  "itemClass": "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/generic-profile",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "broader": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/point-cloud-processing"
  ],
  "keywords": [
    "point cloud",
    "feature collection",
    "conversion"
  ],
  "metadata": [
    {
      "title": "Process Concept: Point Cloud Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/point-cloud-processing"
    }
  ],
  "inputs": {
    "points": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features/inputs/points",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/point-cloud",
      "title": "Point cloud",
      "description": "the input point cloud",
      "keywords": [
        "point cloud"
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features/outputs/result",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/feature-collection",
      "title": "Feature collection",
      "description": "one feature per point, its attributes as feature attributes",
      "keywords": [
        "feature collection"
      ]
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/point-cloud-to-features/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features",
  "type": "GenericProfile",
  "prefLabel": "Point cloud to features",
  "definition": "Converts a point cloud to a feature collection. One point cloud in, one feature collection out.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile",
  "hasAction": {
    "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features/actions/addition",
    "type": "RegisterAction",
    "actionType": "addition",
    "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
    "startedAtTime": "2026-10-08T00:00:00Z",
    "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features"
  },
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features",
  "itemClass": "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/generic-profile",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "broader": [
    "https://geolabs.github.io/bblocks-generic-profiles/def/concept/point-cloud-processing"
  ],
  "keywords": [
    "point cloud",
    "feature collection",
    "conversion"
  ],
  "metadata": [
    {
      "title": "Process Concept: Point Cloud Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/point-cloud-processing"
    }
  ],
  "inputs": {
    "points": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features/inputs/points",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/point-cloud",
      "title": "Point cloud",
      "description": "the input point cloud",
      "keywords": [
        "point cloud"
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features/outputs/result",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/feature-collection",
      "title": "Feature collection",
      "description": "one feature per point, its attributes as feature attributes",
      "keywords": [
        "feature collection"
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

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features> a gp:GenericProfile ;
    skos:broader <https://geolabs.github.io/bblocks-generic-profiles/def/concept/point-cloud-processing> ;
    skos:definition "Converts a point cloud to a feature collection. One point cloud in, one feature collection out." ;
    skos:inScheme gp:generic-profile ;
    skos:prefLabel "Point cloud to features" ;
    gp:inputs [ ns2:points <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features/inputs/points> ] ;
    gp:outputs [ ns1:result <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features/outputs/result> ] ;
    proc:keywords "conversion",
        "feature collection",
        "point cloud" ;
    proc:metadata [ dcterms:title "Process Concept: Point Cloud Processing" ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] ;
    rim:hasAction <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features/actions/addition> ;
    rim:inRegister gp:register ;
    rim:itemClass <https://geolabs.github.io/bblocks-generic-profiles/def/item-class/generic-profile> ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:invalid .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features/actions/addition> a rim:RegisterAction ;
    prov:startedAtTime "2026-10-08T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType rim:additionAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features> ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features/inputs/points> dcterms:description "the input point cloud" ;
    dcterms:title "Point cloud" ;
    dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/point-cloud> ;
    proc:keywords "point cloud" .

<https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features/outputs/result> dcterms:description "one feature per point, its attributes as feature attributes" ;
    dcterms:title "Feature collection" ;
    dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/feature-collection> ;
    proc:keywords "feature collection" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Generic Profile "Point cloud to features" -- see generic-profiles.generic-profile
  for the general shape every Generic Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features
      x-jsonld-id: '@id'
    type:
      const: GenericProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Point cloud to features
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/concept/point-cloud-processing
      x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
    inputs:
      properties:
        points:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features/inputs/points
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-data-types/def/data-type/point-cloud
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/inputs/
    outputs:
      properties:
        result:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features/outputs/result
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-data-types/def/data-type/feature-collection
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
  itemIdentifier: generic-profiles.generic-profile.point-cloud-to-features
  register: https://geolabs.github.io/bblocks-generic-profiles/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-04'

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/point-cloud-to-features/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/point-cloud-to-features/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/point-cloud-to-features/context.jsonld)

## Sources

* [ZOO-Project process-profiles: Concept / Generic Profile / Implementation Profile](https://zoo-project.github.io/docs/services/process-profiles.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/generic-profile/point-cloud-to-features`

