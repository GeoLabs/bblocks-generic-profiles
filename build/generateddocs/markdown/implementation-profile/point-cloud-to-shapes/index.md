
# Implementation Profile: Point cloud to shapes (Schema)

`generic-profiles.implementation-profile.point-cloud-to-shapes` *v0.1*

Converts a point cloud to a SAGA shapes layer of points, i.e. a feature collection.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Implementation Profile: **Point cloud to shapes**.

> Converts a point cloud to a SAGA shapes layer of points, i.e. a feature collection.

## Data

- input `points`: `point-cloud`, LAS (OGC 17-030r1); application/vnd.las is the IANA-registered media type
- output `result`: `feature-collection`, GML

The declared format is a minimal default; a real implementation may support others (Table 21,
footnote d). For point clouds, it labels LAS `application/x-ogc-lasf`, not the IANA-registered `application/vnd.las` declared here. For shapes, it also serves KML.

## Source

- [SAGA 7.3.0 -- Point Cloud to Shapes](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/pointcloud_tools_5.html)
- [ZOO-Project Geonovum testbed -- SAGA.pointcloud_tools.5: Point Cloud to Shapes](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.5)

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.point-cloud-to-features`](../../generic-profile/point-cloud-to-features/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.*` in `bblocks-process-profiles` -- a real process of
the ZOO-Project Geonovum testbed.

## Examples

