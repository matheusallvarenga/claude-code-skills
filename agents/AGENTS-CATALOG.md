# Catálogo Completo de Agentes Claude Code

> **Versão:** 2.0
> **Data:** 2026-01-23
> **Total de Agentes:** 28
> **Localização:** `.claude/agents/`
> **Integração:** request-optimizer v4.0, Unified Architecture

---

## Sumário

1. [Visão Geral](#visão-geral)
2. [Estrutura dos Agentes](#estrutura-dos-agentes)
3. [Agentes por Categoria](#agentes-por-categoria)
   - [Obsidian/PKM (5)](#1-agentes-de-obsidianpkm)
   - [Podcast & Mídia (6)](#2-agentes-de-podcast--mídia)
   - [Negócios & Inteligência (4)](#3-agentes-de-negócios--inteligência)
   - [Design & Interface (3)](#4-agentes-de-design--interface)
   - [Desenvolvimento & Prompts (2)](#5-agentes-de-desenvolvimento--prompts)
   - [Gestão & Curadoria (2)](#6-agentes-de-gestão--curadoria)
4. [Guia de Implementação](#guia-de-implementação)
5. [Matriz de Decisão](#matriz-de-decisão)

---

## Visão Geral

Este catálogo documenta os 28 agentes especializados disponíveis para uso com Claude Code. Cada agente é otimizado para tarefas específicas e pode ser invocado proativamente para maximizar produtividade.

### Routing via request-optimizer v4.0

Os agentes são selecionados automaticamente pelo `request-optimizer` baseado em:

1. **Complexity Score** (0.0-1.0)
2. **Category Matching** (keywords no prompt)
3. **Learning History** (correções anteriores do usuário)

```
Complexity 0.3-0.5 → Claude Code Agents (Sonnet)
Complexity 0.5-0.7 → Ralph Loop (coding) ou Agents
Complexity > 0.7   → AIOS Kernel (multi-agent)
```

**Referência**: `.claude/skills/request-optimizer/references/agent-routing.md`

### Distribuição por Modelo

| Modelo | Quantidade | Uso Recomendado |
|--------|------------|-----------------|
| **Sonnet** | 21 agentes | Tarefas gerais, análises, automações |
| **Opus** | 7 agentes | Tarefas complexas, alta precisão, criação sofisticada |

### Novos Agentes (v4.0)

| Agente | Modelo | Descrição |
|--------|--------|-----------|
| `fullstack-developer` | Opus | Full-stack: React, Node.js, databases, APIs |
| `frontend-developer` | Sonnet | Frontend: React/Next.js, TypeScript, Tailwind |
| `backend-architect` | Opus | Arquitetura backend, microservices, databases |
| `code-reviewer` | Sonnet | Code review, best practices, security |
| `supabase-specialist` | Opus | Supabase: RLS, Edge Functions, LGPD |
| `task-decomposition-expert` | Sonnet | Decomposição de tarefas complexas |

### Distribuição por Categoria

```
Development ........... 6 agentes (21%) [NEW]
Obsidian/PKM .......... 5 agentes (18%)
Podcast & Mídia ....... 6 agentes (21%)
Negócios .............. 4 agentes (14%)
Design ................ 3 agentes (11%)
Gestão ................ 4 agentes (14%)
```

---

## Estrutura dos Agentes

Cada agente é definido em um arquivo `.md` com a seguinte estrutura:

```yaml
---
name: nome-do-agente           # Identificador único
description: Descrição breve   # Quando e como usar
tools: Tool1, Tool2, Tool3     # Ferramentas disponíveis
model: sonnet | opus           # Modelo de IA
---

[System Prompt Detalhado]
```

### Tools Disponíveis

| Tool | Função |
|------|--------|
| `Read` | Ler arquivos do sistema |
| `Write` | Escrever/criar arquivos |
| `Edit` | Editar arquivos existentes |
| `MultiEdit` | Edições múltiplas simultâneas |
| `Bash` | Executar comandos shell |
| `Glob` | Buscar arquivos por padrão |
| `Grep` | Buscar conteúdo em arquivos |
| `LS` | Listar diretórios |
| `WebSearch` | Pesquisar na web |
| `WebFetch` | Buscar conteúdo de URLs |
| `TodoWrite` | Gerenciar lista de tarefas |

---

## Agentes por Categoria

---

## 1. Agentes de Obsidian/PKM

Especializados em gestão de conhecimento pessoal e vaults Obsidian.

---

### 1.1 connection-agent

**Especialista em Conexões de Conhecimento**

| Atributo | Valor |
|----------|-------|
| **Arquivo** | `connection-agent.md` |
| **Modelo** | Sonnet |
| **Tools** | Read, Grep, Bash, Write, Glob |

#### Finalidade

Descobrir e sugerir conexões significativas entre notas, criando um grafo de conhecimento rico e interconectado.

#### Responsabilidades

1. **Conexões Baseadas em Entidades**: Encontrar notas que mencionam as mesmas pessoas, projetos ou tecnologias
2. **Análise de Sobreposição de Keywords**: Identificar notas com terminologia e conceitos similares
3. **Detecção de Notas Órfãs**: Encontrar notas sem links de entrada ou saída
4. **Geração de Sugestões de Links**: Criar relatórios acionáveis para curadoria manual
5. **Análise de Padrões de Conexão**: Identificar clusters e gaps de conhecimento

#### Estratégias de Conexão

- **Extração de Entidades**: Nomes de pessoas, tecnologias (LangChain, Claude, GPT-4), empresas (Anthropic, OpenAI)
- **Similaridade Semântica**: Termos técnicos comuns, tags compartilhadas, estruturas de diretório similares
- **Análise Estrutural**: Notas no mesmo diretório, MOCs linkando conteúdo relevante

#### Outputs Gerados

- `/System_Files/Link_Suggestions_Report.md`
- `/System_Files/Orphaned_Content_Connection_Report.md`
- `/System_Files/Orphaned_Nodes_Connection_Summary.md`

#### Quando Usar

- Após adicionar múltiplas notas novas ao vault
- Revisões periódicas de conectividade
- Quando perceber notas isoladas sem contexto
- Para descobrir relações não óbvias entre tópicos

---

### 1.2 moc-agent

**Especialista em Maps of Content**

| Atributo | Valor |
|----------|-------|
| **Arquivo** | `moc-agent.md` |
| **Modelo** | Sonnet |
| **Tools** | Read, Write, Bash, LS, Glob |

#### Finalidade

Criar e manter Maps of Content (MOCs) que servem como hubs de navegação para o conteúdo do vault.

#### Responsabilidades

1. **Identificar MOCs Faltantes**: Encontrar diretórios sem Maps of Content apropriados
2. **Gerar Novos MOCs**: Criar MOCs usando templates estabelecidos
3. **Organizar Imagens Órfãs**: Criar notas de galeria para assets visuais não linkados
4. **Atualizar MOCs Existentes**: Manter MOCs atualizados com novo conteúdo
5. **Manter Rede de MOCs**: Garantir que MOCs linkem entre si apropriadamente

#### Template de MOC

```markdown
---
tags:
- moc
- [relevant-tags]
type: moc
created: YYYY-MM-DD
modified: YYYY-MM-DD
status: active
---

# MOC - [Nome do Tópico]

## Overview
Breve descrição deste domínio de conhecimento.

## Core Concepts
- [[Conceito Chave 1]]
- [[Conceito Chave 2]]

## Resources
### Documentation
- [[Recurso 1]]

### Tools & Scripts
- [[Tool 1]]

## Related MOCs
- [[MOC Relacionado 1]]
```

#### Padrões de Nomenclatura

- Localização: `/map-of-content/`
- Formato: `MOC - [Nome do Tópico].md`
- Tipo no frontmatter: `type: "moc"`

#### Quando Usar

- Ao criar novas áreas de conhecimento no vault
- Quando diretórios crescem sem organização
- Para criar navegação hierárquica
- Ao reorganizar estrutura do vault

---

### 1.3 metadata-agent

**Especialista em Gestão de Metadados**

| Atributo | Valor |
|----------|-------|
| **Arquivo** | `metadata-agent.md` |
| **Modelo** | Sonnet |
| **Tools** | Read, MultiEdit, Bash, Glob, LS |

#### Finalidade

Garantir que todos os arquivos tenham frontmatter de metadados apropriados seguindo os padrões estabelecidos do vault.

#### Responsabilidades

1. **Adicionar Frontmatter Padronizado**: Adicionar frontmatter a arquivos markdown faltando
2. **Extrair Datas de Criação**: Obter datas de criação dos metadados do filesystem
3. **Gerar Tags**: Criar tags baseadas em estrutura de diretório e conteúdo
4. **Determinar Tipos de Arquivo**: Atribuir tipo apropriado (note, reference, moc, etc.)
5. **Manter Consistência**: Garantir que todos os metadados sigam padrões do vault

#### Padrões de Metadados

| Campo | Valores Possíveis | Obrigatório |
|-------|-------------------|-------------|
| `tags` | Array de tags hierárquicas | Sim |
| `type` | note, reference, moc, daily-note, template, system | Sim |
| `created` | YYYY-MM-DD | Sim |
| `modified` | YYYY-MM-DD | Sim |
| `status` | active, archive, draft | Sim |

#### Workflow

```bash
# Preview (dry-run)
python3 /System_Files/Scripts/metadata_adder.py --dry-run

# Aplicar mudanças
python3 /System_Files/Scripts/metadata_adder.py
```

#### Quando Usar

- Após importar notas de outras fontes
- Ao migrar conteúdo entre vaults
- Revisões periódicas de qualidade de metadados
- Antes de executar outros agentes de enhancement

---

### 1.4 tag-agent

**Especialista em Taxonomia de Tags**

| Atributo | Valor |
|----------|-------|
| **Arquivo** | `tag-agent.md` |
| **Modelo** | Sonnet |
| **Tools** | Read, MultiEdit, Bash, Glob |

#### Finalidade

Manter uma taxonomia de tags limpa, hierárquica e consistente em todo o vault.

#### Responsabilidades

1. **Normalizar Nomes de Tecnologia**: Garantir nomenclatura consistente (langchain → LangChain)
2. **Aplicar Estrutura Hierárquica**: Organizar tags em relações pai/filho
3. **Consolidar Duplicatas**: Mesclar tags similares (ai-agents e ai/agents)
4. **Gerar Relatórios de Análise**: Documentar uso de tags e inconsistências
5. **Manter Taxonomia**: Manter documento mestre de taxonomia atualizado

#### Hierarquia de Tags Padrão

```
ai/
├── agents/
├── embeddings/
├── llm/
│   ├── anthropic/
│   ├── openai/
│   └── google/
├── frameworks/
│   ├── langchain/
│   └── llamaindex/
└── research/

business/
├── client-work/
├── strategy/
└── startups/

development/
├── python/
├── javascript/
└── tools/
```

#### Regras de Padronização

| Categoria | Regra | Exemplo |
|-----------|-------|---------|
| Nomes de Tecnologia | Capitalização correta | LangChain, OpenAI, PostgreSQL |
| Caminhos Hierárquicos | Forward slashes, sem trailing | `ai/agents` |
| Multi-palavras | Hífens | `client-work` |
| Profundidade Máxima | 3 níveis | `ai/llm/anthropic` |

#### Quando Usar

- Após adicionar muito conteúdo novo
- Quando tags ficam inconsistentes
- Revisões trimestrais de taxonomia
- Antes de gerar relatórios ou análises

---

### 1.5 review-agent

**Especialista em Quality Assurance**

| Atributo | Valor |
|----------|-------|
| **Arquivo** | `review-agent.md` |
| **Modelo** | Sonnet |
| **Tools** | Read, Grep, LS |

#### Finalidade

Revisar e validar o trabalho realizado por outros agentes de enhancement, garantindo consistência e qualidade em todo o vault.

#### Responsabilidades

1. **Revisar Relatórios Gerados**: Validar output de outros agentes
2. **Verificar Consistência de Metadados**: Checar compliance com padrões de frontmatter
3. **Validar Qualidade de Links**: Garantir que conexões sugeridas fazem sentido
4. **Checar Padronização de Tags**: Verificar aderência à taxonomia
5. **Avaliar Completude de MOCs**: Garantir que MOCs organizam conteúdo apropriadamente

#### Checklists de Revisão

**Metadata Review**
- [ ] Todos arquivos têm campos de frontmatter obrigatórios
- [ ] Tags seguem estrutura hierárquica
- [ ] Tipos de arquivo atribuídos apropriadamente
- [ ] Datas no formato correto (YYYY-MM-DD)
- [ ] Campos de status válidos (active, archive, draft)

**Connection Review**
- [ ] Links sugeridos são contextualmente relevantes
- [ ] Sem referências de links quebrados
- [ ] Links bidirecionais onde apropriado
- [ ] Notas órfãs foram endereçadas

**Tag Review**
- [ ] Nomes de tecnologia capitalizados corretamente
- [ ] Sem tags duplicadas ou redundantes
- [ ] Máximo 3 níveis de hierarquia mantido

**MOC Review**
- [ ] Todos diretórios principais têm MOCs
- [ ] MOCs seguem convenção de nomenclatura
- [ ] Links para conteúdo relevante incluídos

#### Métricas de Qualidade

- Número de arquivos enhanced
- Notas órfãs reduzidas
- Novas conexões criadas
- Tags padronizadas
- MOCs gerados
- Score geral de conectividade do vault

#### Quando Usar

- Após executar outros agentes de vault enhancement
- Revisões periódicas de qualidade
- Antes de considerar vault "production-ready"
- Para auditorias de consistência

---

## 2. Agentes de Podcast & Mídia

Especializados em produção, otimização e distribuição de conteúdo de podcast.

---

### 2.1 podcast-content-analyzer

**Especialista em Análise de Conteúdo**

| Atributo | Valor |
|----------|-------|
| **Arquivo** | `podcast-content-analyzer.md` |
| **Modelo** | **Opus** |
| **Tools** | Read |

#### Finalidade

Transformar transcrições brutas em insights acionáveis para criadores de conteúdo, identificando momentos de alto engajamento.

#### Responsabilidades

1. **Análise de Segmentos**: Analisar conteúdo sistematicamente para identificar momentos com alto potencial de engajamento
2. **Avaliação de Potencial Viral**: Identificar clips adequados para redes sociais (15-60 segundos)
3. **Estrutura de Conteúdo**: Criar quebras lógicas de capítulos
4. **Otimização SEO**: Extrair keywords, entidades e tópicos relevantes
5. **Métricas de Qualidade**: Aplicar scoring consistente (escala 1-10)

#### Critérios de Avaliação por Segmento

| Score | Classificação | Ação Recomendada |
|-------|---------------|------------------|
| 9-10 | Excepcional com potencial viral | Prioridade máxima para clips |
| 7-8 | Conteúdo forte para destaque | Incluir em highlights |
| 5-6 | Bom conteúdo de suporte | Manter no episódio |
| <5 | Considerar cortar ou condensar | Revisar necessidade |

#### Fatores de Scoring

- **Impacto Emocional**: Humor, surpresa, revelação, controvérsia
- **Valor Educacional**: Informações únicas, insights práticos
- **Completude da História**: Arco narrativo com início, meio e fim
- **Demonstração de Expertise**: Credibilidade do convidado
- **Perspectivas Únicas**: Visões contrárias ou inovadoras
- **Relatabilidade**: Apelo universal

#### Requisitos por Plataforma

| Plataforma | Requisitos |
|------------|------------|
| TikTok/Reels/Shorts | Alta energia, hooks rápidos, potencial visual |
| Twitter/X | Insights quotáveis, takes controversos |
| LinkedIn | Insights profissionais, conselhos de carreira |
| Instagram | Momentos inspiracionais, behind-the-scenes |

#### Output (JSON)

```json
{
  "key_moments": [
    {
      "timestamp": "00:15:30",
      "title": "Título do Momento",
      "score": 8.5,
      "viral_potential": "high",
      "platforms": ["tiktok", "twitter"]
    }
  ],
  "chapters": [...],
  "keywords": [...],
  "thematic_analysis": "..."
}
```

#### Quando Usar

- Após transcrever novo episódio
- Para criar clips de redes sociais
- Planejamento de capítulos do YouTube
- Análise de performance de conteúdo

---

### 2.2 podcast-metadata-specialist

**Especialista em Metadados e Show Notes**

| Atributo | Valor |
|----------|-------|
| **Arquivo** | `podcast-metadata-specialist.md` |
| **Modelo** | **Opus** |
| **Tools** | Read, Write |

#### Finalidade

Transformar conteúdo de podcast em pacotes de metadados completos, descobríveis e engajantes.

#### Responsabilidades

1. **Títulos SEO-Otimizados**: Criar títulos que capturam atenção e representam conteúdo
2. **Timestamps Detalhados**: Criar marcadores de capítulo descritivos
3. **Show Notes Completas**: Escrever notas que servem ouvintes e mecanismos de busca
4. **Quotes Memoráveis**: Extrair citações com timestamps precisos
5. **Tags e Categorias**: Gerar para máxima descobribilidade
6. **Templates de Social Media**: Criar posts otimizados por plataforma
7. **Descrições por Plataforma**: Formatar respeitando requisitos únicos

#### Limites por Plataforma

| Plataforma | Limite de Caracteres | Características |
|------------|---------------------|-----------------|
| YouTube | 5000 chars | Timestamps clicáveis MM:SS ou HH:MM:SS |
| Apple Podcasts | 4000 chars | Texto limpo, foco em value proposition |
| Spotify | Sem limite rígido | HTML suportado, ênfase em engajamento |

#### Padrões de Qualidade

- **Títulos**: 60-70 caracteres para display ótimo
- **Descrições**: Hook nos primeiros 125 caracteres
- **Títulos de Capítulo**: Action-oriented e descritivos
- **Tags**: Termos amplos e de nicho combinados
- **Social Media Posts**: Engajantes com hashtags relevantes
- **Timestamps**: Precisos e formatados corretamente

#### Output (JSON)

```json
{
  "episode_metadata": {
    "title": "...",
    "description": "...",
    "tags": [...],
    "categories": [...],
    "guest_details": {...}
  },
  "chapters": [
    {
      "timestamp": "00:05:30",
      "title": "Título do Capítulo",
      "description": "..."
    }
  ],
  "key_quotes": [
    {
      "quote": "...",
      "speaker": "...",
      "timestamp": "00:12:45"
    }
  ],
  "social_media_posts": {
    "twitter": "...",
    "linkedin": "...",
    "instagram": "..."
  },
  "platform_descriptions": {
    "youtube": "...",
    "apple_podcasts": "...",
    "spotify": "..."
  }
}
```

#### Quando Usar

- Preparação de publicação de episódio
- Otimização de episódios existentes
- Criação de material promocional
- Melhoria de SEO do podcast

---

### 2.3 podcast-trend-scout

**Especialista em Análise de Tendências**

| Atributo | Valor |
|----------|-------|
| **Arquivo** | `podcast-trend-scout.md` |
| **Modelo** | Sonnet |
| **Tools** | Read, Write, WebSearch |

#### Finalidade

Identificar 3-5 tópicos emergentes ou notícias que fariam conteúdo compelling para próximos episódios.

#### Responsabilidades

1. **Descoberta de Tendências**: Buscar e analisar tendências tech atuais
2. **Filtragem de Relevância**: Avaliar adequação para o podcast
3. **Desenvolvimento de Tópicos**: Fornecer headlines, rationale e perguntas para guests

#### Metodologia de Descoberta

- Breaking tech news das últimas 48-72 horas
- Tecnologias emergentes ganhando tração
- Mudanças na indústria ou anúncios notáveis
- Desenvolvimentos controversos ou debatíveis
- Histórias sub-reportadas com implicações significativas

#### Critérios de Filtragem

| Critério | Avaliação |
|----------|-----------|
| Timing e valor de notícia | Alto/Médio/Baixo |
| Alinhamento com foco do podcast | Sim/Parcial/Não |
| Potencial para discussão engajante | Alto/Médio/Baixo |
| Disponibilidade de guests/perspectivas | Fácil/Moderado/Difícil |
| Diferenciação de tópicos recentes | Novo/Relacionado/Coberto |

#### Formato de Output

```
1. [Headline do Tópico]
Rationale: [2-3 sentenças explicando relevância e timing]
Guest Question: [Uma pergunta engajante para discussão]

2. [Próximo tópico...]
```

#### Padrões de Qualidade

- Priorizar tendências genuinamente emergentes sobre notícias requentadas
- Garantir tópicos com profundidade suficiente para segmentos de 15-30 minutos
- Balancear inovação técnica com histórias de impacto mais amplo
- Evitar tópicos que requerem pré-requisitos técnicos extensivos
- Considerar perspectivas diversas e relevância global

#### Quando Usar

- Planejamento semanal de episódios
- Brainstorming de conteúdo
- Identificação de guests potenciais
- Análise de oportunidades de timing

---

### 2.4 timestamp-precision-specialist

**Especialista em Precisão de Timestamps**

| Atributo | Valor |
|----------|-------|
| **Arquivo** | `timestamp-precision-specialist.md` |
| **Modelo** | **Opus** |
| **Tools** | Bash, Read, Write |

#### Finalidade

Extrair e refinar timestamps exatos para garantir cortes de qualidade profissional em produção de podcast.

#### Responsabilidades

1. **Análise de Waveform**: Analisar formas de onda de áudio para identificar pontos de corte precisos
2. **Detecção de Boundaries de Fala**: Garantir cortes que nunca ocorrem mid-word ou mid-syllable
3. **Detecção de Silêncio**: Usar filtros FFmpeg para identificar gaps de áudio
4. **Timing Frame-Accurate**: Calcular números de frame exatos para edição de vídeo
5. **Cálculos de Fade**: Determinar durações apropriadas de fade-in/fade-out

#### Comandos FFmpeg Utilizados

```bash
# Analisar arquivo de mídia
ffprobe -v quiet -print_format json -show_format -show_streams input.mp4

# Gerar visualização de waveform
ffmpeg -i input.wav -filter_complex "showwavespic=s=1920x1080:colors=white|0x808080" -frames:v 1 waveform.png

# Detecção de silêncio
ffmpeg -i input.wav -af "silencedetect=n=-50dB:d=0.5" -f null - 2>&1 | grep -E "silence_(start|end)"

# Análise frame-específica
ffmpeg -i input.mp4 -vf "select='between(t,START,END)',showinfo" -f null - 2>&1 | grep pts_time
```

#### Parâmetros de Detecção

| Parâmetro | Valor Padrão | Descrição |
|-----------|--------------|-----------|
| Threshold de Silêncio | -50dB | Nível abaixo considerado silêncio |
| Duração Mínima | 0.5s | Duração mínima de silêncio |
| Padding de Silêncio | 0.2s mínimo | Margem de segurança |
| Duração de Fade | 0.5-1.0s | Transições suaves |

#### Formatos de Output

- `HH:MM:SS.mmm` - Legibilidade humana
- Total de segundos com precisão de milissegundos
- Números de frame para software de edição de vídeo
- Scores de confiança baseados em clareza do boundary

#### Output (JSON)

```json
{
  "segments": [
    {
      "segment_id": "intro_01",
      "start_time": "00:00:00.000",
      "end_time": "00:02:30.500",
      "start_frame": 0,
      "end_frame": 4515,
      "fade_in_duration": 0.5,
      "fade_out_duration": 0.5,
      "silence_padding": {
        "before": 0.0,
        "after": 0.3
      },
      "boundary_type": "natural_pause",
      "confidence": 0.95
    }
  ],
  "video_info": {
    "fps": 30.0,
    "total_frames": 108000,
    "duration": "01:00:00.000"
  },
  "analysis_notes": "..."
}
```

#### Quando Usar

- Edição profissional de podcast
- Criação de clips para redes sociais
- Marcação de capítulos precisa
- Preparação de conteúdo para plataformas de vídeo

---

### 2.5 seo-podcast-optimizer

**Especialista em SEO para Podcasts**

| Atributo | Valor |
|----------|-------|
| **Arquivo** | `seo-podcast-optimizer.md` |
| **Modelo** | Sonnet |
| **Tools** | Read, Write, WebSearch |

#### Finalidade

Criar conteúdo otimizado para busca que balanceia efetividade de keywords com copy engajante e click-worthy.

#### Responsabilidades

1. **Analisar Conteúdo**: Extrair temas-chave, tecnologias e conceitos
2. **Criar Título SEO-Otimizado**: <= 60 caracteres, keywords naturais, click-worthy
3. **Escrever Meta Description**: <= 160 caracteres, value proposition clara
4. **Identificar Long-Tail Keywords**: Exatamente 3 keywords de 3-5 palavras cada

#### Limites de Caracteres

| Elemento | Limite | Objetivo |
|----------|--------|----------|
| Título | ≤60 chars | Display ótimo em SERPs |
| Meta Description | ≤160 chars | Preview completo em resultados |
| Long-Tail Keywords | 3-5 palavras cada | Competição moderada |

#### Critérios de Keywords

- Priorizar keywords com 100-1000 buscas mensais
- Garantir alinhamento com conteúdo real do episódio
- Evitar keyword stuffing; manter fluxo de linguagem natural
- Considerar intenção de busca do usuário
- Balancear termos trending com keywords evergreen

#### Formato de Output

```
SEO OPTIMIZATION REPORT

Optimized Title: "[Título]" (X characters)

Meta Description: "[Descrição]" (X characters)

Long-Tail Keywords:
1. [Keyword] - Est. Volume: [X]/month - Relevance: [X]/10
2. [Keyword] - Est. Volume: [X]/month - Relevance: [X]/10
3. [Keyword] - Est. Volume: [X]/month - Relevance: [X]/10

Rationale: [Breve explicação da estratégia de seleção de keywords]
```

#### Quando Usar

- Publicação de novos episódios
- Otimização de episódios antigos
- Planejamento de conteúdo baseado em SEO
- Análise de competidores

---

### 2.6 social-media-copywriter

**Especialista em Criação de Conteúdo Social**

| Atributo | Valor |
|----------|-------|
| **Arquivo** | `social-media-copywriter.md` |
| **Modelo** | Sonnet |
| **Tools** | Read, Write, WebSearch |

#### Finalidade

Transformar informações de episódios em conteúdo de redes sociais compelling que impulsiona engajamento e audiência.

#### Responsabilidades

Criar três peças distintas de conteúdo para cada episódio:

#### 1. Twitter/X Thread (3-5 tweets)

- Começar com hook que captura insight-chave ou momento intrigante
- Construir tensão narrativa através do thread
- Incluir 2-3 hashtags relevantes por tweet
- Terminar com call-to-action claro e link do episódio
- Cada tweet < 280 caracteres

#### 2. LinkedIn Update (max 1300 caracteres)

- Abrir com pergunta thought-provoking ou insight da indústria
- Fornecer contexto profissional e key takeaways
- Incluir links Spotify e YouTube
- Tom profissional mas conversacional
- Formatar com line breaks para legibilidade

#### 3. Instagram Caption Bullets (3 pontos curtos)

- Cada bullet punchy e scannable
- Foco em hooks visuais/emocionais
- Incluir emojis relevantes
- Manter cada bullet < 50 caracteres

#### Tom por Plataforma

| Plataforma | Tom |
|------------|-----|
| Twitter/X | Conversacional, punchy, thought-provoking |
| LinkedIn | Profissional mas personable, insight-driven |
| Instagram | Energético, visual, community-focused |

#### Checklist de Auto-Verificação

- [ ] O hook faz alguém querer parar de scrollar?
- [ ] Os insights-chave estão claramente comunicados?
- [ ] O guest está propriamente creditado e posicionado como expert?
- [ ] As hashtags alinham com trends atuais e conteúdo do episódio?
- [ ] Todos os limites de caracteres/palavras respeitados?
- [ ] Este conteúdo faria VOCÊ querer ouvir o episódio?

#### Padrões de Qualidade

- Nunca usar frases genéricas como "Don't miss this episode!"
- Sempre incluir detalhes específicos e concretos do episódio
- Garantir que conteúdo de cada plataforma pareça nativo, não copy-pasted
- Verificar todos fatos, nomes e credenciais

#### Quando Usar

- Lançamento de episódios
- Promoção de conteúdo evergreen
- Campanhas de engajamento
- Cross-posting estratégico

---

## 3. Agentes de Negócios & Inteligência

Especializados em análise competitiva, pesquisa de mercado e automação de vendas.

---

### 3.1 competitive-intelligence-analyst

**Especialista em Inteligência Competitiva**

| Atributo | Valor |
|----------|-------|
| **Arquivo** | `competitive-intelligence-analyst.md` |
| **Modelo** | Sonnet |
| **Tools** | Read, Write, Edit, WebSearch, WebFetch |

#### Finalidade

Pesquisa de mercado, análise de competidores e coleta de inteligência de negócios estratégica.

#### Responsabilidades

1. **Mapeamento de Landscape Competitivo**: Identificação de players, market share, estratégias de posicionamento
2. **Análise SWOT**: Avaliação de forças, fraquezas, oportunidades e ameaças
3. **Porter's Five Forces**: Dinâmicas competitivas, poder de fornecedores/compradores
4. **Segmentação de Mercado**: Demographics, psychographics, padrões comportamentais
5. **Análise de Tendências**: Evolução da indústria, tecnologias emergentes, mudanças regulatórias

#### Fontes de Inteligência

| Categoria | Fontes |
|-----------|--------|
| Dados de Empresas Públicas | Annual reports (10-K, 10-Q), SEC filings, investor presentations |
| News e Mídia | Press releases, publicações da indústria, trade journals |
| Inteligência Social | LinkedIn, Twitter, Glassdoor |
| Análise de Patentes | Innovation tracking, R&D direction |
| Job Postings | Padrões de contratação, direção estratégica |

#### Frameworks Incluídos

```python
class CompetitorAnalysisFramework:
    # Perfis completos de competidores
    # Análise SWOT estruturada

class MarketIntelligenceCollector:
    # Coleta de inteligência financeira
    # Monitoramento de movimentos competitivos
    # Análise de job postings

class MarketTrendAnalyzer:
    # Identificação de tendências de mercado
    # Mapeamento de landscape competitivo
    # Avaliação de oportunidade de mercado

class CompetitiveIntelligenceReporter:
    # Briefings executivos
    # Dashboards de inteligência competitiva
```

#### Output Estruturado

- **Executive Summary**: Key findings, implicações estratégicas, ações recomendadas
- **Competitive Positioning**: Análise de posição de mercado e benchmarking
- **Threat Assessment**: Ameaças competitivas com probabilidade de impacto
- **Opportunity Identification**: Gaps de mercado e oportunidades de crescimento
- **Strategic Recommendations**: Insights acionáveis com níveis de prioridade
- **Monitoring Framework**: Prioridades de coleta de inteligência contínua

#### Quando Usar

- Entrada em novos mercados
- Análise de competidores específicos
- Planejamento estratégico
- Due diligence em aquisições
- Monitoramento contínuo de mercado

---

### 3.2 market-research-analyst

**Especialista em Pesquisa de Mercado**

| Atributo | Valor |
|----------|-------|
| **Arquivo** | `market-research-analyst.md` |
| **Modelo** | Sonnet |
| **Tools** | Read, Write, Edit, WebSearch |

#### Finalidade

Combinar expertise analítica profunda com metodologias de pesquisa cutting-edge para entregar inteligência de mercado acionável.

#### Responsabilidades

1. **Análise de Mercado Abrangente**: Investigar dinâmicas de mercado, tamanho, taxas de crescimento, segmentação
2. **Identificação de Key Players**: Perfil de participantes principais, market share, posicionamento
3. **Análise de Tendências**: Detectar tendências emergentes, disrupções tecnológicas, mudanças regulatórias
4. **Inteligência Competitiva**: Estratégias de competidores, pricing, canais de distribuição
5. **Validação Colaborativa**: Cross-verificar findings, desafiar assumptions

#### Metodologia de Pesquisa

1. Framework estruturado: market definition → size/growth → key players → trends → opportunities/threats
2. Usar múltiplas fontes de dados para triangular findings
3. Priorizar dados recentes (últimos 12-24 meses)
4. Distinguir claramente entre fatos verificados, estimativas e insights analíticos
5. Documentar todas as fontes meticulosamente

#### Padrões de Output

- Fornecer dados de pesquisa brutos organizados por categoria
- Incluir métricas específicas, percentuais e valores monetários quando disponíveis
- Sinalizar gaps de dados ou informações conflitantes explicitamente
- Destacar oportunidades ou ameaças time-sensitive
- Estruturar findings para fácil extração e aplicação estratégica

#### Quality Assurance

- Verificar currency e credibilidade das fontes
- Cross-reference múltiplas fontes para data points críticos
- Acknowledger limitações ou vieses nos dados disponíveis
- Fornecer níveis de confiança para diferentes findings
- Sugerir áreas que requerem investigação mais profunda

#### Quando Usar

- Planejamento de novos produtos
- Análise de viabilidade de mercado
- Identificação de oportunidades
- Suporte a decisões de investimento

---

### 3.3 sales-automator

**Especialista em Automação de Vendas**

| Atributo | Valor |
|----------|-------|
| **Arquivo** | `sales-automator.md` |
| **Modelo** | Sonnet |
| **Tools** | Read, Write |

#### Finalidade

Automação de vendas focada em conversões e relacionamentos.

#### Áreas de Foco

- Cold email sequences com personalização
- Campanhas e cadências de follow-up
- Templates de propostas e quotes
- Case studies e social proof
- Scripts de vendas e handling de objeções
- A/B testing de subject lines

#### Abordagem

1. Liderar com valor, não features
2. Personalizar usando pesquisa
3. Manter emails curtos e scannable
4. Focar em um CTA claro
5. Rastrear o que converte

#### Outputs

| Tipo | Descrição |
|------|-----------|
| Email Sequence | 3-5 touchpoints estruturados |
| Subject Lines | Variantes para A/B testing |
| Personalization Variables | Campos para customização |
| Follow-up Schedule | Cronograma de follow-ups |
| Objection Handling Scripts | Respostas para objeções comuns |
| Tracking Metrics | Métricas para monitorar |

#### Princípios de Escrita

- Escrever conversacionalmente
- Mostrar empatia para problemas do cliente
- Focar em benefícios, não funcionalidades
- Manter brevidade e clareza

#### Quando Usar

- Lançamento de campanhas de outreach
- Criação de sequências de nurturing
- Desenvolvimento de playbooks de vendas
- Otimização de taxas de conversão

---

### 3.4 seo-analyzer

**Especialista em Análise SEO**

| Atributo | Valor |
|----------|-------|
| **Arquivo** | `seo-analyzer.md` |
| **Modelo** | Sonnet |
| **Tools** | Read, Write, WebFetch, Grep, Glob |

#### Finalidade

Auditorias técnicas de SEO, otimização de conteúdo e melhorias de performance em mecanismos de busca.

#### Áreas de Foco

- Auditorias técnicas de SEO e análise de estrutura de site
- Otimização de meta tags, títulos e descrições
- Análise de Core Web Vitals e performance de página
- Implementação de Schema markup e structured data
- Estrutura de internal linking e otimização de URLs
- Validação de mobile-first indexing e responsive design

#### Abordagem

1. Assessment técnico abrangente de SEO
2. Análise de qualidade de conteúdo e otimização de keywords
3. Avaliação de métricas de performance e Core Web Vitals
4. Testing de usabilidade mobile e responsive design
5. Validação e enhancement de structured data
6. Análise competitiva e benchmarking

#### Outputs

| Tipo | Descrição |
|------|-----------|
| SEO Audit Reports | Relatórios detalhados com ranking de prioridade |
| Meta Tag Recommendations | Sugestões de otimização |
| Core Web Vitals Strategies | Estratégias de melhoria de performance |
| Schema Markup Implementations | Implementações de structured data |
| Internal Linking Improvements | Melhorias de estrutura de links |
| Performance Optimization Roadmaps | Roadmaps de otimização |

#### Quando Usar

- Auditorias periódicas de SEO
- Lançamento de novos sites/páginas
- Diagnóstico de queda de rankings
- Análise de performance técnica

---

## 4. Agentes de Design & Interface

Especializados em criação de interfaces, experiência do usuário e análise visual.

---

### 4.1 cli-ui-designer

**Especialista em Design de Interface CLI**

| Atributo | Valor |
|----------|-------|
| **Arquivo** | `cli-ui-designer.md` |
| **Modelo** | Sonnet |
| **Tools** | Read, Write, Edit, MultiEdit, Glob, Grep |

#### Finalidade

Criar interfaces web inspiradas em terminal usando tecnologias web modernas.

#### Expertise Core

**Terminal Aesthetics**
- Tipografia monospace com fallback fonts: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace
- Esquemas de cores terminal com CSS custom properties
- Padrões visuais command-line: prompts, cursors, status indicators
- Integração de ASCII art para headers e branding

**Princípios de Design**
1. Sensação autêntica de terminal
2. Elementos de command line (prompts: $, >, ⎿)
3. Status dots coloridos (verde, laranja, vermelho)
4. Sistema de cores CSS completo

#### Sistema de Cores Terminal

```css
:root {
    /* Terminal Background Colors */
    --bg-primary: #0f0f0f;
    --bg-secondary: #1a1a1a;
    --bg-tertiary: #2a2a2a;

    /* Terminal Text Colors */
    --text-primary: #ffffff;
    --text-secondary: #a0a0a0;
    --text-accent: #d97706;
    --text-success: #10b981;
    --text-warning: #f59e0b;
    --text-error: #ef4444;

    /* Terminal Borders */
    --border-primary: #404040;
    --border-secondary: #606060;
}
```

#### Componentes Incluídos

- Terminal Header com ASCII art
- Command Sections
- Interactive Command Input
- Filter Chips (Terminal Style)
- Command Line Examples
- Navigation
- Search Interface
- Data Display
- Modal/Dialog
- Buttons e Form Inputs
- Status Indicators
- Animações de cursor

#### Padrões de Qualidade

**Visual Consistency**
- Todo texto usa monospace fonts
- Color scheme segue CSS custom properties
- Spacing segue 8px baseline grid
- Border radius consistente (4px small, 8px large)

**Terminal Authenticity**
- Command prompts usam símbolos adequados ($, >, ⎿)
- Status indicators usam cores apropriadas
- ASCII art formatado corretamente
- Feedback interativo imita comportamento de terminal

#### Quando Usar

- Criação de dashboards estilo terminal
- Interfaces para desenvolvedores
- Ferramentas CLI web-based
- Projetos com estética hacker/dev

---

### 4.2 ui-ux-designer

**Especialista em UI/UX Design**

| Atributo | Valor |
|----------|-------|
| **Arquivo** | `ui-ux-designer.md` |
| **Modelo** | Sonnet |
| **Tools** | Read, Write, Edit |

#### Finalidade

Design centrado no usuário e sistemas de interface.

#### Áreas de Foco

- User research e desenvolvimento de personas
- Workflows de wireframing e prototipagem
- Criação e manutenção de design systems
- Acessibilidade e princípios de design inclusivo
- Information architecture e user flows
- Usability testing e estratégias de iteração

#### Abordagem

1. User needs first - design com empatia e dados
2. Progressive disclosure para interfaces complexas
3. Padrões de design e componentes consistentes
4. Mobile-first responsive design thinking
5. Acessibilidade built-in desde o início

#### Outputs

| Tipo | Descrição |
|------|-----------|
| User Journey Maps | Mapas de jornada e diagramas de fluxo |
| Wireframes | Low e high-fidelity |
| Design System Components | Componentes e guidelines |
| Prototype Specifications | Especificações para desenvolvimento |
| Accessibility Annotations | Anotações e requisitos de acessibilidade |
| Usability Testing Plans | Planos de teste e métricas |

#### Princípios

- Focar em resolver problemas do usuário
- Incluir design rationale e notas de implementação
- Considerar edge cases e cenários de erro
- Documentar decisões de design

#### Quando Usar

- Início de novos projetos de produto
- Redesign de interfaces existentes
- Criação de design systems
- Auditorias de usabilidade

---

### 4.3 visual-analysis-ocr

**Especialista em Análise Visual e OCR**

| Atributo | Valor |
|----------|-------|
| **Arquivo** | `visual-analysis-ocr.md` |
| **Modelo** | Sonnet |
| **Tools** | Read, Write |

#### Finalidade

Analisar imagens PNG e extrair texto preservando meticulosamente formatação, estrutura e hierarquia visual original.

#### Responsabilidades

**1. Text Extraction**
- Main body text
- Headers e subheaders em todos níveis
- Bullet points e listas numeradas
- Captions, footnotes e marginalia
- Caracteres especiais, símbolos e notação matemática

**2. Structure Recognition**
- Detectar níveis de heading baseado em tamanho, peso e posição de fonte
- Reconhecer estruturas de lista (ordered, unordered, nested)
- Identificar ênfase de texto (bold, italic, underline)
- Detectar blocos de código, quotes e regiões de formatação especial
- Mapear indentação e espaçamento para hierarquia lógica

**3. Markdown Conversion**
- Usar níveis de heading apropriados (# ## ### etc.)
- Formatar listas com marcadores corretos (-, *, 1., etc.)
- Aplicar marcadores de ênfase (**bold**, *italic*, `code`)
- Preservar line breaks e espaçamento de parágrafos
- Lidar com caracteres especiais que podem precisar de escape

**4. Quality Assurance**
- Cross-check texto extraído para completude
- Garantir que nenhum elemento de formatação seja perdido
- Validar que estrutura markdown representa hierarquia visual
- Sinalizar seções ambíguas ou unclear

#### Handling de Edge Cases

| Situação | Abordagem |
|----------|-----------|
| Texto unclear ou ambíguo | Notar incerteza e fornecer melhor interpretação |
| Layouts complexos | Descrever estrutura e fornecer representação markdown mais lógica |
| Elementos non-text | Acknowledger presença e descrever relação com texto |
| Qualidade de imagem pobre | Indicar níveis de confiança para texto extraído |

#### Quando Usar

- Digitalização de documentos físicos
- Extração de texto de screenshots
- Conversão de imagens para markdown
- Análise de materiais visuais

---

## 5. Agentes de Desenvolvimento & Prompts

Especializados em otimização de prompts e edição de vídeo.

---

### 5.1 prompt-engineer

**Especialista em Engenharia de Prompts**

| Atributo | Valor |
|----------|-------|
| **Arquivo** | `prompt-engineer.md` |
| **Modelo** | **Opus** |
| **Tools** | Read, Write, Edit |

#### Finalidade

Crafting de prompts efetivos para LLMs e sistemas de IA, compreendendo nuances de diferentes modelos.

#### Áreas de Expertise

**Prompt Optimization**
- Seleção few-shot vs zero-shot
- Chain-of-thought reasoning
- Role-playing e perspective setting
- Especificação de formato de output
- Configuração de constraints e boundaries

**Arsenal de Técnicas**
- Constitutional AI principles
- Recursive prompting
- Tree of thoughts
- Self-consistency checking
- Prompt chaining e pipelines

**Otimização por Modelo**

| Modelo | Ênfase |
|--------|--------|
| Claude | Helpful, harmless, honest |
| GPT | Estrutura clara e exemplos |
| Open Models | Necessidades de formatação específicas |
| Specialized Models | Adaptação de domínio |

#### Processo de Otimização

1. Analisar o use case pretendido
2. Identificar requisitos e constraints chave
3. Selecionar técnicas de prompting apropriadas
4. Criar prompt inicial com estrutura clara
5. Testar e iterar baseado em outputs
6. Documentar padrões efetivos

#### Formato de Output Obrigatório

```markdown
### The Prompt
```
[Display do texto completo do prompt aqui]
```

### Implementation Notes
- Técnicas-chave usadas
- Por que essas escolhas foram feitas
- Resultados esperados
```

#### Deliverables

- **Texto do prompt** (displayed em full, formatado)
- Explicação de design choices
- Guidelines de uso
- Exemplos de outputs esperados
- Performance benchmarks
- Estratégias de error handling

#### Padrões Comuns

- Estrutura System/User/Assistant
- XML tags para seções claras
- Formatos de output explícitos
- Step-by-step reasoning
- Self-evaluation criteria

#### Quando Usar

- Desenvolvimento de features de IA
- Otimização de agentes existentes
- Criação de system prompts
- Debugging de outputs de LLM

---

### 5.2 video-editor

**Especialista em Edição de Vídeo**

| Atributo | Valor |
|----------|-------|
| **Arquivo** | `video-editor.md` |
| **Modelo** | **Opus** |
| **Tools** | Bash, Read, Write |

#### Finalidade

Produção profissional de vídeo e pós-processamento.

#### Áreas de Foco

- Video cutting, trimming e sequence assembly
- Transition effects e smooth cuts
- Workflows de color correction e grading
- Sincronização multi-track de vídeo e áudio
- Visual effects e overlay composition
- Otimização de rendering para diferentes formatos

#### Abordagem

1. Non-destructive editing - preservar qualidade da fonte
2. Timeline-based workflow planning
3. Consistência de color space e formato
4. Verificação de sincronização áudio-vídeo
5. Rendering eficiente com quality presets
6. Padrões de output profissional

#### Outputs

| Tipo | Descrição |
|------|-----------|
| Video Editing Sequences | Sequências completas de edição |
| Transition Parameters | Parâmetros de transição e efeitos |
| Color Grading | LUTs e correções de cor |
| Export Configurations | Configurações de export multi-formato |
| Batch Processing Workflows | Workflows de processamento em batch |
| Quality Control | Quality control e preview generation |

#### Padrões Profissionais

- Frame-accurate cuts
- Broadcast-safe levels
- Consistência de codec e bitrate
- Metadata preservation

#### Quando Usar

- Edição de episódios de podcast em vídeo
- Criação de clips para redes sociais
- Color grading profissional
- Batch processing de conteúdo

---

## 6. Agentes de Gestão & Curadoria

Especializados em gestão de contexto e curadoria de conteúdo.

---

### 6.1 context-manager

**Especialista em Gestão de Contexto**

| Atributo | Valor |
|----------|-------|
| **Arquivo** | `context-manager.md` |
| **Modelo** | **Opus** |
| **Tools** | Read, Write, Edit, TodoWrite |

#### Finalidade

Manter estado coerente através de múltiplas interações de agentes e sessões, crítico para projetos complexos e de longa duração.

#### Funções Primárias

**Context Capture**
1. Extrair decisões-chave e rationale de outputs de agentes
2. Identificar padrões e soluções reusáveis
3. Documentar pontos de integração entre componentes
4. Rastrear issues não resolvidos e TODOs

**Context Distribution**
1. Preparar contexto mínimo e relevante para cada agente
2. Criar briefings agent-specific
3. Manter índice de contexto para quick retrieval
4. Prune informação outdated ou irrelevante

**Memory Management**
- Armazenar decisões críticas de projeto em memória
- Manter rolling summary de mudanças recentes
- Indexar informação comumente acessada
- Criar checkpoints de contexto em major milestones

#### Workflow de Integração

1. Revisar conversa atual e outputs de agentes
2. Extrair e armazenar contexto importante
3. Criar summary para próximo agente/sessão
4. Atualizar índice de contexto do projeto
5. Sugerir quando full context compression é necessária

#### Formatos de Contexto

| Tipo | Tamanho | Conteúdo |
|------|---------|----------|
| **Quick Context** | < 500 tokens | Task atual, goals imediatos, decisões recentes, blockers ativos |
| **Full Context** | < 2000 tokens | Arquitetura do projeto, design decisions, integration points, work streams |
| **Archived Context** | Em memória | Decisões históricas, issues resolvidos, pattern library, benchmarks |

#### Princípio Core

> "Always optimize for relevance over completeness. Good context accelerates work; bad context creates confusion."

#### Quando Usar

- Projetos multi-agente complexos
- Sessões de trabalho longas
- Handoff entre diferentes agentes
- Preservação de decisões críticas

---

### 6.2 content-curator

**Especialista em Curadoria de Conteúdo**

| Atributo | Valor |
|----------|-------|
| **Arquivo** | `content-curator.md` |
| **Modelo** | Sonnet |
| **Tools** | Read, Write, Edit, Grep, Glob |

#### Finalidade

Manter conteúdo de alta qualidade, relevante e bem organizado em sistemas de gestão de conhecimento.

#### Responsabilidades

1. **Content Quality Assessment**: Identificar conteúdo de baixa qualidade ou outdated
2. **Duplicate Detection**: Encontrar e consolidar notas similares ou redundantes
3. **Content Enhancement**: Sugerir melhorias para notas incompletas
4. **Relevance Analysis**: Identificar conteúdo que precisa de updates ou archiving
5. **Knowledge Gap Identification**: Encontrar áreas onde conteúdo é escasso ou ausente

#### Métricas de Qualidade

**Quality Indicators**
- Comprimento e profundidade da nota (evitar stubs)
- Densidade de links e conexões bidirecionais
- Recência de updates e relevância
- Completude e precisão de tags
- Formatação e estrutura adequadas

**Content Health Checks**
| Check | Threshold |
|-------|-----------|
| Notas com poucas palavras | < 50 palavras (potential stubs) |
| Arquivos não modificados | > 6 meses |
| Notas órfãs | Sem conexões |
| Metadata incompleta | Campos obrigatórios faltando |
| Links quebrados | Referências inválidas |

#### Padrões de Qualidade

| Métrica | Padrão |
|---------|--------|
| Minimum note length | 100 palavras para conteúdo substantivo |
| Maximum stub threshold | 50 palavras |
| Link density | Pelo menos 2 outbound links por nota |
| Update frequency | Conteúdo crítico revisado trimestralmente |
| Tag completeness | Todas notas devem ter tags relevantes |

#### Workflows de Curadoria

**Duplicate Content Analysis**
1. Detecção de similaridade semântica
2. Comparar títulos e conteúdo
3. Identificar tópicos e conceitos overlapping
4. Encontrar explicações ou definições redundantes

**Consolidation Recommendations**
1. Merge notas similares com valor distinto
2. Criar redirects para conteúdo consolidado
3. Atualizar links para apontar para notas consolidadas

**Content Enhancement**
1. Identificar notas com conteúdo mínimo
2. Sugerir tópicos de expansão e estrutura
3. Recomendar conteúdo relacionado para linkar

#### Curation Reports

- Candidatos a conteúdo duplicado para review
- Stub notes requerendo enhancement
- Conteúdo outdated precisando updates
- Métricas de qualidade e trends de melhoria
- Success stories de consolidação

#### Quando Usar

- Maintenance periódica do vault
- Após importações bulk de conteúdo
- Revisões de qualidade trimestrais
- Antes de publicação ou sharing de conhecimento

---

## Guia de Implementação

### Passo 1: Instalação

```bash
# Copiar agentes para seu projeto Claude Code
cp -r /path/to/source/.claude/agents ~/.claude/agents

# Ou para projeto específico
cp -r /path/to/source/.claude/agents /seu-projeto/.claude/agents
```

### Passo 2: Adaptação de Paths

Vários agentes (especialmente os de Obsidian) referenciam paths específicos:

```markdown
# Paths originais (adaptar para seu ambiente)
/Users/cam/VAULT01/System_Files/Scripts/

# Seu path
/Users/seu-usuario/seu-vault/Scripts/
```

### Passo 3: Scripts Auxiliares

Para agentes de Obsidian, criar scripts Python:

| Script | Agente | Função |
|--------|--------|--------|
| `link_suggester.py` | connection-agent | Descoberta de links |
| `moc_generator.py` | moc-agent | Geração de MOCs |
| `metadata_adder.py` | metadata-agent | Adição de frontmatter |
| `tag_standardizer.py` | tag-agent | Padronização de tags |

### Passo 4: Invocação via Task Tool

```
Task tool:
  subagent_type: "general-purpose"
  prompt: "Use o agente [nome-do-agente] para [tarefa específica]..."
```

### Passo 5: Customização

Cada agente pode ser customizado editando seu arquivo `.md`:

1. Ajustar `description` para seu use case
2. Modificar `tools` conforme necessário
3. Alterar `model` (sonnet/opus) baseado em complexidade
4. Editar system prompt para seu domínio

---

## Matriz de Decisão

### Qual Agente Usar?

| Necessidade | Agente Recomendado | Modelo |
|-------------|-------------------|--------|
| Conectar notas no Obsidian | connection-agent | Sonnet |
| Criar navegação no vault | moc-agent | Sonnet |
| Padronizar metadados | metadata-agent | Sonnet |
| Organizar taxonomia de tags | tag-agent | Sonnet |
| Validar qualidade do vault | review-agent | Sonnet |
| Analisar conteúdo de podcast | podcast-content-analyzer | **Opus** |
| Criar show notes | podcast-metadata-specialist | **Opus** |
| Encontrar tópicos trending | podcast-trend-scout | Sonnet |
| Cortes frame-accurate | timestamp-precision-specialist | **Opus** |
| SEO para podcasts | seo-podcast-optimizer | Sonnet |
| Conteúdo social media | social-media-copywriter | Sonnet |
| Análise de competidores | competitive-intelligence-analyst | Sonnet |
| Pesquisa de mercado | market-research-analyst | Sonnet |
| Automação de vendas | sales-automator | Sonnet |
| Auditoria SEO técnica | seo-analyzer | Sonnet |
| Interface estilo terminal | cli-ui-designer | Sonnet |
| Design de UX | ui-ux-designer | Sonnet |
| Extrair texto de imagens | visual-analysis-ocr | Sonnet |
| Otimizar prompts | prompt-engineer | **Opus** |
| Edição de vídeo | video-editor | **Opus** |
| Gerenciar contexto multi-agente | context-manager | **Opus** |
| Curadoria de conteúdo | content-curator | Sonnet |

### Modelo Opus vs Sonnet

| Usar Opus Quando | Usar Sonnet Quando |
|------------------|-------------------|
| Tarefas requerem alta precisão | Tarefas são mais diretas |
| Output precisa ser sofisticado | Volume de processamento é alto |
| Análise profunda necessária | Custo é uma consideração |
| Criação de conteúdo premium | Iterações rápidas necessárias |

---

## Changelog

| Versão | Data | Alterações |
|--------|------|------------|
| 1.0 | 2025-12-23 | Documentação inicial de 22 agentes |

---

*Documento gerado automaticamente. Para atualizações, edite os arquivos individuais dos agentes em `.claude/agents/`*
