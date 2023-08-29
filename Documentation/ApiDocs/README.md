# Documentação de API

## Introdução
Este documento delineia os endpoints da API disponíveis no sistema e serve como um guia para sua utilização.

## Autenticação
Consulte loginController.py para métodos de autenticação.
- **Endpoint:** /auth
- **Métodos:** POST

## Gerenciamento de Eventos
Consulte eventoController.py para funcionalidades de gerenciamento de eventos.
- **Endpoint:** /events
- **Métodos:** GET, POST, PUT, DELETE

## Pesquisa de Eventos
Consulte eventoSearchController.py para funcionalidades de pesquisa de eventos.
- **Endpoint:** /events/search
- **Métodos:** GET

## Geração de Relatórios
Consulte elatorioController.py para funcionalidades de geração de relatórios.
- **Endpoint:** /reports
- **Métodos:** GET, POST

## Códigos de Status
Os códigos de status HTTP comumente retornados pela API incluem:
- 200 OK
- 400 Solicitação Incorreta
- 401 Não Autorizado
- 403 Proibido
- 404 Não Encontrado

## Exemplos
Amostras de código para chamadas à API podem ser encontradas dentro do diretório controller.

## Suporte
Para dúvidas adicionais, favor contatar a equipe de desenvolvimento.
