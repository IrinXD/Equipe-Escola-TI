"""Converte os diagramas do draw.io (casos de uso e classes) em Markdown com Mermaid,
que o GitHub desenha direto na página.

Usado por gerar_docs.py; não precisa rodar sozinho.
"""
import html
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET


def text(cell, sep=" "):
    raw = (cell.get("value") or "") if cell is not None else ""
    raw = re.sub(r"<br\s*/?>|</div>|</p>", "\n", raw, flags=re.I)
    raw = html.unescape(re.sub(r"<[^>]+>", "", raw))
    lines = [re.sub(r"\s+", " ", l).strip() for l in raw.split("\n")]
    lines = [l for l in lines if l]
    return lines if sep is None else sep.join(lines)


def style(cell):
    st = cell.get("style") or ""
    d = {}
    parts = st.split(";")
    d["_shape"] = parts[0]
    for kv in parts:
        if "=" in kv:
            k, v = kv.split("=", 1)
            d[k] = v
    return d


def geo(cell):
    g = cell.find("mxGeometry")
    if g is None:
        return None
    return tuple(float(g.get(k, 0)) for k in ("x", "y", "width", "height"))


def point(edge, name):
    g = edge.find("mxGeometry")
    if g is None:
        return None
    for p in g.findall("mxPoint"):
        if p.get("as") == name:
            return float(p.get("x", 0)), float(p.get("y", 0))
    return None


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"\W+", "_", s).strip("_") or "x"


def load(path):
    root = ET.parse(path).getroot()
    cells = {c.get("id"): c for c in root.iter("mxCell")}
    return cells


def inside(inner, outer):
    x, y, w, h = inner
    cx, cy = x + w / 2, y + h / 2
    ox, oy, ow, oh = outer
    return ox <= cx <= ox + ow and oy <= cy <= oy + oh


# ---------------------------------------------------------------- classes
def classes(path):
    cells = load(path)
    klass = {}
    for c in cells.values():
        if style(c).get("_shape") == "swimlane":
            kids = [d for d in cells.values() if d.get("parent") == c.get("id")
                    and style(d).get("_shape") == "text"]
            kids.sort(key=lambda d: geo(d)[1])
            attrs = text(kids[0], None) if kids else []
            meths = text(kids[1], None) if len(kids) > 1 else []
            klass[c.get("id")] = dict(name=text(c), attrs=attrs, meths=meths, geo=geo(c))
    groups = []
    for c in cells.values():
        if style(c).get("_shape") == "rounded=1" or (c.get("vertex") and (c.get("style") or "").startswith("rounded=1")):
            groups.append(dict(name=text(c), geo=geo(c), members=[]))
    groups.sort(key=lambda g: g["geo"][0])
    for k in klass.values():
        k["group"] = None
        for g in groups:
            if inside(k["geo"], g["geo"]):
                k["group"] = g["name"]
                g["members"].append(k["name"])
                break
    rels = []
    for e in cells.values():
        if not e.get("edge"):
            continue
        s, t = klass.get(e.get("source")), klass.get(e.get("target"))
        if not s or not t:
            continue
        st = style(e)
        labels = {}
        for d in cells.values():
            if d.get("parent") == e.get("id"):
                x = float(d.find("mxGeometry").get("x", 0))
                labels["s" if x < 0 else "t"] = text(d)
        name = text(e)
        if st.get("endArrow") == "block" and st.get("endFill", "1") == "0":
            arrow = "<|--"; s, t = t, s; labels = {"s": labels.get("t"), "t": labels.get("s")}
        elif st.get("endArrow") == "block":
            arrow = "<|--"; s, t = t, s; labels = {"s": labels.get("t"), "t": labels.get("s")}
        elif st.get("startArrow", "").startswith("diamond"):
            arrow = "*--" if st.get("startFill", "1") == "1" else "o--"
        elif st.get("dashed") == "1":
            arrow = "..>"
        else:
            arrow = "-->"
        rels.append(dict(s=s["name"], t=t["name"], arrow=arrow,
                         ls=labels.get("s"), lt=labels.get("t"), label=name))
    return klass, groups, rels


def member(m):
    m = m.replace("<", "~").replace(">", "~")
    if ":" in m and m.split(":", 1)[0].find("(") == -1:
        # atributo: parênteses no tipo fariam o Mermaid tratar como método
        m = m.replace("(", "[").replace(")", "]")
    return m.replace("+ ", "+").replace("- ", "-").replace("# ", "#")


def class_block(k, indent="  "):
    out = [f"{indent}class {k['name']} {{"]
    for a in k["attrs"]:
        out.append(f"{indent}  {member(a)}")
    for m in k["meths"]:
        out.append(f"{indent}  {member(m)}")
    out.append(f"{indent}}}")
    return out


