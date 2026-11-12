
# Implementation Profile: Convex hull (Schema)

`generic-profiles.implementation-profile.convex-hull` *v0.1*

Implementation Profile of the operation Convex hull, whose meaning is its activity type (activityType): the signature of the Generic Profile Unary geometry operation, bound to data exchange formats.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Implementation Profile: **Convex hull**.

> Implementation Profile of the operation Convex hull, whose meaning is its activity type (activityType): the signature of the Generic Profile Unary geometry operation, bound to data exchange formats.

## Activity type

The meaning of the operation -- its definition, the standards that define it and its illustration --
is the activity type [`generic-profiles.activity-type.convex-hull`](../../activity-type/convex-hull/), to which this
profile points with `activityType` (decisions D3 and D4).

## Signature and representations

The signature of the Generic Profile [Unary geometry operation](../../generic-profile/unary-geometry-operation/), with each data-carrying
input and output bound to a representation of the
[`bblocks-data-formats`](https://github.com/GeoLabs/bblocks-data-formats) register (Table 21 Data
format, D; decision D6):

| Role | Data type | Representation |
|---|---|---|
| input `geometry` | `geometry` | [`geometry-gml`](https://w3id.org/geolabs/ospd/data-formats/representation/geometry-gml) (Geometry as GML) |
| output `result` | `geometry` | [`geometry-gml`](https://w3id.org/geolabs/ospd/data-formats/representation/geometry-gml) (Geometry as GML) |

The representations are a minimal default: a deployment may support more formats (OGC 14-065 WPS
2.0.2 §7.5.4 Table 21, footnote d).

## Source

- [OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1, §2.1.1.3 ConvexHull()](https://www.ogc.org/standards/sfs/)
- ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_ConvexHull
- [ZOO-Project Geonovum testbed -- ConvexHull: Compute convex hull.](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/ConvexHull)

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.unary-geometry-operation`](../../generic-profile/unary-geometry-operation/)
- `activityType`: [`generic-profiles.activity-type.convex-hull`](../../activity-type/convex-hull/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see [`ospd.process-profiles.sqlmm.convex-hull`](https://github.com/GeoLabs/bblocks-process-profiles/tree/master/_sources/sqlmm/convex-hull)
in `bblocks-process-profiles` -- a real process of the ZOO-Project Geonovum testbed
(<https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/ConvexHull>).

That process names this profile with `implementsProfile`. Tools, hosts and testbeds are
recorded there; this item carries none as keyword or source (decision D4). The sections
above keep the tools and testbed that its defaults were grounded in.

## Changes

A proposal, amended in place on 2026-11-09 (`gp:amendmentAction`):

- `meaning-2026-11-09`, substantive
- `operation-sources-2026-11-09`, clarifying
- `representation-2026-11-09`, substantive
- `tools-2026-11-09`, clarifying
- `sections-restored-2026-11-09`, clarifying

## Examples

### Convex hull
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull",
  "type": "ImplementationProfile",
  "prefLabel": "Convex hull",
  "definition": "Implementation Profile of the operation Convex hull, whose meaning is its activity type (activityType): the signature of the Generic Profile Unary geometry operation, bound to data exchange formats.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "hasAction": [
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-10-06T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/meaning-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "The meaning of the operation moves to the activity type https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/convex-hull, linked by activityType (gp:activityType). The definition no longer defines the operation; it was: \"Returns a geometry that represents the convex hull of this Geometry.\"",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/operation-sources-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "clarifying",
      "description": "The keyword ST_ConvexHull becomes an altLabel of the activity type; the sources defining the operation move to the activity type: OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1, \u00a72.1.1.3 ConvexHull(); ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_ConvexHull.",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/representation-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "The schema copied on each input and output that had one is replaced by the representation that realizes its data type in the data-formats register (decision D6): inputs/geometry -> geometry-gml (schema was {\"type\": \"string\", \"contentMediaType\": \"text/xml\", \"description\": \"GML\"}); outputs/result -> geometry-gml (schema was {\"type\": \"string\", \"contentMediaType\": \"text/xml\", \"description\": \"GML\"}).",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/tools-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "clarifying",
      "description": "Decision D4: 2 format keywords removed from inputs and outputs (inputs/geometry: GML; outputs/result: GML); sources removed (tools, testbed, the bbox schema now in the representation's format): ZOO-Project Geonovum testbed -- ConvexHull: Compute convex hull. <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/ConvexHull>; description rewritten without tool, host or testbed. Each removed tool or testbed reference remains findable at tier 4, in bblocks-process-profiles.",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/sections-restored-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "clarifying",
      "description": "Corrects what https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/tools-2026-11-09 describes: the description sections removed then (sources, illustrations, data formats, multiplicity and the open question where present, and the Register position reference to the tier-4 process and its testbed URL) are restored. Tools and testbed stay in the prose; decision D4 applies to the model (keywords, source, properties), which carries none. Decision of 2026-11-09.",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull"
    }
  ],
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull",
  "itemClass": "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/implementation-profile",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation",
  "activityType": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/convex-hull",
  "keywords": [
    "vector",
    "geometry",
    "derived geometry",
    "ConvexHull"
  ],
  "metadata": [
    {
      "title": "Process Concept: Vector Geometry Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"
    },
    {
      "title": "Generic Profile: Unary geometry operation",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation"
    }
  ],
  "inputs": {
    "geometry": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/inputs/geometry",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/geometry",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/geometry-gml"
      ],
      "keywords": [
        "geometry"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Unary geometry operation -- input `geometry`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation/inputs/geometry"
        }
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/outputs/result",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/geometry",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/geometry-gml"
      ],
      "keywords": [
        "geometry"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Unary geometry operation -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation/outputs/result"
        }
      ]
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/convex-hull/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull",
  "type": "ImplementationProfile",
  "prefLabel": "Convex hull",
  "definition": "Implementation Profile of the operation Convex hull, whose meaning is its activity type (activityType): the signature of the Generic Profile Unary geometry operation, bound to data exchange formats.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "hasAction": [
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-10-06T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/meaning-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "The meaning of the operation moves to the activity type https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/convex-hull, linked by activityType (gp:activityType). The definition no longer defines the operation; it was: \"Returns a geometry that represents the convex hull of this Geometry.\"",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/operation-sources-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "clarifying",
      "description": "The keyword ST_ConvexHull becomes an altLabel of the activity type; the sources defining the operation move to the activity type: OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1, \u00a72.1.1.3 ConvexHull(); ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_ConvexHull.",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/representation-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "The schema copied on each input and output that had one is replaced by the representation that realizes its data type in the data-formats register (decision D6): inputs/geometry -> geometry-gml (schema was {\"type\": \"string\", \"contentMediaType\": \"text/xml\", \"description\": \"GML\"}); outputs/result -> geometry-gml (schema was {\"type\": \"string\", \"contentMediaType\": \"text/xml\", \"description\": \"GML\"}).",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/tools-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "clarifying",
      "description": "Decision D4: 2 format keywords removed from inputs and outputs (inputs/geometry: GML; outputs/result: GML); sources removed (tools, testbed, the bbox schema now in the representation's format): ZOO-Project Geonovum testbed -- ConvexHull: Compute convex hull. <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/ConvexHull>; description rewritten without tool, host or testbed. Each removed tool or testbed reference remains findable at tier 4, in bblocks-process-profiles.",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/sections-restored-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "clarifying",
      "description": "Corrects what https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/tools-2026-11-09 describes: the description sections removed then (sources, illustrations, data formats, multiplicity and the open question where present, and the Register position reference to the tier-4 process and its testbed URL) are restored. Tools and testbed stay in the prose; decision D4 applies to the model (keywords, source, properties), which carries none. Decision of 2026-11-09.",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull"
    }
  ],
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull",
  "itemClass": "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/implementation-profile",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation",
  "activityType": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/convex-hull",
  "keywords": [
    "vector",
    "geometry",
    "derived geometry",
    "ConvexHull"
  ],
  "metadata": [
    {
      "title": "Process Concept: Vector Geometry Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"
    },
    {
      "title": "Generic Profile: Unary geometry operation",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation"
    }
  ],
  "inputs": {
    "geometry": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/inputs/geometry",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/geometry",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/geometry-gml"
      ],
      "keywords": [
        "geometry"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Unary geometry operation -- input `geometry`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation/inputs/geometry"
        }
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/outputs/result",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/geometry",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/geometry-gml"
      ],
      "keywords": [
        "geometry"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Unary geometry operation -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation/outputs/result"
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
@prefix ns1: <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/> .
@prefix ns2: <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/addition> a rim:RegisterAction ;
    prov:startedAtTime "2026-10-06T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType rim:additionAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull> ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/meaning-2026-11-09> a rim:RegisterAction ;
    dcterms:description "The meaning of the operation moves to the activity type https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/convex-hull, linked by activityType (gp:activityType). The definition no longer defines the operation; it was: \"Returns a geometry that represents the convex hull of this Geometry.\"" ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType gp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/operation-sources-2026-11-09> a rim:RegisterAction ;
    dcterms:description "The keyword ST_ConvexHull becomes an altLabel of the activity type; the sources defining the operation move to the activity type: OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1, §2.1.1.3 ConvexHull(); ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_ConvexHull." ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType gp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull> ;
    rim:changeClassification rim:clarifyingChange ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/representation-2026-11-09> a rim:RegisterAction ;
    dcterms:description "The schema copied on each input and output that had one is replaced by the representation that realizes its data type in the data-formats register (decision D6): inputs/geometry -> geometry-gml (schema was {\"type\": \"string\", \"contentMediaType\": \"text/xml\", \"description\": \"GML\"}); outputs/result -> geometry-gml (schema was {\"type\": \"string\", \"contentMediaType\": \"text/xml\", \"description\": \"GML\"})." ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType gp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/sections-restored-2026-11-09> a rim:RegisterAction ;
    dcterms:description "Corrects what https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/tools-2026-11-09 describes: the description sections removed then (sources, illustrations, data formats, multiplicity and the open question where present, and the Register position reference to the tier-4 process and its testbed URL) are restored. Tools and testbed stay in the prose; decision D4 applies to the model (keywords, source, properties), which carries none. Decision of 2026-11-09." ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType gp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull> ;
    rim:changeClassification rim:clarifyingChange ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/tools-2026-11-09> a rim:RegisterAction ;
    dcterms:description "Decision D4: 2 format keywords removed from inputs and outputs (inputs/geometry: GML; outputs/result: GML); sources removed (tools, testbed, the bbox schema now in the representation's format): ZOO-Project Geonovum testbed -- ConvexHull: Compute convex hull. <https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/ConvexHull>; description rewritten without tool, host or testbed. Each removed tool or testbed reference remains findable at tier 4, in bblocks-process-profiles." ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType gp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull> ;
    rim:changeClassification rim:clarifyingChange ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/inputs/geometry> dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/geometry> ;
    gp:representation <https://w3id.org/geolabs/ospd/data-formats/representation/geometry-gml> ;
    proc:keywords "geometry" ;
    proc:metadata [ dcterms:title "Generic Profile: Unary geometry operation -- input `geometry`" ;
            ns2:href "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation/inputs/geometry" ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/outputs/result> dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/geometry> ;
    gp:representation <https://w3id.org/geolabs/ospd/data-formats/representation/geometry-gml> ;
    proc:keywords "geometry" ;
    proc:metadata [ dcterms:title "Generic Profile: Unary geometry operation -- output `result`" ;
            ns1:href "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation/outputs/result" ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull> a gp:ImplementationProfile ;
    skos:definition "Implementation Profile of the operation Convex hull, whose meaning is its activity type (activityType): the signature of the Generic Profile Unary geometry operation, bound to data exchange formats." ;
    skos:inScheme gp:implementation-profile ;
    skos:prefLabel "Convex hull" ;
    gp:activityType <https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/convex-hull> ;
    gp:inputs [ ns2:geometry <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/inputs/geometry> ] ;
    gp:outputs [ ns1:result <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/outputs/result> ] ;
    gp:refinesGenericProfile <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation> ;
    proc:keywords "ConvexHull",
        "derived geometry",
        "geometry",
        "vector" ;
    proc:metadata [ dcterms:title "Process Concept: Vector Geometry Processing" ],
        [ dcterms:title "Generic Profile: Unary geometry operation" ] ;
    rim:hasAction <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/addition>,
        <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/meaning-2026-11-09>,
        <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/operation-sources-2026-11-09>,
        <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/representation-2026-11-09>,
        <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/sections-restored-2026-11-09>,
        <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/actions/tools-2026-11-09> ;
    rim:inRegister gp:register ;
    rim:itemClass <https://geolabs.github.io/bblocks-generic-profiles/def/item-class/implementation-profile> ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:invalid .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Implementation Profile "Convex hull" -- see generic-profiles.implementation-profile
  for the general shape every Implementation Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull
      x-jsonld-id: '@id'
    type:
      const: ImplementationProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Convex hull
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
    refinesGenericProfile:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/refinesGenericProfile
      x-jsonld-type: '@id'
    activityType:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/convex-hull
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/activityType
      x-jsonld-type: '@id'
    keywords:
      allOf:
      - contains:
          const: vector
      - contains:
          const: geometry
      - contains:
          const: derived geometry
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing
      - contains:
          type: object
          required:
          - role
          - href
          properties:
            role:
              const: http://www.opengis.net/spec/wps/2.0/def/process-profile/generic
            href:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation
      x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
    inputs:
      type: object
      required:
      - geometry
      properties:
        geometry:
          properties:
            keywords:
              allOf:
              - contains:
                  const: geometry
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation/inputs/geometry
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
                  const: geometry
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/unary-geometry-operation/outputs/result
              x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/outputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/
- type: object
  properties:
    inputs:
      properties:
        geometry:
          required:
          - id
          - dataType
          - representation
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/inputs/geometry
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-data-types/def/data-type/geometry
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
            representation:
              const:
              - https://w3id.org/geolabs/ospd/data-formats/representation/geometry-gml
              x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/representation
              x-jsonld-type: '@id'
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/
    outputs:
      properties:
        result:
          required:
          - id
          - dataType
          - representation
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/convex-hull/outputs/result
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-data-types/def/data-type/geometry
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
            representation:
              const:
              - https://w3id.org/geolabs/ospd/data-formats/representation/geometry-gml
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
  itemIdentifier: generic-profiles.implementation-profile.convex-hull
  register: https://geolabs.github.io/bblocks-generic-profiles/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-12'

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/convex-hull/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/convex-hull/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/convex-hull/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/implementation-profile/convex-hull`

