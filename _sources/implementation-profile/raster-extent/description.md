Implementation Profile: **Raster extent**.

> Implementation Profile of the operation Raster extent, whose meaning is its activity type (activityType): the signature of the Generic Profile Raster extent, bound to data exchange formats.

## Activity type

The meaning of the operation -- its definition, the standards that define it and its illustration --
is the activity type [`generic-profiles.activity-type.raster-extent`](../../activity-type/raster-extent/), to which this
profile points with `activityType` (decisions D3 and D4).

## Signature and representations

The signature of the Generic Profile [Raster extent](../../generic-profile/raster-extent/), with each data-carrying
input and output bound to a representation of the
[`bblocks-data-formats`](https://github.com/GeoLabs/bblocks-data-formats) register (Table 21 Data
format, D; decision D6):

| Role | Data type | Representation |
|---|---|---|
| input `raster` | `raster` | [`raster-geotiff`](https://w3id.org/geolabs-ospd/data-formats/representation/raster-geotiff) (Raster as GeoTIFF) |
| output `result` | `surface` | [`surface-gml`](https://w3id.org/geolabs-ospd/data-formats/representation/surface-gml) (Surface as GML) |

The representations are a minimal default: a deployment may support more formats (OGC 14-065 WPS
2.0.2 §7.5.4 Table 21, footnote d).

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

`raster`: the representation `raster-geotiff` (GeoTIFF; until 2026-11-09 a `schema` of
`{type: string, contentEncoding: base64, contentMediaType: image/tiff}`) -- the register's minimal default (Table 21, D: Declare), consistent with every other
raster Implementation Profile in this register (not grounded in `OTB.ImageEnvelope`'s own `in`
the same way `OTB.BandMath`'s `il` is -- its schema was not individually re-checked here, GeoTIFF
follows this tier's general raster-input convention).

`result`: the representation `surface-gml` (GML; until 2026-11-09 a `schema` of
`{type: string, contentMediaType: text/xml}`) -- grounded in
`OTB.ImageEnvelope`'s own `out`, which declares `text/xml` (GML),
`application/vnd.google-earth.kml+xml` (KML), `object` and `application/zip`; GML is kept as this
tier's minimal baseline, consistent with every vector-typed output elsewhere in this register.
Not the bbox representation (`bounding-box-ogcapi-processes-bbox`, whose format `$ref`s
`ogc.api.processes.part1.v1.schemas.bbox`) that [`raster-crop`](../raster-crop/)'s `areaOfInterest` uses -- this output is a real polygon, not a
plain numeric extent.

Per [OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32), a
specific deployment may *Extend* (E, footnote d) this minimal default -- this tier intentionally
does not pre-empt that.

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.raster-extent`](../../generic-profile/raster-extent/)
- `activityType`: [`generic-profiles.activity-type.raster-extent`](../../activity-type/raster-extent/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see [`ospd.process-profiles.raster.extent`](https://github.com/GeoLabs/bblocks-process-profiles/tree/master/_sources/raster/extent)
in `bblocks-process-profiles` -- a real process of the ZOO-Project Geonovum testbed
(<https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.ImageEnvelope>).

That process names this profile with `implementsProfile`. Tools, hosts and testbeds are
recorded there; this item carries none as keyword or source (decision D4). The sections
above keep the tools and testbed that its defaults were grounded in.

## Changes

A proposal, amended in place on 2026-11-09 (`gp:amendmentAction`):

- `meaning-2026-11-09`, substantive
- `operation-sources-2026-11-09`, clarifying
- `representation-2026-11-09`, substantive
- `tools-2026-11-09`, clarifying
- `sections-restored-2026-11-09`, clarifying
