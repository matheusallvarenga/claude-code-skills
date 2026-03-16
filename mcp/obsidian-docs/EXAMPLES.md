# Exemplos de Uso - Obsidian Integration

Este documento mostra exemplos práticos de como usar o comando `/obsidian` e o MCP Server.

## Exemplo 1: Criar uma Nota de Reunião

### Com `/obsidian`

**Prompt:**
```
/obsidian

Crie uma nota de reunião sobre planejamento de sprint
```

**Resultado esperado:**
```markdown
---
title: Reunião - Planejamento Sprint
created: 2025-11-05
tags: [reunião, sprint, planejamento]
type: meeting
status: completed
---

# Reunião - Planejamento Sprint

## Participantes
- [[Nome 1]]
- [[Nome 2]]

## Tópicos Discutidos

### Sprint Goals
- [ ] [[Goal 1]]
- [ ] [[Goal 2]]

## Action Items
- [ ] [[Task 1]] - Responsável: [[Nome]]
- [ ] [[Task 2]] - Responsável: [[Nome]]

## Links Relacionados
- [[Sprint Anterior]]
- [[Backlog]]
- [[Roadmap]]

## Observações
%%Adicionar notas privadas aqui%%
```

## Exemplo 2: Criar Sistema Zettelkasten

### Com `/obsidian`

**Prompt:**
```
/obsidian

Crie uma nota permanente sobre o conceito de "Flow State" seguindo Zettelkasten
```

**Resultado esperado:**
```markdown
---
title: Flow State
created: 2025-11-05
tags: [zettelkasten, psicologia, produtividade]
type: permanent-note
id: 202511050001
aliases: [Estado de Fluxo, Fluxo]
---

# Flow State

Estado mental de completa imersão e foco em uma atividade.

## Conceito Principal
O flow state ocorre quando [[Desafio]] e [[Habilidade]] estão balanceados em nível alto.

## Características
- Perda da noção de tempo
- Foco total na tarefa
- Sensação de controle
- Feedback imediato

## Conexões
- Relacionado a [[Deep Work]]
- Oposto de [[Distração]]
- Requer [[Ambiente sem Interrupções]]
- Facilita [[Aprendizado]]

## Fontes
- [[Mihaly Csikszentmihalyi - Flow]]
- [[Cal Newport - Deep Work]]

## Notas Relacionadas
- [[Como Entrar em Flow]]
- [[Bloqueios ao Flow]]
- [[Medindo Produtividade]]

^202511050001
```

## Exemplo 3: Buscar Sintaxe Específica

### Com MCP Server

**Prompt:**
```
Use o MCP tool get_obsidian_syntax_reference para mostrar a sintaxe completa de callouts
```

**Resultado esperado:**
```markdown
# Callouts
> [!note] Optional Title
> Content with **markdown** and [[links]]

Types: note, abstract, info, todo, tip, success, question, warning, failure, danger, bug, example, quote
Modifiers: [!note]- (collapsed) or [!note]+ (expanded)
```

## Exemplo 4: Criar Template de Daily Note

### Com `/obsidian`

**Prompt:**
```
/obsidian

Crie um template para daily notes com seções para tarefas, notas e reflexões
```

**Resultado esperado:**
```markdown
---
created: {{date}}
tags: [daily-note]
type: daily
---

# {{date:YYYY-MM-DD}} - {{date:dddd}}

## 🎯 Objetivos do Dia
- [ ]
- [ ]
- [ ]

## 📝 Notas Rápidas


## 🔗 Links Importantes
- [[Projeto em Andamento]]
-

## ✅ Tarefas Concluídas
- [x]

## 💭 Reflexões
> [!note] O que aprendi hoje?
>

> [!tip] Melhorias para amanhã
>

## 📊 Métricas
- Pomodoros:
- Energia: ⭐⭐⭐⭐⭐
- Foco: ⭐⭐⭐⭐⭐

---
[[{{date-1d:YYYY-MM-DD}}|← Ontem]] | [[{{date+1d:YYYY-MM-DD}}|Amanhã →]]
```

## Exemplo 5: Pesquisar Documentação de Plugins

### Com MCP Server

**Prompt:**
```
Use search_obsidian_docs para buscar informações sobre "ribbon actions" na categoria "Plugins"
```

**Uso:** Quando você está desenvolvendo um plugin e precisa saber como adicionar ícones na ribbon.

## Exemplo 6: Criar Estrutura MOC (Map of Content)

### Com `/obsidian`

**Prompt:**
```
/obsidian

Crie um MOC sobre "Desenvolvimento de Software"
```

