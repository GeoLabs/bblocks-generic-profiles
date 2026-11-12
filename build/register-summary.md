# Generic Process Profiles

A general-purpose, provider-independent vocabulary of process Concepts, Generic Profiles and
Implementation Profiles, the first three tiers of OGC 14-065 WPS 2.0.2 §7.5, independent of any
one project. The tiers differ in what they may carry: a Process Concept documents a general group
of processes, with no input or output; a Generic Profile gives one or more related operations an
abstract I/O signature (named roles, `dataType` concepts, multiplicity; no format, no size limit),
e.g. every binary boolean spatial predicate (Intersects, Contains, Within, Touches, Crosses,
Equals, Disjoint) takes two geometry inputs and returns one boolean, and is one Generic Profile,
not seven; an Implementation Profile refines one Generic Profile with the exchange formats it
supports, for any provider to implement. Real deployed or deployable processes, the fourth tier,
are not part of this register; they live wherever the implementation itself is profiled (e.g.
`ospd.process-profiles.*` for OSPD's CWL- and OGC-API-Processes-sourced profiles) and link back
here via their own `implementsProfile` property.


Produced by GeoLabs, first grounded in the spatial predicates and set operations of OGC Simple
Feature Access - Common Architecture (06-103r4) as a worked example: they share a small number of
I/O shapes, so the Generic Profile layer stays small. SQL/MM Spatial (ISO/IEC 13249-3) binds the
same operations to SQL (the `ST_Geometry` type, `ST_Intersects`-style function names) and is
profiled here, at the Implementation Profile tier; real deployed processes bind them further
still (e.g. to GML 3.1.0 Polygon) and are profiled in whichever register profiles the concrete
process (e.g. `ospd.process-profiles.*`), linked back here by `implementsProfile`.
Not limited to spatial operations -- any domain with standardised abstract operations and several
independent bindings is a candidate.


## Building Blocks

### `generic-profiles.register` — Generic Process Profiles register (ISO 19135:2026)

**Type:** model

This register described with the Registered Item Model (ISO 19135:2026): one rim:Register, three rim:RegisterItemClasses (Process Concept, Generic Profile, Implementation Profile) and the three owl:Classes, each a sub-class of rim:RegisterItem, that every entry of the corresponding tier is typed with. A profile of ogc.rim.schemas.register-item-class, following the same pattern as that register's own activity-type profile.

### `generic-profiles.activity-type` — Activity type

**Type:** schema

The shape every activity type of this register shares: the meaning of one operation, as an acttype:ActivityType item of the Activity Type Register's item class, held in gp:register. One per operation, distinct from the Implementation Profile that points to it with activityType.

### `generic-profiles.concept` — Process Concept

**Type:** schema

The shape every Process Concept shares: high-level documentation about a general group of processes, no input, no output, no format, no implementation (OGC 14-065 WPS 2.0.2 §7.5.1). Each real Concept (generic-profiles.concept.*) is its own building block that allOf-references this one -- this block is not itself a catalogue, only the common shape plus one illustrative example.

### `generic-profiles.activity-type.analytical-hillshading` — Activity type: Analytical hillshading

**Type:** schema

For each cell, the angle at which light coming from the position of the light source hits the terrain surface.

### `generic-profiles.activity-type.area` — Activity type: Area

**Type:** schema

The area of this Surface, as measured in the spatial reference system of this Surface.

### `generic-profiles.activity-type.band-retrieval` — Activity type: Band retrieval

**Type:** schema

Retrieves one band, one range component, of an Earth observation product as a raster, over the whole product or over an area of interest, with the values the product provides, possibly converted to physical units by the scale and offset the product declares.

### `generic-profiles.activity-type.buffer` — Activity type: Buffer

**Type:** schema

Returns a geometric object representing all points whose distance from this geometric object is less than or equal to a given distance.

### `generic-profiles.activity-type.centroid` — Activity type: Centroid

**Type:** schema

The mathematical centroid for this Surface as a Point. The result is not guaranteed to be on this Surface.

### `generic-profiles.activity-type.contains` — Activity type: Contains

**Type:** schema

Returns TRUE if this geometric object spatially contains anotherGeometry (no point of anotherGeometry lies outside this geometric object, and at least one point of the interior of anotherGeometry lies in the interior of this geometric object).

### `generic-profiles.activity-type.convex-hull` — Activity type: Convex hull

**Type:** schema

Returns a geometry that represents the convex hull of this Geometry.

### `generic-profiles.activity-type.crosses` — Activity type: Crosses

**Type:** schema

Returns TRUE if this geometric object 'spatially crosses' anotherGeometry: the intersection results in a geometry of dimension one less than the maximum dimension of the two source geometries, and the intersection set is interior to both.

### `generic-profiles.activity-type.difference` — Activity type: Difference

**Type:** schema

Returns a geometric object representing the point set difference of this geometric object with anotherGeometry.

### `generic-profiles.activity-type.disjoint` — Activity type: Disjoint

**Type:** schema

Returns TRUE if this geometric object is spatially disjoint from anotherGeometry (they share no point). Equivalent to the negation of Intersects.

### `generic-profiles.activity-type.equals` — Activity type: Equals

**Type:** schema

Returns TRUE if this geometric object is spatially equal to anotherGeometry (same point set), independent of vertex order or representation.

### `generic-profiles.activity-type.geometry-extent` — Activity type: Geometry extent

**Type:** schema

Computes the minimum bounding rectangle of a set of input geometries, as a geometry.

### `generic-profiles.activity-type.intersection` — Activity type: Intersection

**Type:** schema

Returns a geometric object representing the point set intersection of this geometric object with anotherGeometry.

### `generic-profiles.activity-type.intersects` — Activity type: Intersects

**Type:** schema

Returns TRUE if this geometric object spatially intersects anotherGeometry (i.e. they share at least one point). Equivalent to the negation of Disjoint.

### `generic-profiles.activity-type.is-simple` — Activity type: Is simple

**Type:** schema

Returns 1 (TRUE) if this Geometry has no anomalous geometric points, such as self intersection or self tangency.

### `generic-profiles.activity-type.otsu-thresholding` — Activity type: Otsu thresholding

**Type:** schema

Divides the cells of a single-band raster into two classes at the threshold computed from the histogram of the cell values by Otsu's method, which maximises the variance between the two classes, and returns the cells of the upper class as a binary mask.

### `generic-profiles.activity-type.point-cloud-thinning` — Activity type: Point cloud thinning (simple)

**Type:** schema

Reduces the number of points to the given percentage by sequential point removal, which suits points stored in chronological order best.

### `generic-profiles.activity-type.point-cloud-to-grid` — Activity type: Point cloud to grid

**Type:** schema

Writes one value per grid cell from the points falling in it -- by default the z value of the first point -- as a single-band raster.

### `generic-profiles.activity-type.point-cloud-to-shapes` — Activity type: Point cloud to shapes

**Type:** schema

Converts a point cloud to a feature collection of points.

### `generic-profiles.activity-type.product-selection` — Activity type: Product selection

**Type:** schema

Selects, from a catalogue of Earth observation products, those of a collection whose footprint intersects an area of interest and whose acquisition time falls within a time interval, possibly filtered further on their metadata, such as their cloud cover.

### `generic-profiles.activity-type.radiometric-index` — Activity type: Radiometric index

**Type:** schema

Computes one or more named radiometric indices (e.g. NDVI, NDWI, SAVI) from the relevant spectral channels of the input raster(s).

### `generic-profiles.activity-type.raster-band-math` — Activity type: Raster band math

**Type:** schema

Evaluates a user-supplied mathematical expression per pixel across one or more input rasters, producing a monoband output raster.

### `generic-profiles.activity-type.raster-band-math-multiband` — Activity type: Raster band math (multi-band output)

**Type:** schema

Evaluates a user-supplied, possibly vector-valued mathematical expression per pixel across one or more input rasters, producing an output raster with one or more bands.

### `generic-profiles.activity-type.raster-crop` — Activity type: Raster crop

**Type:** schema

Extracts the pixels of a raster coverage that fall within a region of interest.

### `generic-profiles.activity-type.raster-extent` — Activity type: Raster extent

**Type:** schema

Computes the bounding envelope of a raster coverage, as a vector polygon.

### `generic-profiles.activity-type.raster-format-conversion` — Activity type: Raster format conversion

**Type:** schema

Re-encodes a raster coverage into another raster format, without altering its content.

### `generic-profiles.activity-type.raster-rendering` — Activity type: Raster rendering

**Type:** schema

Depicts a raster as an image for viewing, giving each cell a colour from a colour map that associates values, or classes of values, with colours.

### `generic-profiles.activity-type.raster-reprojection` — Activity type: Raster reprojection

**Type:** schema

Reprojects a raster coverage to another coordinate reference system, resampling pixel values as needed, preserving the coverage's content.

### `generic-profiles.activity-type.raster-resampling` — Activity type: Raster resampling

**Type:** schema

Changes the cell size of a raster coverage, or its number of cells along each axis, over the same extent and in the same coordinate reference system, computing each new cell value from the input cells by an interpolation method.

### `generic-profiles.activity-type.slope` — Activity type: Slope

**Type:** schema

The slope gradient of an elevation model at each cell, from a local fit of the surface by the 9 parameter 2nd order polynom of Zevenbergen & Thorne (1987).

### `generic-profiles.activity-type.symdifference` — Activity type: Symmetric difference

**Type:** schema

Returns a geometric object representing the point set symmetric difference of this geometric object with anotherGeometry.

### `generic-profiles.activity-type.terrain-ruggedness-index` — Activity type: Terrain ruggedness index

**Type:** schema

The terrain ruggedness index (TRI) of Riley et al. (1999): how much the elevation of each cell differs from that of its neighbourhood.

### `generic-profiles.activity-type.topographic-position-index` — Activity type: Topographic position index

**Type:** schema

The topographic position index (TPI) of Guisan et al. (1999): the difference between the elevation of each cell and the mean elevation of its neighbourhood.

### `generic-profiles.activity-type.touches` — Activity type: Touches

**Type:** schema

Returns TRUE if the only points in common between this geometric object and anotherGeometry lie in the union of their boundaries: at least one boundary point in common, but no interior points in common.

### `generic-profiles.activity-type.union` — Activity type: Union

**Type:** schema

Returns a geometric object representing the point set union of this geometric object with anotherGeometry.

### `generic-profiles.activity-type.within` — Activity type: Within

**Type:** schema

Returns TRUE if this geometric object is spatially within anotherGeometry. The converse of Contains.

### `generic-profiles.concept.data-discovery-and-access` — Process Concept: Data Discovery and Access

**Type:** schema

Operations that find data products in catalogues and retrieve their data: selecting products by area, time and metadata, and retrieving bands or areas of a product, without computing new quantities from them -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 §7.5.1).

