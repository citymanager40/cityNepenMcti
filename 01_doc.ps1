# Script PowerShell para criar estrutura de Documentação Técnica

# Navegar até o diretório do projeto cityNepenMcti (ajuste o caminho conforme necessário)
Set-Location -Path "C:\path\to\cityNepenMcti"

# Criar o diretório principal para Documentação Técnica
New-Item -Path ".\Documentation" -ItemType Directory

# Criar subdiretórios para diferentes tipos de documentação
New-Item -Path ".\Documentation\Architecture" -ItemType Directory
New-Item -Path ".\Documentation\SecurityPolicies" -ItemType Directory
New-Item -Path ".\Documentation\ApiDocs" -ItemType Directory
New-Item -Path ".\Documentation\UserGuides" -ItemType Directory
New-Item -Path ".\Documentation\Testing" -ItemType Directory
New-Item -Path ".\Documentation\Deployment" -ItemType Directory
New-Item -Path ".\Documentation\Diagrams" -ItemType Directory

# Criar arquivos de documentação em cada subdiretório
New-Item -Path ".\Documentation\Architecture\README.md" -ItemType File
New-Item -Path ".\Documentation\SecurityPolicies\README.md" -ItemType File
New-Item -Path ".\Documentation\ApiDocs\README.md" -ItemType File
New-Item -Path ".\Documentation\UserGuides\README.md" -ItemType File
New-Item -Path ".\Documentation\Testing\README.md" -ItemType File
New-Item -Path ".\Documentation\Deployment\README.md" -ItemType File
New-Item -Path ".\Documentation\Diagrams\README.md" -ItemType File

# Exibir mensagem de conclusão
Write-Host "Estrutura de Documentação Técnica criada com sucesso."