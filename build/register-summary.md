# Generic Process Profiles

A general-purpose, engine- and format-agnostic vocabulary of Generic Profiles, independent of
any one project. A Generic Profile gives one or more related operations an abstract I/O
signature (named roles and abstract types, no format, no size limit) -- e.g. every binary
boolean spatial predicate (Intersects, Contains, Within, Touches, Crosses, Equals, Disjoint)
takes two Geometry inputs and returns one Boolean, and is one Generic Profile, not seven.
Implementation Profiles (concrete, deployable processes binding a Generic Profile to real
formats) are not part of this register; they live wherever the implementation itself is
profiled (e.g. `ospd.process-profiles.*` for OSPD's CWL- and OGC-API-Processes-sourced profiles)
and link back here via their own `implementsGenericProfile` property.


Produced by GeoLabs, first grounded in the 12 spatial predicates and set operations of OGC
Simple Feature Access - Common Architecture (06-103r4) as a worked example: every one of them
shares one of a small number of I/O shapes, so the Generic Profile layer stays small (3 profiles
cover all 12 here). SQL/MM Spatial (ISO/IEC 13249-3) binds the same operations to SQL (the
`ST_Geometry` type, `ST_Intersects`-style function names) and real deployed processes bind them
further still (e.g. to GML 3.1.0 Polygon) -- both are concrete bindings, not part of this
register; they are profiled as Implementation Profiles in whichever register profiles the
concrete process (e.g. `ospd.process-profiles.*`), linked back here by `implementsGenericProfile`.
Not limited to spatial operations -- any domain with standardised abstract operations and several
independent bindings is a candidate.


## Building Blocks

### `generic-profiles.concept` — Process Concept

**Type:** schema

The shape every Process Concept shares: high-level documentation about a general group of processes, no input, no output, no format, no implementation (OGC 14-065 WPS 2.0.2 §7.5.1). Each real Concept (generic-profiles.concept.*) is its own building block that allOf-references this one -- this block is not itself a catalogue, only the common shape plus one illustrative example.

### `generic-profiles.data-type` — Data types

**Type:** schema

Reference vocabulary of the kinds of data process profile inputs and outputs carry (raster, single- or multi-band, elevation model, geometry by type, feature collection, point cloud, TIN, table, bounding box, literals).

### `generic-profiles.concept.point-cloud-processing` — Process Concept: Point Cloud Processing

**Type:** schema

Operations on point clouds: converting them to other kinds of data (grids, feature collections) and reducing them (thinning) -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 §7.5.1).

### `generic-profiles.concept.raster-coverage-processing` — Process Concept: Raster Coverage Processing

**Type:** schema

Operations on raster/coverage data: reprojecting a coverage to another coordinate reference system, deriving a new raster from one or more others via a mathematical expression or a named radiometric index, cropping a coverage to a region of interest, or converting a coverage to another encoding -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 §7.5.1).

### `generic-profiles.concept.terrain-analysis` — Process Concept: Terrain Analysis

**Type:** schema

Operations deriving terrain attributes from an elevation model: local surface derivatives (slope, aspect, curvature), neighbourhood indices (terrain ruggedness, topographic position) and illumination (hillshading) -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 §7.5.1). A kind of raster coverage processing: an elevation model is a single-band raster whose values are elevations.

### `generic-profiles.concept.vector-geometry-processing` — Process Concept: Vector Geometry Processing

**Type:** schema

General group covering operations on vector geometries: testing spatial relationships between two geometries, deriving a new geometry from one or two others, and measuring a geometry's own properties -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 §7.5.1).

### `generic-profiles.generic-profile` — Generic Process Profile

**Type:** schema

The shape every Generic Profile shares: the abstract interface of one process, declaring a signature for its inputs and outputs (OGC 14-065 WPS 2.0.2 §7.5.2), linked to its Process Concept by `broader`. Each real Generic Profile (generic-profiles.generic-profile.*) is its own building block that allOf-references this one -- this block is not itself a catalogue, only the common shape plus one illustrative example.

