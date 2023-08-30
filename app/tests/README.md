# Planejamento de Testes Unitários para o Projeto cityNepenMcti

## Introdução

O presente documento descreve o planejamento para a implementação de uma bateria de testes unitários com o objetivo de assegurar a robustez, funcionalidade e confiabilidade do projeto cityNepenMcti. O framework sugerido para a condução desses testes é o pytest, dada sua capacidade de fornecer uma abordagem eficaz e abrangente para testes de unidade em Python.

## Estrutura de Diretórios de Teste

A estrutura de diretórios para os testes seguirá um padrão similar ao da aplicação para facilitar a correspondência entre os componentes da aplicação e seus respectivos testes. A estrutura será organizada sob a pasta pp/tests, subdividida em:

- unit/ : para os testes unitários
- unctional/ : para os testes funcionais (não abordados neste documento)

## Componentes para Teste

A seguir, descrevemos os componentes da aplicação que serão foco dos testes unitários.

### 1. Controladores (Controllers)

Arquivos a serem testados:

- eventoController.py
- loginController.py
- eventoSearchController.py
- elatorioController.py

Objetivo: Testar métodos e funções que lidam com a lógica de negócio e a interação com os modelos.

### 2. Modelos (Models)

Arquivos a serem testados:

- eventoModel.py
- userModel.py
- categoriaModel.py
- eventoHistoricoModel.py
- eventoObservacaoModel.py
- statusEventoModel.py
- subcategoriaModel.py

Objetivo: Testar a lógica de negócios e validações relacionadas às entidades de negócios.

### 3. Formulários (Forms)

Arquivos a serem testados:

- eventoForm.py
- loginForm.py
- egisterForm.py

Objetivo: Validar a lógica de validação e outras funcionalidades presentes nos formulários.

### 4. Funções de Utilidade e Rotas

Arquivos a serem testados:

- eventoRout.py
- eventoSearchRout.py
- loginRout.py
- elatorioRout.py

Objetivo: Testar qualquer código adicional em utilidades e rotas que seja crítico para a lógica do negócio.

### 5. Enumerações

Arquivos a serem testados:

- statusEventoEnum.py

Objetivo: Compreender e validar as constantes usadas ao longo do projeto.

### 6. Relatórios

Arquivos a serem testados:

- elatorio.py

Objetivo: Verificar como os relatórios são gerados e se atendem às especificações.

## Etapas Futuras

Após a definição e aprovação deste planejamento, os testes unitários serão desenvolvidos de acordo com os componentes listados.

## Conclusão

O planejamento aqui apresentado visa fornecer uma estratégia abrangente para a implementação de testes unitários no projeto cityNepenMcti. A implementação de uma bateria de testes unitários é crucial para garantir a qualidade do software, fornecendo uma base sólida para futuras iterações do projeto.
