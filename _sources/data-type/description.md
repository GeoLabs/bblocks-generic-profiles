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
