Process Concept: **Data Discovery and Access**.

> Operations that find data products in catalogues and retrieve their data: selecting products by area, time and metadata, and retrieving bands or areas of a product, without computing new quantities from them -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 §7.5.1).

## What it covers

Operations whose purpose is to find data or to deliver it, not to compute new quantities from it: selecting the products of a collection by area, time and metadata, and retrieving a band, or an area, of one product. The four other Process Concepts of this register are defined by the data they process (vector geometries, rasters, elevation models, point clouds); this one by what it does with any of them. Added on 2026-11-10 for the OSPD processes that search a catalogue or download a band (decision of 2026-11-10).

## Source

- [OGC 13-026r9 OpenSearch Extension for Earth Observation 1.1, §1 Scope and the parameters for the discovery of products (parentIdentifier, cloudCover)](https://docs.ogc.org/is/13-026r9/13-026r9.html)
- [OGC 12-040 Web Coverage Service Interface Standard - Range Subsetting Extension 1.0, §1 Scope](https://portal.ogc.org/files/12-040)
- [OGC 14-065 WPS 2.0.2 Interface Standard Corrigendum 2, §7.5.1 Process Concept](https://docs.ogc.org/is/14-065/14-065.html) -- what a Process Concept is.

Both OGC standards were read on 2026-11-10: OpenSearch EO for selecting the products of a collection (`parentIdentifier`) with filters such as `cloudCover`, the Range Subsetting Extension of WCS for retrieving selected range components (bands) of a coverage.

## Relations

- Broader concept of (`broader`): [`product-selection`](../../generic-profile/product-selection/), [`band-retrieval`](../../generic-profile/band-retrieval/)

## Register position

Top tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): **Concept** -> Generic Profile ->
Implementation Profile -> Implementation (instance level).
