
# Activity type: Product selection (Schema)

`generic-profiles.activity-type.product-selection` *v0.1*

Selects, from a catalogue of Earth observation products, those of a collection whose footprint intersects an area of interest and whose acquisition time falls within a time interval, possibly filtered further on their metadata, such as their cloud cover.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Activity type: **Product selection**.

> Selects, from a catalogue of Earth observation products, those of a collection whose footprint intersects an area of interest and whose acquisition time falls within a time interval, possibly filtered further on their metadata, such as their cloud cover.

## The item

`https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of the family [`generic-profiles.activity-type.catalogue-search`](../catalogue-search/) (decision of 2026-11-19), itself a sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate spatial data, declared with GeoSPARQL 1.1 classes: `usedEntityType` `geo:Geometry`; `generatedEntityType` `geo:Feature`. The class is chosen per kind of role (see `scripts/activity-types.yaml`); how a data type of `bblocks-data-types` maps to an entity type is still open (decision D8, question 5).

The run of an activity of this type is not typed here (decision D8, open).

## Sources

- [OGC 13-026r9 OpenSearch Extension for Earth Observation 1.1, §1 Scope and the parameters for the discovery of products (parentIdentifier, cloudCover)](https://docs.ogc.org/is/13-026r9/13-026r9.html)
- [OGC 17-069r4 OGC API - Features - Part 1: Core, §7.15.3 Parameter bbox and §7.15.4 Parameter datetime](https://docs.ogc.org/is/17-069r4/17-069r4.html)
- [STAC API - Item Search 1.0.0 (community specification), parameters bbox, intersects, datetime and collections](https://github.com/radiantearth/stac-api-spec/blob/v1.0.0/item-search/README.md)

## Notes

It passes the geoprocessing shapes through its area of interest, and the search is a spatial query (a footprint intersects an area), but nothing geographic is computed or produced; the products may be returned as references. Whether a parent for discovery and access outside geoprocessing should be used is asked to the maintainers (question 5, decision C10 of 2026-11-10).

## Profiles of this operation

The Implementation Profile [`generic-profiles.implementation-profile.product-selection`](../../implementation-profile/product-selection/) points here with `activityType`. It holds the signature and the representations; this item holds the meaning.

## Examples

### Product selection
#### json
```json
{
  "id": "https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection",
  "type": [
    "ActivityType",
    "Class"
  ],
  "prefLabel": "Product selection",
  "definition": "Selects, from a catalogue of Earth observation products, those of a collection whose footprint intersects an area of interest and whose acquisition time falls within a time interval, possibly filtered further on their metadata, such as their cloud cover.",
  "subClassOf": "https://w3id.org/geolabs/ospd/generic-profiles/activity-type/catalogue-search",
  "objectIdentifier": "https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection",
  "itemClass": "https://w3id.org/ogc/rim/activity-type/activityTypeItemClass",
  "inRegister": "https://w3id.org/geolabs/ospd/generic-profiles/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "sameAs": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/product-selection",
  "hasAction": [
    {
      "id": "https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://w3id.org/geolabs/ospd/org/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection"
    },
    {
      "id": "https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection/actions/identifier-2026-11-17",
      "type": "RegisterAction",
      "actionType": "https://w3id.org/geolabs/ospd/generic-profiles/amendmentAction",
      "changeClassification": "clarifying",
      "affectedProperty": "https://w3id.org/ogc/rim/objectIdentifier",
      "description": "The object identifier of this item moves from https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/product-selection to https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection, which resolves through w3id.org (decision of 2026-11-17); the register actions of the item move with it, under https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection/actions/. The old IRI is kept as owl:sameAs. The content of the item is unchanged. Classified clarifying: the item is the same, only its identifier changes.",
      "proposer": "https://w3id.org/geolabs/ospd/org/geolabs",
      "startedAtTime": "2026-11-17T00:00:00Z",
      "appliesTo": "https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection"
    },
    {
      "id": "https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection/actions/family-2026-11-19",
      "type": "RegisterAction",
      "actionType": "https://w3id.org/geolabs/ospd/generic-profiles/amendmentAction",
      "changeClassification": "substantive",
      "affectedProperty": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
      "description": "The parent class (rdfs:subClassOf) changes from https://w3id.org/ogc/rim/geoprocessing/GeoprocessingActivityType to the family https://w3id.org/geolabs/ospd/generic-profiles/activity-type/catalogue-search, itself a sub-class of it (decision of 2026-11-19: activity types grouped by meaning). The definition and the entity types are unchanged. Classified substantive, a change of parent class.",
      "proposer": "https://w3id.org/geolabs/ospd/org/geolabs",
      "startedAtTime": "2026-11-19T00:00:00Z",
      "appliesTo": "https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection"
    }
  ],
  "usedEntityType": "http://www.opengis.net/ont/geosparql#Geometry",
  "generatedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "associatedAgentType": "http://www.w3.org/ns/prov#SoftwareAgent",
  "source": [
    {
      "title": "OGC 13-026r9 OpenSearch Extension for Earth Observation 1.1, §1 Scope and the parameters for the discovery of products (parentIdentifier, cloudCover)",
      "link": "https://docs.ogc.org/is/13-026r9/13-026r9.html"
    },
    {
      "title": "OGC 17-069r4 OGC API - Features - Part 1: Core, §7.15.3 Parameter bbox and §7.15.4 Parameter datetime",
      "link": "https://docs.ogc.org/is/17-069r4/17-069r4.html"
    },
    {
      "title": "STAC API - Item Search 1.0.0 (community specification), parameters bbox, intersects, datetime and collections",
      "link": "https://github.com/radiantearth/stac-api-spec/blob/v1.0.0/item-search/README.md"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/activity-type/product-selection/context.jsonld",
  "id": "https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection",
  "type": [
    "ActivityType",
    "Class"
  ],
  "prefLabel": "Product selection",
  "definition": "Selects, from a catalogue of Earth observation products, those of a collection whose footprint intersects an area of interest and whose acquisition time falls within a time interval, possibly filtered further on their metadata, such as their cloud cover.",
  "subClassOf": "https://w3id.org/geolabs/ospd/generic-profiles/activity-type/catalogue-search",
  "objectIdentifier": "https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection",
  "itemClass": "https://w3id.org/ogc/rim/activity-type/activityTypeItemClass",
  "inRegister": "https://w3id.org/geolabs/ospd/generic-profiles/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "sameAs": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/product-selection",
  "hasAction": [
    {
      "id": "https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://w3id.org/geolabs/ospd/org/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection"
    },
    {
      "id": "https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection/actions/identifier-2026-11-17",
      "type": "RegisterAction",
      "actionType": "https://w3id.org/geolabs/ospd/generic-profiles/amendmentAction",
      "changeClassification": "clarifying",
      "affectedProperty": "https://w3id.org/ogc/rim/objectIdentifier",
      "description": "The object identifier of this item moves from https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/product-selection to https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection, which resolves through w3id.org (decision of 2026-11-17); the register actions of the item move with it, under https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection/actions/. The old IRI is kept as owl:sameAs. The content of the item is unchanged. Classified clarifying: the item is the same, only its identifier changes.",
      "proposer": "https://w3id.org/geolabs/ospd/org/geolabs",
      "startedAtTime": "2026-11-17T00:00:00Z",
      "appliesTo": "https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection"
    },
    {
      "id": "https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection/actions/family-2026-11-19",
      "type": "RegisterAction",
      "actionType": "https://w3id.org/geolabs/ospd/generic-profiles/amendmentAction",
      "changeClassification": "substantive",
      "affectedProperty": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
      "description": "The parent class (rdfs:subClassOf) changes from https://w3id.org/ogc/rim/geoprocessing/GeoprocessingActivityType to the family https://w3id.org/geolabs/ospd/generic-profiles/activity-type/catalogue-search, itself a sub-class of it (decision of 2026-11-19: activity types grouped by meaning). The definition and the entity types are unchanged. Classified substantive, a change of parent class.",
      "proposer": "https://w3id.org/geolabs/ospd/org/geolabs",
      "startedAtTime": "2026-11-19T00:00:00Z",
      "appliesTo": "https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection"
    }
  ],
  "usedEntityType": "http://www.opengis.net/ont/geosparql#Geometry",
  "generatedEntityType": "http://www.opengis.net/ont/geosparql#Feature",
  "associatedAgentType": "http://www.w3.org/ns/prov#SoftwareAgent",
  "source": [
    {
      "title": "OGC 13-026r9 OpenSearch Extension for Earth Observation 1.1, \u00a71 Scope and the parameters for the discovery of products (parentIdentifier, cloudCover)",
      "link": "https://docs.ogc.org/is/13-026r9/13-026r9.html"
    },
    {
      "title": "OGC 17-069r4 OGC API - Features - Part 1: Core, \u00a77.15.3 Parameter bbox and \u00a77.15.4 Parameter datetime",
      "link": "https://docs.ogc.org/is/17-069r4/17-069r4.html"
    },
    {
      "title": "STAC API - Item Search 1.0.0 (community specification), parameters bbox, intersects, datetime and collections",
      "link": "https://github.com/radiantearth/stac-api-spec/blob/v1.0.0/item-search/README.md"
    }
  ]
}
```

#### ttl
```ttl
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix gp: <https://w3id.org/geolabs/ospd/generic-profiles/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection/actions/addition> a rim:RegisterAction ;
    prov:startedAtTime "2026-11-10T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType rim:additionAction ;
    rim:appliesTo <https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection> ;
    rim:proposer <https://w3id.org/geolabs/ospd/org/geolabs> .

<https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection/actions/family-2026-11-19> a rim:RegisterAction ;
    dcterms:description "The parent class (rdfs:subClassOf) changes from https://w3id.org/ogc/rim/geoprocessing/GeoprocessingActivityType to the family https://w3id.org/geolabs/ospd/generic-profiles/activity-type/catalogue-search, itself a sub-class of it (decision of 2026-11-19: activity types grouped by meaning). The definition and the entity types are unchanged. Classified substantive, a change of parent class." ;
    prov:startedAtTime "2026-11-19T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType gp:amendmentAction ;
    rim:affectedProperty rdfs:subClassOf ;
    rim:appliesTo <https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer <https://w3id.org/geolabs/ospd/org/geolabs> .

<https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection/actions/identifier-2026-11-17> a rim:RegisterAction ;
    dcterms:description "The object identifier of this item moves from https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/product-selection to https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection, which resolves through w3id.org (decision of 2026-11-17); the register actions of the item move with it, under https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection/actions/. The old IRI is kept as owl:sameAs. The content of the item is unchanged. Classified clarifying: the item is the same, only its identifier changes." ;
    prov:startedAtTime "2026-11-17T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType gp:amendmentAction ;
    rim:affectedProperty rim:objectIdentifier ;
    rim:appliesTo <https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection> ;
    rim:changeClassification rim:clarifyingChange ;
    rim:proposer <https://w3id.org/geolabs/ospd/org/geolabs> .

<https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection> a owl:Class,
        acttype:ActivityType ;
    dcterms:source [ dcterms:references <https://github.com/radiantearth/stac-api-spec/blob/v1.0.0/item-search/README.md> ;
            dcterms:title "STAC API - Item Search 1.0.0 (community specification), parameters bbox, intersects, datetime and collections" ],
        [ dcterms:references <https://docs.ogc.org/is/13-026r9/13-026r9.html> ;
            dcterms:title "OGC 13-026r9 OpenSearch Extension for Earth Observation 1.1, §1 Scope and the parameters for the discovery of products (parentIdentifier, cloudCover)" ],
        [ dcterms:references <https://docs.ogc.org/is/17-069r4/17-069r4.html> ;
            dcterms:title "OGC 17-069r4 OGC API - Features - Part 1: Core, §7.15.3 Parameter bbox and §7.15.4 Parameter datetime" ] ;
    rdfs:subClassOf <https://w3id.org/geolabs/ospd/generic-profiles/activity-type/catalogue-search> ;
    owl:sameAs <https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/product-selection> ;
    skos:definition "Selects, from a catalogue of Earth observation products, those of a collection whose footprint intersects an area of interest and whose acquisition time falls within a time interval, possibly filtered further on their metadata, such as their cloud cover." ;
    skos:prefLabel "Product selection" ;
    acttype:associatedAgentType prov:SoftwareAgent ;
    acttype:generatedEntityType geo:Feature ;
    acttype:usedEntityType geo:Geometry ;
    rim:hasAction <https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection/actions/addition>,
        <https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection/actions/family-2026-11-19>,
        <https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection/actions/identifier-2026-11-17> ;
    rim:inRegister gp:register ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:invalid .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The activity type "Product selection" -- see generic-profiles.activity-type
  for the shape every activity type of this register shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/activity-type/schema.yaml
- type: object
  properties:
    id:
      const: https://w3id.org/geolabs/ospd/generic-profiles/activity-type/product-selection
      x-jsonld-id: '@id'
    prefLabel:
      const: Product selection
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
    subClassOf:
      const: https://w3id.org/geolabs/ospd/generic-profiles/activity-type/catalogue-search
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
  sameAs:
    x-jsonld-id: http://www.w3.org/2002/07/owl#sameAs
    x-jsonld-type: '@id'
  affectedProperty:
    x-jsonld-id: https://w3id.org/ogc/rim/affectedProperty
    x-jsonld-type: '@id'
  isReplacedBy:
    x-jsonld-id: http://purl.org/dc/terms/isReplacedBy
    x-jsonld-type: '@id'
x-jsonld-prefixes:
  acttype: https://w3id.org/ogc/rim/activity-type/
  owl: http://www.w3.org/2002/07/owl#
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  skos: http://www.w3.org/2004/02/skos/core#
  dct: http://purl.org/dc/terms/
  gp: https://w3id.org/geolabs/ospd/generic-profiles/
x-bblocks-metadata:
  itemIdentifier: generic-profiles.activity-type.product-selection
  register: https://geolabs.github.io/bblocks-generic-profiles/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-25'

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/activity-type/product-selection/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/activity-type/product-selection/schema.yaml)


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
    "sameAs": {
      "@id": "owl:sameAs",
      "@type": "@id"
    },
    "affectedProperty": {
      "@id": "rim:affectedProperty",
      "@type": "@id"
    },
    "isReplacedBy": {
      "@id": "dct:isReplacedBy",
      "@type": "@id"
    },
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
    "gp": "https://w3id.org/geolabs/ospd/generic-profiles/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/activity-type/product-selection/context.jsonld)

## Sources

* [OGC 13-026r9 OpenSearch Extension for Earth Observation 1.1, §1 Scope and the parameters for the discovery of products (parentIdentifier, cloudCover)](https://docs.ogc.org/is/13-026r9/13-026r9.html)
* [OGC 17-069r4 OGC API - Features - Part 1: Core, §7.15.3 Parameter bbox and §7.15.4 Parameter datetime](https://docs.ogc.org/is/17-069r4/17-069r4.html)
* [STAC API - Item Search 1.0.0 (community specification), parameters bbox, intersects, datetime and collections](https://github.com/radiantearth/stac-api-spec/blob/v1.0.0/item-search/README.md)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/activity-type/product-selection`

