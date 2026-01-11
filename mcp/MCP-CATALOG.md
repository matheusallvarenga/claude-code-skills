# Catálogo Completo de MCP Servers

> **Versão:** 1.0
> **Data:** 2025-12-23
> **Total de MCPs:** 14 (6 Cloud + 6 Built-in + 1 Custom + 1 Dev)
> **Localização Config:** `.claude/mcp.json`

---

## Sumário

1. [Visão Geral](#visão-geral)
2. [Estrutura de Configuração](#estrutura-de-configuração)
3. [MCPs por Categoria](#mcps-por-categoria)
   - [Cloud APIs (6)](#1-cloud-api-mcps)
   - [Built-in (6)](#2-built-in-mcps)
   - [Custom (1)](#3-custom-mcps)
   - [Development (1)](#4-development-mcps)
4. [Guia de Implementação](#guia-de-implementação)
5. [Troubleshooting](#troubleshooting)

---

## Visão Geral

MCP (Model Context Protocol) servers permitem que o Claude Code se conecte a serviços externos, APIs e ferramentas locais, expandindo suas capacidades.

### Distribuição por Tipo

| Tipo | Quantidade | Descrição |
|------|------------|-----------|
| **Cloud API** | 6 | Serviços externos via HTTP/HTTPS |
| **Built-in** | 6 | Habilitados via settings.json |
| **Custom** | 1 | Desenvolvido localmente (Node.js) |
| **Development** | 1 | Para desenvolvimento (Genkit) |

### Status Atual

```
Cloud APIs ............ 6 ativos
├── Notion ............ mcp.notion.com
├── Supabase .......... mcp.supabase.com
├── Figma Desktop ..... localhost:3845
├── shadcn ............ npx command
├── Context7 .......... npx command
└── Vercel ............ mcp.vercel.com

Built-in .............. 6 habilitados
├── markitdown
├── memory
├── filesystem
├── context7
├── github
└── fetch

Custom ................ 1 implementado
└── obsidian-docs ..... Node.js StdIO
```

---

## Estrutura de Configuração

### Arquivo Principal: `.claude/mcp.json`

```json
{
  "mcpServers": {
    "nome-do-mcp": {
      "url": "https://...",      // Para Cloud APIs
      // OU
      "command": "npx",          // Para CLI tools
      "args": ["package-name"]
    }
  }
}
```

### Habilitação: `.claude/settings.json`

```json
{
  "enableAllProjectMcpServers": true,
  "enabledMcpjsonServers": [
    "markitdown",
    "memory",
    "filesystem",
    "context7",
    "github",
    "fetch"
  ]
}
```

---

## MCPs por Categoria

---

## 1. Cloud API MCPs

Serviços externos acessados via HTTP/HTTPS.

---

### 1.1 Notion

**Integração com Notion Workspace**

| Atributo | Valor |
|----------|-------|
| **URL** | `https://mcp.notion.com/mcp` |
| **Tipo** | Cloud API |
| **Autenticação** | OAuth via Notion |

#### Funcionalidades

- Criar, ler e atualizar páginas
- Gerenciar databases
- Buscar conteúdo
- Criar blocos e templates

#### Configuração

```json
{
  "notion": {
    "url": "https://mcp.notion.com/mcp"
  }
}
```

#### Casos de Uso

- Documentação de projetos
- Bases de conhecimento
- Task management
- Wiki colaborativo

#### Quando Usar

- Criar páginas de documentação automaticamente
- Sincronizar informações entre Claude e Notion
- Gerenciar projetos e tarefas
- Manter registros estruturados

---

### 1.2 Supabase

**Backend-as-a-Service Integration**

| Atributo | Valor |
|----------|-------|
| **URL** | `https://mcp.supabase.com/mcp` |
| **Tipo** | Cloud API |
| **Autenticação** | API Key |

#### Funcionalidades

- Operações CRUD em databases
- Autenticação de usuários
- Storage de arquivos
- Realtime subscriptions
- Edge Functions

#### Configuração

```json
{
  "supabase": {
    "url": "https://mcp.supabase.com/mcp"
  }
}
```

#### Casos de Uso

- Backend para aplicações web
- Autenticação OAuth
- Storage de mídia
- APIs RESTful

#### Quando Usar

- Criar tabelas e schemas
- Executar queries SQL
- Gerenciar autenticação
- Upload/download de arquivos

---

### 1.3 Figma Desktop

**Design Tool Integration**

| Atributo | Valor |
|----------|-------|
| **URL** | `http://127.0.0.1:3845/mcp` |
| **Tipo** | Local Service |
| **Requisito** | Figma Desktop rodando |

#### Funcionalidades

- Acessar design files
- Extrair componentes
- Obter design tokens
- Exportar assets

#### Configuração

```json
{
  "figma-desktop": {
    "url": "http://127.0.0.1:3845/mcp"
  }
}
```

#### Pré-requisitos

1. Figma Desktop instalado
2. Plugin MCP habilitado no Figma
3. Figma Desktop em execução

#### Casos de Uso

- Extrair cores e tipografia
- Gerar código CSS de componentes
- Documentar design system
- Sincronizar design com código

#### Quando Usar

- Implementar designs do Figma em código
- Extrair especificações de design
- Gerar documentação de componentes
- Validar implementação vs design

---

### 1.4 shadcn/ui

**Component Library Integration**

| Atributo | Valor |
|----------|-------|
| **Command** | `npx shadcn@latest mcp` |
| **Tipo** | NPX Package |
| **Framework** | React + Tailwind |

#### Funcionalidades

- Listar componentes disponíveis
- Adicionar componentes ao projeto
- Configurar themes
- Customizar variantes

#### Configuração

```json
{
  "shadcn": {
    "command": "npx",
    "args": ["shadcn@latest", "mcp"]
  }
}
```

#### Componentes Disponíveis

- Accordion, Alert, Avatar
- Button, Card, Checkbox
- Dialog, Dropdown, Form
- Input, Label, Modal
- Select, Tabs, Table
- Toast, Tooltip
- E muitos outros...

#### Casos de Uso

- Adicionar componentes UI rapidamente
- Configurar design system
- Customizar temas
- Scaffold de interfaces

#### Quando Usar

- Criar interfaces React com Tailwind
- Adicionar componentes pré-estilizados
- Implementar design systems
- Prototipar rapidamente

---

### 1.5 Context7 (Upstash)

**Expanded Context Management**

| Atributo | Valor |
|----------|-------|
| **Command** | `npx -y @upstash/context7-mcp` |
| **Tipo** | NPX Package |
| **Provider** | Upstash |

#### Funcionalidades

- Memória persistente entre sessões
- Contexto expandido
- Cache de informações
- Busca semântica

#### Configuração

```json
{
  "context7": {
    "command": "npx",
    "args": ["-y", "@upstash/context7-mcp"]
  }
}
```

#### Casos de Uso

- Manter contexto de projetos longos
- Armazenar decisões e padrões
- Cache de informações frequentes
- Memória de longo prazo

#### Quando Usar

- Projetos com múltiplas sessões
- Informações que precisam persistir
- Referências frequentes
- Histórico de decisões

---

### 1.6 Vercel

**Deployment Platform Integration**

| Atributo | Valor |
|----------|-------|
| **URL** | `https://mcp.vercel.com` |
| **Tipo** | Cloud API |
| **Autenticação** | OAuth via Vercel |

#### Funcionalidades

- Deploy de projetos
- Gerenciar domains
- Environment variables
- Logs e analytics
- Preview deployments

#### Configuração

```json
{
  "vercel": {
    "url": "https://mcp.vercel.com"
  }
}
```

#### Casos de Uso

- Deploy automático
- Configurar environment variables
- Gerenciar domínios
- Monitorar deployments

#### Quando Usar

- Fazer deploy de aplicações
- Configurar ambientes (dev/staging/prod)
- Verificar status de deployments
- Gerenciar infraestrutura

---

## 2. Built-in MCPs

MCPs habilitados via `settings.json`, já integrados ao Claude Code.

---

### 2.1 markitdown

**Document Conversion**

| Atributo | Valor |
|----------|-------|
| **Tipo** | Built-in |
| **Habilitação** | settings.json |

#### Funcionalidades

- Converter documentos para Markdown
- Suporte a PDF, DOCX, XLSX, PPTX
- Extração de texto
- Preservação de estrutura

#### Formatos Suportados

| Formato | Extensões |
|---------|-----------|
| Microsoft Office | .docx, .xlsx, .pptx |
| PDF | .pdf |
| Images | .png, .jpg (com OCR) |
| HTML | .html, .htm |

#### Casos de Uso

- Converter documentos para edição
- Extrair conteúdo de PDFs
- Importar documentos para análise
- Transformar formatos

#### Quando Usar

- Ler documentos Office
- Analisar PDFs
- Converter para formato editável
- Extrair texto de documentos

---

### 2.2 memory

**Persistent Memory**

| Atributo | Valor |
|----------|-------|
| **Tipo** | Built-in |
| **Habilitação** | settings.json |

#### Funcionalidades

- Armazenar informações persistentes
- Recuperar dados entre sessões
- Indexar por categorias
- Busca por keywords

#### Operações

```
save_memory(key, value)   # Salvar
get_memory(key)           # Recuperar
list_memories()           # Listar
delete_memory(key)        # Deletar
search_memories(query)    # Buscar
```

#### Casos de Uso

- Preferências do usuário
- Decisões de projeto
- Padrões recorrentes
- Referências importantes

#### Quando Usar

- Informações que devem persistir
- Preferências e configurações
- Histórico de decisões
- Contexto de longo prazo

---

### 2.3 filesystem

**File System Access**

| Atributo | Valor |
|----------|-------|
| **Tipo** | Built-in |
| **Habilitação** | settings.json |

#### Funcionalidades

- Ler arquivos e diretórios
- Criar e editar arquivos
- Navegar estrutura de pastas
- Operações de arquivo

#### Operações

```
read_file(path)           # Ler arquivo
write_file(path, content) # Escrever
list_directory(path)      # Listar diretório
create_directory(path)    # Criar pasta
delete_file(path)         # Deletar
move_file(from, to)       # Mover
```

#### Casos de Uso

- Manipulação de arquivos
- Navegação de projetos
- Criação de estruturas
- Backup e organização

#### Quando Usar

- Operações de arquivo avançadas
- Navegação de estruturas
- Criação de scaffolds
- Gerenciamento de assets

---

### 2.4 github

**GitHub Integration**

| Atributo | Valor |
|----------|-------|
| **Tipo** | Built-in |
| **Habilitação** | settings.json |

#### Funcionalidades

- Clonar repositórios
- Criar issues e PRs
- Gerenciar branches
- Code review
- Actions e workflows

#### Operações

```
clone_repo(url)           # Clonar
create_issue(title, body) # Criar issue
create_pr(title, body)    # Criar PR
list_branches()           # Listar branches
get_file(path)            # Obter arquivo
```

#### Casos de Uso

- Gerenciamento de repositórios
- Code review automatizado
- Issue tracking
- CI/CD integration

#### Quando Usar

- Operações Git avançadas
- Gerenciar issues e PRs
- Automatizar workflows
- Integrar com GitHub Actions

---

### 2.5 fetch

**HTTP Requests**

| Atributo | Valor |
|----------|-------|
| **Tipo** | Built-in |
| **Habilitação** | settings.json |

#### Funcionalidades

- Fazer requisições HTTP
- GET, POST, PUT, DELETE
- Headers customizados
- Parse de JSON

#### Operações

```
fetch(url)                         # GET simples
fetch(url, {method: 'POST', body}) # POST com body
fetch(url, {headers: {...}})       # Com headers
```

#### Casos de Uso

- Consumir APIs
- Web scraping básico
- Testes de endpoints
- Integração com serviços

#### Quando Usar

- Acessar APIs REST
- Verificar endpoints
- Obter dados externos
- Testar integrações

---

### 2.6 context7

**Context Enhancement**

| Atributo | Valor |
|----------|-------|
| **Tipo** | Built-in |
| **Habilitação** | settings.json |

#### Funcionalidades

- Expandir contexto de conversação
- Manter referências
- Indexar informações
- Busca semântica

#### Casos de Uso

- Projetos longos
- Múltiplas sessões
- Referências frequentes
- Continuidade de trabalho

---

## 3. Custom MCPs

MCPs desenvolvidos localmente.

---

### 3.1 obsidian-docs

**Obsidian Documentation Server**

| Atributo | Valor |
|----------|-------|
| **Tipo** | Custom Node.js |
| **Transport** | StdIO |
| **Localização** | `MCPs/obsidian-docs/` |
| **Autor** | Matheus Allvarenga |

#### Arquitetura

```
MCPs/obsidian-docs/
├── index.js          # Server principal (382 linhas)
├── package.json      # Dependências
├── SETUP.md          # Guia de instalação
├── EXAMPLES.md       # Exemplos de uso
├── SUMMARY.md        # Resumo de integração
└── node_modules/     # Dependências instaladas
```

#### Dependências

```json
{
  "dependencies": {
    "@modelcontextprotocol/sdk": "^1.0.0"
  }
}
```

#### Tools Disponíveis (3)

| Tool | Descrição | Parâmetros |
|------|-----------|------------|
| `search_obsidian_docs` | Buscar na documentação oficial | query, category (Plugins/Themes/Reference/All) |
| `get_obsidian_syntax_reference` | Referência de sintaxe completa | syntax_type (links/embeds/callouts/properties/tags/all) |
| `get_plugin_documentation` | Documentação de plugins | topic |

#### Resources Disponíveis (2)

| URI | Descrição |
|-----|-----------|
| `obsidian://docs/home` | Página inicial da documentação |
| `obsidian://docs/syntax` | Referência completa de sintaxe |

#### Sintaxe Suportada

**Links Internos**
```markdown
[[Note Name]]                    # Wikilink básico
[[Note Name|Display Text]]       # Texto customizado
[[Note Name#Heading]]            # Link para heading
[[Note Name#^block-id]]          # Link para bloco
```

**Embedding**
```markdown
![[Note Name]]                   # Embed nota inteira
![[Note Name#Heading]]           # Embed heading específico
![[image.png]]                   # Embed imagem
![[image.png|200]]               # Redimensionar (200px)
![[document.pdf#page=3]]         # PDF página específica
```

**Callouts**
```markdown
> [!note] Título Opcional
> Conteúdo com **markdown** e [[links]]

> [!warning]- Collapsed por padrão
> Conteúdo oculto

> [!tip]+ Expandido por padrão
> Conteúdo visível
```

**Tipos de Callout:** note, abstract, info, todo, tip, success, question, warning, failure, danger, bug, example, quote

**Properties (Frontmatter)**
```yaml
---
title: Note Title
tags: [tag1, tag2]
aliases: [Alias 1, Alias 2]
created: 2024-01-15
status: in-progress
---
```

**Tags**
```markdown
#tag                    # Tag inline
#parent/child           # Tag hierárquica
#parent/child/grandchild # Nested tag
```

#### Instalação

```bash
# 1. Clonar documentação
cd /tmp/claude
git clone --depth 1 https://github.com/obsidianmd/obsidian-developer-docs.git obsidian-docs

# 2. Instalar dependências
cd /Users/matheusallvarenga/Desktop/itm-dev/claude-code/MCPs/obsidian-docs
npm install

# 3. Testar servidor
node index.js
# Ctrl+C para sair

# 4. Configurar no Claude Code
# Adicionar em ~/.claude/mcp.json ou settings.json
```

#### Configuração

```json
{
  "obsidian-docs": {
    "command": "node",
    "args": [
      "/Users/matheusallvarenga/Desktop/itm-dev/claude-code/MCPs/obsidian-docs/index.js"
    ]
  }
}
```

#### Quando Usar

- Buscar sintaxe específica do Obsidian
- Desenvolvimento de plugins
- Verificar API do Obsidian
- Obter exemplos de código

---

## 4. Development MCPs

MCPs para desenvolvimento e debugging.

---

### 4.1 Google Genkit

**AI Development Framework**

| Atributo | Valor |
|----------|-------|
| **Command** | `genkit mcp --no-update-notification` |
| **Tipo** | CLI Tool |
| **Framework** | Google Genkit |

#### Funcionalidades

- Desenvolvimento de flows AI
- Testing de prompts
- Debugging de chains
- Observabilidade

#### Configuração

```json
{
  "genkit": {
    "command": "genkit",
    "args": ["mcp", "--no-update-notification"]
  }
}
```

#### Localização

```
/Users/matheusallvarenga/Desktop/itm-dev/Google-Code/genkit-intro/my-genkit-app/
├── .cursor/mcp.json
└── .gemini/settings.json
```

#### Casos de Uso

- Desenvolver com Google AI
- Testar flows de LLM
- Debug de aplicações AI
- Observability de chains

---

## Guia de Implementação

### Passo 1: Verificar Configuração Atual

```bash
# Ver MCPs configurados
cat ~/.claude/mcp.json

# Ver MCPs habilitados
cat ~/.claude/settings.json | grep -A 10 "enabledMcpjsonServers"
```

### Passo 2: Adicionar Novo MCP

**Para Cloud API:**
```json
// Em ~/.claude/mcp.json
{
  "mcpServers": {
    "novo-mcp": {
      "url": "https://api.exemplo.com/mcp"
    }
  }
}
```

**Para NPX Package:**
```json
{
  "mcpServers": {
    "novo-mcp": {
      "command": "npx",
      "args": ["-y", "package-name"]
    }
  }
}
```

**Para Custom Local:**
```json
{
  "mcpServers": {
    "novo-mcp": {
      "command": "node",
      "args": ["/path/to/index.js"]
    }
  }
}
```

### Passo 3: Habilitar Built-in MCP

```json
// Em ~/.claude/settings.json
{
  "enabledMcpjsonServers": [
    "markitdown",
    "memory",
    "filesystem",
    "context7",
    "github",
    "fetch",
    "novo-mcp"  // Adicionar aqui
  ]
}
```

### Passo 4: Reiniciar Claude Code

```bash
# Fechar completamente e reabrir
# Ou usar comando de reload se disponível
```

### Passo 5: Verificar Funcionamento

```
Liste os MCP tools disponíveis
```

---

## Troubleshooting

### Erro: MCP não aparece

1. Verificar path absoluto no config
2. Verificar se `enableAllProjectMcpServers: true`
3. Reiniciar Claude Code completamente
4. Verificar logs de erro

### Erro: Cannot find module

```bash
cd /path/to/mcp
rm -rf node_modules package-lock.json
npm install
```

### Erro: ENOENT (arquivo não encontrado)

- Verificar se o path está correto
- Usar paths absolutos, não relativos
- Verificar permissões do arquivo

### Erro: Connection refused (localhost)

- Verificar se o serviço local está rodando
- Verificar a porta correta
- Verificar firewall

### Debug Mode

```bash
# Testar MCP manualmente
node /path/to/mcp/index.js

# Ver output de erro
# Ctrl+C para sair
```

---

## Configuração Completa Atual

### ~/.claude/mcp.json

```json
{
  "mcpServers": {
    "notion": {
      "url": "https://mcp.notion.com/mcp"
    },
    "supabase": {
      "url": "https://mcp.supabase.com/mcp"
    },
    "figma-desktop": {
      "url": "http://127.0.0.1:3845/mcp"
    },
    "shadcn": {
      "command": "npx",
      "args": ["shadcn@latest", "mcp"]
    },
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    },
    "vercel": {
      "url": "https://mcp.vercel.com"
    }
  }
}
```

### ~/.claude/settings.json

```json
{
  "enableAllProjectMcpServers": true,
  "enabledMcpjsonServers": [
    "markitdown",
    "memory",
    "filesystem",
    "context7",
    "github",
    "fetch"
  ]
}
```

---

## Matriz de Decisão

### Qual MCP Usar?

| Necessidade | MCP Recomendado | Tipo |
|-------------|-----------------|------|
| Documentação/Wiki | Notion | Cloud |
| Backend/Database | Supabase | Cloud |
| Design/UI | Figma Desktop | Local |
| Componentes React | shadcn | NPX |
| Deploy | Vercel | Cloud |
| Contexto persistente | memory, context7 | Built-in |
| Arquivos | filesystem | Built-in |
| GitHub | github | Built-in |
| APIs externas | fetch | Built-in |
| Converter docs | markitdown | Built-in |
| Obsidian docs | obsidian-docs | Custom |

---

## Changelog

| Versão | Data | Alterações |
|--------|------|------------|
| 1.0 | 2025-12-23 | Documentação inicial de 14 MCPs |

---

*Documento gerado automaticamente. Para atualizações, edite a configuração em `.claude/mcp.json` e `.claude/settings.json`*
