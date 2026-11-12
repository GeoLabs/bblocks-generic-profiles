
# Implementation Profile: Raster band math (multi-band output) (Schema)

`generic-profiles.implementation-profile.raster-band-math-multiband` *v0.1*

Implementation Profile of the operation Raster band math (multi-band output), whose meaning is its activity type (activityType): the signature of the Generic Profile Raster band math, bound to data exchange formats.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Implementation Profile: **Raster band math (multi-band output)**.

> Implementation Profile of the operation Raster band math (multi-band output), whose meaning is its activity type (activityType): the signature of the Generic Profile Raster band math, bound to data exchange formats.

## Activity type

The meaning of the operation -- its definition, the standards that define it and its illustration --
is the activity type [`generic-profiles.activity-type.raster-band-math-multiband`](../../activity-type/raster-band-math-multiband/), to which this
profile points with `activityType` (decisions D3 and D4).

## Signature and representations

The signature of the Generic Profile [Raster band math](../../generic-profile/raster-band-math/), with each data-carrying
input and output bound to a representation of the
[`bblocks-data-formats`](https://github.com/GeoLabs/bblocks-data-formats) register (Table 21 Data
format, D; decision D6):

| Role | Data type | Representation |
|---|---|---|
| input `rasters` (minOccurs 1, maxOccurs unbounded) | `raster` | [`raster-geotiff`](https://w3id.org/geolabs/ospd/data-formats/representation/raster-geotiff) (Raster as GeoTIFF) |
| input `expression` | `expression` | -- |
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
  and [Generic Profile](../../generic-profile/raster-band-math/) are grounded in too). As with
  the other raster Implementation Profiles, WCPS is not the language this operation is actually
  bound to below -- GDAL/OTB, not WCPS, is what the Geonovum testbed runs.
- [OTB BandMathX -- Performs mathematical operations on several multiband images, outputting a mono- or multi-band image](https://www.orfeo-toolbox.org/CookBook/Applications/app_BandMathX.html) -- the concrete software binding: a widely
  deployed, de facto standard implementation (not itself an ISO/OGC standard) that the Geonovum
  testbed's own
  [`OTB.BandMathX`](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.BandMathX)
  process wraps directly. OTB's own documentation states the distinction this Implementation
  Profile exists to capture: *"outputs the result into an image (multi- or mono-band, as opposed
  to the BandMath OTB-application)... As opposed to muParser (and thus the BandMath
  OTB-application), muParserX supports vector expressions which allows outputting multi-band
  images."* [`raster-band-math`](../raster-band-math/) (`OTB.BandMath`/muParser) is the
  monoband-only sibling of this Implementation Profile -- both now refine the **same** Generic
  Profile, `raster-band-math` (see "Open question" below for why).

## Open question: how to formally express "one band" vs. "several bands"

This Implementation Profile and its sibling [`raster-band-math`](../raster-band-math/) exist
precisely because `OTB.BandMath` and `OTB.BandMathX` differ in this one respect. An earlier
draft of this register tried to express that with `cardinality: one-or-many` on the Generic
Profile's output -- that was wrong: a multi-band raster is still **one** Raster output value, not
several, so output cardinality is not the right tool (see `raster-band-math`'s own
"Why one Generic Profile, not two" section, and the base `generic-profile.schema.yaml`'s note on
`outputs`).

