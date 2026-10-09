
# Data types (Schema)

`generic-profiles.data-type` *v0.1*

Reference vocabulary of the kinds of data process profile inputs and outputs carry (raster, single- or multi-band, elevation model, geometry by type, feature collection, point cloud, TIN, table, bounding box, literals).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Reference vocabulary of **data types**: what kind of data a process profile's input or output
carries, independent of how it is encoded (an Implementation Profile's `schema` declares that).

Every Generic Profile and Implementation Profile input/output points at one of these concepts with
`dataType`. An Implementation Profile may use the Generic Profile's type or a narrower one, following
`broader`: this is how a band-count restriction (`raster` to `raster-single-band`) or a geometry-type
restriction (`geometry` to `surface`) is stated, where Table 21 gives the Generic Profile no data
format at all.

| Type | Label | Broader |
|---|---|---|
| `raster` | Raster | -- |
| `raster-single-band` | Raster (single band) | `raster` |
| `raster-multi-band` | Raster (multiple bands) | `raster` |
| `elevation-model` | Elevation model | `raster-single-band` |
| `geometry` | Geometry | -- |
| `point` | Point | `geometry` |
| `curve` | Curve | `geometry` |
| `surface` | Surface | `geometry` |
| `feature-collection` | Feature collection | -- |
| `point-cloud` | Point cloud | -- |
| `tin` | Triangulated irregular network | -- |
| `table` | Table | -- |
| `bounding-box` | Bounding box | -- |
| `number` | Number | -- |
| `string` | String | -- |
| `boolean` | Boolean | -- |

Each concept cites where it comes from (OGC CIS for rasters and their range type, OGC Simple Feature
Access for geometries, OGC API - Features for feature collections, the OGC LAS Community Standard for
point clouds, SAGA's tool libraries where no standard was found).

## Examples

### Data types
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type",
  "type": "ConceptScheme",
  "prefLabel": "Data types",
  "definition": "The kinds of data a process profile's inputs and outputs carry, independent of any encoding (which an Implementation Profile's `schema` declares).",
  "concepts": [
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster",
      "type": "DataType",
      "prefLabel": "Raster",
      "definition": "A coverage on a regular grid of cells, each cell carrying one value per band; how many bands it has, and what they mean, is its range type.",
      "source": [
        {
          "title": "OGC 09-146r8 Coverage Implementation Schema (CIS) 1.1.1, \u00a76.5 RangeType",
          "link": "https://docs.ogc.org/is/09-146r8/09-146r8.html"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster-single-band",
      "type": "DataType",
      "prefLabel": "Raster (single band)",
      "definition": "A raster with exactly one band: a range type of one field.",
      "broader": [
        "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster"
      ],
      "source": [
        {
          "title": "OGC 09-146r8 Coverage Implementation Schema (CIS) 1.1.1, \u00a76.5 RangeType",
          "link": "https://docs.ogc.org/is/09-146r8/09-146r8.html"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster-multi-band",
      "type": "DataType",
      "prefLabel": "Raster (multiple bands)",
      "definition": "A raster with more than one band: a range type of several fields.",
      "broader": [
        "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster"
      ],
      "source": [
        {
          "title": "OGC 09-146r8 Coverage Implementation Schema (CIS) 1.1.1, \u00a76.5 RangeType",
          "link": "https://docs.ogc.org/is/09-146r8/09-146r8.html"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/elevation-model",
      "type": "DataType",
      "prefLabel": "Elevation model",
      "definition": "A single-band raster whose values are elevations of the terrain or of a surface (DEM, DTM, DSM).",
      "broader": [
        "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster-single-band"
      ],
      "source": [
        {
          "title": "OGC 09-146r8 Coverage Implementation Schema (CIS) 1.1.1, \u00a76.5 RangeType",
          "link": "https://docs.ogc.org/is/09-146r8/09-146r8.html"
        },
        {
          "title": "SAGA 7.3.0 Terrain Analysis tools, `Elevation` grid inputs",
          "link": "https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/ta_morphometry.html"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/geometry",
      "type": "DataType",
      "prefLabel": "Geometry",
      "definition": "A geometric object of the Simple Feature Access geometry model.",
      "source": [
        {
          "title": "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture",
          "link": "https://www.ogc.org/standards/sfa/"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/point",
      "type": "DataType",
      "prefLabel": "Point",
      "definition": "A 0-dimensional geometry, a single location.",
      "broader": [
        "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/geometry"
      ],
      "source": [
        {
          "title": "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture",
          "link": "https://www.ogc.org/standards/sfa/"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/curve",
      "type": "DataType",
      "prefLabel": "Curve",
      "definition": "A 1-dimensional geometry, e.g. a LineString.",
      "broader": [
        "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/geometry"
      ],
      "source": [
        {
          "title": "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture",
          "link": "https://www.ogc.org/standards/sfa/"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/surface",
      "type": "DataType",
      "prefLabel": "Surface",
      "definition": "A 2-dimensional geometry, e.g. a Polygon.",
      "broader": [
        "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/geometry"
      ],
      "source": [
        {
          "title": "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture",
          "link": "https://www.ogc.org/standards/sfa/"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/feature-collection",
      "type": "DataType",
      "prefLabel": "Feature collection",
      "definition": "A set of features, each with a geometry and attributes -- e.g. a SAGA shapes layer, a GeoJSON or OGC API - Features feature collection.",
      "source": [
        {
          "title": "OGC 17-069r4 OGC API - Features - Part 1: Core",
          "link": "https://docs.ogc.org/is/17-069r4/17-069r4.html"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/point-cloud",
      "type": "DataType",
      "prefLabel": "Point cloud",
      "definition": "A set of three-dimensional points, each with its own attributes (intensity, classification, ...), typically from LiDAR.",
      "source": [
        {
          "title": "OGC 17-030r1 LAS Specification 1.4 OGC Community Standard",
          "link": "https://www.ogc.org/standards/las/"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/tin",
      "type": "DataType",
      "prefLabel": "Triangulated irregular network",
      "definition": "A surface represented by a network of triangles over irregularly spaced points.",
      "source": [
        {
          "title": "ISO 19107:2019 Geographic information -- Spatial schema (TIN)"
        },
        {
          "title": "SAGA 7.3.0 TIN tools",
          "link": "https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/tin_tools.html"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/table",
      "type": "DataType",
      "prefLabel": "Table",
      "definition": "Records of attribute values, without geometry.",
      "source": [
        {
          "title": "SAGA 7.3.0 Table tools",
          "link": "https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/table_tools.html"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/bounding-box",
      "type": "DataType",
      "prefLabel": "Bounding box",
      "definition": "An axis-aligned extent given by its corners, with its CRS.",
      "source": [
        {
          "title": "ogc.api.processes.v1.schemas.bbox, after OGC 17-069r4 \u00a77.15.3 `bbox`",
          "link": "https://docs.ogc.org/is/17-069r4/17-069r4.html"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/number",
      "type": "DataType",
      "prefLabel": "Number",
      "definition": "A literal number.",
      "source": [
        {
          "title": "OGC 18-062r2 OGC API - Processes - Part 1: Core (inputs/outputs `schema`, JSON Schema)",
          "link": "https://docs.ogc.org/is/18-062r2/18-062r2.html"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/string",
      "type": "DataType",
      "prefLabel": "String",
      "definition": "A literal character string, e.g. an expression, a CRS identifier or a format name.",
      "source": [
        {
          "title": "OGC 18-062r2 OGC API - Processes - Part 1: Core (inputs/outputs `schema`, JSON Schema)",
          "link": "https://docs.ogc.org/is/18-062r2/18-062r2.html"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/boolean",
      "type": "DataType",
      "prefLabel": "Boolean",
      "definition": "A literal truth value.",
      "source": [
        {
          "title": "OGC 18-062r2 OGC API - Processes - Part 1: Core (inputs/outputs `schema`, JSON Schema)",
          "link": "https://docs.ogc.org/is/18-062r2/18-062r2.html"
        }
      ]
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/data-type/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type",
  "type": "ConceptScheme",
  "prefLabel": "Data types",
  "definition": "The kinds of data a process profile's inputs and outputs carry, independent of any encoding (which an Implementation Profile's `schema` declares).",
  "concepts": [
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster",
      "type": "DataType",
      "prefLabel": "Raster",
      "definition": "A coverage on a regular grid of cells, each cell carrying one value per band; how many bands it has, and what they mean, is its range type.",
      "source": [
        {
          "title": "OGC 09-146r8 Coverage Implementation Schema (CIS) 1.1.1, \u00a76.5 RangeType",
          "link": "https://docs.ogc.org/is/09-146r8/09-146r8.html"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster-single-band",
      "type": "DataType",
      "prefLabel": "Raster (single band)",
      "definition": "A raster with exactly one band: a range type of one field.",
      "broader": [
        "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster"
      ],
      "source": [
        {
          "title": "OGC 09-146r8 Coverage Implementation Schema (CIS) 1.1.1, \u00a76.5 RangeType",
          "link": "https://docs.ogc.org/is/09-146r8/09-146r8.html"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster-multi-band",
      "type": "DataType",
      "prefLabel": "Raster (multiple bands)",
      "definition": "A raster with more than one band: a range type of several fields.",
      "broader": [
        "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster"
      ],
      "source": [
        {
          "title": "OGC 09-146r8 Coverage Implementation Schema (CIS) 1.1.1, \u00a76.5 RangeType",
          "link": "https://docs.ogc.org/is/09-146r8/09-146r8.html"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/elevation-model",
      "type": "DataType",
      "prefLabel": "Elevation model",
      "definition": "A single-band raster whose values are elevations of the terrain or of a surface (DEM, DTM, DSM).",
      "broader": [
        "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster-single-band"
      ],
      "source": [
        {
          "title": "OGC 09-146r8 Coverage Implementation Schema (CIS) 1.1.1, \u00a76.5 RangeType",
          "link": "https://docs.ogc.org/is/09-146r8/09-146r8.html"
        },
        {
          "title": "SAGA 7.3.0 Terrain Analysis tools, `Elevation` grid inputs",
          "link": "https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/ta_morphometry.html"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/geometry",
      "type": "DataType",
      "prefLabel": "Geometry",
      "definition": "A geometric object of the Simple Feature Access geometry model.",
      "source": [
        {
          "title": "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture",
          "link": "https://www.ogc.org/standards/sfa/"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/point",
      "type": "DataType",
      "prefLabel": "Point",
      "definition": "A 0-dimensional geometry, a single location.",
      "broader": [
        "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/geometry"
      ],
      "source": [
        {
          "title": "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture",
          "link": "https://www.ogc.org/standards/sfa/"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/curve",
      "type": "DataType",
      "prefLabel": "Curve",
      "definition": "A 1-dimensional geometry, e.g. a LineString.",
      "broader": [
        "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/geometry"
      ],
      "source": [
        {
          "title": "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture",
          "link": "https://www.ogc.org/standards/sfa/"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/surface",
      "type": "DataType",
      "prefLabel": "Surface",
      "definition": "A 2-dimensional geometry, e.g. a Polygon.",
      "broader": [
        "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/geometry"
      ],
      "source": [
        {
          "title": "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture",
          "link": "https://www.ogc.org/standards/sfa/"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/feature-collection",
      "type": "DataType",
      "prefLabel": "Feature collection",
      "definition": "A set of features, each with a geometry and attributes -- e.g. a SAGA shapes layer, a GeoJSON or OGC API - Features feature collection.",
      "source": [
        {
          "title": "OGC 17-069r4 OGC API - Features - Part 1: Core",
          "link": "https://docs.ogc.org/is/17-069r4/17-069r4.html"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/point-cloud",
      "type": "DataType",
      "prefLabel": "Point cloud",
      "definition": "A set of three-dimensional points, each with its own attributes (intensity, classification, ...), typically from LiDAR.",
      "source": [
        {
          "title": "OGC 17-030r1 LAS Specification 1.4 OGC Community Standard",
          "link": "https://www.ogc.org/standards/las/"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/tin",
      "type": "DataType",
      "prefLabel": "Triangulated irregular network",
      "definition": "A surface represented by a network of triangles over irregularly spaced points.",
      "source": [
        {
          "title": "ISO 19107:2019 Geographic information -- Spatial schema (TIN)"
        },
        {
          "title": "SAGA 7.3.0 TIN tools",
          "link": "https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/tin_tools.html"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/table",
      "type": "DataType",
      "prefLabel": "Table",
      "definition": "Records of attribute values, without geometry.",
      "source": [
        {
          "title": "SAGA 7.3.0 Table tools",
          "link": "https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/table_tools.html"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/bounding-box",
      "type": "DataType",
      "prefLabel": "Bounding box",
      "definition": "An axis-aligned extent given by its corners, with its CRS.",
      "source": [
        {
          "title": "ogc.api.processes.v1.schemas.bbox, after OGC 17-069r4 \u00a77.15.3 `bbox`",
          "link": "https://docs.ogc.org/is/17-069r4/17-069r4.html"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/number",
      "type": "DataType",
      "prefLabel": "Number",
      "definition": "A literal number.",
      "source": [
        {
          "title": "OGC 18-062r2 OGC API - Processes - Part 1: Core (inputs/outputs `schema`, JSON Schema)",
          "link": "https://docs.ogc.org/is/18-062r2/18-062r2.html"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/string",
      "type": "DataType",
      "prefLabel": "String",
      "definition": "A literal character string, e.g. an expression, a CRS identifier or a format name.",
      "source": [
        {
          "title": "OGC 18-062r2 OGC API - Processes - Part 1: Core (inputs/outputs `schema`, JSON Schema)",
          "link": "https://docs.ogc.org/is/18-062r2/18-062r2.html"
        }
      ]
    },
    {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/data-type/boolean",
      "type": "DataType",
      "prefLabel": "Boolean",
      "definition": "A literal truth value.",
      "source": [
        {
          "title": "OGC 18-062r2 OGC API - Processes - Part 1: Core (inputs/outputs `schema`, JSON Schema)",
          "link": "https://docs.ogc.org/is/18-062r2/18-062r2.html"
        }
      ]
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix gp: <https://geolabs.github.io/bblocks-generic-profiles/def/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/data-type/boolean> a skos:Concept ;
    dcterms:source [ dcterms:references <https://docs.ogc.org/is/18-062r2/18-062r2.html> ;
            dcterms:title "OGC 18-062r2 OGC API - Processes - Part 1: Core (inputs/outputs `schema`, JSON Schema)" ] ;
    skos:definition "A literal truth value." ;
    skos:inScheme gp:data-type ;
    skos:prefLabel "Boolean" .

<https://geolabs.github.io/bblocks-generic-profiles/def/data-type/bounding-box> a skos:Concept ;
    dcterms:source [ dcterms:references <https://docs.ogc.org/is/17-069r4/17-069r4.html> ;
            dcterms:title "ogc.api.processes.v1.schemas.bbox, after OGC 17-069r4 §7.15.3 `bbox`" ] ;
    skos:definition "An axis-aligned extent given by its corners, with its CRS." ;
    skos:inScheme gp:data-type ;
    skos:prefLabel "Bounding box" .

<https://geolabs.github.io/bblocks-generic-profiles/def/data-type/curve> a skos:Concept ;
    dcterms:source [ dcterms:references <https://www.ogc.org/standards/sfa/> ;
            dcterms:title "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture" ] ;
    skos:broader <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/geometry> ;
    skos:definition "A 1-dimensional geometry, e.g. a LineString." ;
    skos:inScheme gp:data-type ;
    skos:prefLabel "Curve" .

<https://geolabs.github.io/bblocks-generic-profiles/def/data-type/elevation-model> a skos:Concept ;
    dcterms:source [ dcterms:references <https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/ta_morphometry.html> ;
            dcterms:title "SAGA 7.3.0 Terrain Analysis tools, `Elevation` grid inputs" ],
        [ dcterms:references <https://docs.ogc.org/is/09-146r8/09-146r8.html> ;
            dcterms:title "OGC 09-146r8 Coverage Implementation Schema (CIS) 1.1.1, §6.5 RangeType" ] ;
    skos:broader <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster-single-band> ;
    skos:definition "A single-band raster whose values are elevations of the terrain or of a surface (DEM, DTM, DSM)." ;
    skos:inScheme gp:data-type ;
    skos:prefLabel "Elevation model" .

<https://geolabs.github.io/bblocks-generic-profiles/def/data-type/feature-collection> a skos:Concept ;
    dcterms:source [ dcterms:references <https://docs.ogc.org/is/17-069r4/17-069r4.html> ;
            dcterms:title "OGC 17-069r4 OGC API - Features - Part 1: Core" ] ;
    skos:definition "A set of features, each with a geometry and attributes -- e.g. a SAGA shapes layer, a GeoJSON or OGC API - Features feature collection." ;
    skos:inScheme gp:data-type ;
    skos:prefLabel "Feature collection" .

<https://geolabs.github.io/bblocks-generic-profiles/def/data-type/number> a skos:Concept ;
    dcterms:source [ dcterms:references <https://docs.ogc.org/is/18-062r2/18-062r2.html> ;
            dcterms:title "OGC 18-062r2 OGC API - Processes - Part 1: Core (inputs/outputs `schema`, JSON Schema)" ] ;
    skos:definition "A literal number." ;
    skos:inScheme gp:data-type ;
    skos:prefLabel "Number" .

<https://geolabs.github.io/bblocks-generic-profiles/def/data-type/point> a skos:Concept ;
    dcterms:source [ dcterms:references <https://www.ogc.org/standards/sfa/> ;
            dcterms:title "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture" ] ;
    skos:broader <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/geometry> ;
    skos:definition "A 0-dimensional geometry, a single location." ;
    skos:inScheme gp:data-type ;
    skos:prefLabel "Point" .

<https://geolabs.github.io/bblocks-generic-profiles/def/data-type/point-cloud> a skos:Concept ;
    dcterms:source [ dcterms:references <https://www.ogc.org/standards/las/> ;
            dcterms:title "OGC 17-030r1 LAS Specification 1.4 OGC Community Standard" ] ;
    skos:definition "A set of three-dimensional points, each with its own attributes (intensity, classification, ...), typically from LiDAR." ;
    skos:inScheme gp:data-type ;
    skos:prefLabel "Point cloud" .

<https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster-multi-band> a skos:Concept ;
    dcterms:source [ dcterms:references <https://docs.ogc.org/is/09-146r8/09-146r8.html> ;
            dcterms:title "OGC 09-146r8 Coverage Implementation Schema (CIS) 1.1.1, §6.5 RangeType" ] ;
    skos:broader <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster> ;
    skos:definition "A raster with more than one band: a range type of several fields." ;
    skos:inScheme gp:data-type ;
    skos:prefLabel "Raster (multiple bands)" .

<https://geolabs.github.io/bblocks-generic-profiles/def/data-type/string> a skos:Concept ;
    dcterms:source [ dcterms:references <https://docs.ogc.org/is/18-062r2/18-062r2.html> ;
            dcterms:title "OGC 18-062r2 OGC API - Processes - Part 1: Core (inputs/outputs `schema`, JSON Schema)" ] ;
    skos:definition "A literal character string, e.g. an expression, a CRS identifier or a format name." ;
    skos:inScheme gp:data-type ;
    skos:prefLabel "String" .

<https://geolabs.github.io/bblocks-generic-profiles/def/data-type/surface> a skos:Concept ;
    dcterms:source [ dcterms:references <https://www.ogc.org/standards/sfa/> ;
            dcterms:title "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture" ] ;
    skos:broader <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/geometry> ;
    skos:definition "A 2-dimensional geometry, e.g. a Polygon." ;
    skos:inScheme gp:data-type ;
    skos:prefLabel "Surface" .

<https://geolabs.github.io/bblocks-generic-profiles/def/data-type/table> a skos:Concept ;
    dcterms:source [ dcterms:references <https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/table_tools.html> ;
            dcterms:title "SAGA 7.3.0 Table tools" ] ;
    skos:definition "Records of attribute values, without geometry." ;
    skos:inScheme gp:data-type ;
    skos:prefLabel "Table" .

<https://geolabs.github.io/bblocks-generic-profiles/def/data-type/tin> a skos:Concept ;
    dcterms:source [ dcterms:references <https://saga-gis.sourceforge.io/saga_tool_doc/7.3.0/tin_tools.html> ;
            dcterms:title "SAGA 7.3.0 TIN tools" ],
        [ dcterms:title "ISO 19107:2019 Geographic information -- Spatial schema (TIN)" ] ;
    skos:definition "A surface represented by a network of triangles over irregularly spaced points." ;
    skos:inScheme gp:data-type ;
    skos:prefLabel "Triangulated irregular network" .

<https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster-single-band> a skos:Concept ;
    dcterms:source [ dcterms:references <https://docs.ogc.org/is/09-146r8/09-146r8.html> ;
            dcterms:title "OGC 09-146r8 Coverage Implementation Schema (CIS) 1.1.1, §6.5 RangeType" ] ;
    skos:broader <https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster> ;
    skos:definition "A raster with exactly one band: a range type of one field." ;
    skos:inScheme gp:data-type ;
    skos:prefLabel "Raster (single band)" .

<https://geolabs.github.io/bblocks-generic-profiles/def/data-type/raster> a skos:Concept ;
    dcterms:source [ dcterms:references <https://docs.ogc.org/is/09-146r8/09-146r8.html> ;
            dcterms:title "OGC 09-146r8 Coverage Implementation Schema (CIS) 1.1.1, §6.5 RangeType" ] ;
    skos:definition "A coverage on a regular grid of cells, each cell carrying one value per band; how many bands it has, and what they mean, is its range type." ;
    skos:inScheme gp:data-type ;
    skos:prefLabel "Raster" .

<https://geolabs.github.io/bblocks-generic-profiles/def/data-type/geometry> a skos:Concept ;
    dcterms:source [ dcterms:references <https://www.ogc.org/standards/sfa/> ;
            dcterms:title "OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture" ] ;
    skos:definition "A geometric object of the Simple Feature Access geometry model." ;
    skos:inScheme gp:data-type ;
    skos:prefLabel "Geometry" .

gp:data-type a skos:ConceptScheme ;
    skos:definition "The kinds of data a process profile's inputs and outputs carry, independent of any encoding (which an Implementation Profile's `schema` declares)." ;
    skos:prefLabel "Data types" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: 'The data type vocabulary: a SKOS concept scheme whose concepts are what
  Generic and Implementation Profile inputs/outputs point at with `dataType`. A type''s
  `broader` type is what an Implementation Profile may narrow from (e.g. `raster`
  to `raster-single-band`).'
type: object
required:
- id
- type
- prefLabel
- concepts
properties:
  id:
    const: https://geolabs.github.io/bblocks-generic-profiles/def/data-type
    x-jsonld-id: '@id'
  type:
    const: ConceptScheme
    x-jsonld-id: '@type'
  prefLabel:
    type: string
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
  definition:
    type: string
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#definition
  concepts:
    type: array
    minItems: 1
    items:
      type: object
      required:
      - id
      - type
      - prefLabel
      - definition
      - source
      properties:
        id:
          type: string
          format: uri
          pattern: ^https://geolabs\.github\.io/bblocks\-generic\-profiles/def/data\-type/
          x-jsonld-id: '@id'
        type:
          const: DataType
          x-jsonld-id: '@type'
        prefLabel:
          type: string
          x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
        definition:
          type: string
          x-jsonld-id: http://www.w3.org/2004/02/skos/core#definition
        broader:
          type: array
          items:
            type: string
            format: uri
          x-jsonld-id: http://www.w3.org/2004/02/skos/core#broader
          x-jsonld-type: '@id'
        source:
          type: array
          minItems: 1
          items:
            type: object
            required:
            - title
            properties:
              title:
                type: string
                x-jsonld-id: http://purl.org/dc/terms/title
              link:
                type: string
                format: uri
                x-jsonld-id: http://purl.org/dc/terms/references
                x-jsonld-type: '@id'
          x-jsonld-id: http://purl.org/dc/terms/source
    x-jsonld-reverse: skos:inScheme
x-jsonld-extra-terms:
  ConceptScheme: http://www.w3.org/2004/02/skos/core#ConceptScheme
  DataType: http://www.w3.org/2004/02/skos/core#Concept
  clause: https://geolabs.github.io/bblocks-generic-profiles/def/clause
x-jsonld-prefixes:
  skos: http://www.w3.org/2004/02/skos/core#
  dct: http://purl.org/dc/terms/
  gp: https://geolabs.github.io/bblocks-generic-profiles/def/

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/data-type/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/data-type/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "ConceptScheme": "skos:ConceptScheme",
    "DataType": "skos:Concept",
    "clause": "gp:clause",
    "id": "@id",
    "type": "@type",
    "prefLabel": "skos:prefLabel",
    "definition": "skos:definition",
    "concepts": {
      "@context": {
        "broader": {
          "@id": "skos:broader",
          "@type": "@id"
        },
        "source": {
          "@context": {
            "title": "dct:title",
            "link": {
              "@id": "dct:references",
              "@type": "@id"
            }
          },
          "@id": "dct:source"
        }
      },
      "@reverse": "skos:inScheme"
    },
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dct": "http://purl.org/dc/terms/",
    "gp": "https://geolabs.github.io/bblocks-generic-profiles/def/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/data-type/context.jsonld)

## Sources

* [OGC 09-146r8 Coverage Implementation Schema (CIS) 1.1.1, §6.5 RangeType](https://docs.ogc.org/is/09-146r8/09-146r8.html)
* [OGC 06-103r4 Simple Feature Access - Part 1: Common Architecture](https://www.ogc.org/standards/sfa/)
* [OGC 17-030r1 LAS Specification 1.4 OGC Community Standard](https://www.ogc.org/standards/las/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/data-type`