### `generic-profiles.concept.point-cloud-processing` — Process Concept: Point Cloud Processing

**Type:** schema

Operations on point clouds: converting them to other kinds of data (grids, feature collections) and reducing them (thinning) -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 §7.5.1).

### `generic-profiles.concept.raster-coverage-processing` — Process Concept: Raster Coverage Processing

**Type:** schema

Operations on raster/coverage data: reprojecting a coverage to another coordinate reference system, resampling it to another cell size, deriving a new raster from one or more others via a mathematical expression, a named radiometric index or a threshold, cropping a coverage to a region of interest, converting a coverage to another encoding, or depicting it as an image -- independent of any input/output signature or implementation (OGC 14-065 WPS 2.0.2 §7.5.1).

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

### `generic-profiles.generic-profile.band-retrieval` — Generic Profile: Band retrieval

**Type:** schema

Retrieves one band of an Earth observation product as a raster, over the whole product or over an area of interest. A product, a band identifier and an optional bounding box in, one Raster out.

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

### `generic-profiles.generic-profile.product-selection` — Generic Profile: Product selection

**Type:** schema

Selects, from a catalogue, the products of a collection whose footprint intersects an area of interest and whose acquisition time falls within a time interval. An area of interest, a time interval and a collection in, the selected products out.

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

