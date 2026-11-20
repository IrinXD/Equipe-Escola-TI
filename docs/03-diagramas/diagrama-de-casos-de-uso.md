# Diagrama de Casos de Uso

> Página gerada a partir de [`Caso de uso`](../../Documentos%20de%20Diagramas/Caso%20de%20uso) para leitura no GitHub. O arquivo original continua sendo a fonte oficial: edite o original e rode `python3 scripts/docs/gerar_docs.py`.
>
> Para ver o desenho original, com o layout do draw.io: [abrir no visualizador do draw.io](https://viewer.diagrams.net/?nav=1&lightbox=1#Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fbialemesvsouza%2FEquipe-Escola-TI%2Fmain%2FDocumentos%2520de%2520Diagramas%2FCaso%2520de%2520uso) (só leitura) ou abra o arquivo no [app.diagrams.net](https://app.diagrams.net) / extensão Draw.io do VS Code. O arquivo `Caso de uso` não tem extensão, mas é um diagrama do draw.io.

[⬅ Voltar para Diagramas](../README.md#3-diagramas) · [Sumário geral](../README.md)


**59 casos de uso**, **4 atores** (Administrador, Administrador do Grupo, Sistema, Usuário) em **9 pacotes**.

Legenda: linha cheia = ator participa do caso de uso · tracejada `«include»` = sempre executa o outro · tracejada `«extend»` = pode executar o outro.

O detalhamento de cada caso de uso (fluxos, pré e pós-condições) está em [Casos de Uso detalhados](casos-de-uso.md).

## Sumário

- [Usuários e Autenticação](#usuários-e-autenticação)
- [Personalização](#personalização)
- [Grupo de estudo](#grupo-de-estudo)
- [Técnicas de Estudo](#técnicas-de-estudo)
- [Monitoramento e Relatórios](#monitoramento-e-relatórios)
- [Notificação e Foco](#notificação-e-foco)
- [Gamificação](#gamificação)
- [Compras, Pagamento e Backoffice](#compras-pagamento-e-backoffice)
- [Gerenciamento de Estudos e Tempo](#gerenciamento-de-estudos-e-tempo)
- [Lista completa](#lista-completa)

## Usuários e Autenticação

```mermaid
flowchart LR
  A4["👤 Usuário"]
  subgraph Usuarios_e_Autenticacao["Usuários e Autenticação"]
    U53(["Atualizar Perfil"])
    U54(["Cadastrar Usuário"])
    U55(["Excluir Conta de Usuário"])
    U56(["Realizar Login"])
    U57(["Realizar Logout"])
    U58(["Recuperar Senha"])
    U59(["Visualizar Perfil"])
  end
  A4 --- U54
  A4 --- U56
  A4 --- U57
  A4 --- U58
  A4 --- U53
  A4 --- U55
  A4 --- U59
  U56 -. "«extend»" .-> U58
  U53 -. "«extend»" .-> U59
  U55 -. "«include»" .-> U57
```

## Personalização

```mermaid
flowchart LR
  A4["👤 Usuário"]
  subgraph Personalizacao["Personalização"]
    U41(["Alternar Tema da Interface"])
    U42(["Configurar Acessibilidade Visual"])
    U43(["Personalizar Cores das Disciplinas"])
    U44(["Pesquisar GIF para Personalização"])
    U45(["Restaurar Personalização Padrão"])
    U46(["Selecionar Pacote de Ícones"])
    U47(["Visualizar Evolução dos Ícones"])
    U48(["Visualizar Personalizações Aplicadas"])
  end
  A4 --- U44
  A4 --- U48
  A4 --- U45
  A4 --- U46
  A4 --- U47
  A4 --- U42
  A4 --- U41
  A4 --- U43
```

## Grupo de estudo

```mermaid
flowchart LR
  A4["👤 Usuário"]
  A2["👤 Administrador do Grupo"]
  subgraph Grupo_de_estudo["Grupo de estudo"]
    U19(["Administrar Grupo de Estudos"])
    U20(["Compartilhar Grupo de Estudos"])
    U21(["Criar Grupo de Estudo"])
    U22(["Entrar em Grupo de Estudo"])
    U23(["Sair de Grupo de Estudo"])
    U24(["Visualizar Informações de Participante"])
    U25(["Visualizar Participantes do Grupo"])
  end
  A4 --- U22
  A4 --- U23
  A4 --- U25
  U24 -. "«extend»" .-> U25
  A2 --- U19
  A4 --- U21
  A4 --- U20
```

## Técnicas de Estudo

```mermaid
flowchart LR
  A4["👤 Usuário"]
  subgraph Tecnicas_de_Estudo["Técnicas de Estudo"]
    U49(["Configurar Parâmetros de Técnica"])
    U50(["Gerenciar Técnicas de Estudo Personalizadas"])
    U51(["Notificar Períodos da Técnica"])
    U52(["Selecionar e Executar Técnica de Estudo"])
  end
  A4 --- U52
  A4 --- U51
  A4 --- U50
  A4 --- U49
```

## Monitoramento e Relatórios

```mermaid
flowchart LR
  A4["👤 Usuário"]
  subgraph Monitoramento_e_Relatorios["Monitoramento e Relatórios"]
    U26(["Exportar Relatório"])
    U27(["Gerar Relatório"])
    U28(["Solicitar Sugestão de Meta"])
    U29(["Solicitar Sugestão de Técnica de Estudo"])
    U30(["Utilizar Agente de Inteligência Artificial"])
    U31(["Visualizar Dashboard"])
    U32(["Visualizar Gráficos de Desempenho"])
    U33(["Visualizar Indicadores de Desempenho"])
  end
  A4 --- U31
  U26 -. "«extend»" .-> U27
  U29 -. "«extend»" .-> U30
  U28 -. "«extend»" .-> U30
  A4 --- U32
  A4 --- U33
  A4 --- U27
  A4 --- U30
```

## Notificação e Foco

```mermaid
flowchart LR
  A4["👤 Usuário"]
  A3["👤 Sistema"]
  subgraph Notificacao_e_Foco["Notificação e Foco"]
    U34(["Ativar ou Desativar Notificações"])
    U35(["Cadastrar Aplicativo para Bloqueio"])
    U36(["Configurar Notificações"])
    U37(["Editar Aplicativos Bloqueados"])
    U38(["Executar Bloqueio de Aplicativos"])
    U39(["Monitorar Violação do Modo Foco"])
    U40(["Receber Notificação"])
  end
  A4 --- U35
  A4 --- U36
  A4 --- U37
  A4 --- U34
  A3 --- U40
  A3 --- U39
  U38 -. "«extend»" .-> U39
```

## Gamificação

```mermaid
flowchart LR
  A4["👤 Usuário"]
  A3["👤 Sistema"]
  subgraph Gamificacao["Gamificação"]
    U5(["Consultar Pontuação"])
    U6(["Realizar Check-in"])
    U7(["Receber Medalha ou Conquista"])
    U8(["Receber Moedas Virtuais"])
    U9(["Receber Pontos"])
    U10(["Trocar Moedas por Recompensa"])
    U11(["Visualizar Ranking"])
  end
  A4 --- U5
  A4 --- U11
  A4 --- U6
  U6 -. "«include»" .-> U8
  A4 --- U10
  A3 --- U7
  U5 -. "«include»" .-> U9
```

## Compras, Pagamento e Backoffice

```mermaid
flowchart LR
  A4["👤 Usuário"]
  A1["👤 Administrador"]
  subgraph Compras_Pagamento_e_Backoffice["Compras, Pagamento e Backoffice"]
    U1(["Consultar Histórico de Compras"])
    U2(["Emitir Comprovante de Compra"])
    U3(["Gerenciar Itens da Loja"])
    U4(["Realizar Compra"])
  end
  A4 --- U4
  A4 --- U1
  U4 -. "«include»" .-> U2
  A1 --- U3
```

## Gerenciamento de Estudos e Tempo

```mermaid
flowchart LR
  A4["👤 Usuário"]
  subgraph Gerenciamento_de_Estudos_e_Tempo["Gerenciamento de Estudos e Tempo"]
    U12(["Cadastrar Disciplina"])
    U13(["Editar Disciplina"])
    U14(["Encerrar Sessão de Estudo"])
    U15(["Pausar Sessão de Estudo"])
    U16(["Registrar Sessão de Estudo"])
    U17(["Utilizar Cronometro"])
    U18(["Utilizar Timer"])
  end
  A4 --- U18
  A4 --- U13
  A4 --- U12
  A4 --- U17
  A4 --- U16
  U16 -. "«extend»" .-> U15
  U16 -. "«include»" .-> U14
```

## Lista completa

| Pacote | Caso de uso | Atores | Relações |
|---|---|---|---|
| Usuários e Autenticação | Cadastrar Usuário | Usuário | — |
| Usuários e Autenticação | Realizar Login | Usuário | «extend» Recuperar Senha |
| Usuários e Autenticação | Realizar Logout | Usuário | — |
| Usuários e Autenticação | Recuperar Senha | Usuário | — |
| Usuários e Autenticação | Atualizar Perfil | Usuário | «extend» Visualizar Perfil |
| Usuários e Autenticação | Visualizar Perfil | Usuário | — |
| Usuários e Autenticação | Excluir Conta de Usuário | Usuário | «include» Realizar Logout |
| Personalização | Visualizar Evolução dos Ícones | Usuário | — |
| Personalização | Restaurar Personalização Padrão | Usuário | — |
| Personalização | Pesquisar GIF para Personalização | Usuário | — |
| Personalização | Visualizar Personalizações Aplicadas | Usuário | — |
| Personalização | Selecionar Pacote de Ícones | Usuário | — |
| Personalização | Personalizar Cores das Disciplinas | Usuário | — |
| Personalização | Alternar Tema da Interface | Usuário | — |
| Personalização | Configurar Acessibilidade Visual | Usuário | — |
| Grupo de estudo | Criar Grupo de Estudo | Usuário | — |
| Grupo de estudo | Entrar em Grupo de Estudo | Usuário | — |
| Grupo de estudo | Sair de Grupo de Estudo | Usuário | — |
| Grupo de estudo | Compartilhar Grupo de Estudos | Usuário | — |
| Grupo de estudo | Administrar Grupo de Estudos | Administrador do Grupo | — |
| Grupo de estudo | Visualizar Informações de Participante | — | «extend» Visualizar Participantes do Grupo |
| Grupo de estudo | Visualizar Participantes do Grupo | Usuário | — |
| Técnicas de Estudo | Selecionar e Executar Técnica de Estudo | Usuário | — |
| Técnicas de Estudo | Configurar Parâmetros de Técnica | Usuário | — |
| Técnicas de Estudo | Notificar Períodos da Técnica | Usuário | — |
| Técnicas de Estudo | Gerenciar Técnicas de Estudo Personalizadas | Usuário | — |
| Monitoramento e Relatórios | Visualizar Dashboard | Usuário | — |
| Monitoramento e Relatórios | Visualizar Gráficos de Desempenho | Usuário | — |
| Monitoramento e Relatórios | Visualizar Indicadores de Desempenho | Usuário | — |
| Monitoramento e Relatórios | Gerar Relatório | Usuário | — |
| Monitoramento e Relatórios | Exportar Relatório | — | «extend» Gerar Relatório |
| Monitoramento e Relatórios | Utilizar Agente de Inteligência Artificial | Usuário | — |
| Monitoramento e Relatórios | Solicitar Sugestão de Técnica de Estudo | — | «extend» Utilizar Agente de Inteligência Artificial |
| Monitoramento e Relatórios | Solicitar Sugestão de Meta | — | «extend» Utilizar Agente de Inteligência Artificial |
| Notificação e Foco | Configurar Notificações | Usuário | — |
| Notificação e Foco | Ativar ou Desativar Notificações | Usuário | — |
| Notificação e Foco | Receber Notificação | Sistema | — |
| Notificação e Foco | Monitorar Violação do Modo Foco | Sistema | — |
| Notificação e Foco | Executar Bloqueio de Aplicativos | — | «extend» Monitorar Violação do Modo Foco |
| Notificação e Foco | Editar Aplicativos Bloqueados | Usuário | — |
| Notificação e Foco | Cadastrar Aplicativo para Bloqueio | Usuário | — |
| Gamificação | Receber Pontos | — | — |
| Gamificação | Receber Moedas Virtuais | — | — |
| Gamificação | Receber Medalha ou Conquista | Sistema | — |
| Gamificação | Consultar Pontuação | Usuário | «include» Receber Pontos |
| Gamificação | Realizar Check-in | Usuário | «include» Receber Moedas Virtuais |
| Gamificação | Visualizar Ranking | Usuário | — |
| Gamificação | Trocar Moedas por Recompensa | Usuário | — |
| Compras, Pagamento e Backoffice | Realizar Compra | Usuário | «include» Emitir Comprovante de Compra |
| Compras, Pagamento e Backoffice | Consultar Histórico de Compras | Usuário | — |
| Compras, Pagamento e Backoffice | Emitir Comprovante de Compra | — | — |
| Compras, Pagamento e Backoffice | Gerenciar Itens da Loja | Administrador | — |
| Gerenciamento de Estudos e Tempo | Cadastrar Disciplina | Usuário | — |
| Gerenciamento de Estudos e Tempo | Editar Disciplina | Usuário | — |
| Gerenciamento de Estudos e Tempo | Registrar Sessão de Estudo | Usuário | «extend» Pausar Sessão de Estudo<br>«include» Encerrar Sessão de Estudo |
| Gerenciamento de Estudos e Tempo | Pausar Sessão de Estudo | — | — |
| Gerenciamento de Estudos e Tempo | Encerrar Sessão de Estudo | — | — |
| Gerenciamento de Estudos e Tempo | Utilizar Cronometro | Usuário | — |
| Gerenciamento de Estudos e Tempo | Utilizar Timer | Usuário | — |

---

[⬅ Voltar para Diagramas](../README.md#3-diagramas) · [Sumário geral](../README.md) · [↑ Topo da página](#)
