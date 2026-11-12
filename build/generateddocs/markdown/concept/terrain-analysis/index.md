
# Process Concept: Terrain Analysis (Schema)

`generic-profiles.concept.terrain-analysis` *v0.1*

Operations deriving terrain attributes from an elevation model: local surface derivatives (slope, aspect, curvature), neighbourhood indices (terrain ruggedness, topographic position) and illumination (hillshading) -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 §7.5.1). A kind of raster coverage processing: an elevation model is a single-band raster whose values are elevations.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Process Concept: **Terrain Analysis**.

> Operations deriving terrain attributes from an elevation model: local surface derivatives (slope, aspect, curvature), neighbourhood indices (terrain ruggedness, topographic position) and illumination (hillshading) -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 §7.5.1). A kind of raster coverage processing: an elevation model is a single-band raster whose values are elevations.

## Source

- [SAGA 7.3.0 tool libraries, category Terrain Analysis](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/index.html)
- Wilson, J.P., Gallant, J.C. (2000): Terrain Analysis: Principles and Applications (cited by SAGA's Topographic Position Index tool)

## Relations

- Broader concept of (`broader`): [`terrain-derivative`](../../generic-profile/terrain-derivative/), [`analytical-hillshading`](../../generic-profile/analytical-hillshading/)
- Narrower than [`raster-coverage-processing`](../raster-coverage-processing/) (listed in its `narrower`)

## Register position

Top tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): **Concept** -> Generic Profile ->
Implementation Profile -> Implementation (instance level).

## Examples

### Terrain Analysis
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis",
  "type": "ProcessConcept",
  "prefLabel": "Terrain Analysis",
  "definition": "Operations deriving terrain attributes from an elevation model: local surface derivatives (slope, aspect, curvature), neighbourhood indices (terrain ruggedness, topographic position) and illumination (hillshading) -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 \u00a77.5.1). A kind of raster coverage processing: an elevation model is a single-band raster whose values are elevations.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/concept",
  "hasAction": {
    "id": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis/actions/addition",
    "type": "RegisterAction",
    "actionType": "addition",
    "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
    "startedAtTime": "2026-10-08T00:00:00Z",
    "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis"
  },
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis",
  "itemClass": "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/process-concept",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "source": [
    {
      "title": "SAGA 7.3.0 tool libraries, category Terrain Analysis",
      "link": "https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/index.html"
    },
    {
      "title": "Wilson, J.P., Gallant, J.C. (2000): Terrain Analysis: Principles and Applications (cited by SAGA's Topographic Position Index tool)"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/concept/terrain-analysis/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis",
  "type": "ProcessConcept",
  "prefLabel": "Terrain Analysis",
  "definition": "Operations deriving terrain attributes from an elevation model: local surface derivatives (slope, aspect, curvature), neighbourhood indices (terrain ruggedness, topographic position) and illumination (hillshading) -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 \u00a77.5.1). A kind of raster coverage processing: an elevation model is a single-band raster whose values are elevations.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/concept",
  "hasAction": {
    "id": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis/actions/addition",
    "type": "RegisterAction",
    "actionType": "addition",
    "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
    "startedAtTime": "2026-10-08T00:00:00Z",
    "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis"
  },
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis",
  "itemClass": "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/process-concept",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "source": [
    {
      "title": "SAGA 7.3.0 tool libraries, category Terrain Analysis",
      "link": "https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/index.html"
    },
    {
      "title": "Wilson, J.P., Gallant, J.C. (2000): Terrain Analysis: Principles and Applications (cited by SAGA's Topographic Position Index tool)"
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

<https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis> a gp:ProcessConcept ;
    dcterms:source [ dcterms:references <https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/index.html> ;
            dcterms:title "SAGA 7.3.0 tool libraries, category Terrain Analysis" ],
        [ dcterms:title "Wilson, J.P., Gallant, J.C. (2000): Terrain Analysis: Principles and Applications (cited by SAGA's Topographic Position Index tool)" ] ;
    skos:definition "Operations deriving terrain attributes from an elevation model: local surface derivatives (slope, aspect, curvature), neighbourhood indices (terrain ruggedness, topographic position) and illumination (hillshading) -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 §7.5.1). A kind of raster coverage processing: an elevation model is a single-band raster whose values are elevations." ;
    skos:inScheme gp:concept ;
    skos:prefLabel "Terrain Analysis" ;
    rim:hasAction <https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis/actions/addition> ;
    rim:inRegister gp:register ;
    rim:itemClass <https://geolabs.github.io/bblocks-generic-profiles/def/item-class/process-concept> ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:invalid .

<https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis/actions/addition> a rim:RegisterAction ;
    prov:startedAtTime "2026-10-08T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType rim:additionAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis> ;
    rim:proposer gp:geolabs .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Concept "Terrain Analysis" -- see generic-profiles.concept for the
  general shape every Concept shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/concept/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis
      x-jsonld-id: '@id'
    type:
      const: ProcessConcept
      x-jsonld-id: '@type'
    prefLabel:
      const: Terrain Analysis
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
  itemIdentifier: generic-profiles.concept.terrain-analysis
  register: https://geolabs.github.io/bblocks-generic-profiles/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-12'

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/concept/terrain-analysis/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/concept/terrain-analysis/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/concept/terrain-analysis/context.jsonld)

## Sources

* [OGC 14-065 WPS 2.0.2 Interface Standard Corrigendum 2, §7.5.1 Process Concept](https://docs.ogc.org/is/14-065/14-065.html)
* [SAGA 7.3.0 tool libraries, category Terrain Analysis](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/index.html)
* Wilson, J.P., Gallant, J.C. (2000): Terrain Analysis: Principles and Applications (cited by SAGA's Topographic Position Index tool)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/concept/terrain-analysis`

