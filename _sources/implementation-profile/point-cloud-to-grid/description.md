Implementation Profile: **Point cloud to grid**.

> Writes one value per grid cell from the points falling in it -- by default the z value of the first point -- as a single-band raster.

## Data

- input `points`: `point-cloud`, LAS (OGC 17-030r1); application/vnd.las is the IANA-registered media type
- input `cellSize`: `number`, no format to declare
- output `result`: `raster-single-band`, GeoTIFF

Narrowed data types: `result` (output): `raster-single-band`, narrower than the Generic Profile's `raster`.

The declared format is a minimal default; a real implementation may support others (Table 21,
footnote d). For rasters, the Geonovum testbed's SAGA also serves ESRI ASCII grids, ENVI and PNG. For point clouds, it labels LAS `application/x-ogc-lasf`, not the IANA-registered `application/vnd.las` declared here.

## Source

- [SAGA 7.3.0 -- Point Cloud to Grid](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/pointcloud_tools_4.html)
- [ZOO-Project Geonovum testbed -- SAGA.pointcloud_tools.4: Point Cloud to Grid](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.4)

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.point-cloud-rasterization`](../../generic-profile/point-cloud-rasterization/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.*` in `bblocks-process-profiles` -- a real process of
the ZOO-Project Geonovum testbed.
