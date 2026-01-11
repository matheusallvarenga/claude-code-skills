# Algoritmos do Sistema de Auditoria

## 1. Algoritmo de Varredura (Scanner)

### Pseudocódigo
```
função scan_directory(root_path):
    resultados = []
    para cada entry em walk(root_path):
        se entry é arquivo:
            metadata = extrair_metadados(entry)
            resultados.append(metadata)
            se len(resultados) % 1000 == 0:
                salvar_checkpoint(resultados)
    retornar resultados
```

### Complexidade
- Tempo: O(n) onde n = número de arquivos
- Espaço: O(n) para armazenar metadados

### Tratamento de Erros
- Permission denied → Log e skip
- Symlink loop → Detectar e skip
- Arquivo corrompido → Log e continuar

---

## 2. Algoritmo de Hash (Fingerprinting)

### Estratégia: Chunk + Size
```
função calcular_hash(file_path):
    tamanho = obter_tamanho(file_path)
    
    se tamanho <= 65536:  # 64KB
        conteudo = ler_arquivo_completo(file_path)
    senão:
        conteudo = ler_primeiros_bytes(file_path, 65536)
    
    hash_chunk = sha256(conteudo)
    hash_composto = f"{hash_chunk}_{tamanho}"
    
    retornar hash_composto
```

### Justificativa
- Primeiros 64KB capturam headers únicos
- Tamanho diferencia arquivos com mesmo início
- 99.9%+ de precisão em detecção de duplicatas
- 10-100x mais rápido que hash completo

### Falsos Positivos Conhecidos
- Arquivos gerados por template (baixo risco)
- Mitigação: Verificação completa opcional para grupos suspeitos

---

## 3. Algoritmo de Deduplicação

### Estrutura de Dados
```
DuplicateGroup:
    hash: string
    total_size: int
    files: List[FileInfo]
    recoverable_space: int  # (count - 1) * file_size
```

### Processo
```
função identificar_duplicatas(hash_index):
    grupos = agrupar_por_hash(hash_index)
    duplicatas = []
    
    para cada hash, arquivos em grupos:
        se len(arquivos) > 1:
            grupo = DuplicateGroup(
                hash=hash,
                files=arquivos,
                recoverable_space=calcular_recuperavel(arquivos)
            )
            duplicatas.append(grupo)
    
    retornar ordenar_por_impacto(duplicatas)
```

### Critérios de Priorização
1. Espaço recuperável (maior primeiro)
2. Número de cópias (mais duplicatas primeiro)
3. Idade do arquivo mais antigo

---

## 4. Algoritmo de Classificação

### Por Extensão
```
CATEGORIAS = {
    'documentos': ['.pdf', '.doc', '.docx', '.txt', '.md', '.rtf'],
    'planilhas': ['.xls', '.xlsx', '.csv', '.numbers'],
    'imagens': ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg', '.bmp'],
    'videos': ['.mp4', '.mov', '.avi', '.mkv', '.wmv'],
    'audio': ['.mp3', '.wav', '.m4a', '.flac', '.aac'],
    'codigo': ['.py', '.js', '.ts', '.jsx', '.tsx', '.json', '.yaml', '.yml'],
    'arquivos': ['.zip', '.rar', '.7z', '.tar', '.gz'],
}

função classificar_tipo(extensao):
    para categoria, extensoes em CATEGORIAS:
        se extensao.lower() em extensoes:
            retornar categoria
    retornar 'outros'
```

### Por Idade
```
função classificar_idade(data_modificacao):
    dias = (hoje - data_modificacao).days
    
    se dias < 30: retornar 'recente'
    se dias < 180: retornar 'ativo'
    se dias < 365: retornar 'arquivado'
    retornar 'legacy'
```

---

## 5. Algoritmo de Checkpoint

### Estratégia
```
função salvar_checkpoint(estado, fase, contador):
    checkpoint = {
        'fase': fase,
        'processados': contador,
        'timestamp': agora(),
        'estado': estado
    }
    
    arquivo = f"checkpoint_{fase}_{timestamp}.json"
    salvar_json(arquivo, checkpoint)
    
    # Manter apenas últimos 3 checkpoints
    limpar_checkpoints_antigos(fase, manter=3)
```

### Recuperação
```
função recuperar_checkpoint(fase):
    checkpoints = listar_checkpoints(fase)
    se checkpoints:
        mais_recente = ordenar_por_data(checkpoints)[-1]
        retornar carregar_json(mais_recente)
    retornar None
```

---

## 6. Algoritmo de Priorização Pareto

### Cálculo 80/20
```
função calcular_pareto(items, metrica):
    total = sum(item[metrica] para item em items)
    ordenados = ordenar_desc(items, key=metrica)
    
    acumulado = 0
    pareto_20 = []
    
    para item em ordenados:
        acumulado += item[metrica]
        pareto_20.append(item)
        se acumulado >= total * 0.8:
            break
    
    retornar pareto_20
```

### Aplicações
- Top 20% arquivos = 80% do espaço
- Top 20% duplicatas = 80% do espaço recuperável
- Top 20% diretórios = 80% do volume
