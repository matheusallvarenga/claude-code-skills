# Obsidian Docs MCP Server

MCP server para acesso dinâmico à documentação oficial do Obsidian.

## Funcionalidades

### Tools (Ferramentas)

1. **search_obsidian_docs**
   - Busca tópicos específicos na documentação oficial
   - Parâmetros:
     - `query`: Termo de busca
     - `category`: Categoria opcional (Plugins, Themes, Reference, All)

2. **get_obsidian_syntax_reference**
   - Retorna referência completa da sintaxe do Obsidian
   - Parâmetros:
     - `syntax_type`: Tipo de sintaxe (links, embeds, callouts, properties, tags, all)

3. **get_plugin_documentation**
   - Documentação detalhada para desenvolvimento de plugins
   - Parâmetros:
     - `topic`: Tópico de desenvolvimento

### Resources (Recursos)

- `obsidian://docs/home` - Página principal da documentação
- `obsidian://docs/syntax` - Referência completa de sintaxe

## Instalação

1. Instalar dependências:
```bash
cd ~/Desktop/Dev-Tools-Projects/ClaudeCode/MCP-Servers/obsidian-docs
npm install
```

2. Adicionar ao Claude Code config (`~/.claude/claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "obsidian-docs": {
      "command": "node",
      "args": [
        "~/.claude/mcps/obsidian-docs/index.js"
      ]
    }
  }
}
```

3. Reiniciar Claude Code

## Uso

O servidor acessa automaticamente a documentação clonada em `/tmp/claude/obsidian-docs/en`.

### Exemplos de uso no Claude Code:

**Buscar documentação:**
```
Use o MCP tool search_obsidian_docs com query "callouts"
```

**Obter referência de sintaxe:**
```
Use o MCP tool get_obsidian_syntax_reference com syntax_type "links"
```

**Documentação de plugins:**
```
Use o MCP tool get_plugin_documentation com topic "views"
```

## Estrutura

- `index.js` - Servidor MCP principal
- `package.json` - Configuração do projeto
- `README.md` - Esta documentação

## Fonte dos Dados

A documentação é obtida do repositório oficial:
https://github.com/obsidianmd/obsidian-developer-docs

## Integração com `/obsidian` Command

Este MCP server complementa o comando `/obsidian` expandido:
- **Comando `/obsidian`**: Contém conhecimento estático e completo da sintaxe
- **MCP Server**: Busca dinâmica na documentação oficial para casos específicos

## Licença

MIT
