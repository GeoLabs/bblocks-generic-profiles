
# Implementation Profile: Raster reprojection (Schema)

`generic-profiles.implementation-profile.raster-reprojection` *v0.1*

Implementation Profile of the operation Raster reprojection, whose meaning is its activity type (activityType): the signature of the Generic Profile Raster reprojection, bound to data exchange formats.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Implementation Profile: **Raster reprojection**.

> Implementation Profile of the operation Raster reprojection, whose meaning is its activity type (activityType): the signature of the Generic Profile Raster reprojection, bound to data exchange formats.

## Activity type

The meaning of the operation -- its definition, the standards that define it and its illustration --
is the activity type [`generic-profiles.activity-type.raster-reprojection`](../../activity-type/raster-reprojection/), to which this
profile points with `activityType` (decisions D3 and D4).

## Signature and representations

The signature of the Generic Profile [Raster reprojection](../../generic-profile/raster-reprojection/), with each data-carrying
input and output bound to a representation of the
[`bblocks-data-formats`](https://github.com/GeoLabs/bblocks-data-formats) register (Table 21 Data
format, D; decision D6):

| Role | Data type | Representation |
|---|---|---|
| input `raster` | `raster` | [`raster-geotiff`](https://w3id.org/geolabs/ospd/data-formats/representation/raster-geotiff) (Raster as GeoTIFF) |
| input `targetCRS` | `coordinate-reference-system` | -- |
| output `raster` | `raster` | [`raster-geotiff`](https://w3id.org/geolabs/ospd/data-formats/representation/raster-geotiff) (Raster as GeoTIFF) |

The representations are a minimal default: a deployment may support more formats (OGC 14-065 WPS
2.0.2 §7.5.4 Table 21, footnote d).

## Source

Two standards define this operation at different levels -- the abstract semantics, and the
concrete tool binding an Implementation Profile is specifically meant to add (OGC 14-065 WPS
2.0.2 §7.5.3, "down to the supported data exchange formats"):

- [OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard](https://www.ogc.org/standards/wcps/)
  -- the OGC standards-track evidence that this kind of coverage operation is a recognised,
  harmonised processing concept (this is what [its Concept](../../concept/raster-coverage-processing/)
  and [Generic Profile](../../generic-profile/raster-reprojection/) are grounded in too). Unlike
  SQL/MM for the vector Implementation Profiles, WCPS is not the language this operation is
  actually bound to below -- GDAL/OTB, not WCPS, is what the Geonovum testbed runs.
- [GDAL gdalwarp -- Image mosaicing, reprojection and warping utility](https://gdal.org/programs/gdalwarp.html) -- the concrete software binding: a
  widely deployed, de facto standard implementation (not itself an ISO/OGC standard, unlike
  SQL/MM's formal status for the vector operations) that the Geonovum testbed's own
  [`Gdal_Warp`](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Gdal_Warp)
  process wraps directly.

## Data formats

`raster` (input and output): GeoTIFF -- the register's minimal default (Table 21, D: Declare).
Not grounded in `Gdal_Warp`'s own processDescription: its `InputDSN`/`OutputDSN`/`Result` are
typed as plain `string` (a DSN/path), with no `oneOf`/`contentMediaType` declared -- GDAL's
wrappers on this testbed do not expose format constraints structurally the way the OTB
applications below do. GeoTIFF is kept as the vocabulary's own minimal baseline (the standard
GDAL raster format), not a claim about what this specific deployment structurally declares.

Per [OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32), a specific deployment may *Extend* (E, footnote d) this minimal default with additional formats it happens to support -- this tier intentionally does not pre-empt that.

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.raster-reprojection`](../../generic-profile/raster-reprojection/)
- `activityType`: [`generic-profiles.activity-type.raster-reprojection`](../../activity-type/raster-reprojection/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see [`ospd.process-profiles.raster.reprojection`](https://github.com/GeoLabs/bblocks-process-profiles/tree/master/_sources/raster/reprojection)
in `bblocks-process-profiles` -- a real process of the ZOO-Project Geonovum testbed
(<https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Gdal_Warp>).

That process names this profile with `implementsProfile`. Tools, hosts and testbeds are
recorded there; this item carries none as keyword or source (decision D4). The sections
above keep the tools and testbed that its defaults were grounded in.

## Changes

A proposal, amended in place on 2026-11-09 (`gp:amendmentAction`):

- `meaning-2026-11-09`, substantive
- `operation-sources-2026-11-09`, clarifying
- `representation-2026-11-09`, substantive
- `tools-2026-11-09`, clarifying
- `data-type-2026-11-09`, substantive
- `sections-restored-2026-11-09`, clarifying

## Examples

### Raster reprojection
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection",
  "type": "ImplementationProfile",
  "prefLabel": "Raster reprojection",
  "definition": "Implementation Profile of the operation Raster reprojection, whose meaning is its activity type (activityType): the signature of the Generic Profile Raster reprojection, bound to data exchange formats.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "hasAction": [
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-09-30T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/meaning-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "The meaning of the operation moves to the activity type https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-reprojection, linked by activityType (gp:activityType). The definition no longer defines the operation; it was: \"Reprojects a raster coverage to another coordinate reference system, resampling pixel values as needed, preserving the coverage's content.\"",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/operation-sources-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "clarifying",
      "description": "The source defining the operation moves to the activity type: OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard.",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/representation-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "The schema copied on each input and output that had one is replaced by the representation that realizes its data type in the data-formats register (decision D6): inputs/raster -> raster-geotiff (schema was {\"type\": \"string\", \"contentEncoding\": \"base64\", \"contentMediaType\": \"image/tiff\", \"description\": \"GeoTIFF\"}); outputs/raster -> raster-geotiff (schema was {\"type\": \"string\", \"contentEncoding\": \"base64\", \"contentMediaType\": \"image/tiff\", \"description\": \"GeoTIFF\"}).",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/tools-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "clarifying",
      "description": "Decision D4: tool keywords removed: GDAL, gdalwarp; 2 format keywords removed from inputs and outputs (inputs/raster: GeoTIFF; outputs/raster: GeoTIFF); sources removed (tools, testbed, the bbox schema now in the representation's format): GDAL gdalwarp -- Image mosaicing, reprojection and warping utility <https://gdal.org/programs/gdalwarp.html>; description rewritten without tool, host or testbed. Each removed tool or testbed reference remains findable at tier 4, in bblocks-process-profiles.",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/data-type-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "The dataType of input `targetCRS` changes from https://geolabs.github.io/bblocks-data-types/def/data-type/string, which hid the concept, to https://geolabs.github.io/bblocks-data-types/def/data-type/coordinate-reference-system, created for this role in the data-types register.",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/sections-restored-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "clarifying",
      "description": "Corrects what https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/tools-2026-11-09 describes: the description sections removed then (sources, illustrations, data formats, multiplicity and the open question where present, and the Register position reference to the tier-4 process and its testbed URL) are restored. Tools and testbed stay in the prose; decision D4 applies to the model (keywords, source, properties), which carries none. Decision of 2026-11-09.",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection"
    }
  ],
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection",
  "itemClass": "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/implementation-profile",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-reprojection",
  "activityType": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-reprojection",
  "keywords": [
    "raster",
    "coverage",
    "reprojection"
  ],
  "metadata": [
    {
      "title": "Process Concept: Raster Coverage Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
    },
    {
      "title": "Generic Profile: Raster reprojection",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-reprojection"
    }
  ],
  "inputs": {
    "raster": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/inputs/raster",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/raster",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-geotiff"
      ],
      "keywords": [
        "raster"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster reprojection -- input `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-reprojection/inputs/raster"
        }
      ]
    },
    "targetCRS": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/inputs/targetCRS",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/coordinate-reference-system",
      "keywords": [
        "CRS"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster reprojection -- input `targetCRS`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-reprojection/inputs/targetCRS"
        }
      ]
    }
  },
  "outputs": {
    "raster": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/outputs/raster",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/raster",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-geotiff"
      ],
      "keywords": [
        "raster"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster reprojection -- output `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-reprojection/outputs/raster"
        }
      ]
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/raster-reprojection/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection",
  "type": "ImplementationProfile",
  "prefLabel": "Raster reprojection",
  "definition": "Implementation Profile of the operation Raster reprojection, whose meaning is its activity type (activityType): the signature of the Generic Profile Raster reprojection, bound to data exchange formats.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "hasAction": [
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-09-30T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/meaning-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "The meaning of the operation moves to the activity type https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-reprojection, linked by activityType (gp:activityType). The definition no longer defines the operation; it was: \"Reprojects a raster coverage to another coordinate reference system, resampling pixel values as needed, preserving the coverage's content.\"",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/operation-sources-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "clarifying",
      "description": "The source defining the operation moves to the activity type: OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard.",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/representation-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "The schema copied on each input and output that had one is replaced by the representation that realizes its data type in the data-formats register (decision D6): inputs/raster -> raster-geotiff (schema was {\"type\": \"string\", \"contentEncoding\": \"base64\", \"contentMediaType\": \"image/tiff\", \"description\": \"GeoTIFF\"}); outputs/raster -> raster-geotiff (schema was {\"type\": \"string\", \"contentEncoding\": \"base64\", \"contentMediaType\": \"image/tiff\", \"description\": \"GeoTIFF\"}).",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/tools-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "clarifying",
      "description": "Decision D4: tool keywords removed: GDAL, gdalwarp; 2 format keywords removed from inputs and outputs (inputs/raster: GeoTIFF; outputs/raster: GeoTIFF); sources removed (tools, testbed, the bbox schema now in the representation's format): GDAL gdalwarp -- Image mosaicing, reprojection and warping utility <https://gdal.org/programs/gdalwarp.html>; description rewritten without tool, host or testbed. Each removed tool or testbed reference remains findable at tier 4, in bblocks-process-profiles.",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/data-type-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "The dataType of input `targetCRS` changes from https://geolabs.github.io/bblocks-data-types/def/data-type/string, which hid the concept, to https://geolabs.github.io/bblocks-data-types/def/data-type/coordinate-reference-system, created for this role in the data-types register.",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/sections-restored-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "clarifying",
      "description": "Corrects what https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/tools-2026-11-09 describes: the description sections removed then (sources, illustrations, data formats, multiplicity and the open question where present, and the Register position reference to the tier-4 process and its testbed URL) are restored. Tools and testbed stay in the prose; decision D4 applies to the model (keywords, source, properties), which carries none. Decision of 2026-11-09.",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection"
    }
  ],
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection",
  "itemClass": "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/implementation-profile",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-reprojection",
  "activityType": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-reprojection",
  "keywords": [
    "raster",
    "coverage",
    "reprojection"
  ],
  "metadata": [
    {
      "title": "Process Concept: Raster Coverage Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
    },
    {
      "title": "Generic Profile: Raster reprojection",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-reprojection"
    }
  ],
  "inputs": {
    "raster": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/inputs/raster",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/raster",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-geotiff"
      ],
      "keywords": [
        "raster"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster reprojection -- input `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-reprojection/inputs/raster"
        }
      ]
    },
    "targetCRS": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/inputs/targetCRS",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/coordinate-reference-system",
      "keywords": [
        "CRS"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster reprojection -- input `targetCRS`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-reprojection/inputs/targetCRS"
        }
      ]
    }
  },
  "outputs": {
    "raster": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/outputs/raster",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/raster",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-geotiff"
      ],
      "keywords": [
        "raster"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster reprojection -- output `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-reprojection/outputs/raster"
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

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/addition> a rim:RegisterAction ;
    prov:startedAtTime "2026-09-30T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType rim:additionAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection> ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/data-type-2026-11-09> a rim:RegisterAction ;
    dcterms:description "The dataType of input `targetCRS` changes from https://geolabs.github.io/bblocks-data-types/def/data-type/string, which hid the concept, to https://geolabs.github.io/bblocks-data-types/def/data-type/coordinate-reference-system, created for this role in the data-types register." ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType gp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/meaning-2026-11-09> a rim:RegisterAction ;
    dcterms:description "The meaning of the operation moves to the activity type https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-reprojection, linked by activityType (gp:activityType). The definition no longer defines the operation; it was: \"Reprojects a raster coverage to another coordinate reference system, resampling pixel values as needed, preserving the coverage's content.\"" ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType gp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/operation-sources-2026-11-09> a rim:RegisterAction ;
    dcterms:description "The source defining the operation moves to the activity type: OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard." ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType gp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection> ;
    rim:changeClassification rim:clarifyingChange ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/representation-2026-11-09> a rim:RegisterAction ;
    dcterms:description "The schema copied on each input and output that had one is replaced by the representation that realizes its data type in the data-formats register (decision D6): inputs/raster -> raster-geotiff (schema was {\"type\": \"string\", \"contentEncoding\": \"base64\", \"contentMediaType\": \"image/tiff\", \"description\": \"GeoTIFF\"}); outputs/raster -> raster-geotiff (schema was {\"type\": \"string\", \"contentEncoding\": \"base64\", \"contentMediaType\": \"image/tiff\", \"description\": \"GeoTIFF\"})." ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType gp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/sections-restored-2026-11-09> a rim:RegisterAction ;
    dcterms:description "Corrects what https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/tools-2026-11-09 describes: the description sections removed then (sources, illustrations, data formats, multiplicity and the open question where present, and the Register position reference to the tier-4 process and its testbed URL) are restored. Tools and testbed stay in the prose; decision D4 applies to the model (keywords, source, properties), which carries none. Decision of 2026-11-09." ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType gp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection> ;
    rim:changeClassification rim:clarifyingChange ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/tools-2026-11-09> a rim:RegisterAction ;
    dcterms:description "Decision D4: tool keywords removed: GDAL, gdalwarp; 2 format keywords removed from inputs and outputs (inputs/raster: GeoTIFF; outputs/raster: GeoTIFF); sources removed (tools, testbed, the bbox schema now in the representation's format): GDAL gdalwarp -- Image mosaicing, reprojection and warping utility <https://gdal.org/programs/gdalwarp.html>; description rewritten without tool, host or testbed. Each removed tool or testbed reference remains findable at tier 4, in bblocks-process-profiles." ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType gp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection> ;
    rim:changeClassification rim:clarifyingChange ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/inputs/raster> dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/raster> ;
    gp:representation <https://w3id.org/geolabs/ospd/data-formats/representation/raster-geotiff> ;
    proc:keywords "raster" ;
    proc:metadata [ dcterms:title "Generic Profile: Raster reprojection -- input `raster`" ;
            ns2:href "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-reprojection/inputs/raster" ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/inputs/targetCRS> dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/coordinate-reference-system> ;
    proc:keywords "CRS" ;
    proc:metadata [ dcterms:title "Generic Profile: Raster reprojection -- input `targetCRS`" ;
            ns2:href "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-reprojection/inputs/targetCRS" ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/outputs/raster> dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/raster> ;
    gp:representation <https://w3id.org/geolabs/ospd/data-formats/representation/raster-geotiff> ;
    proc:keywords "raster" ;
    proc:metadata [ dcterms:title "Generic Profile: Raster reprojection -- output `raster`" ;
            ns1:href "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-reprojection/outputs/raster" ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection> a gp:ImplementationProfile ;
    skos:definition "Implementation Profile of the operation Raster reprojection, whose meaning is its activity type (activityType): the signature of the Generic Profile Raster reprojection, bound to data exchange formats." ;
    skos:inScheme gp:implementation-profile ;
    skos:prefLabel "Raster reprojection" ;
    gp:activityType <https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-reprojection> ;
    gp:inputs [ ns2:raster <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/inputs/raster> ;
            ns2:targetCRS <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/inputs/targetCRS> ] ;
    gp:outputs [ ns1:raster <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/outputs/raster> ] ;
    gp:refinesGenericProfile <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-reprojection> ;
    proc:keywords "coverage",
        "raster",
        "reprojection" ;
    proc:metadata [ dcterms:title "Generic Profile: Raster reprojection" ],
        [ dcterms:title "Process Concept: Raster Coverage Processing" ] ;
    rim:hasAction <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/addition>,
        <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/data-type-2026-11-09>,
        <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/meaning-2026-11-09>,
        <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/operation-sources-2026-11-09>,
        <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/representation-2026-11-09>,
        <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/sections-restored-2026-11-09>,
        <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/actions/tools-2026-11-09> ;
    rim:inRegister gp:register ;
    rim:itemClass <https://geolabs.github.io/bblocks-generic-profiles/def/item-class/implementation-profile> ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:invalid .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Implementation Profile "Raster reprojection" -- see generic-profiles.implementation-profile
  for the general shape every Implementation Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection
      x-jsonld-id: '@id'
    type:
      const: ImplementationProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Raster reprojection
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
    refinesGenericProfile:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-reprojection
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/refinesGenericProfile
      x-jsonld-type: '@id'
    activityType:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-reprojection
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/activityType
      x-jsonld-type: '@id'
    keywords:
      allOf:
      - contains:
          const: raster
      - contains:
          const: coverage
      - contains:
          const: reprojection
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-reprojection
      x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
    inputs:
      type: object
      required:
      - raster
      - targetCRS
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-reprojection/inputs/raster
              x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
        targetCRS:
          properties:
            keywords:
              allOf:
              - contains:
                  const: CRS
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-reprojection/inputs/targetCRS
              x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/
    outputs:
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output
                    href:
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-reprojection/outputs/raster
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/inputs/raster
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-data-types/def/data-type/raster
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
            representation:
              const:
              - https://w3id.org/geolabs/ospd/data-formats/representation/raster-geotiff
              x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/representation
              x-jsonld-type: '@id'
        targetCRS:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/inputs/targetCRS
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-data-types/def/data-type/coordinate-reference-system
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/
    outputs:
      properties:
        raster:
          required:
          - id
          - dataType
          - representation
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-reprojection/outputs/raster
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-data-types/def/data-type/raster
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
            representation:
              const:
              - https://w3id.org/geolabs/ospd/data-formats/representation/raster-geotiff
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
  itemIdentifier: generic-profiles.implementation-profile.raster-reprojection
  register: https://geolabs.github.io/bblocks-generic-profiles/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-12'

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/raster-reprojection/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/raster-reprojection/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/raster-reprojection/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/implementation-profile/raster-reprojection`

