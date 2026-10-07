Implementation Profile: **Raster format conversion**.

> Re-encodes a raster coverage into another raster format, without altering its content.

## Source

Two standards define this operation at different levels -- the abstract semantics, and the
concrete tool binding an Implementation Profile is specifically meant to add (OGC 14-065 WPS
2.0.2 §7.5.3, "down to the supported data exchange formats"):

- [OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard](https://www.ogc.org/standards/wcps/)
  -- the OGC standards-track evidence that this kind of coverage operation is a recognised,
  harmonised processing concept (this is what [its Concept](../../concept/raster-coverage-processing/)
  and [Generic Profile](../../generic-profile/raster-format-conversion/) are grounded in too). Unlike
  SQL/MM for the vector Implementation Profiles, WCPS is not the language this operation is
  actually bound to below -- GDAL/OTB, not WCPS, is what the Geonovum testbed runs.
- [GDAL gdal_translate -- Converts raster data between formats](https://gdal.org/programs/gdal_translate.html) -- the concrete software binding: a
  widely deployed, de facto standard implementation (not itself an ISO/OGC standard, unlike
  SQL/MM's formal status for the vector operations) that the Geonovum testbed's own
  [`Gdal_Translate`](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Gdal_Translate)
  process wraps directly.

## Data formats

`raster` (input and output): GeoTIFF -- the register's minimal default (Table 21, D: Declare).
Not grounded in `Gdal_Translate`'s own processDescription either, for the same reason as
`raster-reprojection`: its `InputDSN`/`OutputDSN` are plain `string` DSNs, with no declared media
type. `targetFormat` (the input selecting which format to convert to) carries no data format of
its own -- it names one, it is not itself a payload.

Per [OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32), a specific deployment may *Extend* (E, footnote d) this minimal default with additional formats it happens to support -- this tier intentionally does not pre-empt that.

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.raster-format-conversion`](../../generic-profile/raster-format-conversion/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.*` in `bblocks-process-profiles` -- real processes of
the ZOO-Project Geonovum testbed
(<https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/Gdal_Translate>).
