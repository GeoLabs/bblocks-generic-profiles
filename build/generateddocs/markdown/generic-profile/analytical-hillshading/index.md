
# Generic Profile: Analytical hillshading (Schema)

`generic-profiles.generic-profile.analytical-hillshading` *v0.1*

Computes how the terrain is lit by a light source. One elevation model and the light source's azimuth and altitude in, one single-band raster out.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Generic Profile: **Analytical hillshading**.

> Computes how the terrain is lit by a light source. One elevation model and the light source's azimuth and altitude in, one single-band raster out.

## Signature

| | Name | Data type | Description |
|---|---|---|---|
| input | `elevation` | [`elevation-model`](../../data-type/) | the elevation model |
| input | `azimuth` | [`number`](../../data-type/) | the light source's direction, in degrees clockwise from north |
| input | `altitude` | [`number`](../../data-type/) | the light source's height above the horizon, in degrees |
| output | `result` | [`raster-single-band`](../../data-type/) | the shaded relief |

## Source

- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic Profile is.
- The operations below are each grounded in their own SAGA 7.3.0 tool documentation (see each
  Implementation Profile).

## Relations

- `broader`: [`generic-profiles.concept.terrain-analysis`](../../concept/terrain-analysis/)
- Refined by (1 Implementation Profile): [`analytical-hillshading`](../../implementation-profile/analytical-hillshading/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).

## Examples

