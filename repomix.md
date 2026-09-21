# repomix.md — tailored repomix commands for this codebase

Feed a capable LLM for **design / architecture / coding** on this Anki template repo.
`repomix` packs the repo into one file. The default `repomix` is **wasteful here** — it
ships ~215k tokens with stale backups + chat transcripts that drown the real signal.
These commands are adapted to the repo's actual structure (Anki templates, not a generic JS app).

> Tested on `repomix@1.18.0` (`npx repomix@latest`), Linux, 2026-09-21.
> All token counts use the default `o200k_base` tokenizer (GPT-4o family).

---

## TL;DR — copy-paste daily driver

```bash
# Full curated pack — templates + styling + tooling + tests + spec (recommended)
repomix --style markdown --output-show-line-numbers \
  -o repomix-output.md \
  --ignore "chat_history/**,conversations/**,Card 1 - Front.template.anki.*,backups/**,dist/**,reports/**,**/__pycache__/**,**/.ruff_cache/**,.anki_fields.json,repomix-output.*,repomix.md,*.apkg"
```

- **Output:** `repomix-output.md` — markdown with line numbers (`file:line` refs match `AGENTS.md`).
- **Scope:** 35 files, ~92k tokens, ~322k chars (vs 49 files / ~216k tokens default — saves **123k tokens, 57%**). `repomix.md` itself is excluded (meta-doc, not product) to keep the pack stable after this file was added.
- **When:** design review, architecture change, feature work, bug hunting. This is the one to paste into ChatGPT / Claude / Gemini.

Add `--copy` to copy straight to clipboard instead of a file:

```bash
repomix --style markdown --output-show-line-numbers --copy \
  --ignore "chat_history/**,conversations/**,Card 1 - Front.template.anki.*,backups/**,dist/**,reports/**,**/__pycache__/**,**/.ruff_cache/**,.anki_fields.json,repomix-output.*,repomix.md,*.apkg"
```

---

## Why `repomix` (no args) is wrong for this repo

Measured with `repomix --verbose` on `main` (2026-09-21):

| Run | Files | Tokens | Chars | Output |
|-----|-------|--------|-------|--------|
| `repomix` (bare default) | 49 | 215,796 | 917,178 | `repomix-output.xml` |
| Curated full (below) | 35 | 92,229 | 322,156 | `repomix-output.md` |
| Lean (no tests) | 25 | 62,372 | 220k | `repomix-lean.md` |
| Spec only (docs) | 13 | 17,529 | 72k | `repomix-spec.md` |

Default packs **12 stale Front snapshots** + **3 chat transcripts** + **allows `conversations/` leakage when `.gitignore` is applied late**. The top-5 token consumers in the default run tell the story:

```
1. chat_history/gemini_cli_prompts.txt   32,498 tokens (15.1%) — 132k chars of old prompts
2. chat_history/opencode_prompts.txt     15,029 tokens (7.0%)  — archived prompts
3. Card 1 - Style.css                    14,018 tokens (6.5%)  — real product, keep
4. Card 1 - Front.template.anki.before_orphan_removal  8,480 tokens — stale backup
5. Card 1 - Front.template.anki.backup_before_final    8,433 tokens — stale backup
```

12 tracked stale copies of `Card 1 - Front.template.anki` (`*.backup*` / `*.bak*` / `*.safeapi` / `*.before_*`) waste ~100k tokens collectively and confuse the LLM with contradictory Front implementations. `chat_history/` alone wastes ~47k tokens. `conversations/` (6.3 MB, 7 long transcripts + images) is gitignored but was still collected by bare `repomix` in verification — explicit `--ignore` is defense-in-depth.

**Principle:** keep everything the LLM needs to reason about the product and its enforcement, drop everything that is a snapshot, transcript, or build artifact.

---

## What to keep / what to drop

### Keep (the LLM must see these)

