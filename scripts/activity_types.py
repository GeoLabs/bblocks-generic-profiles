#!/usr/bin/env python3
"""Generate the activity type building blocks of this register from scripts/activity-types.yaml.

One acttype:ActivityType item per operation (decision D3): _sources/activity-type/<key>/ with its
bblock.json, schema.yaml, context.jsonld, examples.yaml, examples/<key>.json and description.md.
Files under assets/ are kept as they are. The base block _sources/activity-type/ is hand-written,
except the item class constant this script writes into its schema.yaml.

The Activity Type Register item class is held in one constant, ATR_ITEM_CLASS: the upstream branch
model-tweaks renames it acttype:ActivityTypeItemClass, so it must be changed in one place only.

Usage: python3 scripts/activity_types.py
"""
import json
import pathlib

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = ROOT / "_sources" / "activity-type"

ACTTYPE_NS = "https://w3id.org/ogc/rim/activity-type/"
ATR_ITEM_CLASS = ACTTYPE_NS + "activityTypeItemClass"
# Every activity type of this register is a geoprocessing activity type (decision of 2026-11-09).
PARENTS = {
    "geoprocessing": "https://w3id.org/ogc/rim/geoprocessing/GeoprocessingActivityType",
}
PREFIXES = {"geo:": "http://www.opengis.net/ont/geosparql#", "prov:": "http://www.w3.org/ns/prov#"}
GP = "https://geolabs.github.io/bblocks-generic-profiles/def/"
AT = GP + "activity-type/"
GEOLABS = GP + "geolabs"
ADDED = "2026-11-09"


def expand(curie):
    for prefix, ns in PREFIXES.items():
        if curie.startswith(prefix):
            return ns + curie[len(prefix):]
    return curie


def dump_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def dump_yaml(path, data):
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100))


def item(op):
    iri = AT + op["key"]
    entry = {
        "id": iri,
        "type": ["ActivityType", "Class"],
        "prefLabel": op["prefLabel"],
    }
    if op.get("altLabel"):
        entry["altLabel"] = op["altLabel"]
    entry.update({
        "definition": " ".join(op["definition"].split()),
        "subClassOf": PARENTS[op["parent"]],
        "objectIdentifier": iri,
        "itemClass": ATR_ITEM_CLASS,
        "inRegister": GP + "register",
        "validityStatus": "invalid",
        "publicationStatus": "published",
        "hasAction": {
            "id": iri + "/actions/addition",
            "type": "RegisterAction",
            "actionType": "addition",
            "proposer": GEOLABS,
            "startedAtTime": op.get("added", ADDED) + "T00:00:00Z",
            "appliesTo": iri,
        },
    })
    for key in ("usedEntityType", "generatedEntityType"):
        values = [expand(v) for v in op.get(key, [])]
        # The ATR JSON schema (activity-types-schema) types each of these as one IRI.
        assert len(values) <= 1, f"{op['key']}: one {key} at most"
        if values:
            entry[key] = values[0]
    entry["associatedAgentType"] = PREFIXES["prov:"] + "SoftwareAgent"
    if op.get("sources"):
        entry["source"] = op["sources"]
    return entry


def bblock(op):
    entry = {
        "$schema": "https://raw.githubusercontent.com/opengeospatial/bblocks-postprocess/master/ogc/bblocks/metadata-schema.yaml",
        "name": f"Activity type: {op['prefLabel']}",
        "abstract": " ".join(op["definition"].split()),
        "status": "under-development",
        "dateTimeAddition": op.get("added", ADDED) + "T00:00:00Z",
        "dateOfLastChange": op.get("added", ADDED),
        "version": "0.1",
        "itemClass": "schema",
        "register": "generic-profiles",
        "dependsOn": ["generic-profiles.activity-type"],
        "isProfileOf": ["generic-profiles.activity-type"],
        "scope": "dev",
        "tags": ["activity type", "operation", op["prefLabel"]],
        "sourceSchema": "schema.yaml",
        "ldContext": "context.jsonld",
        "maturity": "development",
        "group": "Activity Types",
    }
    if op.get("sources"):
        entry["sources"] = op["sources"]
    return entry


