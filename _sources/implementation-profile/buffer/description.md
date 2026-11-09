Implementation Profile: **Buffer**.

> Implementation Profile of the operation Buffer, whose meaning is its activity type (activityType): the signature of the Generic Profile Geometry buffer, bound to data exchange formats.

## Activity type

The meaning of the operation -- its definition, the standards that define it and its illustration --
is the activity type [`generic-profiles.activity-type.buffer`](../../activity-type/buffer/), to which this
profile points with `activityType` (decisions D3 and D4).

## Signature and representations

The signature of the Generic Profile [Geometry buffer](../../generic-profile/geometry-buffer/), with each data-carrying
input and output bound to a representation of the
[`bblocks-data-formats`](https://github.com/GeoLabs/bblocks-data-formats) register (Table 21 Data
format, D; decision D6):

| Role | Data type | Representation |
|---|---|---|
| input `geometry` | `geometry` | [`geometry-gml`](https://w3id.org/geolabs-ospd/data-formats/representation/geometry-gml) (Geometry as GML) |
| input `distance` | `number` | -- |
| output `result` | `surface` | [`surface-gml`](https://w3id.org/geolabs-ospd/data-formats/representation/surface-gml) (Surface as GML) |

The representations are a minimal default: a deployment may support more formats (OGC 14-065 WPS
2.0.2 §7.5.4 Table 21, footnote d).

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.geometry-buffer`](../../generic-profile/geometry-buffer/)
- `activityType`: [`generic-profiles.activity-type.buffer`](../../activity-type/buffer/)

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level). The fourth tier is not part of this
register: deployed processes are profiled in `bblocks-process-profiles`, and name this profile with
`implementsProfile`. Tools, hosts and testbeds are recorded there, not here.

## Changes

A proposal, amended in place on 2026-11-09 (`gp:amendmentAction`):

- `meaning-2026-11-09`, substantive
- `operation-sources-2026-11-09`, clarifying
- `representation-2026-11-09`, substantive
- `tools-2026-11-09`, clarifying