The formally correct mechanism does exist: [OGC 09-146r8 Coverage Implementation Schema (CIS)
1.1.1](https://docs.ogc.org/is/09-146r8/09-146r8.html) §6.5 "RangeType" describes a coverage's
band/field structure as a `SWE Common::DataRecord` -- one named `field` per band, each with its
own data type -- attached to the coverage itself, not to a process's output cardinality. OGC API
- Coverages (draft) exposes the same concept operationally as "field selection" (retrieving only
certain fields/bands of a coverage's range). That is the standards-grounded answer to "how do you
say a process's output has N bands, or that N depends on the input": a RangeType-like field list
on the output, not a cardinality.

**This register does not yet model a RangeType-like structure.** Adding one properly (field
names, per-field data types, and how a process declares what it contributes to or restricts in
the output RangeType) is a real modelling task of its own, not a one-line schema addition, and is
left as an open point for a future revision rather than bolted on here provisionally. The band
count itself is structurally enforced: since the data type `raster-single-band` was added
(declared 2026-10-08; first used here in commit `1ec787b`, 2026-10-09), `raster-band-math`'s output
has the dataType `raster-single-band` and this profile's keeps `raster`, each pinned by the `const`
of the profile's `schema.yaml` (`gp:DataTypeReferenceShape` only checks that a dataType is a
`dt:DataType`). What stays in prose only is which bands the output has.

## Data formats

`rasters`, `raster` (output): GeoTIFF -- the register's minimal default (Table 21, D: Declare),
grounded in `OTB.BandMathX`'s own processDescription, whose `il`/`out` both declare exactly three
media types (`image/tiff`, `image/jpeg`, `image/png`); GeoTIFF is kept here as the one
georeferencing-capable member of that set (plain JPEG/PNG carry no CRS).

## Multiplicity

`rasters`: `maxOccurs: unbounded`, as in the Generic Profile. Any practical cap belongs to a real
implementation, not to this tier.

Per [OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32), a specific deployment may *Extend* (E, footnote d) this minimal default with additional formats it happens to support -- this tier intentionally does not pre-empt that.

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.raster-band-math`](../../generic-profile/raster-band-math/)
- `activityType`: [`generic-profiles.activity-type.raster-band-math-multiband`](../../activity-type/raster-band-math-multiband/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see [`ospd.process-profiles.raster.band-math-multiband`](https://github.com/GeoLabs/bblocks-process-profiles/tree/master/_sources/raster/band-math-multiband)
in `bblocks-process-profiles` -- a real process of the ZOO-Project Geonovum testbed
(<https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.BandMathX>).

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
- `band-count-2026-11-09`, clarifying
- `band-count-correction-2026-11-09`, clarifying
- `sections-restored-2026-11-09`, clarifying

## Examples

### Raster band math (multi-band output)
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband",
  "type": "ImplementationProfile",
  "prefLabel": "Raster band math (multi-band output)",
  "definition": "Implementation Profile of the operation Raster band math (multi-band output), whose meaning is its activity type (activityType): the signature of the Generic Profile Raster band math, bound to data exchange formats.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "hasAction": [
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-09-30T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/meaning-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "The meaning of the operation moves to the activity type https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-band-math-multiband, linked by activityType (gp:activityType). The definition no longer defines the operation; it was: \"Evaluates a user-supplied, possibly vector-valued mathematical expression per pixel across one or more input rasters, producing an output raster with one or more bands.\"",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/operation-sources-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "clarifying",
      "description": "The sources defining the operation move to the activity type: OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard; OGC 09-146r8 Coverage Implementation Schema (CIS) 1.1.1, \u00a76.5 RangeType.",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/representation-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "The schema copied on each input and output that had one is replaced by the representation that realizes its data type in the data-formats register (decision D6): inputs/rasters -> raster-geotiff (schema was {\"type\": \"string\", \"contentEncoding\": \"base64\", \"contentMediaType\": \"image/tiff\", \"description\": \"GeoTIFF\"}); outputs/raster -> raster-geotiff (schema was {\"type\": \"string\", \"contentEncoding\": \"base64\", \"contentMediaType\": \"image/tiff\", \"description\": \"GeoTIFF\"}).",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/tools-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "clarifying",
      "description": "Decision D4: tool keywords removed: OTB, BandMathX; 2 format keywords removed from inputs and outputs (inputs/rasters: GeoTIFF; outputs/raster: GeoTIFF); sources removed (tools, testbed, the bbox schema now in the representation's format): OTB BandMathX -- Performs mathematical operations on several multiband images, outputting a mono- or multi-band image <https://www.orfeo-toolbox.org/CookBook/Applications/app_BandMathX.html>; description rewritten without tool, host or testbed. Each removed tool or testbed reference remains findable at tier 4, in bblocks-process-profiles.",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/data-type-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "The dataType of input `expression` changes from https://geolabs.github.io/bblocks-data-types/def/data-type/string, which hid the concept, to https://geolabs.github.io/bblocks-data-types/def/data-type/expression, created for this role in the data-types register.",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/band-count-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "clarifying",
      "description": "Description corrected: it said the distinction from raster-band-math (one band or several) was documented only in prose and not structurally enforced; it is enforced since the data type raster-single-band was added (declared 2026-10-08), by the dataType of each profile's output. Decision of 2026-11-09.",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/band-count-correction-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "clarifying",
      "description": "Corrects https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/band-count-2026-11-09 and the description: the band count is pinned by the const of each profile's schema.yaml; gp:DataTypeReferenceShape only checks that a dataType is a dt:DataType, not which one.",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/sections-restored-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "clarifying",
      "description": "Corrects what https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/tools-2026-11-09 describes: the description sections removed then (sources, illustrations, data formats, multiplicity and the open question where present, and the Register position reference to the tier-4 process and its testbed URL) are restored. Tools and testbed stay in the prose; decision D4 applies to the model (keywords, source, properties), which carries none. Decision of 2026-11-09.",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband"
    }
  ],
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband",
  "itemClass": "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/implementation-profile",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math",
  "activityType": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-band-math-multiband",
  "keywords": [
    "raster",
    "coverage",
    "band math",
    "multi-band"
  ],
  "metadata": [
    {
      "title": "Process Concept: Raster Coverage Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
    },
    {
      "title": "Generic Profile: Raster band math",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math"
    }
  ],
  "inputs": {
    "rasters": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/inputs/rasters",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/raster",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-geotiff"
      ],
      "maxOccurs": "unbounded",
      "keywords": [
        "raster"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster band math -- input `rasters`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/rasters"
        }
      ]
    },
    "expression": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/inputs/expression",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/expression",
      "keywords": [
        "expression"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster band math -- input `expression`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/expression"
        }
      ]
    }
  },
  "outputs": {
    "raster": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/outputs/raster",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/raster",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-geotiff"
      ],
      "keywords": [
        "raster"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster band math -- output `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/outputs/raster"
        }
      ]
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/raster-band-math-multiband/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband",
  "type": "ImplementationProfile",
  "prefLabel": "Raster band math (multi-band output)",
  "definition": "Implementation Profile of the operation Raster band math (multi-band output), whose meaning is its activity type (activityType): the signature of the Generic Profile Raster band math, bound to data exchange formats.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "hasAction": [
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/addition",
      "type": "RegisterAction",
      "actionType": "addition",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-09-30T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/meaning-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "The meaning of the operation moves to the activity type https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-band-math-multiband, linked by activityType (gp:activityType). The definition no longer defines the operation; it was: \"Evaluates a user-supplied, possibly vector-valued mathematical expression per pixel across one or more input rasters, producing an output raster with one or more bands.\"",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/operation-sources-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "clarifying",
      "description": "The sources defining the operation move to the activity type: OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard; OGC 09-146r8 Coverage Implementation Schema (CIS) 1.1.1, \u00a76.5 RangeType.",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/representation-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "The schema copied on each input and output that had one is replaced by the representation that realizes its data type in the data-formats register (decision D6): inputs/rasters -> raster-geotiff (schema was {\"type\": \"string\", \"contentEncoding\": \"base64\", \"contentMediaType\": \"image/tiff\", \"description\": \"GeoTIFF\"}); outputs/raster -> raster-geotiff (schema was {\"type\": \"string\", \"contentEncoding\": \"base64\", \"contentMediaType\": \"image/tiff\", \"description\": \"GeoTIFF\"}).",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/tools-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "clarifying",
      "description": "Decision D4: tool keywords removed: OTB, BandMathX; 2 format keywords removed from inputs and outputs (inputs/rasters: GeoTIFF; outputs/raster: GeoTIFF); sources removed (tools, testbed, the bbox schema now in the representation's format): OTB BandMathX -- Performs mathematical operations on several multiband images, outputting a mono- or multi-band image <https://www.orfeo-toolbox.org/CookBook/Applications/app_BandMathX.html>; description rewritten without tool, host or testbed. Each removed tool or testbed reference remains findable at tier 4, in bblocks-process-profiles.",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/data-type-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "substantive",
      "description": "The dataType of input `expression` changes from https://geolabs.github.io/bblocks-data-types/def/data-type/string, which hid the concept, to https://geolabs.github.io/bblocks-data-types/def/data-type/expression, created for this role in the data-types register.",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/band-count-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "clarifying",
      "description": "Description corrected: it said the distinction from raster-band-math (one band or several) was documented only in prose and not structurally enforced; it is enforced since the data type raster-single-band was added (declared 2026-10-08), by the dataType of each profile's output. Decision of 2026-11-09.",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/band-count-correction-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "clarifying",
      "description": "Corrects https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/band-count-2026-11-09 and the description: the band count is pinned by the const of each profile's schema.yaml; gp:DataTypeReferenceShape only checks that a dataType is a dt:DataType, not which one.",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband"
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/sections-restored-2026-11-09",
      "type": "RegisterAction",
      "actionType": "https://geolabs.github.io/bblocks-generic-profiles/def/amendmentAction",
      "changeClassification": "clarifying",
      "description": "Corrects what https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/tools-2026-11-09 describes: the description sections removed then (sources, illustrations, data formats, multiplicity and the open question where present, and the Register position reference to the tier-4 process and its testbed URL) are restored. Tools and testbed stay in the prose; decision D4 applies to the model (keywords, source, properties), which carries none. Decision of 2026-11-09.",
      "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
      "startedAtTime": "2026-11-09T00:00:00Z",
      "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband"
    }
  ],
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband",
  "itemClass": "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/implementation-profile",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math",
  "activityType": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-band-math-multiband",
  "keywords": [
    "raster",
    "coverage",
    "band math",
    "multi-band"
  ],
  "metadata": [
    {
      "title": "Process Concept: Raster Coverage Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing"
    },
    {
      "title": "Generic Profile: Raster band math",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math"
    }
  ],
  "inputs": {
    "rasters": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/inputs/rasters",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/raster",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-geotiff"
      ],
      "maxOccurs": "unbounded",
      "keywords": [
        "raster"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster band math -- input `rasters`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/rasters"
        }
      ]
    },
    "expression": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/inputs/expression",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/expression",
      "keywords": [
        "expression"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster band math -- input `expression`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/expression"
        }
      ]
    }
  },
  "outputs": {
    "raster": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/outputs/raster",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/raster",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/raster-geotiff"
      ],
      "keywords": [
        "raster"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster band math -- output `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/outputs/raster"
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

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/addition> a rim:RegisterAction ;
    prov:startedAtTime "2026-09-30T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType rim:additionAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband> ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/band-count-2026-11-09> a rim:RegisterAction ;
    dcterms:description "Description corrected: it said the distinction from raster-band-math (one band or several) was documented only in prose and not structurally enforced; it is enforced since the data type raster-single-band was added (declared 2026-10-08), by the dataType of each profile's output. Decision of 2026-11-09." ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType gp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband> ;
    rim:changeClassification rim:clarifyingChange ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/band-count-correction-2026-11-09> a rim:RegisterAction ;
    dcterms:description "Corrects https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/band-count-2026-11-09 and the description: the band count is pinned by the const of each profile's schema.yaml; gp:DataTypeReferenceShape only checks that a dataType is a dt:DataType, not which one." ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType gp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband> ;
    rim:changeClassification rim:clarifyingChange ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/data-type-2026-11-09> a rim:RegisterAction ;
    dcterms:description "The dataType of input `expression` changes from https://geolabs.github.io/bblocks-data-types/def/data-type/string, which hid the concept, to https://geolabs.github.io/bblocks-data-types/def/data-type/expression, created for this role in the data-types register." ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType gp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/meaning-2026-11-09> a rim:RegisterAction ;
    dcterms:description "The meaning of the operation moves to the activity type https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-band-math-multiband, linked by activityType (gp:activityType). The definition no longer defines the operation; it was: \"Evaluates a user-supplied, possibly vector-valued mathematical expression per pixel across one or more input rasters, producing an output raster with one or more bands.\"" ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType gp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/operation-sources-2026-11-09> a rim:RegisterAction ;
    dcterms:description "The sources defining the operation move to the activity type: OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard; OGC 09-146r8 Coverage Implementation Schema (CIS) 1.1.1, §6.5 RangeType." ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType gp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband> ;
    rim:changeClassification rim:clarifyingChange ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/representation-2026-11-09> a rim:RegisterAction ;
    dcterms:description "The schema copied on each input and output that had one is replaced by the representation that realizes its data type in the data-formats register (decision D6): inputs/rasters -> raster-geotiff (schema was {\"type\": \"string\", \"contentEncoding\": \"base64\", \"contentMediaType\": \"image/tiff\", \"description\": \"GeoTIFF\"}); outputs/raster -> raster-geotiff (schema was {\"type\": \"string\", \"contentEncoding\": \"base64\", \"contentMediaType\": \"image/tiff\", \"description\": \"GeoTIFF\"})." ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType gp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband> ;
    rim:changeClassification rim:substantiveChange ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/sections-restored-2026-11-09> a rim:RegisterAction ;
    dcterms:description "Corrects what https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/tools-2026-11-09 describes: the description sections removed then (sources, illustrations, data formats, multiplicity and the open question where present, and the Register position reference to the tier-4 process and its testbed URL) are restored. Tools and testbed stay in the prose; decision D4 applies to the model (keywords, source, properties), which carries none. Decision of 2026-11-09." ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType gp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband> ;
    rim:changeClassification rim:clarifyingChange ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/tools-2026-11-09> a rim:RegisterAction ;
    dcterms:description "Decision D4: tool keywords removed: OTB, BandMathX; 2 format keywords removed from inputs and outputs (inputs/rasters: GeoTIFF; outputs/raster: GeoTIFF); sources removed (tools, testbed, the bbox schema now in the representation's format): OTB BandMathX -- Performs mathematical operations on several multiband images, outputting a mono- or multi-band image <https://www.orfeo-toolbox.org/CookBook/Applications/app_BandMathX.html>; description rewritten without tool, host or testbed. Each removed tool or testbed reference remains findable at tier 4, in bblocks-process-profiles." ;
    prov:startedAtTime "2026-11-09T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType gp:amendmentAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband> ;
    rim:changeClassification rim:clarifyingChange ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/inputs/expression> dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/expression> ;
    proc:keywords "expression" ;
    proc:metadata [ dcterms:title "Generic Profile: Raster band math -- input `expression`" ;
            ns1:href "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/expression" ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/inputs/rasters> dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/raster> ;
    gp:representation <https://w3id.org/geolabs/ospd/data-formats/representation/raster-geotiff> ;
    proc:keywords "raster" ;
    proc:maxOccurs "unbounded" ;
    proc:metadata [ dcterms:title "Generic Profile: Raster band math -- input `rasters`" ;
            ns1:href "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/rasters" ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/outputs/raster> dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/raster> ;
    gp:representation <https://w3id.org/geolabs/ospd/data-formats/representation/raster-geotiff> ;
    proc:keywords "raster" ;
    proc:metadata [ dcterms:title "Generic Profile: Raster band math -- output `raster`" ;
            ns2:href "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/outputs/raster" ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband> a gp:ImplementationProfile ;
    skos:definition "Implementation Profile of the operation Raster band math (multi-band output), whose meaning is its activity type (activityType): the signature of the Generic Profile Raster band math, bound to data exchange formats." ;
    skos:inScheme gp:implementation-profile ;
    skos:prefLabel "Raster band math (multi-band output)" ;
    gp:activityType <https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-band-math-multiband> ;
    gp:inputs [ ns1:expression <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/inputs/expression> ;
            ns1:rasters <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/inputs/rasters> ] ;
    gp:outputs [ ns2:raster <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/outputs/raster> ] ;
    gp:refinesGenericProfile <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math> ;
    proc:keywords "band math",
        "coverage",
        "multi-band",
        "raster" ;
    proc:metadata [ dcterms:title "Process Concept: Raster Coverage Processing" ],
        [ dcterms:title "Generic Profile: Raster band math" ] ;
    rim:hasAction <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/addition>,
        <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/band-count-2026-11-09>,
        <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/band-count-correction-2026-11-09>,
        <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/data-type-2026-11-09>,
        <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/meaning-2026-11-09>,
        <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/operation-sources-2026-11-09>,
        <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/representation-2026-11-09>,
        <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/sections-restored-2026-11-09>,
        <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/actions/tools-2026-11-09> ;
    rim:inRegister gp:register ;
    rim:itemClass <https://geolabs.github.io/bblocks-generic-profiles/def/item-class/implementation-profile> ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:invalid .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Implementation Profile "Raster band math (multi-band output)" --
  see generic-profiles.implementation-profile for the general shape every Implementation
  Profile shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband
      x-jsonld-id: '@id'
    type:
      const: ImplementationProfile
      x-jsonld-id: '@type'
    prefLabel:
      const: Raster band math (multi-band output)
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
    refinesGenericProfile:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/refinesGenericProfile
      x-jsonld-type: '@id'
    activityType:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/raster-band-math-multiband
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/activityType
      x-jsonld-type: '@id'
    keywords:
      allOf:
      - contains:
          const: raster
      - contains:
          const: coverage
      - contains:
          const: band math
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math
      x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
    inputs:
      type: object
      required:
      - rasters
      - expression
      properties:
        rasters:
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/rasters
              x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
        expression:
          properties:
            keywords:
              allOf:
              - contains:
                  const: expression
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/expression
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
                      const: https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/outputs/raster
              x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/outputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/
- type: object
  properties:
    inputs:
      properties:
        rasters:
          required:
          - id
          - dataType
          - representation
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/inputs/rasters
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
        expression:
          required:
          - id
          - dataType
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/inputs/expression
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-data-types/def/data-type/expression
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/outputs/raster
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
  itemIdentifier: generic-profiles.implementation-profile.raster-band-math-multiband
  register: https://geolabs.github.io/bblocks-generic-profiles/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-12'

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/raster-band-math-multiband/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/raster-band-math-multiband/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/raster-band-math-multiband/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/implementation-profile/raster-band-math-multiband`