### `generic-profiles.generic-profile.raster-rendering` — Generic Profile: Raster rendering

**Type:** schema

Depicts a raster as an image for viewing, by giving each cell a colour from a colour map. One Raster and a colour map in, one rendered image out.

### `generic-profiles.generic-profile.raster-reprojection` — Generic Profile: Raster reprojection

**Type:** schema

Reprojects a raster coverage to another coordinate reference system, preserving its content. One Raster input, a target CRS, one Raster output in the new CRS.

### `generic-profiles.generic-profile.raster-resampling` — Generic Profile: Raster resampling

**Type:** schema

Changes the cell size of a raster coverage over the same extent and in the same coordinate reference system. One Raster input, a target grid resolution, one Raster output on the new grid.

### `generic-profiles.generic-profile.raster-thresholding` — Generic Profile: Raster thresholding

**Type:** schema

Divides the cells of a single-band raster into two classes at a threshold that the operation determines from the raster's values, and returns the upper class as a binary mask. One single-band Raster input, one Binary mask output.

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

Implementation Profile of the operation Analytical hillshading, whose meaning is its activity type (activityType): the signature of the Generic Profile Analytical hillshading, bound to data exchange formats.

### `generic-profiles.implementation-profile.area` — Implementation Profile: Area

**Type:** schema

