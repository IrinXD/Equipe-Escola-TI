# Regras de Negócio

> Página gerada a partir de [`Regras de negócio.docx`](../../Documentos%20de%20Diagramas/Regras%20de%20neg%C3%B3cio.docx) para leitura no GitHub. O arquivo original continua sendo a fonte oficial: edite o original e rode `python3 scripts/docs/gerar_docs.py`.

[⬅ Voltar para Requisitos](../README.md#2-requisitos) · [Sumário geral](../README.md)

## Sumário

- [Regras de Negócio.](#regras-de-negócio)
- [Usuários e Autenticação](#usuários-e-autenticação)
- [Gerenciamento de Estudos](#gerenciamento-de-estudos)
- [Controle de Tempo](#controle-de-tempo)
- [Gamificação](#gamificação)
- [Grupos de Estudo](#grupos-de-estudo)
- [Monitoramento e Relatórios](#monitoramento-e-relatórios)
- [Notificações](#notificações)
- [Foco e Controle de Distrações](#foco-e-controle-de-distrações)
- [Personalização e Acessibilidade](#personalização-e-acessibilidade)
- [Técnicas de Estudo](#técnicas-de-estudo)
- [Compras e Pagamentos](#compras-e-pagamentos)

## **Regras de Negócio.** 

##  **Usuários e Autenticação**

RB-001: O endereço de e-mail deve ser único para cada usuário cadastrado.

RB-002: A senha deve atender aos critérios mínimos de segurança definidos pelo sistema.

RB-003: Apenas usuários autenticados podem acessar funcionalidades restritas.

RB-004: Alterações cadastrais devem ser salvas automaticamente após confirmação do usuário.

RB-005: O sistema deve validar os dados informados antes de concluir o cadastro ou atualização.

**RB-082:** Elementos arquivados (disciplinas, metas) não devem aparecer nas listas de seleção para novas sessões de estudo, mas devem ser mantidos nos relatórios e estatísticas passadas.

**RB-068:** A exclusão de conta é uma ação irreversível. Após a confirmação, todos os dados identificáveis do usuário devem ser expurgados do banco de dados em conformidade com as leis de proteção de dados.

## **Gerenciamento de Estudos**

RB-006: Toda disciplina deve possuir um nome válido e não vazio.

RB-007: Todo conteúdo de estudo deve estar vinculado a uma disciplina.

RB-008: Toda meta de estudo deve possuir uma descrição e um objetivo definido.

RB-009: O progresso do usuário deve ser calculado com base no tempo estudado e nas atividades realizadas.

RB-010: O progresso de uma disciplina não pode ultrapassar 100%.

RB-011: Toda sessão de estudo deve estar associada a uma disciplina.

RB-012: Alterações em registros de estudo devem ser armazenadas em histórico.

## **Controle de Tempo**

RB-013: Toda sessão de estudo deve possuir duração maior que zero.

RB-014: Apenas uma sessão de estudo pode permanecer ativa por vez.

RB-015: O timer deve encerrar automaticamente ao atingir o tempo configurado.

RB-016: O cronômetro deve permanecer ativo até ser encerrado pelo usuário.

RB-017: O sistema deve registrar automaticamente as sessões interrompidas.

RB-018: O histórico de pausas deve ser mantido durante a sessão.

**RB-083:** O tempo contabilizado para sessões recuperadas após interrupção anómala deve limitar-se estritamente ao último salvamento automático verificado, desconsiderando o período em que o dispositivo permaneceu desligado ou inativo.

**RB-084:** Registos de sessões locais não recuperadas ou não decididas pelo utilizador após 7 dias devem ser consolidados automaticamente no histórico até ao último *heartbeat* e limpos do armazenamento temporário.

## **Gamificação**

RB-019: Pontos e moedas devem ser concedidos apenas por ações válidas definidas pelo sistema.

RB-020: Check-ins diários e semanais devem gerar recompensas.

RB-021: Medalhas e conquistas devem ser concedidas automaticamente quando seus critérios forem atingidos.

RB-022: O ranking deve ser calculado com base nos critérios definidos pelo sistema.

RB-023: O sistema deve recalcular o ranking sempre que houver alteração relevante na pontuação.

RB-024: Recompensas internas devem ser adquiridas exclusivamente com moedas virtuais.

RB-025: O sistema deve impedir tentativas de fraude na obtenção de pontos e moedas.

## **Grupos de Estudo**

RB-026: Um usuário pode participar de múltiplos grupos de estudo.

RB-027: O sistema deve limitar a quantidade de grupos criados simultaneamente por um mesmo usuário.

RB-028: Não deve ser permitida a entrada em grupos que tenham atingido sua capacidade máxima.

RB-029: O tempo estudado exibido nos grupos deve ser obtido dos registros de estudo do participante.

RB-030: As informações dos participantes devem ser atualizadas para todos os membros do grupo.

RB-031: A saída de um grupo deve exigir confirmação do usuário.

**RB-073:** O usuário criador de um grupo de estudos torna-se automaticamente o Administrador Principal com controle total sobre as configurações e membros.

**RB-074:** Grupos configurados como "Privados" exigem que o ingresso de novos membros ocorra via convite por e-mail ou aprovação prévia do administrador ao acessar pelo link.

**RB-075:** Grupos configurados como "Somente Amigos" ficam visíveis apenas para usuários que possuem vínculo de amizade ativo com pelo menos um administrador do grupo.

**RB-076:** A remoção de um usuário de um grupo de estudos não apaga as mensagens e materiais que ele compartilhou previamente no chat do grupo.

## **Monitoramento e Relatórios**

RB-032: Os indicadores exibidos no dashboard devem ser calculados a partir dos registros de estudo armazenados.

RB-033: Os relatórios devem considerar apenas dados válidos e consolidados.

RB-034: O histórico de desempenho deve ser preservado para consultas futuras.

RB-035: Os dados exportados devem refletir as informações existentes no momento da geração do relatório.

**Inteligência Artificial**

RB-036: As recomendações da IA devem considerar as informações fornecidas pelo usuário.

RB-037: As sugestões da IA devem utilizar o histórico de estudos como base para personalização.

RB-038: As metas sugeridas pela IA não devem substituir metas definidas manualmente sem autorização do usuário.

RB-039: As recomendações geradas pela IA devem possuir finalidade exclusivamente educacional.

## **Notificações**

RB-040: As notificações devem respeitar as preferências configuradas pelo usuário.

RB-041: Notificações desativadas não devem ser enviadas.

RB-042: A frequência de notificações deve ser limitada para evitar excesso de envios.

## **Foco e Controle de Distrações**

RB-043: A lista de aplicativos bloqueados pode ser alterada a qualquer momento pelo usuário.

RB-044: Aplicativos cadastrados para bloqueio devem permanecer inacessíveis durante sessões de estudo ativas.

RB-045: O bloqueio deve ser encerrado automaticamente ao término da sessão de estudo.

**RB-077:** O tempo em que a tela de alerta de violação do Modo Foco permanece aberta não deve ser contabilizado como tempo de estudo efetivo.

**RB-078:** Caso o usuário confirme o encerramento da sessão via alerta de foco, a interrupção deve ser registrada no histórico marcando o motivo como "Acesso a Aplicativo Restrito".

##  **Personalização e Acessibilidade**

RB-046: O usuário pode possuir apenas um pacote de ícones ativo por vez.

RB-047: A evolução visual dos ícones deve ocorrer automaticamente quando os critérios definidos forem atingidos.

RB-048: O estágio de evolução dos ícones deve ser armazenado permanentemente.

RB-049: Os pacotes de ícones devem atender aos requisitos mínimos de acessibilidade e legibilidade.

RB-050: GIFs utilizados na personalização devem estar em formatos suportados pelo sistema.

RB-051: GIFs que comprometam o desempenho da aplicação não devem ser permitidos.

RB-052: O usuário pode restaurar a personalização visual padrão a qualquer momento.

RB-053: Os filtros de acessibilidade devem prevalecer sobre as personalizações visuais aplicadas pelo usuário.

## **Técnicas de Estudo**

RB-054: O usuário deve selecionar uma disciplina antes de iniciar uma técnica de estudo associada ao registro de uma sessão.

RB-055: A técnica de estudo utilizada deve ser registrada juntamente com a sessão de estudo.

RB-056: O tempo contabilizado para uma sessão deve considerar apenas os períodos destinados ao estudo.

RB-057: Sessões de estudo interrompidas devem manter o registro do tempo efetivamente estudado antes da interrupção.

RB-059: O progresso obtido durante uma técnica de estudo deve ser calculado com base nas atividades e registros gerados durante a sessão.

**RB-069:** As técnicas de estudo personalizadas criadas pelo utilizador são de acesso exclusivo do seu perfil e não ficam visíveis para outros utilizadores.

**RB-070:** O utilizador não pode editar nem eliminar as técnicas de estudo padrão fornecidas nativamente pelo sistema.

**RB-071:** O nome de uma técnica personalizada deve ser único dentro do perfil de cada utilizador.

**RB-072:** A eliminação de uma técnica personalizada não pode apagar nem comprometer os dados de tempo e progresso armazenados no histórico das sessões de estudo já realizadas

## **Compras e Pagamentos** 

RB-060: O usuário deve estar autenticado para realizar uma compra.

RB-061: O pagamento somente deve ser considerado concluído após a confirmação da transação pelo serviço de pagamento.

RB-062: O conteúdo ou recurso adquirido somente deve ser disponibilizado após a confirmação do pagamento.

RB-063: Transações recusadas ou com falha não devem liberar o conteúdo ou recurso adquirido.

RB-064: O sistema deve registrar o status da transação no histórico de compras.

RB-065: O comprovante deve ser gerado somente para transações processadas com sucesso.

RB-066: O comprovante deve ser enviado para o endereço de e-mail cadastrado do usuário.

RB-067: Os dados de pagamento devem ser tratados de acordo com os mecanismos de segurança definidos pelo serviço de pagamento utilizado.

**RB-079:** A liberação de conteúdos pagos deve ser vinculada ao identificador único do pedido (*idempotência*), garantindo que instabilidades na rede do usuário não dupliquem cobranças nem impeçam a entrega do produto.

**RB-080:** Transações sem resposta conclusiva do gateway por mais de 24 horas devem ser marcadas automaticamente como Expiradas/Canceladas.

**Administrador" e Backoffice**

**RB-081:** Um item da loja não pode ser excluído se já tiver sido adquirido por algum usuário; ele deve ser marcado como "Inativo/Indisponível".

---

[⬅ Voltar para Requisitos](../README.md#2-requisitos) · [Sumário geral](../README.md) · [↑ Topo da página](#)
