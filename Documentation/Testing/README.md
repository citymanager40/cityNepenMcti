# Documento de Instalação e Teste de Banco de Dados - README.md

## Introdução

Este documento serve como um guia de instalação e configuração do banco de dados local para a realização de testes unitários e funcionais no projeto CityManager. A aplicação utiliza dois principais scripts SQL: `Script Comum.sql` e `Script.sql`, que descrevem a estrutura e os dados iniciais do banco de dados.

---

## Requisitos

- Sistema de Gerenciamento de Banco de Dados PostgreSQL instalado.
- Ambiente de Desenvolvimento Integrado (IDE) como o VSCode para execução dos scripts.
  
---

## Instruções de Instalação

### Passo 1: Clonar o Repositório

Se você ainda não clonou o repositório, faça-o utilizando o VSCode ou qualquer outra ferramenta de sua preferência.

### Passo 2: Acessar o Sistema de Gerenciamento de Banco de Dados

Abra o PostgreSQL e acesse utilizando as credenciais apropriadas.

### Passo 3: Execução de Scripts

#### Script para Criação do Banco de Dados

Primeiramente, execute a instrução abaixo para criar o banco de dados.

```sql
CREATE DATABASE citymanager;
Conecte-se ao banco de dados criado.
```

Script de Esquema e Tabelas
Agora, no banco de dados citymanager, execute o script Script.sql inteiro. Este script criará esquemas, tabelas, sequências e relações.

Script de Dados de Teste
Posteriormente, no mesmo banco de dados, execute o script Script Comum.sql. Este script inserirá dados iniciais nas tabelas para fins de testes.

Execução de Testes
Com o banco de dados devidamente configurado, você agora está pronto para executar as baterias de testes unitários e funcionais na aplicação.

Testes unitários: Execute o comando correspondente em seu ambiente de desenvolvimento.
Testes funcionais: Siga as diretrizes fornecidas pela documentação da aplicação ou pela equipe de desenvolvimento.
Conclusão
Este documento proporciona as etapas necessárias para a configuração do ambiente local de banco de dados para testes. É imprescindível a correta execução dessas etapas para garantir a eficácia dos testes unitários e funcionais.

Para quaisquer dúvidas ou problemas enfrentados durante a instalação, por favor, consulte a equipe de desenvolvimento.

Fim do documento.