### `generic-profiles.generic-profile.analytical-hillshading` — Generic Profile: Analytical hillshading

**Type:** schema

Computes how the terrain is lit by a light source. One elevation model and the light source's azimuth and altitude in, one single-band raster out.

### `generic-profiles.generic-profile.binary-spatial-operation` — Generic Profile: Binary spatial set operation

**Type:** schema

Computes a new geometry from the point-set relationship of two input geometries. Shared I/O shape of the SQL/MM set-operation family: two Geometry inputs, one Geometry output.

### `generic-profiles.generic-profile.binary-spatial-predicate` — Generic Profile: Binary spatial predicate

**Type:** schema

Tests a boolean spatial relationship between two geometries. Shared I/O shape of every SQL/MM DE-9IM-family predicate: two Geometry inputs, one Boolean output, no side effect.

### `generic-profiles.generic-profile.geometry-buffer` — Generic Profile: Geometry buffer

**Type:** schema

Computes a new geometry from one input geometry and a scalar distance. A different shape from binary-spatial-operation: one Geometry, one Number, not two Geometries.

### `generic-profiles.generic-profile.geometry-measure` — Generic Profile: Geometry measure

**Type:** schema

Computes a scalar measurement of a single geometry. One Geometry input, one Number output.

### `generic-profiles.generic-profile.point-cloud-rasterization` — Generic Profile: Point cloud rasterization

**Type:** schema

Converts a point cloud to a raster on a grid of a given cell size. One point cloud and one cell size in, one raster out.

### `generic-profiles.generic-profile.point-cloud-thinning` — Generic Profile: Point cloud thinning

**Type:** schema

Reduces the number of points of a point cloud. One point cloud and the share of points to keep in, one point cloud out.

### `generic-profiles.generic-profile.point-cloud-to-features` — Generic Profile: Point cloud to features

**Type:** schema

Converts a point cloud to a feature collection. One point cloud in, one feature collection out.

### `generic-profiles.generic-profile.radiometric-index` — Generic Profile: Radiometric index

**Type:** schema

Computes one or more named radiometric indices (e.g. NDVI, NDWI, SAVI) from the relevant spectral bands of one or more input rasters. One or more Raster inputs, the name(s) of the index/indices to compute, one Raster output (one band per selected index).

### `generic-profiles.generic-profile.raster-band-math` — Generic Profile: Raster band math

**Type:** schema

Derives a new raster from one or more input rasters via a user-supplied mathematical expression evaluated per pixel. One or more Raster inputs, an expression, one Raster output -- the output's band structure (one band or several) is not part of this signature, see its Implementation Profiles.

### `generic-profiles.generic-profile.raster-crop` — Generic Profile: Raster crop

**Type:** schema

Crops a raster coverage to a region of interest. One Raster input, a bounding box, one Raster output covering only that area.

### `generic-profiles.generic-profile.raster-extent` — Generic Profile: Raster extent

**Type:** schema

