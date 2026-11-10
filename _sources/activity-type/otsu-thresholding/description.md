Activity type: **Otsu thresholding**.

> Divides the cells of a single-band raster into two classes at the threshold computed from the histogram of the cell values by Otsu's method, which maximises the variance between the two classes, and returns the cells of the upper class as a binary mask.

## The item

`https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/otsu-thresholding` is an `acttype:ActivityType` item of this register (`gp:register`), of the Activity Type Register's item class, and an OWL class, sub-class of `geoproc:GeoprocessingActivityType`.

Its activities use or generate spatial data, declared with GeoSPARQL 1.1 classes: `usedEntityType` `geo:Feature`; `generatedEntityType` `geo:Feature`. The class is chosen per kind of role (see `scripts/activity-types.yaml`); how a data type of `bblocks-data-types` maps to an entity type is still open (decision D8, question 5).

The run of an activity of this type is not typed here (decision D8, open).

## Notes

The method is the one of N. Otsu, A Threshold Selection Method from Gray-Level Histograms, IEEE Transactions on Systems, Man, and Cybernetics 9(1), 1979, 62-66, DOI 10.1109/TSMC.1979.4310076 (record checked on Crossref on 2026-11-10). Its text is not openly available and was not read, so it is not given as a source.

## Profiles of this operation

The Implementation Profile [`generic-profiles.implementation-profile.otsu-thresholding`](../../implementation-profile/otsu-thresholding/) points here with `activityType`. It holds the signature and the representations; this item holds the meaning.
