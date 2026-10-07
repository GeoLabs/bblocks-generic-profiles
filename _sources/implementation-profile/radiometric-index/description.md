Implementation Profile: **Radiometric index**.

> Computes one or more named radiometric indices (e.g. NDVI, NDWI, SAVI) from the relevant spectral channels of the input raster(s).

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

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.*` in `bblocks-process-profiles` -- real processes of
the ZOO-Project Geonovum testbed
(<https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.RadiometricIndices>).