def rel_line(r):
    ls = f' "{r["ls"]}"' if r["ls"] else ""
    lt = f' "{r["lt"]}"' if r["lt"] else ""
    lab = f" : {r['label']}" if r["label"] else ""
    return f"  {r['s']}{ls} {r['arrow']}{lt} {r['t']}{lab}"


def render_classes(path, out, header):
    klass, groups, rels = classes(path)
    by_name = {k["name"]: k for k in klass.values()}
    L = []
    L.append("# Diagrama de Classes")
    L.append("")
    L += header
    L.append("")
    L.append(f"**{len(klass)} classes** em **{len(groups)} módulos** e **{len(rels)} relacionamentos**.")
    L.append("")
    L.append("Legenda: `*--` composição · `o--` agregação · `-->` associação · `<|--` herança. Os números são as multiplicidades.")
    L.append("")
    L.append("## Sumário")
    L.append("")
    L.append("- [Visão geral (classes e relacionamentos)](#visão-geral)")
    for g in groups:
        L.append(f"- [{g['name']}](#{anchor(g['name'])})")
    L.append("")
    L.append("## Visão geral")
    L.append("")
    L.append("Todas as classes, só com os nomes, para enxergar como os módulos se ligam. Os atributos e métodos estão nas seções de cada módulo.")
    L.append("")
    L.append("```mermaid")
    L.append("classDiagram")
    L.append("  direction LR")
    for g in groups:
        L.append(f"  namespace {slug(g['name'])} {{")
        for n in g["members"]:
            L.append(f"    class {n}")
        L.append("  }")
    for k in klass.values():
        if not k["group"]:
            L.append(f"  class {k['name']}")
    for r in rels:
        L.append(rel_line(r))
    L.append("```")
    L.append("")
    for g in groups:
        L.append(f"## {g['name']}")
        L.append("")
        mem = set(g["members"])
        ext = set()
        rr = [r for r in rels if r["s"] in mem or r["t"] in mem]
        for r in rr:
            for n in (r["s"], r["t"]):
                if n not in mem:
                    ext.add(n)
        L.append("Classes do módulo: " + ", ".join(f"`{n}`" for n in g["members"]) + ".")
        if ext:
            L.append("")
            L.append("Ligações com outros módulos: " + ", ".join(f"`{n}`" for n in sorted(ext)) + " (aparecem sem detalhes).")
        L.append("")
        L.append("```mermaid")
        L.append("classDiagram")
        for n in g["members"]:
            L += class_block(by_name[n])
        for n in sorted(ext):
            L.append(f"  class {n}")
        for r in rr:
            L.append(rel_line(r))
        L.append("```")
        L.append("")
        L.append("<details><summary>Atributos e métodos em texto</summary>")
        L.append("")
        for n in g["members"]:
            k = by_name[n]
            L.append(f"**{n}**")
            L.append("")
            L.append("| Atributos | Métodos |")
            L.append("|---|---|")
            rows = max(len(k["attrs"]), len(k["meths"]), 1)
            for i in range(rows):
                a = k["attrs"][i] if i < len(k["attrs"]) else ""
                m = k["meths"][i] if i < len(k["meths"]) else ""
                L.append(f"| `{a}` | `{m}` |" .replace("``", ""))
            L.append("")
        L.append("</details>")
        L.append("")
    open(out, "w", encoding="utf-8").write("\n".join(L))