Implementation Profile of the operation Area, whose meaning is its activity type (activityType): the signature of the Generic Profile Geometry measure, bound to data exchange formats.

### `generic-profiles.implementation-profile.band-retrieval` — Implementation Profile: Band retrieval

**Type:** schema

Implementation Profile of the operation Band retrieval, whose meaning is its activity type (activityType): the signature of the Generic Profile Band retrieval, bound to data exchange formats.

### `generic-profiles.implementation-profile.buffer` — Implementation Profile: Buffer

**Type:** schema

Implementation Profile of the operation Buffer, whose meaning is its activity type (activityType): the signature of the Generic Profile Geometry buffer, bound to data exchange formats.

### `generic-profiles.implementation-profile.centroid` — Implementation Profile: Centroid

**Type:** schema

Implementation Profile of the operation Centroid, whose meaning is its activity type (activityType): the signature of the Generic Profile Unary geometry operation, bound to data exchange formats.

### `generic-profiles.implementation-profile.contains` — Implementation Profile: Contains

**Type:** schema

Implementation Profile of the operation Contains, whose meaning is its activity type (activityType): the signature of the Generic Profile Binary spatial predicate, bound to data exchange formats.

### `generic-profiles.implementation-profile.convex-hull` — Implementation Profile: Convex hull

**Type:** schema

Implementation Profile of the operation Convex hull, whose meaning is its activity type (activityType): the signature of the Generic Profile Unary geometry operation, bound to data exchange formats.

### `generic-profiles.implementation-profile.crosses` — Implementation Profile: Crosses

**Type:** schema

Implementation Profile of the operation Crosses, whose meaning is its activity type (activityType): the signature of the Generic Profile Binary spatial predicate, bound to data exchange formats.

### `generic-profiles.implementation-profile.difference` — Implementation Profile: Difference

**Type:** schema

Implementation Profile of the operation Difference, whose meaning is its activity type (activityType): the signature of the Generic Profile Binary spatial set operation, bound to data exchange formats.

