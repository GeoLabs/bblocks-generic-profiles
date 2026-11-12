
# Implementation Profile: Otsu thresholding (Schema)

`generic-profiles.implementation-profile.otsu-thresholding` *v0.1*

Implementation Profile of the operation Otsu thresholding, whose meaning is its activity type (activityType): the signature of the Generic Profile Raster thresholding, bound to data exchange formats.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Implementation Profile: **Otsu thresholding**.

> Implementation Profile of the operation Otsu thresholding, whose meaning is its activity type (activityType): the signature of the Generic Profile Raster thresholding, bound to data exchange formats.

## Activity type

The meaning of the operation -- its definition, the standards that define it and its illustration --
is the activity type [`generic-profiles.activity-type.otsu-thresholding`](../../activity-type/otsu-thresholding/), to which this
profile points with `activityType` (decisions D3 and D4).

## Signature and representations

The signature of the Generic Profile [Raster thresholding](../../generic-profile/raster-thresholding/), with each data-carrying
input and output bound to a representation of the
[`bblocks-data-formats`](https://github.com/GeoLabs/bblocks-data-formats) register (Table 21 Data
format, D; decision D6):

| Role | Data type | Cardinality | Representation |
|---|---|---|---|
| input `raster` | `raster-single-band` | exactly one | [`raster-single-band-geotiff`](https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff) (Single-band raster as GeoTIFF) |
| output `mask` | `binary-mask` | -- | [`raster-single-band-geotiff`](https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff) (Single-band raster as GeoTIFF) |

The representations are a minimal default: a deployment may support more formats (OGC 14-065 WPS
2.0.2 §7.5.4 Table 21, footnote d).

## Notes