### Point cloud to shapes
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-shapes",
  "type": "ImplementationProfile",
  "prefLabel": "Point cloud to shapes",
  "definition": "Converts a point cloud to a SAGA shapes layer of points, i.e. a feature collection.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "hasAction": {
    "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-shapes/actions/addition",
    "type": "RegisterAction",
    "actionType": "addition",
    "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
    "startedAtTime": "2026-10-08T00:00:00Z",
    "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-shapes"
  },
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-shapes",
  "itemClass": "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/implementation-profile",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features",
  "keywords": [
    "point cloud",
    "feature collection",
    "conversion",
    "Point Cloud to Shapes",
    "pointcloud_tools"
  ],
  "metadata": [
    {
      "title": "Process Concept: Point Cloud Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/point-cloud-processing"
    },
    {
      "title": "Generic Profile: Point cloud to features",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features"
    }
  ],
  "inputs": {
    "points": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-shapes/inputs/points",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/point-cloud",
      "schema": {
        "type": "string",
        "contentEncoding": "base64",
        "contentMediaType": "application/vnd.las",
        "description": "LAS (OGC 17-030r1); application/vnd.las is the IANA-registered media type"
      },
      "keywords": [
        "point cloud",
        "LAS"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Point cloud to features -- input `points`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features/inputs/points"
        }
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-shapes/outputs/result",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/feature-collection",
      "schema": {
        "type": "string",
        "contentMediaType": "text/xml",
        "description": "GML"
      },
      "keywords": [
        "feature collection",
        "GML"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Point cloud to features -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features/outputs/result"
        }
      ]
    }
  },
  "source": [
    {
      "title": "SAGA 7.3.0 -- Point Cloud to Shapes",
      "link": "https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/pointcloud_tools_5.html"
    },
    {
      "title": "ZOO-Project Geonovum testbed -- SAGA.pointcloud_tools.5: Point Cloud to Shapes",
      "link": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.5"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/point-cloud-to-shapes/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-shapes",
  "type": "ImplementationProfile",
  "prefLabel": "Point cloud to shapes",
  "definition": "Converts a point cloud to a SAGA shapes layer of points, i.e. a feature collection.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "hasAction": {
    "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-shapes/actions/addition",
    "type": "RegisterAction",
    "actionType": "addition",
    "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
    "startedAtTime": "2026-10-08T00:00:00Z",
    "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-shapes"
  },
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-shapes",
  "itemClass": "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/implementation-profile",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features",
  "keywords": [
    "point cloud",
    "feature collection",
    "conversion",
    "Point Cloud to Shapes",
    "pointcloud_tools"
  ],
  "metadata": [
    {
      "title": "Process Concept: Point Cloud Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/point-cloud-processing"
    },
    {
      "title": "Generic Profile: Point cloud to features",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features"
    }
  ],
  "inputs": {
    "points": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-shapes/inputs/points",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/point-cloud",
      "schema": {
        "type": "string",
        "contentEncoding": "base64",
        "contentMediaType": "application/vnd.las",
        "description": "LAS (OGC 17-030r1); application/vnd.las is the IANA-registered media type"
      },
      "keywords": [
        "point cloud",
        "LAS"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Point cloud to features -- input `points`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features/inputs/points"
        }
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-shapes/outputs/result",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/feature-collection",
      "schema": {
        "type": "string",
        "contentMediaType": "text/xml",
        "description": "GML"
      },
      "keywords": [
        "feature collection",
        "GML"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Point cloud to features -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features/outputs/result"
        }
      ]
    }
  },
  "source": [
    {
      "title": "SAGA 7.3.0 -- Point Cloud to Shapes",
      "link": "https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/pointcloud_tools_5.html"
    },
    {
      "title": "ZOO-Project Geonovum testbed -- SAGA.pointcloud_tools.5: Point Cloud to Shapes",
      "link": "https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.5"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix gp: <https://geolabs.github.io/bblocks-generic-profiles/def/> .
@prefix ns1: <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/> .
@prefix ns2: <https://w3id.org/ogc/api/schema/> .
@prefix ns3: <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-shapes> a gp:ImplementationProfile ;
    dcterms:source [ dcterms:references <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.5> ;
            dcterms:title "ZOO-Project Geonovum testbed -- SAGA.pointcloud_tools.5: Point Cloud to Shapes" ],
        [ dcterms:references <https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/pointcloud_tools_5.html> ;
            dcterms:title "SAGA 7.3.0 -- Point Cloud to Shapes" ] ;
    skos:definition "Converts a point cloud to a SAGA shapes layer of points, i.e. a feature collection." ;
    skos:inScheme gp:implementation-profile ;
    skos:prefLabel "Point cloud to shapes" ;
    gp:inputs [ ns1:points <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-shapes/inputs/points> ] ;
    gp:outputs [ ns3:result <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-shapes/outputs/result> ] ;
    gp:refinesGenericProfile <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features> ;
    proc:keywords "Point Cloud to Shapes",
        "conversion",
        "feature collection",
        "point cloud",
        "pointcloud_tools" ;
    proc:metadata [ dcterms:title "Process Concept: Point Cloud Processing" ],
        [ dcterms:title "Generic Profile: Point cloud to features" ] ;
    rim:hasAction <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-shapes/actions/addition> ;
    rim:inRegister gp:register ;
    rim:itemClass <https://geolabs.github.io/bblocks-generic-profiles/def/item-class/implementation-profile> ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-shapes"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:invalid .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-shapes/actions/addition> a rim:RegisterAction ;
    prov:startedAtTime "2026-10-08T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType rim:additionAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-shapes> ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-shapes/inputs/points> dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/point-cloud> ;
    proc:keywords "LAS",
        "point cloud" ;
    proc:metadata [ dcterms:title "Generic Profile: Point cloud to features -- input `points`" ;
            ns1:href "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features/inputs/points" ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] ;
    proc:schema [ a ns2:string ;
            dcterms:description "LAS (OGC 17-030r1); application/vnd.las is the IANA-registered media type" ;
            ns2:contentEncoding "base64" ;
            ns2:contentMediaType "application/vnd.las" ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-shapes/outputs/result> dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/feature-collection> ;
    proc:keywords "GML",
        "feature collection" ;
    proc:metadata [ dcterms:title "Generic Profile: Point cloud to features -- output `result`" ;
            ns3:href "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features/outputs/result" ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output> ] ;
    proc:schema [ a ns2:string ;
            dcterms:description "GML" ;
            ns2:contentMediaType "text/xml" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Implementation Profile "Point cloud to shapes" -- see generic-profiles.implementation-profile
  for the general shape every Implementation Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-shapes
      x-jsonld-id: '@id'
    type:
      const: ImplementationProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Point cloud to shapes
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
    refinesGenericProfile:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/refinesGenericProfile
      x-jsonld-type: '@id'
    keywords:
      allOf:
      - contains:
          const: point cloud
      - contains:
          const: feature collection
      - contains:
          const: conversion
      x-jsonld-id: https://w3id.org/ogc/api/processes/keywords
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
      - contains:
          type: object
          required:
          - role
          - href
          properties:
            role:
              const: http://www.opengis.net/spec/wps/2.0/def/process-profile/generic
            href:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features
      x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
    inputs:
      type: object
      required:
      - points
      properties:
        points:
          properties:
            keywords:
              allOf:
              - contains:
                  const: point cloud
              x-jsonld-id: https://w3id.org/ogc/api/processes/keywords
            metadata:
              allOf:
              - contains:
                  type: object
                  required:
                  - role
                  - href
                  properties:
                    role:
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input
                    href:
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features/inputs/points
              x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/
    outputs:
      type: object
      required:
      - result
      properties:
        result:
          properties:
            keywords:
              allOf:
              - contains:
                  const: feature collection
              x-jsonld-id: https://w3id.org/ogc/api/processes/keywords
            metadata:
              allOf:
              - contains:
                  type: object
                  required:
                  - role
                  - href
                  properties:
                    role:
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output
                    href:
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/point-cloud-to-features/outputs/result
              x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/outputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/
- type: object
  properties:
    inputs:
      properties:
        points:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-shapes/inputs/points
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-data-types/def/data-type/point-cloud
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/
    outputs:
      properties:
        result:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/point-cloud-to-shapes/outputs/result
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-data-types/def/data-type/feature-collection
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/outputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/
x-jsonld-extra-terms:
  ImplementationProfile: https://geolabs.github.io/bblocks-generic-profiles/def/ImplementationProfile
  definition: http://www.w3.org/2004/02/skos/core#definition
  inScheme:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#inScheme
    x-jsonld-type: '@id'
  source: http://purl.org/dc/terms/source
  title: http://purl.org/dc/terms/title
  link:
    x-jsonld-id: http://purl.org/dc/terms/references
    x-jsonld-type: '@id'
x-jsonld-prefixes:
  gp: https://geolabs.github.io/bblocks-generic-profiles/def/
  skos: http://www.w3.org/2004/02/skos/core#
  proc: https://w3id.org/ogc/api/processes/
  dct: http://purl.org/dc/terms/
x-bblocks-metadata:
  itemIdentifier: generic-profiles.implementation-profile.point-cloud-to-shapes
  register: https://geolabs.github.io/bblocks-generic-profiles/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-04'

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/point-cloud-to-shapes/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/point-cloud-to-shapes/schema.yaml)


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
    "refinesGenericProfile": {
      "@id": "gp:refinesGenericProfile",
      "@type": "@id"
    },
    "keywords": "proc:keywords",
    "metadata": "proc:metadata",
    "inputs": {
      "@context": {
        "@vocab": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/",
        "dataType": {
          "@id": "dct:type",
          "@type": "@id"
        },
        "schema": {
          "@context": {
            "@vocab": "https://w3id.org/ogc/api/schema/"
          },
          "@id": "proc:schema"
        },
        "maxOccurs": "proc:maxOccurs",
        "metadata": {
          "@context": {
            "role": {
              "@id": "proc:role",
              "@type": "@id"
            }
          },
          "@id": "proc:metadata"
        }
      },
      "@id": "gp:inputs"
    },
    "outputs": {
      "@context": {
        "@vocab": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/",
        "dataType": {
          "@id": "dct:type",
          "@type": "@id"
        },
        "schema": {
          "@context": {
            "@vocab": "https://w3id.org/ogc/api/schema/"
          },
          "@id": "proc:schema"
        },
        "metadata": {
          "@context": {
            "role": {
              "@id": "proc:role",
              "@type": "@id"
            }
          },
          "@id": "proc:metadata"
        }
      },
      "@id": "gp:outputs"
    },
    "source": "dct:source",
    "ImplementationProfile": "gp:ImplementationProfile",
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
    "gp": "https://geolabs.github.io/bblocks-generic-profiles/def/",
    "proc": "https://w3id.org/ogc/api/processes/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/point-cloud-to-shapes/context.jsonld)

## Sources

* [SAGA 7.3.0 -- Point Cloud to Shapes](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/pointcloud_tools_5.html)
* [ZOO-Project Geonovum testbed -- SAGA.pointcloud_tools.5: Point Cloud to Shapes](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.5)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/implementation-profile/point-cloud-to-shapes`

