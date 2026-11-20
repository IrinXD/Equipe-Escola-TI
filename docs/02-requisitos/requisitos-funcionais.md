# Requisitos Funcionais

> Página gerada a partir de [`Requisitos Funcionais_.docx`](../../Documentos%20de%20Diagramas/Requisitos%20Funcionais_.docx) para leitura no GitHub. O arquivo original continua sendo a fonte oficial: edite o original e rode `python3 scripts/docs/gerar_docs.py`.

[⬅ Voltar para Requisitos](../README.md#2-requisitos) · [Sumário geral](../README.md)

## Sumário

- [Requisitos Funcionais](#requisitos-funcionais)
- [Usuários e Autenticação](#usuários-e-autenticação)
- [Gerenciamento de Estudos](#gerenciamento-de-estudos)
- [Controle de Tempo](#controle-de-tempo)
- [Técnicas de Estudo](#técnicas-de-estudo)
- [Gamificação](#gamificação)
- [Grupos de Estudo](#grupos-de-estudo)
- [Monitoramento e Relatórios](#monitoramento-e-relatórios)
- [Inteligência Artificial](#inteligência-artificial)
- [Notificações](#notificações)
- [Foco e Controle de Distrações](#foco-e-controle-de-distrações)
- [Personalização e Acessibilidade](#personalização-e-acessibilidade)
- [Compras e Pagamentos](#compras-e-pagamentos)
- [Administrador" e Backoffice](#administrador-e-backoffice)

## Requisitos Funcionais

## Usuários e Autenticação

RF-001: O sistema deve permitir o cadastro de usuários.

RF-002: O sistema deve permitir a autenticação de usuários cadastrados.

RF-003: O sistema deve permitir a recuperação de senha.

RF-004: O sistema deve permitir a edição dos dados cadastrais do usuário.

RF-005: O sistema deve permitir a visualização dos dados do perfil do usuário.

**RF-082:** O sistema deve permitir que o usuário encerre sua sessão ativa de forma segura.

**RF-083:** O sistema deve permitir que o usuário solicite a exclusão permanente de sua conta e de todos os seus dados pessoais associados.

**RF-084:** O sistema deve permitir o arquivamento de disciplinas, roteiros e metas, inativando-os para uso futuro sem deletar o histórico passado.

## Gerenciamento de Estudos

RF-006: O sistema deve permitir o cadastro de disciplinas.

RF-007: O sistema deve permitir a edição de disciplinas cadastradas.

RF-008: O sistema deve permitir o cadastro de conteúdos de estudo.

RF-009: O sistema deve permitir a categorização de conteúdos de estudo.

RF-010: O sistema deve permitir a criação de roteiros de estudo.

RF-011: O sistema deve permitir a edição de roteiros de estudo.

RF-012: O sistema deve permitir a criação de metas de estudo.

RF-013: O sistema deve permitir a edição de metas de estudo.

RF-014: O sistema deve permitir o registro de sessões de estudo.

RF-015: O sistema deve permitir a consulta do histórico de estudos.

RF-016: O sistema deve permitir a visualização do progresso dos estudos.

## Controle de Tempo

RF-017: O sistema deve disponibilizar um cronômetro para contabilização do tempo de estudo.

RF-018: O sistema deve disponibilizar um timer para sessões de estudo com duração definida.

RF-019: O sistema deve permitir iniciar uma sessão de estudo.

RF-020: O sistema deve permitir pausar uma sessão de estudo.

RF-021: O sistema deve permitir encerrar uma sessão de estudo.

**RF-085:** O sistema deve realizar a persistência periódica local do tempo decorrido e estado da sessão de estudo em intervalos regulares (ex.: a cada 30 segundos).

**RF-086:** O sistema deve detetar sessões de estudo que sofreram encerramento anómalo ao reabrir a aplicação e disponibilizar opções de recuperação ou salvamento do progresso parcial.

## Técnicas de Estudo

Funcionalidades gerais das técnicas:

RF-022: O sistema deve disponibilizar diferentes técnicas de estudo.

RF-023: O sistema deve permitir ao usuário selecionar uma técnica de estudo antes de iniciar uma sessão.

RF-024: O sistema deve registrar a técnica de estudo utilizada em cada sessão.

RF-025: O sistema deve contabilizar o tempo efetivamente destinado ao estudo durante a utilização de uma técnica.

RF-026: O sistema deve registrar o tempo efetivamente estudado em sessões interrompidas.

RF-027: O sistema deve permitir a configuração dos parâmetros das técnicas que possuam duração ou intervalos personalizáveis.

RF-028: O sistema deve notificar o usuário sobre o início e o término dos períodos de estudo e descanso das técnicas aplicáveis.

Técnicas específicas:

RF-029: O sistema deve permitir a utilização da técnica Pomodoro.

RF-030: O sistema deve permitir a utilização da técnica 52/17.

RF-031: O sistema deve permitir a utilização da técnica Timeboxing.

RF-032: O sistema deve permitir a utilização da técnica Flowtime.

RF-033: O sistema deve controlar automaticamente os períodos de estudo e descanso da técnica Pomodoro.

RF-034: O sistema deve controlar automaticamente os períodos de estudo e descanso da técnica 52/17.

RF-035: O sistema deve permitir ao usuário definir o período destinado à atividade na técnica Timeboxing.

RF-036: O sistema deve permitir que o usuário determine o momento de iniciar e encerrar os períodos de descanso na técnica Flowtime.

RF-037: O sistema deve registrar o progresso obtido durante a utilização das técnicas de estudo.  
  
**RF-087:** O sistema deve permitir o cadastro de técnicas de estudo personalizadas com parametrização de nome, descrição, cronómetro/ciclos, roteiro de passos e modo foco.

**RF-088:** O sistema deve permitir a edição de técnicas de estudo personalizadas criadas pelo próprio utilizador.

**RF-089:** O sistema deve permitir a eliminação de técnicas de estudo personalizadas criadas pelo utilizador.

**RF-90:** O sistema deve exibir o roteiro de passos configurado e permitir a marcação de conclusão de cada etapa durante uma sessão de estudo

## Gamificação

RF-038: O sistema deve atribuir pontos ao usuário conforme as ações válidas realizadas.

RF-039: O sistema deve atribuir moedas virtuais ao usuário conforme as ações válidas realizadas.

RF-040: O sistema deve permitir a visualização do saldo de pontos e moedas virtuais.

RF-041: O sistema deve permitir a realização de check-ins.

RF-042: O sistema deve conceder medalhas e conquistas quando os critérios definidos forem atingidos.

RF-043: O sistema deve permitir a visualização do ranking de usuários.

RF-044: O sistema deve permitir a troca de moedas virtuais por recompensas internas.

## Grupos de Estudo

RF-045: O sistema deve permitir a criação de grupos de estudo.

RF-046: O sistema deve permitir o ingresso de usuários em grupos de estudo.

RF-047: O sistema deve permitir que usuários saiam de grupos de estudo.

RF-048: O sistema deve permitir a visualização dos participantes dos grupos de estudo.

RF-049: O sistema deve permitir a visualização das informações dos participantes dos grupos de estudo.

**RF-091:** O sistema deve permitir a criação e edição de grupos de estudo com parametrização de nome, descrição, imagem de perfil/avatar e imagem de capa.

**RF-092:** O sistema deve permitir a definição de níveis de privacidade para grupos de estudo (Público, Privado ou Somente Amigos).

**RF-093:** O sistema deve permitir ao administrador do grupo gerenciar as permissões dos membros e remover participantes do grupo.

**RF-094:** O sistema deve permitir o compartilhamento do grupo de estudos por meio de envio de convites diretos por e-mail e geração de links copiáveis.

## Monitoramento e Relatórios

RF-051: O sistema deve disponibilizar um dashboard para acompanhamento do desempenho dos estudos.

RF-052: O sistema deve apresentar gráficos relacionados ao desempenho dos estudos.

RF-053: O sistema deve apresentar indicadores relacionados ao desempenho dos estudos.

RF-054: O sistema deve permitir a geração de relatórios de desempenho.

RF-055: O sistema deve permitir a exportação de relatórios de desempenho.

## Inteligência Artificial

RF-056: O sistema deve disponibilizar um agente de inteligência artificial para auxiliar o usuário nos estudos.

RF-057: O agente de inteligência artificial deve coletar informações fornecidas pelo usuário.

RF-058: O agente de inteligência artificial deve utilizar o histórico de estudos para personalizar suas recomendações.

RF-059: O agente de inteligência artificial deve sugerir técnicas de estudo de acordo com o perfil e os objetivos do usuário.

RF-060: O agente de inteligência artificial deve sugerir metas de estudo de acordo com as informações fornecidas pelo usuário.

## Notificações

RF-061: O sistema deve permitir a configuração das preferências de notificações.

RF-062: O sistema deve permitir ao usuário ativar ou desativar as notificações.

RF-063: O sistema deve enviar notificações de acordo com as preferências configuradas pelo usuário.

## Foco e Controle de Distrações

RF-064: O sistema deve permitir o cadastro de aplicativos para bloqueio.

RF-065: O sistema deve permitir a edição da lista de aplicativos bloqueados.

**RF-095:** O sistema deve detectar a abertura de aplicativos restritos durante uma sessão de estudo ativa com o Modo Foco ativado.

**RF-096:** O sistema deve exibir uma tela de bloqueio e confirmação ao identificar o acesso a um aplicativo restrito, permitindo ao usuário escolher entre encerrar ou retomar a sessão.

## Personalização e Acessibilidade

RF-067: O sistema deve permitir a aplicação de filtros de acessibilidade visual.

RF-068: O sistema deve permitir a alternância entre os modos claro e escuro.

RF-069: O sistema deve permitir a personalização das cores das disciplinas.

RF-070: O sistema deve permitir a seleção de pacotes de ícones.

RF-071: O sistema deve apresentar diferentes versões visuais dos pacotes de ícones de acordo com a evolução do usuário.

RF-072: O sistema deve permitir restaurar as configurações de personalização visual padrão.

RF-073: O sistema deve permitir pesquisar GIFs para personalização visual.

RF-074: O sistema deve permitir a visualização das personalizações aplicadas pelo usuário.

## Compras e Pagamentos

RF-075: O sistema deve permitir a aquisição de conteúdos ou recursos pagos.

RF-076: O sistema deve permitir o pagamento de compras por PIX.

RF-077: O sistema deve permitir o pagamento de compras por cartão.

RF-078: O sistema deve validar o resultado da transação junto ao meio de pagamento.

RF-079: O sistema deve disponibilizar o comprovante das compras realizadas.

RF-080: O sistema deve enviar o comprovante da compra para o e-mail cadastrado do usuário.

RF-081: O sistema deve permitir a consulta do histórico de compras realizadas pelo usuário.

**RF-097:** O sistema deve tratar prazos estourados (*timeout*) de comunicação com serviços de pagamento, mantendo a transação em estado pendente até conciliação.

**RF-098:** O sistema deve disponibilizar um endpoint seguro para recebimento de notificações assíncronas (*webhooks*) dos gateways de pagamento para atualização de status de transações.

**RF-099:** O sistema deve verificar compras pendentes ao iniciar a aplicação e atualizar o inventário do usuário caso o pagamento tenha sido confirmado off-line.

## Administrador" e Backoffice 

**RF-100:** O sistema deve possuir um módulo administrativo (backoffice) restrito a usuários com perfil de Administrador.

**RF-101:** O sistema deve permitir ao administrador cadastrar, editar, inativar e precificar os itens oferecidos na loja (recompensas, avatares, temas, pacotes).

---

[⬅ Voltar para Requisitos](../README.md#2-requisitos) · [Sumário geral](../README.md) · [↑ Topo da página](#)