### `generic-profiles.implementation-profile.disjoint` — Implementation Profile: Disjoint

**Type:** schema

Implementation Profile of the operation Disjoint, whose meaning is its activity type (activityType): the signature of the Generic Profile Binary spatial predicate, bound to data exchange formats.

### `generic-profiles.implementation-profile.equals` — Implementation Profile: Equals

**Type:** schema

Implementation Profile of the operation Equals, whose meaning is its activity type (activityType): the signature of the Generic Profile Binary spatial predicate, bound to data exchange formats.

### `generic-profiles.implementation-profile.geometry-extent` — Implementation Profile: Geometry extent

**Type:** schema

Implementation Profile of the operation Geometry extent, whose meaning is its activity type (activityType): the signature of the Generic Profile Unary geometry operation, bound to data exchange formats.

### `generic-profiles.implementation-profile.intersection` — Implementation Profile: Intersection

**Type:** schema

Implementation Profile of the operation Intersection, whose meaning is its activity type (activityType): the signature of the Generic Profile Binary spatial set operation, bound to data exchange formats.

### `generic-profiles.implementation-profile.intersects` — Implementation Profile: Intersects

**Type:** schema

Implementation Profile of the operation Intersects, whose meaning is its activity type (activityType): the signature of the Generic Profile Binary spatial predicate, bound to data exchange formats.

### `generic-profiles.implementation-profile.is-simple` — Implementation Profile: Is simple

**Type:** schema

Implementation Profile of the operation Is simple, whose meaning is its activity type (activityType): the signature of the Generic Profile Unary spatial predicate, bound to data exchange formats.

### `generic-profiles.implementation-profile.otsu-thresholding` — Implementation Profile: Otsu thresholding

**Type:** schema

Implementation Profile of the operation Otsu thresholding, whose meaning is its activity type (activityType): the signature of the Generic Profile Raster thresholding, bound to data exchange formats.

### `generic-profiles.implementation-profile.point-cloud-thinning` — Implementation Profile: Point cloud thinning (simple)

**Type:** schema

Implementation Profile of the operation Point cloud thinning (simple), whose meaning is its activity type (activityType): the signature of the Generic Profile Point cloud thinning, bound to data exchange formats.

### `generic-profiles.implementation-profile.point-cloud-to-grid` — Implementation Profile: Point cloud to grid

**Type:** schema

Implementation Profile of the operation Point cloud to grid, whose meaning is its activity type (activityType): the signature of the Generic Profile Point cloud rasterization, bound to data exchange formats.

### `generic-profiles.implementation-profile.point-cloud-to-shapes` — Implementation Profile: Point cloud to shapes

**Type:** schema

Implementation Profile of the operation Point cloud to shapes, whose meaning is its activity type (activityType): the signature of the Generic Profile Point cloud to features, bound to data exchange formats.

### `generic-profiles.implementation-profile.product-selection` — Implementation Profile: Product selection

**Type:** schema

Implementation Profile of the operation Product selection, whose meaning is its activity type (activityType): the signature of the Generic Profile Product selection, bound to data exchange formats.

### `generic-profiles.implementation-profile.radiometric-index` — Implementation Profile: Radiometric index

**Type:** schema

Implementation Profile of the operation Radiometric index, whose meaning is its activity type (activityType): the signature of the Generic Profile Radiometric index, bound to data exchange formats.

### `generic-profiles.implementation-profile.radiometric-index-single-band` — Implementation Profile: Radiometric index (single-band rasters)

**Type:** schema

Implementation Profile of the operation Radiometric index, whose meaning is its activity type (activityType): the signature of the Generic Profile Radiometric index, bound to data exchange formats.

### `generic-profiles.implementation-profile.raster-band-math` — Implementation Profile: Raster band math

**Type:** schema

Implementation Profile of the operation Raster band math, whose meaning is its activity type (activityType): the signature of the Generic Profile Raster band math, bound to data exchange formats.

