#!/usr/bin/env python3
"""Generate the activity type building blocks of this register from scripts/activity-types.yaml.

One acttype:ActivityType item per operation (decision D3): _sources/activity-type/<key>/ with its
bblock.json, schema.yaml, context.jsonld, examples.yaml, examples/<key>.json and description.md.
Files under assets/ are kept as they are. The base block _sources/activity-type/ is hand-written,
except the item class constant this script writes into its schema.yaml.

The Activity Type Register item class is held in one constant, ATR_ITEM_CLASS: the upstream branch
model-tweaks renames it acttype:ActivityTypeItemClass, so it must be changed in one place only.

Families (decision of 2026-11-19): an entry with `family: true` is an abstract activity type, a
sub-class of geoproc:GeoprocessingActivityType that groups operations by meaning; an operation names its
family as `parent`. No Implementation Profile points to a family. The script also writes:
- _sources/activity-type/families.ttl, a data resource of the base block: each family's rdfs:subClassOf,
  untyped, so that geoproc:GeoprocessingActivityTypesShape reaches an operation through its family when
  the operation's example is validated alone;
- the enum of subClassOf in the base schema (geoproc:GeoprocessingActivityType or a family);
- the enum of activityType in the Implementation Profile base schema: the published operations, neither
  a family nor a retired operation, and two failing fixtures of it (a family, a retired operation).

Retirement: an entry with `retired` (date, replacedBy, description) is unpublished, never deleted, with
an unpublish action classified substantive and dct:isReplacedBy towards its replacement, as the
data-types register did for its string-* items (rim:supersededBy would require the replacement to be
typed rim:RegisterItem in the graph of the retired item, which validates alone).

Usage: python3 scripts/activity_types.py
"""
import re
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
GP = "https://w3id.org/geolabs/ospd/generic-profiles/"
AT = GP + "activity-type/"
# GeoLabs SARL: one agent IRI for the four OSPD registers, defined in the data-types register
# (decision of 2026-11-19).
GEOLABS = "https://w3id.org/geolabs/ospd/org/geolabs"
ADDED = "2026-11-09"
# Namespace of the items published before the move to w3id.org on IDENTIFIER_MOVED.
LEGACY_GP = "https://geolabs.github.io/bblocks-generic-profiles/def/"
IDENTIFIER_MOVED = "2026-11-17"
# The operations move under their families on FAMILIES_ADDED (a substantive change of parent class).
FAMILIES_ADDED = "2026-11-19"
SUBCLASS_OF = "http://www.w3.org/2000/01/rdf-schema#subClassOf"


