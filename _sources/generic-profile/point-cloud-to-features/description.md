Generic Profile: **Point cloud to features**.

> Converts a point cloud to a feature collection. One point cloud in, one feature collection out.

## Signature

| | Name | Data type | Description |
|---|---|---|---|
| input | `points` | [`point-cloud`](../../data-type/) | the input point cloud |
| output | `result` | [`feature-collection`](../../data-type/) | one feature per point, its attributes as feature attributes |

## Source

- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic Profile is.
- The operations below are each grounded in their own SAGA 7.3.0 tool documentation (see each
  Implementation Profile).

## Relations

- `broader`: [`generic-profiles.concept.point-cloud-processing`](../../concept/point-cloud-processing/)
- Refined by (1 Implementation Profile): [`point-cloud-to-shapes`](../../implementation-profile/point-cloud-to-shapes/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).
