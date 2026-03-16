# Deep Research Orchestration

Multi-agent parallel research skill for comprehensive ecosystem mapping.

## Metadata
- **Name**: deep-research
- **Version**: 1.0.0
- **Author**: AIOS Framework
- **Tags**: research, orchestration, multi-agent, parallel

## Description

Orchestrates a complete deep research workflow: scans existing research corpus, identifies coverage gaps, deploys parallel analysis and web search agents, consolidates findings into a structured framework document, and tracks remaining gaps.

**Human interactions:** 2-3 total (trigger + approval + optional review)

## Usage

```
/deep-research {domain} {corpus_path}
```

**Examples:**
```
/deep-research "Meta Business Platform" projects/meta-ecossystem/research/
/deep-research "AWS Cloud Services" research/aws/
/deep-research "Stripe Payments" docs/research/stripe/
```

## Instructions

When the user invokes `/deep-research`, execute the following phases sequentially. Each phase produces outputs consumed by the next phase. Phases 4-5 involve parallel agent execution.

---

### Phase 0: Input Parsing

Parse the user's command arguments:
- `domain`: The ecosystem name (e.g., "Meta Business Platform")
- `corpus_path`: Directory containing existing research documents

Validate:
- `corpus_path` exists and contains at least 1 `.md`, `.txt`, or `.pdf` file
- If `corpus_path` is relative, resolve from current working directory

Infer:
- `project_name`: From parent directory name or ask user
- `output_path`: Default to `{corpus_path}/FRAMEWORK.md`

---

### Phase 1: Corpus Discovery (AUTO - no human interaction)

Scan the corpus directory and catalog all research documents.

**Execute:**
1. `Glob(corpus_path + "**/*.md")` to find all markdown files
2. For each file, collect: filename, full path, size (via `ls -lh`)
3. For each file, read the first 50 lines to infer domain from title/headers
4. Group files by inferred domain
5. Count total files, total KB, estimate source count

**Domain inference keywords:**
- "whatsapp", "wpp", "messaging" → WhatsApp
- "ads", "campaign", "marketing api" → Ads/Marketing
- "instagram", "ig" → Instagram
- "messenger", "fbm" → Messenger
- "pixel", "capi", "conversion" → Tracking
- "policy", "compliance" → Policies
- "flow", "form" → Flows
- "commerce", "catalog" → Commerce
- Other → "unclassified"

**Present to user (brief):**
```
Corpus: N files, NKB total across N domains
```

---

### Phase 2: Gap Analysis (AUTO - no human interaction)

Compare covered domains against expected ecosystem domains.

**Auto-detect expected domains based on ecosystem name:**

| Ecosystem keyword | Expected domains |
|-------------------|-----------------|
| "meta", "facebook" | WhatsApp Cloud API, WhatsApp Flows, Commerce/Catalogs, Meta Marketing API, CAPI/Pixel, Instagram Graph API, Messenger Platform, Business Management API, Graph API Core, Business Suite |
| "aws", "amazon" | EC2, Lambda, S3, RDS, DynamoDB, VPC, IAM, SageMaker, ECS/EKS, CloudFront, SQS/SNS |
| "gcp", "google cloud" | Compute Engine, Cloud Functions, GCS, BigQuery, Cloud SQL, GKE, Vertex AI, Pub/Sub |
| "stripe" | Payments, Subscriptions, Connect, Invoicing, Checkout, Payment Links, Billing |

If ecosystem not recognized, ask user for expected domains.

**For each expected domain:**
- If covered by corpus files → status: COVERED, classify depth (Deep >50KB, Moderate 20-50KB, Shallow <20KB)
- If not covered → status: MISSING, classify severity:
  - HIGH: Core to project functionality
  - MEDIUM: Important but non-critical
  - LOW: Supplementary

**Design agent plan:**
- Group covered domains into clusters of 1-3 related files → 1 Type A agent each
- Group missing domains into clusters of max 7 → 1 Type B agent each
- Calculate estimated cost: $0.003/file (Type A) + $0.008/missing area (Type B)

---

### Gate 1: Scope Approval (HUMAN interaction required)

Present the analysis and agent plan using `AskUserQuestion`:

```
## Deep Research Plan

**Corpus:** N files, NKB, ~N sources across N domains
**Coverage:** N/N domains (N%)
**Gaps:** N domains missing (N HIGH, N MEDIUM, N LOW)

**Agent Plan:**
- N Type A agents (document analysis) → N files
- N Type B agents (web search) → N missing areas
- Estimated cost: $X.XX
- Estimated duration: parallel execution

Approve agent deployment?
```

Options:
1. **Approve** - Deploy all agents as planned
2. **Adjust** - Modify scope (add/remove domains)
3. **Cancel** - Abort research

If user selects "Adjust", re-run Phase 2 with modified parameters.
If user selects "Cancel", exit gracefully.

---

### Phase 3: Agent Prompt Generation (AUTO)

For each planned agent, generate a prompt:

**Type A agents (document analysis):**
Use the template structure from `research-agent-analysis-tmpl`:
```
You are analyzing the {DOMAIN} research for the {PROJECT} project.
Your job is to READ and EXTRACT a structured summary from the provided documents.
Do NOT write any code. Just produce analysis.

Read these files IN FULL:
1. {file_path_1}
2. {file_path_2}
...

Then produce a STRUCTURED SUMMARY in this format:
## {DOMAIN} - Ecosystem Map
### APIs & Endpoints Discovered
### Key Entities & Data Models
### Rate Limits & Quotas
### Authentication & Security
### Pricing Model ({YEAR})
### Integration Points
### Constraints & Restrictions ({YEAR})
### Gaps Identified

Respond ONLY with the structured summary. Be exhaustive.
```

**Type B agents (web search):**
Use the template structure from `research-agent-websearch-tmpl`:
```
You are researching the {ECOSYSTEM} to identify areas NOT YET covered.
The existing research covers:
1. {covered_area_1} ({summary})
...

Your task is to use WebSearch to research these MISSING areas:
1. **{missing_area_1}** - {topics}
...

For EACH area: search official docs, list endpoints, note {YEAR} updates,
identify cross-platform connections.

This is RESEARCH ONLY - do not write any code.
```

---

### Phase 4: Parallel Execution (AUTO)

Launch ALL agents in a SINGLE message using multiple Task tool calls:

```
For each agent_prompt in agent_prompts:
  Task(
    description: "{agent_type}: {domain}",
    prompt: agent_prompt,
    subagent_type: "general-purpose",
    run_in_background: true
  )
```

**CRITICAL:** All Task calls must be in ONE message for true parallelism.

Store all returned agent IDs for Phase 5.

---

### Phase 5: Progressive Collection (AUTO)

Collect agent outputs as they complete:

1. Wait briefly (30 seconds) for fast agents (Type A) to complete
2. Use `TaskOutput(agent_id, block=false)` to check status
3. Collect completed outputs immediately
4. For still-running agents (typically Type B), wait with `TaskOutput(agent_id, block=true, timeout=300000)` (5 min)
5. If any agent times out after 10 minutes, proceed with available data

Store all collected outputs for Phase 6.

---

### Phase 6: Consolidation (AUTO)

Merge all agent outputs into the framework document:

1. **Extract structured data** from each agent output:
   - Endpoints: `{method, path, description}`
   - Entities: `{name, fields, relations}`
   - Rate limits: `{resource, limit, window}`
   - Pricing: `{type, value, note}`
   - Constraints: `string[]`
   - Gaps: `{area, severity, description}`

2. **Deduplicate gaps** across all agents:
   - Same domain + similar description (>70% keyword overlap) = merge
   - Keep highest severity of merged gaps
   - Assign IDs: G1, G2, G3...

3. **Assemble framework** following `research-framework-output-tmpl` structure:
   - Header with corpus stats and methodology
   - Overview diagram (ASCII)
   - API table with all domains and statuses
   - One section per domain with endpoints/entities/limits
   - Gap analysis with consolidated gaps
   - Methodology section (auto-generated)
   - Changelog

4. **Version handling:**
   - If all agents completed: write as v1.0
   - If some agents still pending: write as v1.0, update to v1.1 when remaining complete

5. **Write to output_path** using the Write tool

---

### Phase 7: Gap Tracking & Delivery (AUTO)

Final phase - report results to user:

1. **Classify gaps** by current status: Resolvido, Parcial, Aberto
2. **Generate gap report** with statistics
3. **Propose next steps** based on gap profile:
   - HIGH gaps remaining → suggest follow-up agents
   - Only MEDIUM/LOW → suggest accepting framework
   - All resolved → framework is complete

4. **Present delivery:**
```
## Deep Research Complete

Framework created at: {output_path}
Version: v{version}

| Metric | Value |
|--------|-------|
| Agents deployed | N |
| APIs mapped | N |
| Endpoints cataloged | N |
| Gaps (raw → consolidated) | N → N |
| Gaps resolved | N |
| Gaps open | N |

Next steps:
1. Launch follow-up agents for N open HIGH gaps
2. Accept framework as-is
3. Review and adjust gap priorities
```

---

## AIOS Integration

This skill implements the `research-orchestration` workflow defined in:
`.aios-core/development/workflows/research-orchestration.yaml`

**Tasks used:**
- `research-corpus-discovery` (Phase 1)
- `research-gap-analysis` (Phase 2)
- `research-consolidation` (Phase 6)
- `research-gap-tracking` (Phase 7)

**Templates used:**
- `research-agent-analysis-tmpl` (Phase 3 - Type A prompts)
- `research-agent-websearch-tmpl` (Phase 3 - Type B prompts)
- `research-framework-output-tmpl` (Phase 6 - output structure)

## Notes

- Minimum corpus: 3 documents recommended for this workflow
- For single-topic research, use `create-deep-research-prompt` task instead
- Type B agents (web search) typically take 3-5x longer than Type A (doc analysis)
- Framework versions are incremental (v1.0 → v1.1 → v1.2)
- Cost is primarily driven by agent count and corpus size
- All agents use `general-purpose` subagent type with default (Sonnet) model