def parent_iri(op):
    return PARENTS.get(op["parent"], AT + op["parent"])


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
        "subClassOf": parent_iri(op),
        "objectIdentifier": iri,
        "itemClass": ATR_ITEM_CLASS,
        "inRegister": GP + "register",
        "validityStatus": "invalid",
        "publicationStatus": "unpublished" if op.get("retired") else "published",
        "hasAction": {
            "id": iri + "/actions/addition",
            "type": "RegisterAction",
            "actionType": "addition",
            "proposer": GEOLABS,
            "startedAtTime": op.get("added", ADDED) + "T00:00:00Z",
            "appliesTo": iri,
        },
    })
    amendments = list(op.get("amendments", []))
    if op["parent"] not in PARENTS and op.get("added", ADDED) < FAMILIES_ADDED:
        # Moved under its family (decision of 2026-11-19): a change of parent class, substantive by
        # the rule of gp:specification for an activity type.
        amendments.append({
            "id": f"family-{FAMILIES_ADDED}", "date": FAMILIES_ADDED, "classification": "substantive",
            "affectedProperty": SUBCLASS_OF,
            "description": (
                f"The parent class (rdfs:subClassOf) changes from {PARENTS['geoprocessing']} to the family "
                f"{parent_iri(op)}, itself a sub-class of it (decision of {FAMILIES_ADDED}: activity types "
                "grouped by meaning). The definition and the entity types are unchanged. Classified "
                "substantive, a change of parent class.")})
    if amendments:
        # In-place amendments of the proposal (gp:amendmentAction, always classified), after its
        # addition, as on the profiles of this register.
        entry["hasAction"] = [entry["hasAction"]] + [{
            "id": f"{iri}/actions/{a['id']}",
            "type": "RegisterAction",
            "actionType": GP + "amendmentAction",
            "changeClassification": a["classification"],
            **({"affectedProperty": a["affectedProperty"]} if a.get("affectedProperty") else {}),
            "description": " ".join(a["description"].split()),
            "proposer": GEOLABS,
            "startedAtTime": f"{a['date']}T00:00:00Z",
            "appliesTo": iri,
        } for a in amendments]
    if op.get("added", ADDED) < IDENTIFIER_MOVED:
        # Published under the github.io namespace: the old IRI stays declared as owl:sameAs, and
        # the move of the identifier is recorded as a clarifying amendment (decision of 2026-11-17).
        old = LEGACY_GP + iri[len(GP):]
        entry = {**{k: v for k, v in entry.items() if k != "hasAction"}, "sameAs": old,
                 "hasAction": (entry["hasAction"] if isinstance(entry["hasAction"], list)
                               else [entry["hasAction"]]) + [{
            "id": f"{iri}/actions/identifier-{IDENTIFIER_MOVED}",
            "type": "RegisterAction",
            "actionType": GP + "amendmentAction",
            "changeClassification": "clarifying",
            "affectedProperty": "https://w3id.org/ogc/rim/objectIdentifier",
            "description": (
                f"The object identifier of this item moves from {old} to {iri}, which resolves "
                f"through w3id.org (decision of {IDENTIFIER_MOVED}); the register actions of the item "
                f"move with it, under {iri}/actions/. The old IRI is kept as owl:sameAs. The content "
                f"of the item is unchanged. Classified clarifying: the item is the same, only its "
                f"identifier changes."),
            "proposer": GEOLABS,
            "startedAtTime": f"{IDENTIFIER_MOVED}T00:00:00Z",
            "appliesTo": iri,
        }]}
    if op.get("retired"):
        r = op["retired"]
        entry["isReplacedBy"] = AT + r["replacedBy"]
        actions = entry["hasAction"] if isinstance(entry["hasAction"], list) else [entry["hasAction"]]
        entry["hasAction"] = actions + [{
            "id": f"{iri}/actions/unpublication",
            "type": "RegisterAction",
            "actionType": "unpublish",
            "changeClassification": "substantive",
            "description": " ".join(r["description"].split()),
            "proposer": GEOLABS,
            "startedAtTime": f"{r['date']}T00:00:00Z",
            "appliesTo": iri,
        }]
    if isinstance(entry["hasAction"], list):
        # The addition first, then the other actions in date order (stable for the same date).
        entry["hasAction"] = entry["hasAction"][:1] + sorted(entry["hasAction"][1:],
                                                             key=lambda a: a["startedAtTime"])
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
        "status": "superseded" if op.get("retired") else "under-development",
        "dateTimeAddition": op.get("added", ADDED) + "T00:00:00Z",
        "dateOfLastChange": op.get("added", ADDED),
        "version": "0.1",
        "itemClass": "schema",
        "register": "generic-profiles",
        "dependsOn": ["generic-profiles.activity-type"],
        "isProfileOf": ["generic-profiles.activity-type"],
        "scope": "dev",
        "tags": ["activity type", "family" if op.get("family") else "operation", op["prefLabel"]],
        "sourceSchema": "schema.yaml",
        "ldContext": "context.jsonld",
        "maturity": "development",
        "group": "Activity Types",
    }
    if op.get("retired"):
        # Aligned on the RIM status (decision of 2026-11-16 on bblock.json status): unpublished and
        # replaced -> superseded, with the replacement as successor.
        entry["successor"] = AT + op["retired"]["replacedBy"]
        entry["highlighted"] = False
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
                "subClassOf": {"const": parent_iri(op)},
            }},
        ],
    }


def at_link(key):
    return f"[`generic-profiles.activity-type.{key}`](../{key}/)"