| Group | Files | Why it matters |
|-------|-------|----------------|
| **Spec stack** | `PRODUCT.md`, `MVP.md`, `ARCHITECTURE.md`, `QUALITY.md`, `TEST_STRATEGY.md`, `AGENTS.md`, `IMPLEMENTATION_PLAN.md`, `README.md`, `HANDOFF.md` | Authority hierarchy (`AGENTS.md` §0). Product intent, scope, invariants, test enforcement. Without them the LLM invents fields or widens scope. |
| **Decisions** | `docs/adr/*.md` (4 files) | Lasting choices: mature interval, compactor scoping, native audio, release loop. |
| **Product** | `Card 1 - Front.template.anki`, `Card 1 - Back.template.anki`, `Card 1 - Style.css` | The entire card. Front is ~30k chars of conditional + JS resolver + Mature Word Mode; Back is the hierarchy; CSS §1–§16 is the contract (themes, hero grid, compactor §6b, truncator §6c, audio rings, furigana). |
| **Tooling** | `fetch_anki_fields.py`, `sync_to_anki.py`, `release_apkg.py`, `verify`, `finish.sh` | Field bootstrap, snapshotted sync, `exportPackage`, one-command release. Shows the real workflow. |
| **Tests + fixtures** | `tests/*.py` (5 suites), `tests/fixtures/*.html` (4 fixtures), `.github/workflows/verify.yml` | How invariants are mechanically enforced. Fixtures capture Yomitan markup drift. CI re-runs `./verify`. |
| **Meta** | `.gitignore`, `.opencodeignore`, `fix_summary.md` | Process hygiene. |

### Drop (noise that pollutes context)

| Pattern | Reason | Token saving |
|---------|--------|-------------|
| `chat_history/**` (3 files, tracked) | Prompt archives: `opencode_prompts.txt` (67k), `gemini_cli_prompts.txt` (132k), `definition-truncation-handoff.md`. Useful as history, not as architecture context. Pack separately if you need prompt-history. | ~47k tokens (22%) |
| `conversations/**` (gitignored, 6.3 MB) | Old agent transcripts. Explicitly ignore — `repomix` was observed to collect them despite `.gitignore`. | Up to ~100k+ if leaked |
| `Card 1 - Front.template.anki.*` (12 tracked files) | Stale snapshots: `.backup*`, `.bak*`, `.bak2/.bak4`, `.safeapi`, `.before_*`. Only the canonical `Card 1 - Front.template.anki` is truth. | ~100k tokens (46%) |
| `backups/**` (gitignored, microsecond snapshots) | Pre-sync Anki dumps. Never useful to the LLM. | variable |
| `dist/**` (gitignored) | Released `.apkg` binary. | — |
| `reports/**` (gitignored) | CI reports. | — |
| `**/__pycache__/**`, `**/.ruff_cache/**` | Python caches. | — |
| `.anki_fields.json` (gitignored) | Live field dump from `fetch_anki_fields.py`. Ephemeral, never committed. | — |
| `repomix-output.*` | Self-reference. Always ignore the output you just wrote. | — |
| `repomix.md` | This file (meta-doc about packing). Not product logic; saves ~6k tokens post-creation. | ~6k tokens |
| `*.apkg` | Binary deck exports. | — |

> **Hygiene note:** 12 `Card 1 - Front.template.anki.*` files are currently **tracked** in git. Ideally untrack and delete them, and add `Card 1 - Front.template.anki.*` to `.gitignore` so they never re-enter the pack:

```bash
git rm --cached "Card 1 - Front.template.anki.backup2" "Card 1 - Front.template.anki.backup3" "Card 1 - Front.template.anki.backup4" \
  "Card 1 - Front.template.anki.backup_before_final" "Card 1 - Front.template.anki.backup_before_final_fix" \
  "Card 1 - Front.template.anki.backup_before_safeapi" "Card 1 - Front.template.anki.bak" "Card 1 - Front.template.anki.bak2" \
  "Card 1 - Front.template.anki.bak4" "Card 1 - Front.template.anki.before_fix" "Card 1 - Front.template.anki.before_orphan_removal" \
  "Card 1 - Front.template.anki.safeapi"
rm -f "Card 1 - Front.template.anki".backup* "Card 1 - Front.template.anki".bak* "Card 1 - Front.template.anki".safeapi "Card 1 - Front.template.anki".before_*
echo "Card 1 - Front.template.anki.*" >> .gitignore
```

---

## Commands

All commands quote the `--ignore` list so filenames with spaces (`Card 1 - …`) work in `zsh`/`bash`.

### 1. Full curated — `repomix-output.md` (recommended daily driver)

```bash
repomix --style markdown --output-show-line-numbers \
  -o repomix-output.md \
  --ignore "chat_history/**,conversations/**,Card 1 - Front.template.anki.*,backups/**,dist/**,reports/**,**/__pycache__/**,**/.ruff_cache/**,.anki_fields.json,repomix-output.*,repomix.md,*.apkg"
```

