
# Activity type: Band retrieval (Schema)

`generic-profiles.activity-type.band-retrieval` *v0.1*

Retrieves one band, one range component, of an Earth observation product as a raster, over the whole product or over an area of interest, with the values the product provides, possibly converted to physical units by the scale and offset the product declares.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Activity type: **Band retrieval**.

> Retrieves one band, one range component, of an Earth observation product as a raster, over the whole product or over an area of interest, with the values the product provides, possibly converted to physical units by the scale and offset the product declares.

## The item

`https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/band-retrieval` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate spatial data, declared with GeoSPARQL 1.1 classes: `usedEntityType` `geo:Feature`; `generatedEntityType` `geo:Feature`. The class is chosen per kind of role (see `scripts/activity-types.yaml`); how a data type of `bblocks-data-types` maps to an entity type is still open (decision D8, question 5).

The run of an activity of this type is not typed here (decision D8, open).

## Sources

- [OGC 12-040 Web Coverage Service Interface Standard - Range Subsetting Extension 1.0, §1 Scope (retrieval of selected range components of a coverage)](https://portal.ogc.org/files/12-040)
- [OGC 09-110r4 WCS 2.0 Interface Standard - Core, version 2.0.1, §4.5 (coverage) trimming and §8.4.1 GetCoverage request (domain subsetting)](https://portal.ogc.org/files/09-110r4)

## Profiles of this operation

The Implementation Profile [`generic-profiles.implementation-profile.band-retrieval`](../../implementation-profile/band-retrieval/) points here with `activityType`. It holds the signature and the representations; this item holds the meaning.

## Examples

### Band retrieval
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/band-retrieval",
  "type": [
    "ActivityType",
    "Class"
  ],
  "prefLabel": "Band retrieval",
  "definition": "Retrieves one band, one range component, of an Earth observation product as a raster, over the whole product or over an area of interest, with the values the product provides, possibly converted to physical units by the scale and offset the product declares.",
  "subClassOf": "https://w3id.org/ogc/rim/geoprocessing/GeoprocessingActivityType",
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/band-retrieval",
  "itemClass": "https://w3id.org/ogc/rim/activity-type/activityTypeItemClass",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "hasAction": {
    "id": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/band-retrieval/actions/addition",
    "type": "RegisterAction",
    "actionType": "addition",
    "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
    "startedAtTime": "2026-11-10T00:00:00Z",
    "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/band-retrieval"
  },
  "usedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "generatedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "associatedAgentType": "http://www.w3.org/ns/prov#SoftwareAgent",
  "source": [
    {
      "title": "OGC 12-040 Web Coverage Service Interface Standard - Range Subsetting Extension 1.0, §1 Scope (retrieval of selected range components of a coverage)",
      "link": "https://portal.ogc.org/files/12-040"
    },
    {
      "title": "OGC 09-110r4 WCS 2.0 Interface Standard - Core, version 2.0.1, §4.5 (coverage) trimming and §8.4.1 GetCoverage request (domain subsetting)",
      "link": "https://portal.ogc.org/files/09-110r4"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/activity-type/band-retrieval/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/band-retrieval",
  "type": [
    "ActivityType",
    "Class"
  ],
  "prefLabel": "Band retrieval",
  "definition": "Retrieves one band, one range component, of an Earth observation product as a raster, over the whole product or over an area of interest, with the values the product provides, possibly converted to physical units by the scale and offset the product declares.",
  "subClassOf": "https://w3id.org/ogc/rim/geoprocessing/GeoprocessingActivityType",
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/band-retrieval",
  "itemClass": "https://w3id.org/ogc/rim/activity-type/activityTypeItemClass",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "hasAction": {
    "id": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/band-retrieval/actions/addition",
    "type": "RegisterAction",
    "actionType": "addition",
    "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
    "startedAtTime": "2026-11-10T00:00:00Z",
    "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/band-retrieval"
  },
  "usedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "generatedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "associatedAgentType": "http://www.w3.org/ns/prov#SoftwareAgent",
  "source": [
    {
      "title": "OGC 12-040 Web Coverage Service Interface Standard - Range Subsetting Extension 1.0, \u00a71 Scope (retrieval of selected range components of a coverage)",
      "link": "https://portal.ogc.org/files/12-040"
    },
    {
      "title": "OGC 09-110r4 WCS 2.0 Interface Standard - Core, version 2.0.1, \u00a74.5 (coverage) trimming and \u00a78.4.1 GetCoverage request (domain subsetting)",
      "link": "https://portal.ogc.org/files/09-110r4"
    }
  ]
}
```

#### ttl
```ttl
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix gp: <https://geolabs.github.io/bblocks-generic-profiles/def/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/band-retrieval> a owl:Class,
        acttype:ActivityType ;
    dcterms:source [ dcterms:references <https://portal.ogc.org/files/12-040> ;
            dcterms:title "OGC 12-040 Web Coverage Service Interface Standard - Range Subsetting Extension 1.0, §1 Scope (retrieval of selected range components of a coverage)" ],
        [ dcterms:references <https://portal.ogc.org/files/09-110r4> ;
            dcterms:title "OGC 09-110r4 WCS 2.0 Interface Standard - Core, version 2.0.1, §4.5 (coverage) trimming and §8.4.1 GetCoverage request (domain subsetting)" ] ;
    rdfs:subClassOf <https://w3id.org/ogc/rim/geoprocessing/GeoprocessingActivityType> ;
    skos:definition "Retrieves one band, one range component, of an Earth observation product as a raster, over the whole product or over an area of interest, with the values the product provides, possibly converted to physical units by the scale and offset the product declares." ;
    skos:prefLabel "Band retrieval" ;
    acttype:associatedAgentType prov:SoftwareAgent ;
    acttype:generatedEntityType geo:Feature ;
    acttype:usedEntityType geo:Feature ;
    rim:hasAction <https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/band-retrieval/actions/addition> ;
    rim:inRegister gp:register ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/band-retrieval"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:invalid .

<https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/band-retrieval/actions/addition> a rim:RegisterAction ;
    prov:startedAtTime "2026-11-10T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType rim:additionAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/band-retrieval> ;
    rim:proposer gp:geolabs .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The activity type "Band retrieval" -- see generic-profiles.activity-type
  for the shape every activity type of this register shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/activity-type/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/band-retrieval
      x-jsonld-id: '@id'
    prefLabel:
      const: Band retrieval
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
    subClassOf:
      const: https://w3id.org/ogc/rim/geoprocessing/GeoprocessingActivityType
      x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#subClassOf
      x-jsonld-type: '@id'
x-jsonld-extra-terms:
  type: '@type'
  ActivityType: https://w3id.org/ogc/rim/activity-type/ActivityType
  Class: http://www.w3.org/2002/07/owl#Class
  altLabel: http://www.w3.org/2004/02/skos/core#altLabel
  definition: http://www.w3.org/2004/02/skos/core#definition
  usedEntityType:
    x-jsonld-id: https://w3id.org/ogc/rim/activity-type/usedEntityType
    x-jsonld-type: '@id'
  generatedEntityType:
    x-jsonld-id: https://w3id.org/ogc/rim/activity-type/generatedEntityType
    x-jsonld-type: '@id'
  associatedAgentType:
    x-jsonld-id: https://w3id.org/ogc/rim/activity-type/associatedAgentType
    x-jsonld-type: '@id'
  source: http://purl.org/dc/terms/source
  title: http://purl.org/dc/terms/title
  link:
    x-jsonld-id: http://purl.org/dc/terms/references
    x-jsonld-type: '@id'
x-jsonld-prefixes:
  acttype: https://w3id.org/ogc/rim/activity-type/
  owl: http://www.w3.org/2002/07/owl#
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  skos: http://www.w3.org/2004/02/skos/core#
  dct: http://purl.org/dc/terms/
  gp: https://geolabs.github.io/bblocks-generic-profiles/def/
x-bblocks-metadata:
  itemIdentifier: generic-profiles.activity-type.band-retrieval
  register: https://geolabs.github.io/bblocks-generic-profiles/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-12'

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/activity-type/band-retrieval/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/activity-type/band-retrieval/schema.yaml)


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
    "usedEntityType": {
      "@id": "rim:activity-type/usedEntityType",
      "@type": "@id"
    },
    "generatedEntityType": {
      "@id": "rim:activity-type/generatedEntityType",
      "@type": "@id"
    },
    "associatedAgentType": {
      "@id": "rim:activity-type/associatedAgentType",
      "@type": "@id"
    },
    "informedByActivityType": {
      "@id": "rim:activity-type/informedByActivityType",
      "@type": "@id"
    },
    "altLabel": "skos:altLabel",
    "subClassOf": {
      "@id": "rdfs:subClassOf",
      "@type": "@id"
    },
    "source": "dct:source",
    "ActivityType": "rim:activity-type/ActivityType",
    "Class": "owl:Class",
    "link": {
      "@id": "dct:references",
      "@type": "@id"
    },
    "rim": "https://w3id.org/ogc/rim/",
    "prov": "http://www.w3.org/ns/prov#",
    "dct": "http://purl.org/dc/terms/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "acttype": "rim:activity-type/",
    "gp": "https://geolabs.github.io/bblocks-generic-profiles/def/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/activity-type/band-retrieval/context.jsonld)

## Sources

* [OGC 12-040 Web Coverage Service Interface Standard - Range Subsetting Extension 1.0, §1 Scope (retrieval of selected range components of a coverage)](https://portal.ogc.org/files/12-040)
* [OGC 09-110r4 WCS 2.0 Interface Standard - Core, version 2.0.1, §4.5 (coverage) trimming and §8.4.1 GetCoverage request (domain subsetting)](https://portal.ogc.org/files/09-110r4)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/activity-type/band-retrieval`

