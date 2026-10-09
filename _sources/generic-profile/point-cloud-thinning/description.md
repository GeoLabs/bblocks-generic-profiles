Generic Profile: **Point cloud thinning**.

> Reduces the number of points of a point cloud. One point cloud and the share of points to keep in, one point cloud out.

## Signature

| | Name | Data type | Description |
|---|---|---|---|
| input | `points` | [`point-cloud`](../../data-type/) | the input point cloud |
| input | `percentage` | [`number`](../../data-type/) | the share of points to keep, in percent |
| output | `result` | [`point-cloud`](../../data-type/) | the thinned point cloud |

## Source

- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic Profile is.
- The operations below are each grounded in their own SAGA 7.3.0 tool documentation (see each
  Implementation Profile).

## Relations

- `broader`: [`generic-profiles.concept.point-cloud-processing`](../../concept/point-cloud-processing/)
- Refined by (1 Implementation Profile): [`point-cloud-thinning`](../../implementation-profile/point-cloud-thinning/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).