- **Scope:** 35 files. Spec stack + ADRs + all 3 card files + all tooling + all 5 test suites + 4 fixtures + CI workflow. No chat/conversation noise, no stale Front copies.
- **Output:** `markdown` — readable for ChatGPT / Gemini / Claude; `xml` is equally valid for Claude (see variant below). `--output-show-line-numbers` prefixes every line with `N:` so the LLM can obey `file_path:line_number` references (`AGENTS.md` requires them).
- **Cost:** ~92k tokens (measured 92,229), ~321 KB. Fits comfortably in 128k–200k context models with room left for your prompt. ~57% cheaper than bare `repomix`.
- **When:** any design / architecture / coding session. **Default to this.**
- **Extras:** add `--copy` to skip the file and copy to clipboard; add `--token-count-tree` to print a token tree before packing.

Flag-by-flag:

| Flag | Effect in this repo |
|------|---------------------|
| `--style markdown` | `# File Summary` + `# Repository Structure` + `## File: path` per file. Preferred for this codebase because templates/CSS contain `{{{triple-mustache}}}` + Japanese + SVG that would need XML escaping. `xml` works too (74k tokens, slightly cheaper) but `markdown` is what most web LLM UIs render best. |
| `--output-show-line-numbers` | `  42: <div class="hero-header">` — lets the LLM cite `Card 1 - Style.css:432`. Costs ~17.5k tokens (+23% vs no-line-numbers) but pays for itself in coding tasks. Drop it only for pure prose/architecture chat. |
| `-o repomix-output.md` | Explicit output path. The `repomix-output.*` ignore keeps it from recursing into itself on the next run. |
| `--ignore "…"` | Blacklist that removes exactly the noise table above while letting **new** docs/tests/ADRs auto-include (better than a whitelist `--include` that you'd forget to update). |

### 2. Lean — `repomix-lean.md` (quick / cheap / focus on product)

```bash
repomix --style markdown --output-show-line-numbers \
  -o repomix-lean.md \
  --ignore "chat_history/**,conversations/**,Card 1 - Front.template.anki.*,backups/**,dist/**,reports/**,**/__pycache__/**,**/.ruff_cache/**,.anki_fields.json,repomix-output.*,repomix.md,*.apkg,tests/**"
```

- **Scope:** 25 files. Same as full **minus `tests/**`** (5 suites + 4 fixtures). Keeps all spec/docs/product/tooling.
- **Cost:** ~62k tokens, ~218 KB. 33% cheaper than full. Still covers the entire product surface; just drops enforcement detail.
- **When:** you want fast iteration, token budget is tight, or you're asking purely about layout / CSS / front-mode logic and don't need the test harness. Not for tasks where you need to update or extend tests.

### 3. Spec-only — `repomix-spec.md` (architecture / product discussion)

```bash
repomix --style markdown \
  -o repomix-spec.md \
  --include "PRODUCT.md,MVP.md,ARCHITECTURE.md,QUALITY.md,TEST_STRATEGY.md,AGENTS.md,IMPLEMENTATION_PLAN.md,README.md,docs/**/*.md,HANDOFF.md" \
  --ignore "chat_history/**,conversations/**,Card 1 - Front.template.anki.*,backups/**,dist/**,reports/**,**/__pycache__/**,**/.ruff_cache/**,.anki_fields.json,repomix-output.*,repomix.md,*.apkg"
```

- **Scope:** 13 files. **Whitelist** of the methodology stack + ADRs + README/HANDOFF. No templates, no CSS, no tooling, no tests.
- **Cost:** ~17.5k tokens, ~74 KB.
- **When:** pure design / scope / invariant questions where code would distract the LLM ("is this feature in scope per `MVP.md`?", "does this violate `QUALITY.md`?", drafting an ADR). `--include` is intentional here: you explicitly want *only* docs.

### 4. Debug — `repomix-debug.md` (bug hunting with git context)

```bash
repomix --style markdown --output-show-line-numbers \
  -o repomix-debug.md \
  --ignore "chat_history/**,conversations/**,Card 1 - Front.template.anki.*,backups/**,dist/**,reports/**,**/__pycache__/**,**/.ruff_cache/**,.anki_fields.json,repomix-output.*,repomix.md,*.apkg" \
  --include-diffs --include-logs --include-logs-count 20
```

- **Scope:** full curated pack **plus** git working-tree + staged diffs and last 20 commits (messages + file lists).
- **Cost:** ~76k tokens without line numbers; ~94k with line numbers + logs (measured 76,295 + 1,207 log tokens for 20 commits).
- **When:** regression triage, "what changed since yesterday?", blame, reproducing a failing `./verify` run. `--include-diffs` shows uncommitted edits; `--include-logs` gives the LLM commit history context.

### 5. Token audit — print cost per file

```bash
repomix --verbose --token-count-tree \
  --ignore "chat_history/**,conversations/**,Card 1 - Front.template.anki.*,backups/**,dist/**,reports/**,**/__pycache__/**,**/.ruff_cache/**,.anki_fields.json,repomix-output.*,repomix.md,*.apkg"
# Threshold variant — only files ≥200 tokens:
repomix --token-count-tree 200 --ignore "chat_history/**,conversations/**,Card 1 - Front.template.anki.*,backups/**,dist/**,reports/**,**/__pycache__/**,**/.ruff_cache/**,.anki_fields.json,repomix-output.*,repomix.md,*.apkg"
```

- **Scope:** same as full curated, but prints a hierarchical token tree (dir + file counts, sorted by cost) **before** packing. Use to spot a new file that suddenly balloons context.
- **When:** before a big LLM session, or when you add fixtures / docs and want to budget.

### 6. XML variant — `repomix-output.xml` (Claude-optimized)

```bash
repomix --style xml \
  -o repomix-output.xml \
  --ignore "chat_history/**,conversations/**,Card 1 - Front.template.anki.*,backups/**,dist/**,reports/**,**/__pycache__/**,**/.ruff_cache/**,.anki_fields.json,repomix-output.*,repomix.md,*.apkg"
# With line numbers (costs extra):
repomix --style xml --output-show-line-numbers -o repomix-output.xml \
  --ignore "chat_history/**,conversations/**,Card 1 - Front.template.anki.*,backups/**,dist/**,reports/**,**/__pycache__/**,**/.ruff_cache/**,.anki_fields.json,repomix-output.*,repomix.md,*.apkg"
```

- **Scope:** identical to (1), just different wrapper.
- **Cost:** ~74.7k tokens without line numbers (vs 74.8k for markdown without line numbers — essentially parity). Markdown + line numbers is ~92k.
- **When:** Anthropic's [Use XML tags](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags) guidance suggests Claude parses `<file path="…">…</file>` slightly more reliably than markdown headings. If you live in Claude, use `xml`. For ChatGPT/Gemini/mixed use, `markdown` is fine.

---

## Persistent config — `repomix.config.json` (optional)

If you prefer bare `repomix` (no flags), create a committed config so every run is curated:

```bash
cat > repomix.config.json <<'JSON'
{
  "$schema": "https://repomix.com/schemas/repomix-config.json",
  "output": {
    "filePath": "repomix-output.md",
    "style": "markdown",
    "showLineNumbers": true,
    "fileSummary": true,
    "directoryStructure": true,
    "git": { "sortByChanges": true }
  },
  "ignore": {
    "useGitignore": true,
    "useDotIgnore": true,
    "useDefaultPatterns": true,
    "customPatterns": [
      "chat_history/**",
      "conversations/**",
      "Card 1 - Front.template.anki.*",
      "backups/**",
      "dist/**",
      "reports/**",
      "**/__pycache__/**",
      "**/.ruff_cache/**",
      ".anki_fields.json",
      "repomix-output.*",
      "repomix.md",
      "*.apkg"
    ]
  },
  "security": { "enableSecurityCheck": true }
}
JSON
# then just:
repomix
# or watch mode while editing templates:
repomix --watch
```

- Checked in, this makes bare `repomix` behave like command (1) above.
- Output becomes `repomix-output.md` (markdown + line numbers, 35 files, ~92k tokens). Remove `"showLineNumbers": true` to drop to ~75k tokens.
- Add a second config for the lean pack if you use it often: `repomix --config repomix-lean.config.json`.

> Do not commit `repomix-output.md`/`xml` — they are transient LLM context. `.gitignore` already excludes `dist/` and `backups/`; consider adding `repomix-output.*`.

---

## Flag glossary (what each flag does here)

| Flag | Docs meaning | Repo-specific effect |
|------|--------------|----------------------|
| `--style markdown|xml|json|plain` | Output wrapper. | `markdown` = headings + fenced blocks (recommended). `xml` = `<file>` tags (Claude-friendly, same token cost without line numbers). `json` = machine-parseable (`jq` friendly) but noisier for prose LLMs. `plain` = raw separators, avoid. |
| `--output-show-line-numbers` | Prefix each content line with `N:`. | +~17k tokens (+23%) but enables `path:line` refs per `AGENTS.md`. Keep for coding, drop for pure spec chat. |
| `-o, --output <file>` | Output path (default `repomix-output.xml`). | Always set explicitly; pattern `repomix-output.*` in `--ignore` prevents self-collection. |
| `--ignore <patterns>` | Comma-separated globs added to `.gitignore` + defaults. | Blacklist that strips the noise table above while auto-including any new doc/test/ADR. **Quote the whole value** so `Card 1 - …` spaces survive. |
| `--include <patterns>` | Whitelist — only these globs are packed. | Used only for spec-only (3): forces docs-only view. |
| `--compress` | Tree-sitter extraction of class/function signatures. | **Never use here.** Templates/CSS are not parsed as code; compression destroys Yomitan fixture HTML and numbered CSS section contracts (§6b/§6c). Measured: 35 files collapsed to 49k tokens but truncated meaningful markup. |
| `--remove-comments` / `--remove-empty-lines` | Strip comments / blank lines. | **Never use here.** Comments carry invariant docs (front-mode priority, Policy B, `LONG_INTERVAL_DAYS`, compactor scoping). Stripping them removes the LLM's guardrails. |
| `--token-count-tree [threshold]` | Print `dir/ (N tokens)` tree. | Audit tool. `200` threshold hides tiny files. |
| `--top-files-len <n>` | How many largest files to list in summary (default 5). | Default is fine; increase to 10 when auditing after bulk fixture changes. |
| `--include-diffs` / `--include-logs` / `--include-logs-count` | Append `git diff` + commit logs. | Debug-only. Include-logs adds ~1.2k tokens for 20 commits. |
| `--copy` | Copy output to OS clipboard (suppress file). | Handy for one-shot paste into a chat window. |
| `--no-security-check` | Skip Secretlint scan. | **Never use.** Keep enabled — AnkiConnect URL is `127.0.0.1:8765` and benign, but the scan is cheap. |
| `--verbose` / `--quiet` / `--stdout` | Logging control. | `--verbose` shows merged config + file counts (use for debugging the pack). `--stdout` pipes to another tool (`repomix --stdout | llm "…"`) . |

---

## What NOT to do

| Anti-pattern | Why it hurts this repo |
|--------------|------------------------|
| `repomix --compress` | Destroys `tests/fixtures/*.html` Yomitan markup and `Card 1 - Style.css` section headers that tests enforce. Output drops from 92k → 49k but loses the exact glossary shapes the compactor targets. |
| `repomix --remove-comments` | Front template header comment documents the entire mode priority + Policy B + Mature fallback. `Style.css` header documents version + product philosophy. Stripping them leaves the LLM guessing. |
| `repomix --remove-empty-lines` | CSS readability collapses; no token win worth the confusion. |
| `repomix --no-gitignore --no-default-patterns` | Re-includes `node_modules`/`dist`/`backups` etc. Never widen without an explicit `--ignore` to compensate. |
| Bare `repomix` with no ignore | Ships 215k tokens with stale Front copies and chat transcripts that cause the LLM to reference the wrong Front implementation. |

---

## Maintenance checklist

- [ ] Delete untracked backups already committed: see hygiene snippet above. After cleanup, `repomix --token-count-tree` should no longer list `Card 1 - Front.template.anki.*` as tracked.
- [ ] Verify line-numbers fit your model's budget: compare `repomix --style markdown` (75k) vs `--output-show-line-numbers` (92k). If context is tight, drop `--output-show-line-numbers` for spec sessions.
- [ ] Re-measure after bulk changes: `repomix --verbose --token-count-tree --ignore "…"` shows if a new fixture or prompt transcript re-inflated the pack.
- [ ] Keep `repomix.config.json` committed if your team uses bare `repomix`; otherwise document only CLI commands here.

---

## Repository scope note (for the LLM)

This is **not a generic app repo**. Fields live **only in the Anki UI** (never in the repo; bootstrap via `python3 fetch_anki_fields.py` → gitignored `.anki_fields.json`). Local `.template.anki` / `.css` are the single source of truth (`AGENTS.md` §1). Release is one command `./finish.sh "<msg>"` which runs `verify → stamp → sync → export → commit → push → release` (`ARCHITECTURE.md` Tooling). Vanilla JS/CSS only, scoped, resilient to WebView DOM re-use. Mature Word Mode is desktop-only (AnkiConnect content search, never picks candidate 0); mobile intentionally degrades to sentence front. Listening Policy B requires usable audio. `R` is Anki-owned. `:has()` is intentional architecture. Pack context should always include the full spec stack so the LLM respects these invariants.

