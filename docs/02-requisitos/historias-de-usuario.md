# Histórias de Usuário

> Página gerada a partir de [`Histórias de Usuário_.docx`](../../Documentos%20de%20Diagramas/Hist%C3%B3rias%20de%20Usu%C3%A1rio_.docx) para leitura no GitHub. O arquivo original continua sendo a fonte oficial: edite o original e rode `python3 scripts/docs/gerar_docs.py`.
>
> Os diagramas de sequência de cada história estão em [Diagramas de Sequência](../03-diagramas/diagramas-de-sequencia.md).

[⬅ Voltar para Requisitos](../README.md#2-requisitos) · [Sumário geral](../README.md)

## Sumário

- [HU001 — Criar conta](#hu001--criar-conta)
  - [HU002 — Acessar minha conta](#hu002--acessar-minha-conta)
  - [HU003 — Recuperar acesso](#hu003--recuperar-acesso)
  - [HU004 — Gerenciar perfil](#hu004--gerenciar-perfil)
  - [HU005 — Encerrar sessão](#hu005--encerrar-sessão)
  - [HU006 — Excluir conta](#hu006--excluir-conta)
- [Organização dos Estudos](#organização-dos-estudos)
  - [HU007 — Gerenciar disciplinas](#hu007--gerenciar-disciplinas)
  - [HU008 — Gerenciar conteúdos](#hu008--gerenciar-conteúdos)
  - [HU009 — Criar roteiros de estudo](#hu009--criar-roteiros-de-estudo)
  - [HU010 — Definir metas](#hu010--definir-metas)
  - [HU011 — Acompanhar atividades](#hu011--acompanhar-atividades)
  - [HU012 — Arquivar estudos](#hu012--arquivar-estudos)
- [Controle de Tempo e Sessões de Estudo](#controle-de-tempo-e-sessões-de-estudo)
  - [HU013 — Iniciar sessão](#hu013--iniciar-sessão)
  - [HU014 — Controlar sessão](#hu014--controlar-sessão)
  - [HU015 — Utilizar cronômetro e timer](#hu015--utilizar-cronômetro-e-timer)
  - [HU016 — Recuperar sessão interrompida](#hu016--recuperar-sessão-interrompida)
  - [HU017 — Persistir sessão de estudo](#hu017--persistir-sessão-de-estudo)
- [Técnicas de Estudo](#técnicas-de-estudo)
  - [HU018 — Escolher técnica de estudo](#hu018--escolher-técnica-de-estudo)
  - [HU019 — Configurar técnica de estudo](#hu019--configurar-técnica-de-estudo)
  - [HU020 — Utilizar técnicas disponíveis](#hu020--utilizar-técnicas-disponíveis)
  - [HU021 — Acompanhar etapas da técnica](#hu021--acompanhar-etapas-da-técnica)
  - [HU022 — Registrar progresso da técnica](#hu022--registrar-progresso-da-técnica)
  - [HU023 — Criar técnica personalizada](#hu023--criar-técnica-personalizada)
  - [HU024 — Gerenciar técnica personalizada](#hu024--gerenciar-técnica-personalizada)
- [Gamificação](#gamificação)
  - [HU025 — Receber pontos e moedas](#hu025--receber-pontos-e-moedas)
  - [HU026 — Acompanhar saldo](#hu026--acompanhar-saldo)
  - [HU027 — Realizar check in](#hu027--realizar-check-in)
  - [HU028 — Acompanhar conquistas](#hu028--acompanhar-conquistas)
  - [HU029 — Acompanhar ranking](#hu029--acompanhar-ranking)
  - [HU030 — Resgatar recompensas](#hu030--resgatar-recompensas)
- [Grupos de Estudo](#grupos-de-estudo)
  - [HU031 — Criar grupo de estudo](#hu031--criar-grupo-de-estudo)
  - [HU032 — Personalizar grupo](#hu032--personalizar-grupo)
  - [HU033 — Definir privacidade do grupo](#hu033--definir-privacidade-do-grupo)
  - [HU034 — Participar de grupos](#hu034--participar-de-grupos)
  - [HU035 — Visualizar participantes](#hu035--visualizar-participantes)
  - [HU036 — Gerenciar participantes](#hu036--gerenciar-participantes)
  - [HU037 — Convidar pessoas](#hu037--convidar-pessoas)
- [Monitoramento e Relatórios](#monitoramento-e-relatórios)
  - [HU038 — Acompanhar desempenho](#hu038--acompanhar-desempenho)
  - [HU039 — Visualizar dashboard](#hu039--visualizar-dashboard)
  - [HU040 — Analisar indicadores e gráficos](#hu040--analisar-indicadores-e-gráficos)
  - [HU041 — Gerar relatórios](#hu041--gerar-relatórios)
  - [HU042 — Exportar relatórios](#hu042--exportar-relatórios)
- [Inteligência Artificial](#inteligência-artificial)
  - [HU043 — Utilizar assistente de IA](#hu043--utilizar-assistente-de-ia)
  - [HU044 — Receber recomendações personalizadas](#hu044--receber-recomendações-personalizadas)
  - [HU045 — Receber sugestões de técnicas](#hu045--receber-sugestões-de-técnicas)
  - [HU046 — Receber sugestões de metas](#hu046--receber-sugestões-de-metas)
- [Notificações](#notificações)
  - [HU047 — Configurar notificações](#hu047--configurar-notificações)
  - [HU048 — Ativar ou desativar notificações](#hu048--ativar-ou-desativar-notificações)
  - [HU049 — Receber lembretes de estudo](#hu049--receber-lembretes-de-estudo)
- [Foco e Controle de Distrações](#foco-e-controle-de-distrações)
  - [HU050 — Configurar aplicativos restritos](#hu050--configurar-aplicativos-restritos)
  - [HU051 — Configurar Modo Foco](#hu051--configurar-modo-foco)
  - [HU052 — Detectar distrações](#hu052--detectar-distrações)
  - [HU053 — Controlar acesso durante o foco](#hu053--controlar-acesso-durante-o-foco)
- [Personalização e Acessibilidade](#personalização-e-acessibilidade)
  - [HU054 — Personalizar aparência](#hu054--personalizar-aparência)
  - [HU055 — Utilizar acessibilidade visual](#hu055--utilizar-acessibilidade-visual)
  - [HU056 — Alternar tema visual](#hu056--alternar-tema-visual)
  - [HU057 — Personalizar disciplinas](#hu057--personalizar-disciplinas)
  - [HU058 — Personalizar elementos visuais](#hu058--personalizar-elementos-visuais)
  - [HU059 — Desbloquear personalizações](#hu059--desbloquear-personalizações)
  - [HU060 — Restaurar personalização](#hu060--restaurar-personalização)
  - [HU061 — Utilizar GIFs](#hu061--utilizar-gifs)
- [Compras e Pagamentos](#compras-e-pagamentos)
  - [HU062 — Adquirir recursos](#hu062--adquirir-recursos)
  - [HU063 — Realizar pagamento](#hu063--realizar-pagamento)
  - [HU064 — Acompanhar compra](#hu064--acompanhar-compra)
  - [HU065 — Receber comprovante](#hu065--receber-comprovante)
  - [HU066 — Consultar compras](#hu066--consultar-compras)
- [Administração e Backoffice](#administração-e-backoffice)
  - [HU067 — Acessar área administrativa](#hu067--acessar-área-administrativa)
  - [HU068 — Gerenciar itens da loja](#hu068--gerenciar-itens-da-loja)
  - [HU069 — Gerenciar preços](#hu069--gerenciar-preços)
  - [HU070 — Gerenciar recompensas](#hu070--gerenciar-recompensas)

### HU001 — Criar conta

Como estudante, quero criar uma conta, para que eu possa utilizar a plataforma e armazenar minha rotina de estudos.

### HU002 — Acessar minha conta

Como estudante, quero acessar minha conta com segurança, para que eu possa continuar meus estudos e acessar meu progresso.

### HU003 — Recuperar acesso

Como estudante, quero recuperar meu acesso, para que eu possa voltar a utilizar minha conta caso não consiga entrar.

### HU004 — Gerenciar perfil

Como estudante, quero visualizar e atualizar meus dados, para que meu perfil permaneça adequado às minhas necessidades.

### HU005 — Encerrar sessão

Como estudante, quero encerrar minha sessão, para que minha conta permaneça protegida após o uso da plataforma.

### HU006 — Excluir conta

Como estudante, quero solicitar a exclusão da minha conta e dos meus dados, para que eu possa deixar de utilizar a plataforma e remover meus dados pessoais.

## Organização dos Estudos

### HU007 — Gerenciar disciplinas

Como estudante, quero cadastrar, editar e organizar minhas disciplinas, para que eu consiga estruturar minha rotina de estudos.

### HU008 — Gerenciar conteúdos

Como estudante, quero cadastrar, editar e organizar conteúdos relacionados às minhas disciplinas, para que eu consiga localizar facilmente o que preciso estudar.

### HU009 — Criar roteiros de estudo

Como estudante, quero criar e editar roteiros de estudo, para que eu possa organizar uma sequência de conteúdos e atividades.

### HU010 — Definir metas

Como estudante, quero criar e editar metas de estudo, para que eu tenha objetivos claros para minha rotina.

### HU011 — Acompanhar atividades

Como estudante, quero acompanhar as atividades concluídas e pendentes, para que eu saiba o que já realizei e o que ainda preciso estudar.

### HU012 — Arquivar estudos

Como estudante, quero arquivar disciplinas, roteiros e metas concluídos, para que meu ambiente permaneça organizado sem perder meu histórico.

## Controle de Tempo e Sessões de Estudo

### HU013 — Iniciar sessão

Como estudante, quero iniciar uma sessão de estudo, para que eu possa registrar e controlar meu período de dedicação.

### HU014 — Controlar sessão

Como estudante, quero pausar, retomar e encerrar uma sessão de estudo, para que eu tenha controle sobre meu período de estudo.

### HU015 — Utilizar cronômetro e timer

Como estudante, quero utilizar um cronômetro ou timer durante meus estudos, para que eu possa controlar o tempo dedicado às atividades.

### HU016 — Recuperar sessão interrompida

Como estudante, quero recuperar uma sessão de estudo interrompida inesperadamente, para que eu não perca meu tempo e progresso registrados.

### HU017 — Persistir sessão de estudo

Como estudante, quero que o estado da minha sessão seja salvo periodicamente, para que meu progresso seja preservado mesmo em caso de encerramento inesperado da aplicação.

## Técnicas de Estudo

### HU018 — Escolher técnica de estudo

Como estudante, quero escolher uma técnica de estudo para minha sessão, para que eu possa utilizar uma estratégia adequada ao meu objetivo.

### HU019 — Configurar técnica de estudo

Como estudante, quero configurar os parâmetros da técnica escolhida, para que eu possa adaptar a sessão às minhas necessidades.

### HU020 — Utilizar técnicas disponíveis

Como estudante, quero utilizar diferentes técnicas de estudo, como Pomodoro, 52/17, Timeboxing e Flow Time, para que eu possa escolher a estratégia mais adequada para cada situação.

### HU021 — Acompanhar etapas da técnica

Como estudante, quero acompanhar e concluir as etapas da técnica durante a sessão, para que eu saiba o que devo realizar em cada momento.

### HU022 — Registrar progresso da técnica

Como estudante, quero registrar meu progresso durante a utilização de uma técnica de estudo, para que meu histórico reflita como utilizar cada estratégia.

### HU023 — Criar técnica personalizada

Como estudante, quero criar técnicas de estudo personalizadas com meus próprios parâmetros, para que eu possa adaptar o método às minhas necessidades.

### HU024 — Gerenciar técnica personalizada

Como estudante, quero editar e excluir minhas técnicas personalizadas, para que eu possa mantê-las atualizadas conforme minha rotina evolui.

## Gamificação

### HU025 — Receber pontos e moedas

Como estudante, quero receber pontos e moedas por minhas atividades de estudo, para que meu esforço seja reconhecido e minha rotina seja mais motivadora.

### HU026 — Acompanhar saldo

Como estudante, quero visualizar meu saldo de pontos e moedas, para que eu possa acompanhar minha evolução e meus recursos disponíveis.

### HU027 — Realizar check in

Como estudante, quero realizar check ins de estudo, para que eu seja incentivado a manter uma rotina consistente.

### HU028 — Acompanhar conquistas

Como estudante, quero visualizar minhas medalhas e conquistas, para que eu possa acompanhar e valorizar minha evolução.

### HU029 — Acompanhar ranking

Como estudante, quero acompanhar meu posicionamento no ranking, para que eu tenha um estímulo adicional para manter minha rotina.

### HU030 — Resgatar recompensas

Como estudante, quero utilizar minhas moedas para resgatar recompensas, para que minhas conquistas tenham benefícios dentro da plataforma.

## Grupos de Estudo

### HU031 — Criar grupo de estudo

Como estudante, quero criar um grupo de estudo, para que eu possa compartilhar minha rotina e estudar com outras pessoas.

### HU032 — Personalizar grupo

Como administrador de um grupo, quero personalizar suas informações e aparência, para que o grupo tenha uma identidade própria.

### HU033 — Definir privacidade do grupo

Como administrador de um grupo, quero definir a privacidade do grupo, para que eu tenha controle sobre quem pode participar.

### HU034 — Participar de grupos

Como estudante, quero entrar ou sair de grupos de estudo, para que eu possa participar das comunidades que contribuem para minha rotina.

### HU035 — Visualizar participantes

Como participante de um grupo, quero visualizar os participantes e suas informações, para que eu possa conhecer as pessoas que fazem parte da comunidade.

### HU036 — Gerenciar participantes

Como administrador de um grupo, quero gerenciar participantes e permissões, para que o grupo permaneça organizado e seguro.

### HU037 — Convidar pessoas

Como participante de um grupo, quero convidar outras pessoas por email ou link, para que eu possa estudar com pessoas que tenham objetivos semelhantes aos meus.

## Monitoramento e Relatórios

### HU038 — Acompanhar desempenho

Como estudante, quero acompanhar meu desempenho nos estudos, para que eu tenha uma visão geral da minha evolução.

### HU039 — Visualizar dashboard

Como estudante, quero visualizar meu desempenho em um dashboard, para que eu tenha uma visão consolidada da minha rotina de estudos.

### HU040 — Analisar indicadores e gráficos

Como estudante, quero visualizar indicadores e gráficos sobre meus estudos, para que eu possa identificar padrões, avanços e pontos de melhoria.

### HU041 — Gerar relatórios

Como estudante, quero gerar relatórios sobre meu desempenho, para que eu possa analisar minha evolução de forma detalhada.

### HU042 — Exportar relatórios

Como estudante, quero exportar meus relatórios de desempenho, para que eu possa utilizálos ou analisálos fora da plataforma.

## Inteligência Artificial

### HU043 — Utilizar assistente de IA

Como estudante, quero utilizar um assistente de inteligência artificial, para que eu tenha suporte durante minha jornada de estudos.

### HU044 — Receber recomendações personalizadas

Como estudante, quero receber recomendações baseadas no meu perfil, informações fornecidas e histórico de estudos, para que eu possa melhorar minha estratégia de estudos.

### HU045 — Receber sugestões de técnicas

Como estudante, quero receber sugestões de técnicas de estudo, para que eu possa encontrar estratégias mais adequadas às minhas necessidades.

### HU046 — Receber sugestões de metas

Como estudante, quero receber sugestões de metas de estudo, para que eu possa planejar uma rotina mais realista e eficiente.

## Notificações

### HU047 — Configurar notificações

Como estudante, quero configurar minhas preferências de notificações, para que eu receba apenas avisos relevantes para minha rotina.

### HU048 — Ativar ou desativar notificações

Como estudante, quero ativar ou desativar as notificações, para que eu possa controlar como e quando desejo receber avisos.

### HU049 — Receber lembretes de estudo

Como estudante, quero receber lembretes sobre meus estudos, sessões e metas, para que eu consiga manter minha rotina e cumprir meus objetivos.

## Foco e Controle de Distrações

### HU050 — Configurar aplicativos restritos

Como estudante, quero cadastrar e editar os aplicativos que desejo restringir, para que eu possa controlar possíveis distrações durante meus estudos.

### HU051 — Configurar Modo Foco

Como estudante, quero configurar e ativar o Modo Foco durante uma sessão, para que eu possa reduzir as distrações enquanto estudo.

### HU052 — Detectar distrações

Como estudante, quero ser alertado quando tentar acessar um aplicativo restrito durante uma sessão, para que eu possa decidir conscientemente se devo interromper meu estudo.

### HU053 — Controlar acesso durante o foco

Como estudante, quero receber uma confirmação ao tentar acessar um aplicativo restrito, para que eu possa escolher entre encerrar ou retomar minha sessão de estudo.

## Personalização e Acessibilidade

### HU054 — Personalizar aparência

Como estudante, quero personalizar a aparência da plataforma, para que meu ambiente de estudos seja mais agradável e tenha minha identidade.

### HU055 — Utilizar acessibilidade visual

Como estudante, quero utilizar recursos de acessibilidade visual, como filtros de cores, para que eu possa utilizar a plataforma com maior conforto.

### HU056 — Alternar tema visual

Como estudante, quero alternar entre os modos claro e escuro, para que eu possa utilizar a interface de acordo com minha preferência.

### HU057 — Personalizar disciplinas

Como estudante, quero definir cores para minhas disciplinas, para que eu consiga identificálas rapidamente.

### HU058 — Personalizar elementos visuais

Como estudante, quero escolher diferentes pacotes de ícones e elementos visuais, para que eu possa personalizar meu ambiente de estudos.

### HU059 — Desbloquear personalizações

Como estudante, quero desbloquear elementos visuais conforme avanço nos estudos, para que minha evolução também seja representada na personalização da plataforma.

### HU060 — Restaurar personalização

Como estudante, quero restaurar minhas configurações visuais para o padrão, para que eu possa retornar à aparência original da plataforma quando desejar.

### HU061 — Utilizar GIFs

Como estudante, quero pesquisar e utilizar GIFs nas personalizações disponíveis, para que meu ambiente de estudos seja mais divertido e personalizado.

## Compras e Pagamentos

### HU062 — Adquirir recursos

Como estudante, quero adquirir conteúdos e recursos adicionais, para que eu possa ampliar minha experiência na plataforma.

### HU063 — Realizar pagamento

Como estudante, quero realizar pagamentos por diferentes formas disponíveis, como PIX e cartão, para que eu possa concluir minhas compras de maneira conveniente.

### HU064 — Acompanhar compra

Como estudante, quero acompanhar o status das minhas compras, para que eu saiba quando os recursos adquiridos estarão disponíveis.

### HU065 — Receber comprovante

Como estudante, quero receber um comprovante da minha compra e uma cópia no email cadastrado, para que eu tenha um registro da transação realizada.

### HU066 — Consultar compras

Como estudante, quero consultar minhas compras anteriores, para que eu possa acompanhar os recursos que já adquiri.

## Administração e Backoffice

### HU067 — Acessar área administrativa

Como administrador, quero acessar uma área administrativa restrita, para que eu possa gerenciar os recursos disponibilizados na plataforma.

### HU068 — Gerenciar itens da loja

Como administrador, quero cadastrar, editar e inativar os itens disponibilizados na loja, para que os recursos oferecidos aos estudantes permaneçam atualizados.

### HU069 — Gerenciar preços

Como administrador, quero definir e atualizar os preços dos itens da loja, para que os valores cobrados permaneçam corretos.

### HU070 — Gerenciar recompensas

Como administrador, quero cadastrar, editar e inativar recompensas, para que eu possa manter o sistema de recompensas atualizado.

---

[⬅ Voltar para Requisitos](../README.md#2-requisitos) · [Sumário geral](../README.md) · [↑ Topo da página](#)
