Implementation Profile: **Point cloud to shapes**.

> Converts a point cloud to a SAGA shapes layer of points, i.e. a feature collection.

## Data

- input `points`: `point-cloud`, LAS (OGC 17-030r1); application/vnd.las is the IANA-registered media type
- output `result`: `feature-collection`, GML

The declared format is a minimal default; a real implementation may support others (Table 21,
footnote d). For point clouds, it labels LAS `application/x-ogc-lasf`, not the IANA-registered `application/vnd.las` declared here. For shapes, it also serves KML.

## Source

- [SAGA 7.3.0 -- Point Cloud to Shapes](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/pointcloud_tools_5.html)
- [ZOO-Project Geonovum testbed -- SAGA.pointcloud_tools.5: Point Cloud to Shapes](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.5)

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.point-cloud-to-features`](../../generic-profile/point-cloud-to-features/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.*` in `bblocks-process-profiles` -- a real process of
the ZOO-Project Geonovum testbed.