def schema(op):
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "description": (f"The activity type \"{op['prefLabel']}\" -- see generic-profiles.activity-type for "
                        "the shape every activity type of this register shares."),
        "allOf": [
            {"$ref": "bblocks://generic-profiles.activity-type"},
            {"type": "object", "properties": {
                "id": {"const": AT + op["key"]},
                "prefLabel": {"const": op["prefLabel"]},
                "subClassOf": {"const": PARENTS[op["parent"]]},
            }},
        ],
    }


def description(op):
    iri = AT + op["key"]
    ip = GP + "implementation-profile/" + op["key"]
    parts = [f"Activity type: **{op['prefLabel']}**.", "",
             f"> {' '.join(op['definition'].split())}", ""]
    if op.get("altLabel"):
        parts += ["SQL/MM name: " + ", ".join(f"`{a}`" for a in op["altLabel"]) + ".", ""]
    parts += ["## The item", "",
              f"`{iri}` is an `acttype:ActivityType` item of this register (`gp:register`), of the "
              "Activity Type Register's item class, and an OWL class, sub-class of "
              "`geoproc:GeoprocessingActivityType`.", ""]
    parts += ["Its activities use or generate spatial data, declared with GeoSPARQL 1.1 classes: "
              + "; ".join(f"`{k}` {', '.join('`' + v + '`' for v in op[k])}"
                          for k in ("usedEntityType", "generatedEntityType") if op.get(k)) + ". "
              "The class is chosen per kind of role (see `scripts/activity-types.yaml`); how a data type of "
              "`bblocks-data-types` maps to an entity type is still open (decision D8, question 5).", ""]
    parts += ["The run of an activity of this type is not typed here (decision D8, open).", ""]
    if op.get("sources"):
        parts += ["## Sources", ""]
        for s in op["sources"]:
            parts.append(f"- [{s['title']}]({s['link']})" if s.get("link") else f"- {s['title']}")
        parts.append("")
    if op.get("note"):
        parts += ["## Notes", "", " ".join(op["note"].split()), ""]
    if op.get("illustration"):
        parts += ["## Illustration", "", op["illustration"], ""]
    # One activity type per operation (decision D3); several Implementation Profiles may point to it
    # (decision C4 of 2026-11-10). `profiles` lists them; by default, the one named like the operation.
    profiles = op.get("profiles", [op["key"]])
    links = ", ".join(f"[`generic-profiles.implementation-profile.{p}`](../../implementation-profile/{p}/)"
                      for p in profiles)
    if len(profiles) == 1:
        text = (f"The Implementation Profile {links} points here with `activityType`. It holds the "
                "signature and the representations; this item holds the meaning.")
    else:
        text = (f"The Implementation Profiles {links} point here with `activityType`: the same operation, bound "
                "to different representations or cardinalities. They hold the signature and the representations; "
                "this item holds the meaning.")
    parts += ["## Profiles of this operation", "", text, ""]
    return "\n".join(parts)


FIXTURE = """# {comment}
@prefix gp:      <https://geolabs.github.io/bblocks-generic-profiles/def/> .
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix geoproc: <https://w3id.org/ogc/rim/geoprocessing/> .
@prefix geo:     <http://www.opengis.net/ont/geosparql#> .
@prefix rim:     <https://w3id.org/ogc/rim/> .
@prefix skos:    <http://www.w3.org/2004/02/skos/core#> .
@prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl:     <http://www.w3.org/2002/07/owl#> .
@prefix prov:    <http://www.w3.org/ns/prov#> .
@prefix xsd:     <http://www.w3.org/2001/XMLSchema#> .

<{iri}> a {types} ;
{body}
<{iri}/actions/addition> a rim:RegisterAction ;
    rim:actionType rim:additionAction ;
{proposer}    rim:appliesTo <{iri}> ;
    prov:startedAtTime "2026-11-09T00:00:00Z"^^xsd:dateTime .
"""

