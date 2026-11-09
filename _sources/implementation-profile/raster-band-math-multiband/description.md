Implementation Profile: **Raster band math (multi-band output)**.

> Implementation Profile of the operation Raster band math (multi-band output), whose meaning is its activity type (activityType): the signature of the Generic Profile Raster band math, bound to data exchange formats.

## Activity type

The meaning of the operation -- its definition, the standards that define it and its illustration --
is the activity type [`generic-profiles.activity-type.raster-band-math-multiband`](../../activity-type/raster-band-math-multiband/), to which this
profile points with `activityType` (decisions D3 and D4).

## Signature and representations

The signature of the Generic Profile [Raster band math](../../generic-profile/raster-band-math/), with each data-carrying
input and output bound to a representation of the
[`bblocks-data-formats`](https://github.com/GeoLabs/bblocks-data-formats) register (Table 21 Data
format, D; decision D6):

| Role | Data type | Representation |
|---|---|---|
| input `rasters` (minOccurs 1, maxOccurs unbounded) | `raster` | [`raster-geotiff`](https://w3id.org/geolabs-ospd/data-formats/representation/raster-geotiff) (Raster as GeoTIFF) |
| input `expression` | `string` | -- |
| output `raster` | `raster` | [`raster-geotiff`](https://w3id.org/geolabs-ospd/data-formats/representation/raster-geotiff) (Raster as GeoTIFF) |

The representations are a minimal default: a deployment may support more formats (OGC 14-065 WPS
2.0.2 §7.5.4 Table 21, footnote d).

## Open question: how to say "one band" or "several bands"

This profile and its sibling [`raster-band-math`](../raster-band-math/) differ only in the band count
of the output: `raster-single-band` there, `raster` (one band or several) here. An earlier draft
expressed that with `cardinality: one-or-many` on the Generic Profile's output, which was wrong: a
multi-band raster is still **one** output value (see `raster-band-math`'s "Why one Generic Profile,
not two").

The standards-grounded mechanism is a coverage's range type:
[OGC 09-146r8 Coverage Implementation Schema (CIS) 1.1.1](https://docs.ogc.org/is/09-146r8/09-146r8.html)
§6.5 "RangeType" describes the band structure as a `SWE Common::DataRecord`, one named field per
band. **This register does not model a range type yet**: field names, per-field data types and how
a process declares what it contributes to the output range are a modelling task of their own, left
open. The data type says "one band" or "several", not which bands.

## Relations

- `refinesGenericProfile`: [`generic-profiles.generic-profile.raster-band-math`](../../generic-profile/raster-band-math/)
- `activityType`: [`generic-profiles.activity-type.raster-band-math-multiband`](../../activity-type/raster-band-math-multiband/)

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
