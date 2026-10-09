
# Process Concept: Terrain Analysis (Schema)

`generic-profiles.concept.terrain-analysis` *v0.1*

Operations deriving terrain attributes from an elevation model: local surface derivatives (slope, aspect, curvature), neighbourhood indices (terrain ruggedness, topographic position) and illumination (hillshading) -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 §7.5.1). A kind of raster coverage processing: an elevation model is a single-band raster whose values are elevations.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Process Concept: **Terrain Analysis**.

> Operations deriving terrain attributes from an elevation model: local surface derivatives (slope, aspect, curvature), neighbourhood indices (terrain ruggedness, topographic position) and illumination (hillshading) -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 §7.5.1). A kind of raster coverage processing: an elevation model is a single-band raster whose values are elevations.

## Source

- [SAGA 7.3.0 tool libraries, category Terrain Analysis](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/index.html)
- Wilson, J.P., Gallant, J.C. (2000): Terrain Analysis: Principles and Applications (cited by SAGA's Topographic Position Index tool)

## Relations

- Broader concept of (`broader`): [`terrain-derivative`](../../generic-profile/terrain-derivative/), [`analytical-hillshading`](../../generic-profile/analytical-hillshading/)
- Narrower than [`raster-coverage-processing`](../raster-coverage-processing/) (listed in its `narrower`)

## Register position

Top tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): **Concept** -> Generic Profile ->
Implementation Profile -> Implementation (instance level).

## Examples

### Terrain Analysis
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis",
  "type": "Concept",
  "prefLabel": "Terrain Analysis",
  "definition": "Operations deriving terrain attributes from an elevation model: local surface derivatives (slope, aspect, curvature), neighbourhood indices (terrain ruggedness, topographic position) and illumination (hillshading) -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 \u00a77.5.1). A kind of raster coverage processing: an elevation model is a single-band raster whose values are elevations.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/concept",
  "status": "submitted",
  "source": [
    {
      "title": "SAGA 7.3.0 tool libraries, category Terrain Analysis",
      "link": "https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/index.html"
    },
    {
      "title": "Wilson, J.P., Gallant, J.C. (2000): Terrain Analysis: Principles and Applications (cited by SAGA's Topographic Position Index tool)"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/concept/terrain-analysis/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis",
  "type": "Concept",
  "prefLabel": "Terrain Analysis",
  "definition": "Operations deriving terrain attributes from an elevation model: local surface derivatives (slope, aspect, curvature), neighbourhood indices (terrain ruggedness, topographic position) and illumination (hillshading) -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 \u00a77.5.1). A kind of raster coverage processing: an elevation model is a single-band raster whose values are elevations.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/concept",
  "status": "submitted",
  "source": [
    {
      "title": "SAGA 7.3.0 tool libraries, category Terrain Analysis",
      "link": "https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/index.html"
    },
    {
      "title": "Wilson, J.P., Gallant, J.C. (2000): Terrain Analysis: Principles and Applications (cited by SAGA's Topographic Position Index tool)"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix gp: <https://geolabs.github.io/bblocks-generic-profiles/def/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis> a skos:Concept ;
    dcterms:source [ dcterms:title "Wilson, J.P., Gallant, J.C. (2000): Terrain Analysis: Principles and Applications (cited by SAGA's Topographic Position Index tool)" ],
        [ dcterms:references <https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/index.html> ;
            dcterms:title "SAGA 7.3.0 tool libraries, category Terrain Analysis" ] ;
    skos:definition "Operations deriving terrain attributes from an elevation model: local surface derivatives (slope, aspect, curvature), neighbourhood indices (terrain ruggedness, topographic position) and illumination (hillshading) -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 §7.5.1). A kind of raster coverage processing: an elevation model is a single-band raster whose values are elevations." ;
    skos:inScheme gp:concept ;
    skos:prefLabel "Terrain Analysis" ;
    gp:status "submitted" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: The Concept "Terrain Analysis" -- see generic-profiles.concept for the
  general shape every Concept shares.
allOf:
- $ref: https://geolabs.github.io/bblocks-generic-profiles/build/annotated/concept/schema.yaml
- type: object
  properties:
    id:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/concept/terrain-analysis
      x-jsonld-id: '@id'
    type:
      const: Concept
      x-jsonld-id: '@type'
    prefLabel:
      const: Terrain Analysis
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
x-jsonld-extra-terms:
  Concept: http://www.w3.org/2004/02/skos/core#Concept
  definition: http://www.w3.org/2004/02/skos/core#definition
  inScheme:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#inScheme
    x-jsonld-type: '@id'
  status: https://geolabs.github.io/bblocks-generic-profiles/def/status
  narrower:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#narrower
    x-jsonld-type: '@id'
  source: http://purl.org/dc/terms/source
  title: http://purl.org/dc/terms/title
  link:
    x-jsonld-id: http://purl.org/dc/terms/references
    x-jsonld-type: '@id'
  clause: https://geolabs.github.io/bblocks-generic-profiles/def/clause
x-jsonld-prefixes:
  skos: http://www.w3.org/2004/02/skos/core#
  gp: https://geolabs.github.io/bblocks-generic-profiles/def/
  dct: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/concept/terrain-analysis/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/concept/terrain-analysis/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "Concept": "skos:Concept",
    "id": "@id",
    "type": "@type",
    "prefLabel": "skos:prefLabel",
    "definition": "skos:definition",
    "inScheme": {
      "@id": "skos:inScheme",
      "@type": "@id"
    },
    "status": "gp:status",
    "source": "dct:source",
    "narrower": {
      "@id": "skos:narrower",
      "@type": "@id"
    },
    "title": "dct:title",
    "link": {
      "@id": "dct:references",
      "@type": "@id"
    },
    "clause": "gp:clause",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "gp": "https://geolabs.github.io/bblocks-generic-profiles/def/",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/concept/terrain-analysis/context.jsonld)

## Sources

* [OGC 14-065 WPS 2.0.2 Interface Standard Corrigendum 2, §7.5.1 Process Concept](https://docs.ogc.org/is/14-065/14-065.html)
* [SAGA 7.3.0 tool libraries, category Terrain Analysis](https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/index.html)
* Wilson, J.P., Gallant, J.C. (2000): Terrain Analysis: Principles and Applications (cited by SAGA's Topographic Position Index tool)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/concept/terrain-analysis`

