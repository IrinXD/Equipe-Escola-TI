# MindLiner — Equipe Escola de TI

Hub do projeto MindLiner, o app de estudos gamificado do TCC de Engenharia de Software (Unicesumar).
Aqui ficam a documentação, o design e o mapa dos repositórios de código.

> 📚 **Quer ler a documentação pelo navegador?** Comece pelo [sumário da documentação](docs/README.md): requisitos, casos de uso, diagramas, arquitetura, gestão e design em páginas que abrem direto no GitHub.

## Sumário

- [Repositórios](#repositórios)
- [Montar o ambiente](#montar-o-ambiente)
- [Rodar tudo junto](#rodar-tudo-junto)
- [Combinados da equipe](#combinados-da-equipe)
- [Design](#design)
- [Documentação](#documentação)
  - [Sumário completo da documentação](docs/README.md)
  - [Requisitos funcionais](docs/02-requisitos/requisitos-funcionais.md) · [Regras de negócio](docs/02-requisitos/regras-de-negocio.md) · [Histórias de usuário](docs/02-requisitos/historias-de-usuario.md)
  - [Diagrama de casos de uso](docs/03-diagramas/diagrama-de-casos-de-uso.md) · [Diagrama de classes](docs/03-diagramas/diagrama-de-classes.md) · [Diagramas de sequência](docs/03-diagramas/diagramas-de-sequencia.md)
  - [Arquitetura](docs/04-arquitetura/arquitetura.md) · [Wireframes](docs/05-design/wireframes.md)

## Repositórios

| Repositório | O que tem | Stack |
|---|---|---|
| **Equipe-Escola-TI** (este) | Documentação, requisitos, diagramas, wireframes e Figma | — |
| [BackEnd_ML](https://github.com/bialemesvsouza/BackEnd_ML) | API REST usada pelo web e pelo mobile | Spring Boot 3, Java 17, PostgreSQL (Supabase) |
| [FrontEnd_ML](https://github.com/bialemesvsouza/FrontEnd_ML) | Interface web | React 19, TypeScript, Vite |
| [MindLiner-Mobile](https://github.com/IrinXD/MindLiner-Mobile) | App mobile | Expo, React Native |

```
                 ┌───────────────┐
  FrontEnd_ML ──▶│               │
  (web :5173)    │  BackEnd_ML   │──▶ PostgreSQL (Supabase)
                 │  API :8080    │
  Mobile ───────▶│  /api/**      │
  (Expo :8081)   └───────────────┘
```

Os clientes só falam com a API, por JSON e token JWT. O contrato está no Swagger do backend: `http://localhost:8080/swagger-ui/index.html`.

## Montar o ambiente

Clone os quatro repositórios lado a lado, na mesma pasta:

```
Escola de TI/
├── Equipe-Escola-TI/
├── BackEnd_ML/
├── FrontEnd_ML/
└── MindLiner-Mobile/
```

Com este repositório clonado, o script baixa os outros três (ou atualiza os que já existem):

```powershell
# Windows (PowerShell)
powershell -ExecutionPolicy Bypass -File .\scripts\clonar-repos.ps1
```

```bash
# macOS / Linux
./scripts/clonar-repos.sh
```

Depois abra `MindLiner.code-workspace` no VS Code: ele mostra os quatro repositórios numa janela só, cada um com o próprio git.

## Rodar tudo junto

| Ordem | Repositório | Comando | Endereço |
|---|---|---|---|
| 1 | BackEnd_ML | `cd mindliner-backend` e `mvn spring-boot:run` (precisa do `.env` com as credenciais) | `http://localhost:8080` |
| 2 | FrontEnd_ML | `npm install` e `npm run dev` | `http://localhost:5173` |
| 3 | MindLiner-Mobile | `npm install` e `npx expo start` | Expo Go ou `http://localhost:8081` |

O front web usa um proxy do Vite para `/api`, então não depende do CORS. O backend libera `localhost:5173` e `localhost:8081` para quem chamar direto.

## Combinados da equipe

- Uma branch por card: `feature/TI-90-gerenciar-conteudos`, `fix/TI-164-erro-login`.
- Commits no padrão `tipo: descrição` (`feat`, `fix`, `docs`, `chore`, `refactor`).
- Mudança de contrato da API (endpoint, DTO, coluna nova) vai em duas PRs, uma no BackEnd_ML e outra no cliente afetado, citando uma na outra.
- Coluna nova no banco: o script SQL vai junto na PR do backend (`docs/sql/`), porque o Hibernate roda em `validate` e não cria tabela.

## Design

- Figma: [MindLiner-V2](https://www.figma.com/design/LnZBM8l8aZfuRsFkhKdAsg/MindLiner-V2?node-id=8-7) — senha em [`Design - UI/README.md`](Design%20-%20UI/README.md)
- Exportações das telas: [`Design - UI/Wireframes`](Design%20-%20UI/Wireframes) (`Fundamentos.pdf` tem cores, tipografia e espaçamentos)

## Documentação

| Pasta | Conteúdo | Ler no GitHub |
|---|---|---|
| `Documentos de Diagramas/` | Casos de uso, diagramas de sequência e de classe, histórias de usuário, requisitos e regras de negócio | [Requisitos](docs/README.md#2-requisitos) · [Diagramas](docs/README.md#3-diagramas) |
| `Documentação Arquitetura/` | Documento de arquitetura | [Arquitetura](docs/04-arquitetura/arquitetura.md) |
| `Documentação de Gestão - Mercado/` | Abertura do projeto, RACI, SWOT, concorrentes, LGPD e CDC | [Gestão e mercado](docs/README.md#1-gestão-e-mercado) |
| `Design - UI/` | Pesquisa de branding e wireframes | [Branding](docs/05-design/pesquisa-de-branding.md) · [Wireframes](docs/05-design/wireframes.md) |
| `Consolidado de Horas por Integrante - Projeto TI.pdf` | Horas rastreadas por integrante | [Horas](docs/06-acompanhamento/horas-por-integrante.md) |

Os arquivos originais (.docx, .xlsx, .drawio, .pdf) continuam sendo a fonte oficial. A pasta [`docs/`](docs/README.md) tem uma versão de cada um em Markdown, e os diagramas do draw.io viraram Mermaid, que o GitHub desenha na página. Mudou algum original? Rode `python3 scripts/docs/gerar_docs.py` para atualizar as páginas (detalhes no [fim do sumário](docs/README.md#7-como-atualizar-estas-páginas)).
