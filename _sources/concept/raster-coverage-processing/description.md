Process Concept: **Raster Coverage Processing**.

> Operations on raster/coverage data: reprojecting a coverage to another coordinate reference
> system, deriving a new raster from one or more others via a mathematical expression or a named
> radiometric index, cropping a coverage to a region of interest, or converting a coverage to
> another encoding.

## What a Process Concept is

OGC 14-065 WPS 2.0.2 §7.5.1: *"a process concept is an object that provides high-level
documentation about a general group of processes. It describes the purpose, methodology and
properties of a process but not the specific input and output parameters. It is rather a
documentation resource that may be referenced by refined process definitions to document their
relation to a common principle."*

This Concept deliberately carries no input, no output, no format, no CWL and no implementation --
that is what the two tiers below it are for. It exists so that several Generic Profiles with
different I/O shapes can still declare their kinship:
[`raster-reprojection`](../../generic-profile/raster-reprojection/),
[`raster-band-math`](../../generic-profile/raster-band-math/),
[`radiometric-index`](../../generic-profile/radiometric-index/),
[`raster-crop`](../../generic-profile/raster-crop/),
[`raster-format-conversion`](../../generic-profile/raster-format-conversion/) and
[`raster-extent`](../../generic-profile/raster-extent/) each declare this
Concept as their `broader`.

## Source

Two standards, at different levels, the same way [`vector-geometry-processing`](../vector-geometry-processing/)
is grounded in Simple Feature Access and SQL/MM:

- ISO 19123-1:2023 *Geographic information -- Schema for coverage geometry and functions -- Part 1:
  Fundamentals* -- the abstract domain/range model of a coverage (a raster is one kind of coverage),
  with no processing language attached. This is the raster/coverage analogue of what OGC 06-103r4
  Simple Feature Access is for vector geometry.
- [OGC 08-068r2 Web Coverage Processing Service (WCPS) Language Interface Standard](https://www.ogc.org/standards/wcps/)
  -- an OGC standard that *does* bind coverage operations (subsetting, band math, reprojection) to
  a concrete query language. It is not cited as any one Implementation Profile's format binding
  below (GDAL and OTB, not WCPS, are what the Geonovum testbed actually runs), only as the
  standards-track evidence that these operations are recognised, harmonised processing concepts
  and not implementation-specific inventions.

## Register position

Top tier of the four-tier model this register implements (OGC 14-065 WPS 2.0.2 §7.5): Concept ->
Generic Profile -> Implementation Profile -> Implementation (instance level). The fourth tier is
not part of this register -- see `ospd.process-profiles.*` in `bblocks-process-profiles`.
