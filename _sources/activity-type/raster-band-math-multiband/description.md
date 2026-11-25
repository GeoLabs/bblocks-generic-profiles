Activity type: **Raster band math (multi-band output)**.

> Evaluates a user-supplied, possibly vector-valued mathematical expression per pixel across one or more input rasters, producing an output raster with one or more bands.

**Withdrawn on 2026-11-19**, replaced by [`generic-profiles.activity-type.raster-band-math`](../raster-band-math/): Withdrawal of the proposal (decision of 2026-11-19). The operation is the same as raster-band-math; only the number of bands of the output differed, a matter of signature already enforced by the dataType of each Implementation Profile's output. raster-band-math, whose definition now covers one or more output bands, replaces it (dct:isReplacedBy), and the Implementation Profile raster-band-math-multiband points there. Nothing is deleted; the item stays, unpublished. Classified substantive, the retirement of a type.

## The item

`https://w3id.org/geolabs/ospd/generic-profiles/activity-type/raster-band-math-multiband` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate spatial data, declared with GeoSPARQL 1.1 classes: `usedEntityType` `geo:Feature`; `generatedEntityType` `geo:Feature`. The class is chosen per kind of role (see `scripts/activity-types.yaml`); how a data type of `bblocks-data-types` maps to an entity type is still open (decision D8, question 5).

The run of an activity of this type is not typed here (decision D8, open).

## Sources

- [OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard](https://www.ogc.org/standards/wcps/)
- [OGC 09-146r8 Coverage Implementation Schema (CIS) 1.1.1, §6.5 RangeType](https://docs.ogc.org/is/09-146r8/09-146r8.html)

## Profiles of this operation

None since 2026-11-19: the Implementation Profiles that pointed here point to [`generic-profiles.activity-type.raster-band-math`](../raster-band-math/).
