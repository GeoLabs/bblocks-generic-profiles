Process Concept -- the shape every Concept in this register shares.

## What a Process Concept is

OGC 14-065 WPS 2.0.2 §7.5.1: *"a process concept is an object that provides high-level
documentation about a general group of processes. It describes the purpose, methodology and
properties of a process but not the specific input and output parameters. It is rather a
documentation resource that may be referenced by refined process definitions to document their
relation to a common principle."*

This block is not itself a catalogue: it carries one placeholder example only, clearly marked as
illustrative, not a real vocabulary entry. The real Concepts in this register are each their own
building block, `allOf`-referencing this one and adding their own `const`-pinned `id`/`prefLabel`:

- [`vector-geometry-processing`](vector-geometry-processing/) -- operations on vector geometries.
- [`raster-coverage-processing`](raster-coverage-processing/) -- operations on raster/coverage data.

## Register position

Top tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): **Concept** -> Generic Profile ->
Implementation Profile -> Implementation (instance level).
