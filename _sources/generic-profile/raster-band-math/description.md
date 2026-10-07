Generic Profile: **Raster band math**.

> Derives a new raster from one or more input rasters via a user-supplied mathematical expression
> evaluated per pixel. One or more Raster inputs, an expression, one Raster output.

## Source

- ISO 19123-1:2023 *Geographic information -- Schema for coverage geometry and functions -- Part
  1: Fundamentals* -- the abstract coverage domain/range model this signature is grounded in (see
  [its Concept](../../concept/raster-coverage-processing/) for the full citation).
- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic
  Profile is.

## Why one Generic Profile, not two

An earlier draft of this register split this into two Generic Profiles -- one for a
fixed-one-band output (`OTB.BandMath`/muParser), one for a possibly-multi-band output
(`OTB.BandMathX`/muParserX) -- and tried to express the difference with `cardinality: one-or-many`
on the output. That was wrong on two counts: first, a multi-band raster is still exactly **one**
Raster output value, not several -- `cardinality` describes how many separate output values a
process returns, not the internal band structure of one of them (see the base
`generic-profile.schema.yaml`'s own note on this). Second, and more fundamentally, WPS §7.5.2's
"signature for process inputs and outputs" is about which *parameters* exist, at what abstract
type -- both variants have the identical signature: Raster(s), Expression -> Raster. What
distinguishes them (how many bands the result happens to have) is exactly WPS §7.5.3's territory,
"down to the supported data exchange formats" -- Implementation Profile, not Generic Profile. See
[`raster-band-math-multiband`](../../implementation-profile/raster-band-math-multiband/)'s own
`description.md` for where that distinction now lives, and for the still-open question of how to
express it formally.

## Relations

- `broader`: [`generic-profiles.concept.raster-coverage-processing`](../../concept/raster-coverage-processing/)
- Refined by (2 Implementation Profiles):
- [`raster-band-math`](../../implementation-profile/raster-band-math/) -- fixed to one band (`OTB.BandMath`/muParser)
- [`raster-band-math-multiband`](../../implementation-profile/raster-band-math-multiband/) -- may produce several bands (`OTB.BandMathX`/muParserX)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).
