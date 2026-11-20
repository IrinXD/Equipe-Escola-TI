# Matriz RACI

> Página gerada a partir de [`RACI.xlsx`](../../Documenta%C3%A7%C3%A3o%20de%20Gest%C3%A3o%20-%20Mercado/RACI.xlsx) para leitura no GitHub. O arquivo original continua sendo a fonte oficial: edite o original e rode `python3 scripts/docs/gerar_docs.py`.

[⬅ Voltar ao sumário](../README.md)

**R** = Responsável (executa) · **A** = Aprovador (presta contas) · **C** = Consultado · **I** = Informado

| Tarefa / Etapa | PO | Scrum Master | Designer | Dev BackEnd | Dev FrontEnd | Usuários |
|---|---|---|---|---|---|---|
| 1. Definir Casos de Uso e Backlog (Ex: UC-01 a UC-71) | R/A | I | I | C | C | C |
| 2. Definir Arquitetura e Decisões Técnicas (ADRs) | A | I | I | R | R | I |
| 3. Desenhar Telas (App e Web) e Identidade Visual | A | I | R | I | C | C |
| 4. Desenvolver a API Backend (PostgreSQL + Java) | A | I | I | R | C | I |
| 5. Desenvolver Aplicação Mobile (React Native) | A | I | C | C | R | I |
| 6. Desenvolver Módulos Nativos (Modo Foco/Bloqueio) | A | I | I | R | R | I |
| 7. Integrar Gamificação e Pagamentos (UC-31 a UC-37, UC-68) | A | I | I | R | R | I |
| 8. Realizar Testes de Funcionalidade (Review) | A | C | C | C | C | R |
| 9. Implantar e Disponibilizar (Deploy) | A | C | I | R | R | I |
