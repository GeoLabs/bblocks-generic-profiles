Generic Profile: **Analytical hillshading**.

> Computes how the terrain is lit by a light source. One elevation model and the light source's azimuth and altitude in, one single-band raster out.

## Signature

| | Name | Data type | Description |
|---|---|---|---|
| input | `elevation` | [`elevation-model`](../../data-type/) | the elevation model |
| input | `azimuth` | [`number`](../../data-type/) | the light source's direction, in degrees clockwise from north |
| input | `altitude` | [`number`](../../data-type/) | the light source's height above the horizon, in degrees |
| output | `result` | [`raster-single-band`](../../data-type/) | the shaded relief |

## Source

- [OGC 14-065 WPS 2.0.2](https://docs.ogc.org/is/14-065/14-065.html) §7.5.2 -- what a Generic Profile is.
- The operations below are each grounded in their own SAGA 7.3.0 tool documentation (see each
  Implementation Profile).

## Relations

- `broader`: [`generic-profiles.concept.terrain-analysis`](../../concept/terrain-analysis/)
- Refined by (1 Implementation Profile): [`analytical-hillshading`](../../implementation-profile/analytical-hillshading/)

## Register position

Second tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> **Generic Profile** ->
Implementation Profile -> Implementation (instance level).
