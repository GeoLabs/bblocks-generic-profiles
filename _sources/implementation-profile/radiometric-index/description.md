Implementation Profile: **Radiometric index**.

> Implementation Profile of the operation Radiometric index, whose meaning is its activity type (activityType): the signature of the Generic Profile Radiometric index, bound to data exchange formats.

## Activity type

The meaning of the operation -- its definition, the standards that define it and its illustration --
is the activity type [`generic-profiles.activity-type.radiometric-index`](../../activity-type/radiometric-index/), to which this
profile points with `activityType` (decisions D3 and D4).

## Signature and representations

The signature of the Generic Profile [Radiometric index](../../generic-profile/radiometric-index/), with each data-carrying
input and output bound to a representation of the
[`bblocks-data-formats`](https://github.com/GeoLabs/bblocks-data-formats) register (Table 21 Data
format, D; decision D6):

| Role | Data type | Representation |
|---|---|---|
| input `rasters` (minOccurs 1, maxOccurs 1) | `raster` | [`raster-geotiff`](https://w3id.org/geolabs/ospd/data-formats/representation/raster-geotiff) (Raster as GeoTIFF) |
| input `index` | `radiometric-index` | -- |
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
  and [Generic Profile](../../generic-profile/radiometric-index/) are grounded in too). Unlike
  SQL/MM for the vector Implementation Profiles, WCPS is not the language this operation is
  actually bound to below -- GDAL/OTB, not WCPS, is what the Geonovum testbed runs.
- [OTB RadiometricIndices -- Computes radiometric indices from the relevant channels of the input image](https://www.orfeo-toolbox.org/CookBook/Applications/app_RadiometricIndices.html) -- the concrete software binding: a
  widely deployed, de facto standard implementation (not itself an ISO/OGC standard, unlike
  SQL/MM's formal status for the vector operations) that the Geonovum testbed's own
  [`OTB.RadiometricIndices`](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.RadiometricIndices)
  process wraps directly.

## Data formats

`rasters`, `raster` (output): GeoTIFF -- grounded the same way as `raster-band-math`: OTB's own
`in`/`out` declare exactly `image/tiff`, `image/jpeg`, `image/png`; GeoTIFF is the
georeferencing-capable member kept as the default.

## Multiplicity

`rasters`: restricted (Table 21, R, footnote c) to exactly one -- unlike `OTB.BandMath`/
`OTB.BandMathX`'s `il` (an image list), `OTB.RadiometricIndices`' own `in` input is a *single*
pre-stacked multi-band image (the red/nir/green/mir channels are selected from within it via
`channels.red`/`channels.nir`/...); the Generic Profile's abstract "one-or-many" is narrowed all
the way down to one here.

Per [OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32), a specific deployment may *Extend* (E, footnote d) this minimal default with additional formats it happens to support -- this tier intentionally does not pre-empt that.

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.radiometric-index`](../../generic-profile/radiometric-index/)
- `activityType`: [`generic-profiles.activity-type.radiometric-index`](../../activity-type/radiometric-index/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see [`ospd.process-profiles.raster.radiometric-index`](https://github.com/GeoLabs/bblocks-process-profiles/tree/master/_sources/raster/radiometric-index)
in `bblocks-process-profiles` -- a real process of the ZOO-Project Geonovum testbed
(<https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.RadiometricIndices>).

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
