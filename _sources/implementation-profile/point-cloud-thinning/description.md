Implementation Profile: **Point cloud thinning (simple)**.

> Reduces the number of points to the given percentage by sequential point removal, which suits points stored in chronological order best.

## Data

- input `points`: `point-cloud`, LAS (OGC 17-030r1); application/vnd.las is the IANA-registered media type
- input `percentage`: `number`, no format to declare
- output `result`: `point-cloud`, LAS (OGC 17-030r1); application/vnd.las is the IANA-registered media type

The declared format is a minimal default; a real implementation may support others (Table 21,
footnote d). For point clouds, it labels LAS `application/x-ogc-lasf`, not the IANA-registered `application/vnd.las` declared here.

## Source

- [SAGA 7.3.0 -- Point Cloud Thinning (Simple)](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/pointcloud_tools_9.html)
- [ZOO-Project Geonovum testbed -- SAGA.pointcloud_tools.9: Point Cloud Thinning (Simple)](https://host1.tb.geonovum.geolabs.fr/ogc-api/processes/SAGA.pointcloud_tools.9)

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.point-cloud-thinning`](../../generic-profile/point-cloud-thinning/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of
this register: see `ospd.process-profiles.*` in `bblocks-process-profiles` -- a real process of
the ZOO-Project Geonovum testbed.