### `generic-profiles.implementation-profile.raster-band-math-multiband` — Implementation Profile: Raster band math (multi-band output)

**Type:** schema

Implementation Profile of the operation Raster band math (multi-band output), whose meaning is its activity type (activityType): the signature of the Generic Profile Raster band math, bound to data exchange formats.

### `generic-profiles.implementation-profile.raster-crop` — Implementation Profile: Raster crop

**Type:** schema

Implementation Profile of the operation Raster crop, whose meaning is its activity type (activityType): the signature of the Generic Profile Raster crop, bound to data exchange formats.

### `generic-profiles.implementation-profile.raster-extent` — Implementation Profile: Raster extent

**Type:** schema

Implementation Profile of the operation Raster extent, whose meaning is its activity type (activityType): the signature of the Generic Profile Raster extent, bound to data exchange formats.

### `generic-profiles.implementation-profile.raster-format-conversion` — Implementation Profile: Raster format conversion

**Type:** schema

Implementation Profile of the operation Raster format conversion, whose meaning is its activity type (activityType): the signature of the Generic Profile Raster format conversion, bound to data exchange formats.

### `generic-profiles.implementation-profile.raster-rendering` — Implementation Profile: Raster rendering

**Type:** schema

Implementation Profile of the operation Raster rendering, whose meaning is its activity type (activityType): the signature of the Generic Profile Raster rendering, bound to data exchange formats.

### `generic-profiles.implementation-profile.raster-reprojection` — Implementation Profile: Raster reprojection

**Type:** schema

Implementation Profile of the operation Raster reprojection, whose meaning is its activity type (activityType): the signature of the Generic Profile Raster reprojection, bound to data exchange formats.

### `generic-profiles.implementation-profile.raster-resampling` — Implementation Profile: Raster resampling

**Type:** schema

Implementation Profile of the operation Raster resampling, whose meaning is its activity type (activityType): the signature of the Generic Profile Raster resampling, bound to data exchange formats.

### `generic-profiles.implementation-profile.slope` — Implementation Profile: Slope

**Type:** schema

Implementation Profile of the operation Slope, whose meaning is its activity type (activityType): the signature of the Generic Profile Terrain derivative, bound to data exchange formats.

### `generic-profiles.implementation-profile.symdifference` — Implementation Profile: Symmetric difference

**Type:** schema

Implementation Profile of the operation Symmetric difference, whose meaning is its activity type (activityType): the signature of the Generic Profile Binary spatial set operation, bound to data exchange formats.

### `generic-profiles.implementation-profile.terrain-ruggedness-index` — Implementation Profile: Terrain ruggedness index

**Type:** schema

Implementation Profile of the operation Terrain ruggedness index, whose meaning is its activity type (activityType): the signature of the Generic Profile Terrain derivative, bound to data exchange formats.

### `generic-profiles.implementation-profile.topographic-position-index` — Implementation Profile: Topographic position index

**Type:** schema

Implementation Profile of the operation Topographic position index, whose meaning is its activity type (activityType): the signature of the Generic Profile Terrain derivative, bound to data exchange formats.

### `generic-profiles.implementation-profile.touches` — Implementation Profile: Touches

**Type:** schema

Implementation Profile of the operation Touches, whose meaning is its activity type (activityType): the signature of the Generic Profile Binary spatial predicate, bound to data exchange formats.

### `generic-profiles.implementation-profile.union` — Implementation Profile: Union

**Type:** schema

Implementation Profile of the operation Union, whose meaning is its activity type (activityType): the signature of the Generic Profile Binary spatial set operation, bound to data exchange formats.

### `generic-profiles.implementation-profile.within` — Implementation Profile: Within

**Type:** schema

Implementation Profile of the operation Within, whose meaning is its activity type (activityType): the signature of the Generic Profile Binary spatial predicate, bound to data exchange formats.