Computes the bounding envelope of a raster coverage, returned as a geometry (a rectangular polygon in the coverage's CRS). One Raster input, one Geometry output.

### `generic-profiles.generic-profile.raster-format-conversion` — Generic Profile: Raster format conversion

**Type:** schema

Converts a raster coverage from one encoding to another, without changing its content. One Raster input, a target format, one Raster output in the new encoding.

### `generic-profiles.generic-profile.raster-reprojection` — Generic Profile: Raster reprojection

**Type:** schema

Reprojects a raster coverage to another coordinate reference system, preserving its content. One Raster input, a target CRS, one Raster output in the new CRS.

### `generic-profiles.generic-profile.terrain-derivative` — Generic Profile: Terrain derivative

**Type:** schema

Derives one terrain attribute, as a single-band raster, from an elevation model. One elevation model input, one single-band raster output. Covers operations that differ only in the attribute computed (slope, aspect, curvature, terrain ruggedness, topographic position), not in signature.

### `generic-profiles.generic-profile.unary-geometry-operation` — Generic Profile: Unary geometry operation

**Type:** schema

Derives a new geometry from a single input geometry. One Geometry input, one Geometry output. Covers operations that differ only in what they compute (bounding envelope, centroid, convex hull), not in signature -- the same principle `binary-spatial-predicate` and `binary-spatial-operation` already use for their own several operations.

### `generic-profiles.generic-profile.unary-spatial-predicate` — Generic Profile: Unary spatial predicate

**Type:** schema

Tests a boolean property of a single geometry. One Geometry input, one Boolean output -- the one-input counterpart to `binary-spatial-predicate`'s two.

### `generic-profiles.implementation-profile` — Process Implementation Profile

**Type:** schema

The shape every Implementation Profile shares: a specific named operation refining one Generic Profile, adding the standard data exchange formats it is commonly expressed in (OGC 14-065 WPS 2.0.2 §7.5.3). Each real Implementation Profile (generic-profiles.implementation-profile.*) is its own building block that allOf-references this one.

### `generic-profiles.implementation-profile.analytical-hillshading` — Implementation Profile: Analytical hillshading

**Type:** schema

For each cell, the angle at which light coming from the position of the light source hits the terrain surface (SAGA's standard method).

### `generic-profiles.implementation-profile.area` — Implementation Profile: Area

**Type:** schema

The area of this Surface, as measured in the spatial reference system of this Surface.

### `generic-profiles.implementation-profile.buffer` — Implementation Profile: Buffer

**Type:** schema

Returns a geometric object representing all points whose distance from this geometric object is less than or equal to a given distance.

### `generic-profiles.implementation-profile.centroid` — Implementation Profile: Centroid

**Type:** schema

The mathematical centroid for this Surface as a Point. The result is not guaranteed to be on this Surface.

### `generic-profiles.implementation-profile.contains` — Implementation Profile: Contains

**Type:** schema

Returns TRUE if this geometric object spatially contains anotherGeometry (no point of anotherGeometry lies outside this geometric object, and at least one point of the interior of anotherGeometry lies in the interior of this geometric object).

### `generic-profiles.implementation-profile.convex-hull` — Implementation Profile: Convex hull

**Type:** schema

Returns a geometry that represents the convex hull of this Geometry.

### `generic-profiles.implementation-profile.crosses` — Implementation Profile: Crosses

**Type:** schema

Returns TRUE if this geometric object 'spatially crosses' anotherGeometry: the intersection results in a geometry of dimension one less than the maximum dimension of the two source geometries, and the intersection set is interior to both.

### `generic-profiles.implementation-profile.difference` — Implementation Profile: Difference

**Type:** schema

Returns a geometric object representing the point set difference of this geometric object with anotherGeometry.

### `generic-profiles.implementation-profile.disjoint` — Implementation Profile: Disjoint

**Type:** schema

Returns TRUE if this geometric object is spatially disjoint from anotherGeometry (they share no point). Equivalent to the negation of Intersects.

### `generic-profiles.implementation-profile.equals` — Implementation Profile: Equals

**Type:** schema

Returns TRUE if this geometric object is spatially equal to anotherGeometry (same point set), independent of vertex order or representation.

### `generic-profiles.implementation-profile.geometry-extent` — Implementation Profile: Geometry extent

**Type:** schema

Computes the minimum bounding rectangle of a set of input geometries, as a geometry.

### `generic-profiles.implementation-profile.intersection` — Implementation Profile: Intersection

**Type:** schema

Returns a geometric object representing the point set intersection of this geometric object with anotherGeometry.

### `generic-profiles.implementation-profile.intersects` — Implementation Profile: Intersects

**Type:** schema

Returns TRUE if this geometric object spatially intersects anotherGeometry (i.e. they share at least one point). Equivalent to the negation of Disjoint.

### `generic-profiles.implementation-profile.is-simple` — Implementation Profile: Is simple

**Type:** schema

Returns 1 (TRUE) if this Geometry has no anomalous geometric points, such as self intersection or self tangency.

### `generic-profiles.implementation-profile.point-cloud-thinning` — Implementation Profile: Point cloud thinning (simple)

**Type:** schema

Reduces the number of points to the given percentage by sequential point removal, which suits points stored in chronological order best.

### `generic-profiles.implementation-profile.point-cloud-to-grid` — Implementation Profile: Point cloud to grid

**Type:** schema

Writes one value per grid cell from the points falling in it -- by default the z value of the first point -- as a single-band raster.

### `generic-profiles.implementation-profile.point-cloud-to-shapes` — Implementation Profile: Point cloud to shapes

**Type:** schema

Converts a point cloud to a SAGA shapes layer of points, i.e. a feature collection.

### `generic-profiles.implementation-profile.radiometric-index` — Implementation Profile: Radiometric index

**Type:** schema

Computes one or more named radiometric indices (e.g. NDVI, NDWI, SAVI) from the relevant spectral channels of the input raster(s).

### `generic-profiles.implementation-profile.raster-band-math` — Implementation Profile: Raster band math

**Type:** schema

Evaluates a user-supplied mathematical expression per pixel across one or more input rasters, producing a monoband output raster.

### `generic-profiles.implementation-profile.raster-band-math-multiband` — Implementation Profile: Raster band math (multi-band output)

**Type:** schema

Evaluates a user-supplied, possibly vector-valued mathematical expression per pixel across one or more input rasters, producing an output raster with one or more bands.

### `generic-profiles.implementation-profile.raster-crop` — Implementation Profile: Raster crop

**Type:** schema

Extracts the pixels of a raster coverage that fall within a region of interest. `areaOfInterest`'s `schema` $refs `ogc.api.processes.v1.schemas.bbox` directly (OGC API - Processes Part 1 Core's own bbox type), not a bespoke format string.

### `generic-profiles.implementation-profile.raster-extent` — Implementation Profile: Raster extent

**Type:** schema

Computes the bounding envelope of a raster coverage, as a vector polygon.

### `generic-profiles.implementation-profile.raster-format-conversion` — Implementation Profile: Raster format conversion

**Type:** schema

Re-encodes a raster coverage into another raster format, without altering its content.

### `generic-profiles.implementation-profile.raster-reprojection` — Implementation Profile: Raster reprojection

**Type:** schema

Reprojects a raster coverage to another coordinate reference system, resampling pixel values as needed, preserving the coverage's content.

### `generic-profiles.implementation-profile.slope` — Implementation Profile: Slope

**Type:** schema

The slope gradient of an elevation model at each cell, from a local fit of the surface (SAGA's default method: the 9 parameter 2nd order polynom of Zevenbergen & Thorne 1987).

### `generic-profiles.implementation-profile.symdifference` — Implementation Profile: Symmetric difference

**Type:** schema

Returns a geometric object representing the point set symmetric difference of this geometric object with anotherGeometry.

### `generic-profiles.implementation-profile.terrain-ruggedness-index` — Implementation Profile: Terrain ruggedness index

**Type:** schema

The terrain ruggedness index (TRI) of Riley et al. (1999): how much the elevation of each cell differs from that of its neighbourhood.

### `generic-profiles.implementation-profile.topographic-position-index` — Implementation Profile: Topographic position index

**Type:** schema

The topographic position index (TPI) of Guisan et al. (1999): the difference between the elevation of each cell and the mean elevation of its neighbourhood.

### `generic-profiles.implementation-profile.touches` — Implementation Profile: Touches

**Type:** schema

Returns TRUE if the only points in common between this geometric object and anotherGeometry lie in the union of their boundaries: at least one boundary point in common, but no interior points in common.

### `generic-profiles.implementation-profile.union` — Implementation Profile: Union

**Type:** schema

Returns a geometric object representing the point set union of this geometric object with anotherGeometry.

### `generic-profiles.implementation-profile.within` — Implementation Profile: Within

**Type:** schema

Returns TRUE if this geometric object is spatially within anotherGeometry. The converse of Contains.

