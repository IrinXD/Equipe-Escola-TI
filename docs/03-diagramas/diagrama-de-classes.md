# Diagrama de Classes

> Página gerada a partir de [`Diagrama_De_Classe_Atualizado.drawio`](../../Documentos%20de%20Diagramas/Diagrama_De_Classe_Atualizado.drawio) para leitura no GitHub. O arquivo original continua sendo a fonte oficial: edite o original e rode `python3 scripts/docs/gerar_docs.py`.
>
> Para ver o desenho original, com o layout do draw.io: [abrir no visualizador do draw.io](https://viewer.diagrams.net/?nav=1&lightbox=1#Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fbialemesvsouza%2FEquipe-Escola-TI%2Fmain%2FDocumentos%2520de%2520Diagramas%2FDiagrama_De_Classe_Atualizado.drawio) (só leitura) ou abra o arquivo no [app.diagrams.net](https://app.diagrams.net) / extensão Draw.io do VS Code.

[⬅ Voltar ao sumário](../README.md)


**51 classes** em **10 módulos** e **62 relacionamentos**.

Legenda: `*--` composição · `o--` agregação · `-->` associação · `<|--` herança. Os números são as multiplicidades.

## Sumário

- [Visão geral (classes e relacionamentos)](#visão-geral)
- [Perfil e Configurações](#perfil-e-configurações)
- [Técnicas de Estudo](#técnicas-de-estudo)
- [Estudo e Sessões](#estudo-e-sessões)
- [Planejamento](#planejamento)
- [Gamificação](#gamificação)
- [Loja e Inventário](#loja-e-inventário)
- [Compras e Pagamentos](#compras-e-pagamentos)
- [Grupos de Estudo](#grupos-de-estudo)
- [Monitoramento e Relatórios](#monitoramento-e-relatórios)
- [Inteligência Artificial](#inteligência-artificial)

## Visão geral

Todas as classes, só com os nomes, para enxergar como os módulos se ligam. Os atributos e métodos estão nas seções de cada módulo.

```mermaid
classDiagram
  direction LR
  namespace Perfil_e_Configuracoes {
    class Perfil
    class Avatar
    class ConfiguracaoAcessibilidade
    class ConfiguracaoPersonalizacao
    class ConfiguracaoNotificacao
    class Notificacao
    class ListaBloqueio
    class AppBloqueado
  }
  namespace Tecnicas_de_Estudo {
    class TecnicaEstudo
    class Pomodoro
    class Tecnica5217
    class Timeboxing
    class Flowtime
    class TecnicaPersonalizada
    class PassoTecnica
  }
  namespace Estudo_e_Sessoes {
    class Disciplina
    class ConteudoEstudo
    class SessaoEstudo
    class PausaSessao
    class EstadoSessaoLocal
    class ViolacaoFoco
    class ProgressoPasso
  }
  namespace Planejamento {
    class PlanoEstudo
    class RoteiroEstudo
    class ItemRoteiro
    class MetaEstudo
  }
  namespace Gamificacao {
    class Carteira
    class Pontuacao
    class TransacaoMoeda
    class CheckIn
    class ConquistaUsuario
    class Medalha
    class Ranking
    class InventarioItem
  }
  namespace Loja_e_Inventario {
    class ItemLoja
    class PacoteIcones
    class VersaoIcone
  }
  namespace Compras_e_Pagamentos {
    class Compra
    class Comprovante
    class EventoWebhook
  }
  namespace Grupos_de_Estudo {
    class MembroGrupo
    class GrupoEstudo
    class ConviteGrupo
  }
  namespace Monitoramento_e_Relatorios {
    class Dashboard
    class Relatorio
    class Progresso
  }
  namespace Inteligencia_Artificial {
    class AgenteIA
    class MensagemIA
    class SugestaoIA
  }
  class Usuario
  class Administrador
  Usuario "1" *-- "1" Perfil
  Usuario "1" *-- "1" PlanoEstudo
  Usuario "1" --> "0..*" Disciplina : possui
  Usuario "1" *-- "1" Carteira
  Usuario "1" --> "0..*" Compra : realiza
  Usuario "1" --> "0..*" MembroGrupo : participa
  Usuario "1" --> "1" Dashboard : acompanha
  Usuario "1" --> "1" AgenteIA : interage
  Usuario <|-- Administrador
  Administrador "1..*" --> "0..*" ItemLoja : gerencia
  Perfil "1" *-- "1" Avatar
  Perfil "1" *-- "1" ConfiguracaoAcessibilidade
  Perfil "1" *-- "1" ConfiguracaoPersonalizacao
  Perfil "1" *-- "1" ConfiguracaoNotificacao
  Perfil "1" *-- "1" ListaBloqueio
  Perfil "1" --> "0..*" TecnicaPersonalizada : biblioteca pessoal
  ConfiguracaoNotificacao "1" --> "0..*" Notificacao : gera
  ListaBloqueio "1" *-- "0..*" AppBloqueado
  TecnicaEstudo <|-- TecnicaPersonalizada
  TecnicaEstudo <|-- Pomodoro
  TecnicaEstudo <|-- Tecnica5217
  TecnicaEstudo <|-- Timeboxing
  TecnicaEstudo <|-- Flowtime
  TecnicaPersonalizada "1" *-- "0..*" PassoTecnica : roteiro
  ProgressoPasso "0..*" --> "1" PassoTecnica
  Disciplina "1" *-- "0..*" ConteudoEstudo
  Disciplina "1" --> "0..*" SessaoEstudo : tem
  SessaoEstudo "0..*" --> "0..1" ConteudoEstudo
  SessaoEstudo "0..*" --> "0..1" TecnicaEstudo : utiliza
  SessaoEstudo ..> ListaBloqueio : aplica (Modo Foco)
  SessaoEstudo "1" *-- "0..*" PausaSessao
  SessaoEstudo "1" *-- "0..1" EstadoSessaoLocal
  SessaoEstudo "1" *-- "0..*" ViolacaoFoco
  SessaoEstudo "1" *-- "0..*" ProgressoPasso
  PlanoEstudo "1" *-- "0..*" RoteiroEstudo
  PlanoEstudo "1" *-- "0..*" MetaEstudo
  RoteiroEstudo "1" *-- "1..*" ItemRoteiro
  ItemRoteiro "0..*" --> "1" Disciplina
  ItemRoteiro "0..*" --> "0..1" ConteudoEstudo
  Carteira "1" *-- "0..*" Pontuacao
  Carteira "1" *-- "0..*" TransacaoMoeda
  Carteira "1" *-- "0..*" CheckIn
  Carteira "1" *-- "0..*" ConquistaUsuario
  Carteira "1" *-- "0..*" InventarioItem
  Carteira "1" --> "0..1" Ranking : posição
  ConquistaUsuario "0..*" --> "1" Medalha
  InventarioItem "0..*" --> "1" ItemLoja
  TransacaoMoeda "0..*" --> "0..1" ItemLoja : troca por
  ItemLoja <|-- PacoteIcones
  PacoteIcones "1" *-- "1..*" VersaoIcone
  Compra "0..*" --> "1" ItemLoja
  Compra "1" *-- "0..1" Comprovante
  EventoWebhook "0..*" --> "0..1" Compra : atualiza status
  MembroGrupo "0..*" --> "1" GrupoEstudo
  GrupoEstudo "1" *-- "0..*" ConviteGrupo
  Dashboard "1" *-- "0..*" Relatorio
  Dashboard "1" *-- "0..*" Progresso
  Progresso ..> SessaoEstudo : calculado a partir de
  AgenteIA "1" *-- "0..*" MensagemIA
  AgenteIA "1" --> "0..*" SugestaoIA : gera
  SugestaoIA ..> TecnicaEstudo : recomenda
  SugestaoIA ..> MetaEstudo : sugere
```

## Perfil e Configurações

Classes do módulo: `Perfil`, `Avatar`, `ConfiguracaoAcessibilidade`, `ConfiguracaoPersonalizacao`, `ConfiguracaoNotificacao`, `Notificacao`, `ListaBloqueio`, `AppBloqueado`.

Ligações com outros módulos: `SessaoEstudo`, `TecnicaPersonalizada`, `Usuario` (aparecem sem detalhes).

```mermaid
classDiagram
  class Perfil {
    +id: int
    +gerenciarPerfil()
    +visualizarDados()
  }
  class Avatar {
    +id: int
    +imagem: String
    +acessorios: String
    +editarAvatar()
  }
  class ConfiguracaoAcessibilidade {
    +id: int
    +filtroCor: String
    +tamanhoFonte: int
    +audioDescricao: boolean
    +altoContraste: boolean
    +aplicarFiltro()
  }
  class ConfiguracaoPersonalizacao {
    +id: int
    +tema: String [claro | escuro]
    +gifFundo: String
    +pacoteIconesAtivo: int
    +aplicarTema()
    +pesquisarGif()
    +restaurarPadrao()
    +visualizarPersonalizacoes()
  }
  class ConfiguracaoNotificacao {
    +id: int
    +ativa: boolean
    +som: boolean
    +push: boolean
    +frequencia: String
    +silencioInicio: Time
    +silencioFim: Time
    +configurar()
    +ativarDesativar()
  }
  class Notificacao {
    +id: int
    +mensagem: String
    +horario: DateTime
    +tipo: String
    +entregue: boolean
    +enviar()
    +agendar()
  }
  class ListaBloqueio {
    +id: int
    +ativa: boolean
    +adicionarApp()
    +removerApp()
    +editarLista()
  }
  class AppBloqueado {
    +id: int
    +nome: String
    +identificador: String
  }
  class SessaoEstudo
  class TecnicaPersonalizada
  class Usuario
  Usuario "1" *-- "1" Perfil
  Perfil "1" *-- "1" Avatar
  Perfil "1" *-- "1" ConfiguracaoAcessibilidade
  Perfil "1" *-- "1" ConfiguracaoPersonalizacao
  Perfil "1" *-- "1" ConfiguracaoNotificacao
  Perfil "1" *-- "1" ListaBloqueio
  Perfil "1" --> "0..*" TecnicaPersonalizada : biblioteca pessoal
  ConfiguracaoNotificacao "1" --> "0..*" Notificacao : gera
  ListaBloqueio "1" *-- "0..*" AppBloqueado
  SessaoEstudo ..> ListaBloqueio : aplica (Modo Foco)
```

<details><summary>Atributos e métodos em texto</summary>

**Perfil**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ gerenciarPerfil()` |
|  | `+ visualizarDados()` |

**Avatar**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ editarAvatar()` |
| `+ imagem: String` |  |
| `+ acessorios: String` |  |

**ConfiguracaoAcessibilidade**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ aplicarFiltro()` |
| `+ filtroCor: String` |  |
| `+ tamanhoFonte: int` |  |
| `+ audioDescricao: boolean` |  |
| `+ altoContraste: boolean` |  |

**ConfiguracaoPersonalizacao**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ aplicarTema()` |
| `+ tema: String (claro | escuro)` | `+ pesquisarGif()` |
| `+ gifFundo: String` | `+ restaurarPadrao()` |
| `+ pacoteIconesAtivo: int` | `+ visualizarPersonalizacoes()` |

**ConfiguracaoNotificacao**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ configurar()` |
| `+ ativa: boolean` | `+ ativarDesativar()` |
| `+ som: boolean` |  |
| `+ push: boolean` |  |
| `+ frequencia: String` |  |
| `+ silencioInicio: Time` |  |
| `+ silencioFim: Time` |  |

**Notificacao**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ enviar()` |
| `+ mensagem: String` | `+ agendar()` |
| `+ horario: DateTime` |  |
| `+ tipo: String` |  |
| `+ entregue: boolean` |  |

**ListaBloqueio**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ adicionarApp()` |
| `+ ativa: boolean` | `+ removerApp()` |
|  | `+ editarLista()` |

**AppBloqueado**

| Atributos | Métodos |
|---|---|
| `+ id: int` |  |
| `+ nome: String` |  |
| `+ identificador: String` |  |

</details>

## Técnicas de Estudo

Classes do módulo: `TecnicaEstudo`, `Pomodoro`, `Tecnica5217`, `Timeboxing`, `Flowtime`, `TecnicaPersonalizada`, `PassoTecnica`.

Ligações com outros módulos: `Perfil`, `ProgressoPasso`, `SessaoEstudo`, `SugestaoIA` (aparecem sem detalhes).

```mermaid
classDiagram
  class TecnicaEstudo {
    +id: int
    +nome: String
    +descricao: String
    +tempoFoco: int
    +tempoDescanso: int
    +ciclos: int
    +modoFoco: boolean
    +aplicar()
    +configurarParametros()
    +controlarPeriodos()
    +notificarPeriodo()
  }
  class Pomodoro {
    +iniciarPomodoro()
  }
  class Tecnica5217 {
    +iniciar5217()
  }
  class Timeboxing {
    +periodoAtividade: int
    +definirPeriodo()
  }
  class Flowtime {
    +iniciarDescanso()
    +encerrarDescanso()
  }
  class TecnicaPersonalizada {
    +ativa: boolean
    +cadastrar()
    +editar()
    +eliminar()
    +validarNomeUnico()
  }
  class PassoTecnica {
    +id: int
    +ordem: int
    +descricao: String
  }
  class Perfil
  class ProgressoPasso
  class SessaoEstudo
  class SugestaoIA
  Perfil "1" --> "0..*" TecnicaPersonalizada : biblioteca pessoal
  TecnicaEstudo <|-- TecnicaPersonalizada
  TecnicaEstudo <|-- Pomodoro
  TecnicaEstudo <|-- Tecnica5217
  TecnicaEstudo <|-- Timeboxing
  TecnicaEstudo <|-- Flowtime
  TecnicaPersonalizada "1" *-- "0..*" PassoTecnica : roteiro
  ProgressoPasso "0..*" --> "1" PassoTecnica
  SessaoEstudo "0..*" --> "0..1" TecnicaEstudo : utiliza
  SugestaoIA ..> TecnicaEstudo : recomenda
```

<details><summary>Atributos e métodos em texto</summary>

**TecnicaEstudo**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ aplicar()` |
| `+ nome: String` | `+ configurarParametros()` |
| `+ descricao: String` | `+ controlarPeriodos()` |
| `+ tempoFoco: int` | `+ notificarPeriodo()` |
| `+ tempoDescanso: int` |  |
| `+ ciclos: int` |  |
| `+ modoFoco: boolean` |  |

**Pomodoro**

| Atributos | Métodos |
|---|---|
|  | `+ iniciarPomodoro()` |

**Tecnica5217**

| Atributos | Métodos |
|---|---|
|  | `+ iniciar5217()` |

**Timeboxing**

| Atributos | Métodos |
|---|---|
| `+ periodoAtividade: int` | `+ definirPeriodo()` |

**Flowtime**

| Atributos | Métodos |
|---|---|
|  | `+ iniciarDescanso()` |
|  | `+ encerrarDescanso()` |

**TecnicaPersonalizada**

| Atributos | Métodos |
|---|---|
| `+ ativa: boolean` | `+ cadastrar()` |
|  | `+ editar()` |
|  | `+ eliminar()` |
|  | `+ validarNomeUnico()` |

**PassoTecnica**

| Atributos | Métodos |
|---|---|
| `+ id: int` |  |
| `+ ordem: int` |  |
| `+ descricao: String` |  |

</details>

## Estudo e Sessões

Classes do módulo: `Disciplina`, `ConteudoEstudo`, `SessaoEstudo`, `PausaSessao`, `EstadoSessaoLocal`, `ViolacaoFoco`, `ProgressoPasso`.

Ligações com outros módulos: `ItemRoteiro`, `ListaBloqueio`, `PassoTecnica`, `Progresso`, `TecnicaEstudo`, `Usuario` (aparecem sem detalhes).

```mermaid
classDiagram
  class Disciplina {
    +id: int
    +nome: String
    +cor: String
    +arquivada: boolean
    +cadastrar()
    +editar()
    +arquivar()
    +alterarCor()
  }
  class ConteudoEstudo {
    +id: int
    +titulo: String
    +descricao: String
    +categoria: String
    +cadastrar()
  }
  class SessaoEstudo {
    +id: int
    +inicio: DateTime
    +fim: DateTime
    +tempoTotal: int
    +tempoEfetivo: int
    +modoControle: String [cronometro | timer]
    +duracaoDefinida: int
    +status: String
    +modoFoco: boolean
    +iniciar()
    +pausar()
    +retomar()
    +encerrar()
    +calcularDuracao()
  }
  class PausaSessao {
    +id: int
    +inicio: DateTime
    +fim: DateTime
  }
  class EstadoSessaoLocal {
    +id: int
    +tempoDecorrido: int
    +estado: String
    +ultimoSalvamento: DateTime
    +persistir()
    +detectarEncerramentoAnomalo()
    +recuperar()
    +continuar()
    +descartar()
  }
  class ViolacaoFoco {
    +id: int
    +horario: DateTime
    +appAcessado: String
    +acao: String [encerrou | retomou | timeout]
    +interceptarAbertura()
    +exibirTelaBloqueio()
  }
  class ProgressoPasso {
    +id: int
    +concluido: boolean
    +dataConclusao: DateTime
    +marcarConclusao()
  }
  class ItemRoteiro
  class ListaBloqueio
  class PassoTecnica
  class Progresso
  class TecnicaEstudo
  class Usuario
  Usuario "1" --> "0..*" Disciplina : possui
  ProgressoPasso "0..*" --> "1" PassoTecnica
  Disciplina "1" *-- "0..*" ConteudoEstudo
  Disciplina "1" --> "0..*" SessaoEstudo : tem
  SessaoEstudo "0..*" --> "0..1" ConteudoEstudo
  SessaoEstudo "0..*" --> "0..1" TecnicaEstudo : utiliza
  SessaoEstudo ..> ListaBloqueio : aplica (Modo Foco)
  SessaoEstudo "1" *-- "0..*" PausaSessao
  SessaoEstudo "1" *-- "0..1" EstadoSessaoLocal
  SessaoEstudo "1" *-- "0..*" ViolacaoFoco
  SessaoEstudo "1" *-- "0..*" ProgressoPasso
  ItemRoteiro "0..*" --> "1" Disciplina
  ItemRoteiro "0..*" --> "0..1" ConteudoEstudo
  Progresso ..> SessaoEstudo : calculado a partir de
```

<details><summary>Atributos e métodos em texto</summary>

**Disciplina**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ cadastrar()` |
| `+ nome: String` | `+ editar()` |
| `+ cor: String` | `+ arquivar()` |
| `+ arquivada: boolean` | `+ alterarCor()` |

**ConteudoEstudo**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ cadastrar()` |
| `+ titulo: String` |  |
| `+ descricao: String` |  |
| `+ categoria: String` |  |

**SessaoEstudo**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ iniciar()` |
| `+ inicio: DateTime` | `+ pausar()` |
| `+ fim: DateTime` | `+ retomar()` |
| `+ tempoTotal: int` | `+ encerrar()` |
| `+ tempoEfetivo: int` | `+ calcularDuracao()` |
| `+ modoControle: String (cronometro | timer)` |  |
| `+ duracaoDefinida: int` |  |
| `+ status: String` |  |
| `+ modoFoco: boolean` |  |

**PausaSessao**

| Atributos | Métodos |
|---|---|
| `+ id: int` |  |
| `+ inicio: DateTime` |  |
| `+ fim: DateTime` |  |

**EstadoSessaoLocal**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ persistir()` |
| `+ tempoDecorrido: int` | `+ detectarEncerramentoAnomalo()` |
| `+ estado: String` | `+ recuperar()` |
| `+ ultimoSalvamento: DateTime` | `+ continuar()` |
|  | `+ descartar()` |

**ViolacaoFoco**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ interceptarAbertura()` |
| `+ horario: DateTime` | `+ exibirTelaBloqueio()` |
| `+ appAcessado: String` |  |
| `+ acao: String (encerrou | retomou | timeout)` |  |

**ProgressoPasso**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ marcarConclusao()` |
| `+ concluido: boolean` |  |
| `+ dataConclusao: DateTime` |  |

</details>

## Planejamento

Classes do módulo: `PlanoEstudo`, `RoteiroEstudo`, `ItemRoteiro`, `MetaEstudo`.

Ligações com outros módulos: `ConteudoEstudo`, `Disciplina`, `SugestaoIA`, `Usuario` (aparecem sem detalhes).

```mermaid
classDiagram
  class PlanoEstudo {
    +id: int
  }
  class RoteiroEstudo {
    +id: int
    +titulo: String
    +objetivo: String
    +dataInicio: Date
    +arquivado: boolean
    +criarRoteiro()
    +editarRoteiro()
    +arquivar()
  }
  class ItemRoteiro {
    +id: int
    +ordem: int
  }
  class MetaEstudo {
    +id: int
    +descricao: String
    +objetivo: String
    +prazo: Date
    +concluida: boolean
    +arquivada: boolean
    +sugeridaPorIA: boolean
    +criarMeta()
    +editarMeta()
    +concluirMeta()
  }
  class ConteudoEstudo
  class Disciplina
  class SugestaoIA
  class Usuario
  Usuario "1" *-- "1" PlanoEstudo
  PlanoEstudo "1" *-- "0..*" RoteiroEstudo
  PlanoEstudo "1" *-- "0..*" MetaEstudo
  RoteiroEstudo "1" *-- "1..*" ItemRoteiro
  ItemRoteiro "0..*" --> "1" Disciplina
  ItemRoteiro "0..*" --> "0..1" ConteudoEstudo
  SugestaoIA ..> MetaEstudo : sugere
```

<details><summary>Atributos e métodos em texto</summary>

**PlanoEstudo**

| Atributos | Métodos |
|---|---|
| `+ id: int` |  |

**RoteiroEstudo**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ criarRoteiro()` |
| `+ titulo: String` | `+ editarRoteiro()` |
| `+ objetivo: String` | `+ arquivar()` |
| `+ dataInicio: Date` |  |
| `+ arquivado: boolean` |  |

**ItemRoteiro**

| Atributos | Métodos |
|---|---|
| `+ id: int` |  |
| `+ ordem: int` |  |

**MetaEstudo**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ criarMeta()` |
| `+ descricao: String` | `+ editarMeta()` |
| `+ objetivo: String` | `+ concluirMeta()` |
| `+ prazo: Date` |  |
| `+ concluida: boolean` |  |
| `+ arquivada: boolean` |  |
| `+ sugeridaPorIA: boolean` |  |

</details>

## Gamificação

Classes do módulo: `Carteira`, `Pontuacao`, `TransacaoMoeda`, `CheckIn`, `ConquistaUsuario`, `Medalha`, `Ranking`, `InventarioItem`.

Ligações com outros módulos: `ItemLoja`, `Usuario` (aparecem sem detalhes).

```mermaid
classDiagram
  class Carteira {
    +id: int
    +pontos: int
    +moedas: int
    +consultarSaldo()
    +atualizarStatus()
  }
  class Pontuacao {
    +id: int
    +valor: int
    +motivo: String
    +data: Date
    +adicionarPontos()
  }
  class TransacaoMoeda {
    +id: int
    +valor: int
    +tipo: String [ganho | gasto]
    +data: DateTime
    +processar()
  }
  class CheckIn {
    +id: int
    +data: Date
    +realizarCheckIn()
    +verificarElegibilidade()
  }
  class ConquistaUsuario {
    +id: int
    +dataConquista: Date
  }
  class Medalha {
    +id: int
    +nome: String
    +descricao: String
    +criterio: String
    +verificarCriterios()
  }
  class Ranking {
    +id: int
    +posicao: int
    +pontuacao: int
    +gerarRanking()
  }
  class InventarioItem {
    +id: int
    +dataAquisicao: DateTime
    +ativo: boolean
    +selecionar()
    +resgatar()
  }
  class ItemLoja
  class Usuario
  Usuario "1" *-- "1" Carteira
  Carteira "1" *-- "0..*" Pontuacao
  Carteira "1" *-- "0..*" TransacaoMoeda
  Carteira "1" *-- "0..*" CheckIn
  Carteira "1" *-- "0..*" ConquistaUsuario
  Carteira "1" *-- "0..*" InventarioItem
  Carteira "1" --> "0..1" Ranking : posição
  ConquistaUsuario "0..*" --> "1" Medalha
  InventarioItem "0..*" --> "1" ItemLoja
  TransacaoMoeda "0..*" --> "0..1" ItemLoja : troca por
```

<details><summary>Atributos e métodos em texto</summary>

**Carteira**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ consultarSaldo()` |
| `+ pontos: int` | `+ atualizarStatus()` |
| `+ moedas: int` |  |

**Pontuacao**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ adicionarPontos()` |
| `+ valor: int` |  |
| `+ motivo: String` |  |
| `+ data: Date` |  |

**TransacaoMoeda**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ processar()` |
| `+ valor: int` |  |
| `+ tipo: String (ganho | gasto)` |  |
| `+ data: DateTime` |  |

**CheckIn**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ realizarCheckIn()` |
| `+ data: Date` | `+ verificarElegibilidade()` |

**ConquistaUsuario**

| Atributos | Métodos |
|---|---|
| `+ id: int` |  |
| `+ dataConquista: Date` |  |

**Medalha**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ verificarCriterios()` |
| `+ nome: String` |  |
| `+ descricao: String` |  |
| `+ criterio: String` |  |

**Ranking**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ gerarRanking()` |
| `+ posicao: int` |  |
| `+ pontuacao: int` |  |

**InventarioItem**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ selecionar()` |
| `+ dataAquisicao: DateTime` | `+ resgatar()` |
| `+ ativo: boolean` |  |

</details>

## Loja e Inventário

Classes do módulo: `ItemLoja`, `PacoteIcones`, `VersaoIcone`.

Ligações com outros módulos: `Administrador`, `Compra`, `InventarioItem`, `TransacaoMoeda` (aparecem sem detalhes).

```mermaid
classDiagram
  class ItemLoja {
    +id: int
    +nome: String
    +descricao: String
    +tipo: String
    +precoMoedas: int
    +precoBRL: decimal
    +ativo: boolean
    +cadastrar()
    +editar()
    +inativar()
    +precificar()
  }
  class PacoteIcones {
    +evolutivo: boolean
  }
  class VersaoIcone {
    +id: int
    +estagio: int
    +xpMinimo: int
    +imagem: String
  }
  class Administrador
  class Compra
  class InventarioItem
  class TransacaoMoeda
  Administrador "1..*" --> "0..*" ItemLoja : gerencia
  InventarioItem "0..*" --> "1" ItemLoja
  TransacaoMoeda "0..*" --> "0..1" ItemLoja : troca por
  ItemLoja <|-- PacoteIcones
  PacoteIcones "1" *-- "1..*" VersaoIcone
  Compra "0..*" --> "1" ItemLoja
```

<details><summary>Atributos e métodos em texto</summary>

**ItemLoja**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ cadastrar()` |
| `+ nome: String` | `+ editar()` |
| `+ descricao: String` | `+ inativar()` |
| `+ tipo: String` | `+ precificar()` |
| `+ precoMoedas: int` |  |
| `+ precoBRL: decimal` |  |
| `+ ativo: boolean` |  |

**PacoteIcones**

| Atributos | Métodos |
|---|---|
| `+ evolutivo: boolean` |  |

**VersaoIcone**

| Atributos | Métodos |
|---|---|
| `+ id: int` |  |
| `+ estagio: int` |  |
| `+ xpMinimo: int` |  |
| `+ imagem: String` |  |

</details>

## Compras e Pagamentos

Classes do módulo: `Compra`, `Comprovante`, `EventoWebhook`.

Ligações com outros módulos: `ItemLoja`, `Usuario` (aparecem sem detalhes).

```mermaid
classDiagram
  class Compra {
    +id: int
    +valor: decimal
    +metodo: String [PIX | cartao]
    +status: String [pendente | aprovada | negada]
    +data: DateTime
    +idTransacaoGateway: String
    +realizarCompra()
    +validarTransacao()
    +tratarTimeout()
    +conciliarPendentes()
  }
  class Comprovante {
    +id: int
    +arquivoPDF: String
    +enviadoPorEmail: boolean
    +gerar()
    +enviarEmail()
  }
  class EventoWebhook {
    +id: int
    +payload: String
    +recebidoEm: DateTime
    +processado: boolean
    +receberNotificacao()
  }
  class ItemLoja
  class Usuario
  Usuario "1" --> "0..*" Compra : realiza
  Compra "0..*" --> "1" ItemLoja
  Compra "1" *-- "0..1" Comprovante
  EventoWebhook "0..*" --> "0..1" Compra : atualiza status
```

<details><summary>Atributos e métodos em texto</summary>

**Compra**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ realizarCompra()` |
| `+ valor: decimal` | `+ validarTransacao()` |
| `+ metodo: String (PIX | cartao)` | `+ tratarTimeout()` |
| `+ status: String (pendente | aprovada | negada)` | `+ conciliarPendentes()` |
| `+ data: DateTime` |  |
| `+ idTransacaoGateway: String` |  |

**Comprovante**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ gerar()` |
| `+ arquivoPDF: String` | `+ enviarEmail()` |
| `+ enviadoPorEmail: boolean` |  |

**EventoWebhook**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ receberNotificacao()` |
| `+ payload: String` |  |
| `+ recebidoEm: DateTime` |  |
| `+ processado: boolean` |  |

</details>

## Grupos de Estudo

Classes do módulo: `MembroGrupo`, `GrupoEstudo`, `ConviteGrupo`.

Ligações com outros módulos: `Usuario` (aparecem sem detalhes).

```mermaid
classDiagram
  class MembroGrupo {
    +id: int
    +papel: String [admin | moderador | membro]
    +dataEntrada: Date
    +entrar()
    +sair()
    +alterarPermissao()
    +remover()
  }
  class GrupoEstudo {
    +id: int
    +nome: String
    +descricao: String
    +imagemPerfil: String
    +imagemCapa: String
    +privacidade: String
    +capacidade: int
    +linkConvite: String
    +criar()
    +editar()
    +gerarLink()
    +revogarLink()
    +compartilhar()
  }
  class ConviteGrupo {
    +id: int
    +email: String
    +status: String
    +enviar()
  }
  class Usuario
  Usuario "1" --> "0..*" MembroGrupo : participa
  MembroGrupo "0..*" --> "1" GrupoEstudo
  GrupoEstudo "1" *-- "0..*" ConviteGrupo
```

<details><summary>Atributos e métodos em texto</summary>

**MembroGrupo**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ entrar()` |
| `+ papel: String (admin | moderador | membro)` | `+ sair()` |
| `+ dataEntrada: Date` | `+ alterarPermissao()` |
|  | `+ remover()` |

**GrupoEstudo**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ criar()` |
| `+ nome: String` | `+ editar()` |
| `+ descricao: String` | `+ gerarLink()` |
| `+ imagemPerfil: String` | `+ revogarLink()` |
| `+ imagemCapa: String` | `+ compartilhar()` |
| `+ privacidade: String` |  |
| `+ capacidade: int` |  |
| `+ linkConvite: String` |  |

**ConviteGrupo**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ enviar()` |
| `+ email: String` |  |
| `+ status: String` |  |

</details>

## Monitoramento e Relatórios

Classes do módulo: `Dashboard`, `Relatorio`, `Progresso`.

Ligações com outros módulos: `SessaoEstudo`, `Usuario` (aparecem sem detalhes).

```mermaid
classDiagram
  class Dashboard {
    +id: int
    +consolidarDesempenho()
    +gerarGraficos()
    +calcularIndicadores()
  }
  class Relatorio {
    +id: int
    +periodo: String
    +tempoTotal: int
    +dataGeracao: DateTime
    +gerar()
    +exportar()
  }
  class Progresso {
    +id: int
    +percentual: float
    +tempoEstudado: int
    +calcularProgresso()
  }
  class SessaoEstudo
  class Usuario
  Usuario "1" --> "1" Dashboard : acompanha
  Dashboard "1" *-- "0..*" Relatorio
  Dashboard "1" *-- "0..*" Progresso
  Progresso ..> SessaoEstudo : calculado a partir de
```

<details><summary>Atributos e métodos em texto</summary>

**Dashboard**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ consolidarDesempenho()` |
|  | `+ gerarGraficos()` |
|  | `+ calcularIndicadores()` |

**Relatorio**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ gerar()` |
| `+ periodo: String` | `+ exportar()` |
| `+ tempoTotal: int` |  |
| `+ dataGeracao: DateTime` |  |

**Progresso**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ calcularProgresso()` |
| `+ percentual: float` |  |
| `+ tempoEstudado: int` |  |

</details>

## Inteligência Artificial

Classes do módulo: `AgenteIA`, `MensagemIA`, `SugestaoIA`.

Ligações com outros módulos: `MetaEstudo`, `TecnicaEstudo`, `Usuario` (aparecem sem detalhes).

```mermaid
classDiagram
  class AgenteIA {
    +id: int
    +responderDuvida()
    +coletarInformacoes()
    +sugerirTecnica()
    +sugerirMeta()
  }
  class MensagemIA {
    +id: int
    +remetente: String
    +conteudo: String
    +data: DateTime
  }
  class SugestaoIA {
    +id: int
    +tipo: String [tecnica | meta]
    +conteudo: String
    +aplicada: boolean
    +aplicar()
  }
  class MetaEstudo
  class TecnicaEstudo
  class Usuario
  Usuario "1" --> "1" AgenteIA : interage
  AgenteIA "1" *-- "0..*" MensagemIA
  AgenteIA "1" --> "0..*" SugestaoIA : gera
  SugestaoIA ..> TecnicaEstudo : recomenda
  SugestaoIA ..> MetaEstudo : sugere
```

<details><summary>Atributos e métodos em texto</summary>

**AgenteIA**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ responderDuvida()` |
|  | `+ coletarInformacoes()` |
|  | `+ sugerirTecnica()` |
|  | `+ sugerirMeta()` |

**MensagemIA**

| Atributos | Métodos |
|---|---|
| `+ id: int` |  |
| `+ remetente: String` |  |
| `+ conteudo: String` |  |
| `+ data: DateTime` |  |

**SugestaoIA**

| Atributos | Métodos |
|---|---|
| `+ id: int` | `+ aplicar()` |
| `+ tipo: String (tecnica | meta)` |  |
| `+ conteudo: String` |  |
| `+ aplicada: boolean` |  |

</details>
