# 03_UpdateDeployReadme.ps1

# Caminho para o arquivo README.md dentro da pasta Documentation\Deployment
$readmePath = ".\Documentation\Deployment\README.md"

# Conteúdo do arquivo README.md
$readmeContent = @"
# Documentação de Implantação

## Introdução

Este documento descreve os passos necessários para implantar o sistema no ambiente de produção.

## Requisitos

- Servidor com Linux/Windows
- Docker instalado
- Acesso ao repositório de imagens do Docker

## Passos para a Implantação

### 1. Clonar o Repositório

Clone o repositório do projeto para o servidor de produção.

\`\`\`
git clone [URL do Repositório]
\`\`\`

### 2. Configurar Variáveis de Ambiente

Configure todas as variáveis de ambiente necessárias conforme descrito na documentação.

### 3. Executar Scripts de Banco de Dados

Execute os scripts SQL para preparar o banco de dados.

\`\`\`
./run-database-scripts.sh
\`\`\`

### 4. Iniciar Serviços via Docker

Navegue até a pasta do projeto e execute o seguinte comando:

\`\`\`
docker-compose up -d
\`\`\`

Isso irá iniciar todos os serviços definidos no arquivo `docker-compose.yml`.

## Verificação

Após seguir os passos acima, o sistema deve estar funcionando conforme esperado. Para verificar, acesse:

\`\`\`
http://[ENDEREÇO DO SERVIDOR]
\`\`\`

## Suporte

Para mais informações ou suporte, consulte a documentação técnica ou entre em contato com a equipe de desenvolvimento.
"@

# Criar ou atualizar o arquivo README.md com o conteúdo especificado
Set-Content -Path $readmePath -Value $readmeContent