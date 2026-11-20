"""Gera a pasta docs/ com versões em Markdown de toda a documentação do projeto,
para ler direto no GitHub (o GitHub não abre .docx, .xlsx nem .drawio).

Os arquivos originais NÃO são alterados: eles continuam sendo a fonte oficial.
Quando alguém atualizar um .docx, .drawio ou PDF, rode de novo:

    python3 scripts/docs/gerar_docs.py              # tudo
    python3 scripts/docs/gerar_docs.py --sem-imagens # pula as prévias dos PDFs (mais rápido)

Precisa de: pandoc, poppler-utils (pdftoppm) e Python com openpyxl e Pillow.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import drawio2mermaid  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DOCS = os.path.join(RAIZ, "docs")
ASSETS = os.path.join(DOCS, "assets")
REPO_RAW = "https://raw.githubusercontent.com/bialemesvsouza/Equipe-Escola-TI/main/"

GESTAO = "Documentação de Gestão - Mercado"
DIAG = "Documentos de Diagramas"
SEQ = DIAG + "/DiagramasDeSequencia"
ARQ = "Documentação Arquitetura"
DESIGN = "Design - UI"
WIRE = DESIGN + "/Wireframes"
HORAS = "Consolidado de Horas por Integrante - Projeto TI.pdf"

# (origem .docx, destino em docs/, título)
DOCX = [
    (f"{GESTAO}/Documento_de_Abertura_do_Projeto_Mind_Liner.docx", "01-gestao/abertura-do-projeto", "Documento de Abertura do Projeto"),
    (f"{GESTAO}/MindLiner — Pesquisa de Mercado e Aplicação de Ferramentas.docx", "01-gestao/pesquisa-de-mercado", "Pesquisa de Mercado e Aplicação de Ferramentas"),
    (f"{GESTAO}/Mind Liner — Análise de Concorrentes_.docx", "01-gestao/analise-de-concorrentes", "Análise de Concorrentes"),
    (f"{GESTAO}/Mind Liner — Análise SWOT Estratégica.docx", "01-gestao/analise-swot", "Análise SWOT Estratégica"),
    (f"{GESTAO}/INPI e Matriz GUT.docx", "01-gestao/inpi-e-matriz-gut", "INPI e Matriz GUT"),
    (f"{GESTAO}/LGPD Termos.docx", "01-gestao/lgpd-termos", "LGPD e Termos"),
    (f"{GESTAO}/Mapeamento do Código de Defesa do Consumidor (Mindliner).docx", "01-gestao/codigo-de-defesa-do-consumidor", "Mapeamento do Código de Defesa do Consumidor"),
    (f"{DIAG}/Requisitos Funcionais_.docx", "02-requisitos/requisitos-funcionais", "Requisitos Funcionais"),
    (f"{DIAG}/Requisitos_Nao_Funcionais_MindLine.docx", "02-requisitos/requisitos-nao-funcionais", "Requisitos Não Funcionais"),
    (f"{DIAG}/Regras de negócio.docx", "02-requisitos/regras-de-negocio", "Regras de Negócio"),
    (f"{DIAG}/Histórias de Usuário_.docx", "02-requisitos/historias-de-usuario", "Histórias de Usuário"),
    (f"{DIAG}/Casos de Uso (Atualizados).docx", "03-diagramas/casos-de-uso", "Casos de Uso (detalhados)"),
    (f"{ARQ}/Documentação de Arquitetura - Encontro 6.docx", "04-arquitetura/arquitetura", "Documentação de Arquitetura"),
    (f"{DESIGN}/Pesquisa de Branding.docx", "05-design/pesquisa-de-branding", "Pesquisa de Branding"),
]


# ------------------------------------------------------------------ utilidades
def link(de, para):
    """Link relativo (com espaços e acentos escapados) do arquivo `de` até `para`, ambos relativos à raiz."""
    rel = os.path.relpath(os.path.join(RAIZ, para), os.path.dirname(os.path.join(RAIZ, de)))
    return quote(rel.replace(os.sep, "/"))


def ancora(titulo, usadas):
    """Mesma regra de âncoras que o GitHub usa nos títulos."""
    t = re.sub(r"<[^>]+>", "", titulo)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = t.replace("*", "").replace("`", "").strip().lower()
    t = re.sub(r"[^\w\- ]", "", t).replace(" ", "-")
    base, n = t, usadas.get(t, 0)
    usadas[t] = n + 1
    return base if n == 0 else f"{base}-{n}"


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def escrever(rel, linhas):
    caminho = os.path.join(DOCS, rel)
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    texto = "\n".join(linhas) if isinstance(linhas, list) else linhas
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(texto.rstrip() + "\n")


def cabecalho(destino, origens, extra=None):
    """Aviso no topo de cada página gerada, apontando para o arquivo original."""
    d = f"docs/{destino}"
    fontes = ", ".join(f"[`{os.path.basename(o.rstrip('/'))}{'/' if o.endswith('/') else ''}`]({link(d, o)})"
                       for o in origens)
    linhas = [f"> Página gerada a partir de {fontes} para leitura no GitHub. "
              "O arquivo original continua sendo a fonte oficial: edite o original e rode "
              "`python3 scripts/docs/gerar_docs.py`."]
    if extra:
        linhas += [">", f"> {extra}"]
    linhas += ["", f"[⬅ Voltar ao sumário]({link(d, 'docs/README.md')})", ""]
    return linhas


def sumario(corpo, nivel_min=2, nivel_max=3):
    usadas, itens = {}, []
    no_codigo = False
    for l in corpo.split("\n"):
        if l.startswith("```"):
            no_codigo = not no_codigo
        m = None if no_codigo else re.match(r"^(#{1,6})\s+(.*)$", l)
        if not m:
            continue
        n, t = len(m.group(1)), m.group(2).strip()
        a = ancora(t, usadas)
        if nivel_min <= n <= nivel_max and re.sub(r"[*`\s]", "", t):
            limpo = re.sub(r"<[^>]+>", "", t).replace("**", "").strip()
            # Só recua se já existe um item "pai" acima; senão a lista fica torta.
            recuo = (n - nivel_min) if any(not i.startswith(" ") for i in itens) else 0
            itens.append("  " * recuo + f"- [{limpo}](#{a})")
    return itens


# ------------------------------------------------------------------ .docx -> .md
def ajustar_historias(md):
    """No .docx os títulos das histórias são parágrafos comuns; aqui viram títulos."""
    saida = []
    for l in md.split("\n"):
        s = l.strip()
        if re.match(r"^\**HU\d+\s*[—–-]", s):
            saida.append("### " + s.strip("*"))
        elif s and not s.startswith(("Como ", "#", "|", ">", "-", "*", "<")) and len(s) < 60 and not s.endswith((".", ":", ";")):
            saida.append("## " + s.strip("*"))
        else:
            saida.append(l)
    return "\n".join(saida)


def converter_docx(origem, destino, titulo, extra_pos=None):
    nome = os.path.basename(destino)
    pasta_img = os.path.join(ASSETS, nome)
    with tempfile.TemporaryDirectory() as tmp:
        md = subprocess.run(
            ["pandoc", os.path.join(RAIZ, origem), "-t", "gfm", "--wrap=none", "--extract-media", tmp],
            check=True, capture_output=True, text=True).stdout
        imagens = {}
        for raiz, _, arquivos in os.walk(tmp):
            for a in sorted(arquivos):
                os.makedirs(pasta_img, exist_ok=True)
                shutil.copy(os.path.join(raiz, a), os.path.join(pasta_img, a))
                imagens[os.path.join(raiz, a)] = f"../assets/{nome}/{a}"

    def troca_img(m):
        src = m.group(1)
        alt = m.group(2) if m.lastindex and m.lastindex >= 2 and m.group(2) else "Figura"
        return f"![{alt}]({imagens.get(src, src)})"

    md = re.sub(r'<img src="([^"]+)"(?:[^>]*?alt="([^"]*)")?[^>]*/>', troca_img, md)
    md = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)",
                lambda m: f"![{m.group(1) or 'Figura'}]({imagens.get(m.group(2), m.group(2))})", md)
    # O GitHub ignora largura de colunas em <colgroup>; deixa as tabelas mais limpas.
    md = re.sub(r"<colgroup>.*?</colgroup>\n?", "", md, flags=re.S)

    if destino.endswith("historias-de-usuario"):
        md = ajustar_historias(md)

    extra = None
    if destino.endswith("historias-de-usuario"):
        extra = ("Os diagramas de sequência de cada história estão em "
                 f"[Diagramas de Sequência]({link('docs/' + destino + '.md', 'docs/03-diagramas/diagramas-de-sequencia.md')}).")
    linhas = [f"# {titulo}", ""] + cabecalho(destino + ".md", [origem], extra)
    toc = sumario(md)
    if len(toc) >= 3:
        linhas += ["## Sumário", "", *toc, ""]
    linhas += [md]
    if extra_pos:
        linhas += ["", *extra_pos]
    escrever(destino + ".md", linhas)
    return toc


# ------------------------------------------------------------------ PDFs -> prévias
def previa_pdf(origem, destino_rel, largura, formato="png"):
    """Renderiza a página do PDF como imagem, recortando a margem branca."""
    from PIL import Image, ImageChops

    destino = os.path.join(ASSETS, destino_rel)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    info = subprocess.run(["pdfinfo", os.path.join(RAIZ, origem)], capture_output=True, text=True).stdout
    larg_pts, alt_pts = map(float, re.search(r"Page size:\s+([\d.]+) x ([\d.]+)", info).groups())
    if larg_pts > alt_pts * 1.2:
        largura *= 2  # telas de desktop lado a lado: precisa de mais resolução para ler
    # Alguns diagramas ocupam só o meio da página: renderiza com folga e recorta depois.
    folga = 2.5 if formato == "png" else 1.0
    dpi = max(20, min(300, int(72 * largura * folga / larg_pts)))
    with tempfile.TemporaryDirectory() as tmp:
        base = os.path.join(tmp, "p")
        subprocess.run(["pdftoppm", "-singlefile", "-png", "-r", str(dpi), os.path.join(RAIZ, origem), base],
                       check=True, capture_output=True)
        img = Image.open(base + ".png").convert("RGB")
    fundo = Image.new("RGB", img.size, img.getpixel((0, 0)))
    caixa = ImageChops.difference(img, fundo).getbbox()
    if caixa:
        m = 16
        img = img.crop((max(caixa[0] - m, 0), max(caixa[1] - m, 0),
                        min(caixa[2] + m, img.width), min(caixa[3] + m, img.height)))
    if img.width > largura:
        img = img.resize((largura, round(img.height * largura / img.width)), Image.LANCZOS)
    if formato == "jpg":
        img.save(destino, "JPEG", quality=78, optimize=True, progressive=True)
    else:
        img = img.quantize(colors=256, method=Image.Quantize.MEDIANCUT)
        img.save(destino, "PNG", optimize=True)


def textos_hu(origem):
    texto = subprocess.run(["pdftotext", os.path.join(RAIZ, origem), "-"], capture_output=True, text=True).stdout
    return [re.sub(r"\s+", " ", l).strip() for l in texto.split("\n") if re.match(r"^HU\d+\s*[-—–]", l)]


def numero(nome):
    m = re.search(r"(\d+)", nome)
    return int(m.group(1)) if m else 999


# ------------------------------------------------------------------ páginas
def pagina_sequencia(imagens):
    pdfs = sorted((a for a in os.listdir(os.path.join(RAIZ, SEQ)) if a.lower().endswith(".pdf")), key=numero)
    destino = "03-diagramas/diagramas-de-sequencia.md"
    d = "docs/" + destino
    L = ["# Diagramas de Sequência", ""]
    L += cabecalho(destino, [SEQ + "/"],
                   "Cada PDF cobre um grupo de **histórias de usuário** (HU001 a HU070). "
                   "O nome do arquivo (\"UC 1-6\") segue a numeração das histórias, não a dos casos de uso. "
                   f"O texto de cada história está em [Histórias de Usuário]({link(d, 'docs/02-requisitos/historias-de-usuario.md')}).")
    grupos = []
    for pdf in pdfs:
        hus = textos_hu(f"{SEQ}/{pdf}")
        titulo = pdf[:-4].replace("UC ", "HU ")
        grupos.append((pdf, titulo, hus))
    L += ["## Sumário", "", "| Arquivo | Histórias |", "|---|---|"]
    usadas = {}
    for pdf, titulo, hus in grupos:
        L.append(f"| [{titulo}](#{ancora(titulo, usadas)}) | {'<br>'.join(hus)} |")
    L.append("")
    for pdf, titulo, hus in grupos:
        L += [f"## {titulo}", ""]
        L += [f"- {h}" for h in hus]
        L += ["", f"PDF original: [`{pdf}`]({link(d, SEQ + '/' + pdf)})", ""]
        if imagens:
            img = f"sequencia/{slug(titulo)}.png"
            L += [f"[![Diagrama de sequência {titulo}](../assets/{img})](../assets/{img})", "",
                  "_Clique na imagem para abrir em tamanho real._", ""]
    escrever(destino, L)
    return grupos


def pagina_wireframes(imagens):
    pdfs = sorted((a for a in os.listdir(os.path.join(RAIZ, WIRE)) if a.lower().endswith(".pdf")),
                  key=lambda a: (0 if a.startswith(("Fundamentos", "Mapa")) else 1, a))
    destino = "05-design/wireframes.md"
    d = "docs/" + destino
    L = ["# Wireframes", ""]
    L += cabecalho(destino, [WIRE + "/"],
                   "Os PDFs dos wireframes são grandes (até 20 MB) e o GitHub nem sempre consegue abri-los. "
                   "Aqui ficam prévias em imagem; para os detalhes, use o PDF ou o "
                   f"[Figma]({link(d, DESIGN + '/README.md')}).")
    L += ["## Sumário", ""]
    usadas = {}
    nomes = []
    for pdf in pdfs:
        t = pdf[:-4]
        nomes.append((pdf, t))
        L.append(f"- [{t}](#{ancora(t, usadas)})")
    L.append("")
    for pdf, t in nomes:
        L += [f"## {t}", "", f"PDF original: [`{pdf}`]({link(d, WIRE + '/' + pdf)})", ""]
        if imagens:
            img = f"wireframes/{slug(t)}.jpg"
            L += [f'<a href="../assets/{img}"><img src="../assets/{img}" alt="{t}" width="480"></a>', "",
                  "_Clique na imagem para abrir em tamanho real._", ""]
    escrever(destino, L)
    return nomes


def pagina_raci():
    import openpyxl

    origem = f"{GESTAO}/RACI.xlsx"
    wb = openpyxl.load_workbook(os.path.join(RAIZ, origem), data_only=True)
    destino = "01-gestao/raci.md"
    L = ["# Matriz RACI", ""] + cabecalho(destino, [origem])
    L += ["**R** = Responsável (executa) · **A** = Aprovador (presta contas) · **C** = Consultado · **I** = Informado", ""]
    for ws in wb:
        linhas = [[("" if c is None else str(c).strip()) for c in r] for r in ws.iter_rows(values_only=True)]
        linhas = [r for r in linhas if any(r)]
        if not linhas:
            continue
        if len(wb.worksheets) > 1:
            L += [f"## {ws.title}", ""]
        L.append("| " + " | ".join(linhas[0]) + " |")
        L.append("|" + "---|" * len(linhas[0]))
        for r in linhas[1:]:
            L.append("| " + " | ".join(c.replace("|", "\\|") for c in r) + " |")
        L.append("")
    escrever(destino, L)


def pagina_horas():
    destino = "06-acompanhamento/horas-por-integrante.md"
    d = "docs/" + destino
    texto = subprocess.run(["pdftotext", "-layout", os.path.join(RAIZ, HORAS), "-"],
                           capture_output=True, text=True).stdout
    L = ["# Consolidado de Horas por Integrante", ""] + cabecalho(destino, [HORAS])
    m = re.search(r"Detalhamento por Integrante(.*?)Total Geral\s+([\d,]+)\s+([\d,%]+)", texto, re.S)
    if m:
        L += ["## Resumo", "", "| Integrante | Horas rastreadas | % do total |", "|---|---:|---:|"]
        for nome, h, p in re.findall(r"^\s*([A-Za-zÀ-ÿ ]+?)\s{2,}([\d,]+)\s+([\d,]+%)", m.group(1), re.M):
            L.append(f"| {nome} | {h} h | {p} |")
        L.append(f"| **Total** | **{m.group(2)} h** | **{m.group(3)}** |")
        L.append("")
    L += [f"O detalhamento por ticket está no [PDF original]({link(d, HORAS)}), que o GitHub mostra direto no navegador.", ""]
    escrever(destino, L)


def pagina_diagramas_drawio():
    viewer = "https://viewer.diagrams.net/?nav=1&lightbox=1#U"
    casos_src, classe_src = f"{DIAG}/Caso de uso", f"{DIAG}/Diagrama_De_Classe_Atualizado.drawio"

    def cab(destino, origem):
        url = viewer + quote(REPO_RAW + quote(origem), safe="")
        nota = (f"Para ver o desenho original, com o layout do draw.io: [abrir no visualizador do draw.io]({url}) "
                "(só leitura) ou abra o arquivo no [app.diagrams.net](https://app.diagrams.net) / extensão Draw.io do VS Code.")
        if origem.endswith("Caso de uso"):
            nota += " O arquivo `Caso de uso` não tem extensão, mas é um diagrama do draw.io."
        return cabecalho(destino, [origem], nota)

    drawio2mermaid.render_casos(os.path.join(RAIZ, casos_src), os.path.join(DOCS, "03-diagramas/diagrama-de-casos-de-uso.md"),
                                cab("03-diagramas/diagrama-de-casos-de-uso.md", casos_src))
    drawio2mermaid.render_classes(os.path.join(RAIZ, classe_src), os.path.join(DOCS, "03-diagramas/diagrama-de-classes.md"),
                                  cab("03-diagramas/diagrama-de-classes.md", classe_src))


def indice(sequencias, wireframes):
    d = "docs/README.md"
    L = ["# Documentação do MindLiner", "",
         "Todo o material do projeto em páginas que abrem direto no GitHub. "
         "Os arquivos originais (.docx, .xlsx, .drawio e .pdf) continuam nas pastas de sempre; "
         "cada página aqui aponta para o seu original.", "",
         f"[⬅ Voltar ao README do projeto]({link(d, 'README.md')})", "",
         "## Sumário", "",
         "1. [Gestão e mercado](#1-gestão-e-mercado)",
         "2. [Requisitos](#2-requisitos)",
         "3. [Diagramas](#3-diagramas)",
         "4. [Arquitetura](#4-arquitetura)",
         "5. [Design e UI](#5-design-e-ui)",
         "6. [Acompanhamento](#6-acompanhamento)",
         "7. [Como atualizar estas páginas](#7-como-atualizar-estas-páginas)", ""]

    def tabela(linhas):
        out = ["| Documento | Ler no GitHub | Original |", "|---|---|---|"]
        for titulo, pagina, origem in linhas:
            orig = f"[`{os.path.basename(origem.rstrip('/')) or origem}`]({link(d, origem)})"
            out.append(f"| {titulo} | [abrir](./{pagina}) | {orig} |")
        return out + [""]

    L += ["## 1. Gestão e mercado", ""]
    L += tabela([
        ("Documento de Abertura do Projeto", "01-gestao/abertura-do-projeto.md", DOCX[0][0]),
        ("Pesquisa de Mercado e Aplicação de Ferramentas", "01-gestao/pesquisa-de-mercado.md", DOCX[1][0]),
        ("Análise de Concorrentes", "01-gestao/analise-de-concorrentes.md", DOCX[2][0]),
        ("Análise SWOT Estratégica", "01-gestao/analise-swot.md", DOCX[3][0]),
        ("INPI e Matriz GUT", "01-gestao/inpi-e-matriz-gut.md", DOCX[4][0]),
        ("Matriz RACI", "01-gestao/raci.md", f"{GESTAO}/RACI.xlsx"),
        ("LGPD e Termos", "01-gestao/lgpd-termos.md", DOCX[5][0]),
        ("Mapeamento do Código de Defesa do Consumidor", "01-gestao/codigo-de-defesa-do-consumidor.md", DOCX[6][0]),
    ])
    L += ["## 2. Requisitos", ""]
    L += tabela([
        ("Requisitos Funcionais", "02-requisitos/requisitos-funcionais.md", DOCX[7][0]),
        ("Requisitos Não Funcionais", "02-requisitos/requisitos-nao-funcionais.md", DOCX[8][0]),
        ("Regras de Negócio", "02-requisitos/regras-de-negocio.md", DOCX[9][0]),
        ("Histórias de Usuário (HU001 a HU070)", "02-requisitos/historias-de-usuario.md", DOCX[10][0]),
    ])
    L += ["## 3. Diagramas", "",
          "Os diagramas do draw.io foram convertidos para [Mermaid](https://mermaid.js.org/), que o GitHub desenha na própria página.", ""]
    L += tabela([
        ("Diagrama de Casos de Uso (por pacote)", "03-diagramas/diagrama-de-casos-de-uso.md", f"{DIAG}/Caso de uso"),
        ("Casos de Uso detalhados (UC-01 a UC-67)", "03-diagramas/casos-de-uso.md", DOCX[11][0]),
        ("Diagrama de Classes (por módulo)", "03-diagramas/diagrama-de-classes.md", f"{DIAG}/Diagrama_De_Classe_Atualizado.drawio"),
        (f"Diagramas de Sequência ({len(sequencias)} arquivos, por história de usuário)", "03-diagramas/diagramas-de-sequencia.md", SEQ + "/"),
    ])
    L += ["## 4. Arquitetura", ""]
    L += tabela([("Documentação de Arquitetura (C4 e ADRs)", "04-arquitetura/arquitetura.md", DOCX[12][0])])
    L += ["## 5. Design e UI", ""]
    L += tabela([
        ("Pesquisa de Branding", "05-design/pesquisa-de-branding.md", DOCX[13][0]),
        (f"Wireframes ({len(wireframes)} telas e fundamentos)", "05-design/wireframes.md", WIRE + "/"),
    ])
    L += [f"Protótipo no Figma: link e senha em [`Design - UI/README.md`]({link(d, DESIGN + '/README.md')}).", ""]
    L += ["## 6. Acompanhamento", ""]
    L += tabela([("Consolidado de Horas por Integrante", "06-acompanhamento/horas-por-integrante.md", HORAS)])
    L += ["## 7. Como atualizar estas páginas", "",
          "As páginas desta pasta são geradas a partir dos arquivos originais. Depois de alterar um .docx, .xlsx, .drawio ou PDF, rode na raiz do repositório:", "",
          "```bash", "python3 scripts/docs/gerar_docs.py", "```", "",
          "Precisa de `pandoc`, `pdftoppm` (pacote poppler-utils) e Python com `openpyxl` e `Pillow` "
          "(`pip install openpyxl pillow`). Use `--sem-imagens` para pular as prévias dos PDFs, que são a parte demorada.", "",
          "Não edite as páginas de `docs/` à mão: a próxima geração sobrescreve. Edite sempre o original.", ""]
    escrever("README.md", L)


def readmes_de_pasta(seqs):
    """README nas pastas originais: o GitHub mostra esse texto abaixo da lista de arquivos."""
    def pasta(p, titulo, itens):
        caminho = os.path.join(RAIZ, p, "README.md")
        if os.path.exists(caminho) and "gerar_docs.py" not in open(caminho, encoding="utf-8").read():
            return  # README escrito pela equipe: não mexe
        rel = p + "/README.md"
        L = [f"# {titulo}", "",
             "Os arquivos desta pasta não abrem direto no GitHub (.docx, .xlsx, .drawio) ou são PDFs grandes. "
             "Use as versões abaixo para ler pelo navegador:", ""]
        for nome, pagina in itens:
            L.append(f"- [{nome}]({link(rel, 'docs/' + pagina)})")
        L += ["", f"Sumário completo: [docs/README.md]({link(rel, 'docs/README.md')})", "",
              "<!-- Gerado por scripts/docs/gerar_docs.py -->"]
        with open(caminho, "w", encoding="utf-8") as f:
            f.write("\n".join(L) + "\n")

    pasta(GESTAO, "Documentação de Gestão e Mercado", [
        ("Documento de Abertura do Projeto", "01-gestao/abertura-do-projeto.md"),
        ("Pesquisa de Mercado", "01-gestao/pesquisa-de-mercado.md"),
        ("Análise de Concorrentes", "01-gestao/analise-de-concorrentes.md"),
        ("Análise SWOT", "01-gestao/analise-swot.md"),
        ("INPI e Matriz GUT", "01-gestao/inpi-e-matriz-gut.md"),
        ("Matriz RACI", "01-gestao/raci.md"),
        ("LGPD e Termos", "01-gestao/lgpd-termos.md"),
        ("Código de Defesa do Consumidor", "01-gestao/codigo-de-defesa-do-consumidor.md")])
    pasta(DIAG, "Documentos de Diagramas", [
        ("Diagrama de Casos de Uso (arquivo `Caso de uso`)", "03-diagramas/diagrama-de-casos-de-uso.md"),
        ("Casos de Uso detalhados", "03-diagramas/casos-de-uso.md"),
        ("Diagrama de Classes", "03-diagramas/diagrama-de-classes.md"),
        ("Diagramas de Sequência", "03-diagramas/diagramas-de-sequencia.md"),
        ("Requisitos Funcionais", "02-requisitos/requisitos-funcionais.md"),
        ("Requisitos Não Funcionais", "02-requisitos/requisitos-nao-funcionais.md"),
        ("Regras de Negócio", "02-requisitos/regras-de-negocio.md"),
        ("Histórias de Usuário", "02-requisitos/historias-de-usuario.md")])
    pasta(SEQ, "Diagramas de Sequência", [("Todos os diagramas com prévia e lista de histórias", "03-diagramas/diagramas-de-sequencia.md")])
    pasta(ARQ, "Documentação de Arquitetura", [("Documentação de Arquitetura", "04-arquitetura/arquitetura.md")])
    pasta(WIRE, "Wireframes", [("Prévias de todos os wireframes", "05-design/wireframes.md"),
                               ("Pesquisa de Branding", "05-design/pesquisa-de-branding.md")])


def main():
    imagens = "--sem-imagens" not in sys.argv
    for pasta in os.listdir(DOCS) if os.path.isdir(DOCS) else []:
        if pasta != "assets" or imagens:
            alvo = os.path.join(DOCS, pasta)
            shutil.rmtree(alvo) if os.path.isdir(alvo) else os.remove(alvo)
    os.makedirs(DOCS, exist_ok=True)

    for origem, destino, titulo in DOCX:
        converter_docx(origem, destino, titulo)
        print("ok", destino)
    pagina_raci()
    pagina_horas()
    pagina_diagramas_drawio()
    seqs = pagina_sequencia(imagens)
    wires = pagina_wireframes(imagens)
    indice(seqs, wires)
    readmes_de_pasta(seqs)
    print("ok páginas")

    if imagens:
        for pdf, titulo, _ in seqs:
            previa_pdf(f"{SEQ}/{pdf}", f"sequencia/{slug(titulo)}.png", 1600, "png")
            print("ok prévia", titulo)
        for pdf, t in wires:
            previa_pdf(f"{WIRE}/{pdf}", f"wireframes/{slug(t)}.jpg", 1200, "jpg")
            print("ok prévia", t)


if __name__ == "__main__":
    main()