The threshold is not an input: Otsu's method computes it from the histogram of the raster's values.
A thresholding at a value given by the caller would need another Generic Profile. The output `mask` is a
`binary-mask`; its representation is the one of `raster-single-band`, its broader data type, which
`gp:RepresentationReferenceShape` accepts.

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.raster-thresholding`](../../generic-profile/raster-thresholding/)
- `activityType`: [`generic-profiles.activity-type.otsu-thresholding`](../../activity-type/otsu-thresholding/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). A proposal added on 2026-11-10 (decision of
2026-11-10, six new process profiles). The processes of `bblocks-process-profiles` that implement it are attached
there, with `implementsProfile`; this item carries no tool, host or testbed (decision D4).

## Examples

### Otsu thresholding
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/otsu-thresholding",
  "type": "ImplementationProfile",
  "prefLabel": "Otsu thresholding",
  "definition": "Implementation Profile of the operation Otsu thresholding, whose meaning is its activity type (activityType): the signature of the Generic Profile Raster thresholding, bound to data exchange formats.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "hasAction": [
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/otsu-thresholding/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/otsu-thresholding"
    }
  ],
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/otsu-thresholding",
  "itemClass": "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/implementation-profile",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-thresholding",
  "activityType": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/otsu-thresholding",
  "keywords": [
    "raster",
    "coverage",
    "thresholding"
  ],
  "metadata": [
    {
      "title": "Process Concept: Raster Coverage Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
    },
    {
      "title": "Generic Profile: Raster thresholding",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-thresholding"
    }
  ],
  "inputs": {
    "raster": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/otsu-thresholding/inputs/raster",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/raster-single-band",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff"
      ],
      "keywords": [
        "raster"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster thresholding -- input `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-thresholding/inputs/raster"
        }
      ]
    }
  },
  "outputs": {
    "mask": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/otsu-thresholding/outputs/mask",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/binary-mask",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff"
      ],
      "keywords": [
        "mask"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster thresholding -- output `mask`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-thresholding/outputs/mask"
        }
      ]
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/otsu-thresholding/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/otsu-thresholding",
  "type": "ImplementationProfile",
  "prefLabel": "Otsu thresholding",
  "definition": "Implementation Profile of the operation Otsu thresholding, whose meaning is its activity type (activityType): the signature of the Generic Profile Raster thresholding, bound to data exchange formats.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "hasAction": [
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/otsu-thresholding/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-10T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/otsu-thresholding"
    }
  ],
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/otsu-thresholding",
  "itemClass": "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/implementation-profile",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-thresholding",
  "activityType": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/otsu-thresholding",
  "keywords": [
    "raster",
    "coverage",
    "thresholding"
  ],
  "metadata": [
    {
      "title": "Process Concept: Raster Coverage Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
    },
    {
      "title": "Generic Profile: Raster thresholding",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-thresholding"
    }
  ],
  "inputs": {
    "raster": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/otsu-thresholding/inputs/raster",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/raster-single-band",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff"
      ],
      "keywords": [
        "raster"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster thresholding -- input `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-thresholding/inputs/raster"
        }
      ]
    }
  },
  "outputs": {
    "mask": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/otsu-thresholding/outputs/mask",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/binary-mask",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff"
      ],
      "keywords": [
        "mask"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster thresholding -- output `mask`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-thresholding/outputs/mask"
        }
      ]
    }
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix gp: <https://geolabs.github.io/bblocks-generic-profiles/def/> .
@prefix ns1: <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/> .
@prefix ns2: <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/otsu-thresholding> a gp:ImplementationProfile ;
    skos:definition "Implementation Profile of the operation Otsu thresholding, whose meaning is its activity type (activityType): the signature of the Generic Profile Raster thresholding, bound to data exchange formats." ;
    skos:inScheme gp:implementation-profile ;
    skos:prefLabel "Otsu thresholding" ;
    gp:activityType <https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/otsu-thresholding> ;
    gp:inputs [ ns1:raster <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/otsu-thresholding/inputs/raster> ] ;
    gp:outputs [ ns2:mask <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/otsu-thresholding/outputs/mask> ] ;
    gp:refinesGenericProfile <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-thresholding> ;
    proc:keywords "coverage",
        "raster",
        "thresholding" ;
    proc:metadata [ dcterms:title "Generic Profile: Raster thresholding" ],
        [ dcterms:title "Process Concept: Raster Coverage Processing" ] ;
    rim:hasAction <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/otsu-thresholding/actions/addition> ;
    rim:inRegister gp:register ;
    rim:itemClass <https://geolabs.github.io/bblocks-generic-profiles/def/item-class/implementation-profile> ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/otsu-thresholding"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:invalid .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/otsu-thresholding/actions/addition> a rim:RegisterAction ;
    prov:startedAtTime "2026-11-10T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType rim:additionAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/otsu-thresholding> ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/otsu-thresholding/inputs/raster> dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/raster-single-band> ;
    gp:representation <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff> ;
    proc:keywords "raster" ;
    proc:metadata [ dcterms:title "Generic Profile: Raster thresholding -- input `raster`" ;
            ns1:href "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-thresholding/inputs/raster" ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/otsu-thresholding/outputs/mask> dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/binary-mask> ;
    gp:representation <https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff> ;
    proc:keywords "mask" ;
    proc:metadata [ dcterms:title "Generic Profile: Raster thresholding -- output `mask`" ;
            ns2:href "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-thresholding/outputs/mask" ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output> ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Implementation Profile "Otsu thresholding" -- see generic-profiles.implementation-profile
  for the general shape every Implementation Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/otsu-thresholding
      x-jsonld-id: '@id'
    type:
      const: ImplementationProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Otsu thresholding
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
    refinesGenericProfile:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-thresholding
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/refinesGenericProfile
      x-jsonld-type: '@id'
    activityType:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/otsu-thresholding
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/activityType
      x-jsonld-type: '@id'
    keywords:
      allOf:
      - contains:
          const: raster
      - contains:
          const: coverage
      - contains:
          const: thresholding
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing
      - contains:
          type: object
          required:
          - role
          - href
          properties:
            role:
              const: http://www.opengis.net/spec/wps/2.0/def/process-profile/generic
            href:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-thresholding
      x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
    inputs:
      type: object
      required:
      - raster
      properties:
        raster:
          properties:
            keywords:
              allOf:
              - contains:
                  const: raster
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-thresholding/inputs/raster
              x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/
    outputs:
      type: object
      required:
      - mask
      properties:
        mask:
          properties:
            keywords:
              allOf:
              - contains:
                  const: mask
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-thresholding/outputs/mask
              x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/outputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/
- type: object
  properties:
    inputs:
      properties:
        raster:
          required:
          - id
          - dataType
          - representation
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/otsu-thresholding/inputs/raster
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-data-types/def/data-type/raster-single-band
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
            representation:
              const:
              - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff
              x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/representation
              x-jsonld-type: '@id'
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/
    outputs:
      properties:
        mask:
          required:
          - id
          - dataType
          - representation
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/otsu-thresholding/outputs/mask
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-data-types/def/data-type/binary-mask
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
            representation:
              const:
              - https://w3id.org/geolabs/ospd/data-formats/representation/raster-single-band-geotiff
              x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/representation
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
  itemIdentifier: generic-profiles.implementation-profile.otsu-thresholding
  register: https://geolabs.github.io/bblocks-generic-profiles/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-12'

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/otsu-thresholding/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/otsu-thresholding/schema.yaml)


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
    "activityType": {
      "@id": "gp:activityType",
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
        "representation": {
          "@id": "gp:representation",
          "@type": "@id"
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
        "representation": {
          "@id": "gp:representation",
          "@type": "@id"
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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/otsu-thresholding/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/implementation-profile/otsu-thresholding`