### Analytical hillshading
#### json
```json
{
  "id": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading",
  "type": "GenericProfile",
  "prefLabel": "Analytical hillshading",
  "definition": "Computes how the terrain is lit by a light source. One elevation model and the light source's azimuth and altitude in, one single-band raster out.",
  "inScheme": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile",
  "hasAction": [
    {
      "id": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://w3id.org/geolabs/ospd/generic-profiles/geolabs",
      "startedAtTime": "2026-10-08T00:00:00Z",
      "appliesTo": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading"
    },
    {
      "id": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/actions/identifier-2026-11-17",
      "type": "RegisterAction",
      "actionType": "https://w3id.org/geolabs/ospd/generic-profiles/amendmentAction",
      "changeClassification": "clarifying",
      "affectedProperty": "https://w3id.org/ogc/rim/objectIdentifier",
      "description": "The object identifier of this item moves from https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading to https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading, which resolves through w3id.org (decision of 2026-11-17); the register actions of the item move with it, under https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/actions/. The old IRI is kept as owl:sameAs. The content of the item is unchanged. Classified clarifying: the item is the same, only its identifier changes.",
      "proposer": "https://w3id.org/geolabs/ospd/generic-profiles/geolabs",
      "startedAtTime": "2026-11-17T00:00:00Z",
      "appliesTo": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading"
    }
  ],
  "objectIdentifier": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading",
  "sameAs": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading",
  "itemClass": "https://w3id.org/geolabs/ospd/generic-profiles/item-class/generic-profile",
  "inRegister": "https://w3id.org/geolabs/ospd/generic-profiles/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "broader": [
    "https://w3id.org/geolabs/ospd/generic-profiles/concept/terrain-analysis"
  ],
  "keywords": [
    "terrain",
    "elevation",
    "raster",
    "illumination",
    "hillshade"
  ],
  "metadata": [
    {
      "title": "Process Concept: Terrain Analysis",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://w3id.org/geolabs/ospd/generic-profiles/concept/terrain-analysis"
    }
  ],
  "inputs": {
    "elevation": {
      "id": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/inputs/elevation",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/elevation-model",
      "title": "Elevation model",
      "description": "the elevation model",
      "keywords": [
        "elevation"
      ]
    },
    "azimuth": {
      "id": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/inputs/azimuth",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/number",
      "title": "Number",
      "description": "the light source's direction, in degrees clockwise from north",
      "keywords": [
        "azimuth"
      ]
    },
    "altitude": {
      "id": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/inputs/altitude",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/number",
      "title": "Number",
      "description": "the light source's height above the horizon, in degrees",
      "keywords": [
        "altitude"
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/outputs/result",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "title": "Raster",
      "description": "the shaded relief",
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
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/analytical-hillshading/context.jsonld",
  "id": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading",
  "type": "GenericProfile",
  "prefLabel": "Analytical hillshading",
  "definition": "Computes how the terrain is lit by a light source. One elevation model and the light source's azimuth and altitude in, one single-band raster out.",
  "inScheme": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile",
  "hasAction": [
    {
      "id": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://w3id.org/geolabs/ospd/generic-profiles/geolabs",
      "startedAtTime": "2026-10-08T00:00:00Z",
      "appliesTo": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading"
    },
    {
      "id": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/actions/identifier-2026-11-17",
      "type": "RegisterAction",
      "actionType": "https://w3id.org/geolabs/ospd/generic-profiles/amendmentAction",
      "changeClassification": "clarifying",
      "affectedProperty": "https://w3id.org/ogc/rim/objectIdentifier",
      "description": "The object identifier of this item moves from https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading to https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading, which resolves through w3id.org (decision of 2026-11-17); the register actions of the item move with it, under https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/actions/. The old IRI is kept as owl:sameAs. The content of the item is unchanged. Classified clarifying: the item is the same, only its identifier changes.",
      "proposer": "https://w3id.org/geolabs/ospd/generic-profiles/geolabs",
      "startedAtTime": "2026-11-17T00:00:00Z",
      "appliesTo": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading"
    }
  ],
  "objectIdentifier": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading",
  "sameAs": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading",
  "itemClass": "https://w3id.org/geolabs/ospd/generic-profiles/item-class/generic-profile",
  "inRegister": "https://w3id.org/geolabs/ospd/generic-profiles/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "broader": [
    "https://w3id.org/geolabs/ospd/generic-profiles/concept/terrain-analysis"
  ],
  "keywords": [
    "terrain",
    "elevation",
    "raster",
    "illumination",
    "hillshade"
  ],
  "metadata": [
    {
      "title": "Process Concept: Terrain Analysis",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://w3id.org/geolabs/ospd/generic-profiles/concept/terrain-analysis"
    }
  ],
  "inputs": {
    "elevation": {
      "id": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/inputs/elevation",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/elevation-model",
      "title": "Elevation model",
      "description": "the elevation model",
      "keywords": [
        "elevation"
      ]
    },
    "azimuth": {
      "id": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/inputs/azimuth",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/number",
      "title": "Number",
      "description": "the light source's direction, in degrees clockwise from north",
      "keywords": [
        "azimuth"
      ]
    },
    "altitude": {
      "id": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/inputs/altitude",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/number",
      "title": "Number",
      "description": "the light source's height above the horizon, in degrees",
      "keywords": [
        "altitude"
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/outputs/result",
      "dataType": "https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band",
      "title": "Raster",
      "description": "the shaded relief",
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
@prefix gp: <https://w3id.org/geolabs/ospd/generic-profiles/> .
@prefix ns1: <https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/inputs/> .
@prefix ns2: <https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/outputs/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/actions/addition> a rim:RegisterAction ;
    prov:startedAtTime "2026-10-08T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType rim:additionAction ;
    rim:appliesTo <https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading> ;
    rim:proposer gp:geolabs .

<https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/actions/identifier-2026-11-17> a rim:RegisterAction ;
    dcterms:description "The object identifier of this item moves from https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading to https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading, which resolves through w3id.org (decision of 2026-11-17); the register actions of the item move with it, under https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/actions/. The old IRI is kept as owl:sameAs. The content of the item is unchanged. Classified clarifying: the item is the same, only its identifier changes." ;
    prov:startedAtTime "2026-11-17T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType gp:amendmentAction ;
    rim:affectedProperty rim:objectIdentifier ;
    rim:appliesTo <https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading> ;
    rim:changeClassification rim:clarifyingChange ;
    rim:proposer gp:geolabs .

<https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/inputs/altitude> dcterms:description "the light source's height above the horizon, in degrees" ;
    dcterms:title "Number" ;
    dcterms:type <https://w3id.org/geolabs/ospd/data-types/data-type/number> ;
    proc:keywords "altitude" .

<https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/inputs/azimuth> dcterms:description "the light source's direction, in degrees clockwise from north" ;
    dcterms:title "Number" ;
    dcterms:type <https://w3id.org/geolabs/ospd/data-types/data-type/number> ;
    proc:keywords "azimuth" .

<https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/inputs/elevation> dcterms:description "the elevation model" ;
    dcterms:title "Elevation model" ;
    dcterms:type <https://w3id.org/geolabs/ospd/data-types/data-type/elevation-model> ;
    proc:keywords "elevation" .

<https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/outputs/result> dcterms:description "the shaded relief" ;
    dcterms:title "Raster" ;
    dcterms:type <https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band> ;
    proc:keywords "raster" .

<https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading> a gp:GenericProfile ;
    owl:sameAs <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/analytical-hillshading> ;
    skos:broader <https://w3id.org/geolabs/ospd/generic-profiles/concept/terrain-analysis> ;
    skos:definition "Computes how the terrain is lit by a light source. One elevation model and the light source's azimuth and altitude in, one single-band raster out." ;
    skos:inScheme gp:generic-profile ;
    skos:prefLabel "Analytical hillshading" ;
    gp:inputs [ ns1:altitude <https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/inputs/altitude> ;
            ns1:azimuth <https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/inputs/azimuth> ;
            ns1:elevation <https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/inputs/elevation> ] ;
    gp:outputs [ ns2:result <https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/outputs/result> ] ;
    proc:keywords "elevation",
        "hillshade",
        "illumination",
        "raster",
        "terrain" ;
    proc:metadata [ dcterms:title "Process Concept: Terrain Analysis" ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ] ;
    rim:hasAction <https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/actions/addition>,
        <https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/actions/identifier-2026-11-17> ;
    rim:inRegister gp:register ;
    rim:itemClass <https://w3id.org/geolabs/ospd/generic-profiles/item-class/generic-profile> ;
    rim:objectIdentifier "https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:invalid .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Generic Profile "Analytical hillshading" -- see generic-profiles.generic-profile
  for the general shape every Generic Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading
      x-jsonld-id: '@id'
    type:
      const: GenericProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Analytical hillshading
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
              const: https://w3id.org/geolabs/ospd/generic-profiles/concept/terrain-analysis
      x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
    inputs:
      properties:
        elevation:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/inputs/elevation
              x-jsonld-id: '@id'
            dataType:
              const: https://w3id.org/geolabs/ospd/data-types/data-type/elevation-model
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
        azimuth:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/inputs/azimuth
              x-jsonld-id: '@id'
            dataType:
              const: https://w3id.org/geolabs/ospd/data-types/data-type/number
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
        altitude:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/inputs/altitude
              x-jsonld-id: '@id'
            dataType:
              const: https://w3id.org/geolabs/ospd/data-types/data-type/number
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
      x-jsonld-id: https://w3id.org/geolabs/ospd/generic-profiles/inputs
      x-jsonld-vocab: https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/inputs/
    outputs:
      properties:
        result:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://w3id.org/geolabs/ospd/generic-profiles/generic-profile/analytical-hillshading/outputs/result
              x-jsonld-id: '@id'
            dataType:
              const: https://w3id.org/geolabs/ospd/data-types/data-type/raster-single-band
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
  itemIdentifier: generic-profiles.generic-profile.analytical-hillshading
  register: https://geolabs.github.io/bblocks-generic-profiles/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-18'

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/analytical-hillshading/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/analytical-hillshading/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/generic-profile/analytical-hillshading/context.jsonld)

## Sources

* [ZOO-Project process-profiles: Concept / Generic Profile / Implementation Profile](https://zoo-project.github.io/docs/services/process-profiles.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/generic-profile/analytical-hillshading`

