# Casos de Uso (detalhados)

> Página gerada a partir de [`Casos de Uso (Atualizados).docx`](../../Documentos%20de%20Diagramas/Casos%20de%20Uso%20%28Atualizados%29.docx) para leitura no GitHub. O arquivo original continua sendo a fonte oficial: edite o original e rode `python3 scripts/docs/gerar_docs.py`.

[⬅ Voltar ao sumário](../README.md)

## Sumário

- [Usuários e Autenticação](#usuários-e-autenticação)
  - [UC-01: Cadastrar Usuário](#uc-01-cadastrar-usuário)
  - [UC-02: Realizar Login](#uc-02-realizar-login)
  - [UC-03: Realizar Logout](#uc-03-realizar-logout)
  - [UC-04: Recuperar Senha](#uc-04-recuperar-senha)
  - [UC-05: Atualizar Perfil](#uc-05-atualizar-perfil)
  - [UC-06: Visualizar Perfil](#uc-06-visualizar-perfil)
  - [UC-07: Excluir Conta de Usuário](#uc-07-excluir-conta-de-usuário)
- [Gerenciamento de Estudos](#gerenciamento-de-estudos)
  - [UC-08: Cadastrar Disciplina](#uc-08-cadastrar-disciplina)
  - [UC-09: Editar Disciplina](#uc-09-editar-disciplina)
  - [UC-10: Cadastrar Conteúdo de Estudo](#uc-10-cadastrar-conteúdo-de-estudo)
  - [UC-11: Criar Roteiro de Estudos](#uc-11-criar-roteiro-de-estudos)
  - [UC-12: Editar Roteiro de Estudos](#uc-12-editar-roteiro-de-estudos)
  - [UC-13: Criar Meta de Estudo](#uc-13-criar-meta-de-estudo)
  - [UC-14: Editar Meta de Estudo](#uc-14-editar-meta-de-estudo)
  - [UC-15: Registrar Sessão de Estudo](#uc-15-registrar-sessão-de-estudo)
  - [UC-16: Consultar Histórico de Estudos](#uc-16-consultar-histórico-de-estudos)
  - [UC-17: Visualizar Progresso dos Estudos](#uc-17-visualizar-progresso-dos-estudos)
  - [UC-18: Utilizar Cronômetro (Controle de Tempo)](#uc-18-utilizar-cronômetro-controle-de-tempo)
  - [UC-19: Utilizar Timer](#uc-19-utilizar-timer)
  - [UC-20: Pausar Sessão de Estudo](#uc-20-pausar-sessão-de-estudo)
  - [UC-21: Encerrar Sessão de Estudo](#uc-21-encerrar-sessão-de-estudo)
- [Técnicas de Estudo](#técnicas-de-estudo)
  - [UC-23: Selecionar e Executar Técnica de Estudo](#uc-23-selecionar-e-executar-técnica-de-estudo)
  - [UC-24: Configurar Parâmetros de Técnica](#uc-24-configurar-parâmetros-de-técnica)
  - [UC-25: Notificar Períodos da Técnica](#uc-25-notificar-períodos-da-técnica)
  - [UC-26: Gerenciar Técnicas de Estudo Personalizadas](#uc-26-gerenciar-técnicas-de-estudo-personalizadas)
- [Gamificação](#gamificação)
  - [UC-27: Receber Pontos](#uc-27-receber-pontos)
  - [UC-28: Receber Moedas Virtuais](#uc-28-receber-moedas-virtuais)
  - [UC-29: Consultar Pontuação](#uc-29-consultar-pontuação)
  - [UC-30: Realizar Check-in](#uc-30-realizar-check-in)
  - [UC-31: Receber Medalha ou Conquista](#uc-31-receber-medalha-ou-conquista)
  - [UC-32: Visualizar Ranking](#uc-32-visualizar-ranking)
  - [UC-33: Trocar Moedas por Recompensa](#uc-33-trocar-moedas-por-recompensa)
- [Grupos de Estudo](#grupos-de-estudo)
  - [UC-34: Criar Grupo de Estudo](#uc-34-criar-grupo-de-estudo)
  - [UC-35: Entrar em Grupo de Estudo](#uc-35-entrar-em-grupo-de-estudo)
  - [UC-36: Sair de Grupo de Estudo](#uc-36-sair-de-grupo-de-estudo)
  - [UC-37: Visualizar Participantes do Grupo](#uc-37-visualizar-participantes-do-grupo)
  - [UC-38: Visualizar Informações de Participante](#uc-38-visualizar-informações-de-participante)
  - [UC-39: Administrar Grupo de Estudos](#uc-39-administrar-grupo-de-estudos)
  - [UC-40: Compartilhar Grupo de Estudos](#uc-40-compartilhar-grupo-de-estudos)
- [Monitoramento e Relatórios](#monitoramento-e-relatórios)
  - [UC-41: Visualizar Dashboard](#uc-41-visualizar-dashboard)
  - [UC-42: Visualizar Gráficos de Desempenho](#uc-42-visualizar-gráficos-de-desempenho)
  - [UC-43: Visualizar Indicadores de Desempenho](#uc-43-visualizar-indicadores-de-desempenho)
  - [UC-44: Gerar Relatório](#uc-44-gerar-relatório)
  - [UC-45: Exportar Relatório](#uc-45-exportar-relatório)
- [Inteligência Artificial](#inteligência-artificial)
  - [UC-46: Utilizar Agente de Inteligência Artificial](#uc-46-utilizar-agente-de-inteligência-artificial)
  - [UC-47: Solicitar Sugestão de Técnica de Estudo](#uc-47-solicitar-sugestão-de-técnica-de-estudo)
  - [UC-48: Solicitar Sugestão de Meta](#uc-48-solicitar-sugestão-de-meta)
- [Notificações](#notificações)
  - [UC-49: Configurar Notificações](#uc-49-configurar-notificações)
  - [UC-50: Ativar ou Desativar Notificações](#uc-50-ativar-ou-desativar-notificações)
  - [UC-51: Receber Notificação](#uc-51-receber-notificação)
- [Foco e Controle de Distrações](#foco-e-controle-de-distrações)
  - [UC-52: Cadastrar Aplicativo para Bloqueio](#uc-52-cadastrar-aplicativo-para-bloqueio)
  - [UC-53: Editar Aplicativos Bloqueados](#uc-53-editar-aplicativos-bloqueados)
  - [UC-54: Executar Bloqueio de Aplicativos](#uc-54-executar-bloqueio-de-aplicativos)
  - [UC-55: Monitorar Violação do Modo Foco](#uc-55-monitorar-violação-do-modo-foco)
- [Personalização e Acessibilidade](#personalização-e-acessibilidade)
  - [UC-56: Configurar Acessibilidade Visual](#uc-56-configurar-acessibilidade-visual)
  - [UC-57: Alternar Tema da Interface](#uc-57-alternar-tema-da-interface)
  - [UC-58: Personalizar Cores das Disciplinas](#uc-58-personalizar-cores-das-disciplinas)
  - [UC-59: Selecionar Pacote de Ícones](#uc-59-selecionar-pacote-de-ícones)
  - [UC-60: Visualizar Evolução dos Ícones](#uc-60-visualizar-evolução-dos-ícones)
  - [UC-61: Restaurar Personalização Padrão](#uc-61-restaurar-personalização-padrão)
  - [UC-62: Pesquisar GIF para Personalização](#uc-62-pesquisar-gif-para-personalização)
  - [UC-63: Visualizar Personalizações Aplicadas](#uc-63-visualizar-personalizações-aplicadas)
- [Compras e Pagamentos](#compras-e-pagamentos)
  - [UC-64: Realizar Compra](#uc-64-realizar-compra)
  - [UC-65: Emitir Comprovante de Compra](#uc-65-emitir-comprovante-de-compra)
  - [UC-66: Consultar Histórico de Compras](#uc-66-consultar-histórico-de-compras)
- [Administrador e Backoffice](#administrador-e-backoffice)
  - [UC-67: Gerenciar Itens da Loja (Backoffice)](#uc-67-gerenciar-itens-da-loja-backoffice)

## Usuários e Autenticação

### UC-01: Cadastrar Usuário

**Objetivo:** Permitir o cadastro de novos usuários no sistema.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-001.

**Pré-condições:** Nenhuma.

**Regras de Negócio:** RB-001, RB-002, RB-005.

**Fluxo Principal:**

1.  Usuário acessa a tela de cadastro.

2.  Sistema solicita nome, e-mail e senha.

3.  Usuário informa os dados.

4.  Sistema valida as informações.

5.  Sistema verifica se o e-mail já está cadastrado.

6.  Sistema cria a conta.

7.  Sistema confirma o cadastro.

**Fluxos Alternativos:**

- **FA-01: E-mail já cadastrado** - Sistema identifica que o e-mail já está em uso, informa o usuário, usuário informa outro e-mail, sistema retorna ao passo 4.

- **FA-02: Senha inválida** - Sistema identifica que a senha não atende aos critérios, apresenta os critérios, usuário informa nova senha, sistema retorna ao passo 4.

**Pós-condições:** Usuário cadastrado.

### UC-02: Realizar Login

**Objetivo:** Permitir que usuários cadastrados acessem o sistema.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-002.

**Pré-condições:** Usuário cadastrado.

**Regras de Negócio:** RB-003.

**Fluxo Principal:**

1.  Usuário acessa a tela de login.

2.  Informa e-mail e senha.

3.  Sistema valida as credenciais.

4.  Sistema autentica o usuário.

5.  Sistema direciona o usuário para a página inicial.

**Fluxos Alternativos:**

- **FA-01: Credenciais inválidas** - Sistema identifica dados incorretos, informa que as credenciais são inválidas, usuário realiza nova tentativa.

**Pós-condições:** Usuário autenticado.

### UC-03: Realizar Logout

**Objetivo:** Encerrar a sessão ativa do usuário no aplicativo, garantindo a segurança da conta.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-082.

**Pré-condições:** O usuário deve estar autenticado no sistema.

**Regras de Negócio:** Nenhuma específica além da invalidação do token de acesso.

**Fluxo Principal:**

1.  O usuário acessa a área de configurações ou perfil.

2.  O usuário seleciona a opção "Sair" ou "Logout".

3.  O sistema solicita uma confirmação simples.

4.  O usuário confirma a ação.

5.  O sistema invalida o token de autenticação da sessão atual.

6.  O sistema redireciona o usuário para a tela inicial de Login (UC-02).

**Fluxos Alternativos:** Nenhum.

**Pós-condições:** O sistema mostra a tela de login.

### UC-04: Recuperar Senha

**Objetivo:** Permitir que o usuário recupere o acesso à sua conta.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-003.

**Pré-condições:** Usuário possuir cadastro.

**Regras de Negócio:** RB-002.

**Fluxo Principal:**

1.  Usuário seleciona "Esqueci minha senha".

2.  Sistema solicita o e-mail.

3.  Usuário informa o e-mail.

4.  Sistema valida o endereço.

5.  Sistema envia as instruções de recuperação.

6.  Usuário define uma nova senha.

7.  Sistema valida a nova senha.

8.  Sistema atualiza a senha.

**Fluxos Alternativos:**

- **FA-01: E-mail não encontrado** - Sistema identifica que o e-mail não está cadastrado, informa o usuário, usuário pode informar outro endereço.

**Pós-condições:** Senha atualizada.

### UC-05: Atualizar Perfil

**Objetivo:** Permitir a alteração dos dados cadastrais.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-004.

**Pré-condições:** Usuário autenticado.

**Regras de Negócio:** RB-004, RB-005.

**Fluxo Principal:**

1.  Usuário acessa o perfil.

2.  Seleciona a opção de edição.

3.  Altera os dados desejados.

4.  Sistema valida os dados.

5.  Usuário confirma as alterações.

6.  Sistema salva as alterações.

**Fluxos Alternativos:**

- **FA-01: Dados inválidos** - Sistema identifica inconsistências, informa os campos que precisam ser corrigidos, usuário corrige os dados, sistema retorna ao passo 4.

**Pós-condições:** Perfil atualizado.

### UC-06: Visualizar Perfil

**Objetivo:** Permitir a visualização dos dados do usuário.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-005.

**Pré-condições:** Usuário autenticado.

**Regras de Negócio:** RB-003.

**Fluxo Principal:**

1.  Usuário acessa o perfil.

2.  Sistema consulta os dados cadastrados.

3.  Sistema apresenta as informações do usuário.

**Fluxos Alternativos:** Nenhum.

**Pós-condições:** Dados do perfil apresentados.

### UC-07: Excluir Conta de Usuário

**Objetivo:** Permitir que o usuário apague seu perfil e histórico de forma definitiva.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-083.

**Pré-condições:** Usuário autenticado.

**Regras de Negócio:** RB-068.

**Fluxo Principal:**

1.  O usuário acessa a área de configurações de conta.

2.  O usuário seleciona a opção "Excluir Conta".

3.  O sistema exibe um aviso claro detalhando a irreversibilidade da ação e a perda total de moedas, recompensas e histórico.

4.  O sistema exige a inserção da senha atual para prosseguir.

5.  O usuário insere a validação de segurança e confirma.

6.  O sistema executa a exclusão de todos os registros vinculados ao usuário.

7.  O sistema encerra a sessão e exibe uma mensagem de despedida.

**Fluxos Alternativos:** Nenhum.

**Pós-condições:** Dados do usuário devem ser expurgados do banco de dados e a conta apagada.

## Gerenciamento de Estudos

### UC-08: Cadastrar Disciplina

**Objetivo:** Permitir o cadastro de disciplinas.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-006.

**Pré-condições:** Usuário autenticado.

**Regras de Negócio:** RB-006.

**Fluxo Principal:**

1.  Usuário acessa o módulo de disciplinas.

2.  Seleciona "Nova disciplina".

3.  Informa o nome da disciplina.

4.  Sistema valida o nome.

5.  Sistema cadastra a disciplina.

**Fluxos Alternativos:**

- **FA-01: Nome inválido** - Sistema identifica nome vazio ou inválido, solicita a correção, usuário informa um nome válido, sistema retorna ao passo 4.

**Pós-condições:** Disciplina cadastrada.

### UC-09: Editar Disciplina

**Objetivo:** Permitir a alteração de uma disciplina cadastrada.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-007, RF-084.

**Pré-condições:** Existir disciplina cadastrada.

**Regras de Negócio:** RB-006.

**Fluxo Principal:**

1.  Usuário acessa as disciplinas.

2.  Seleciona uma disciplina.

3.  Seleciona editar.

4.  Altera os dados.

5.  Sistema valida as alterações.

6.  Sistema salva os dados.

**Fluxos Alternativos:**

- **FA-01: Arquivar Disciplina** - O usuário escolhe arquivar disciplina, o sistema move para disciplinas arquivadas.

**Pós-condições:** Disciplina atualizada.

### UC-10: Cadastrar Conteúdo de Estudo

**Objetivo:** Permitir o cadastro de conteúdos vinculados às disciplinas.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-008.

**Pré-condições:** Existir disciplina cadastrada.

**Regras de Negócio:** RB-007.

**Fluxo Principal:**

1.  Usuário acessa conteúdos.

2.  Seleciona adicionar conteúdo.

3.  Informa os dados.

4.  Seleciona uma disciplina.

5.  Sistema valida os dados.

6.  Sistema cadastra o conteúdo.

**Fluxos Alternativos:**

- **FA-01: Disciplina não selecionada** - Sistema impede o cadastro, solicita a seleção de uma disciplina, usuário seleciona a disciplina, sistema retorna ao passo 5.

**Pós-condições:** Conteúdo cadastrado.

### UC-11: Criar Roteiro de Estudos

**Objetivo:** Permitir a criação de roteiros personalizados.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-010.

**Pré-condições:** Existir disciplinas cadastradas.

**Regras de Negócio:** RB-006, RB-007.

**Fluxo Principal:**

1.  Usuário acessa roteiros.

2.  Seleciona novo roteiro.

3.  Define as disciplinas e conteúdos.

4.  Define a organização do roteiro.

5.  Sistema valida os dados.

6.  Sistema registra o roteiro.

**Pós-condições:** Roteiro criado.

### UC-12: Editar Roteiro de Estudos

**Objetivo:** Permitir a alteração de roteiros existentes.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-011.

**Pré-condições:** Existir roteiro cadastrado.

**Regras de Negócio:** RB-006, RB-007.

**Fluxo Principal:**

1.  Usuário acessa seus roteiros.

2.  Seleciona um roteiro.

3.  Seleciona editar.

4.  Altera os dados.

5.  Sistema valida as alterações.

6.  Sistema salva o roteiro.

**Pós-condições:** Roteiro atualizado.

### UC-13: Criar Meta de Estudo

**Objetivo:** Permitir a criação de metas acadêmicas.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-012.

**Pré-condições:** Usuário autenticado.

**Regras de Negócio:** RB-008.

**Fluxo Principal:**

1.  Usuário acessa metas.

2.  Seleciona uma nova meta.

3.  Informa descrição e objetivo.

4.  Define o prazo.

5.  Sistema valida os dados.

6.  Sistema registra a meta.

**Fluxos Alternativos:**

- **FA-01: Dados obrigatórios ausentes** - Sistema identifica ausência de descrição ou objetivo, solicita o preenchimento, usuário corrige os dados, sistema retorna ao passo 5.

**Pós-condições:** Meta cadastrada.

### UC-14: Editar Meta de Estudo

**Objetivo:** Permitir a alteração de metas.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-013.

**Pré-condições:** Existir meta cadastrada.

**Regras de Negócio:** RB-008.

**Fluxo Principal:**

1.  Usuário acessa as metas.

2.  Seleciona uma meta.

3.  Edita seus dados.

4.  Sistema valida as informações.

5.  Sistema salva as alterações.

**Pós-condições:** Meta atualizada.

### UC-15: Registrar Sessão de Estudo

**Objetivo:** Registrar uma atividade de estudo realizada pelo usuário.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-014, RF-019, RF-021.

**Pré-condições:** Usuário autenticado e disciplina cadastrada.

**Regras de Negócio:** RB-009, RB-011, RB-013, RB-014.

**Fluxo Principal:**

1.  Usuário seleciona uma disciplina.

2.  Inicia uma sessão.

3.  Sistema registra o início.

4.  Usuário realiza o estudo.

5.  Usuário encerra a sessão.

6.  Sistema calcula a duração.

7.  Sistema registra a sessão.

**Fluxos Alternativos:**

- **FA-01: Sessão já ativa** - Sistema identifica uma sessão em andamento, impede nova sessão, usuário encerra a anterior.

- **FA-02: Interrupção Inesperada** - O aplicativo é fechado abruptamente, progresso gravado localmente, ao reabrir o sistema redireciona para FA-03.

- **FA-03: Recuperação de Sessão Pendente** - O sistema calcula tempo válido estudado e exibe modal de recuperação (Salvar, Continuar ou Descartar).

**Pós-condições:** Sessão registrada.

### UC-16: Consultar Histórico de Estudos

**Objetivo:** Permitir a consulta das sessões realizadas.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-015.

**Pré-condições:** Usuário autenticado.

**Regras de Negócio:** RB-012, RB-034.

**Fluxo Principal:**

1.  Usuário acessa o histórico.

2.  Sistema consulta os registros.

3.  Sistema apresenta as sessões.

4.  Usuário pode consultar os detalhes.

**Pós-condições:** Histórico apresentado.

### UC-17: Visualizar Progresso dos Estudos

**Objetivo:** Permitir o acompanhamento do progresso acadêmico.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-016.

**Pré-condições:** Existirem registros de estudo.

**Regras de Negócio:** RB-009, RB-010.

**Fluxo Principal:**

1.  Usuário acessa o progresso.

2.  Sistema consulta os registros.

3.  Sistema calcula o progresso.

4.  Sistema apresenta os resultados.

**Pós-condições:** Progresso apresentado.

### UC-18: Utilizar Cronômetro (Controle de Tempo)

**Objetivo:** Permitir a contabilização livre do tempo de estudo.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-017.

**Pré-condições:** Usuário autenticado.

**Regras de Negócio:** RB-014, RB-016.

**Fluxo Principal:**

1.  Usuário acessa o cronômetro.

2.  Seleciona uma disciplina.

3.  Inicia o cronômetro.

4.  Sistema inicia a contagem.

5.  Usuário encerra o cronômetro.

6.  Sistema registra o tempo.

**Fluxos Alternativos:**

- **FA-01: Pausar cronômetro** - Usuário pausa, sistema registra a pausa, usuário retoma a contagem.

**Pós-condições:** Tempo contabilizado.

### UC-19: Utilizar Timer

**Objetivo:** Permitir sessões com duração previamente definida.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-018.

**Pré-condições:** Usuário autenticado.

**Regras de Negócio:** RB-013, RB-015.

**Fluxo Principal:**

1.  Usuário acessa o timer.

2.  Define a duração.

3.  Seleciona uma disciplina.

4.  Inicia o timer.

5.  Sistema inicia a contagem regressiva.

6.  Ao atingir zero, o sistema encerra a sessão.

7.  Sistema registra o tempo.

**Fluxos Alternativos:**

- **FA-01: Encerramento antecipado** - Usuário encerra o timer antes, sistema registra o tempo efetivamente estudado.

**Pós-condições:** Sessão registrada.

### UC-20: Pausar Sessão de Estudo

**Objetivo:** Permitir interromper temporariamente uma sessão.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-020.

**Pré-condições:** Existir sessão ativa.

**Regras de Negócio:** RB-018.

**Fluxo Principal:**

1.  Usuário seleciona pausar.

2.  Sistema interrompe a contagem.

3.  Sistema registra o horário da pausa.

4.  Usuário retoma a sessão.

5.  Sistema continua a contagem.

**Pós-condições:** Pausa registrada.

### UC-21: Encerrar Sessão de Estudo

**Objetivo:** Permitir o encerramento de uma sessão ativa.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-021.

**Pré-condições:** Existir sessão ativa.

**Regras de Negócio:** RB-013, RB-017, RB-018.

**Fluxo Principal:**

1.  Usuário seleciona encerrar.

2.  Sistema calcula o tempo efetivamente estudado.

3.  Sistema registra a sessão.

4.  Sistema atualiza o progresso.

**Pós-condições:** Sessão encerrada e registrada.

## Técnicas de Estudo

### UC-23: Selecionar e Executar Técnica de Estudo

**Objetivo:** Permitir que o usuário escolha e execute uma técnica de estudo antes de iniciar uma sessão.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-022, RF-023, RF-024, RF-029, RF-030, RF-031, RF-032, RF-033, RF-034, RF-035, RF-036, RF-037.

**Pré-condições:** Usuário autenticado e disciplina selecionada.

**Regras de Negócio:** RB-054, RB-055, RB-056, RB-057, RB-058, RB-059.

**Fluxo Principal (Seleção Genérica):**

1.  Usuário acessa as técnicas de estudo.

2.  O sistema apresenta as técnicas disponíveis (Pomodoro, 52/17, Timeboxing, Flowtime e Personalizadas).

3.  Usuário seleciona uma técnica.

4.  O sistema aplica a técnica escolhida e o usuário inicia a sessão.

5.  O sistema registra a técnica utilizada e contabiliza o tempo estudado.

**Fluxos Alternativos (Execução das Técnicas):**

- **FA-01: Execução Pomodoro (RF-029, RF-033)** - O usuário seleciona a técnica Pomodoro. O sistema controla automaticamente os períodos de estudo e descanso (ex: 25min / 5min). Sistema notifica términos.

- **FA-02: Execução 52/17 (RF-030, RF-034)** - O usuário seleciona a técnica 52/17. O sistema controla automaticamente os períodos de estudo (52 min) e descanso (17 min).

- **FA-03: Execução Timeboxing (RF-031, RF-035)** - O usuário seleciona a técnica Timeboxing. O sistema permite ao usuário definir o período destinado à atividade e encerra o bloco ao fim do tempo estipulado.

- **FA-04: Execução Flowtime (RF-032, RF-036)** - O usuário seleciona a técnica Flowtime. O sistema inicia a contagem e permite que o usuário determine manualmente o momento de iniciar e encerrar os períodos de descanso.

- **FA-05: Interrupção (Inesperada ou Manual)** - O usuário ou dispositivo interrompe a sessão. O sistema registra o tempo efetivamente estudado. Para interrupções anômalas, aplica a Recuperação de Sessão Pendente.

**Pós-condições:** Sessão registrada com a técnica e tempos atualizados.

### UC-24: Configurar Parâmetros de Técnica

**Objetivo:** Permitir a personalização de parâmetros das técnicas que aceitam configurações de tempo/ciclos.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-027.

**Pré-condições:** A técnica selecionada deve permitir personalização de tempo.

**Regras de Negócio:** RB-058.

**Fluxo Principal:**

1.  Usuário seleciona uma técnica configurável.

2.  Acessa as configurações.

3.  Define os parâmetros (tempos de foco, descanso, etc.).

4.  Sistema valida os valores.

5.  Sistema salva as configurações.

**Pós-condições:** Técnica configurada com os novos parâmetros.

### UC-25: Notificar Períodos da Técnica

**Objetivo:** Informar ao usuário sobre mudanças entre períodos de estudo e descanso.

**Ator Principal:** Sistema.

**Requisitos Funcionais:** RF-028.

**Pré-condições:** Técnica com períodos definidos estar ativa.

**Regras de Negócio:** RB-058.

**Fluxo Principal:**

1.  Sistema monitora o período atual.

2.  Sistema identifica o término do período.

3.  Sistema envia uma notificação.

4.  Sistema inicia o próximo período (foco ou descanso).

**Pós-condições:** Usuário notificado da mudança de estado.

### UC-26: Gerenciar Técnicas de Estudo Personalizadas

**Objetivo:** Permitir que o usuário cadastre, edite e elimine apenas as suas próprias técnicas de estudo personalizadas.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-087, RF-088, RF-089, RF-090.

**Pré-condições:** Usuário autenticado.

**Regras de Negócio:** RB-069, RB-070, RB-071, RB-072 (O sistema não permite edição de técnicas de estudo padrão).

**Fluxo Principal (Cadastrar Técnica Personalizada):**

1.  O usuário acessa a seção de "Técnicas de Estudo".

2.  Seleciona a opção "Adicionar Técnica Personalizada".

3.  O sistema apresenta o formulário modular (Nome, Descrição, Ciclos/Tempos, Roteiro de passos, Modo Foco).

4.  O usuário preenche os dados e solicita salvar.

5.  O sistema valida os campos e a unicidade do nome.

6.  O sistema salva a nova técnica e vincula ao perfil do usuário.

**Fluxos Alternativos:**

- **FA-01: Editar Técnica Personalizada** - O usuário seleciona "Editar". O sistema verifica a técnica. *Se for padrão (ex: Pomodoro):* bloqueia a ação informando que não pode ser alterada. *Se for personalizada:* permite a edição dos dados, o usuário salva, e o sistema atualiza.

- **FA-02: Excluir Técnica Personalizada** - O usuário seleciona "Eliminar". O sistema exibe alerta mantendo histórico preservado. O usuário confirma e o sistema inativa/remove a técnica do catálogo pessoal.

- **FA-03: Dados Inválidos/Duplicados** - Sistema bloqueia salvar, informa os erros (ex: nome já existe ou tempo \<= 0), usuário corrige e tenta novamente.

**Pós-condições:** Técnica personalizada gerenciada com sucesso e refletida nas opções de estudo.

## Gamificação

### UC-27: Receber Pontos

**Objetivo:** Atribuir pontos ao usuário por ações realizadas na plataforma.

**Ator Principal:** Sistema.

**Requisitos Funcionais:** RF-038.

**Pré-condições:** Usuário autenticado executando uma ação mapeada pela gamificação.

**Regras de Negócio:** RB-019, RB-025.

**Fluxo Principal:**

1.  Usuário realiza uma ação válida.

2.  Sistema verifica os critérios.

3.  Sistema atribui os pontos.

4.  Sistema atualiza o saldo.

**Pós-condições:** Pontuação atualizada no perfil do usuário.

### UC-28: Receber Moedas Virtuais

**Objetivo:** Conceder moedas virtuais ao usuário como recompensa por engajamento.

**Ator Principal:** Sistema.

**Requisitos Funcionais:** RF-039.

**Pré-condições:** Usuário cumprir os requisitos da ação.

**Regras de Negócio:** RB-019, RB-025.

**Fluxo Principal:**

1.  Usuário realiza uma ação válida.

2.  Sistema valida a ação.

3.  Sistema atribui moedas.

4.  Sistema atualiza o saldo.

**Pós-condições:** Saldo de moedas atualizado.

### UC-29: Consultar Pontuação

**Objetivo:** Visualizar o total de pontos e moedas do perfil.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-040.

**Pré-condições:** Usuário autenticado.

**Regras de Negócio:** RB-019.

**Fluxo Principal:**

1.  Usuário acessa a área de pontuação.

2.  Sistema consulta os saldos.

3.  Sistema apresenta pontos e moedas.

**Pós-condições:** Saldos apresentados na interface.

### UC-30: Realizar Check-in

**Objetivo:** Registrar a entrada diária do usuário e recompensá-lo.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-041.

**Pré-condições:** Usuário autenticado.

**Regras de Negócio:** RB-020.

**Fluxo Principal:**

1.  Usuário acessa o check-in.

2.  Sistema verifica a elegibilidade (se já fez hoje).

3.  Sistema registra o check-in.

4.  Sistema concede a recompensa (pontos/moedas).

**Fluxos Alternativos:**

- **FA-01: Check-in já realizado** - Sistema identifica que o check-in já foi realizado hoje e informa o usuário.

**Pós-condições:** Check-in registrado e recompensa concedida.

### UC-31: Receber Medalha ou Conquista

**Objetivo:** Desbloquear e conceder insígnias com base no progresso acadêmico.

**Ator Principal:** Sistema.

**Requisitos Funcionais:** RF-042.

**Pré-condições:** Usuário ter atingido os limiares pré-definidos para a conquista.

**Regras de Negócio:** RB-021.

**Fluxo Principal:**

1.  Usuário realiza uma ação.

2.  Sistema verifica os critérios contínuos de evolução.

3.  Sistema identifica o cumprimento dos requisitos para uma medalha.

4.  Sistema concede a conquista e disponibiliza a medalha visualmente.

**Pós-condições:** Conquista desbloqueada no perfil do usuário.

### UC-32: Visualizar Ranking

**Objetivo:** Permitir que o usuário veja sua classificação em relação a outros estudantes.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-043.

**Pré-condições:** Usuário autenticado e com permissão para ranqueamento.

**Regras de Negócio:** RB-022, RB-023.

**Fluxo Principal:**

1.  Usuário acessa o ranking.

2.  Sistema calcula a classificação com base na pontuação.

3.  Sistema apresenta as posições e a colocação do usuário.

**Pós-condições:** Ranking atualizado apresentado.

### UC-33: Trocar Moedas por Recompensa

**Objetivo:** Utilizar a moeda virtual para adquirir itens virtuais na loja da plataforma.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-044.

**Pré-condições:** Usuário autenticado e possuir saldo positivo.

**Regras de Negócio:** RB-024, RB-025.

**Fluxo Principal:**

1.  Usuário acessa a loja de recompensas.

2.  Seleciona uma recompensa.

3.  Sistema verifica o saldo de moedas do usuário.

4.  Sistema desconta as moedas e registra a transação.

5.  Sistema disponibiliza a recompensa adquirida.

**Fluxos Alternativos:**

- **FA-01: Saldo insuficiente** - Sistema identifica saldo inferior ao preço do item, informa o usuário e a operação é cancelada.

**Pós-condições:** Recompensa adquirida e saldo deduzido com sucesso.

## Grupos de Estudo

### UC-34: Criar Grupo de Estudo

**Objetivo:** Criar um ambiente colaborativo para usuários estudarem juntos.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-045.

**Pré-condições:** Usuário autenticado.

**Regras de Negócio:** RB-026, RB-027.

**Fluxo Principal:**

1.  Usuário acessa a área de grupos.

2.  Seleciona criar grupo.

3.  Informa os dados do grupo (nome, descrição).

4.  Define a capacidade/limites.

5.  Sistema valida os dados.

6.  Sistema cria o grupo e torna o usuário o administrador.

**Fluxos Alternativos:**

- **FA-01: Limite de grupos atingido** - Sistema identifica que o usuário já atingiu seu limite de criação, impedindo a ação.

**Pós-condições:** Grupo de estudo criado com sucesso.

### UC-35: Entrar em Grupo de Estudo

**Objetivo:** Permitir que usuários participem de grupos já existentes.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-046.

**Pré-condições:** Grupo existir e ter vagas.

**Regras de Negócio:** RB-026, RB-028.

**Fluxo Principal:**

1.  Usuário acessa os grupos disponíveis ou utiliza um link de convite.

2.  Seleciona o grupo.

3.  Solicita entrada.

4.  Sistema verifica a capacidade atual.

5.  Sistema adiciona o usuário à lista de membros.

**Fluxos Alternativos:**

- **FA-01: Grupo lotado** - Sistema identifica que a capacidade máxima foi atingida e impede a entrada.

**Pós-condições:** Usuário vinculado ao grupo.

### UC-36: Sair de Grupo de Estudo

**Objetivo:** Permitir a saída voluntária de um grupo de estudos.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-047.

**Pré-condições:** Usuário ser membro do grupo.

**Regras de Negócio:** RB-031.

**Fluxo Principal:**

1.  Usuário acessa um grupo do qual participa.

2.  Seleciona a opção de sair.

3.  Sistema solicita confirmação.

4.  Usuário confirma.

5.  Sistema remove o vínculo do usuário com o grupo.

**Fluxos Alternativos:**

- **FA-01: Cancelamento** - Usuário cancela a operação no modal de confirmação, vínculo é mantido.

**Pós-condições:** Usuário removido do grupo.

### UC-37: Visualizar Participantes do Grupo

**Objetivo:** Exibir a lista de membros que compõem o grupo de estudos.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-048.

**Pré-condições:** Usuário ser membro ou o grupo ser público.

**Regras de Negócio:** RB-030.

**Fluxo Principal:**

1.  Usuário acessa a página do grupo.

2.  Sistema consulta a lista de participantes vinculados.

3.  Sistema apresenta a lista na interface.

**Pós-condições:** Participantes apresentados.

### UC-38: Visualizar Informações de Participante

**Objetivo:** Permitir ver detalhes básicos do perfil de um colega de grupo.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-049.

**Pré-condições:** Usuário e colega estarem no mesmo grupo.

**Regras de Negócio:** RB-029, RB-030.

**Fluxo Principal:**

1.  Usuário acessa a lista de participantes.

2.  Seleciona um participante específico.

3.  Sistema consulta as configurações de privacidade e informações públicas.

4.  Sistema apresenta os dados permitidos do colega.

**Pós-condições:** Informações do participante apresentadas.

### UC-39: Administrar Grupo de Estudos

**Objetivo:** Permitir ao criador/administrador configurar os parâmetros do grupo.

**Ator Principal:** Administrador do Grupo.

**Requisitos Funcionais:** RF-091, RF-092, RF-093, RF-094.

**Pré-condições:** Usuário possuir o papel de administração no grupo.

**Regras de Negócio:** RB-073, RB-074, RB-075, RB-076.

**Fluxo Principal:**

1.  Administrador acessa a área do seu grupo.

2.  Seleciona "Configurações do Grupo".

3.  Sistema exibe opções de Identidade Visual e Privacidade.

4.  Administrador altera dados e clica em Salvar.

5.  Sistema valida e aplica as configurações.

**Fluxos Alternativos:**

- **FA-01: Gerenciar Permissões** - Administrador acessa a aba "Membros", altera papéis de moderadores, e o sistema atualiza permissões.

- **FA-02: Remover Membro** - Administrador localiza participante, clica em Remover, confirma a ação. O sistema revoga o acesso da pessoa ao grupo.

**Pós-condições:** Configurações do grupo atualizadas.

### UC-40: Compartilhar Grupo de Estudos

**Objetivo:** Convidar novas pessoas gerando um link de acesso ou via e-mail.

**Ator Principal:** Usuário (Membro ou Administrador).

**Requisitos Funcionais:** RF-062.

**Pré-condições:** Usuário pertencer ao grupo.

**Regras de Negócio:** RB-037, RB-038.

**Fluxo Principal:**

1.  Usuário clica em "Compartilhar Grupo".

2.  Sistema apresenta modal com opções (E-mail ou Link).

3.  Usuário seleciona Link de Convite e clica em Copiar.

4.  Sistema gera/resgata o link e copia para a área de transferência.

**Fluxos Alternativos:**

- **FA-01: Convidar por E-mail** - Usuário insere endereços, sistema valida e dispara convites por e-mail automaticamente.

- **FA-02: Revogar Link** - O administrador gera um novo link ou revoga o atual, invalidando convites antigos vazados.

**Pós-condições:** Grupo compartilhado com sucesso.

## Monitoramento e Relatórios

### UC-41: Visualizar Dashboard

**Objetivo:** Fornecer uma visão consolidada do desempenho de estudos.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-051.

**Pré-condições:** Usuário autenticado e com histórico gerado.

**Regras de Negócio:** RB-032.

**Fluxo Principal:**

1.  Usuário acessa o dashboard.

2.  Sistema consulta os registros de sessões e progresso.

3.  Sistema calcula os dados agregados.

4.  Sistema apresenta o dashboard.

**Pós-condições:** Dashboard carregado e exibido.

### UC-42: Visualizar Gráficos de Desempenho

**Objetivo:** Fornecer representação visual métrica dos estudos realizados.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-052.

**Pré-condições:** Usuário autenticado.

**Regras de Negócio:** RB-032.

**Fluxo Principal:**

1.  Usuário acessa a aba de desempenho.

2.  Sistema consulta os registros.

3.  Sistema processa os dados e gera os gráficos.

4.  Sistema apresenta os resultados.

**Pós-condições:** Gráficos exibidos corretamente.

### UC-43: Visualizar Indicadores de Desempenho

**Objetivo:** Destacar KPIs educacionais do usuário (ex: horas estudadas).

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-053.

**Pré-condições:** Usuário autenticado.

**Regras de Negócio:** RB-032.

**Fluxo Principal:**

1.  Usuário visualiza seção de indicadores.

2.  Sistema consulta os registros de base de dados.

3.  Calcula os indicadores.

4.  Apresenta os resultados pontuais.

**Pós-condições:** Indicadores exibidos.

### UC-44: Gerar Relatório

**Objetivo:** Consolidar informações de um período específico em formato estruturado.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-054.

**Pré-condições:** Existirem dados no período selecionado.

**Regras de Negócio:** RB-033, RB-034.

**Fluxo Principal:**

1.  Usuário acessa a funcionalidade de relatórios.

2.  Define o período (ex: última semana, mês).

3.  Sistema consulta os dados.

4.  Sistema valida a existência de registros.

5.  Sistema gera o relatório.

**Fluxos Alternativos:**

- **FA-01: Período sem dados** - Sistema identifica ausência de estudos, notifica usuário da falta de dados.

**Pós-condições:** Relatório gerado pronto para leitura ou exportação.

### UC-45: Exportar Relatório

**Objetivo:** Permitir download do relatório em formatos padrão (ex: PDF, CSV).

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-055.

**Pré-condições:** Relatório gerado com sucesso.

**Regras de Negócio:** RB-035.

**Fluxo Principal:**

1.  Usuário seleciona um relatório já gerado.

2.  Seleciona o formato de exportação.

3.  Sistema gera e compila o arquivo de download.

4.  Sistema disponibiliza o arquivo final.

**Pós-condições:** Relatório exportado baixado para o dispositivo do usuário.

## Inteligência Artificial

### UC-46: Utilizar Agente de Inteligência Artificial

**Objetivo:** Interagir com o chatbot IA para tirar dúvidas e buscar orientação.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-056, RF-057.

**Pré-condições:** Usuário autenticado e com conectividade com o módulo IA.

**Regras de Negócio:** RB-036, RB-039.

**Fluxo Principal:**

1.  Usuário acessa a interface do agente.

2.  Sistema solicita interações ou perguntas.

3.  Usuário fornece dados/dúvidas.

4.  Sistema processa as informações junto à API de IA.

5.  IA formula e apresenta uma resposta educacional ao usuário.

**Pós-condições:** Orientação disponibilizada via chat IA.

### UC-47: Solicitar Sugestão de Técnica de Estudo

**Objetivo:** Receber uma recomendação inteligente sobre como otimizar o aprendizado.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-058, RF-059.

**Pré-condições:** Histórico de estudo disponível para análise do perfil.

**Regras de Negócio:** RB-036, RB-037, RB-039.

**Fluxo Principal:**

1.  Usuário solicita recomendação via IA.

2.  Sistema coleta informações do perfil e contexto atual.

3.  Sistema cruza dados com o histórico de estudos do usuário.

4.  IA analisa os padrões de atenção e rendimento.

5.  IA sugere a técnica mais apropriada.

6.  Sistema apresenta a recomendação e a disponibiliza para uso.

**Pós-condições:** Técnica sugerida para a próxima sessão.

### UC-48: Solicitar Sugestão de Meta

**Objetivo:** Receber metas alcançáveis e realistas com base no ritmo do estudante.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-060.

**Pré-condições:** Histórico de estudo disponível.

**Regras de Negócio:** RB-036, RB-037, RB-038, RB-039.

**Fluxo Principal:**

1.  Usuário solicita uma sugestão de meta de longo ou curto prazo.

2.  Sistema coleta as intenções.

3.  Sistema consulta histórico de rendimento.

4.  IA gera uma sugestão factível.

5.  Sistema apresenta a meta.

6.  Usuário decide se deseja aplicá-la ao seu painel.

**Pós-condições:** Meta sugerida sem substituir automaticamente metas existentes.

## Notificações

### UC-49: Configurar Notificações

**Objetivo:** Personalizar os horários e gatilhos de aviso do aplicativo.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-061.

**Pré-condições:** Usuário autenticado.

**Regras de Negócio:** RB-040, RB-042.

**Fluxo Principal:**

1.  Usuário acessa as configurações.

2.  Seleciona a guia de notificações.

3.  Define preferências de som, push e temas.

4.  Define frequência e horários de silêncio.

5.  Sistema salva as configurações.

**Pós-condições:** Preferências de alertas gravadas.

### UC-50: Ativar ou Desativar Notificações

**Objetivo:** Ligar ou desligar globalmente os alertas emitidos pelo aplicativo.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-062.

**Pré-condições:** Usuário autenticado.

**Regras de Negócio:** RB-041.

**Fluxo Principal:**

1.  Usuário acessa as notificações no sistema (ou configurações do OS).

2.  Ativa ou desativa a permissão chave.

3.  Sistema capta e salva a preferência.

**Pós-condições:** Status de notificação do aplicativo atualizado.

### UC-51: Receber Notificação

**Objetivo:** Processo automatizado de entrega de push ou lembrete ao usuário.

**Ator Principal:** Sistema.

**Requisitos Funcionais:** RF-063.

**Pré-condições:** Evento de alerta ocorrer.

**Regras de Negócio:** RB-040, RB-041, RB-042.

**Fluxo Principal:**

1.  Sistema identifica o evento gatilho (ex: término do Pomodoro).

2.  Sistema consulta se o usuário aceita pushes naquele horário.

3.  Sistema dispara o envio ao dispositivo móvel/web.

**Fluxos Alternativos:**

- **FA-01: Notificações desativadas** - Se estiverem desativadas, o alerta visual é mostrado apenas internamente se o app estiver aberto, mas sem envio de push.

**Pós-condições:** Notificação enviada ou descartada adequadamente.

## Foco e Controle de Distrações

### UC-52: Cadastrar Aplicativo para Bloqueio

**Objetivo:** Escolher quais outros aplicativos devem ser impedidos durante o Modo Foco.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-064.

**Pré-condições:** Aplicativo possuir as permissões de OS necessárias (ex: Acessibilidade no Android).

**Regras de Negócio:** RB-043.

**Fluxo Principal:**

1.  Usuário acessa configurações do Modo Foco.

2.  Sistema lê e apresenta os aplicativos instalados no aparelho.

3.  Usuário marca os apps desejados.

4.  Sistema salva e os adiciona à lista de bloqueio.

**Pós-condições:** Aplicativo cadastrado na blacklist do foco.

### UC-53: Editar Aplicativos Bloqueados

**Objetivo:** Atualizar a lista de aplicativos proibidos.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-065.

**Pré-condições:** Existir pelo menos um app cadastrado.

**Regras de Negócio:** RB-043.

**Fluxo Principal:**

1.  Usuário acessa a lista atual de bloqueios.

2.  Sistema exibe itens.

3.  Usuário adiciona ou desmarca apps.

4.  Sistema salva as alterações e atualiza os filtros locais.

**Pós-condições:** Lista de restrição atualizada.

### UC-54: Executar Bloqueio de Aplicativos

**Objetivo:** Ativar a restrição de fato durante uma sessão ativa.

**Ator Principal:** Sistema.

**Requisitos Funcionais:** RF-066.

**Pré-condições:** Sessão de estudo iniciar com Modo Foco ativo e ter apps na lista.

**Regras de Negócio:** RB-044, RB-045.

**Fluxo Principal:**

1.  Usuário inicia uma sessão.

2.  Sistema identifica apps da blacklist.

3.  Sistema ativa o serviço background de monitoramento.

4.  Ao encerrar a sessão de estudo de forma regular, o sistema encerra o monitoramento.

5.  Sistema remove as restrições e libera o aparelho.

**Pós-condições:** Restrições aplicadas apenas no tempo decorrido da sessão.

### UC-55: Monitorar Violação do Modo Foco

**Objetivo:** Interceptar tentativas de abertura de apps bloqueados, alertando o usuário.

**Ator Principal:** Sistema.

**Requisitos Funcionais:** RF-095, RF-096.

**Pré-condições:** Sessão em andamento com Modo Foco ligado e app na blacklist.

**Regras de Negócio:** RB-013, RB-056, RB-057, RB-077, RB-078.

**Fluxo Principal (Encerrar Sessão por Acesso Restrito):**

1.  Usuário tenta abrir um app restrito (ex: Instagram).

2.  Sistema intercepta a abertura.

3.  Sistema exibe tela sobreposta de bloqueio pausando o timer dos estudos temporariamente.

4.  Sistema solicita confirmação para quebrar o foco e encerrar a sessão.

5.  Usuário confirma desistência.

6.  Sistema grava o tempo efetivo até ali e finaliza a sessão de estudos.

7.  Sistema fecha a sobreposição permitindo uso do app restrito.

**Fluxos Alternativos:**

- **FA-01: Recusar Encerramento** - Usuário desiste de entrar no app restrito, clica em "Voltar a estudar". Sistema fecha sobreposição, retoma o timer de onde parou e bloqueia o app indesejado de volta para background.

- **FA-02: Timeout da tela de alerta** - Usuário não responde ao alerta por X segundos; sistema interpreta como desistência e encerra a sessão com tempo gravado até o incidente.

**Pós-condições:** Sessão protegida com registro final dependendo da atitude do estudante.

## Personalização e Acessibilidade

### UC-56: Configurar Acessibilidade Visual

**Objetivo:** Aplicar filtros que auxiliem estudantes com restrições visuais (ex: daltonismo).

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-067.

**Pré-condições:** Usuário autenticado.

**Regras de Negócio:** RB-049, RB-053.

**Fluxo Principal:**

1.  Usuário acessa acessibilidade nas configurações.

2.  Sistema apresenta os filtros disponíveis.

3.  Usuário seleciona um filtro desejado.

4.  Sistema aplica e altera o esquema de cores.

5.  Sistema grava essa preferência.

**Pós-condições:** Acessibilidade visual ajustada e salva.

### UC-57: Alternar Tema da Interface

**Objetivo:** Mudar a aparência geral entre Dark/Light mode.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-068.

**Pré-condições:** Usuário autenticado.

**Fluxo Principal:**

1.  Usuário acessa seção de aparência.

2.  Alterna chave para "Modo Escuro" ou "Modo Claro".

3.  Sistema atualiza as variáveis de CSS/UI globais e salva.

**Pós-condições:** Tema visual ajustado.

### UC-58: Personalizar Cores das Disciplinas

**Objetivo:** Facilitar a identificação visual de cada matéria.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-069.

**Pré-condições:** Ter disciplinas cadastradas.

**Fluxo Principal:**

1.  Usuário acessa a aba da disciplina.

2.  Clica para editar cor.

3.  Sistema exibe paleta (ou HEX).

4.  Usuário escolhe, sistema salva e os cartões e roteiros passam a exibir o tom escolhido.

**Pós-condições:** Cor da disciplina alterada.

### UC-59: Selecionar Pacote de Ícones

**Objetivo:** Modificar toda a iconografia do aplicativo baseada em temas estéticos adquiridos.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-070.

**Pré-condições:** Usuário possuir um pacote de ícone no inventário.

**Regras de Negócio:** RB-046, RB-049.

**Fluxo Principal:**

1.  Usuário vai ao seu inventário de personalização.

2.  Sistema carrega os pacotes comprados/disponíveis.

3.  Usuário seleciona pacote.

4.  Sistema troca e atualiza a UI geral para aquele estilo.

**Fluxos Alternativos:**

- **FA-01: Pacote indisponível** - Se expirado ou erro de carga, sistema avisa e pede pra escolher outro.

**Pós-condições:** Visual de ícones alterado.

### UC-60: Visualizar Evolução dos Ícones

**Objetivo:** Ver o progresso estético de itens dinâmicos que "evoluem" com o estudante (ex: Tamagotchis, plantas virtuais).

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-071.

**Pré-condições:** Usuário ter pacote evolutivo ativo.

**Regras de Negócio:** RB-047, RB-048.

**Fluxo Principal:**

1.  Usuário clica sobre o avatar/ícone central na sua dashboard.

2.  Sistema consulta o histórico XP e estágio atual.

3.  Sistema exibe a arte exata condizente com a evolução atual.

**Pós-condições:** Evolução visual processada em tela.

### UC-61: Restaurar Personalização Padrão

**Objetivo:** Limpar customizações (cores, GIFs, temas) voltando à estética limpa de fábrica.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-072.

**Pré-condições:** Usuário ter alguma modificação ativa.

**Regras de Negócio:** RB-052.

**Fluxo Principal:**

1.  Usuário acessa configurações de personalização.

2.  Clica em "Restaurar Padrão".

3.  Confirma ação no modal do sistema.

4.  Sistema limpa registros de visual customizados e volta o app ao template default.

**Pós-condições:** Layout restaurado à sua versão base.

### UC-62: Pesquisar GIF para Personalização

**Objetivo:** Integrar mídia animada no fundo ou avatares das disciplinas.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-073.

**Pré-condições:** Estar conectado à internet e na interface de customização visual.

**Regras de Negócio:** RB-050, RB-051.

**Fluxo Principal:**

1.  Usuário clica em buscar GIF na capa de um grupo ou disciplina.

2.  Insere termo de busca.

3.  Sistema conecta à API terceira (Giphy/Tenor) e carrega miniaturas.

4.  Usuário escolhe e o sistema baixa/vincula o asset ao módulo escolhido.

**Fluxos Alternativos:**

- **FA-01: Arquivo inválido/Incompatível** - Arquivo retorna com erro, app bloqueia aplicação e sugere outro resultado.

**Pós-condições:** GIF ativo em tela.

### UC-63: Visualizar Personalizações Aplicadas

**Objetivo:** Rever quais itens estéticos estão ativados nas diversas áreas do app centralizados num único painel.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-074.

**Pré-condições:** Usuário autenticado.

**Fluxo Principal:**

1.  Usuário acessa a vitrine do seu perfil estético.

2.  Sistema carrega tema ativo, pacote de ícone e cores escolhidas e apresenta listado para facilitar a troca.

**Pós-condições:** Sumário de visual customizado apresentado.

## Compras e Pagamentos

### UC-64: Realizar Compra

**Objetivo:** Permitir que o usuário adquira moedas virtuais ou recursos/assinaturas utilizando dinheiro real.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-075, RF-076, RF-077, RF-078.

**Pré-condições:** Usuário logado e item disponível para venda em BRL.

**Regras de Negócio:** RB-060, RB-061, RB-062, RB-063, RB-064, RB-067.

**Fluxo Principal:**

1.  Usuário seleciona item pago da loja.

2.  Sistema exibe checkout com métodos (PIX, Cartão).

3.  Usuário seleciona método e preenche dados.

4.  Sistema envia payload ao Gateway.

5.  Gateway confirma transação e retorna sucesso.

6.  Sistema credita usuário com o pacote comprado.

**Fluxos Alternativos:**

- **FA-01: Pagamento PIX** - Sistema gera o QR Code em vez de formulário, usuário escaneia e paga por fora, sistema monitora o webhook de sucesso e libera.

- **FA-02: Transação Negada** - Cartão sem limite/bloqueado. Gateway informa falha e sistema aborta crédito, orientando o usuário a tentar com outro meio.

- **FA-03: Timeout e Conciliação Assíncrona** - O pagamento demora a aprovar ou usuário perde conexão. O gateway confirma via background (webhook). Na próxima inicialização, o app processa o crédito pendente.

**Pós-condições:** Ordem de pagamento processada e estoque virtual (inventário do usuário) atualizado condicionalmente.

### UC-65: Emitir Comprovante de Compra

**Objetivo:** Formalizar a transação entregando um recibo fiscal/interno ao comprador.

**Ator Principal:** Sistema.

**Requisitos Funcionais:** RF-079, RF-080.

**Pré-condições:** Transação no status Aprovada.

**Regras de Negócio:** RB-065, RB-066.

**Fluxo Principal:**

1.  Após aprovação da transação (UC-64), o sistema compila os dados e gera um recibo PDF.

2.  Sistema disponibiliza link de download via tela.

3.  Sistema dispara via SMTP uma cópia desse recibo no e-mail de registro da conta.

**Fluxos Alternativos:**

- **FA-01: Falha no Envio E-mail** - O SMTP falha, o sistema alerta o usuário na tela, mas preserva a possibilidade de download pelo painel.

**Pós-condições:** Comprovante disponibilizado ao cliente.

### UC-66: Consultar Histórico de Compras

**Objetivo:** Centralizar todos os recibos, estornos e gastos para consulta de transparência financeira.

**Ator Principal:** Usuário.

**Requisitos Funcionais:** RF-081.

**Pré-condições:** Usuário autenticado.

**Regras de Negócio:** RB-064.

**Fluxo Principal:**

1.  Usuário navega até Perfil \> Faturas/Histórico de Compras.

2.  Sistema varre banco de dados atrás de registros concluídos ou falhos.

3.  Sistema lista itens com Data, Valor, Status e botão para (re)ver recibo.

**Pós-condições:** Histórico financeiro renderizado em tela.

## Administrador e Backoffice

### UC-67: Gerenciar Itens da Loja (Backoffice)

**Objetivo:** Permitir ao Administrador popular e gerenciar o catálogo de itens e recompensas disponíveis.

**Ator Principal:** Administrador.

**Requisitos Funcionais:** RF-100, RF-101.

**Pré-condições:** Usuário autenticado com credenciais de permissão master/admin no painel web.

**Regras de Negócio:** RB-081.

**Fluxo Principal:**

1.  O Administrador acessa o painel de "Gestão de Loja".

2.  O sistema exibe o CRUD (Criar, Ler, Atualizar, Deletar) do catálogo.

3.  Administrador preenche informações do novo avatar, tema ou booster. Define preço (Moedas V e BRL).

4.  Administrador submete o form.

5.  O sistema valida a tipagem e salva. A loja do app móvel/client é atualizada em tempo real.

**Fluxos Alternativos:**

- **FA-01: Inativar/Remover Item** - Administrador opta por retirar uma skin sazonal. O sistema oculta a skin das próximas compras, mantendo a posse inalterada no inventário de quem já comprou.

**Pós-condições:** Loja de recompensas alimentada e em funcionamento para base de usuários normais.
