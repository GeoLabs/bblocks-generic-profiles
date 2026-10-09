Generic Profile: **Point cloud rasterization**.

> Converts a point cloud to a raster on a grid of a given cell size. One point cloud and one cell size in, one raster out.

## Signature

| | Name | Data type | Description |
|---|---|---|---|
| input | `points` | [`point-cloud`](../../data-type/) | the input point cloud |
| input | `cellSize` | [`number`](../../data-type/) | the cell size of the output grid |
| output | `result` | [`raster`](../../data-type/) | the point cloud's attribute(s) on the grid |

## Source

- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic Profile is.
- The operations below are each grounded in their own SAGA 7.3.0 tool documentation (see each
  Implementation Profile).

## Relations

- `broader`: [`generic-profiles.concept.point-cloud-processing`](../../concept/point-cloud-processing/)
- Refined by (1 Implementation Profile): [`point-cloud-to-grid`](../../implementation-profile/point-cloud-to-grid/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).
