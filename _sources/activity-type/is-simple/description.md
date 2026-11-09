Activity type: **Is simple**.

> Returns 1 (TRUE) if this Geometry has no anomalous geometric points, such as self intersection or self tangency.

SQL/MM name: `ST_IsSimple`.

## The item

`https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/is-simple` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate geometries: `usedEntityType` `geo:Geometry`.

The run of an activity of this type is not typed here (decision D8, open).

## Sources

- [OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1, §2.1.1.1 IsSimple()](https://www.ogc.org/standards/sfs/)
- ISO/IEC 13249-3:2016 SQL multimedia and application packages -- Part 3: Spatial, ST_IsSimple

## Profiles of this operation

The Implementation Profile [`generic-profiles.implementation-profile.is-simple`](../../implementation-profile/is-simple/) points here with `activityType`. It holds the signature and the representations; this item holds the meaning.
