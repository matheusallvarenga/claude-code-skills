# Troubleshooting - ITM Audit System

## Problemas Comuns

### 1. Varredura Interrompida

**Sintoma:** Scan para antes de completar

**Causas Possíveis:**
- Timeout de sessão
- Erro de permissão em diretório específico
- Memória insuficiente

**Solução:**
```bash
# 1. Verificar último checkpoint
ls -la Projects/itm-audit/data/checkpoint_scan_*.json

# 2. Retomar do checkpoint
# O sistema detecta automaticamente e pergunta se deseja continuar
```

**Prevenção:**
- Usar batches menores para volumes grandes
- Monitorar uso de memória
- Executar em horários de baixa atividade

---

### 2. Erro de Permissão

**Sintoma:** `Permission denied` em arquivos/diretórios

**Diagnóstico:**
```bash
# Identificar arquivos problemáticos
find /path/to/source -type f ! -readable 2>/dev/null
```

**Solução:**
- O sistema automaticamente faz skip e loga
- Verificar log em `audit-reports/errors.log`
- Arquivos inacessíveis são listados separadamente no relatório

---

### 3. Hash Collision Suspeito

**Sintoma:** Arquivos diferentes marcados como duplicatas

**Probabilidade:** < 0.001% com algoritmo chunk+size

**Verificação:**
```python
# Comparação byte-a-byte para confirmação
def verificar_duplicata_real(file1, file2):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        return f1.read() == f2.read()
```

**Solução:**
- Executar verificação completa no grupo suspeito
- Flag `--verify-full` para modo paranóico

---

### 4. Relatório Incompleto

**Sintoma:** Seções faltando no relatório final

**Causas:**
- Fase anterior não completou
- Dados corrompidos no JSON intermediário

**Diagnóstico:**
```bash
# Verificar integridade dos JSONs
python -m json.tool data/scan_results.json > /dev/null
python -m json.tool data/hash_index.json > /dev/null
```

**Solução:**
- Re-executar fase com problema
- Usar checkpoint mais recente válido

---

### 5. Performance Degradada

**Sintoma:** Processamento muito lento

**Benchmarks Esperados:**
| Volume | Scan | Hash | Total |
|--------|------|------|-------|
| 10K arquivos | ~2 min | ~5 min | ~10 min |
| 50K arquivos | ~10 min | ~25 min | ~45 min |
| 100K arquivos | ~20 min | ~50 min | ~90 min |

**Otimizações:**
1. Excluir diretórios conhecidos (node_modules, .git, caches)
2. Processar por partições
3. Usar SSD para dados temporários
4. Aumentar batch size se memória disponível

---

### 6. Encoding de Nomes de Arquivo

**Sintoma:** Caracteres estranhos em paths

**Causa:** Arquivos com encoding não-UTF8

**Solução:**
```python
# O sistema usa errors='surrogateescape' por padrão
path.encode('utf-8', errors='surrogateescape')
```

**Se persistir:**
- Arquivos são listados com path hexadecimal
- Recomendação: Renomear arquivos problemáticos

---

### 7. Espaço em Disco Insuficiente

**Sintoma:** Erro ao salvar resultados

**Espaço Necessário (estimativa):**
- ~1KB por 100 arquivos para metadados
- ~50MB para 100K arquivos completo

**Solução:**
- Limpar checkpoints antigos
- Mover audit-reports para storage com espaço
- Usar compressão nos JSONs intermediários

---

## Logs e Diagnóstico

### Localização dos Logs
```
Projects/itm-audit/
├── data/
│   ├── audit.log          # Log principal
│   ├── errors.log         # Apenas erros
│   └── performance.log    # Métricas de tempo
```

### Níveis de Log
| Nível | Uso |
|-------|-----|
| DEBUG | Desenvolvimento/troubleshooting |
| INFO | Operação normal |
| WARNING | Situações recuperáveis |
| ERROR | Falhas que requerem atenção |

### Ativar Debug
```python
# No início da execução
import logging
logging.getLogger('itm_audit').setLevel(logging.DEBUG)
```

---

## Recuperação de Desastres

### Backup dos Dados de Auditoria
```bash
# Criar snapshot antes de operações arriscadas
tar -czf audit_backup_$(date +%Y%m%d).tar.gz Projects/itm-audit/data/
```

### Restaurar de Checkpoint
```python
# O sistema oferece opção automática
# Ou manualmente:
from scripts.scanner import Scanner
scanner = Scanner()
scanner.load_checkpoint('checkpoint_scan_20241229.json')
scanner.resume()
```

---

## Contato e Suporte

Para problemas não listados:
1. Verificar `errors.log` completo
2. Capturar estado do sistema (memória, disco, processos)
3. Documentar passos para reproduzir
4. Consultar documentação de algoritmos para entender comportamento esperado
