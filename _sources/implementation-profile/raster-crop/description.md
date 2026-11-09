Implementation Profile: **Raster crop**.

> Implementation Profile of the operation Raster crop, whose meaning is its activity type (activityType): the signature of the Generic Profile Raster crop, bound to data exchange formats.

## Activity type

The meaning of the operation -- its definition, the standards that define it and its illustration --
is the activity type [`generic-profiles.activity-type.raster-crop`](../../activity-type/raster-crop/), to which this
profile points with `activityType` (decisions D3 and D4).

## Signature and representations

The signature of the Generic Profile [Raster crop](../../generic-profile/raster-crop/), with each data-carrying
input and output bound to a representation of the
[`bblocks-data-formats`](https://github.com/GeoLabs/bblocks-data-formats) register (Table 21 Data
format, D; decision D6):

| Role | Data type | Representation |
|---|---|---|
| input `raster` | `raster` | [`raster-geotiff`](https://w3id.org/geolabs-ospd/data-formats/representation/raster-geotiff) (Raster as GeoTIFF) |
| input `areaOfInterest` | `bounding-box` | [`bounding-box-ogcapi-processes-bbox`](https://w3id.org/geolabs-ospd/data-formats/representation/bounding-box-ogcapi-processes-bbox) (Bounding box as OGC API - Processes bbox) |
| output `raster` | `raster` | [`raster-geotiff`](https://w3id.org/geolabs-ospd/data-formats/representation/raster-geotiff) (Raster as GeoTIFF) |

The representations are a minimal default: a deployment may support more formats (OGC 14-065 WPS
2.0.2 §7.5.4 Table 21, footnote d).

## Source

Two standards define this operation at different levels -- the abstract semantics, and the
concrete tool binding an Implementation Profile is specifically meant to add (OGC 14-065 WPS
2.0.2 §7.5.3, "down to the supported data exchange formats"):

- [OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard](https://www.ogc.org/standards/wcps/)
  -- the OGC standards-track evidence that this kind of coverage operation is a recognised,
  harmonised processing concept (this is what [its Concept](../../concept/raster-coverage-processing/)
  and [Generic Profile](../../generic-profile/raster-crop/) are grounded in too). Unlike
  SQL/MM for the vector Implementation Profiles, WCPS is not the language this operation is
  actually bound to below -- GDAL/OTB, not WCPS, is what the Geonovum testbed runs.
- [OTB ExtractROI -- Extracts a region of interest defined by the user](https://www.orfeo-toolbox.org/CookBook/Applications/app_ExtractROI.html) -- the concrete software binding: a
  widely deployed, de facto standard implementation (not itself an ISO/OGC standard, unlike
  SQL/MM's formal status for the vector operations) that the Geonovum testbed's own
  [`OTB.ExtractROI`](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/OTB.ExtractROI)
  process wraps directly.
- [OGC 17-069r4 OGC API - Features - Part 1: Core](https://docs.ogc.org/is/17-069r4/17-069r4.html),
  §7.15.3 -- defines the `bbox` parameter (an array of 4 or 6 numbers) that
  `ogc.api.processes.v1.schemas.bbox` (below) itself cites as its own source.

## Data format

`raster` (input and output): the representation `raster-geotiff` (GeoTIFF; until 2026-11-09 a
`schema` of `{type: string, contentEncoding: base64, contentMediaType: image/tiff}`) -- grounded in `OTB.ExtractROI`'s own processDescription
(`in`/`out` both declare `image/tiff`, `image/jpeg`, `image/png`; GeoTIFF kept as the
georeferencing-capable default).

`areaOfInterest`: the representation `bounding-box-ogcapi-processes-bbox`, whose format
`ogcapi-processes-bbox` (bblocks-data-formats) `$ref`s
[`ogc.api.processes.v1.schemas.bbox`](https://geolabs.github.io/bblocks-ogcapi-processes/)'s own
published schema directly (until 2026-11-09 this role's own `schema` did) (`{bbox: [4 or 6 numbers], crs: CRS84|CRS84h}`) -- OGC API - Processes
- Part 1: Core's own bbox type, not a bespoke format string, and grounded directly in
`OTB.ExtractROI`'s own "extent" mode (`mode.extent.ulx`/`uly`/`lrx`/`lry`, four plain numbers).
This Implementation Profile's Generic Profile originally typed `areaOfInterest` as `Geometry`,
which did not match -- see [`raster-crop`](../../generic-profile/raster-crop/)'s own "Why
`areaOfInterest` is `BoundingBox`, not `Geometry`" for that fix, now superseded in turn by
reusing `ogc.api.processes.v1.schemas.bbox` directly rather than inventing a `BoundingBox`
abstract type and a `"BBOX"` format string (see the repository README, "OGC API - Processes
alignment"). `eoap.cct.bbox` (bblocks-eoap-cct) is a *different* type, for CWL inputs/outputs
crossing into OGC API - Processes - Part 2: Deploy, Replace, Undeploy, not used here.
`OTB.ExtractROI`'s other three modes (`standard`, `radius`, `fit`) each use a different parameter
shape again (pixel offset/size, a circle, a reference image/vector) -- none of them a bbox or an
encoded geometry either, and not modelled here.

Per [OGC 14-065 WPS 2.0.2 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065.html#32), a specific deployment may *Extend* (E, footnote d) this minimal default with additional formats it happens to support -- this tier intentionally does not pre-empt that.

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.raster-crop`](../../generic-profile/raster-crop/)
- `activityType`: [`generic-profiles.activity-type.raster-crop`](../../activity-type/raster-crop/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of this
register: deployed processes are profiled in `bblocks-process-profiles`, and name this profile with
`implementsProfile`. Tools, hosts and testbeds are recorded there; this item carries none as
keyword or source (decision D4). The sections above keep the tools and testbed that its defaults
were grounded in.

## Changes

A proposal, amended in place on 2026-11-09 (`gp:amendmentAction`):

- `meaning-2026-11-09`, substantive
- `operation-sources-2026-11-09`, clarifying
- `representation-2026-11-09`, substantive
- `tools-2026-11-09`, clarifying
