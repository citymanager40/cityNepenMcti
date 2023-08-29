# 06_UpdateTestingReadme.ps1

# Caminho para o arquivo README.md dentro da pasta Documentation\Testing
$readmePath = ".\Documentation\Testing\README.md"

# Conteúdo do arquivo README.md
$readmeContent = @"
# Documentação de Testes

## Introdução

Este documento fornece uma visão abrangente dos métodos e práticas de teste empregados neste projeto, garantindo que a qualidade e a estabilidade do sistema sejam mantidas em conformidade com os padrões estabelecidos.

## Metodologias de Teste

1. **Testes Unitários**: Focados em validar o comportamento de unidades isoladas de código.
2. **Testes de Integração**: Avaliam a coesão entre diferentes partes do sistema.
3. **Testes de Carga**: Certificam-se de que o sistema pode lidar com a demanda prevista.

## Ferramentas Utilizadas

- JUnit para testes unitários.
- Selenium para testes de interface.
- Apache JMeter para testes de carga.

## Execução de Testes

Os testes são executados automaticamente durante a fase de integração contínua por meio de um pipeline CI/CD.

### Comandos para Executar Testes Manualmente

1. Testes Unitários: `mvn test`
2. Testes de Integração: `mvn verify`
3. Testes de Carga: `jmeter -n -t [TestFile]`

## Relatórios de Teste

Após a execução dos testes, os relatórios são gerados e armazenados na pasta `Reports`.

## Rastreabilidade

A rastreabilidade dos testes é mantida através de identificadores únicos que vinculam cada caso de teste aos requisitos correspondentes.

## Suporte e Contato

Para quaisquer dúvidas ou informações adicionais, por favor, consulte a documentação técnica ou entre em contato com a equipe de testes.
"@

# Criar ou atualizar o arquivo README.md com o conteúdo especificado
Set-Content -Path $readmePath -Value $readmeContent