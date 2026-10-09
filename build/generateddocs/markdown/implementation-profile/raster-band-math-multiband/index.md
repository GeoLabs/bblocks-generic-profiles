
# Implementation Profile: Raster band math (multi-band output) (Schema)

`generic-profiles.implementation-profile.raster-band-math-multiband` *v0.1*

Evaluates a user-supplied, possibly vector-valued mathematical expression per pixel across one or more input rasters, producing an output raster with one or more bands.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Implementation Profile: **Raster band math (multi-band output)**.

> Evaluates a user-supplied, possibly vector-valued mathematical expression per pixel across one or more input rasters, producing an output raster with one or more bands.

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
left as an open point for a future revision rather than bolted on here provisionally. For now,
the distinction between this Implementation Profile and `raster-band-math` is documented only in
prose (their respective `description.md` and `prefLabel`/`definition`), not structurally
enforced in `schema` or any other schema property.

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

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.raster.band-math-multiband` in
`bblocks-process-profiles` -- a real process of the ZOO-Project Geonovum testbed
(<https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.BandMathX>).

## Examples

### Raster band math (multi-band output)
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband",
  "type": "ImplementationProfile",
  "prefLabel": "Raster band math (multi-band output)",
  "definition": "Evaluates a user-supplied, possibly vector-valued mathematical expression per pixel across one or more input rasters, producing an output raster with one or more bands.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math",
  "keywords": [
    "raster",
    "coverage",
    "band math",
    "OTB",
    "BandMathX",
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
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster",
      "schema": {
        "type": "string",
        "contentEncoding": "base64",
        "contentMediaType": "image/tiff",
        "description": "GeoTIFF"
      },
      "maxOccurs": "unbounded",
      "keywords": [
        "raster",
        "GeoTIFF"
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
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/string",
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
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster",
      "schema": {
        "type": "string",
        "contentEncoding": "base64",
        "contentMediaType": "image/tiff",
        "description": "GeoTIFF"
      },
      "keywords": [
        "raster",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster band math -- output `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/outputs/raster"
        }
      ]
    }
  },
  "source": [
    {
      "title": "OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard",
      "link": "https://www.ogc.org/standards/wcps/"
    },
    {
      "title": "OTB BandMathX -- Performs mathematical operations on several multiband images, outputting a mono- or multi-band image",
      "link": "https://www.orfeo-toolbox.org/CookBook/Applications/app_BandMathX.html"
    },
    {
      "title": "OGC 09-146r8 Coverage Implementation Schema (CIS) 1.1.1, \u00a76.5 RangeType",
      "link": "https://docs.ogc.org/is/09-146r8/09-146r8.html"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/raster-band-math-multiband/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband",
  "type": "ImplementationProfile",
  "prefLabel": "Raster band math (multi-band output)",
  "definition": "Evaluates a user-supplied, possibly vector-valued mathematical expression per pixel across one or more input rasters, producing an output raster with one or more bands.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "status": "submitted",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math",
  "keywords": [
    "raster",
    "coverage",
    "band math",
    "OTB",
    "BandMathX",
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
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster",
      "schema": {
        "type": "string",
        "contentEncoding": "base64",
        "contentMediaType": "image/tiff",
        "description": "GeoTIFF"
      },
      "maxOccurs": "unbounded",
      "keywords": [
        "raster",
        "GeoTIFF"
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
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/string",
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
      "dataType": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster",
      "schema": {
        "type": "string",
        "contentEncoding": "base64",
        "contentMediaType": "image/tiff",
        "description": "GeoTIFF"
      },
      "keywords": [
        "raster",
        "GeoTIFF"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Raster band math -- output `raster`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/outputs/raster"
        }
      ]
    }
  },
  "source": [
    {
      "title": "OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard",
      "link": "https://www.ogc.org/standards/wcps/"
    },
    {
      "title": "OTB BandMathX -- Performs mathematical operations on several multiband images, outputting a mono- or multi-band image",
      "link": "https://www.orfeo-toolbox.org/CookBook/Applications/app_BandMathX.html"
    },
    {
      "title": "OGC 09-146r8 Coverage Implementation Schema (CIS) 1.1.1, \u00a76.5 RangeType",
      "link": "https://docs.ogc.org/is/09-146r8/09-146r8.html"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix gp: <https://geolabs.github.io/bblocks-generic-profiles/def/> .
@prefix ns1: <https://w3id.org/ogc/api/schema/> .
@prefix ns2: <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/> .
@prefix ns3: <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband> a skos:Concept ;
    dcterms:source [ dcterms:references <https://www.ogc.org/standards/wcps/> ;
            dcterms:title "OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard" ],
        [ dcterms:references <https://docs.ogc.org/is/09-146r8/09-146r8.html> ;
            dcterms:title "OGC 09-146r8 Coverage Implementation Schema (CIS) 1.1.1, §6.5 RangeType" ],
        [ dcterms:references <https://www.orfeo-toolbox.org/CookBook/Applications/app_BandMathX.html> ;
            dcterms:title "OTB BandMathX -- Performs mathematical operations on several multiband images, outputting a mono- or multi-band image" ] ;
    skos:definition "Evaluates a user-supplied, possibly vector-valued mathematical expression per pixel across one or more input rasters, producing an output raster with one or more bands." ;
    skos:inScheme gp:implementation-profile ;
    skos:prefLabel "Raster band math (multi-band output)" ;
    gp:inputs [ ns3:expression <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/inputs/expression> ;
            ns3:rasters <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/inputs/rasters> ] ;
    gp:outputs [ ns2:raster <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/outputs/raster> ] ;
    gp:refinesGenericProfile <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math> ;
    gp:status "submitted" ;
    proc:keywords "BandMathX",
        "OTB",
        "band math",
        "coverage",
        "multi-band",
        "raster" ;
    proc:metadata [ dcterms:title "Process Concept: Raster Coverage Processing" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/concept/raster-coverage-processing> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/concept> ],
        [ dcterms:title "Generic Profile: Raster band math" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math> ;
            proc:role <http://www.opengis.net/spec/wps/2.0/def/process-profile/generic> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/inputs/expression> dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/string> ;
    proc:keywords "expression" ;
    proc:metadata [ dcterms:title "Generic Profile: Raster band math -- input `expression`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/expression> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/inputs/rasters> dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster> ;
    proc:keywords "GeoTIFF",
        "raster" ;
    proc:maxOccurs "unbounded" ;
    proc:metadata [ dcterms:title "Generic Profile: Raster band math -- input `rasters`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/inputs/rasters> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] ;
    proc:schema [ a ns1:string ;
            ns1:contentEncoding "base64" ;
            ns1:contentMediaType "image/tiff" ;
            ns1:description "GeoTIFF" ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/outputs/raster> dcterms:type <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster> ;
    proc:keywords "GeoTIFF",
        "raster" ;
    proc:metadata [ dcterms:title "Generic Profile: Raster band math -- output `raster`" ;
            proc:href <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/raster-band-math/outputs/raster> ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output> ] ;
    proc:schema [ a ns1:string ;
            ns1:contentEncoding "base64" ;
            ns1:contentMediaType "image/tiff" ;
            ns1:description "GeoTIFF" ] .


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
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/inputs/rasters
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster
              x-jsonld-id: http://purl.org/dc/terms/type
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
              const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type/string
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
          properties:
            id:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/raster-band-math-multiband/outputs/raster
              x-jsonld-id: '@id'
            dataType:
              const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster
              x-jsonld-id: http://purl.org/dc/terms/type
              x-jsonld-type: '@id'
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/outputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/
x-jsonld-extra-terms:
  ImplementationProfile: http://www.w3.org/2004/02/skos/core#Concept
  definition: http://www.w3.org/2004/02/skos/core#definition
  inScheme:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#inScheme
    x-jsonld-type: '@id'
  status: https://geolabs.github.io/bblocks-generic-profiles/def/status
  source: http://purl.org/dc/terms/source
  title: http://purl.org/dc/terms/title
  link:
    x-jsonld-id: http://purl.org/dc/terms/references
    x-jsonld-type: '@id'
x-jsonld-prefixes:
  skos: http://www.w3.org/2004/02/skos/core#
  gp: https://geolabs.github.io/bblocks-generic-profiles/def/
  proc: https://w3id.org/ogc/api/processes/
  dct: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/raster-band-math-multiband/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/raster-band-math-multiband/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "ImplementationProfile": "skos:Concept",
    "id": "@id",
    "type": "@type",
    "prefLabel": "skos:prefLabel",
    "definition": "skos:definition",
    "inScheme": {
      "@id": "skos:inScheme",
      "@type": "@id"
    },
    "status": "gp:status",
    "refinesGenericProfile": {
      "@id": "gp:refinesGenericProfile",
      "@type": "@id"
    },
    "keywords": "proc:keywords",
    "metadata": {
      "@context": {
        "role": {
          "@id": "proc:role",
          "@type": "@id"
        },
        "href": {
          "@id": "proc:href",
          "@type": "@id"
        }
      },
      "@id": "proc:metadata"
    },
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
        "maxOccurs": "proc:maxOccurs"
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
        }
      },
      "@id": "gp:outputs"
    },
    "source": "dct:source",
    "title": "dct:title",
    "link": {
      "@id": "dct:references",
      "@type": "@id"
    },
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "gp": "https://geolabs.github.io/bblocks-generic-profiles/def/",
    "proc": "https://w3id.org/ogc/api/processes/",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/raster-band-math-multiband/context.jsonld)

## Sources

* [OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard](https://www.ogc.org/standards/wcps/)
* [OTB BandMathX -- Performs mathematical operations on several multiband images, outputting a mono- or multi-band image](https://www.orfeo-toolbox.org/CookBook/Applications/app_BandMathX.html)
* [OGC 09-146r8 Coverage Implementation Schema (CIS) 1.1.1, §6.5 RangeType](https://docs.ogc.org/is/09-146r8/09-146r8.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/implementation-profile/raster-band-math-multiband`

