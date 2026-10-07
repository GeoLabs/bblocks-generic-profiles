Implementation Profile: **Raster reprojection**.

> Reprojects a raster coverage to another coordinate reference system, resampling pixel values as needed, preserving the coverage's content.

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

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.*` in `bblocks-process-profiles` -- real processes of
the ZOO-Project Geonovum testbed
(<https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Gdal_Warp>).
