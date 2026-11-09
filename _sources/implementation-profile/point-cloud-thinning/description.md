Implementation Profile: **Point cloud thinning (simple)**.

> Implementation Profile of the operation Point cloud thinning (simple), whose meaning is its activity type (activityType): the signature of the Generic Profile Point cloud thinning, bound to data exchange formats.

## Activity type

The meaning of the operation -- its definition, the standards that define it and its illustration --
is the activity type [`generic-profiles.activity-type.point-cloud-thinning`](../../activity-type/point-cloud-thinning/), to which this
profile points with `activityType` (decisions D3 and D4).

## Signature and representations

The signature of the Generic Profile [Point cloud thinning](../../generic-profile/point-cloud-thinning/), with each data-carrying
input and output bound to a representation of the
[`bblocks-data-formats`](https://github.com/GeoLabs/bblocks-data-formats) register (Table 21 Data
format, D; decision D6):

| Role | Data type | Representation |
|---|---|---|
| input `points` | `point-cloud` | [`point-cloud-las`](https://w3id.org/geolabs-ospd/data-formats/representation/point-cloud-las) (Point cloud as LAS) |
| input `percentage` | `number` | -- |
| output `result` | `point-cloud` | [`point-cloud-las`](https://w3id.org/geolabs-ospd/data-formats/representation/point-cloud-las) (Point cloud as LAS) |

The representations are a minimal default: a deployment may support more formats (OGC 14-065 WPS
2.0.2 §7.5.4 Table 21, footnote d).

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
- `activityType`: [`generic-profiles.activity-type.point-cloud-thinning`](../../activity-type/point-cloud-thinning/)

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
- `representation-2026-11-09`, substantive
- `tools-2026-11-09`, clarifying
