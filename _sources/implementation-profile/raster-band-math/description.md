Implementation Profile: **Raster band math**.

> Evaluates a user-supplied mathematical expression per pixel across one or more input rasters, producing a monoband output raster.

## Source

Two standards define this operation at different levels -- the abstract semantics, and the
concrete tool binding an Implementation Profile is specifically meant to add (OGC 14-065 WPS
2.0.2 §7.5.3, "down to the supported data exchange formats"):

- [OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard](https://www.ogc.org/standards/wcps/)
  -- the OGC standards-track evidence that this kind of coverage operation is a recognised,
  harmonised processing concept (this is what [its Concept](../../concept/raster-coverage-processing/)
  and [Generic Profile](../../generic-profile/raster-band-math/) are grounded in too). Unlike
  SQL/MM for the vector Implementation Profiles, WCPS is not the language this operation is
  actually bound to below -- GDAL/OTB, not WCPS, is what the Geonovum testbed runs.
- [OTB BandMath -- Outputs a monoband image from a mathematical operation on several multi-band images](https://www.orfeo-toolbox.org/CookBook/Applications/app_BandMath.html) -- the concrete software binding: a
  widely deployed, de facto standard implementation (not itself an ISO/OGC standard, unlike
  SQL/MM's formal status for the vector operations) that the Geonovum testbed's own
  [`OTB.BandMath`](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.BandMath)
  process wraps directly.

## Data formats

`rasters`, `raster` (output): GeoTIFF -- the register's minimal default (Table 21, D: Declare),
grounded in `OTB.BandMath`'s own processDescription, whose `il`/`out` both declare exactly three
media types (`image/tiff`, `image/jpeg`, `image/png`); GeoTIFF is kept here as the one
georeferencing-capable member of that set (plain JPEG/PNG carry no CRS).

## Multiplicity

`rasters`: restricted (Table 21, R, footnote c) to a maximum of 1024 -- `OTB.BandMath`'s own `il`
input declares `maxOccurs: 1024`, narrowing the Generic Profile's abstract "one-or-many". Table
21 footnote c: "Implementation profiles may restrict the maximum cardinality of a superior
generic profile... They shall not modify the minimum cardinality."

Per [OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32), a specific deployment may *Extend* (E, footnote d) this minimal default with additional formats it happens to support -- this tier intentionally does not pre-empt that.

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.raster-band-math`](../../generic-profile/raster-band-math/)
- Sibling of [`raster-band-math-multiband`](../raster-band-math-multiband/) (`OTB.BandMathX`/
  muParserX, may produce several bands): both refine the same Generic Profile, since the
  distinction between them is a band-count/format detail, not a signature difference -- see the
  sibling's "Open question" section for how that distinction is (not yet formally) expressed.

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.*` in `bblocks-process-profiles` -- real processes of
the ZOO-Project Geonovum testbed
(<https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.BandMath>).
