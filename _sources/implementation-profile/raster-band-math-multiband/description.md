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

`rasters`: restricted (Table 21, R, footnote c) to a maximum of 1024 -- `OTB.BandMathX`'s own
`il` input declares `maxOccurs: 1024`, the same cap as `OTB.BandMath`, narrowing the Generic
Profile's abstract "one-or-many".

Per [OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32), a specific deployment may *Extend* (E, footnote d) this minimal default with additional formats it happens to support -- this tier intentionally does not pre-empt that.

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.raster-band-math`](../../generic-profile/raster-band-math/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.raster.band-math-multiband` in
`bblocks-process-profiles` -- a real process of the ZOO-Project Geonovum testbed
(<https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.BandMathX>).