# name -> (comment, changes). Each fixture is the control with one change, so that only one
# constraint can reject it.
FIXTURES = {
    "activity-type-control": ("Must pass: the control of the -fail fixtures here.", {}),
    "activity-type-without-definition-fail": (
        "Must fail: no skos:definition. Only gp:ActivityTypeShape can reject it.", {"definition": None}),
    "activity-type-other-register-fail": (
        "Must fail: in another register. Only gp:ActivityTypeShape can reject it.",
        {"register": "<https://example.org/register>"}),
    "activity-type-not-a-class-fail": (
        "Must fail: not an owl:Class. Only gp:ActivityTypeShape can reject it.",
        {"types": "acttype:ActivityType"}),
    "activity-type-without-addition-fail": (
        "Must fail: its action has no proposer. Only gp:ActivityTypeShape can reject it.",
        {"proposer": None}),
    "activity-type-without-status-fail": (
        "Must fail: no rim:publicationStatus. Only rim:RegisterItemShape (Registered Item Model) can "
        "reject it: this proves that the model's item shape reaches an activity type of this register.",
        {"publication": None}),
    "activity-type-other-item-class-fail": (
        "Must fail: the item class of an Implementation Profile. Only acttype:ActivityTypeShape "
        "(Activity Type Register) can reject it: this proves that its shapes run here.",
        {"itemClass": "<https://geolabs.github.io/bblocks-generic-profiles/def/item-class/implementation-profile>"}),
    "geoprocessing-without-spatial-entity-fail": (
        "Must fail: a geoprocessing activity type with no spatial entity type. Only "
        "geoproc:GeoprocessingActivityTypesShape (Activity Type Register) can reject it.",
        {"entity": None}),
}


def fixtures():
    tests = BASE / "tests"
    tests.mkdir(exist_ok=True)
    for name, (comment, change) in FIXTURES.items():
        iri = AT + "fixture-" + name.replace("-fail", "")
        lines = [
            '    skos:prefLabel "Fixture"@en ;',
            '    skos:definition "An operation used only to test the shapes."@en ;',
            "    rdfs:subClassOf geoproc:GeoprocessingActivityType ;",
            f'    rim:objectIdentifier "{iri}"^^xsd:anyURI ;',
            f"    rim:itemClass {change.get('itemClass', '<' + ATR_ITEM_CLASS + '>')} ;",
            f"    rim:inRegister {change.get('register', 'gp:register')} ;",
            "    rim:validityStatus rim:invalid ;",
            "    rim:publicationStatus rim:published ;",
            "    acttype:usedEntityType geo:Geometry ;",
            "    acttype:associatedAgentType prov:SoftwareAgent ;",
            f"    rim:hasAction <{iri}/actions/addition> .",
            "",
        ]
        drop = {"definition": "skos:definition", "publication": "rim:publicationStatus",
                "entity": "acttype:usedEntityType"}
        lines = [l for l in lines if not any(k in change and change[k] is None and v in l for k, v in drop.items())]
        text = FIXTURE.format(comment=comment, iri=iri, types=change.get("types", "acttype:ActivityType , owl:Class"),
                              body="\n".join(lines),
                              proposer="" if "proposer" in change else "    rim:proposer gp:geolabs ;\n")
        (tests / f"{name}.ttl").write_text(text)


def main():
    fixtures()
    ops = yaml.safe_load((ROOT / "scripts" / "activity-types.yaml").read_text())
    context = json.loads((BASE / "context.jsonld").read_text())
    base_schema = yaml.safe_load((BASE / "schema.yaml").read_text())
    base_schema["allOf"][1]["properties"]["itemClass"]["const"] = ATR_ITEM_CLASS
    dump_yaml(BASE / "schema.yaml", base_schema)
    for op in ops:
        out = BASE / op["key"]
        dump_json(out / "examples" / f"{op['key']}.json", item(op))
        dump_json(out / "bblock.json", bblock(op))
        dump_json(out / "context.jsonld", context)
        dump_yaml(out / "schema.yaml", schema(op))
        dump_yaml(out / "examples.yaml", [{
            "title": op["prefLabel"],
            "base-uri": AT,
            "snippets": [{"language": "json", "ref": f"examples/{op['key']}.json"}],
        }])
        (out / "description.md").write_text(description(op))
    print(f"{len(ops)} activity types")


if __name__ == "__main__":
    main()
