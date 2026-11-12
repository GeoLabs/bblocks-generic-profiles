
# Process Implementation Profile (Schema)

`generic-profiles.implementation-profile` *v0.1*

The shape every Implementation Profile shares: a specific named operation refining one Generic Profile, adding the standard data exchange formats it is commonly expressed in (OGC 14-065 WPS 2.0.2 §7.5.3). Each real Implementation Profile (generic-profiles.implementation-profile.*) is its own building block that allOf-references this one.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Process Implementation Profile -- the shape every Implementation Profile in this register shares.

## What an Implementation Profile is

OGC 14-065 WPS 2.0.2 §7.5.3: *"Implementation profiles cover all descriptive elements of a
process down to the supported data exchange formats. Technically they are process descriptions,
but with the scope of a process profile, i.e., a harmonized and well-defined computing process
that may be implemented by multiple service providers."*

This block is not itself a catalogue: it carries one placeholder example only, clearly marked as
illustrative. The real Implementation Profiles are each their own building block: one per named
operation, each `allOf`-referencing this one and adding its own `const`-pinned
`id`/`prefLabel`/`refinesGenericProfile` --

- 17 vector operations: 15 bound to SQL/MM (Intersects, Contains, Buffer, Centroid, Convex hull,
  Area, Is simple, ...), plus Geometry extent, bound to SAGA GIS (`SAGA.shapes_tools.19`, no
  SQL/MM `ST_Envelope` process exists on this testbed);
- 7 raster/coverage operations bound to GDAL/OTB (Raster reprojection, Raster band math, Raster
  band math (multi-band output), Radiometric index, Raster crop, Raster format conversion,
  Raster extent).
- 4 terrain operations and 3 point cloud operations, bound to GeoTIFF and LAS.
- 6 profiles added on 2026-11-10 for the OSPD processes that were not attached: Radiometric index
  (single-band rasters), Raster resampling, Otsu thresholding and Raster rendering (raster), Product
  selection and Band retrieval (data discovery and access), bound to GeoTIFF, GeoJSON, STAC Item and
  PNG. Radiometric index and Radiometric index (single-band rasters) share one activity type.

The meaning of each operation, and the standards that define it (Simple Feature Access, SQL/MM,
WCPS, the literature of terrain indices), are its activity type, `activityType`
(`generic-profiles.activity-type.*`, decisions D3 and D4). An Implementation Profile item carries no
tool, host or testbed keyword or source (D4); the texts above and in each profile's `description.md`
still name the tools its defaults were grounded in. The processes that implement a profile, and the
tools behind them, are profiled in
`bblocks-process-profiles`.

