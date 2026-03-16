# Session Type Switcher

Altere o modo de sessão durante execução.

---

## Modos Disponíveis

### 1. FULL MODE 🎯
**Quando usar**: Trabalho INTENTUM/QUANTUM IA, decisões importantes
**Configs ativas**:
- ✅ Instructions.md completo
- ✅ Context.md carregado
- ✅ Archetypal Council ativo
- ✅ Weekly ship tracking
- ✅ Token budget: 400 (complex)
- ✅ Slash commands: Todos

**Comportamento**:
- Respostas estruturadas (Clarity → Decision → Execution → Metric)
- Aplicar 80/20 filters
- Enforcement de weekly ship
- Truth over comfort

---

### 2. QUICK MODE ⚡
**Quando usar**: Debug rápido, testes, perguntas pontuais
**Configs ativas**:
- ❌ Sem instructions overhead
- ❌ Sem context
- ❌ Sem Council
- ❌ Sem tracking
- ✅ Token budget: 150 (minimal)
- ✅ Slash commands: Básicos apenas

**Comportamento**:
- Resposta direta
- Sem estrutura obrigatória
- Sem enforcement
- Code over explanation

---

### 3. LEARNING MODE 📚
**Quando usar**: Estudo, pesquisa, exploração de conceitos
**Configs ativas**:
- ✅ Context.md carregado (quem você é)
- ❌ Sem enforcement (ship/council)
- ❌ Sem tracking obrigatório
- ✅ Token budget: 600 (explanatory)
- ✅ Slash commands: Todos

**Comportamento**:
- Explicações detalhadas permitidas
- Foco em entendimento
- Múltiplos exemplos OK
- Sem pressão de ship

---

## Como Usar

```
/session-type
```

Responda com número do modo desejado (1, 2 ou 3).

---

## Protocolo de Troca

Ao receber `/session-type`:

1. **Mostrar seletor**:
```
╔═══════════════════════════════════════════════════════╗
║            Session Type Switcher                      ║
╚═══════════════════════════════════════════════════════╝

Modo atual: [FULL/QUICK/LEARNING]

Trocar para:
[1] 🎯 FULL    - Instructions + Context + Council
[2] ⚡ QUICK   - Minimal overhead, direct answers
[3] 📚 LEARNING - Exploratory, detailed explanations

Digite 1, 2 ou 3:
```

2. **Após escolha, confirmar**:
```
✅ Modo alterado para [FULL/QUICK/LEARNING]

Token budget ajustado: [150/400/600]
Enforcement: [ON/OFF]
Council: [Active/Inactive]

Pronto. Continue.
```

3. **Aplicar comportamento** correspondente nas próximas respostas

---

## Notas

- Troca afeta APENAS sessão atual
- Próxima sessão = volta ao padrão (definido no início)
- Pode trocar quantas vezes quiser
- Estado persiste até fim da sessão ou nova troca

---

**Uso recomendado**:
- Manhã = FULL (trabalho profundo)
- Tarde = QUICK (debug/testes)
- Noite = LEARNING (estudo/exploração)
