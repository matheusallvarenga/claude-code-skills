# Export Session

Exporta summary da conversa atual, decisões e learnings para arquivo permanente.

---

## Propósito

Preservar contexto da sessão antes de encerrar, criando registro permanente em:
```
Sessions/YYYY/MM-Month/YYYY-MM-DD/session-summary.md
```

---

## Quando Usar

- **Fim de sessão importante** (antes de fechar Claude)
- **Após decisões críticas**
- **Ao completar projeto/feature**
- **Antes de trocar de contexto**

**Frequência recomendada**: Fim de toda sessão FULL

---

## Como Funciona

Ao receber `/export-session`:

### 1. Coletar Informações da Sessão

Analise toda a conversa atual e extraia:
- Data e hora da sessão
- Tipo de sessão (FULL/QUICK/LEARNING)
- Tópicos principais discutidos
- Decisões tomadas (com contexto)
- Problemas resolvidos
- Learnings capturados
- Artefatos criados (arquivos, códigos)
- Next steps identificados

### 2. Gerar Session Summary

Criar arquivo estruturado:

```markdown
# Session Summary - [DATE]

**Type**: [FULL/QUICK/LEARNING]
**Duration**: [START - END]
**Focus**: [Tópico principal]

---

## 📋 Overview

[Resumo em 2-3 parágrafos do que foi feito]

---

## 🎯 Objectives

- [ ] Objetivo 1 [✅ Done / ⏳ In Progress / ❌ Not Started]
- [ ] Objetivo 2
- [ ] Objetivo 3

---

## 🔑 Key Decisions

### Decision 1: [Título]
**Context**: [Por que surgiu]
**Decision**: [O que foi decidido]
**Rationale**: [Por que decidimos assim]
**Impact**: [Consequências esperadas]
**Date**: [YYYY-MM-DD HH:MM]

### Decision 2: [Título]
...

---

## 💡 Learnings

### Learning 1: [Tópico]
**Descoberta**: [O que aprendemos]
**Source**: [De onde veio - doc, teste, erro, etc]
**Application**: [Como usar no futuro]

### Learning 2: [Tópico]
...

---

## 🛠️ Artifacts Created

- `file/path/1.md` - [Descrição]
- `file/path/2.py` - [Descrição]
- Configuration X updated
- Script Y created

---

## ❌ Problems Solved

### Problem 1: [Descrição]
**Error/Issue**: [O que estava errado]
**Solution**: [Como resolvemos]
**Root Cause**: [Causa raiz]
**Prevention**: [Como evitar no futuro]

### Problem 2: [Descrição]
...

---

## 📊 Metrics

- Files created: [N]
- Files modified: [N]
- Commands executed: [N]
- Errors encountered: [N]
- Errors resolved: [N]

---

## ⏭️ Next Steps

1. [ ] [Ação 1] - [Prioridade: Alta/Média/Baixa]
2. [ ] [Ação 2]
3. [ ] [Ação 3]

**Next Session Focus**: [O que focar na próxima]

---

## 🔗 Related

- Previous session: [Link se houver]
- Related project: [Nome do projeto]
- Related learnings: [Links para Knowledge/]

---

## 📝 Raw Notes

[Qualquer nota adicional, pensamentos, ideias]

---

**Exported**: [YYYY-MM-DD HH:MM:SS]
**By**: Claude Code Export
```

### 3. Salvar Arquivo

**Localização**:
```
Sessions/YYYY/MM-Month/YYYY-MM-DD/session-summary.md
```

Se diretório não existir, criar automaticamente.

### 4. Confirmar Export

Após criar arquivo, responder:

```
✅ Session exported successfully!

📁 Location: Sessions/2025/10-October/2025-10-29/session-summary.md
📊 Stats:
    - Decisions captured: [N]
    - Learnings extracted: [N]
    - Problems solved: [N]
    - Artifacts created: [N]

💾 Safe to close this session.

🔗 Quick access:
    cat Sessions/2025/10-October/2025-10-29/session-summary.md
```

---

## Exemplo de Uso

```
> /export-session

[Claude analisa toda conversa]
[Gera session-summary.md]

✅ Session exported!
📁 Sessions/2025/10-October/2025-10-29/session-summary.md

Decisões: 5 | Learnings: 8 | Artefatos: 17

Pode fechar com segurança.
```

---

## Notas Importantes

1. **Executar ANTES de fechar Claude**
2. **Não substitui backup** - É complementar
3. **Review manual recomendado** - Ajustar summary se necessário
4. **Uma vez por sessão** - No fim ou após milestone importante
5. **Complementa /evaluate** - Export é mais amplo

---

## Diferença de /evaluate

| Feature | /evaluate | /export-session |
|---------|-----------|-----------------|
| Quando | Sexta (semanal) | Fim de sessão |
| Foco | KPIs + Truth sieve | Decisões + Context |
| Output | Checklist | Documento completo |
| Permanência | Efêmero | Arquivo permanente |

---

## Automação Futura

**Potencial hook** (Fase 2):
```json
{
  "hooks": {
    "SessionEnd": [{
      "command": "claude --export-session-auto"
    }]
  }
}
```

Mas por enquanto: **Manual, sob demanda.**

---

## Campos Opcionais

Se sessão foi QUICK (sem muita profundidade):
- Gerar versão simplificada
- Focar apenas em: Tópico + Artefatos + Next Steps
- Omitir seções vazias

Se sessão foi FULL:
- Gerar versão completa
- Incluir todas seções
- Máximo detalhe

Se sessão foi LEARNING:
- Enfatizar seção Learnings
- Incluir resources consultados
- Next steps = Próximos estudos

---

**Usage**: Sempre antes de fechar sessão importante!
