# Guia de Configuração - Obsidian Docs MCP Server

## Pré-requisitos

- Node.js instalado
- Claude Code instalado
- Documentação do Obsidian clonada em `/tmp/claude/obsidian-docs`

## Passo 1: Verificar Documentação

```bash
ls -la /tmp/claude/obsidian-docs/en
```

Se não existir, clonar:
```bash
cd /tmp/claude
git clone --depth 1 https://github.com/obsidianmd/obsidian-developer-docs.git obsidian-docs
```

## Passo 2: Instalar Dependências

```bash
cd ~/Desktop/Dev-Tools-Projects/ClaudeCode/MCP-Servers/obsidian-docs
npm install
```

## Passo 3: Testar o Servidor

Teste manual (deve esperar entrada stdin):
```bash
node index.js
```

Se funcionar, pressione Ctrl+C para sair.

## Passo 4: Configurar no Claude Code

Editar `~/.claude/claude_desktop_config.json`:

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

**IMPORTANTE:** Se já existir outros servidores MCP, adicione apenas a entrada `"obsidian-docs"` dentro de `"mcpServers"`.

## Passo 5: Reiniciar Claude Code

1. Fechar completamente o Claude Code
2. Reabrir
3. Verificar logs em caso de erro

## Passo 6: Testar no Claude Code

Abrir uma nova conversa e testar:

```
Liste os MCP tools disponíveis relacionados ao Obsidian
```

Você deve ver:
- `search_obsidian_docs`
- `get_obsidian_syntax_reference`
- `get_plugin_documentation`

## Testes de Funcionalidade

### Teste 1: Buscar documentação
```
Use o tool search_obsidian_docs para buscar informações sobre "callouts"
```

### Teste 2: Referência de sintaxe
```
Use o tool get_obsidian_syntax_reference para obter a referência completa de "embeds"
```

### Teste 3: Documentação de plugins
```
Use o tool get_plugin_documentation para o tópico "commands"
```

## Troubleshooting

### Erro: "Cannot find module @modelcontextprotocol/sdk"
```bash
cd ~/Desktop/Dev-Tools-Projects/ClaudeCode/MCP-Servers/obsidian-docs
rm -rf node_modules package-lock.json
npm install
```

### Erro: "ENOENT: no such file or directory '/tmp/claude/obsidian-docs'"
```bash
cd /tmp/claude
git clone --depth 1 https://github.com/obsidianmd/obsidian-developer-docs.git obsidian-docs
```

### MCP Server não aparece no Claude Code
1. Verificar se o caminho no config está correto (absoluto, não relativo)
2. Verificar logs do Claude Code
3. Reiniciar completamente o Claude Code
4. Verificar se o arquivo `index.js` tem permissão de execução

### Permissões
```bash
chmod +x ~/Desktop/Dev-Tools-Projects/ClaudeCode/MCP-Servers/obsidian-docs/index.js
```

## Verificação Final

Após configurar tudo, você terá:

1. ✅ **Comando `/obsidian`** - Conhecimento estático expandido com toda sintaxe oficial
2. ✅ **MCP Server** - Busca dinâmica na documentação oficial
3. ✅ **Documentação local** - Clone do repositório oficial

## Comparação: Comando vs MCP Server

| Recurso | `/obsidian` Command | MCP Server |
|---------|---------------------|------------|
| Velocidade | Instantâneo | Requer busca |
| Conteúdo | Sintaxe + Best Practices | Documentação completa |
| Atualização | Manual (editar .md) | Automática (git pull) |
| Uso | Workflow geral | Dúvidas específicas |

## Quando Usar Cada Um

**Use `/obsidian`:**
- Criar notas rapidamente
- Aplicar convenções do Obsidian
- Workflow diário

**Use MCP Server:**
- Buscar detalhes específicos da API
- Desenvolvimento de plugins
- Verificar sintaxes obscuras
- Obter exemplos de código

## Atualizar Documentação

Para manter a documentação atualizada:
```bash
cd /tmp/claude/obsidian-docs
git pull origin master
```

Recomendado: atualizar mensalmente ou quando houver updates importantes do Obsidian.