def description(op, ops):
    iri = AT + op["key"]
    kind = "Activity type family" if op.get("family") else "Activity type"
    parts = [f"{kind}: **{op['prefLabel']}**.", "",
             f"> {' '.join(op['definition'].split())}", ""]
    if op.get("retired"):
        r = op["retired"]
        parts += [f"**Withdrawn on {r['date']}**, replaced by {at_link(r['replacedBy'])}: "
                  f"{' '.join(r['description'].split())}", ""]
    if op.get("altLabel"):
        parts += ["SQL/MM name: " + ", ".join(f"`{a}`" for a in op["altLabel"]) + ".", ""]
    if op["parent"] in PARENTS:
        parent = "`geoproc:GeoprocessingActivityType`"
    else:
        parent = (f"the family {at_link(op['parent'])} (decision of {FAMILIES_ADDED}), itself a "
                  "sub-class of `geoproc:GeoprocessingActivityType`")
    parts += ["## The item", "",
              f"`{iri}` is an `acttype:ActivityType` item of this register (`gp:register`), of the "
              f"Activity Type Register's item class, and an OWL class, sub-class of {parent}.", ""]
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
    if op.get("family"):
        members = [o for o in ops if o["parent"] == op["key"]]
        parts += ["## Members", "",
                  "A family groups operations by meaning (decision of 2026-11-19), proposed by GeoLabs: no "
                  "source defines this grouping. Its members are its sub-classes; the Generic Profiles, "
                  "which group operations by signature, are another axis. No Implementation Profile points "
                  "to a family.", ""]
        parts += [f"- {at_link(o['key'])}" for o in members] + [""]
        if len(members) == 1:
            parts += ["One member so far: the other operations of this kind are not in the register yet.", ""]
        return "\n".join(parts)
    if op.get("retired"):
        parts += ["## Profiles of this operation", "",
                  f"None since {op['retired']['date']}: the Implementation Profiles that pointed here point to "
                  f"{at_link(op['retired']['replacedBy'])}.", ""]
        return "\n".join(parts)
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
@prefix gp:      <https://w3id.org/geolabs/ospd/generic-profiles/> .
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
        {"itemClass": "<https://w3id.org/geolabs/ospd/generic-profiles/item-class/implementation-profile>"}),
    "geoprocessing-without-spatial-entity-fail": (
        "Must fail: a geoprocessing activity type with no spatial entity type. Only "
        "geoproc:GeoprocessingActivityTypesShape (Activity Type Register) can reject it.",
        {"entity": None}),
    # Families (decision of 2026-11-19). The fixture's parent is a family, whose rdfs:subClassOf
    # geoproc:GeoprocessingActivityType is only in families.ttl, the data resource of the base block.
    "family-member-control": (
        "Must pass: an operation under a family, with a spatial entity type.",
        {"parent": "<" + AT + "geometry-measure>"}),
    "family-member-without-spatial-entity-fail": (
        "Must fail: an operation under a family, with no spatial entity type. Only "
        "geoproc:GeoprocessingActivityTypesShape can reject it, and only if families.ttl brings the "
        "family's rdfs:subClassOf into the graph: this proves that the shape reaches an operation "
        "through its family.",
        {"parent": "<" + AT + "geometry-measure>", "entity": None}),
}


def fixtures():
    tests = BASE / "tests"
    tests.mkdir(exist_ok=True)
    for name, (comment, change) in FIXTURES.items():
        iri = AT + "fixture-" + name.replace("-fail", "")
        lines = [
            '    skos:prefLabel "Fixture"@en ;',
            '    skos:definition "An operation used only to test the shapes."@en ;',
            f"    rdfs:subClassOf {change.get('parent', 'geoproc:GeoprocessingActivityType')} ;",
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
                              proposer="" if "proposer" in change else f"    rim:proposer <{GEOLABS}> ;\n")
        (tests / f"{name}.ttl").write_text(text)


def check(ops):
    """Stop on a family that is not under geoprocessing, an operation whose parent is not a family, an
    empty family, a retirement towards an unknown, retired or family entry, or a fixture family that
    does not exist."""
    by_key = {o["key"]: o for o in ops}
    for o in ops:
        if o.get("family") and o["parent"] not in PARENTS:
            raise SystemExit(f"{o['key']}: a family is a sub-class of geoprocessing, not of {o['parent']}")
        if not o.get("family") and o["parent"] not in PARENTS and not by_key.get(o["parent"], {}).get("family"):
            raise SystemExit(f"{o['key']}: parent {o['parent']} is not a family")
        if not o.get("family") and not o.get("retired") and o["parent"] in PARENTS:
            raise SystemExit(f"{o['key']}: an operation is under a family (decision of 2026-11-19)")
        if o.get("family") and not any(m["parent"] == o["key"] for m in ops):
            raise SystemExit(f"{o['key']}: a family with no member")
        if o.get("family") and o.get("retired"):
            raise SystemExit(f"{o['key']}: retiring a family is not handled")
        if o.get("retired"):
            r = by_key.get(o["retired"]["replacedBy"])
            if not r or r.get("retired") or r.get("family"):
                raise SystemExit(f"{o['key']}: replacedBy must be a published operation")
    for _, change in FIXTURES.values():
        if "parent" in change and change["parent"].strip("<>").split("/")[-1] not in by_key:
            raise SystemExit(f"fixture parent {change['parent']} is not an entry")


