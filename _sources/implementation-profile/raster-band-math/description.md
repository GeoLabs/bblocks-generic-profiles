Implementation Profile: **Raster band math**.

> Implementation Profile of the operation Raster band math, whose meaning is its activity type (activityType): the signature of the Generic Profile Raster band math, bound to data exchange formats.

## Activity type

The meaning of the operation -- its definition, the standards that define it and its illustration --
is the activity type [`generic-profiles.activity-type.raster-band-math`](../../activity-type/raster-band-math/), to which this
profile points with `activityType` (decisions D3 and D4).

## Signature and representations

The signature of the Generic Profile [Raster band math](../../generic-profile/raster-band-math/), with each data-carrying
input and output bound to a representation of the
[`bblocks-data-formats`](https://github.com/GeoLabs/bblocks-data-formats) register (Table 21 Data
format, D; decision D6):

| Role | Data type | Representation |
|---|---|---|
| input `rasters` (minOccurs 1, maxOccurs unbounded) | `raster` | [`raster-geotiff`](https://w3id.org/geolabs-ospd/data-formats/representation/raster-geotiff) (Raster as GeoTIFF) |
| input `expression` | `expression` | -- |
| output `raster` | `raster-single-band` | [`raster-single-band-geotiff`](https://w3id.org/geolabs-ospd/data-formats/representation/raster-single-band-geotiff) (Single-band raster as GeoTIFF) |

The representations are a minimal default: a deployment may support more formats (OGC 14-065 WPS
2.0.2 §7.5.4 Table 21, footnote d).

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

`rasters`: `maxOccurs: unbounded`, as in the Generic Profile. Any practical cap belongs to a real
implementation, not to this tier. Nothing is restricted here (Table 21 would allow it, R, footnote c: "Implementation
profiles may restrict the maximum cardinality of a superior generic profile... They shall not
modify the minimum cardinality."

Per [OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32), a specific deployment may *Extend* (E, footnote d) this minimal default with additional formats it happens to support -- this tier intentionally does not pre-empt that.

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.raster-band-math`](../../generic-profile/raster-band-math/)
- `activityType`: [`generic-profiles.activity-type.raster-band-math`](../../activity-type/raster-band-math/)
- Sibling of [`raster-band-math-multiband`](../raster-band-math-multiband/) (`OTB.BandMathX`/
  muParserX, may produce several bands): both refine the same Generic Profile, since the
  distinction between them is a band-count/format detail, not a signature difference -- see the
  sibling's "Open question" section for how that distinction is expressed (by the output dataType,
  `raster-single-band` here) and what is not expressed yet (which bands).

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see [`ospd.process-profiles.raster.band-math`](https://github.com/GeoLabs/bblocks-process-profiles/tree/master/_sources/raster/band-math)
in `bblocks-process-profiles` -- a real process of the ZOO-Project Geonovum testbed
(<https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.BandMath>).

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