Three of the vector operations (Centroid, Convex hull, Geometry extent) share one Generic
Profile, `unary-geometry-operation` (Geometry -> Geometry); Is simple refines
`unary-spatial-predicate` (Geometry -> Boolean); Area refines `geometry-measure`
(Geometry -> Number). Centroid, Convex hull, Is simple and Area (2026-10-06) are grounded in
[OGC 99-049 OpenGIS Simple Features Specification For SQL, Revision 1.1](https://www.ogc.org/standards/sfs/),
the harmonized-with-SQL predecessor to 06-103r4 that the other SQL/MM-bound operations above
already use.

## What Table 21 asks this tier to carry, and how each row is enforced

[OGC 14-065r1 WPS 2.0 §7.5.4 Table 21](https://docs.ogc.org/is/14-065/14-065r1.html#figure_14)
("Inheritance and override rules for process profiles") is the precise contract, not just the
§7.5.3 prose above. D = Declare, I = Inherit (unchanged), O = Override, E = Extend, R = Restrict.
The "how" column is what each real Implementation Profile's own `schema.yaml` checks against its
Generic Profile (generated from it by `scripts/apply_table21_keywords_metadata.py`):

| Row | GP | **IP** | Instance | How, at this tier |
|---|---|---|---|---|
| Process Identifier, Title, Abstract | D | **O** | O | `id`/`prefLabel`/`definition`, `const`-pinned per operation |
| Process Keywords | D | **E** | E | `keywords` must `contain` every Generic Profile keyword |
| Process Metadata | D | **E/O** ᵃ | E/O ᵃ | `metadata` must keep the Generic Profile's Table 22 `concept` reference and add a `generic` one; `source` (citations) stays free |
| Input (the set itself) | | | E ᵇ | every Generic Profile input must be listed (`required`) |
| Input Identifier, Title, Abstract | D | **I** | I | the input's key; Title/Abstract not repeated (unchanged) |
| Input Keywords | D | **E** | E | `keywords` must `contain` the Generic Profile input's |
| Input Metadata | D | **E/O** ᵃ | E/O ᵃ | `metadata` must reference the corresponding Generic Profile input (`generic-input`, below) |
| Input Multiplicity | D | **R** ᶜ | E ᵈ | only where declared: `maxOccurs` ≤ the Generic Profile's; `minOccurs` between 0 and the Generic Profile's -- making an input optional is allowed, a register choice beyond footnote c; no declaration means the default, exactly one |
| Input Data format | -- | **D** | E ᵈ | `representation`: IRIs of representations of `bblocks-data-formats` (decision D6) |
| Output (the set itself) | | | E ᵇ | every Generic Profile output must be listed (`required`) |
| Output Identifier, Title, Abstract | D | **I** | I | as for inputs |
| Output Keywords | D | **E** | E | `keywords` must `contain` the Generic Profile output's |
| Output Metadata | D | **O** | O | `metadata` references the corresponding Generic Profile output (`generic-output`): a register choice, Table 21 leaves it free |
| Output Data format | -- | **D** | E ᵈ | `representation`, as for inputs |

ᵃ *"The list of metadata references to superior process profiles shall be extended.
Documentation metadata may be overridden."* The references are Table 5 Metadata structures
(`title`, `role`, `href` -- OGC API - Processes' own `ogc.api.processes.part1.v1.schemas.metadata`)
whose `role` is a Table 22 identifier: `http://www.opengis.net/spec/wps/2.0/def/process-profile/`
`concept`, `generic` or `implementation`. ᵇ additional optional inputs or supplementary outputs.
ᶜ maximum only, never the minimum. ᵈ more or larger inputs, additional formats.

Each input/output here has its own IRI, `<Implementation Profile id>/inputs/<name>`
(`/outputs/<name>`), so that an implementation can reference one input rather than the whole
profile. References are made at the level they are about:

- **on the process**, references to whole superior profiles, with the Table 22 roles (`concept`,
  `generic`, `implementation`) -- made once, never repeated on inputs/outputs;
- **on an input/output**, references to the corresponding input/output of each superior profile,
  with roles this register defines, since Table 22 only names profile *levels*:

| Role | Meaning |
|---|---|
| `https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input` | the `href` is the Generic Profile input this input refines |
| `https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output` | the same, for an output |
| `https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-input` | the `href` is one input of an Implementation Profile, which the referencing input implements |
| `https://geolabs.github.io/bblocks-generic-profiles/def/role/implementation-output` | the same, for an output |

They are this register's own identifiers, not OGC ones: nothing is minted under
`http://www.opengis.net/spec/wps/2.0/def/`, where OGC 14-065r1 defines only the three Table 22
roles and `process/description/documentation`.

Footnote a thus becomes a real chain at each level. For an input of `area`: nothing at Generic
Profile (a Process Concept has no inputs), `generic-input` here, and `generic-input` plus
`implementation-input` at the Implementation (instance level) -- see
`ospd.process-profiles.sqlmm.area`'s `processDescription.inherited.json`. On the process: `concept`
at Generic Profile, `concept` + `generic` here, all three at the instance level.

`representation` is Table 21's Data format (decision D6, 2026-11-05): one or more IRIs of
representations of the [`bblocks-data-formats`](https://github.com/GeoLabs/bblocks-data-formats)
register (`https://w3id.org/geolabs/ospd/data-formats/representation/...`). A representation
realizes a version of a data type of `bblocks-data-types` and points to one format, which carries
the specification, the media types observed and, where there is one, a JSON Schema fragment. Until
2026-11-09 this tier copied a JSON Schema into a `schema` property instead; that schema stays at the
Implementation (instance level), as the deployed process serves it. `gp:RepresentationReferenceShape`
rejects a `schema` on an input or output of tiers 2 and 3, a representation that is not a
`df:Representation`, and one that realizes neither the role's data type nor a broader one. Only
inputs/outputs that carry spatial, raster, point cloud or bbox data have a representation; a plain
parameter (an expression, a CRS, a distance) has none.

**The declared default is kept deliberately minimal** -- one format per data-carrying role (GML
for vector geometry, GeoTIFF for raster), not an exhaustive list of everything a deployment might
ever support. Table 21's own inheritance rule for this tier is `E` (Extend) at Implementation
(instance level): *"Implementations may allow more or larger input datasets than the
implementation profile, or support additional data exchange formats"* (footnote d) -- a
deployment is free to go beyond this tier's minimal default, so this tier should not try to
pre-empt every format a future deployment might add. Where this minimal default happens to be
grounded in a real deployment's own processDescription (the vector operations' GML, most of the
raster operations' GeoTIFF), that grounding is cited in each Implementation Profile's own
`description.md` -- where it is not (`Gdal_Warp`/`Gdal_Translate`'s DSN-typed inputs expose no
format structurally at all), that is also stated explicitly rather than implied.

`maxOccurs`, when present, Restricts (footnote c: *"Implementation profiles may restrict the
maximum cardinality of a superior generic profile... They shall not modify the minimum
cardinality"*) the Generic Profile's own `maxOccurs` for one input -- a real integer (or
`unbounded`), the same property OGC API - Processes' own `InputDescription` uses, not free text.
E.g. `OTB.RadiometricIndices`' own `in` input is a single image, restricting the Generic
Profile's `maxOccurs: unbounded` down to `1`; `OTB.BandMath`/`OTB.BandMathX`'s `il` input is a
list, left `maxOccurs: unbounded` here -- a cap a real implementation applies is recorded at the
instance level (`bblocks-process-profiles`), not at this tier. A cardinality is written only where there is one: an input without `minOccurs`/`maxOccurs`
has the OGC API - Processes default, exactly one, and no rule is generated for it.

## Register position

Third tier of the four-tier model (OGC 14-065 WPS 2.0.2 §7.5): Concept -> Generic Profile ->
**Implementation Profile** -> Implementation (instance level).

## Examples

### Example Implementation Profile (illustrative shape only, not a real operation)
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile",
  "type": "ImplementationProfile",
  "prefLabel": "Example Implementation Profile (placeholder, not a real operation)",
  "definition": "Illustrates the shape of an Implementation Profile entry only. Real ones are each their own building block -- see generic-profiles.implementation-profile.intersects, .buffer and the other siblings.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "hasAction": {
    "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/actions/addition",
    "type": "RegisterAction",
    "actionType": "addition",
    "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
    "startedAtTime": "2026-09-30T00:00:00Z",
    "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile"
  },
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile",
  "itemClass": "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/implementation-profile",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate",
  "activityType": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/intersects",
  "keywords": [
    "vector",
    "geometry",
    "spatial relation",
    "predicate",
    "example"
  ],
  "metadata": [
    {
      "title": "Process Concept: Vector Geometry Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"
    },
    {
      "title": "Generic Profile: Binary spatial predicate",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate"
    }
  ],
  "inputs": {
    "geometry1": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/inputs/geometry1",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/geometry",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/geometry-gml"
      ],
      "keywords": [
        "geometry"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Binary spatial predicate -- input `geometry1`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/inputs/geometry1"
        }
      ]
    },
    "geometry2": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/inputs/geometry2",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/geometry",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/geometry-gml"
      ],
      "keywords": [
        "geometry"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Binary spatial predicate -- input `geometry2`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/inputs/geometry2"
        }
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/outputs/result",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/boolean",
      "keywords": [
        "boolean"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Binary spatial predicate -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/outputs/result"
        }
      ]
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile",
  "type": "ImplementationProfile",
  "prefLabel": "Example Implementation Profile (placeholder, not a real operation)",
  "definition": "Illustrates the shape of an Implementation Profile entry only. Real ones are each their own building block -- see generic-profiles.implementation-profile.intersects, .buffer and the other siblings.",
  "inScheme": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile",
  "hasAction": {
    "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/actions/addition",
    "type": "RegisterAction",
    "actionType": "addition",
    "proposer": "https://geolabs.github.io/bblocks-generic-profiles/def/geolabs",
    "startedAtTime": "2026-09-30T00:00:00Z",
    "appliesTo": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile"
  },
  "objectIdentifier": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile",
  "itemClass": "https://geolabs.github.io/bblocks-generic-profiles/def/item-class/implementation-profile",
  "inRegister": "https://geolabs.github.io/bblocks-generic-profiles/def/register",
  "validityStatus": "invalid",
  "publicationStatus": "published",
  "refinesGenericProfile": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate",
  "activityType": "https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/intersects",
  "keywords": [
    "vector",
    "geometry",
    "spatial relation",
    "predicate",
    "example"
  ],
  "metadata": [
    {
      "title": "Process Concept: Vector Geometry Processing",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/concept",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/concept/vector-geometry-processing"
    },
    {
      "title": "Generic Profile: Binary spatial predicate",
      "role": "http://www.opengis.net/spec/wps/2.0/def/process-profile/generic",
      "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate"
    }
  ],
  "inputs": {
    "geometry1": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/inputs/geometry1",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/geometry",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/geometry-gml"
      ],
      "keywords": [
        "geometry"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Binary spatial predicate -- input `geometry1`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/inputs/geometry1"
        }
      ]
    },
    "geometry2": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/inputs/geometry2",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/geometry",
      "representation": [
        "https://w3id.org/geolabs/ospd/data-formats/representation/geometry-gml"
      ],
      "keywords": [
        "geometry"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Binary spatial predicate -- input `geometry2`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/inputs/geometry2"
        }
      ]
    }
  },
  "outputs": {
    "result": {
      "id": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/outputs/result",
      "dataType": "https://geolabs.github.io/bblocks-data-types/def/data-type/boolean",
      "keywords": [
        "boolean"
      ],
      "metadata": [
        {
          "title": "Generic Profile: Binary spatial predicate -- output `result`",
          "role": "https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output",
          "href": "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/outputs/result"
        }
      ]
    }
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix gp: <https://geolabs.github.io/bblocks-generic-profiles/def/> .
@prefix ns1: <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/> .
@prefix ns2: <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile> a gp:ImplementationProfile ;
    skos:definition "Illustrates the shape of an Implementation Profile entry only. Real ones are each their own building block -- see generic-profiles.implementation-profile.intersects, .buffer and the other siblings." ;
    skos:inScheme gp:implementation-profile ;
    skos:prefLabel "Example Implementation Profile (placeholder, not a real operation)" ;
    gp:activityType <https://geolabs.github.io/bblocks-generic-profiles/def/activity-type/intersects> ;
    gp:inputs [ ns1:geometry1 <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/inputs/geometry1> ;
            ns1:geometry2 <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/inputs/geometry2> ] ;
    gp:outputs [ ns2:result <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/outputs/result> ] ;
    gp:refinesGenericProfile <https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate> ;
    proc:keywords "example",
        "geometry",
        "predicate",
        "spatial relation",
        "vector" ;
    proc:metadata [ dcterms:title "Generic Profile: Binary spatial predicate" ],
        [ dcterms:title "Process Concept: Vector Geometry Processing" ] ;
    rim:hasAction <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/actions/addition> ;
    rim:inRegister gp:register ;
    rim:itemClass <https://geolabs.github.io/bblocks-generic-profiles/def/item-class/implementation-profile> ;
    rim:objectIdentifier "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:invalid .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/actions/addition> a rim:RegisterAction ;
    prov:startedAtTime "2026-09-30T00:00:00+00:00"^^xsd:dateTime ;
    rim:actionType rim:additionAction ;
    rim:appliesTo <https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile> ;
    rim:proposer gp:geolabs .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/inputs/geometry1> dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/geometry> ;
    gp:representation <https://w3id.org/geolabs/ospd/data-formats/representation/geometry-gml> ;
    proc:keywords "geometry" ;
    proc:metadata [ dcterms:title "Generic Profile: Binary spatial predicate -- input `geometry1`" ;
            ns1:href "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/inputs/geometry1" ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/inputs/geometry2> dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/geometry> ;
    gp:representation <https://w3id.org/geolabs/ospd/data-formats/representation/geometry-gml> ;
    proc:keywords "geometry" ;
    proc:metadata [ dcterms:title "Generic Profile: Binary spatial predicate -- input `geometry2`" ;
            ns1:href "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/inputs/geometry2" ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input> ] .

<https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/example-implementation-profile/outputs/result> dcterms:type <https://geolabs.github.io/bblocks-data-types/def/data-type/boolean> ;
    proc:keywords "boolean" ;
    proc:metadata [ dcterms:title "Generic Profile: Binary spatial predicate -- output `result`" ;
            ns2:href "https://geolabs.github.io/bblocks-generic-profiles/def/generic-profile/binary-spatial-predicate/outputs/result" ;
            proc:role <https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output> ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: "Process Implementation Profile (OGC 14-065 WPS 2.0.2 \xA77.5.3): \"Implementation
  profiles cover all descriptive elements of a process down to the supported data
  exchange formats.\" One per specific named operation (Intersects, Buffer, ...),
  `refinesGenericProfile` to exactly one Generic Profile (the shared abstract I/O
  shape).\n`inputs`/`outputs` name Table 21's Data format (D) by reference: `representation`,
  one or more IRIs of representations of the bblocks-data-formats register (decision
  D6, 2026-11-05). A representation realizes a version of a data type of bblocks-data-types
  and points to one format (GML, GeoTIFF, LAS, the OGC API - Processes bbox, ...).
  The JSON Schema that a real deployment serves stays at the Implementation (instance
  level), as its processDescription's `schema`; it is not copied here. `maxOccurs`,
  when present, Restricts (R, footnote c: \"Implementation profiles may restrict the
  maximum cardinality of a superior generic profile... They shall not modify the minimum
  cardinality\") the Generic Profile's own value -- a real integer (or `unbounded`),
  not free text. Only inputs/outputs that carry spatial, raster, point cloud or bbox
  data have a representation; a plain parameter (an expression, a CRS, a distance)
  has none to declare.\nKeep the declared representations minimal and deliberately
  not exhaustive (one is often enough). Per Table 21, Implementation (instance level)
  may *Extend* this (footnote d: \"Implementations may... support additional data
  exchange formats\").\nThe meaning of the operation is not here: it is the activity
  type that `activityType` points to (generic-profiles.activity-type.*, decisions
  D3 and D4). No tool, host or testbed is named at this tier.\nThe rest of Table 21
  at this tier, as each real Implementation Profile's own `schema.yaml` enforces it
  against its Generic Profile: - Process: `keywords` Extend (E) -- must contain every
  Generic Profile keyword;\n  `id`/`prefLabel`/`definition` Override (O); `metadata`
  Extends (E, footnote a: \"the list of\n  metadata references to superior process
  profiles shall be extended\") the Generic Profile's\n  list -- its Table 22 `concept`
  reference -- with a `generic` one to the Generic Profile\n  itself. Profile-level
  references are made here only, never repeated on inputs/outputs.\n- Input: every
  Generic Profile input is listed. Its `metadata` references the corresponding\n  Generic
  Profile input (`<Generic Profile id>/inputs/<name>`) with this register's role\n
  \ `https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input` --
  footnote a, at the level of the input; `keywords` Extend (E);\n  Identifier/Title/Abstract
  Inherit (I), so not repeated; `maxOccurs` Restrict (R); `minOccurs`\n  may be restricted
  down to 0 (a register choice beyond Table 21, footnote c forbidding it);\n  `representation`
  Declare (D).\n- Output: every Generic Profile output is listed too; `metadata` references
  the corresponding\n  Generic Profile output with the role `https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output`
  (Table 21 allows any value here,\n  O; the register keeps outputs symmetric with
  inputs); `keywords` Extend (E); `representation`\n  Declare (D)."
allOf:
- $ref: https://ogcincubator.github.io/registered-item-model/build/annotated/rim/schemas/register-item/schema.yaml
- type: object
  required:
  - id
  - type
  - prefLabel
  - definition
  - inScheme
  - refinesGenericProfile
  - activityType
  - keywords
  - metadata
  - inputs
  - outputs
  - itemClass
  - inRegister
  - hasAction
  properties:
    id:
      type: string
      format: uri
      x-jsonld-id: '@id'
    type:
      const: ImplementationProfile
      x-jsonld-id: '@type'
    prefLabel:
      type: string
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
    definition:
      type: string
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#definition
    inScheme:
      type: string
      format: uri
      x-jsonld-id: http://www.w3.org/2004/02/skos/core#inScheme
      x-jsonld-type: '@id'
    itemClass:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/item-class/implementation-profile
    inRegister:
      const: https://geolabs.github.io/bblocks-generic-profiles/def/register
    refinesGenericProfile:
      description: The single Generic Profile (generic-profiles.generic-profile.*)
        this Implementation Profile refines.
      type: string
      format: uri
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/refinesGenericProfile
      x-jsonld-type: '@id'
    activityType:
      description: The activity type (generic-profiles.activity-type.*) that holds
        the meaning of the operation this Implementation Profile binds to formats
        (decisions D3 and D4). gp:activityType, a sub-property of rim:relatedItem.
      type: string
      format: uri
      pattern: ^https://geolabs\.github\.io/bblocks-generic-profiles/def/activity-type/[a-z0-9-]+$
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/activityType
      x-jsonld-type: '@id'
    keywords:
      description: Table 21 Process.Keywords (E) -- the Generic Profile's keywords
        plus this operation's own.
      type: array
      minItems: 1
      items:
        type: string
      x-jsonld-id: https://w3id.org/ogc/api/processes/keywords
    metadata:
      description: 'Table 21 Process.Metadata (E, footnote a): the Generic Profile''s
        references (Table 22 `concept`) plus a Table 22 `generic` reference to the
        Generic Profile.'
      type: array
      items:
        $ref: https://geolabs.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/part1/v1/schemas/metadata/schema.yaml
      allOf:
      - contains:
          type: object
          required:
          - role
          - href
          properties:
            role:
              const: http://www.opengis.net/spec/wps/2.0/def/process-profile/concept
      - contains:
          type: object
          required:
          - role
          - href
          properties:
            role:
              const: http://www.opengis.net/spec/wps/2.0/def/process-profile/generic
      x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
    inputs:
      description: Keyed by the same input names as the Generic Profile's own `inputs`
        (Identifier/Title/ Abstract Inherited, not repeated). `representation` is
        Table 21's Data format (D); `maxOccurs`, when present, Restricts (R, footnote
        c) the Generic Profile's own value; `keywords` Extend (E) the Generic Profile's;
        `metadata` Extends (E, footnote a) its superior-profile references.
      type: object
      additionalProperties:
        type: object
        required:
        - id
        - dataType
        - keywords
        - metadata
        not:
          required:
          - schema
        properties:
          dataType:
            description: 'What kind of data this input is, as a concept of the bblocks-data-types
              register (`https://geolabs.github.io/bblocks-data-types/def/data-type/...`).
              The Generic Profile''s, or a narrower one (`skos:broader` chain): e.g.
              a band-count or a geometry-type restriction.'
            type: string
            format: uri
            x-jsonld-id: http://purl.org/dc/terms/type
            x-jsonld-type: '@id'
          id:
            description: This input's own IRI, `<profile id>/inputs/<name>` -- what
              a lower tier's metadata `href` points at.
            type: string
            format: uri
            x-jsonld-id: '@id'
          representation:
            description: 'Table 21 Data format (D), by reference (decision D6): one
              or more representations of the bblocks-data-formats register (`https://w3id.org/geolabs/ospd/data-formats/representation/...`),
              each realizing a version of this role''s dataType, or of a broader one,
              and pointing to one format. No copied schema: the schema stays at the
              Implementation (instance level), as served.'
            type: array
            minItems: 1
            items:
              type: string
              format: uri
              pattern: ^https://w3id\.org/geolabs/ospd/data-formats/representation/[a-z0-9-]+$
            x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/representation
            x-jsonld-type: '@id'
          minOccurs:
            description: 'Restricts the Generic Profile''s minimum, down to 0 (the
              input becomes optional), never above it. A deliberate departure from
              Table 21 footnote c ("shall not modify the minimum cardinality"): a
              Generic Profile keeps `minOccurs: 1` and lower tiers, down to a real
              implementation, may make the input optional (e.g. a target CRS whose
              absence means no reprojection).'
            type: integer
            minimum: 0
          maxOccurs:
            oneOf:
            - type: integer
            - const: unbounded
            x-jsonld-id: https://w3id.org/ogc/api/processes/maxOccurs
          keywords:
            type: array
            minItems: 1
            items:
              type: string
            x-jsonld-id: https://w3id.org/ogc/api/processes/keywords
          metadata:
            type: array
            items:
              $ref: https://geolabs.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/part1/v1/schemas/metadata/schema.yaml
            contains:
              type: object
              required:
              - role
              - href
              properties:
                role:
                  const: https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-input
                  x-jsonld-id: https://w3id.org/ogc/api/processes/role
                  x-jsonld-type: '@id'
            x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/
    outputs:
      description: Keyed by the same output names as the Generic Profile's own `outputs`.
      type: object
      additionalProperties:
        type: object
        required:
        - id
        - dataType
        - keywords
        - metadata
        not:
          required:
          - schema
        properties:
          dataType:
            description: 'What kind of data this output is, as a concept of the bblocks-data-types
              register (`https://geolabs.github.io/bblocks-data-types/def/data-type/...`).
              The Generic Profile''s, or a narrower one (`skos:broader` chain): e.g.
              a band-count or a geometry-type restriction.'
            type: string
            format: uri
            x-jsonld-id: http://purl.org/dc/terms/type
            x-jsonld-type: '@id'
          id:
            description: This output's own IRI, `<profile id>/outputs/<name>` -- what
              a lower tier's metadata `href` points at.
            type: string
            format: uri
            x-jsonld-id: '@id'
          representation:
            description: 'Table 21 Data format (D), by reference (decision D6): one
              or more representations of the bblocks-data-formats register (`https://w3id.org/geolabs/ospd/data-formats/representation/...`),
              each realizing a version of this role''s dataType, or of a broader one,
              and pointing to one format. No copied schema: the schema stays at the
              Implementation (instance level), as served.'
            type: array
            minItems: 1
            items:
              type: string
              format: uri
              pattern: ^https://w3id\.org/geolabs/ospd/data-formats/representation/[a-z0-9-]+$
            x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/representation
            x-jsonld-type: '@id'
          keywords:
            type: array
            minItems: 1
            items:
              type: string
            x-jsonld-id: https://w3id.org/ogc/api/processes/keywords
          metadata:
            type: array
            items:
              $ref: https://geolabs.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/part1/v1/schemas/metadata/schema.yaml
            contains:
              type: object
              required:
              - role
              - href
              properties:
                role:
                  const: https://geolabs.github.io/bblocks-generic-profiles/def/role/generic-output
                  x-jsonld-id: https://w3id.org/ogc/api/processes/role
                  x-jsonld-type: '@id'
            x-jsonld-id: https://w3id.org/ogc/api/processes/metadata
      x-jsonld-id: https://geolabs.github.io/bblocks-generic-profiles/def/outputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/
    source:
      type: array
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
x-jsonld-extra-terms:
  ImplementationProfile: https://geolabs.github.io/bblocks-generic-profiles/def/ImplementationProfile
x-jsonld-prefixes:
  gp: https://geolabs.github.io/bblocks-generic-profiles/def/
  skos: http://www.w3.org/2004/02/skos/core#
  proc: https://w3id.org/ogc/api/processes/
  dct: http://purl.org/dc/terms/
x-bblocks-metadata:
  itemIdentifier: generic-profiles.implementation-profile
  register: https://geolabs.github.io/bblocks-generic-profiles/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-12'

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "Register": "rim:Register",
    "RegisterSystem": "rim:RegisterSystem",
    "RegisterSpecification": "rim:RegisterSpecification",
    "RegisterItemClass": "rim:RegisterItemClass",
    "RegisterItem": "rim:RegisterItem",
    "RegisterAction": "rim:RegisterAction",
    "Concept": "rim:Concept",
    "ConceptVersion": "rim:ConceptVersion",
    "ConceptSystem": "rim:ConceptSystem",
    "Commitment": "rim:Commitment",
    "Agent": "prov:Agent",
    "Organization": "prov:Organization",
    "Person": "prov:Person",
    "label": "rdfs:label",
    "prefLabel": "skos:prefLabel",
    "definition": "skos:definition",
    "inScheme": {
      "@id": "skos:inScheme",
      "@type": "@id"
    },
    "runsOn": {
      "@id": "rim:runsOn",
      "@type": "@id"
    },
    "hasSpecification": {
      "@id": "rim:hasSpecification",
      "@type": "@id"
    },
    "definesSubstantiveChange": "rim:definesSubstantiveChange",
    "registerOwner": {
      "@id": "rim:registerOwner",
      "@type": "@id"
    },
    "registerManager": {
      "@id": "rim:registerManager",
      "@type": "@id"
    },
    "controlBody": {
      "@id": "rim:controlBody",
      "@type": "@id"
    },
    "registerSystemManager": {
      "@id": "rim:registerSystemManager",
      "@type": "@id"
    },
    "registerUser": {
      "@id": "rim:registerUser",
      "@type": "@id"
    },
    "hasCommitment": {
      "@id": "rim:hasCommitment",
      "@type": "@id"
    },
    "commitmentCategory": {
      "@id": "rim:commitmentCategory",
      "@type": "@vocab"
    },
    "access": "rim:accessCommitment",
    "persistence": "rim:persistenceCommitment",
    "transparency": "rim:transparencyCommitment",
    "definedIn": {
      "@id": "rim:definedIn",
      "@type": "@id"
    },
    "validatedBy": {
      "@id": "rim:validatedBy",
      "@type": "@id"
    },
    "versionOf": {
      "@id": "rim:versionOf",
      "@type": "@id"
    },
    "version": "rim:version",
    "valid": "rim:valid",
    "invalid": "rim:invalid",
    "published": "rim:published",
    "unpublished": "rim:unpublished",
    "appliesTo": {
      "@id": "rim:appliesTo",
      "@type": "@id"
    },
    "proposer": {
      "@id": "rim:proposer",
      "@type": "@id"
    },
    "actionType": {
      "@id": "rim:actionType",
      "@type": "@vocab"
    },
    "addition": "rim:additionAction",
    "publish": "rim:publishAction",
    "unpublish": "rim:unpublishAction",
    "invalidation": "rim:invalidationAction",
    "supersession": "rim:supersessionAction",
    "redaction": "rim:redactionAction",
    "deletion": "rim:deletionAction",
    "changeClassification": {
      "@id": "rim:changeClassification",
      "@type": "@vocab"
    },
    "substantive": "rim:substantiveChange",
    "clarifying": "rim:clarifyingChange",
    "correctional": "rim:correctionalChange",
    "startedAtTime": {
      "@id": "prov:startedAtTime",
      "@type": "xsd:dateTime"
    },
    "endedAtTime": {
      "@id": "prov:endedAtTime",
      "@type": "xsd:dateTime"
    },
    "wasAssociatedWith": {
      "@id": "prov:wasAssociatedWith",
      "@type": "@id"
    },
    "id": "@id",
    "type": "@type",
    "objectIdentifier": {
      "@id": "rim:objectIdentifier",
      "@type": "xsd:anyURI"
    },
    "functionalIdentifier": {
      "@id": "rim:functionalIdentifier",
      "@type": "xsd:anyURI"
    },
    "itemClass": {
      "@id": "rim:itemClass",
      "@type": "@id"
    },
    "inRegister": {
      "@id": "rim:inRegister",
      "@type": "@id"
    },
    "realizes": {
      "@id": "rim:realizes",
      "@type": "@id"
    },
    "validityStatus": {
      "@id": "rim:validityStatus",
      "@type": "@vocab"
    },
    "publicationStatus": {
      "@id": "rim:publicationStatus",
      "@type": "@vocab"
    },
    "isRedacted": {
      "@id": "rim:isRedacted",
      "@type": "xsd:boolean"
    },
    "isDeleted": {
      "@id": "rim:isDeleted",
      "@type": "xsd:boolean"
    },
    "title": "dct:title",
    "description": "dct:description",
    "relatedItem": {
      "@id": "rim:relatedItem",
      "@type": "@id"
    },
    "supersededBy": {
      "@id": "rim:supersededBy",
      "@type": "@id"
    },
    "supersedes": {
      "@id": "rim:supersedes",
      "@type": "@id"
    },
    "hasAction": {
      "@id": "rim:hasAction",
      "@type": "@id"
    },
    "refinesGenericProfile": {
      "@id": "gp:refinesGenericProfile",
      "@type": "@id"
    },
    "activityType": {
      "@id": "gp:activityType",
      "@type": "@id"
    },
    "keywords": "proc:keywords",
    "metadata": "proc:metadata",
    "inputs": {
      "@context": {
        "@vocab": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/inputs/",
        "dataType": {
          "@id": "dct:type",
          "@type": "@id"
        },
        "representation": {
          "@id": "gp:representation",
          "@type": "@id"
        },
        "maxOccurs": "proc:maxOccurs",
        "metadata": {
          "@context": {
            "role": {
              "@id": "proc:role",
              "@type": "@id"
            }
          },
          "@id": "proc:metadata"
        }
      },
      "@id": "gp:inputs"
    },
    "outputs": {
      "@context": {
        "@vocab": "https://geolabs.github.io/bblocks-generic-profiles/def/implementation-profile/outputs/",
        "dataType": {
          "@id": "dct:type",
          "@type": "@id"
        },
        "representation": {
          "@id": "gp:representation",
          "@type": "@id"
        },
        "metadata": {
          "@context": {
            "role": {
              "@id": "proc:role",
              "@type": "@id"
            }
          },
          "@id": "proc:metadata"
        }
      },
      "@id": "gp:outputs"
    },
    "source": {
      "@context": {
        "link": {
          "@id": "dct:references",
          "@type": "@id"
        }
      },
      "@id": "dct:source"
    },
    "ImplementationProfile": "gp:ImplementationProfile",
    "rim": "https://w3id.org/ogc/rim/",
    "prov": "http://www.w3.org/ns/prov#",
    "dct": "http://purl.org/dc/terms/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "gp": "https://geolabs.github.io/bblocks-generic-profiles/def/",
    "proc": "https://w3id.org/ogc/api/processes/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://geolabs.github.io/bblocks-generic-profiles/build/annotated/implementation-profile/context.jsonld)

## Sources

* [OGC 14-065 WPS 2.0.2 Interface Standard Corrigendum 2, §7.5.3 Process Implementation Profile](https://docs.ogc.org/is/14-065/14-065.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-generic-profiles](https://github.com/GeoLabs/bblocks-generic-profiles)
* Path: `_sources/implementation-profile`

