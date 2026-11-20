# Requisitos Não Funcionais

> Página gerada a partir de [`Requisitos_Nao_Funcionais_MindLine.docx`](../../Documentos%20de%20Diagramas/Requisitos_Nao_Funcionais_MindLine.docx) para leitura no GitHub. O arquivo original continua sendo a fonte oficial: edite o original e rode `python3 scripts/docs/gerar_docs.py`.

[⬅ Voltar ao sumário](../README.md)

## Sumário

- [RNF-001 — Arquitetura Backend](#rnf-001--arquitetura-backend)
- [RNF-002 — Multiplataforma](#rnf-002--multiplataforma)
- [RNF-003 — Testes automatizados](#rnf-003--testes-automatizados)
- [RNF-004 — Desempenho](#rnf-004--desempenho)
- [RNF-005 — Comunicação em tempo real](#rnf-005--comunicação-em-tempo-real)
- [RNF-006 — Transações internas](#rnf-006--transações-internas)
- [RNF-007 — Sincronização entre dispositivos](#rnf-007--sincronização-entre-dispositivos)

# **Requisitos Não Funcionais — MindLiner**

Versão: 1.1 Data: 18/06/2026

## **RNF-001 — Arquitetura Backend**

Sistema deve ser implementado usando arquitetura REST Stateless com banco de dados relacional (PostgreSQL), com estrutura preparada para integração futura com banco não relacional.

## **RNF-002 — Multiplataforma**

Sistema deve conter versão Desktop (HTML, CSS, JS) e versão Mobile (em desenvolvimento).

## **RNF-003 — Testes automatizados**

Sistema deve possuir testes automatizados nos principais fluxos do backend (cadastro e autenticação de usuário, CRUD de matérias).

## **RNF-004 — Desempenho**

Sistema deve responder às requisições em menos de 500ms em condições normais de uso.

## **RNF-005 — Comunicação em tempo real**

Sistema deve utilizar WebSocket para sincronização de dados em salas de estudo em grupo (previsto para próxima sprint).

## **RNF-006 — Transações internas**

Sistema deve implementar um sistema de pontos e recompensas internas. Integração com plataforma de pagamento externa (Mercado Pago ou similar) prevista para próxima sprint.

## **RNF-007 — Sincronização entre dispositivos**

Sistema deve permitir acesso aos dados de estudo de qualquer dispositivo através da API REST, mediante autenticação do usuário.
