## Visão Geral da Arquitetura de cityNepenMcti

## Objetivos do Projeto

O objetivo principal deste projeto, cityNepenMcti, é desenvolver um sistema de backend robusto para a coleta de dados de sistemas legados. Este backend terá a dupla função de informar gestores municipais e o público geral sobre o status e as demandas de serviços públicos. Os objetivos específicos incluem:

1. Desenvolvimento de módulos de APIs para escrita e leitura em sistemas de coleta de dados.
2. Criação de painéis de controle para visualização de dados pertinentes às demandas públicas e seu atendimento.
3. Identificação de funcionalidades essenciais com base nas exigências específicas das várias pastas da administração municipal.

## Design Arquitetural

O design arquitetural escolhido é altamente modular, utilizando Python para o desenvolvimento do backend. Ele segue o padrão MVC (Model-View-Controller), que separa de forma eficaz as responsabilidades, permitindo um código escalável e de fácil manutenção. Abaixo, segue a explicação dos componentes estruturais do repositório:

### Diretório Raiz

- `.gitignore`: Especifica arquivos e pastas a serem ignorados pelo Git.
- `app.py`: Ponto de entrada da aplicação, configurando e executando o servidor backend.
- `requirements.txt`: Lista os pacotes Python necessários para uma configuração fácil.
- `Script Comum.sql` e `Script.sql`: Scripts SQL para configuração do banco de dados.

### Diretório `app`

#### Controladores (`app/controller`)

- `eventoController.py`: Gerencia operações CRUD para eventos.
- `eventoSearchController.py`: Lida com as funcionalidades de pesquisa de eventos.
- `loginController.py`: Supervisiona a autenticação do usuário.
- `relatorioController.py`: Gerencia a geração de relatórios.
- `roleRequired.py`: Implementa controle de acesso baseado em função.

#### Banco de Dados (`app/database.py`)

- Gerencia conexões e transações com o banco de dados.

#### Enumerações (`app/enum`)

- `statusEventoEnum.py`: Enumerações para status de eventos.

#### Formulários (`app/forms`)

- `eventoForm.py`: Manipulação de formulários para eventos.
- `loginForm.py`: Manipulação de formulários para login do usuário.
- `registerForm.py`: Manipulação de formulários para registro do usuário.

#### Modelos (`app/models`)

- Contém modelos de Mapeamento Objeto-Relacional (ORM) correspondentes às entidades do banco de dados.

#### Relatórios (`app/relatorios`)

- `relatorio.py`: Implementa funcionalidades de geração de relatórios.

#### Rotas (`app/rotas`)

- Contém a lógica de roteamento, conectando controladores a endpoints de URL.

#### Recursos Estáticos (`app/static`)

- Contém arquivos CSS e JavaScript, além de imagens necessárias para a aplicação web.

#### Modelos (`app/templates`)

- Composto por modelos HTML que compõem a interface do usuário.

### Metodologia Ágil e Integração com o Plano de Trabalho

A metodologia empregada segue três princípios fundamentais extraídos do "Manifesto para o desenvolvimento ágil de software" ou simplesmente Manifesto Ágil:

1. **Entrega de Valor de Negócio**: O projeto prioriza as necessidades da administração municipal, focando na criação de APIs e dashboards que agregam valor direto às operações do governo.
   
2. **Auto-Gestão da Equipe**: A arquitetura modular permite que a equipe trabalhe de forma auto-gerenciada, dividindo as tarefas de acordo com as competências e prioridades.
   
3. **Comunicação Direta**: A documentação e os relatórios gerados, especialmente através do `relatorioController.py`, servem como canais de comunicação direta entre os tomadores de decisão e a equipe de desenvolvimento.

#### Fases de Implementação

1. **Diligências Técnicas**: Entrevistas com o secretariado para identificar demandas específicas e possíveis integrações.
   
2. **Modelagem do Sistema**: Inclui a criação de casos de uso, diagramas de E-R e classes, bem como a revisão do cronograma. A estrutura atual já prepara o terreno para essa fase, segmentando diferentes responsabilidades em diferentes módulos.
   
3. **Desenvolvimento do Backend**: A estrutura do repositório está bem posicionada para abordar esta etapa. Módulos para autenticação (AAA), dashboards, e APIs já estão em desenvolvimento.
   
4. **Integração e Testes**: O sistema estará hospedado na nuvem para testes e avaliações, com a possibilidade de integração com outros produtos.

5. **Transferência de Tecnologia**: Workshops e treinamentos, além da documentação técnica, para garantir uma transferência de conhecimento eficiente.

#### Resultados Esperados

1. Uma ferramenta computacional integrada para a gestão de dados de cidades inteligentes, incluindo APIs e dashboards.
   
2. Testes através de um aplicativo desenvolvido em uma ação paralela.
   
3. Disponibilização do sistema através de containers, com documentação completa para implementações futuras.

Para consultas adicionais ou colaborações, favor referir-se às diretrizes de contribuição ou contatar o arquiteto sênior responsável.

## Conclusão

O design arquitetural escolhido está substancialmente alinhado com os objetivos estipulados, otimizando para modularidade, escalabilidade e manutenção. Ele foi projetado especificamente para se conectar com sistemas legados para coleta de dados e apresenta uma abordagem direta para futuras adaptações e extensões.

Para mais informações ou contribuições, consulte as diretrizes de contribuição ou entre em contato com o arquiteto sênior responsável por este repositório.

---
Última atualização: 29 de março de 2023  
Arquiteto de Soluções Sênior: [Marcos Aires]  
---