# ---------------------------------------------------------------- casos de uso
def render_casos(path, out, header):
    cells = load(path)
    shapes = {}
    for c in cells.values():
        sh = style(c).get("_shape")
        if sh in ("ellipse", "shape=folder", "shape=umlActor"):
            shapes[c.get("id")] = dict(kind=sh, name=text(c), geo=geo(c), id=c.get("id"))
    folders = sorted([s for s in shapes.values() if s["kind"] == "shape=folder"], key=lambda s: (s["geo"][1], s["geo"][0]))
    cases = [s for s in shapes.values() if s["kind"] == "ellipse"]
    actors = [s for s in shapes.values() if s["kind"] == "shape=umlActor"]
    for uc in cases:
        uc["folder"] = None
        for f in folders:
            if inside(uc["geo"], f["geo"]):
                uc["folder"] = f["name"]
                break

    def nearest(p):
        if p is None:
            return None
        best, bd = None, 1e18
        for s in shapes.values():
            if s["kind"] == "shape=folder":
                continue
            x, y, w, h = s["geo"]
            dx = max(x - p[0], 0, p[0] - (x + w))
            dy = max(y - p[1], 0, p[1] - (y + h))
            d = dx * dx + dy * dy
            if d < bd:
                best, bd = s, d
        return best if bd < 60 * 60 else None

    links = []
    for e in cells.values():
        if not e.get("edge"):
            continue
        s = shapes.get(e.get("source")) or nearest(point(e, "sourcePoint"))
        t = shapes.get(e.get("target")) or nearest(point(e, "targetPoint"))
        if not s or not t or s is t:
            continue
        lbl = text(e) or " ".join(text(d) for d in cells.values() if d.get("parent") == e.get("id"))
        st = style(e)
        kind = "assoc"
        if "include" in lbl:
            kind = "include"
        elif "extend" in lbl:
            kind = "extend"
        elif st.get("dashed") == "1":
            kind = "dep"
        if kind == "assoc" and t["kind"] == "shape=umlActor":
            s, t = t, s
        links.append(dict(s=s, t=t, kind=kind))

    ids = {}
    for i, a in enumerate(sorted(actors, key=lambda a: a["name"])):
        ids[a["id"]] = f"A{i + 1}"
    for i, u in enumerate(sorted(cases, key=lambda u: (u["folder"] or "~", u["name"]))):
        ids[u["id"]] = f"U{i + 1}"

    def node(s):
        q = s["name"].replace('"', "'")
        if s["kind"] == "shape=umlActor":
            return f'{ids[s["id"]]}["👤 {q}"]'
        return f'{ids[s["id"]]}(["{q}"])'

    def link(l):
        a, b = ids[l["s"]["id"]], ids[l["t"]["id"]]
        if l["kind"] == "include":
            return f"  {a} -. \"«include»\" .-> {b}"
        if l["kind"] == "extend":
            return f"  {a} -. \"«extend»\" .-> {b}"
        if l["kind"] == "dep":
            return f"  {a} -.-> {b}"
        return f"  {a} --- {b}"

    L = ["# Diagrama de Casos de Uso", ""]
    L += header
    L.append("")
    L.append(f"**{len(cases)} casos de uso**, **{len(actors)} atores** ({', '.join(a['name'] for a in sorted(actors, key=lambda a: a['name']))}) em **{len(folders)} pacotes**.")
    L.append("")
    L.append("Legenda: linha cheia = ator participa do caso de uso · tracejada `«include»` = sempre executa o outro · tracejada `«extend»` = pode executar o outro.")
    L.append("")
    L.append("O detalhamento de cada caso de uso (fluxos, pré e pós-condições) está em [Casos de Uso detalhados](casos-de-uso.md).")
    L.append("")
    L.append("## Sumário")
    L.append("")
    for f in folders:
        L.append(f"- [{f['name']}](#{anchor(f['name'])})")
    L.append("- [Lista completa](#lista-completa)")
    L.append("")
    for f in folders:
        mine = [u for u in cases if u["folder"] == f["name"]]
        mine.sort(key=lambda u: u["name"])
        mids = {u["id"] for u in mine}
        ll = [l for l in links if l["s"]["id"] in mids or l["t"]["id"] in mids]
        extra = {}
        for l in ll:
            for s in (l["s"], l["t"]):
                if s["id"] not in mids:
                    extra[s["id"]] = s
        L.append(f"## {f['name']}")
        L.append("")
        L.append("```mermaid")
        L.append("flowchart LR")
        for s in extra.values():
            if s["kind"] == "shape=umlActor":
                L.append("  " + node(s))
        L.append(f'  subgraph {slug(f["name"])}["{f["name"]}"]')
        for u in mine:
            L.append("    " + node(u))
        L.append("  end")
        for s in extra.values():
            if s["kind"] != "shape=umlActor":
                L.append("  " + node(s))
        for l in ll:
            L.append(link(l))
        L.append("```")
        L.append("")
    L.append("## Lista completa")
    L.append("")
    L.append("| Pacote | Caso de uso | Atores | Relações |")
    L.append("|---|---|---|---|")
    for u in sorted(cases, key=lambda u: ([f["name"] for f in folders] + [None]).index(u["folder"]) if u["folder"] in [f["name"] for f in folders] else 99):
        act = sorted({(l["s"] if l["t"] is u else l["t"])["name"] for l in links
                      if l["kind"] == "assoc" and (l["s"] is u or l["t"] is u)
                      and (l["s"] if l["t"] is u else l["t"])["kind"] == "shape=umlActor"})
        rel = [f"«{l['kind']}» {l['t']['name']}" for l in links if l["s"] is u and l["kind"] in ("include", "extend")]
        L.append(f"| {u['folder'] or '—'} | {u['name']} | {', '.join(act) or '—'} | {'<br>'.join(rel) or '—'} |")
    L.append("")
    open(out, "w", encoding="utf-8").write("\n".join(L))


def anchor(s):
    s = s.lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")