**Resultado esperado:**
```markdown
---
title: MOC - Desenvolvimento de Software
tags: [moc, desenvolvimento, software]
type: moc
created: 2025-11-05
---

# 🗺️ MOC - Desenvolvimento de Software

Mapa de conteúdo organizando conhecimento sobre desenvolvimento de software.

## 📚 Fundamentos
- [[Algoritmos]]
- [[Estruturas de Dados]]
- [[Paradigmas de Programação]]
- [[Design Patterns]]

## 🛠️ Práticas
- [[Clean Code]]
- [[TDD - Test Driven Development]]
- [[Refactoring]]
- [[Code Review]]

## 🏗️ Arquitetura
- [[Arquitetura de Software]]
- [[Microservices]]
- [[Design Patterns Arquiteturais]]
- [[API Design]]

## 🔧 Ferramentas
- [[Git]]
- [[Docker]]
- [[CI-CD]]
- [[IDE Setup]]

## 📖 Projetos
- [[Projeto A]]
- [[Projeto B]]

## 🌱 Áreas para Aprofundar
- [ ] [[Performance Optimization]]
- [ ] [[Security Best Practices]]
- [ ] [[Scalability Patterns]]

## 🔗 MOCs Relacionados
- [[MOC - DevOps]]
- [[MOC - Computer Science]]
- [[MOC - Career Development]]
```

## Exemplo 7: Callout Complexo com Nesting

### Com `/obsidian`

**Prompt:**
```
/obsidian

Crie uma nota explicando recursão com callouts aninhados
```

**Resultado esperado:**
```markdown
---
title: Recursão
tags: [programação, algoritmos, conceito]
---

# Recursão

> [!abstract] Definição
> Técnica onde uma função chama a si mesma para resolver problemas.

> [!example] Exemplo Clássico - Fatorial
>
> ```python
> def fatorial(n):
>     if n <= 1:
>         return 1
>     return n * fatorial(n - 1)
> ```
>
> > [!tip] Como Funciona
> > Para calcular fatorial(5):
> > - 5 * fatorial(4)
> >   - 4 * fatorial(3)
> >     - 3 * fatorial(2)
> >       - 2 * fatorial(1)
> >         - retorna 1
>
> > [!warning] Cuidado
> > Sem caso base → Stack Overflow!

> [!todo] Exercícios
> - [ ] Implementar Fibonacci recursivo
> - [ ] Converter para iterativo
> - [ ] Comparar performance

## Links
- [[Stack e Heap]]
- [[Complexidade de Algoritmos]]
- [[Dynamic Programming]]
```

## Exemplo 8: Criar Canvas para Brainstorming

### Com `/obsidian`

**Prompt:**
```
/obsidian

Descreva como criar um canvas para brainstorming de features de um app
```

**Orientação fornecida:**
```markdown
# Canvas para Brainstorming

1. Criar arquivo `.canvas` no vault
2. Adicionar cards:
   - **Text cards**: Ideias iniciais
   - **File cards**: Links para [[Requisitos]], [[User Stories]]
   - **Link cards**: Referências externas

3. Estrutura sugerida:
```json
{
  "nodes": [
    {
      "id": "feature-1",
      "type": "text",
      "text": "# Feature: Login Social\n\n- Google\n- GitHub\n- Apple",
      "x": 0,
      "y": 0,
      "width": 250,
      "height": 200,
      "color": "1"
    },
    {
      "id": "requisitos",
      "type": "file",
      "file": "Docs/Requisitos.md",
      "x": 300,
      "y": 0,
      "width": 400,
      "height": 300
    }
  ],
  "edges": [
    {
      "id": "edge1",
      "fromNode": "feature-1",
      "toNode": "requisitos",
      "label": "implementa"
    }
  ]
}
```

4. Cores para categorias:
   - Azul (1): Features principais
   - Verde (2): Features secundárias
   - Amarelo (3): Nice to have
   - Vermelho (4): Bloqueadores

## Exemplo 9: Comparação - Command vs MCP

### Cenário: Dúvida sobre Block References

**Com `/obsidian` command:**
- Resposta instantânea com sintaxe básica
- Exemplo prático imediato
- Sem necessidade de busca

**Com MCP Server:**
```
Use search_obsidian_docs para buscar "block reference" na documentação
```
- Retorna documentação oficial completa
- Exemplos mais detalhados
- Casos de uso avançados

### Conclusão
Use `/obsidian` para 95% dos casos. Use MCP Server quando precisar:
- Detalhes técnicos específicos
- Desenvolvimento de plugins
- Edge cases complexos

## Exemplo 10: Workflow Completo

### Criar Sistema de Gestão de Conhecimento

**Passo 1:** Ativar modo Obsidian
```
/obsidian
```

**Passo 2:** Criar estrutura base
```
Crie uma estrutura inicial para um segundo cérebro digital incluindo:
- MOC principal
- Índices por área
- Templates básicos
```

**Passo 3:** Popular com conteúdo inicial usando convenções aprendidas

**Resultado:** Sistema completo seguindo best practices oficiais do Obsidian.
