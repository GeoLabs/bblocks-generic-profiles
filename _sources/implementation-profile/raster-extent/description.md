Implementation Profile: **Raster extent**.

> Computes the bounding envelope of a raster coverage, as a vector polygon.

## Source

- [OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard](https://www.ogc.org/standards/wcps/)
  -- the OGC standards-track evidence that this kind of coverage operation is a recognised,
  harmonised processing concept (this is what [its Concept](../../concept/raster-coverage-processing/)
  and [Generic Profile](../../generic-profile/raster-extent/) are grounded in too).
- [OTB ImageEnvelope -- Build a vector data containing the image envelope polygon](https://www.orfeo-toolbox.org/CookBook/Applications/app_ImageEnvelope.html)
  -- the concrete software binding the Geonovum testbed actually runs,
  [`OTB.ImageEnvelope`](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.ImageEnvelope):
  takes a raster (`in`) and returns a vector polygon (`out`, GML/KML/`object`/zip) representing its
  envelope, in a requestable output projection (`proj`), optionally densified along the edges
  (`sr`, sampling rate) -- the real evidence that this operation's output is a vector polygon,
  not a plain four-number bounding box (see [its Generic Profile](../../generic-profile/raster-extent/)
  for why that distinction matters).

## Data format

`raster`: a `schema` of `{type: string, contentEncoding: base64, contentMediaType: image/tiff}`
(GeoTIFF) -- the register's minimal default (Table 21, D: Declare), consistent with every other
raster Implementation Profile in this register (not grounded in `OTB.ImageEnvelope`'s own `in`
the same way `OTB.BandMath`'s `il` is -- its schema was not individually re-checked here, GeoTIFF
follows this tier's general raster-input convention).

`result`: a `schema` of `{type: string, contentMediaType: text/xml}` (GML) -- grounded in
`OTB.ImageEnvelope`'s own `out`, which declares `text/xml` (GML),
`application/vnd.google-earth.kml+xml` (KML), `object` and `application/zip`; GML is kept as this
tier's minimal baseline, consistent with every vector-typed output elsewhere in this register.
Not a `$ref` to `ogc.api.processes.v1.schemas.bbox` the way
[`raster-crop`](../raster-crop/)'s `areaOfInterest` is -- this output is a real polygon, not a
plain numeric extent.

Per [OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32), a
specific deployment may *Extend* (E, footnote d) this minimal default -- this tier intentionally
does not pre-empt that.

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.raster-extent`](../../generic-profile/raster-extent/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.raster.extent` in `bblocks-process-profiles` -- a real
process of the ZOO-Project Geonovum testbed
(<https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.ImageEnvelope>).