def write_families(ops):
    """families.ttl: each family's rdfs:subClassOf, untyped (the family is validated in its own block,
    and the shapes that target acttype:ActivityType must not run on this partial description)."""
    lines = ["# Generated by scripts/activity_types.py from scripts/activity-types.yaml. Do not edit.",
             "# Each family's parent class only, so that geoproc:GeoprocessingActivityTypesShape reaches an",
             "# operation through its family when the operation's example is validated alone.",
             "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .", ""]
    for o in ops:
        if o.get("family"):
            lines.append(f"<{AT + o['key']}> rdfs:subClassOf <{parent_iri(o)}> .")
    (BASE / "families.ttl").write_text("\n".join(lines) + "\n")


def write_ip_activity_types(ops):
    """The enum of activityType in the Implementation Profile base schema: the published operations,
    neither a family nor a retired operation. The file is hand-written otherwise: only the block of
    activityType's constraint (from `type: string` to the next key) is rewritten."""
    path = ROOT / "_sources" / "implementation-profile" / "schema.yaml"
    text = path.read_text()
    keys = sorted(o["key"] for o in ops if not o.get("family") and not o.get("retired"))
    new = ("        enum:\n" + "".join(f"        - {AT}{k}\n" for k in keys))
    pattern = re.compile(r"(      activityType:\n(?:        description: >-\n(?:          .*\n)+))"
                         r"(?:        type: string\n        format: uri\n        pattern: .*\n|        enum:\n(?:        - .*\n)+)")
    if len(pattern.findall(text)) != 1:
        raise SystemExit("implementation-profile/schema.yaml: activityType block not found")
    path.write_text(pattern.sub(lambda m: m.group(1) + new, text))


def write_ip_fixtures(ops):
    """Fixtures of the Implementation Profile base schema, each the example of raster-band-math with
    activityType changed (decision of 2026-11-19): to a family, to a retired operation. Both must fail
    on the enum written by write_ip_activity_types."""
    ip = ROOT / "_sources" / "implementation-profile"
    base = json.loads((ip / "raster-band-math" / "examples" / "raster-band-math.json").read_text())
    family = next(o["key"] for o in ops if o.get("family"))
    retired = next(o["key"] for o in ops if o.get("retired"))
    for name, key in (("activity-type-family-fail", family), ("activity-type-retired-fail", retired)):
        dump_json(ip / "tests" / f"{name}.json", {**base, "activityType": AT + key})


def main():
    ops = yaml.safe_load((ROOT / "scripts" / "activity-types.yaml").read_text())
    check(ops)
    fixtures()
    context = json.loads((BASE / "context.jsonld").read_text())
    base_schema = yaml.safe_load((BASE / "schema.yaml").read_text())
    base_schema["allOf"][1]["properties"]["itemClass"]["const"] = ATR_ITEM_CLASS
    sub = base_schema["allOf"][1]["properties"]["subClassOf"]
    sub.pop("const", None)
    sub["description"] = ("geoproc:GeoprocessingActivityType, for a family; a family of this register, for an "
                          "operation (decision of 2026-11-19). Every activity type has at least one GeoSPARQL "
                          "spatial used or generated entity type (geoproc shapes). Written by "
                          "scripts/activity_types.py.")
    sub["enum"] = [PARENTS["geoprocessing"]] + [AT + o["key"] for o in ops if o.get("family")]
    dump_yaml(BASE / "schema.yaml", base_schema)
    write_families(ops)
    write_ip_activity_types(ops)
    write_ip_fixtures(ops)
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
        (out / "description.md").write_text(description(op, ops))
    print(f"{len(ops)} activity types: {sum(1 for o in ops if o.get('family'))} families, "
          f"{sum(1 for o in ops if o.get('retired'))} retired")


if __name__ == "__main__":
    main()
