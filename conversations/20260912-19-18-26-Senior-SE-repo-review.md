# Session: Senior SE repo review

**Created:** 2026-09-12 19:18:26

---

## Conversation

### 🤖 Assistant
*2026-09-12 19:24:58*

read my repo, and give you honest thoughts as a sernior SE.

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

💭 **Reasoning:**

<details>
<summary>Click to expand reasoning</summary>

**Evaluating Repo for Senior Review**

The request is for a comprehensive review as a senior SE, so initial focus must be on code quality, architecture, and maintainability. A detailed examination of design patterns and adherence to best practices is needed. Plan to identify potential areas of concern or improvement.




</details>

#### 🔧 Tool: bash
**Status:** completed
**Title:** fd

**Input:**
```json
{
  "command": "fd"
}
```

**Output:**
```
AGENTS.md
ARCHITECTURE.md
Card 1 - Back.template.anki
Card 1 - Front.template.anki
Card 1 - Style.css
Design.md
IMPLEMENTATION_PLAN.md
MVP.md
New Folder/
PRODUCT.md
QUALITY.md
README.md
TEST_STRATEGY.md
chat_history/
chat_history/definition-truncation-handoff.md
chat_history/gemini_cli_prompts.txt
chat_history/opencode_prompts.txt
conversations/
conversations/20260909-13-38-47-Dynamic-layout-for-wide-screen.md
conversations/20260910-15-42-11-New-session-2026-09-10T14-42-1.md
conversations/20260910-19-58-16-Reading-codebase.md
conversations/20260912-01-55-22-Anki-Japanese-card-template-vi.md
conversations/images/
conversations/images/20260909-13-38-47-Dynamic-layout-for-wide-screens-0.png
dist/
docs/
docs/adr/
docs/adr/001-mature-word-mode-interval.md
docs/adr/002-definition-compactor-css.md
docs/adr/003-native-audio-delegation.md
docs/adr/004-single-command-release.md
fetch_anki_fields.py
finish.sh
release_apkg.py
sync_to_anki.py
tests/
tests/fixtures/
tests/fixtures/extended_definition_control.html
tests/fixtures/yomitan_daijirin_daijisen.html
tests/fixtures/yomitan_dict_label.html
tests/fixtures/yomitan_plain_gloss.html
tests/test_compactor.py
tests/test_front_modes.py
tests/test_layout.py
tests/test_templates.py
verify

```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

💭 **Reasoning:**

<details>
<summary>Click to expand reasoning</summary>

**Reviewing Available Project Documentation**

Examining the repository contents reveals a suite of markdown documents. These appear to outline product specifications, architectural design, quality considerations, and implementation strategies. Also present are architectural decision records (ADRs), which provide further insight into the project's evolution.




</details>

#### 🔧 Tool: read
**Status:** completed
**Title:** README.md

**Input:**
```json
{
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/README.md"
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/README.md</path>
<type>file</type>
<content>
1: # 🎴 Japanese Anki Note Template (Ergonomic & Responsive)
2: 
3: A modern, ultra-compact Japanese sentence-mining note type for Anki. Built for dense, information-efficient review on **Desktop (Arch Linux, Qt6)** and **Mobile (AnkiDroid, small screens)**.
4: 
5: ---
6: 
7: ## 🎥 Demo
8: 
9: [Screencast_20260903_034628.webm](https://github.com/user-attachments/assets/c3021cdb-7cfd-4cb1-b1a7-ff52a990e305)
10: 
11: ---
12: 
13: ## ✨ Features
14: 
15: - **🌙 Dual themes** — Tokyo Night dark (default) and Aki Paper light, following Anki's Night Mode.
16: - **🔢 Minimal by design** — every visible element must justify its screen space. The front is a pure retrieval surface (just the Japanese); the back is a quiet reading interface: target → reading → meaning → context, with secondary info collapsed behind `More ▾`. Anki is the SRS — no badges, dashboards, or grading UI.
17: - **📱 Fluid responsive layout** — `clamp()` sizing with no breakpoint jumps; sentence + picture context grid on desktop, single column on phones; container queries with a media-query fallback for old WebViews. Cards size to their content (no forced viewport fill).
18: - **🔤 Zero-reflow furigana** — hidden by default, revealed on hover (desktop) / tap (mobile); **`F`** pins full-card furigana on the back. Nothing ever shifts.
19: - **🔊 Native audio** — `文` / `言葉` buttons and Anki's own **`R`** shortcut delegate to Anki's replay link (never HTML5 audio), with re-tap debounce so audio can't overlap on AnkiDroid.
20: - **👁️ On-demand secondary info** — `T` reveals the translation; `More ▾` exposes the full Yomitan definition, extra context, kanji and general notes. Quiet by default.
21: - **🖼️ Lightbox** — tap any image for a full-screen overlay; closes on backdrop click or <kbd>Escape</kbd>.
22: - **🏷️ Behavioral tags** — tags drive card behavior (e.g. `#listening` forces the listening front) and are never rendered as decoration.
23: 
24: ---
25: 
26: ## 🃏 Front Card Modes
27: 
28: The front contains ONLY the thing being tested — the sentence itself is the retrieval prompt.
29: 
30: | Situation | Front shows |
31: | :--- | :--- |
32: | Definition present | Sentence (or Expression if no Sentence) |
33: | No definitions, but `Frequency` set (legacy cards) | Usual sentence — never the audio button |
34: | No definitions, no Frequency, `Sentence Audio` set | Listening-mode audio button |
35: | Card tagged `#listening` | Listening-mode audio button (deliberate listening exercise, even with glosses) |
36: | Nothing available | Sentence / Expression fallback |
37: | Sentence has no bold term + cloze trio complete | Rebuilt `prefix + `<b>`body`</b>` + suffix`, styled identically to a Yomitan sentence |
38: | Review interval ≥ 365 days | Word only (Mature Word Mode, see below) |
39: 
40: **Cloze fallback** (jidoushio mobile exports): when `Sentence` lacks its `<b>` target word, JS rebuilds it from `cloze-prefix` / `cloze-body` / `cloze-suffix` — but only if all three are non-empty, otherwise the sentence is kept as-is.
41: 
42: **Mature Word Mode** (anti-overlearning): old cards stop testing the word and start testing sentence recognition, so at `interval ≥ LONG_INTERVAL_DAYS` (default `365`, one constant in `Card 1 - Front.template.anki`) the front shows only the `Expression`. The interval is read live at render time — AnkiConnect (`guiCurrentCard` → `cardsInfo`, with a `findCards` content-search fallback for the Browse previewer) on desktop, the AnkiDroid JS API on mobile. Any failure degrades to the normal sentence front; listening cards are never touched; an anti-flash gate keeps the card hidden until the decision is made (500 ms fetch timeout, 1200 ms reveal cap).
43: 
44: **Listening semantics**: the audio button markup is gated on `Sentence Audio` and inert until a synchronous resolver confirms the listening condition — the classic audio-only field shape OR the `#listening` tag. Every other card (and every failure path, including no-JS) keeps the sentence front.
45: 
46: ---
47: 
48: ## 📖 Back Card
49: 
50: Typography does the work — no dashboard chrome:
51: 
52: 1. **Target + reading** — the headword with hover furigana, the largest element; pitch accent as quiet muted text.
53: 2. **Primary meaning** — **Definition Compactor** (CSS §6b) trims the Yomitan glossary to the first dictionary, max 2 senses, no appendices; **Definition Truncator** (§6c) caps it at 3 lines with a fade + `▼`, click expands and stays open.
54: 3. **Context** — the sentence (with hover furigana) plus the picture when present, side by side on wide screens.
55: 4. **Secondary info** — collapsed behind a quiet `More ▾`: translation (`T`), additional context, kanji notes, general notes, and the **full extended definition** (the compactor never touches it).
56: 5. A discreet **Context / Word / Listening** label explains the retrieval condition on hover; the source footer identifies the material.
57: 
58: ---
59: 
60: ## 🗂️ Fields
61: 
62: Fields are managed **exclusively inside the Anki UI** — the repo keeps no static list. For the live names + descriptions, run:
63: 
64: ```bash
65: python3 fetch_anki_fields.py   # dumps gitignored .anki_fields.json
66: ```
67: 
68: Current set (20): `Expression`, `Definition`, `Kanji Notes`, `Source`, `Sentence`, `Sentence (furigana)`, `Sentence Audio`, `Translation`, `Picture`, `context`, `Notes`, `Word Audio`, `Pitch Accent`, `furigana`, `reading`, `cloze-prefix`, `cloze-body`, `cloze-suffix`, `Frequency`, `Extended definition`. Yomitan-mining compatible.
69: 
70: ---
71: 
72: ## 🚀 Installation
73: 
74: **Option 1 — Quick install (recommended):** download `anki-japanese-template.apkg` from [Releases](https://github.com/mansourvery-hub/anki-japanese-template/releases), import via **File → Import**, then delete the sample cards (the note type is retained).
75: 
76: **Option 2 — Sync from source** (needs Anki + [Anki-Connect](https://ankiweb.net/shared/info/2055492159), Python 3 stdlib only):
77: ```bash
78: git clone https://github.com/mansourvery-hub/anki-japanese-template.git
79: cd anki-japanese-template
80: python3 sync_to_anki.py    # snapshots live state to backups/, then pushes Front/Back/CSS
81: python3 release_apkg.py    # exports sample deck to dist/*.apkg
82: ```
83: 
84: **Option 3 — Manual:** paste `Card 1 - Front.template.anki`, `Card 1 - Back.template.anki`, and `Card 1 - Style.css` into the card template editor (**Tools → Manage Note Types → Cards**).
85: 
86: ---
87: 
88: ## 🛠️ Project Structure
89: 
90: ```
91: ├── Card 1 - Front.template.anki   # Front HTML: modes, cloze fallback, Mature Word Mode
92: ├── Card 1 - Back.template.anki    # Back HTML: header, definition, sentence, side column
93: ├── Card 1 - Style.css             # Themes, layout, compactor (§6b), truncator (§6c)
94: ├── fetch_anki_fields.py           # Read-only dump of live Anki fields (see above)
95: ├── sync_to_anki.py                # Push templates/CSS to Anki (pre-sync backup)
96: ├── release_apkg.py                # Export sample deck to dist/*.apkg
97: ├── verify                         # Local quality gate (tests only, no side effects)
98: ├── finish.sh                      # One command: verify + sync + export + commit + push + release
99: ├── PRODUCT.md / MVP.md            # Product intent / current scope
100: ├── ARCHITECTURE.md + docs/adr/    # Technical structure / lasting decisions
101: ├── QUALITY.md / TEST_STRATEGY.md  # Invariants / how they are verified
102: ├── IMPLEMENTATION_PLAN.md         # Task graph + status
103: ├── tests/                         # test_compactor.py + test_templates.py (run by finish.sh)
104: ├── chat_history/                  # Archived agent prompts
105: ├── dist/                          # Exported .apkg (gitignored, GitHub Release asset)
106: ├── backups/                       # Pre-sync Anki snapshots (gitignored)
107: ├── AGENTS.md                      # Agent operating rules
108: └── README.md                      # This file
109: ```
110: 
111: ---
112: 
113: ## 🔄 Development Workflow
114: 
115: Edit the local `.template.anki` / `.css` files (never inside Anki's UI), then run one command:
116: 
117: ```bash
118: ./finish.sh "scope: what changed"
119: # --local: sync + export + commit only · --minor: bump v1.x.0 · --prompt "text": archive prompt
120: ```
121: 
122: This runs tests, syncs to Anki, exports the apkg, commits, pushes, and publishes a tagged release. `tests/` covers the compactor selectors and template invariants (furigana ban on front, audio/lightbox semantics, balanced conditionals, Mature Mode + cloze + truncator rules).
123: 
124: ---
125: 
126: Built with Opencode and Gemini CLI. MIT License.

(End of file - total 126 lines)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: read
**Status:** completed
**Title:** PRODUCT.md

**Input:**
```json
{
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/PRODUCT.md"
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/PRODUCT.md</path>
<type>file</type>
<content>
1: # PRODUCT.md — Japanese sentence-mining note type
2: 
3: Authoritative source for **what the product is supposed to do**.
4: Architecture, plans, and agent instructions all defer to this file.
5: 
6: ## Problem
7: 
8: Yomitan sentence-mining cards are verbose and ergonomically poor out of the
9: box: oversized headwords, full multi-dictionary glosses, dead screen space,
10: clunky audio controls, and a familiar sentence that becomes the retrieval cue
11: once a card is mature (overlearning). Review on a small phone (Galaxy A50) is
12: especially wasteful.
13: 
14: ## Target users
15: 
16: - Solo learner (the maintainer) mining Japanese sentences via Yomitan /
17:   jidoujisho into Anki.
18: - Review contexts: Anki Desktop Qt6 WebEngine (Arch Linux, widescreen) and
19:   AnkiDroid WebView (Samsung Galaxy A50, small screen).
20: - Installs via the released `.apkg` (GitHub Release asset), or syncs from
21:   source with Anki-Connect.
22: 
23: ## Core design philosophy
24: 
25: > **Every visible element must justify its existence and its screen space.**
26: 
27: The card is a **minimal Japanese-reading interface**, not a dashboard,
28: dictionary UI, or mini-SRS. Anki is the SRS: it handles scheduling and
29: grading. The template's only job is to present the Japanese item clearly,
30: provide the necessary context for retrieval, and get out of the way.
31: 
32: - The fundamental learning task is: **Japanese word → reading + meaning.**
33:   No English→Japanese production, no custom grading or confidence buttons,
34:   no additional learning-mode systems.
35: - The front is a pure retrieval surface: it contains ONLY the thing being
36:   tested (sentence with target, mature word, or listening audio button).
37: - The back establishes hierarchy through typography — target → reading →
38:   meaning → context — with everything secondary collapsed by default.
39: - Removal beats addition: when uncertain between adding UI and removing
40:   it, remove; between always-visible and collapsed/hover, prefer
41:   collapsed.
42: 
43: ## Mining / card-quality invariant
44: 
45: > **The mined sentence shown on the front must be independently
46: > understandable enough to solve the card.** Additional surrounding
47: > context (previous/next paragraph, dialogue) is supplementary reference
48:   material and must never be required for the card to be intelligible.
49: 
50: ```
51: Front sentence = self-contained learning unit
52: Additional surrounding context = optional reference material
53: ```
54: 
55: This is a mining invariant, not a UI preference: a card whose front needs
56: off-screen context to be solvable is a bad mine and should be re-mined.
57: 
58: ## Core user journeys
59: 
60: 1. **Mine → review sentence card.** Yomitan fills Expression / Sentence /
61:    Definition / audio / Frequency; the front tests sentence recognition, the
62:    back shows the hierarchy: target+reading, compacted meaning, context.
63: 2. **Review mature card as word card.** Cards with interval ≥
64:    `LONG_INTERVAL_DAYS` show only the Expression on the front
65:    (anti-overlearning), with silent fallback to the sentence front. The
66:    familiar sentence must never become the retrieval cue.
67: 3. **Review listening card.** Cards whose audio is the test (audio-only
68:    fields, or the deliberate `#listening` tag) show a single large audio
69:    button; normal cards are unaffected.
70: 4. **Expand information on demand.** Secondary info (translation,
71:    extended definition, additional context, kanji/general notes) sits
72:    behind one quiet `More ▾` toggle; `T` reveals the translation, `F`
73:    toggles full-card furigana on the back, picture opens the lightbox.
74: 5. **Install / update.** Import the release `.apkg`, or push local
75:    templates/CSS to the live profile and re-export via `finish.sh`.
76: 
77: ## Functional requirements
78: 
79: - Front modes (in priority order): Definition/Extended-definition →
80:   sentence; legacy Frequency-only → sentence; listening (classic
81:   audio-only fields **or** `#listening` tag) → listening button, hidden
82:   by default and activated by a synchronous resolver; otherwise
83:   sentence/Expression fallback; cloze trio rebuild when Sentence
84:   lacks `<b>`; mature interval-gated word-only front. The sentence
85:   front is the universal fallback for every failure path.
86: - Back hierarchy: word/furigana target (largest), quiet pitch text,
87:   compacted primary definition (§6b), context (sentence + picture as
88:   core information), native circular audio (`文`/`言葉`), secondary
89:   information collapsed behind `More ▾` (translation, context, kanji
90:   notes, notes, full extended definition), source footer, discreet
91:   retrieval-state label (Context/Word/Listening, hover-explained).
92: - Mature Word Mode: live interval read at render time (desktop AnkiConnect
93:   `guiCurrentCard`→`cardsInfo` + `findCards` content-search fallback for the
94:   Browse previewer; mobile AnkiDroid JS API `ankiGetCardInterval()` only);
95:   never fetch AnkiConnect from a mobile WebView; any failure → sentence
96:   front; listening fronts untouched.
97: - Tags are behavioral metadata, never decoration: hidden probes only;
98:   `#listening` forces listening behavior; extensible for future
99:   behavior-related tags without card redesign.
100: - Tooling: `sync_to_anki.py` pushes Front/Back/CSS with a pre-sync snapshot
101:   to `backups/<timestamp>/`; `release_apkg.py` exports deck
102:   `My Life Decks::Japanese::anki-japanese-template` via `exportPackage`;
103:   `finish.sh` runs tests → sync → export → commit → push → release.
104: 
105: ## UX requirements
106: 
107: - Ultra-compact, content-driven height (no viewport fill, no dead space);
108:   empty space on the front is acceptable — never filled with UI.
109: - Fluid `clamp()` sizing phone → 4K; sentence+picture context grid on
110:   desktop (container queries + media-query fallback), single column on
111:   phones.
112: - Zero-reflow furigana (hidden, hover/tap reveal, absolute ruby); `F`
113:   toggles full-card furigana on the back.
114: - Native-only audio (delegate to Anki replay link, re-tap debounce, ring
115:   pulse — never HTML5 `Audio`); `R` (Anki native) remains the primary
116:   audio path.
117: - Dual themes (Tokyo Night dark / Aki Paper light, follows Anki Night Mode),
118:   accent color reserved for target highlighting and interactive states,
119:   `prefers-reduced-motion` support, keyboard focus indicators, aria
120:   labels/roles.
121: - Japanese remains the dominant visual language: English typography never
122:   competes with it.
123: 
124: ## Constraints
125: 
126: - Vanilla JS/CSS only, scoped, resilient to Anki WebView DOM re-use.
127: - Fields live **exclusively in the Anki UI**; repo keeps no static field
128:   list (`fetch_anki_fields.py` → gitignored `.anki_fields.json` is the only
129:   source).
130: - Local `.template.anki` / `.css` files are the single source of truth —
131:   never edit inside the Anki UI.
132: - Screen real estate is precious: no debug badges or verbose header labels.
133: - Stdlib-only Python tooling (no third-party runtime deps; test-only deps
134:   allowed).
135: 
136: ## Non-goals
137: 
138: - New Anki note-type fields, add-ons, or Python-at-review solutions.
139: - Multi-note-type theming system or generic card framework.
140: - Enterprise release management (solo `finish.sh` flow is enough).
141: - Server/cloud sync, collaboration, analytics.
142: - English→Japanese production mode, custom grading UI, confidence
143:   buttons, learning-mode systems beyond context/word/listening.
144: 
145: ## Important assumptions
146: 
147: - Yomitan markup shape (`.yomitan-glossary`, `data-sc-*` attributes) is
148:   stable enough for structural CSS scoping; drift is caught by fixtures.
149: - AnkiConnect on `127.0.0.1:8765` (desktop) and the AnkiDroid JS bridge
150:   (reviewer only) remain the interval sources; both can be absent.
151: - One card type ("Card 1"); model name
152:   `Japanese Note type (Sentence card by Default)` is stable.
153: 
154: ## Open questions
155: 
156: - None blocking. Candidate evolution items live in `MVP.md` (Deferred) and
157:   `IMPLEMENTATION_PLAN.md` (roadmap).

(End of file - total 157 lines)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: read
**Status:** completed
**Title:** ARCHITECTURE.md

**Input:**
```json
{
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/ARCHITECTURE.md"
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/ARCHITECTURE.md</path>
<type>file</type>
<content>
1: # ARCHITECTURE.md — authoritative technical structure
2: 
3: Covers *how the software is structured* for the `MVP.md` scope. Additional
4: documents are created only where they would otherwise make this file unwieldy
5: or where a domain needs an independently maintained contract. Current extras:
6: `docs/adr/` (decisions with lasting consequences); no separate
7: `DATA_MODEL.md` / `API_CONTRACTS.md` / `STATE_MODEL.md` — the project is too
8: small to justify them.
9: 
10: ## System map
11: 
12: ```text
13: Anki note fields (live in Anki UI, never in repo)
14:   │  Yomitan / jidoujisho mining
15:   ↓
16: Card 1 - Front.template.anki ──→ review front (sentence / word / listening)
17: Card 1 - Back.template.anki  ──→ review back (grid: main + side columns)
18: Card 1 - Style.css           ──→ themes, layout, compactor, truncator
19:   │  vanilla JS (scoped, DOM-reuse safe), no libraries
20:   ↓
21: Anki renderers: Desktop Qt6 WebEngine · AnkiDroid WebView
22:   │  live services at render time: AnkiConnect :8765 (desktop only),
23:   │  AnkiDroid JS bridge (mobile reviewer only)
24:   ↓
25: Tooling (stdlib-only): fetch_anki_fields.py · sync_to_anki.py ·
26:                        release_apkg.py · verify · finish.sh
27: ```
28: 
29: ## Components
30: 
31: ### Front (`Card 1 - Front.template.anki`)
32: 
33: A pure retrieval surface: only the tested Japanese renders. HTML
34: conditionals pick the branch; a synchronous JS resolver finalizes the
35: listening decision; async JS finalizes Mature Word Mode:
36: 
37: ```text
38: Definition / Extended definition? ──yes──→ sentence-display
39:         │ no
40: Frequency (legacy)? ──yes──→ sentence-display (never audio)
41:         │ no
42: Sentence Audio? ──yes──→ sentence-display + hidden listening-view
43:         │ no                      │
44: sentence-display fallback          └─ synchronous LISTENING RESOLVER:
45:                                     classic audio-only fields OR
46:                                     #listening tag? → activate audio
47:                                     front, drop the sentence;
48:                                     else the markup stays inert
49:         │
50: cloze fixup: Sentence has no <b> AND cloze trio complete?
51:         │ yes → prefix + <b>body</b> + suffix
52:         │
53: Mature check (not listening, Expression non-empty,
54:               interval ≥ LONG_INTERVAL_DAYS=365)?
55:         │ yes → .word-mode: front-word-display only
56:         │ no  → sentence front (also the universal fallback)
57: ```
58: 
59: Hidden behavioral probes never render visibly: the cloze trio, a
60: `{{#Tags}}` probe carrying the `#listening` signal, and
61: Definition/Extended/Frequency presence markers consumed by the resolver.
62: The resolver writes `window.__ajtFrontState` for the back's discreet
63: state label. Interval retrieval is **platform-exclusive**: mobile uses
64: only the AnkiDroid bridge (`ankiGetCardInterval()`, constructor + direct
65: shapes, stub guard, timeouts, 700 ms late-injection poll); desktop uses
66: only AnkiConnect (`guiCurrentCard`→`cardsInfo`, `findCards`
67: content-search fallback for the Browse previewer — no `note:` clause,
68: `{{Type}}` is not the model name, 500 ms fetch timeout). Anti-flash gate
69: (`visibility:hidden` → reveal, 1200 ms safety cap); blank sentence
70: blocks are removed after the cloze fixup. See `docs/adr/001-*`.
71: 
72: ### Back (`Card 1 - Back.template.anki`)
73: 
74: Single quiet column with typography-driven hierarchy:
75: 
76: ```text
77: card-container
78:  ├── .retrieval-state (hidden unless front set it: Context/Word/Listening,
79:  │                      hover-explained, never a big badge)
80:  ├── word-display (target + furigana hover — largest element)
81:  ├── .pitch-quiet (muted supplement to the reading)
82:  ├── definition-box.primary-definition (compacted §6b, 3-line §6c)
83:  ├── .audio-row (文/言葉 native-delegating buttons, :has() empty guard)
84:  ├── .context-grid (sentence + picture; row on wide screens, stacked on phones)
85:  ├── .more-section (hidden) + .more-toggle "More ▾"
86:  │    └── translation (click/T) · context · kanji notes · notes · full
87:  │        extended definition (.extended-full — compactor never touches it)
88:  └── .source-footer
89: ```
90: 
91: JS controllers (all idempotent under WebView DOM re-use): state-label
92: renderer (reads `window.__ajtFrontState`), More toggle (one-way reveal;
93: section+button self-remove when secondary content is absent),
94: native-only circular audio (`playCircularAudio` → sibling replay link
95: click, re-tap debounce, ring pulse), definition truncator (blank boxes
96: removed, then measure → `.is-truncated` → one-way `.is-expanded`),
97: lightbox (backdrop-click / `Escape` close, alt preserved), back-only
98: keyboard shortcuts (`F` full-card furigana, `T` translation reveal).
99: 
100: ### Style (`Card 1 - Style.css`)
101: 
102: Numbered sections are the contract: §1 tokens/themes (no `--freq-*`:
103: accent is reserved for the target and interactive states), §2 containers,
104: §3 retrieval-state label + More toggle, §4 context grid + desktop
105: overrides, §5 front type, §5b word-mode swap, §6 back hierarchy
106: (word/pitch/audio), **§6b Definition Compactor** (first dictionary, ≤2
107: senses, no appendices, `.primary-definition`-scoped), §6c truncator
108: (3-line cap + fade + chevron), §7 audio rings, §8 sentence/translation +
109: secondary blocks, §9 zero-reflow ruby + §9b full-card furigana mode,
110: §10 media/lightbox, §11 footer, §12 listening (inert until
111: `.listening-mode`), §13 mobile, §14 deletable Fuji backdrop, §15 reduced
112: motion.
113: 
114: ### Tooling
115: 
116: ```text
117: fetch_anki_fields.py → .anki_fields.json (gitignored, read-only dump)
118: sync_to_anki.py      → snapshot backups/<ts>/, push Front/Back/CSS
119: release_apkg.py      → exportPackage deck → dist/*.apkg (gitignored)
120: verify               → local quality gate (tests only, no side effects)
121: finish.sh            → verify → stamp → sync → export → commit → push → release
122: tests/               → test_compactor.py + test_templates.py
123:                         + test_front_modes.py + test_layout.py
124: ```
125: 
126: Fields are **not** a repo artifact: the Anki UI owns them; agents bootstrap
127: via `fetch_anki_fields.py` every session.
128: 
129: ## Diagrams
130: 
131: Produced only where prose is ambiguous. The two graphs above (front-mode
132: decision, back grid) are the standing set; sequence/state/entity diagrams
133: are omitted — no complex async choreography, state machine, or persistent
134: entity graph exists beyond what is shown.
135: 
136: ## Key decisions (summaries; full records in `docs/adr/`)
137: 
138: - **001** Mature interval via platform-exclusive live read (no
139:   `{{Interval}}`, no new fields/add-ons; mobile never touches AnkiConnect).
140: - **002** Definition Compactor as structural CSS (dictionary-agnostic,
141:   `.primary-definition`-scoped; extended definition untouched).
142: - **003** Native-only audio delegation (no `new Audio()`; sibling replay
143:   link; debounce; visually-hidden-not-`display:none` source).
144: - **004** Single-command release (`finish.sh`; `verify` as the side-effect-free
145:   subset; snapshots before overwrite).
146: 
147: ## Evolution rule
148: 
149: Small change → implement normally. Moderate change → update this file
150: (+ ADR when justified) first, then add tasks. Major change → stop feature
151: work, run an explicit architecture-change effort with a migration plan.

(End of file - total 151 lines)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: read
**Status:** completed
**Title:** QUALITY.md

**Input:**
```json
{
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/QUALITY.md"
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/QUALITY.md</path>
<type>file</type>
<content>
1: # QUALITY.md — properties that must remain true
2: 
3: Answers *what must remain true*. `TEST_STRATEGY.md` answers *how it is
4: mechanically verified*. Code implements; tests enforce.
5: 
6: ## Architecture invariants
7: 
8: - Local `.template.anki` / `.css` files are the single source of truth;
9:   never instruct edits inside the Anki UI.
10: - Fields live in the Anki UI only; the repo keeps no static field list.
11: - Vanilla JS/CSS only, scoped, DOM-reuse safe (idempotent init, no globals
12:   beyond the documented `window.*` controllers).
13: - Single `LONG_INTERVAL_DAYS = 365` const; no hard-coded `>= 365` elsewhere.
14: - CSS section numbers (§6b compactor, §6c truncator, §14 backdrop) are stable
15:   contracts referenced by tests and docs.
16: 
17: ## Front invariants
18: 
19: - Front renders **no** furigana filter/field (`Sentence (furigana)` ban);
20:   raw `{{edit:Sentence}}` / `{{edit:Expression}}` only.
21: - Front shows **no UI** beyond the tested Japanese: no tags, badges,
22:   metadata, labels, or controls (hidden behavioral probes only:
23:   cloze trio, `#listening` tag probe, field-presence markers).
24: - Balanced `{{#field}}` / `{{^field}}` / `{{/field}}` conditionals.
25: - The sentence front is the **universal fallback**: every listening /
26:   mature failure path degrades to it, never to a blank or hung card.
27: - Listening activation is a synchronous hidden-by-default resolver:
28:   the listening markup renders only under `{{#Sentence Audio}}` and is
29:   inert until the resolver confirms classic audio-only fields OR the
30:   `#listening` tag; it then removes the sentence display. No JS =>
31:   sentence front.
32: - Listening cards never enter Mature Word Mode and skip all interval
33:   retrieval.
34: - Interval has no `{{Interval}}` marker and no `note:` search clause
35:   (`{{Type}}` is the scheduling type, not the model): desktop AnkiConnect
36:   only, mobile AnkiDroid bridge only; mobile never fetches
37:   `127.0.0.1:8765`.
38: - Any retrieval failure degrades to the sentence front; anti-flash
39:   `visibility:hidden` gate with a bounded reveal cap.
40: - Cloze rebuild fires only when Sentence lacks `<b>`/`<strong>` **and** the
41:   full prefix/body/suffix trio is non-empty; rebuild uses `<b>`.
42: - AnkiDroid stub bridges (`signal:jsapi`) are never invoked;
43:   `{success:false}` never becomes an interval; numeric strings and
44:   JSON-encoded responses parse; bridge calls time out.
45: 
46: ## Back invariants
47: 
48: - Back hierarchy is typography-driven: word-display (largest) → pitch
49:   quiet text → definition → sentence context → secondary collapsed.
50:   No sticky tags bar, no frequency/pitch badges, no oversized controls.
51: - Secondary information (translation, context, kanji notes, notes,
52:   full extended definition) lives inside `.more-section`, collapsed by
53:   default behind one quiet `More ▾` toggle; the toggle and section
54:   self-remove when no secondary content exists.
55: - The retrieval-state label (`Context` / `Word` / `Listening`) is
56:   hidden by default, appears only when `window.__ajtFrontState` is
57:   set, is hover-explanatory, and never a large colored badge.
58: - Keyboard shortcuts on the back: `F` toggles full-card furigana
59:   (`.furigana-mode`), `T` reveals the translation (opening More first);
60:   shortcuts never fire in inputs/contentEditable.
61: - Every circular audio button has an `aria-label`; replay source is a
62:   **sibling** `.raw-audio-source` (never inside `<button>`, never
63:   `display:none`); playback delegates to the native replay link; re-tap is
64:   debounced; `playCircularAudio` starts with `resetAudioState`; no `new
65:   Audio()`, no `is-paused` remnants, no `div`-inside-`button`.
66: - Lightbox closes only on backdrop click (`e.target === overlay`) or
67:   `Escape`; overlay carries dialog semantics; cloned image preserves `alt`.
68: - Definition expand is one-way (never re-collapses); `.is-truncated` is set
69:   only on real overflow; no-JS still shows the full definition.
70: - No JS font-scaler overrides CSS (`.sentence-japanese` `clamp()` is the
71:   sizing authority).
72: 
73: ## CSS invariants
74: 
75: - Zero-reflow furigana: absolute `ruby rt`, hidden until
76:   `:hover`/`:active`/`:focus`; `F` mode pins all rt visible with no
77:   reflow (same geometry).
78: - Content-driven card height (no `100vh`/`100dvh` fill); `container-type:
79:   inline-size` present; the context grid (sentence + picture) has a
80:   media-query fallback.
81: - Compactor hide rules all scoped to `.primary-definition`; the full
82:   extended definition (`.extended-full` inside More) stays untouched.
83: - Word-mode swap rules exist and never touch `.listening-view`; the
84:   listening-view is inert until `.listening-mode` activates it.
85: - `:focus-visible` indicators and `prefers-reduced-motion` present.
86: - Accent color is reserved for target highlighting and interactive
87:   states; no per-content-type semantic color palette (no `--freq-*`).
88: 
89: ## Empty-field collapse (space discipline)
90: 
91: - Every rendered field is enclosed in an Anki `{{#field}}` conditional —
92:   except the hidden cloze-probe trio, the hidden behavioral probes
93:   (`tags-probe`, field-presence markers), and the front word probe
94:   (`display:none` default, word-mode gate only).
95: - Unconditionally rendered shells collapse when all conditional children are
96:   absent: `.audio-row` via `:has()` guards; `.more-section` +
97:   `.more-toggle` self-remove via JS cleanup.
98: - Degenerate content removes itself instead of leaving chrome behind:
99:   blank definition/sentence blocks are removed (front runs after the cloze
100:   fixup, before the reveal); empty secondary blocks inside More are
101:   stripped.
102: - Net rule: no padding, border, or margin may survive an empty field.
103: 
104: ## Tooling / process invariants
105: 
106: - Python tooling stays stdlib-only; backups use microsecond timestamps;
107:   snapshots happen **before** any overwrite; empty live state aborts sync.
108: - `finish.sh` no-op runs never publish a release.
109: - Every user prompt is archived to `chat_history/opencode_prompts.txt`
110:   before/with the commit that follows it.

(End of file - total 110 lines)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: read
**Status:** completed
**Title:** TEST_STRATEGY.md

**Input:**
```json
{
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/TEST_STRATEGY.md"
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/TEST_STRATEGY.md</path>
<type>file</type>
<content>
1: # TEST_STRATEGY.md — how QUALITY.md is mechanically verified
2: 
3: ```text
4: QUALITY.md (WHAT must remain true)
5:   → TEST_STRATEGY.md (HOW it is verified)
6:     → tests / linters / headless checks / CI
7: ```
8: 
9: ## Layers (narrow → broad)
10: 
11: ```text
12: tiny brick test → targeted suite → ./verify → CI (clean env)
13: ```
14: 
15: While iterating, run the targeted suite; before declaring a task complete,
16: run `./verify`; CI re-runs `./verify` after every push.
17: 
18: ## Enforcement map
19: 
20: | Requirement (QUALITY.md) | Enforcement |
21: | --- | --- |
22: | Compactor keeps 1st dictionary, ≤2 senses, no appendices; extended definition untouched; rules scoped to `.primary-definition` | `tests/test_compactor.py` — extracts real `display:none` rules from CSS §6b, applies to `tests/fixtures/*.html` (bs4 + soupsieve) |
23: | Front furigana ban; raw Sentence/Expression present | `tests/test_templates.py` §1 |
24: | Audio aria-labels; native-only controller; sibling replay source; debounce; restart-only | `tests/test_templates.py` §§2–3b |
25: | Cloze probe shape, trio gate, `<b>` rebuild, bold guard | `tests/test_templates.py` §2c |
26: | Lightbox backdrop-only close, dialog semantics, alt | `tests/test_templates.py` §4 |
27: | Balanced Anki conditionals | `tests/test_templates.py` §5 |
28: | Minimal redesign: no tags bar / frequency badges; More collapse; state label; F/T shortcuts; listening resolver wiring | `tests/test_templates.py` §§6b–6c |
29: | `:focus-visible`, reduced motion, content-driven sizing, context-grid fallback, clamp() authority, no JS font override | `tests/test_templates.py` §§6–7 |
30: | Mature Word Mode: const, platform-exclusive retrieval, no `note:` clause, stub/timeout/fallback rules, anti-flash gate, word-mode CSS | `tests/test_templates.py` §8b |
31: | Stdlib-only sync, microsecond backups, finish.sh no-op guard | `tests/test_templates.py` §9 |
32: | Content-driven height, no h-overflow, furigana containment, type hierarchy, 3-line clamp + one-way expand, listening target size, context grid, More collapsed by default, footer containment | `tests/test_layout.py` — headless Chrome on the **real** stylesheet; skipped gracefully when Chrome is absent |
33: | Listening resolver behavior: classic audio-only fields and `#listening` tag activate the audio front; gloss/no-tag, no-audio, and Frequency-legacy shapes keep the sentence front | `tests/test_front_modes.py` — extracts the real resolver from the front template and runs 6 state harnesses in headless Chrome; skipped gracefully when Chrome is absent |
34: | Clean-environment pass, no forgotten files/deps | CI (`.github/workflows/verify.yml`) runs `./verify` |
35: | Every UI element collapses when its field is empty | `tests/test_templates.py` §10 — conditional-enclosure parser over Front/Back, `:has()` shell-guard checks, JS self-removal checks |
36: 
37: ## The gate
38: 
39: `./verify` = the repository's complete mandatory **local** quality gate.
40: Side-effect free: it never touches Anki, never writes releases, never
41: commits. `finish.sh` step 0 delegates to it, so the gate and the release
42: pipeline can never disagree.
43: 
44: ## Regression rule (inside the dev loop, not a separate phase)
45: 
46: ```text
47: bug → diagnose → fix → add regression test → verify → commit
48: ```
49: 
50: Every escaped bug earns a permanent test: compactor regressions → new
51: fixture/assertion; template/CSS regressions → new `test_templates.py`
52: check; layout regressions → new `test_layout.py` probe assertion.
53: 
54: ## Dependencies
55: 
56: - `test_compactor.py`: `beautifulsoup4` + `soupsieve` (test-only).
57: - `test_templates.py`: stdlib only.
58: - `test_front_modes.py`: headless Chrome if present, else skip (pass).
59: - `test_layout.py`: headless Chrome if present, else skip (pass).

(End of file - total 59 lines)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: read
**Status:** completed
**Title:** IMPLEMENTATION_PLAN.md

**Input:**
```json
{
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/IMPLEMENTATION_PLAN.md"
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/IMPLEMENTATION_PLAN.md</path>
<type>file</type>
<content>
1: # IMPLEMENTATION_PLAN.md — task graph + status
2: 
3: The graph is part of the plan (not a substitute): the graph says *what
4: depends on what*, the task entries say *what each node means*. This is a
5: task/slice graph, not a todo list (`Build frontend` would not qualify).
6: 
7: ## Dependency graph
8: 
9: ```text
10:                     ┌───────────────────┐
11:                     │ T1 fields bootstrap│
12:                     └─────────┬─────────┘
13:                               │
14:                     ┌─────────┴─────────┐
15:                     ↓                   ↓
16:             ┌───────────────┐   ┌───────────────┐
17:             │ T2 front modes │   │ T3 back grid  │
18:             └───────┬───────┘   └───────┬───────┘
19:                     │                   │
20:                     ↓                   ↓
21:             ┌───────────────┐   ┌───────────────┐
22:             │ T4 mature mode │   │ T5 compactor  │
23:             └───────┬───────┘   └───────┬───────┘
24:                     │                   │
25:                     └─────────┬─────────┘
26:                               ↓
27:                     ┌───────────────────┐
28:                     │ T6 audio/lightbox │
29:                     └─────────┬─────────┘
30:                               │
31:                               ↓
32:                     ┌───────────────────┐
33:                     │ T7 responsive/    │
34:                     │ themes/density    │
35:                     └─────────┬─────────┘
36:                               │
37:                               ↓
38:                     ┌───────────────────┐
39:                     │ T8 verify gate +  │
40:                     │ regression tests  │
41:                     └─────────┬─────────┘
42:                               │
43:                               ↓
44:                     ┌───────────────────┐
45:                     │ T9 release loop   │
46:                     │ (sync/export/tag) │
47:                     └─────────┬─────────┘
48:                               │
49:                               ↓
50:                     ┌───────────────────┐
51:                     │ T10 methodology   │
52:                     │ refactor (this)   │
53:                     └─────────┬─────────┘
54:                               │
55:                               ↓
56:                     ┌───────────────────┐
57:                     │ T11 empty-field   │
58:                     │ collapse          │
59:                     └─────────┬─────────┘
60:                               │
61:                               ↓
62:                     ┌───────────────────┐
63:                     │ T12 minimal-       │
64:                     │ interface redesign │
65:                     └───────────────────┘
66: ```
67: 
68: Dependencies: `T1 → {T2, T3} → {T4, T5} → T6 → T7 → T8 → T9 → T10 → T11 → T12`.
69: T2/T3 are parallelizable; T4 needs T2; T5 needs T3.
70: 
71: ## Tasks
72: 
73: - **T1 — Field bootstrap.** `fetch_anki_fields.py` + gitignored
74:   `.anki_fields.json`; agents read exact names per session. Status: COMPLETE.
75: - **T2 — Front modes.** Sentence/Expression, listening button,
76:   Frequency-legacy path, fallback, cloze-trio rebuild. Status: COMPLETE.
77: - **T3 — Back grid.** Tags, word header, sentence/translation/context, side
78:   column, footer; DOM-reuse-safe controllers. Status: COMPLETE.
79: - **T4 — Mature Word Mode.** `LONG_INTERVAL_DAYS` gate, platform-exclusive
80:   interval retrieval, fallbacks, anti-flash reveal. Status: COMPLETE.
81: - **T5 — Definition Compactor + truncator.** CSS §6b structural scoping +
82:   §6c 3-line one-way expand. Status: COMPLETE.
83: - **T6 — Audio + lightbox.** Native delegation, debounce, sibling source;
84:   backdrop/`Escape` close. Status: COMPLETE.
85: - **T7 — Responsive/themes/density.** Clamps, container queries + fallback,
86:   zero-reflow ruby, Tokyo Night / Aki Paper, backdrop, reduced motion.
87:   Status: COMPLETE.
88: - **T8 — Verify gate + regression tests.** `verify`, `test_compactor.py`,
89:   `test_templates.py`, `test_layout.py`, CI. Status: COMPLETE (this refactor
90:   introduces `verify` + CI; suites pre-exist).
91: - **T9 — Release loop.** `sync_to_anki.py` (pre-sync snapshots),
92:   `release_apkg.py` (`exportPackage`), `finish.sh` one-command flow, apkg as
93:   Release asset only. Status: COMPLETE.
94: - **T10 — Methodology refactor.** Adopt PRODUCT/MVP/ARCHITECTURE/QUALITY/
95:   TEST_STRATEGY/PLAN + slim AGENTS.md + `verify`/CI without changing card
96:   behavior. Status: COMPLETE (`./verify` 129/129 green; released with this
97:   commit).
98: - **T11 — Empty-field collapse.** QUALITY rule + `:has()` shell guards +
99:   degenerate-content self-removal + enclosure parser test (§10). Turns the
100:   standing conditional coverage into a total, mechanically enforced
101:   guarantee. Status: COMPLETE (`./verify` 135/135 green; released with this
102:   commit).
103: - **T12 — Minimal-interface redesign.** Front = pure retrieval surface
104:   (hidden behavioral probes; listening as a hidden-by-default resolver:
105:   classic audio-only fields OR `#listening` tag; sentence front as the
106:   universal fallback). Back = typography hierarchy (word → pitch quiet →
107:   compacted meaning → context grid sentence+picture → secondary collapsed
108:   behind `More ▾`), discreet Context/Word/Listening state label,
109:   `F` full-card furigana + `T` translation shortcuts, tags/frequency
110:   badges removed (tags are behavioral metadata). Bug fixes: `{{Type}}`/
111:   `note:` search clause removed (wrong value), mobile `.word-meta-row`
112:   specificity, JS syntax gate added after an unbalanced-brace regression
113:   was caught by visual QA. Status: COMPLETE (`./verify` 168/168 green).
114: 
115: ## Roadmap (evolution loop input, not committed scope)
116: 
117: - R1: extra compactor fixtures if Yomitan markup drifts.
118: - R2: further density tuning only with layout-probe proof.
119: - R3: new ADRs only for decisions with alternatives + consequences.
120: 
121: ## State updates
122: 
123: Mark a task COMPLETE only after targeted checks + `./verify` + (for
124: template/CSS changes) the `finish.sh` release run. Update technical docs
125: only when something actually changed — no churn.

(End of file - total 125 lines)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: read
**Status:** completed
**Title:** MVP.md

**Input:**
```json
{
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/MVP.md"
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/MVP.md</path>
<type>file</type>
<content>
1: # MVP.md — current scope
2: 
3: `PRODUCT.md` answers *what is this product?* This file answers *what are we
4: actually building right now?* Agents must not independently widen this scope
5: while coding.
6: 
7: ## MVP goal
8: 
9: A shippable, review-ready Japanese sentence-mining note type: dense on
10: desktop, usable on a small phone, with sentence/word/listening fronts, a
11: compact informative back, and a one-command sync → export → release loop.
12: 
13: ## Core user journey(s)
14: 
15: 1. Import the release `.apkg` → review mined cards daily on desktop and phone.
16: 2. Mature cards automatically test the word, not the memorized sentence.
17: 3. Edit templates/CSS locally → `./finish.sh` → cards updated in Anki and a
18:    new tagged release published.
19: 
20: ## Included capabilities
21: 
22: - Front: pure retrieval surface — sentence / Expression fallback,
23:   Frequency-legacy sentence path, cloze-trio rebuild, listening as a
24:   hidden-by-default resolver (classic audio-only fields **or**
25:   `#listening` tag; sentence front is the universal fallback), Mature
26:   Word Mode (interval-gated, platform-exclusive retrieval, sentence
27:   fallback).
28: - Back: typography-driven hierarchy — word+furigana target, quiet pitch
29:   text, Definition Compactor (CSS §6b), 3-line truncator with one-way
30:   expand (§6c), context (sentence + picture as core information,
31:   responsive grid), native circular audio, discreet retrieval-state
32:   label (Context/Word/Listening, hover-explained), secondary
33:   information collapsed behind `More ▾` (translation, context, kanji
34:   notes, notes, full extended definition), source footer.
35: - Styling: Tokyo Night + Aki Paper themes, fluid clamps, container-query
36:   context grid with media fallback, zero-reflow furigana + `F`
37:   full-card furigana mode (back only), Fuji backdrop, reduced-motion
38:   support.
39: - Empty-field collapse everywhere: no padding, border, or margin survives an
40:   empty field; the More section and its toggle self-remove when empty.
41: - Tooling: field bootstrap (`fetch_anki_fields.py`), snapshotted sync
42:   (`sync_to_anki.py`), apkg export (`release_apkg.py`), `verify` gate,
43:   `finish.sh` release loop, regression tests (compactor + templates +
44:   front-modes + layout).
45: 
46: ## Excluded capabilities
47: 
48: - New fields, add-ons, or review-time Python.
49: - Additional card types or note types.
50: - Cloud sync / collaboration / analytics.
51: - Mandatory per-project doc/diagram checklists beyond `ARCHITECTURE.md`.
52: 
53: ## Acceptance criteria
54: 
55: - `./verify` passes (compactor + template invariants; layout checks when
56:   Chrome is present).
57: - A real user can complete: import → review sentence card → review mature
58:   word card → review listening card → expand definition/translation/image →
59:   edit locally → `./finish.sh` → updated cards + tagged release.
60: - No horizontal overflow, no viewport-fill dead space, furigana never shifts
61:   layout, audio never overlaps, failures always degrade to the sentence front.
62: 
63: ## Known limitations
64: 
65: - Mature interval needs AnkiConnect (desktop) or the AnkiDroid reviewer
66:   bridge; Browse/template previews without a bridge correctly fall back to
67:   the sentence front.
68: - AnkiDroid fragment-reviewer stub bridges (`signal:jsapi`) are detected and
69:   never invoked.
70: - Headless layout checks skip gracefully when Chrome is absent.
71: 
72: ## Deferred features
73: 
74: - Further density passes beyond the current clamp/container-query system.
75: - Additional AnkiDroid bridge capabilities (beyond interval read).
76: - Extra dictionaries/markup variants beyond current compactor fixtures.
77: - Any `docs/adr/` entries beyond decided items (added only when a decision
78:   has alternatives + consequences + long-term relevance).

(End of file - total 78 lines)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: read
**Status:** completed
**Title:** Design.md

**Input:**
```json
{
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/Design.md"
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/Design.md</path>
<type>file</type>
<content>
1: - The design should be modern, simple, elegant, refined
2: - the whole screen should be utlised(ie very ergonomical design)
3: - the card should work on PC(arch linux) but also on a smaller screen(samsung galaxy A50), text size and even visual elements should change with screen size
4: - furigana should be dispalyed only in back card, on mouse hover using the furigana fields(like {{furigana}} with the help of `furigana:`, for ex, {{furigana:furigana}} to display the word with furigana hover)
5: - on click on the image, it should expand, another click outside it should bring it back to normal
6: - anti-overlearning: once a card is mature (interval >= 365 days, see `LONG_INTERVAL_DAYS` in the front template), the front shows only the word instead of the sentence — the familiar sentence must never become the retrieval cue; the interval is read live from the card (no addons, no new fields), and any retrieval failure falls back to the normal sentence front
7: - mature word mode no longer triggers on listening cards (prevents answer leak)
8: - frequency tooltips corrected (ranks, not per M)
9: - translation box no longer collapses when clicking inside revealed text
10: - empty side column now uses 1-column layout on cards without side content
11: - audio feedback includes visual pulse when using native Anki replay buttons
12: - front card blank-rendering risks mitigated with safety timeout and finally block
13: - backdrop fixed positioning corrected
14: - furigana tap interaction improved (double-tap or click)

(End of file - total 14 lines)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: bash
**Status:** completed
**Title:** fd . "New Folder"

**Input:**
```json
{
  "command": "fd . \"New Folder\""
}
```

**Output:**
```
(no output)
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: bash
**Status:** completed
**Title:** rtk git status

**Input:**
```json
{
  "command": "rtk git status"
}
```

**Output:**
```
* main...origin/main
?? conversations/20260912-01-55-22-Anki-Japanese-card-template-vi.md

```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: read
**Status:** completed
**Title:** Card 1 - Front.template.anki

**Input:**
```json
{
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/Card 1 - Front.template.anki"
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/Card 1 - Front.template.anki</path>
<type>file</type>
<content>
1: <!-- FRONT CARD TEMPLATE
2:      Premium Ergonomic Japanese Front Card
3:      
4:        Behavior:
5:        - Standard: Shows Sentence (or Expression) if Definition / Extended definition exists.
6:        - Listening: Shows circular interactive audio player if definitions are missing AND Frequency is empty.
7:        - Cloze Fallback: Sentence without a bold term (jidoushio mobile
8:          exports) is rebuilt in JS from cloze-prefix + <b>cloze-body</b>
9:          + cloze-suffix when all three are non-empty; otherwise the
10:          usual sentence is kept untouched.
11:        - Frequency legacy: No definitions but Frequency present (old cards with deleted glosses) → usual sentence, never the audio button.
12:        - Fallback: Shows Sentence / Expression if both definitions and audio are missing.
13:       - Mature Word Mode: If the card interval >= LONG_INTERVAL_DAYS (script constant),
14:         the front shows only the Expression instead of the sentence (anti-overlearning).
15:          Interval is read at review time: AnkiDroid JS API (ankiGetCardInterval) on mobile,
16:          AnkiConnect on desktop — guiCurrentCard during active review, with a content
17:          search fallback (Expression field) for the Browse previewer where no review
18:          is active. Mobile preview screens have no JS bridge (only the reviewer
19:          injects js-api.js), so they always fall back to the sentence front.
20:          Any failure falls back to the normal sentence front.
21:        - Front sentence sizing: pure CSS (base clamp + smaller phone
22:          override in the stylesheet's mobile block). No JS involved.
23: 
24:        Minimalism (PRODUCT.md): the front shows NO other UI — no tags,
25:        no badges, no metadata, no labels. Hidden probes carry only
26:        behavioral signals (#listening tag, field presence) for the JS
27:        front-mode resolver; they never render visibly.
28: -->
29: 
30: <div class="card-wrapper">
31:   <div class="card-container" style="visibility: hidden;">
32:     <!-- Mature-Card Word Mode probe: shown instead of sentence when interval >= threshold -->
33:     <div class="front-word-display">{{edit:Expression}}</div>
34: 
35:     <!-- Cloze-fallback probe (jidoushio mobile exports): hidden source
36:          parts for JS sentence reconstruction when Sentence has no bold
37:          term. Plain filters — never displayed, never edited. -->
38:     <div class="cloze-probe" hidden>
39:       <span class="cloze-pre">{{cloze-prefix}}</span>
40:       <span class="cloze-mid">{{cloze-body}}</span>
41:       <span class="cloze-suf">{{cloze-suffix}}</span>
42:     </div>
43: 
44:     <!-- Behavioral tag probe: #listening marks a deliberate listening
45:          exercise and forces the audio-button front. Tags are behavioral
46:          metadata, never rendered as decoration. -->
47:     {{#Tags}}
48:       <div class="tags-probe" hidden>{{Tags}}</div>
49:     {{/Tags}}
50: 
51:     <!-- Field-presence probes for the listening resolver (hidden) -->
52:     {{#Definition}}<span class="probe-def" hidden></span>{{/Definition}}
53:     {{#Extended definition}}<span class="probe-ext" hidden></span>{{/Extended definition}}
54:     {{#Frequency}}<span class="probe-freq" hidden></span>{{/Frequency}}
55: 
56:     <!-- Standard Study View -->
57:     {{#Definition}}
58:       <div class="sentence-display">
59:         {{#Sentence}}
60:           {{edit:Sentence}}
61:         {{/Sentence}}
62:         {{^Sentence}}
63:           {{edit:Expression}}
64:         {{/Sentence}}
65:       </div>
66:     {{/Definition}}
67: 
68:     <!-- Fallback Standard View (When only Extended definition is present) -->
69:     {{^Definition}}
70:       {{#Extended definition}}
71:         <div class="sentence-display">
72:           {{#Sentence}}
73:             {{edit:Sentence}}
74:           {{/Sentence}}
75:           {{^Sentence}}
76:             {{edit:Expression}}
77:           {{/Sentence}}
78:         </div>
79:       {{/Extended definition}}
80:     {{/Definition}}
81: 
82:     <!-- Listening Mode / Pathological Fallback -->
83:     {{^Definition}}
84:       {{^Extended definition}}
85: 
86:         <!-- Frequency present but definitions missing (legacy cards with
87:              deleted English glosses): NOT a listening card — show the
88:              usual sentence instead of the audio button. -->
89:         {{#Frequency}}
90:             <div class="sentence-display">
91:               {{#Sentence}}
92:                 {{edit:Sentence}}
93:               {{/Sentence}}
94:               {{^Sentence}}
95:                 {{edit:Expression}}
96:               {{/Sentence}}
97:             </div>
98:         {{/Frequency}}
99: 
100:         {{^Frequency}}
101:         <!-- Classic listening fields (Sentence Audio present, nothing
102:              else): the sentence still renders as the safe fallback; the
103:              JS resolver below swaps it for the audio button. No JS /
104:              resolver failure => sentence front. -->
105:         {{#Sentence Audio}}
106:           <div class="sentence-display">
107:             {{#Sentence}}
108:               {{edit:Sentence}}
109:             {{/Sentence}}
110:             {{^Sentence}}
111:               {{edit:Expression}}
112:             {{/Sentence}}
113:           </div>
114:         {{/Sentence Audio}}
115: 
116:         <!-- Bulletproof Fallback: No Sentence audio -->
117:         {{^Sentence Audio}}
118:             <div class="sentence-display">
119:               {{#Sentence}}
120:                 {{edit:Sentence}}
121:               {{/Sentence}}
122:               {{^Sentence}}
123:                 {{edit:Expression}}
124:               {{/Sentence}}
125:             </div>
126:         {{/Sentence Audio}}
127:         {{/Frequency}}
128:       {{/Extended definition}}
129:     {{/Definition}}
130: 
131:     <!-- Listening view: renders hidden whenever Sentence Audio exists
132:          (any card shape, including #listening-tagged cards with
133:          glosses). The JS resolver activates it only when the listening
134:          condition holds; on every other card it stays inert. -->
135:     {{#Sentence Audio}}
136:       <div class="listening-view">
137:         <div class="audio-btn-wrapper">
138:           <button type="button" class="circular-audio-btn large-audio-btn" title="Play Sentence Audio" aria-label="Play sentence audio" onclick="playCircularAudio(this)">
139:             <svg class="audio-progress-ring" viewBox="0 0 80 80">
140:               <circle class="ring-bg" cx="40" cy="40" r="36" />
141:               <circle class="ring-fill" cx="40" cy="40" r="36" stroke-dasharray="226.19" stroke-dashoffset="226.19" />
142:             </svg>
143:             <span class="audio-btn-content">
144:               <span class="audio-btn-label">文</span>
145:             </span>
146:           </button>
147:           <span class="raw-audio-source" aria-hidden="true">{{Sentence Audio}}</span>
148:         </div>
149:       </div>
150:     {{/Sentence Audio}}
151: 
152:   </div>
153: </div>
154: 
155: <script>
156:   (async function() {
157:     /* --- 1. HOISTED UTILITIES & FUNCTIONS --- */
158: 
159:     /* --- CIRCULAR AUDIO CONTROLLER (native-only) ---
160:        Always delegates to Anki's own replay link (desktop `replay-button`,
161:        AnkiDroid `replaybutton`). Never constructs an HTML5 audio element:
162:        on AnkiDroid the rendered link carries no usable filename (old builds
163:        emit `playsound:q:0`, which would be loaded as a bogus file and fail).
164:        The ring is a decorative play-pulse, not true progress. */
165:     window.currentActiveBtn = window.currentActiveBtn || null;
166:     window.currentActiveTimer = window.currentActiveTimer || null;
167: 
168:     window.resetAudioState = function() {
169:         if (window.currentActiveTimer) {
170:             clearTimeout(window.currentActiveTimer);
171:             window.currentActiveTimer = null;
172:         }
173:         if (window.currentActiveBtn) {
174:             window.currentActiveBtn.classList.remove('is-playing');
175:             const ring = window.currentActiveBtn.querySelector('.ring-fill');
176:             if (ring) {
177:                 const circ = parseFloat(ring.getAttribute('stroke-dasharray')) || 226.19;
178:                 ring.style.transition = '';
179:                 ring.style.strokeDashoffset = circ;
180:             }
181:             window.currentActiveBtn = null;
182:         }
183:     };
184: 
185:     window.playCircularAudio = function(btn) {
186:         /* Debounce: native playback can't be stopped programmatically, so
187:            ignore rapid re-taps on the already-playing button (prevents
188:            overlapping audio on AnkiDroid). */
189:         if (window.currentActiveBtn === btn) return;
190:         window.resetAudioState();
191:         const ringFill = btn.querySelector('.ring-fill');
192: 
193:         /* The replay link lives in the sibling .raw-audio-source (kept OUT
194:            of the <button>: <a> inside <button> is invalid HTML and Android
195:            WebView mishandles taps on it). */
196:         const scope = (btn.closest && btn.closest('.audio-btn-wrapper')) || document;
197:         const nativeReplay = scope.querySelector('.replaybutton, .replay-button, a.sound, .soundLink')
198:           || btn.querySelector('.replaybutton, .replay-button, a.sound, .soundLink');
199:         if (nativeReplay) {
200:             try { nativeReplay.click(); } catch (e) { return; }
201:             btn.classList.add('is-playing');
202:             if (ringFill) {
203:                 ringFill.style.transition = 'stroke-dashoffset 0.8s ease-in-out';
204:                 ringFill.style.strokeDashoffset = '0';
205:             }
206:             window.currentActiveBtn = btn;
207:             window.currentActiveTimer = setTimeout(() => {
208:                 if (window.currentActiveBtn === btn) {
209:                     window.resetAudioState();
210:                 }
211:             }, 800);
212:         }
213:     };
214: 
215:     /* --- 2. MAIN EXECUTION BLOCK --- */
216:     const container = document.querySelector('.card-container');
217:     const wrapper = document.querySelector('.card-wrapper');
218: 
219:     if (container && wrapper) {
220:       /* Front-state store: cleared at script start (before any async
221:          work) so a card whose front script crashes mid-way can never
222:          inherit the previous card's state; the back label then stays
223:          hidden (state unknown) instead of showing stale data. */
224:       try { window.__ajtFrontState = undefined; } catch (_) {}
225: 
226:       let wordMode = false;
227:       let interval = null;
228:       let source = 'unavailable';
229:       /* Latency probe: t0 at script start; elapsed retrieval time is
230:          logged with the decision, so AnkiConnect (desktop) vs bridge
231:          (mobile) costs can be compared per card. */
232:       const nowMs = () => (
233:         (typeof performance !== 'undefined' && performance.now)
234:           ? performance.now()
235:           : Date.now()
236:       );
237:       const t0 = nowMs();
238: 
239:       /* Safety Reveal: Ensure card shows even if async calls hang.
240:          The cap sits well above the slowest happy path (low hundreds
241:          of ms) and only binds failure paths. */
242:       const reveal = () => {
243:         container.style.visibility = 'visible';
244:       };
245:       const safetyTimeout = setTimeout(reveal, 1200);
246: 
247:       /* --- CLOZE FALLBACK (BEGIN — headless check extracts this block verbatim) ---
248:          jidoujisho mobile exports often carry a Sentence with no <b>
249:          target term. When the rendered sentence has no bold element but
250:          the cloze trio (prefix/body/suffix) is complete, rebuild it as
251:          prefix + <b>body</b> + suffix so the front is indistinguishable
252:          from a proper Yomitan sentence (same .sentence-display b styling).
253:          Any gap or failure keeps the original sentence untouched. */
254:       try {
255:         const probe = container.querySelector('.cloze-probe');
256:         const probeText = (sel) => {
257:           const el = probe && probe.querySelector(sel);
258:           return el ? (el.textContent || '').replace(/\s+/g, ' ').trim() : '';
259:         };
260:         const clozePre = probeText('.cloze-pre');
261:         const clozeMid = probeText('.cloze-mid');
262:         const clozeSuf = probeText('.cloze-suf');
263:         if (clozePre && clozeMid && clozeSuf) {
264:           container.querySelectorAll('.sentence-display').forEach((sd) => {
265:             if (!sd.querySelector('b, strong')) {
266:               sd.textContent = '';
267:               const bold = document.createElement('b');
268:               bold.textContent = clozeMid;
269:               sd.append(
270:                 document.createTextNode(clozePre),
271:                 bold,
272:                 document.createTextNode(clozeSuf)
273:               );
274:             }
275:           });
276:         }
277:       } catch (clozeErr) {
278:         console.warn('[Cloze Fallback]', clozeErr);
279:       }
280:       /* --- CLOZE FALLBACK (END) --- */
281: 
282:       /* Empty-field collapse (QUALITY.md): after the cloze rebuild, a
283:          sentence block with no text at all (neither Sentence nor
284:          Expression) leaves no padded void. Runs before the reveal. */
285:       try {
286:         container.querySelectorAll('.sentence-display').forEach((sd) => {
287:           if (!sd.textContent || !sd.textContent.trim()) sd.remove();
288:         });
289:       } catch (blankErr) {
290:         console.warn('[Blank Collapse]', blankErr);
291:       }
292: 
293:       /* --- LISTENING RESOLVER (classic field condition + #listening tag) ---
294:          The listening markup renders hidden whenever Sentence Audio
295:          exists. It becomes the active front when the classic field
296:          condition holds (no Definition / Extended definition /
297:          Frequency — the original audio-only path) OR the card carries
298:          the #listening tag (deliberate listening exercise, even with
299:          glosses). Runs synchronously before the reveal, so there is
300:          no flash; any failure leaves the sentence front in place. */
301:       let isListening = false;
302:       try {
303:         const listeningView = container.querySelector('.listening-view');
304:         if (listeningView) {
305:           const tagsProbe = container.querySelector('.tags-probe');
306:           const tagText = tagsProbe ? (tagsProbe.textContent || '') : '';
307:           const hasListeningTag = /(^|\s)listening(\s|$)/.test(tagText);
308:           const fieldListening =
309:             !container.querySelector('.probe-def') &&
310:             !container.querySelector('.probe-ext') &&
311:             !container.querySelector('.probe-freq');
312:           isListening = fieldListening || hasListeningTag;
313:           if (isListening) {
314:             wrapper.classList.add('listening-mode');
315:             container.querySelectorAll('.sentence-display').forEach((sd) => sd.remove());
316:           }
317:         }
318:       } catch (listenErr) {
319:         console.warn('[Listening Resolver]', listenErr);
320:       }
321: 
322:       /* Anki-Connect helper with timeout. 500ms is ~15x the measured
323:          healthy localhost latency (~25ms/call), so it only ever binds
324:          a wedged/busy Anki — and the fallback is always the safe
325:          sentence front, never a hang. */
326:       const post = (action, params) => {
327:         const timeout = new Promise((_, rej) => 
328:           setTimeout(() => rej(new Error('AnkiConnect timeout')), 500)
329:         );
330:         const fetchPromise = fetch('http://127.0.0.1:8765', {
331:           method: 'POST',
332:           body: JSON.stringify({ action: action, version: 6, params: params })
333:         }).then(r => r.json()).then(data => {
334:           if (data.error) throw new Error(data.error);
335:           return data.result;
336:         });
337:         return Promise.race([fetchPromise, timeout]);
338:       };
339: 
340:       const escQuery = (s) => s.replace(/\\/g, '\\\\').replace(/"/g, '\\"').replace(/([*_])/g, '\\$1');
341:       const normText = (s) => s
342:         .replace(/<br\s*\/?>/gi, ' ')
343:         .replace(/<[^>]+>/g, ' ')
344:         .replace(/&nbsp;/gi, ' ')
345:         .replace(/\s+/g, ' ')
346:         .trim();
347: 
348:       try {
349:         /* isListening (resolved above): listening cards never use word
350:            mode — skip ALL retrieval up front (also avoids needless
351:            AnkiDroid JS-API calls, which can trigger AnkiDroid's known
352:            false-positive "Failed to load *.bin" toast). */
353:         /* Mobile WebViews (AnkiDroid / AnkiMobile) have no AnkiConnect: a
354:            fetch to 127.0.0.1 is refused and Android surfaces it natively as
355:            "Failed to load 'downloadfile.bin'". Never fetch from a phone. */
356:         const ua = (typeof navigator !== 'undefined' && navigator.userAgent) || '';
357:         const isMobile = /Android|iPhone|iPad|iPod/i.test(ua);
358:         /* AnkiDroid compatibility helpers */
359:         const bridgeAvailable = () =>
360:           typeof AnkiDroidJS !== 'undefined' &&
361:           AnkiDroidJS !== null;
362: 
363:         const withBridgeTimeout = (promise, ms) =>
364:           new Promise((resolve, reject) => {
365:             const timer = setTimeout(
366:               () => reject(new Error('AnkiDroid bridge timeout')),
367:               ms
368:             );
369: 
370:             Promise.resolve(promise).then(
371:               value => {
372:                 clearTimeout(timer);
373:                 resolve(value);
374:               },
375:               error => {
376:                 clearTimeout(timer);
377:                 reject(error);
378:               }
379:             );
380:           });
381: 
382:         /*
383:          * Accept:
384:          *   365
385:          *   "365"
386:          *   {success: true, value: 365}
387:          *   {success: true, value: "365"}
388:          *   JSON-encoded versions of these responses
389:          *
390:          * Never turn null, false, or an empty string into an interval.
391:          */
392:         const parseDroidInterval = raw => {
393:           let value = raw;
394: 
395:           for (let depth = 0; depth < 6; depth++) {
396:             if (typeof value === 'number') {
397:               if (!Number.isFinite(value) || value < 0) {
398:                 throw new Error('No usable card interval');
399:               }
400:               return value;
401:             }
402: 
403:             if (typeof value === 'string') {
404:               const text = value.trim();
405: 
406:               if (!text) {
407:                 throw new Error('Empty interval response');
408:               }
409: 
410:               // Ordinary numeric string.
411:               const number = Number(text);
412:               if (Number.isFinite(number)) {
413:                 value = number;
414:                 continue;
415:               }
416: 
417:               // JSON-encoded response.
418:               try {
419:                 value = JSON.parse(text);
420:               } catch (_) {
421:                 throw new Error(
422:                   'Unrecognized interval response: ' + text.slice(0, 120)
423:                 );
424:               }
425:               continue;
426:             }
427: 
428:             if (value && typeof value === 'object') {
429:               if (
430:                 value.success === false ||
431:                 value.success === 'false'
432:               ) {
433:                 throw new Error('AnkiDroid reported success=false');
434:               }
435: 
436:               if (
437:                 Object.prototype.hasOwnProperty.call(value, 'value')
438:               ) {
439:                 value = value.value;
440:                 continue;
441:               }
442: 
443:               if (
444:                 Object.prototype.hasOwnProperty.call(value, 'interval')
445:               ) {
446:                 value = value.interval;
447:                 continue;
448:               }
449:             }
450: 
451:             throw new Error('Unsupported interval response');
452:           }
453: 
454:           throw new Error('Unexpectedly nested interval response');
455:         };
456: 
457:         const getAnkiDroidInterval = async () => {
458:           try {
459:             const options = {
460:               developer: 'mansourvery-hub@users.noreply.github.com',
461:               version: '0.0.3'
462:             };
463: 
464:             let api;
465:             let apiKind;
466: 
467:             if (typeof AnkiDroidJS === 'function') {
468:               // Constructor-based API.
469:               api = new AnkiDroidJS(options);
470:               apiKind = 'constructor';
471:             } else {
472:               // Direct/native bridge API.
473:               api = AnkiDroidJS;
474:               apiKind = 'direct';
475: 
476:               if (typeof api.init === 'function') {
477:                 const initialized = await withBridgeTimeout(
478:                   api.init(JSON.stringify(options)),
479:                   1000
480:                 );
481: 
482:                 if (
483:                   initialized === false ||
484:                   initialized === 'false'
485:                 ) {
486:                   throw new Error('AnkiDroid API initialization failed');
487:                 }
488:               }
489:             }
490: 
491:             if (
492:               !api ||
493:               typeof api.ankiGetCardInterval !== 'function'
494:             ) {
495:               throw new Error('ankiGetCardInterval is unavailable');
496:             }
497: 
498:             /* New-reviewer stub guard: AnkiDroid's fragment-based reviewer
499:                injects a placeholder AnkiDroidJS whose methods only navigate
500:                to 'signal:jsapi' (no data). Never invoke it — the navigation
501:                is unhandled and yields nothing. Detect by method source. */
502:             let methodSrc = '';
503:             try {
504:               methodSrc = Function.prototype.toString.call(api.ankiGetCardInterval);
505:             } catch (_) { /* fall through to the call */ }
506:             if (/signal\s*:\s*jsapi/.test(methodSrc)) {
507:               return {
508:                 interval: null,
509:                 source: 'ankiDroid-stub (reviewer without interval API)'
510:               };
511:             }
512: 
513:             const raw = await withBridgeTimeout(
514:               api.ankiGetCardInterval(),
515:               1000
516:             );
517: 
518:             return {
519:               interval: parseDroidInterval(raw),
520:               source: 'ankiDroid-' + apiKind
521:             };
522:           } catch (error) {
523:             return {
524:               interval: null,
525:               source: 'ankiDroid-error: ' +
526:                 (error && error.message ? error.message : String(error))
527:             };
528:           }
529:         };
530:         /* Platform-exclusive retrieval. Phones use ONLY the AnkiDroid
531:            bridge (AnkiConnect is unreachable from a mobile WebView — the
532:            refused fetch surfaces natively as "Failed to load
533:            downloadfile.bin"). Desktops use ONLY AnkiConnect (no
534:            AnkiDroidJS global exists there). Neither platform ever
535:            attempts the other's method. */
536:         if (!isListening && isMobile) {
537:           if (bridgeAvailable()) {
538:             const r = await getAnkiDroidInterval();
539:             interval = r.interval;
540:             source = r.source;
541:           } else {
542:             /* Phone without an (already injected) bridge: AnkiDroid injects
543:                its API around card load, often AFTER card scripts run — so poll
544:                for it while the card is still hidden (no flash risk), then give
545:                up to the sentence front. 700ms cap: the legacy reviewer
546:                injects js-api.js synchronously in <head>, so a longer wait
547:                only delays preview screens, where the sentence fallback is
548:                correct anyway. */
549:             const waitForBridge = async (deadlineMs, stepMs) => {
550:               const start = Date.now();
551:               while (!bridgeAvailable()) {
552:                 if (Date.now() - start >= deadlineMs) return false;
553:                 await new Promise(r => setTimeout(r, stepMs));
554:               }
555:               return true;
556:             };
557:             if (await waitForBridge(700, 100)) {
558:               const r = await getAnkiDroidInterval();
559:               interval = r.interval;
560:               source = r.source;
561:             } else {
562:               /* No bridge script in the page: on AnkiDroid this means a
563:                  preview screen (card browser / template / editor preview),
564:                  never a real review — the legacy reviewer always injects
565:                  js-api.js synchronously via card_template.html <head>.
566:                  Sentence fallback is correct here; review the card for
567:                  real to exercise mature mode. */
568:               source = 'no-bridge-mobile (preview? bridge exists only in reviewer)';
569:             }
570:           }
571:         } else if (!isListening) {
572:           /* DESKTOP-ONLY: AnkiConnect guiCurrentCard -> cardsInfo. The
573:              bridge is never touched here. guiCurrentCard carries no
574:              interval field (per the AnkiConnect action docs), so the
575:              cardsInfo follow-up is mandatory, not redundant. */
576:           try {
577:             const current = await post('guiCurrentCard', {});
578:             if (current && current.cardId) {
579:               const infos = await post('cardsInfo', { cards: [current.cardId] });
580:               if (infos && infos[0]) {
581:                 interval = infos[0].interval;
582:                 source = 'guiCurrentCard';
583:               }
584:             }
585:           } catch (reviewErr) {
586:             console.log('[Mature Word Mode] no active review, trying content search');
587:             const wordEl = document.querySelector('.front-word-display');
588:             const sentEl = document.querySelector('.sentence-display');
589:             if (wordEl && !isListening) {
590:               const exprDom = normText(wordEl.innerText || wordEl.textContent || '');
591:               if (exprDom) {
592:                 /* No "note:" clause: the note type name is not exposed to
593:                    templates ({{Type}} is the scheduling type, not the
594:                    model name), and the exact Expression field match below
595:                    already restricts results to this note type's cards. */
596:                 const query = '"Expression:' + escQuery(exprDom) + '"';
597:                 const ids = await post('findCards', { query: query });
598:                 if (ids && ids.length) {
599:                   const infos = await post('cardsInfo', { cards: ids });
600:                   const fieldText = (info, name) =>
601:                     normText((info.fields && info.fields[name] && info.fields[name].value) || '');
602:                   let matches = infos.filter(i => fieldText(i, 'Expression') === exprDom);
603:                   if (matches.length > 1 && sentEl) {
604:                     const sentDom = normText(sentEl.innerText || sentEl.textContent || '');
605:                     const withSent = matches.filter(i => fieldText(i, 'Sentence') === sentDom);
606:                     if (withSent.length) matches = withSent;
607:                   }
608:                   if (matches.length) {
609:                     interval = matches[0].interval;
610:                     source = 'content-search';
611:                   }
612:                 }
613:               }
614:             }
615:           }
616:         }
617:       } catch (e) {
618:         source = 'error: ' + (e && e.message ? e.message : String(e));
619:         console.warn('[Mature Word Mode]', e);
620:       } finally {
621:         clearTimeout(safetyTimeout);
622:         const elapsedMs = Math.round(nowMs() - t0);
623:         console.log('[Mature Word Mode] source=' + source +
624:           ' ivl=' + String(interval) + ' in ' + elapsedMs + 'ms');
625: 
626:         const LONG_INTERVAL_DAYS = 365;
627: 
628:         // Set to false after confirming that Android works.
629:         const DEBUG_MATURE_MODE = false;
630: 
631:         const wordEl = container.querySelector('.front-word-display');
632:         const hasExpression = !!(
633:           wordEl && (wordEl.textContent || '').trim()
634:         );
635: 
636:         wordMode =
637:           typeof interval === 'number' &&
638:           Number.isFinite(interval) &&
639:           interval >= LONG_INTERVAL_DAYS &&
640:           !isListening &&
641:           hasExpression;
642: 
643:         // Explicitly reset the class as well as enabling it.
644:         wrapper.classList.toggle('word-mode', wordMode);
645: 
646:         /* Front-state store: the back card reads this to render its
647:            discreet retrieval-condition label (Context / Word /
648:            Listening). Same WebView document in the reviewer; when the
649:            back renders without the front state (lone back preview),
650:            the label simply stays hidden. */
651:         try {
652:           window.__ajtFrontState = {
653:             mode: wordMode ? 'word' : (isListening ? 'listening' : 'context')
654:           };
655:         } catch (_) { /* preview-only environments */ }
656: 
657:         if (DEBUG_MATURE_MODE) {
658:           let diagnostic = wrapper.querySelector('.mwm-debug');
659: 
660:           if (!diagnostic) {
661:             diagnostic = document.createElement('div');
662:             diagnostic.className = 'mwm-debug';
663:             diagnostic.style.cssText =
664:               'padding:6px 10px;' +
665:               'font:12px/1.4 sans-serif;' +
666:               'color:var(--text-secondary,#888);' +
667:               'overflow-wrap:anywhere;' +
668:               'text-align:left;';
669:             wrapper.appendChild(diagnostic);
670:           }
671: 
672:           diagnostic.textContent =
673:             'Mature mode: ' + (wordMode ? 'ON' : 'OFF') +
674:             ' | interval=' + String(interval) +
675:             ' | threshold=' + LONG_INTERVAL_DAYS +
676:             ' | source=' + source +
677:             ' | ' + elapsedMs + 'ms';
678:         }
679: 
680:         reveal();
681:       }
682:     }
683:   })();
684: </script>

(End of file - total 684 lines)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: read
**Status:** completed
**Title:** Card 1 - Back.template.anki

**Input:**
```json
{
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/Card 1 - Back.template.anki"
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/Card 1 - Back.template.anki</path>
<type>file</type>
<content>
1: <!-- BACK CARD TEMPLATE
2:      Minimal Japanese Back Card — strong information hierarchy.
3: 
4:      Hierarchy (PRODUCT.md redesign):
5:        Level 1  Target word + reading (furigana hover)   — largest
6:        Level 2  Primary meaning (compacted definition)    — §6b CSS
7:        Level 3  Context (sentence + picture when present) — core info
8:        Level 4  Secondary info — collapsed behind "More ▾":
9:                 translation (click/T), extended definition,
10:                 additional context, kanji notes, notes, source.
11: 
12:       Removed vs the old layout: sticky tags bar (tags are behavioral
13:       metadata now, never decoration), frequency/pitch badges (visual
14:       noise without retrieval value), the two-column side dashboard.
15: 
16:       Preserved subsystems: Definition Compactor (§6b), truncator (§6c),
17:       native-delegating audio buttons (文/言葉 — Anki's R shortcut also
18:       remains fully functional), lightbox, empty-field collapse.
19: -->
20: 
21: <div class="card-wrapper back-card">
22:   <div class="card-container">
23: 
24:     <!-- Discreet retrieval-condition label: Context / Word / Listening.
25:          Set by the front script's window.__ajtFrontState; stays hidden
26:          when the state is unknown (lone back preview). Hover explains
27:          the two-tier maturity model. Never a large colored badge. -->
28:     <div class="retrieval-state" data-state="context" hidden>
29:       <span class="retrieval-state-label"></span>
30:     </div>
31: 
32:     <!-- LEVEL 1: TARGET + READING (one conceptual unit) -->
33:     {{#furigana}}
34:       <div class="word-display">{{edit:furigana:furigana}}</div>
35:     {{/furigana}}
36:     {{^furigana}}
37:       {{#Expression}}
38:         <div class="word-display">{{edit:furigana:Expression}}</div>
39:       {{/Expression}}
40:     {{/furigana}}
41: 
42:     <!-- Reading detail: pitch accent as quiet muted text (never a
43:          colored badge — it supplements the reading, it is not UI). -->
44:     {{#Pitch Accent}}
45:       <div class="pitch-quiet">{{edit:Pitch Accent}}</div>
46:     {{/Pitch Accent}}
47: 
48:     <!-- LEVEL 2: PRIMARY MEANING (compact: see Definition Compactor §6b) -->
49:     {{#Definition}}
50:       <div class="definition-box primary-definition" tabindex="0" role="button" aria-expanded="false" onclick="expandDefinition(this)" onkeydown="handleDefinitionKey(event, this)">
51:         {{edit:furigana:Definition}}
52:       </div>
53:     {{/Definition}}
54:     {{^Definition}}
55:       {{#Extended definition}}
56:         <div class="definition-box primary-definition" tabindex="0" role="button" aria-expanded="false" onclick="expandDefinition(this)" onkeydown="handleDefinitionKey(event, this)">
57:           {{Extended definition}}
58:         </div>
59:       {{/Extended definition}}
60:     {{/Definition}}
61: 
62:     <!-- Native-delegating replay buttons (preserved subsystem): 文/言葉
63:          click Anki's own replay link — never HTML5 audio. Kept small
64:          and quiet; Anki's R shortcut remains the primary path. -->
65:     <div class="audio-row">
66:       {{#Word Audio}}
67:         <span class="audio-btn-wrapper">
68:           <button type="button" class="circular-audio-btn small-audio-btn" title="Play Word Audio" aria-label="Play word audio" onclick="playCircularAudio(this)">
69:             <svg class="audio-progress-ring" viewBox="0 0 44 44">
70:               <circle class="ring-bg" cx="22" cy="22" r="19" />
71:               <circle class="ring-fill" cx="22" cy="22" r="19" stroke-dasharray="119.38" stroke-dashoffset="119.38" />
72:             </svg>
73:             <span class="audio-btn-content">
74:               <span class="audio-btn-label">言葉</span>
75:             </span>
76:           </button>
77:           <span class="raw-audio-source" aria-hidden="true">{{Word Audio}}</span>
78:         </span>
79:       {{/Word Audio}}
80: 
81:       {{#Sentence Audio}}
82:         <span class="audio-btn-wrapper">
83:           <button type="button" class="circular-audio-btn small-audio-btn" title="Play Sentence Audio" aria-label="Play sentence audio" onclick="playCircularAudio(this)">
84:             <svg class="audio-progress-ring" viewBox="0 0 44 44">
85:               <circle class="ring-bg" cx="22" cy="22" r="19" />
86:               <circle class="ring-fill" cx="22" cy="22" r="19" stroke-dasharray="119.38" stroke-dashoffset="119.38" />
87:             </svg>
88:             <span class="audio-btn-content">
89:               <span class="audio-btn-label">文</span>
90:             </span>
91:           </button>
92:           <span class="raw-audio-source" aria-hidden="true">{{Sentence Audio}}</span>
93:         </span>
94:       {{/Sentence Audio}}
95:     </div>
96: 
97:     <!-- LEVEL 3: CONTEXT (sentence + picture; core information) -->
98:     <div class="context-grid">
99:       <div class="context-main">
100:         {{#Sentence}}
101:           <div class="sentence-japanese">
102:             {{#Sentence (furigana)}}
103:               {{edit:furigana:Sentence (furigana)}}
104:             {{/Sentence (furigana)}}
105:             {{^Sentence (furigana)}}
106:               {{edit:Sentence}}
107:             {{/Sentence (furigana)}}
108:           </div>
109:         {{/Sentence}}
110: 
111:         <!-- Orphan context (When Sentence is empty) -->
112:         {{^Sentence}}
113:           {{#context}}
114:             <div class="html-content context-only">{{edit:context}}</div>
115:           {{/context}}
116:         {{/Sentence}}
117:       </div>
118: 
119:       {{#Picture}}
120:         <div class="context-picture">
121:           <div class="picture-container" onclick="openLightbox(this)" role="button" tabindex="0" aria-label="Expand image" onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault(); this.click()}">
122:             {{Picture}}
123:           </div>
124:         </div>
125:       {{/Picture}}
126:     </div>
127: 
128:     <!-- LEVEL 4: SECONDARY INFORMATION — collapsed behind "More ▾" -->
129:     <div class="more-section" hidden>
130:       {{#Sentence}}
131:         {{#Translation}}
132:           <div class="translation-box"
133:                role="button"
134:                tabindex="0"
135:                aria-expanded="false"
136:                 onclick="if(event.target.closest('.translation-text')) return; this.classList.toggle('revealed'); this.setAttribute('aria-expanded', this.classList.contains('revealed'))"
137:                 onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();this.click()}">
138:             <div class="translation-hint">Translation</div>
139:             <div class="translation-text">{{edit:Translation}}</div>
140:           </div>
141:         {{/Translation}}
142:         {{#context}}
143:           <div class="html-content secondary-block">{{edit:context}}</div>
144:         {{/context}}
145:       {{/Sentence}}
146: 
147:       <!-- Orphan Translation (When Sentence is empty) -->
148:       {{^Sentence}}
149:         {{#Translation}}
150:           <div class="translation-text revealed-static">{{edit:Translation}}</div>
151:         {{/Translation}}
152:       {{/Sentence}}
153: 
154:       {{#Kanji Notes}}
155:         <div class="html-content secondary-block">{{edit:Kanji Notes}}</div>
156:       {{/Kanji Notes}}
157: 
158:       {{#Notes}}
159:         <div class="html-content secondary-block">{{edit:furigana:Notes}}</div>
160:       {{/Notes}}
161: 
162:       <!-- Full Yomitan definition (only when the compact one exists too) -->
163:       {{#Definition}}
164:         {{#Extended definition}}
165:           <div class="html-content secondary-block extended-full">{{Extended definition}}</div>
166:         {{/Extended definition}}
167:       {{/Definition}}
168:     </div>
169: 
170:     <!-- The quiet "More ▾" toggle: rendered only when secondary content
171:          exists (JS removes it otherwise, so no dead chrome). -->
172:     <button type="button" class="more-toggle" aria-expanded="false" onclick="toggleMore(this)">
173:       More <span class="more-caret">▾</span>
174:     </button>
175: 
176:     <!-- Source footer (secondary; stays outside More as a one-line
177:          quiet caption — it identifies the material, not a UI panel) -->
178:     {{#Source}}
179:       <div class="source-footer">{{edit:Source}}</div>
180:     {{/Source}}
181: 
182:   </div> <!-- End card-container -->
183: </div>
184: 
185: <!-- Lightbox, Audio & Secondary-Section Scripts -->
186: <script>
187:   (function() {
188:     /* NOTE: sentence font sizing is pure CSS.
189:        The stylesheet's .sentence-japanese clamp() is the single source of
190:        truth. A previous JS length-tier scaler overrode it with an inline
191:        font-size, which silently defeated any manual CSS edits. */
192: 
193:     /* --- RETRIEVAL-STATE LABEL (discreet Context / Word / Listening) ---
194:        Reads the front script's decision. Unknown state (lone back
195:        preview, no JS) => label stays hidden — no clutter. */
196:     try {
197:       var stateEl = document.querySelector('.retrieval-state');
198:       var state = window.__ajtFrontState && window.__ajtFrontState.mode;
199:       if (stateEl && (state === 'context' || state === 'word' || state === 'listening')) {
200:         stateEl.hidden = false;
201:         stateEl.dataset.state = state;
202:         var labelEl = stateEl.querySelector('.retrieval-state-label');
203:         var labels = {
204:           context: 'Context',
205:           word: 'Word',
206:           listening: 'Listening'
207:         };
208:         var titles = {
209:           context: 'This card currently uses the sentence as a retrieval cue. After long-term consolidation, the sentence is removed so the word must be recognized independently.',
210:           word: 'This mature card intentionally removes its original context. Retrieve the reading and meaning from the word itself.',
211:           listening: 'This card tests listening recognition: play the audio and retrieve the reading and meaning.'
212:         };
213:         if (labelEl) labelEl.textContent = labels[state];
214:         stateEl.setAttribute('title', titles[state]);
215:         stateEl.setAttribute('aria-label', 'Retrieval condition: ' + labels[state]);
216:       }
217:     } catch (e) { /* label stays hidden */ }
218: 
219:     /* --- SECONDARY SECTION ("More ▾") ---
220:        Hidden by default; one-way reveal (a second click never
221:        re-collapses — same philosophy as the definition truncator).
222:        toggleMore also runs the state cleanup: if no secondary content
223:        exists, remove the button so no dead chrome survives. */
224:     window.toggleMore = function(btn) {
225:       var section = document.querySelector('.more-section');
226:       if (!section || btn.getAttribute('aria-expanded') === 'true') return;
227:       section.hidden = false;
228:       btn.setAttribute('aria-expanded', 'true');
229:       btn.classList.add('is-open');
230:       var caret = btn.querySelector('.more-caret');
231:       if (caret) caret.textContent = '▾';
232:     };
233: 
234:     /* --- LIGHTBOX CONTROLLER (click to expand / click outside to close) --- */
235:     window.openLightbox = function(target) {
236:       const img = target.querySelector('img') || (target.tagName === 'IMG' ? target : null);
237:       if (!img) return;
238:       if (document.querySelector('.lightbox-overlay')) return;
239: 
240:       const overlay = document.createElement('div');
241:       overlay.className = 'lightbox-overlay';
242:       overlay.setAttribute('role', 'dialog');
243:       overlay.setAttribute('aria-modal', 'true');
244: 
245:       const clone = document.createElement('img');
246:       clone.src = img.src;
247:       clone.className = 'expanded-img';
248:       if (img.alt) clone.alt = img.alt;
249: 
250:       overlay.appendChild(clone);
251:       document.body.appendChild(overlay);
252: 
253:       const closeOverlay = () => {
254:         if (overlay.parentNode) overlay.parentNode.removeChild(overlay);
255:         document.removeEventListener('keydown', handleKey);
256:         if (img.focus) img.focus();
257:       };
258: 
259:       const handleKey = (e) => {
260:         if (e.key === 'Escape') closeOverlay();
261:       };
262: 
263:       /* Only a click on the backdrop itself (outside the image) closes —
264:          clicks on the enlarged image stop here and never bubble up. */
265:       overlay.onclick = (e) => {
266:         if (e.target === overlay) closeOverlay();
267:       };
268:       document.addEventListener('keydown', handleKey);
269:     };
270: 
271:     /* --- CIRCULAR AUDIO CONTROLLER (native-only) ---
272:        Always delegates to Anki's own replay link (desktop `replay-button`,
273:        AnkiDroid `replaybutton`). Never constructs an HTML5 audio element:
274:        on AnkiDroid the rendered link carries no usable filename. The ring
275:        is a decorative play-pulse, not true progress. Retained for the
276:        front listening view and any future audio surfaces; the back card
277:        itself relies on Anki's native replay (R). */
278:     window.currentActiveBtn = window.currentActiveBtn || null;
279:     window.currentActiveTimer = window.currentActiveTimer || null;
280: 
281:     window.resetAudioState = function() {
282:         if (window.currentActiveTimer) {
283:             clearTimeout(window.currentActiveTimer);
284:             window.currentActiveTimer = null;
285:         }
286:         if (window.currentActiveBtn) {
287:             window.currentActiveBtn.classList.remove('is-playing');
288:             const ring = window.currentActiveBtn.querySelector('.ring-fill');
289:             if (ring) {
290:                 const circ = parseFloat(ring.getAttribute('stroke-dasharray')) || 119.38;
291:                 ring.style.transition = '';
292:                 ring.style.strokeDashoffset = circ;
293:             }
294:             window.currentActiveBtn = null;
295:         }
296:     };
297: 
298:     window.playCircularAudio = function(btn) {
299:         /* Debounce: native playback can't be stopped programmatically, so
300:            ignore rapid re-taps on the already-playing button (prevents
301:            overlapping audio on AnkiDroid). */
302:         if (window.currentActiveBtn === btn) return;
303:         window.resetAudioState();
304:         const ringFill = btn.querySelector('.ring-fill');
305: 
306:         /* The replay link lives in the sibling .raw-audio-source (kept OUT
307:            of the <button>: <a> inside <button> is invalid HTML that Android
308:            WebView mishandles). */
309:         const scope = (btn.closest && btn.closest('.audio-btn-wrapper')) || document;
310:         const nativeReplay = scope.querySelector('.replaybutton, .replay-button, a.sound, .soundLink')
311:           || btn.querySelector('.replaybutton, .replay-button, a.sound, .soundLink');
312:         if (nativeReplay) {
313:             try { nativeReplay.click(); } catch (e) { return; }
314:             btn.classList.add('is-playing');
315:             if (ringFill) {
316:                 ringFill.style.transition = 'stroke-dashoffset 0.8s ease-in-out';
317:                 ringFill.style.strokeDashoffset = '0';
318:             }
319:             window.currentActiveBtn = btn;
320:             window.currentActiveTimer = setTimeout(() => {
321:                 if (window.currentActiveBtn === btn) {
322:                     window.resetAudioState();
323:                 }
324:             }, 800);
325:         }
326:     };
327: 
328:     /* --- DEFINITION TRUNCATOR (3-line cap + click to expand, stays open) ---
329:        .is-truncated is set only when content truly overflows the 3-line
330:        cap, so short glosses never show a misleading fade/chevron. Expand
331:        is one-way: once open it never re-collapses (a second click is a
332:        no-op). Idempotent: safe under Anki WebView DOM re-use. */
333:     window.expandDefinition = function(element) {
334:       if (element.classList.contains('is-expanded')) return;
335:       element.classList.add('is-expanded');
336:       element.setAttribute('aria-expanded', 'true');
337:     };
338: 
339:     window.handleDefinitionKey = function(evt, element) {
340:       if (evt.key === 'Enter' || evt.key === ' ') {
341:         evt.preventDefault();
342:         window.expandDefinition(element);
343:       }
344:     };
345: 
346:     window.initDefinitionTruncation = function(root) {
347:       const scope = root || document;
348:       scope.querySelectorAll('.primary-definition').forEach(function(box) {
349:         /* Empty-field collapse (QUALITY.md): a definition section that
350:            survived its conditional with only whitespace leaves no bordered
351:            void — remove it. */
352:         if (!box.textContent || !box.textContent.trim()) { box.remove(); return; }
353:         box.classList.remove('is-expanded');
354:         box.setAttribute('aria-expanded', 'false');
355:         const overflows = box.scrollHeight > box.clientHeight + 2;
356:         box.classList.toggle('is-truncated', overflows);
357:       });
358:     };
359: 
360:     /* --- SECONDARY SECTION CLEANUP + KEYBOARD SHORTCUTS ---
361:        Empty-field collapse: remove the More toggle when no secondary
362:        content exists; strip empty secondary blocks themselves.
363:        Keyboard (back only): F toggles full-card furigana, T reveals
364:        the translation (opening More first when needed). Shortcuts are
365:        scoped to this card wrapper and never intercept typing fields. */
366:     window.initSecondarySection = function() {
367:       try {
368:         var section = document.querySelector('.more-section');
369:         var btn = document.querySelector('.more-toggle');
370:         if (section && btn) {
371:           section.querySelectorAll('.secondary-block, .translation-box, .revealed-static, .extended-full').forEach(function(el) {
372:             if (!el.textContent || !el.textContent.trim()) el.remove();
373:           });
374:           if (!section.querySelector('.secondary-block, .translation-box, .revealed-static, .extended-full')) {
375:             btn.remove();
376:             section.remove();
377:           }
378:         }
379:       } catch (e) { /* keep default rendering */ }
380:     };
381: 
382:     window.initCardShortcuts = function() {
383:       var wrapper = document.querySelector('.card-wrapper.back-card');
384:       if (!wrapper || wrapper.dataset.shortcutsBound) return;
385:       wrapper.dataset.shortcutsBound = '1';
386:       document.addEventListener('keydown', function(e) {
387:         if (e.altKey || e.ctrlKey || e.metaKey) return;
388:         var tag = (e.target && e.target.tagName) || '';
389:         if (tag === 'INPUT' || tag === 'TEXTAREA' || (e.target && e.target.isContentEditable)) return;
390:         var key = (e.key || '').toLowerCase();
391:         if (key === 'f') {
392:           wrapper.classList.toggle('furigana-mode');
393:         } else if (key === 't') {
394:           var box = wrapper.querySelector('.translation-box');
395:           if (box && !box.classList.contains('revealed')) {
396:             var moreBtn = wrapper.querySelector('.more-toggle');
397:             if (moreBtn && moreBtn.getAttribute('aria-expanded') !== 'true') window.toggleMore(moreBtn);
398:             box.classList.add('revealed');
399:             box.setAttribute('aria-expanded', 'true');
400:           }
401:         }
402:       });
403:     };
404: 
405:     window.initDefinitionTruncation();
406:     window.initSecondarySection();
407:     window.initCardShortcuts();
408:     /* Late fonts can reflow line breaks: re-check once loading settles. */
409:     try {
410:       if (document.fonts && document.fonts.ready) {
411:         document.fonts.ready.then(function() { window.initDefinitionTruncation(); });
412:       } else {
413:         window.addEventListener('load', function() { window.initDefinitionTruncation(); });
414:       }
415:     } catch (e) { /* measure-once fallback above already ran */ }
416:   })();
417: </script>

(End of file - total 417 lines)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: read
**Status:** completed
**Title:** Card 1 - Style.css

**Input:**
```json
{
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/Card 1 - Style.css",
  "limit": 2000
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/Card 1 - Style.css</path>
<type>file</type>
<content>
1: /**
2:  * ==============================================================================
3:  * Japanese Note Type — Minimal Japanese Reading Interface
4:  * (Tokyo Night Dark / Aki Paper Light)
5:  *
6:  * Source & documentation: https://github.com/mansourvery-hub/anki-japanese-template
7:  * Version: v1.5.0 — auto-bumped by finish.sh; matches the GitHub release tag
8:  *
9:  * Front = pure retrieval surface (sentence / word / audio only).
10:  * Back = strong hierarchy: target → reading → meaning → context →
11:  * secondary (collapsed behind "More ▾"). Anki is the SRS; this
12:  * template is presentation only — every visible element must justify
13:  * its screen space.
14:  *
15:  * Optimized for Arch Linux Desktop (Anki Qt6) and Samsung Galaxy A50
16:  * (AnkiDroid): cards size to their content; fluid clamp() tokens,
17:  * container queries with media-query fallback.
18:  * ==============================================================================
19:  */
20: 
21: /* ==============================================================================
22:    1. COLOR SYSTEM & CSS VARIABLES
23:    ============================================================================== */
24: :root {
25:   /* --- TOKYO NIGHT DARK (Default) --- */
26:   --bg-color: #0f141c;
27:   --card-bg: #182030;
28:   --card-border: rgba(255, 255, 255, 0.08);
29:   --text-primary: #f0f6fc;
30:   --text-secondary: #94a3b8;
31:   --text-muted: #64748b;
32:   
33:    --accent-color: #38bdf8;
34:   --accent-light: rgba(56, 189, 248, 0.12);
35:   --accent-soft: rgba(56, 189, 248, 0.22);
36:   --accent-glow: 0 0 16px rgba(56, 189, 248, 0.35);
37: 
38:   --shadow-premium: 0 6px 20px -3px rgba(0, 0, 0, 0.4);
39:   --border-radius-lg: 12px;
40:   --border-radius-md: 8px;
41:   --border-radius-sm: 6px;
42: 
43:   /* Spacing Tokens - Fluid viewport-based (single values, usable via padding: X Y).
44:      Tightened for density: the card should read as one compact hierarchy,
45:      not a stack of padded boxes. */
46:   --gap-block: clamp(2px, 0.8vmin, 6px);
47:   --block-pad-y: clamp(0px, 0.2vmin, 2px);
48:   --block-pad-x: clamp(6px, 1.4vmin, 14px);
49:   --container-pad-y: clamp(0px, 0.25vmin, 2px);
50:   --container-pad-x: clamp(2px, 0.7vmin, 8px);
51: 
52:   /* Furigana clearance: rt height (0.55em of parent font) + 2px hover gap.
53:      em-based so it scales with font size (which scales with viewport) —
54:      never a fixed pixel value. Consumed by furigana-bearing fields. */
55:   --furigana-headroom: calc(0.55em + 2px);
56:   
57:   /* Fonts */
58:   --font-japanese-serif: "Yu Mincho", "Hiragino Mincho ProN", "MS Mincho", "Noto Serif JP", serif;
59:   --font-japanese-sans: "Inter", "Hiragino Sans", "Meiryo", "Noto Sans JP", sans-serif;
60:   --font-interface: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
61:   
62:   --max-content-width: 100%;
63: }
64: 
65: /* --- AKI PAPER LIGHT THEME --- */
66: .card:not(.nightMode):not(.night_mode) {
67:   --bg-color: #fcfaf6;
68:   --card-bg: #ffffff;
69:   --card-border: #e4e2dd;
70:   --text-primary: #1a1b1e;
71:   --text-secondary: #4b5563;
72:   --text-muted: #9ca3af;
73:   
74:   --accent-color: #d97706;
75:   --accent-light: rgba(217, 119, 6, 0.08);
76:   --accent-soft: rgba(217, 119, 6, 0.16);
77:   --accent-glow: 0 0 16px rgba(217, 119, 6, 0.25);
78: 
79:   --shadow-premium: 0 4px 16px rgba(0, 0, 0, 0.06);
80: }
81: 
82: .card.nightMode,
83: .card.night_mode {
84:   /* These are redundant as they are identical to :root, but kept for specificity */
85:   --bg-color: #0f141c;
86:   --card-bg: #182030;
87:   --card-border: rgba(255, 255, 255, 0.08);
88:   --text-primary: #f0f6fc;
89:   --text-secondary: #94a3b8;
90:   --text-muted: #64748b;
91:   --accent-color: #38bdf8;
92:   --accent-light: rgba(56, 189, 248, 0.12);
93:   --accent-soft: rgba(56, 189, 248, 0.22);
94: }
95: 
96: 
97: /* ==============================================================================
98:    2. BASE CARD LAYOUT & CONTAINER
99:    ============================================================================== */
100: .card {
101:   background-color: var(--bg-color);
102:   color: var(--text-primary);
103:   font-family: var(--font-interface);
104:   margin: 0;
105:   padding: 0;
106:   text-align: center;
107:   -webkit-font-smoothing: antialiased;
108:   line-height: 1.45;
109:   -webkit-tap-highlight-color: transparent;
110: }
111: 
112: .card-wrapper {
113:   display: flex;
114:   flex-direction: column;
115:   width: 100%;
116:   /* Content-driven sizing: the card is exactly as tall as its content.
117:      No viewport fill — spare screen space stays BELOW the card, where
118:      it is harmless, instead of being distributed between sections. */
119:   margin: 0;
120:   padding: 0;
121:   container-type: inline-size;
122:   container-name: anki-card;
123: }
124: 
125: .card-container {
126:   width: 98%;
127:   max-width: 100%;
128:   margin: 0 auto;
129:   padding: var(--container-pad-y) var(--container-pad-x);
130:   box-sizing: border-box;
131: }
132: 
133: 
134: /* ==============================================================================
135:    3. RETRIEVAL-STATE LABEL & SECONDARY-INFO TOGGLE (back only, quiet)
136:    ============================================================================== */
137: /* Discreet Context / Word / Listening caption. Set by the front script;
138:    hover explains the two-tier maturity model. Never a big badge. */
139: .retrieval-state {
140:   font-size: 0.72rem;
141:   font-weight: 600;
142:   letter-spacing: 0.08em;
143:   text-transform: uppercase;
144:   color: var(--text-muted);
145:   cursor: help;
146:   user-select: none;
147:   padding: 2px 0 4px 0;
148: }
149: 
150: .retrieval-state .retrieval-state-label {
151:   display: inline-block;
152: }
153: 
154: /* "More ▾" — the single quiet control for all secondary information. */
155: .more-toggle {
156:   font-family: var(--font-interface);
157:   font-size: 0.8rem;
158:   font-weight: 600;
159:   letter-spacing: 0.04em;
160:   color: var(--text-muted);
161:   background: none;
162:   border: none;
163:   padding: 6px 14px;
164:   margin: 2px auto;
165:   display: block;
166:   cursor: pointer;
167:   border-radius: 12px;
168:   transition: color 0.15s ease-out, background-color 0.15s ease-out;
169:   user-select: none;
170:   -webkit-tap-highlight-color: transparent;
171: }
172: 
173: .more-toggle:hover,
174: .more-toggle:focus-visible {
175:   color: var(--accent-color);
176:   background-color: var(--accent-light);
177:   outline: none;
178: }
179: 
180: .more-toggle:focus-visible {
181:   outline: 2px solid var(--accent-color);
182:   outline-offset: 1px;
183: }
184: 
185: .more-toggle .more-caret {
186:   display: inline-block;
187:   margin-left: 4px;
188:   transition: transform 0.15s ease-out;
189: }
190: 
191: .more-toggle.is-open .more-caret {
192:   transform: rotate(180deg);
193: }
194: 
195: .more-section {
196:   margin-top: 4px;
197: }
198: 
199: 
200: /* ==============================================================================
201:    4. CONTEXT GRID (core info: sentence + picture)
202:    ============================================================================== */
203: /* Minimal layout: no side dashboard. The picture is CORE information
204:    and sits beside the sentence when the viewport is wide and both
205:    exist; otherwise everything stacks in one quiet column. */
206: .context-grid {
207:   display: flex;
208:   flex-direction: column;
209:   gap: var(--gap-block);
210:   align-items: center;
211: }
212: 
213: .context-main {
214:   width: 100%;
215:   min-width: 0;
216:   text-align: center;
217: }
218: 
219: .context-picture {
220:   width: 100%;
221:   text-align: center;
222: }
223: 
224: @container anki-card (min-width: 768px) {
225:   /* Sentence left, picture right — only when a picture actually
226:      exists. The picture hugs its own width; the sentence dominates. */
227:   .context-grid:has(.context-picture) {
228:     flex-direction: row;
229:     align-items: center;
230:     gap: clamp(8px, 1.5vmin, 18px);
231:   }
232: 
233:   .context-main {
234:     flex: 1 1 auto;
235:   }
236: 
237:   .context-picture {
238:     flex: 0 1 auto;
239:     width: auto;
240:     max-width: 42vw;
241:   }
242: 
243:   /* Dense card, but the desktop is still a pointer+keyboard environment:
244:      keep the small audio buttons at their a11y-friendly 44px floor. */
245:   .small-audio-btn {
246:     width: 44px;
247:     height: 44px;
248:   }
249: }
250: 
251: /* Portability fallback for WebViews without container-query support
252:    (older AnkiDroid): same arrangement via a conventional media query. */
253: @media (min-width: 768px) {
254:   .context-grid:has(.context-picture) {
255:     flex-direction: row;
256:     align-items: center;
257:     gap: clamp(8px, 1.5vmin, 18px);
258:   }
259: 
260:   .context-main {
261:     flex: 1 1 auto;
262:   }
263: 
264:   .context-picture {
265:     flex: 0 1 auto;
266:     width: auto;
267:     max-width: 42vw;
268:   }
269: }
270: 
271: .card-block {
272:   background-color: var(--card-bg);
273:   border: 1px solid var(--card-border);
274:   border-radius: var(--border-radius-lg);
275:   padding: var(--block-pad-y) var(--block-pad-x);
276:   box-shadow: var(--shadow-premium);
277:   text-align: left;
278: }
279: 
280: 
281: /* ==============================================================================
282:     5. FRONT CARD TYPOGRAPHY - Fluid Sizing
283:        One base clamp for all screens (vmin respects height too), plus a
284:        smaller override in the mobile block (section 13) for phones.
285:     ============================================================================== */
286: .sentence-display,
287: .front-word-display {
288:   font-family: var(--font-japanese-serif);
289:   /* Density-tuned cap: 5.25rem keeps the sentence dominant without
290:      flooding a widescreen front with a single line of huge text. */
291:   font-size: clamp(1.8rem, 5vmin + 0.75rem, 5.25rem);
292:   line-height: 1.3;
293:   padding: 4px 6px;
294:   text-align: center;
295:   width: 100%;
296:   box-sizing: border-box;
297:   margin: 0 auto;
298:   font-weight: 400;
299:   overflow-wrap: anywhere;
300: }
301: 
302: /* Front: Yomitan wraps the target word in <b> even for word-only fronts
303:    (Sentence field = "<b>word</b>"). Force it light — color + underline
304:    still mark it without the heavy stroke. */
305: .sentence-display b,
306: .sentence-display strong,
307: .front-word-display b,
308: .front-word-display strong {
309:   color: var(--accent-color);
310:   font-weight: 400;
311:   background: linear-gradient(transparent 75%, var(--accent-light) 75%);
312:   padding: 0 4px;
313: }
314: 
315: /* Back sentence target matches surrounding weight — color + underline mark it. */
316: .sentence-japanese b,
317: .sentence-japanese strong {
318:   color: var(--accent-color);
319:   font-weight: 400;
320:   background: linear-gradient(transparent 75%, var(--accent-light) 75%);
321:   padding: 0 4px;
322: }
323: 
324: /* Back headword: never bold, even if Yomitan injects <b>/<strong>. */
325: .word-display b,
326: .word-display strong {
327:   font-weight: 400;
328: }
329: 
330: /* 5b. MATURE-CARD WORD MODE
331:    Used when card interval >= LONG_INTERVAL_DAYS.
332:    Swaps the sentence display for the bare expression. */
333: .front-word-display {
334:   display: none;
335:   font-weight: 400;
336: }
337: 
338: .card-wrapper.word-mode .sentence-display {
339:   display: none;
340: }
341: 
342: .card-wrapper.word-mode .front-word-display {
343:   display: block;
344: }
345: 
346: 
347: /* ==============================================================================
348:     6. BACK CARD HIERARCHY — target, reading, meaning (Fluid Typography)
349:     ============================================================================== */
350: /* Target + reading form ONE conceptual unit, centered, the loudest
351:    element on the card. Frequency/pitch badges are gone (visual noise
352:    without retrieval value); pitch stays as quiet muted text below. */
353: 
354: /* Furigana headroom: ruby rt renders 0.55em above the text with a 2px gap.
355:    Fields that use {{furigana:...}} get exactly that clearance as top padding
356:    (plus the base pad), so hover furigana never clips or overlaps neighbors.
357:    em-based => scales continuously with font size across all screen sizes. */
358: .word-display {
359:   font-family: var(--font-japanese-serif);
360:   /* The headword stays the loudest element on the card. */
361:   font-size: clamp(2.5rem, 5vw + 1rem, 5.75rem);
362:   font-weight: 400;
363:   line-height: 1.05;
364:   padding-top: calc(var(--block-pad-y, 0px) + var(--furigana-headroom));
365:   margin: 0 auto;
366:   text-align: center;
367: }
368: 
369: /* Pitch accent: quiet muted supplement to the reading, never a badge. */
370: .pitch-quiet {
371:   font-size: clamp(0.9rem, 0.8vw + 0.75rem, 1.15rem);
372:   color: var(--text-muted);
373:   line-height: 1.4;
374:   margin-top: 2px;
375:   text-align: center;
376: }
377: 
378: /* Audio row: the two quiet replay buttons under the meaning. */
379: .audio-row {
380:   display: flex;
381:   align-items: center;
382:   justify-content: center;
383:   flex-wrap: wrap;
384:   gap: 10px;
385:   margin: 6px 0 2px 0;
386: }
387: 
388: /* Empty-shell guard (QUALITY.md "Empty-field collapse"): .audio-row
389:    renders unconditionally while its buttons are conditional — collapse
390:    the shell when every child is absent so no margin/gap survives an
391:    empty field. */
392: .audio-row:not(:has(.circular-audio-btn)) {
393:   display: none;
394: }
395: 
396: .definition-box {
397:   /* Medium emphasis: clearly smaller than the sentence, one step above
398:      notes/translation. Fluid so wide main columns stay filled. */
399:   font-size: clamp(1.05rem, 0.45vw + 0.85rem, 1.55rem);
400:   /* Furigana-safe density: the Definition field is furigana-bearing
401:      ({{furigana:...}}), and hover rt renders in the inter-line gap, so
402:      line-height must stay >= headroom + 1em. 1.5 satisfies that with a
403:      little slack; the old 1.6 was roomier than rt ever needs. */
404:   line-height: calc(var(--furigana-headroom) + 1em + 0.05em);
405:   color: var(--text-primary);
406:   border-top: 1px solid var(--card-border);
407:   /* Furigana headroom: rt renders 0.55em + 2px above the text — reserve
408:      exactly that (em-based, scales with fluid font size). */
409:   padding-top: var(--furigana-headroom);
410:   margin-top: 5px;
411:   width: 100%;
412: }
413: 
414: 
415: /* ==============================================================================
416:    6b. DEFINITION COMPACTOR (scope: .primary-definition ONLY)
417:    ==============================================================================
418:    Yomitan mines the full Definition field as a .yomitan-glossary containing
419:    one <li data-dictionary="..."> per dictionary plus embedded <style> blocks.
420:    That is far too verbose for the main card. Rules below collapse it to:
421:      - 1 dictionary entry (the first)
422:      - at most 2 numbered senses within it
423:      - no appendices (possible-forms / synonym / supplementary blocks)
424:    Dictionary-agnostic: matches structural attributes, never dictionary
425:     names. Deliberately does NOT touch .extended-full (the full Yomitan
426:     definition inside the More section stays full) or any other field.
427:    ============================================================================== */
428: 
429: /* --- Collapse all dictionary entries after the first --- */
430: /* List markers: Yomitan emits <ol><li> per dictionary; suppress the "1."
431:    numbering and the ol indent so the kept entry reads as plain text. */
432: .primary-definition .yomitan-glossary > ol {
433:   list-style: none;
434:   margin: 0;
435:   padding-left: 0;
436: }
437: /* Dictionary name labels and metadata <i>(...)</i> are noise. */
438: .primary-definition i {
439:   display: none;
440: }
441: .primary-definition .yomitan-glossary > ol > li ~ li {
442:   display: none;
443: }
444: 
445: /* --- Keep at most 2 numbered senses per dictionary --- */
446: /* Structured dictionaries (data-sc-name variants: 語義G sense blocks in
447:    大辞林-style SC markup, data-sc-l3* sense wrappers in 大辞泉-style SC
448:    markup). Sibling chains select everything from the 3rd occurrence on. */
449: .primary-definition div[data-sc-name="語義G"] ~ div[data-sc-name="語義G"] ~ div[data-sc-name="語義G"],
450: .primary-definition div[data-sc-l3] ~ div[data-sc-l3] ~ div[data-sc-l3],
451: .primary-definition div[data-sc-l3-a] ~ div[data-sc-l3-a] {
452:   display: none;
453: }
454: 
455: /* Simple merged dictionaries: plain gloss <li> lists — keep max 2 glosses */
456: .primary-definition [data-sc-content="glossary"] > li ~ li ~ li {
457:   display: none;
458: }
459: 
460: /* --- Hide sense appendices (any dictionary, structural match) --- */
461: /* 補説G = supplementary note; 可能形 = possible-form line;
462:    歴史仮名 = historical kana reading; アクセントG = accent [n] notation
463:    (hiding the group also hides its nested [n] number) */
464: .primary-definition div[data-sc-name="補説G"],
465: .primary-definition span[data-sc-name="可能形"],
466: .primary-definition span[data-sc-name="歴史仮名"],
467: .primary-definition span[data-sc-name="アクセントG"],
468: .primary-definition li[data-sc-content="forms"] {
469:   display: none;
470: }
471: 
472: /* Hide attribution (JMdict | Tatoeba) */
473: .primary-definition div[data-sc-content="attribution"] {
474:   display: none;
475: }
476: 
477: /* Yomitan inline <style> blocks inside the glossary leak their own rules
478:    (list display modes, per-dictionary colors). Neutralize styling that
479:    fights the card theme; keep size/margins untouched so SC layouts hold. */
480: .primary-definition .yomitan-glossary ul[data-sc-content="glossary"] {
481:   display: inline;
482:   list-style: none;
483:   padding-left: 0;
484: }
485: .primary-definition .yomitan-glossary ul[data-sc-content="glossary"] > li {
486:   display: inline;
487: }
488: .primary-definition .yomitan-glossary ul[data-sc-content="glossary"] > li:not(:first-child)::before {
489:   content: " | ";
490:   white-space: pre-wrap;
491:   display: inline;
492:   color: var(--text-muted);
493: }
494: 
495: /* ==============================================================================
496:     6c. DEFINITION TRUNCATOR & EXPANDABLE UI
497:     ==============================================================================
498:     Primary definition shows THREE lines by default (line-height computed
499:     from --furigana-headroom + 1em + 0.05em). Longer content clips and
500:     gets a progressive fade + one small ▼ chevron (no text label). Click,
501:     tap, Enter or Space expands to the full text and STAYS expanded
502:     (one-way: a second click never re-collapses it).
503: 
504:     Mechanics are deliberately boring so they hold for ANY nested Yomitan
505:     markup on every client (Qt6 WebEngine + AnkiDroid WebKit):
506:       - display:block + max-height + overflow:hidden clips everything.
507:         (-webkit-line-clamp was tried and reverted: it needs -webkit-box,
508:         miscounts nested block children, and silently kept .is-expanded
509:         clamped because the clamp was never unset on expand.)
510:       - .is-truncated is added by JS only when content truly overflows
511:         (scrollHeight > clientHeight), so short glosses never show a
512:         misleading fade/chevron. Without JS the box is just a plain full
513:         definition — never broken, never misleading.
514:     ============================================================================== */
515: 
516: /* Collapsed cap = 3 lines. Line-height is the furigana-headroom formula
517:    from .definition-box; max-height applies to the CONTENT box (no
518:    box-sizing override here), so the top headroom padding sits outside
519:    the cap — no extra term needed. */
520: .definition-box.primary-definition {
521:   position: relative;
522:   overflow: hidden;
523:   max-height: calc((var(--furigana-headroom) + 1em + 0.05em) * 3);
524:   cursor: default;
525: }
526: 
527: /* Expanded: cap removed entirely, stays expanded (no re-collapse) */
528: .definition-box.primary-definition.is-expanded {
529:   max-height: none;
530:   cursor: default;
531: }
532: 
533: /* Overflow confirmed by JS: clickable affordance */
534: .definition-box.primary-definition.is-truncated {
535:   cursor: pointer;
536: }
537: 
538: /* Progressive fade: line bottom dissolves into the card => "there's more" */
539: .definition-box.primary-definition.is-truncated:not(.is-expanded)::after {
540:   content: "";
541:   position: absolute;
542:   bottom: 0;
543:   left: 0;
544:   right: 0;
545:   height: 1.1em;
546:   background: linear-gradient(to bottom,
547:     transparent 0%,
548:     var(--card-bg) 100%
549:   );
550:   pointer-events: none;
551: }
552: 
553: /* Collapsed indicator: one small chevron, no text */
554: .definition-box.primary-definition.is-truncated:not(.is-expanded)::before {
555:   content: "▼";
556:   position: absolute;
557:   bottom: 0;
558:   left: 50%;
559:   transform: translateX(-50%);
560:   color: var(--text-muted);
561:   font-size: 0.65rem;
562:   line-height: 1;
563:   pointer-events: none;
564: }
565: 
566: .definition-box.primary-definition.is-truncated:not(.is-expanded):hover::before,
567: .definition-box.primary-definition.is-truncated:not(.is-expanded):focus-visible::before {
568:   color: var(--accent-color);
569: }
570: 
571: /* ==============================================================================
572:     7. CIRCULAR AUDIO BUTTON WITH SVG PROGRESS RING
573:     ============================================================================== */
574: .audio-row {
575:   display: inline-flex;
576:   align-items: center;
577:   gap: 10px;
578: }
579: 
580: .circular-audio-btn {
581:   position: relative;
582:   display: inline-flex;
583:   align-items: center;
584:   justify-content: center;
585:   background-color: var(--card-bg);
586:   border: 1px solid var(--card-border);
587:   border-radius: 50%;
588:   cursor: pointer;
589:   padding: 0;
590:   margin: 0;
591:   outline: none;
592:   box-shadow: 0 3px 8px rgba(0, 0, 0, 0.25);
593:   transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1),
594:               box-shadow 0.2s ease,
595:               border-color 0.2s ease,
596:               background-color 0.2s ease;
597:   user-select: none;
598:   -webkit-tap-highlight-color: transparent;
599: }
600: 
601: .small-audio-btn {
602:   width: 44px;
603:   height: 44px;
604: }
605: 
606: /* Keyboard focus indicator (outline: none above only affects mouse clicks;
607:    :focus-visible restores a compact accent ring for keyboard navigation) */
608: .circular-audio-btn:focus-visible,
609: .translation-box:focus-visible,
610: .picture-container:focus-visible {
611:   outline: 2px solid var(--accent-color);
612:   outline-offset: 2px;
613: }
614: 
615: .large-audio-btn {
616:   width: 80px;
617:   height: 80px;
618: }
619: 
620: .circular-audio-btn:hover,
621: .circular-audio-btn:active {
622:   transform: scale(1.08);
623:   border-color: var(--accent-color);
624:   box-shadow: var(--accent-glow);
625: }
626: 
627: .circular-audio-btn.is-playing {
628:   border-color: var(--accent-color);
629:   box-shadow: var(--accent-glow);
630:   background-color: var(--accent-light);
631: }
632: 
633: .audio-progress-ring {
634:   position: absolute;
635:   top: 0;
636:   left: 0;
637:   width: 100%;
638:   height: 100%;
639:   transform: rotate(-90deg);
640:   pointer-events: none;
641: }
642: 
643: .audio-progress-ring .ring-bg {
644:   fill: none;
645:   stroke: var(--accent-light);
646:   stroke-width: 3px;
647: }
648: 
649: .audio-progress-ring .ring-fill {
650:   fill: none;
651:   stroke: var(--accent-color);
652:   stroke-width: 3px;
653:   stroke-linecap: round;
654:   transition: stroke-dashoffset 0.08s linear;
655: }
656: 
657: .audio-btn-content {
658:   display: flex;
659:   align-items: center;
660:   justify-content: center;
661:   z-index: 2;
662: }
663: 
664: .small-audio-btn .audio-btn-label {
665:   font-family: var(--font-japanese-serif);
666:   font-size: 0.85rem;
667:   font-weight: 700;
668:   color: var(--accent-color);
669:   letter-spacing: 0.04em;
670:   line-height: 1;
671: }
672: 
673: .large-audio-btn .audio-btn-label {
674:   font-family: var(--font-japanese-serif);
675:   font-size: 1.5rem;
676:   font-weight: 700;
677:   color: var(--accent-color);
678:   letter-spacing: 0.04em;
679:   line-height: 1;
680: }
681: 
682: .circular-audio-btn.is-playing .audio-btn-label {
683:   color: var(--text-primary);
684: }
685: 
686: 
687: /* ==============================================================================
688:     8. SENTENCE & TRANSLATION - Fluid Typography
689:     ============================================================================== */
690: /* Level 3 (context): the sentence supports the target; it reads as
691:    context, not as the loudest element (that is the headword). */
692: .sentence-japanese {
693:   font-family: var(--font-japanese-serif);
694:   /* Hierarchy: second to the headword, dominant over the definition.
695:      Cap 3.5rem: with headroom-based line-height, every wrapped line costs
696:      ~1.65em, so a 4.5rem sentence was the single largest vertical expense
697:      on the card. 3.5rem keeps the example sentence loud but affordable. */
698:   font-size: clamp(1.8rem, 3.5vw + 0.9rem, 3.5rem);
699:   /* Multi-line clearance: each wrapped line needs room for hover furigana
700:      above it (rt height + gap), delivered via line-height. Final line is
701:      covered by --furigana-headroom on top padding below. */
702:   line-height: calc(var(--furigana-headroom) + 1em);
703:   padding-top: calc(var(--block-pad-y, 0px) + var(--furigana-headroom));
704:   margin-bottom: clamp(4px, 2vmin, 8px);
705:   color: var(--text-primary);
706:   text-align: center;
707: }
708: 
709: /* Secondary blocks inside the More section: quiet, no card-in-card. */
710: .secondary-block {
711:   font-size: clamp(1rem, 0.4vw + 0.8rem, 1.35rem);
712:   line-height: 1.5;
713:   color: var(--text-secondary);
714:   text-align: left;
715:   margin-top: 8px;
716: }
717: 
718: .translation-box {
719:   background-color: rgba(0, 0, 0, 0.15);
720:   border-left: 3px solid var(--accent-color);
721:   padding: 6px 10px;
722:   border-radius: 4px;
723:   cursor: pointer;
724:   transition: all 0.2s ease;
725:   width: 100%;
726:   box-sizing: border-box;
727:   margin-top: 5px;
728: }
729: 
730: .card:not(.nightMode):not(.night_mode) .translation-box {
731:   background-color: rgba(0, 0, 0, 0.03);
732: }
733: 
734: .translation-hint {
735:   font-size: 0.9rem;
736:   font-weight: 600;
737:   color: var(--text-muted);
738:   user-select: none;
739: }
740: 
741: .translation-text {
742:   display: none;
743:   /* Lower emphasis tier: floor sits below the definition's 1.05rem floor
744:      so revealed translations read as secondary. */
745:   font-size: clamp(1rem, 0.4vw + 0.8rem, 1.35rem);
746:   color: var(--text-secondary);
747:   line-height: 1.45;
748: }
749: 
750: .translation-box.revealed .translation-text { display: block; }
751: .translation-box.revealed .translation-hint { display: none; }
752: 
753: /* Orphan translation (no Sentence): rendered statically, same tier. */
754: .revealed-static.translation-text {
755:   display: block;
756:   font-size: clamp(1rem, 0.4vw + 0.8rem, 1.35rem);
757:   color: var(--text-secondary);
758:   line-height: 1.45;
759: }
760: 
761: .context-block {
762:   margin-top: 6px;
763: }
764: 
765: .html-content {
766:   /* Lower emphasis tier: notes/context are support material, quieter
767:      than the definition (and floor-below it, unlike before). */
768:   font-size: clamp(1rem, 0.4vw + 0.8rem, 1.35rem);
769:   line-height: 1.5;
770: }
771: 
772: 
773: /* ==============================================================================
774:    9. FURIGANA HOVER & TOUCH ERGONOMICS (Zero-Reflow / Zero-Shift)
775:    ============================================================================== */
776: ruby {
777:   position: relative;
778:   display: inline-block;
779:   line-height: 1;
780: }
781: 
782: ruby rt {
783:   position: absolute;
784:   left: 50%;
785:   transform: translateX(-50%);
786:   bottom: 100%;
787:   font-size: 0.55em;
788:   line-height: 1;
789:   white-space: nowrap;
790:   visibility: hidden;
791:   opacity: 0;
792:   color: var(--accent-color);
793:   transition: opacity 0.15s ease-out;
794:   pointer-events: none;
795:   user-select: none;
796:   /* Gap above the base text — part of the reserved headroom */
797:   margin-bottom: 2px;
798: }
799: 
800: /* Mouse Hover & Mobile Tap Active - 100% Shift-free */
801: ruby:hover rt,
802: ruby:active rt,
803: ruby:focus rt,
804: ruby:focus-within rt {
805:   visibility: visible;
806:   opacity: 1;
807: }
808: 
809: /* 9b. FULL-CARD FURIGANA MODE (back only; F toggles).
810:    Pins every rt visible at once — same absolute geometry, so nothing
811:    reflows. .furigana-mode lives on the back card wrapper only; the
812:    front is a retrieval surface and stays furigana-free. */
813: .card-wrapper.furigana-mode ruby rt {
814:   visibility: visible;
815:   opacity: 1;
816: }
817: 
818: 
819: /* ==============================================================================
820:    10. MEDIA & LIGHTBOX MODAL
821:    ============================================================================== */
822: .picture-container img {
823:   /* Block-level: kills the inline-baseline descender gap that left a few
824:      loose pixels under the image. margin-inline:auto handles centering. */
825:   display: block;
826:   margin-inline: auto;
827:   max-width: 100%;
828:   max-height: 40vh;
829:   height: auto;
830:   object-fit: contain;
831:   border-radius: var(--border-radius-md);
832:   border: 1px solid var(--card-border);
833:   cursor: zoom-in;
834:   transition: transform 0.2s ease;
835: }
836: 
837: .picture-container img:hover {
838:   transform: scale(1.015);
839: }
840: 
841: .lightbox-overlay {
842:   position: fixed;
843:   top: 0;
844:   left: 0;
845:   width: 100%;
846:   height: 100%;
847:   background: rgba(0, 0, 0, 0.72);
848:   z-index: 2000;
849:   backdrop-filter: blur(10px);
850:   -webkit-backdrop-filter: blur(10px);
851:   display: flex;
852:   align-items: center;
853:   justify-content: center;
854:   cursor: zoom-out;
855: }
856: 
857: .expanded-img {
858:   position: fixed;
859:   top: 50%;
860:   left: 50%;
861:   transform: translate(-50%, -50%) scale(1);
862:   max-width: 96vw;
863:   max-height: 96vh;
864:   z-index: 2001;
865:   border-radius: var(--border-radius-md);
866:   box-shadow: 0 20px 60px rgba(0, 0, 0, 0.88);
867:   animation: lightboxIn 0.18s cubic-bezier(0.34, 1.56, 0.64, 1);
868: }
869: 
870: @keyframes lightboxIn {
871:   from {
872:     transform: translate(-50%, -50%) scale(0.92);
873:     opacity: 0;
874:   }
875:   to {
876:     transform: translate(-50%, -50%) scale(1);
877:     opacity: 1;
878:   }
879: }
880: 
881: 
882: /* ==============================================================================
883:    11. FOOTER
884:    ============================================================================== */
885: /* The full Yomitan definition (.extended-full inside the More section)
886:    and secondary blocks are plain quiet text — no cards-within-cards. */
887: 
888: .source-footer {
889:   text-align: center;
890:   padding: 4px 0;
891:   font-size: 0.75rem;
892:   font-weight: 600;
893:   color: var(--text-muted);
894:   letter-spacing: 0.04em;
895:   text-transform: uppercase;
896: }
897: 
898: 
899: /* ==============================================================================
900:    12. LISTENING MODE FRONT
901:    ============================================================================== */
902: /* The listening markup renders whenever Sentence Audio exists but is
903:    INERT until the front resolver confirms the listening condition
904:    (classic audio-only fields or #listening tag) and adds
905:    .listening-mode to the wrapper. Any other card with sentence audio
906:    never sees it; no-JS renders keep the sentence front. */
907: .listening-view {
908:   display: none;
909:   align-items: center;
910:   justify-content: center;
911:   /* Deliberate presence: enough height that the lone audio button reads
912:       as THE card, not an accident — but a fraction of the old 32px-padded
913:       slab. 28vh is the sweet spot for both the desktop reviewer and the
914:       A50's tall screen. */
915:   min-height: 28vh;
916:   padding: 12px;
917: }
918: 
919: .card-wrapper.listening-mode .listening-view {
920:   display: flex;
921: }
922: 
923: /* Listening mode is exclusive with the sentence/word fronts. */
924: .card-wrapper.listening-mode .sentence-display,
925: .card-wrapper.listening-mode .front-word-display {
926:   display: none;
927: }
928: 
929: .audio-btn-wrapper {
930:   display: inline-flex;
931:   align-items: center;
932:   justify-content: center;
933:   position: relative;
934: }
935: 
936: /* Holds Anki's own replay link. Visually hidden but KEPT in layout:
937:    display:none breaks programmatic .click() playback on some clients,
938:    and the link must not live inside the <button> (invalid HTML that
939:    Android WebView mishandles). */
940: .raw-audio-source {
941:   position: absolute;
942:   width: 1px;
943:   height: 1px;
944:   margin: -1px;
945:   padding: 0;
946:   overflow: hidden;
947:   clip: rect(0 0 0 0);
948:   white-space: nowrap;
949:   opacity: 0;
950:   pointer-events: none;
951: }
952: 
953: 
954: /* ==============================================================================
955:     13. MOBILE SPECIFIC OPTIMIZATIONS (< 600px / Samsung Galaxy A50)
956:     Density, hierarchy, furigana, and JS interactions stay intact on the
957:     narrow screen.
958:     ============================================================================== */
959: @media (max-width: 600px) {
960:   .sentence-display,
961:   .front-word-display {
962:     font-size: clamp(1rem, 3vmin + 0.75rem, 2rem);
963:     padding: 2px 4px;
964:   }
965:   .sentence-japanese {    font-size: clamp(1rem, 3vmin + 0.75rem, 2rem);}
966:   .word-display {
967:     font-size: clamp(1.6rem, 2.8vmin + 1rem, 2.6rem);
968:   }
969: 
970:   .picture-container img {
971:     max-height: clamp(20vh, 15vmin, 25vh);
972:     border-radius: clamp(3px, 1vmin, 4px);
973:   }
974: 
975:   .audio-row {
976:     gap: clamp(3px, 1vmin, 4px);
977:   }
978: 
979:   .small-audio-btn {
980:     width: clamp(36px, 10vmin, 40px);
981:     height: clamp(36px, 10vmin, 40px);
982:   }
983: 
984:   .small-audio-btn .audio-btn-label {
985:     font-size: clamp(0.6rem, 2vmin, 0.7rem);
986:   }
987: 
988:   .more-toggle {
989:     font-size: 0.75rem;
990:     padding: 5px 12px;
991:   }
992: }
993: 
994: 
995: /* ==============================================================================
996:     14. BACKDROP SYSTEM (Back card only)
997:     ==============================================================================
998:     Full-card decorative background: fully isolated and swappable.
999:     inspired  by thttps://miaai-lab.github.io/Fable-5.1-100-HTML-Files/
1000:     ENABLE / DISABLE THE BACKDROP
1001:       Delete or comment out everything between the two marker lines
1002:       ".backdrop-block-start" and ".backdrop-block-end" below. The rules
1003:       between the markers contain no comments of their own, so the whole
1004:       region can also be wrapped in a single block comment, or each rule
1005:       deleted individually. Nothing else in this stylesheet depends on
1006:       this block; the Back card then renders exactly as before this
1007:       section existed.
1008: 
1009:     SWAP THE BACKGROUND (any future scene)
1010:       Edit ONLY the two --backdrop-image lines (rule 3 = dark theme,
1011:       rule 4 = Aki Paper light theme). Any CSS background value works:
1012:       a data-URI SVG, url(...), a gradient... The other rules are
1013:       art-agnostic plumbing:
1014: 
1015:       Block contents, in order:
1016:         1. strength dial: --backdrop-opacity (currently 0.5)
1017:         2. generic placement: fixed full-viewport, bottom-anchored, cover
1018:         3. dark-theme scene: --backdrop-image (paper-cut Fuji)
1019:         4. light-theme scene: --backdrop-image (washi-tone variant)
1020:         5. z-index plumbing: keeps card content above the scene
1021:     ============================================================================== */
1022: 
1023: /* ================= .backdrop-block-start =================
1024:    (delete or comment everything from here...
1025: */
1026: 
1027: .card.back-card {
1028:   --backdrop-opacity: 0.5;
1029: }
1030: 
1031: .card.back-card::before {
1032:   content: "";
1033:   position: fixed;
1034:   top: 0;
1035:   left: 0;
1036:   right: 0;
1037:   bottom: 0;
1038:   z-index: 0;
1039:   pointer-events: none;
1040:   background-image: var(--backdrop-image);
1041:   background-repeat: no-repeat;
1042:   background-size: cover;
1043:   background-position: bottom center;
1044:   opacity: var(--backdrop-opacity, 0.5);
1045: }
1046: 
1047: .back-card::before {
1048:   --backdrop-image: url("data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201600%20900'%20preserveAspectRatio='xMidYMax%20slice'%3E%3Ccircle%20cx='730'%20cy='380'%20r='140'%20fill='%23c9575f'/%3E%3Cpath%20d='M400%20900%20L400%20780%20C600%20620%20720%20460%20790%20335%20L815%20300%20C835%20285%20885%20285%20905%20300%20L930%20335%20C1000%20460%201120%20620%201280%20780%20L1280%20900%20Z'%20fill='%232e3a5c'/%3E%3Cpath%20d='M772%20362%20L815%20300%20C835%20285%20885%20285%20905%20300%20L948%20362%20C920%20370%20895%20358%20868%20364%20C840%20370%20815%20358%20795%20364%20C786%20366%20778%20364%20772%20362%20Z'%20fill='%23d8dde8'/%3E%3Cpath%20d='M-40%20900%20L-40%20812%20C240%20762%20480%20792%20720%20776%20C960%20760%201180%20724%201400%20748%20C1480%20756%201560%20772%201640%20782%20L1640%20900%20Z'%20fill='%23232f4d'/%3E%3Cpath%20d='M-40%20900%20L-40%20852%20C280%20812%20540%20842%20800%20828%20C1040%20816%201260%20786%201460%20818%20C1520%20828%201600%20844%201640%20838%20L1640%20900%20Z'%20fill='%231b2440'/%3E%3Cpath%20d='M-40%20900%20L-40%20880%20C320%20854%20620%20872%20900%20864%20C1140%20858%201390%20840%201640%20866%20L1640%20900%20Z'%20fill='%23151d33'/%3E%3C/svg%3E");
1049: }
1050: 
1051: .card:not(.nightMode):not(.night_mode) .card.back-card::before {
1052:   --backdrop-image: url("data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201600%20900'%20preserveAspectRatio='xMidYMax%20slice'%3E%3Ccircle%20cx='730'%20cy='380'%20r='140'%20fill='%23cc5f43'/%3E%3Cpath%20d='M400%20900%20L400%20780%20C600%20620%20720%20460%20790%20335%20L815%20300%20C835%20285%20885%20285%20905%20300%20L930%20335%20C1000%20460%201120%20620%201280%20780%20L1280%20900%20Z'%20fill='%23d8bd96'/%3E%3Cpath%20d='M772%20362%20L815%20300%20C835%20285%20885%20285%20905%20300%20L948%20362%20C920%20370%20895%20358%20868%20364%20C840%20370%20815%20358%20795%20364%20C786%20366%20778%20364%20772%20362%20Z'%20fill='%23fbf7ee'/%3E%3Cpath%20d='M-40%20900%20L-40%20812%20C240%20762%20480%20792%20720%20776%20C960%20760%201180%20724%201400%20748%20C1480%20756%201560%20772%201640%20782%20L1640%20900%20Z'%20fill='%23e8dcc6'/%3E%3Cpath%20d='M-40%20900%20L-40%20852%20C280%20812%20540%20842%20800%20828%20C1040%20816%201260%20786%201460%20818%20C1520%20828%201600%20844%201640%20838%20L1640%20900%20Z'%20fill='%23dcc8a6'/%3E%3Cpath%20d='M-40%20900%20L-40%20880%20C320%20854%20620%20872%20900%20864%20C1140%20858%201390%20840%201640%20866%20L1640%20900%20Z'%20fill='%23cfb390'/%3E%3C/svg%3E");
1053: }
1054: 
1055: .back-card .card-container {
1056:   position: relative;
1057:   z-index: 1;
1058: }
1059: 
1060: /* ...to here) ================== .backdrop-block-end ================= */
1061: 
1062: 
1063: /* ==============================================================================
1064:     15. REDUCED MOTION
1065:     ============================================================================== */
1066: 
1067: @media (prefers-reduced-motion: reduce) {
1068:   *,
1069:   *::before,
1070:   *::after {
1071:     transition-duration: 0.01ms !important;
1072:     animation-duration: 0.01ms !important;
1073:     animation-iteration-count: 1 !important;
1074:   }
1075: }

(End of file - total 1075 lines)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: read
**Status:** completed
**Title:** fetch_anki_fields.py

**Input:**
```json
{
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/fetch_anki_fields.py"
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/fetch_anki_fields.py</path>
<type>file</type>
<content>
1: #!/usr/bin/env python3
2: """Fetch live note-type field names + descriptions from Anki (read-only).
3: 
4: Fields are managed EXCLUSIVELY inside the Anki UI — this repo keeps no
5: static field list. Agents must run this script at session start (see
6: AGENTS.md rule 0) and read the generated `.anki_fields.json` snapshot
7: instead of guessing field names.
8: 
9: Usage:  python3 fetch_anki_fields.py
10: Output: .anki_fields.json (gitignored) + the field list on stdout.
11: 
12: Requires: Anki running with the Anki-Connect add-on.
13: Standard library only (mirrors sync_to_anki.py).
14: """
15: 
16: import json
17: import os
18: import sys
19: import urllib.request
20: 
21: # Keep in sync with sync_to_anki.py
22: ANKI_CONNECT_URL = "http://127.0.0.1:8765"
23: MODEL_NAME = "Japanese Note type (Sentence card by Default)"
24: 
25: SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
26: OUT_FILE = os.path.join(SCRIPT_DIR, ".anki_fields.json")
27: 
28: 
29: def _anki(action, **params):
30:     req = urllib.request.Request(
31:         ANKI_CONNECT_URL,
32:         data=json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8"),
33:         headers={"Content-Type": "application/json"},
34:     )
35:     try:
36:         with urllib.request.urlopen(req, timeout=10) as response:
37:             result = json.loads(response.read().decode("utf-8"))
38:     except Exception as e:
39:         print(f"ERROR: Could not reach Anki-Connect at {ANKI_CONNECT_URL}. "
40:               f"Is Anki running with the add-on installed? ({e})")
41:         sys.exit(1)
42:     if result.get("error"):
43:         print(f"ERROR: Anki-Connect returned: {result['error']}")
44:         sys.exit(1)
45:     return result.get("result")
46: 
47: 
48: def _anki_soft(action, **params):
49:     """Like _anki but returns None instead of exiting (optional data)."""
50:     req = urllib.request.Request(
51:         ANKI_CONNECT_URL,
52:         data=json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8"),
53:         headers={"Content-Type": "application/json"},
54:     )
55:     try:
56:         with urllib.request.urlopen(req, timeout=10) as response:
57:             result = json.loads(response.read().decode("utf-8"))
58:     except Exception:
59:         return None
60:     return result.get("result") if not result.get("error") else None
61: 
62: 
63: def main():
64:     fields = _anki("modelFieldNames", modelName=MODEL_NAME)
65:     if not isinstance(fields, list) or not fields:
66:         print(f"ERROR: no fields returned for model '{MODEL_NAME}' — does it still exist?")
67:         sys.exit(1)
68:     # Descriptions are typed by the user in Anki (Fields dialog). Older
69:     # Anki-Connect builds lack this action — degrade to names only.
70:     descriptions = _anki_soft("modelFieldDescriptions", modelName=MODEL_NAME)
71:     if not isinstance(descriptions, list) or len(descriptions) != len(fields):
72:         descriptions = [""] * len(fields)
73:     entries = [
74:         {"name": name, "description": desc or ""}
75:         for name, desc in zip(fields, descriptions)
76:     ]
77:     with open(OUT_FILE, "w", encoding="utf-8") as f:
78:         json.dump({"model": MODEL_NAME, "fields": entries}, f, ensure_ascii=False, indent=2)
79:         f.write("\n")
80:     print(f"Model: {MODEL_NAME} ({len(entries)} fields) -> .anki_fields.json")
81:     for i, entry in enumerate(entries):
82:         line = f"  {i:2d}. {entry['name']}"
83:         if entry["description"]:
84:             line += f" — {entry['description']}"
85:         print(line)
86: 
87: 
88: if __name__ == "__main__":
89:     main()

(End of file - total 89 lines)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: read
**Status:** completed
**Title:** sync_to_anki.py

**Input:**
```json
{
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/sync_to_anki.py"
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/sync_to_anki.py</path>
<type>file</type>
<content>
1: import urllib.request
2: import json
3: import os
4: import sys
5: from datetime import datetime
6: 
7: # Configuration for the Japanese Note Type
8: ANKI_CONNECT_URL = "http://127.0.0.1:8765"
9: MODEL_NAME = "Japanese Note type (Sentence card by Default)"
10: 
11: # Resolve project root so the script works from any directory
12: SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
13: 
14: FRONT_FILE = os.path.join(SCRIPT_DIR, "Card 1 - Front.template.anki")
15: BACK_FILE = os.path.join(SCRIPT_DIR, "Card 1 - Back.template.anki")
16: CSS_FILE = os.path.join(SCRIPT_DIR, "Card 1 - Style.css")
17: 
18: # Pre-sync snapshots of the live Anki state (gitignored safety net)
19: BACKUP_DIR = os.path.join(SCRIPT_DIR, "backups")
20: 
21: 
22: def _read_file(path: str) -> str:
23:     """Read a UTF-8 file from the project directory."""
24:     try:
25:         with open(path, "r", encoding="utf-8") as f:
26:             return f.read()
27:     except FileNotFoundError:
28:         print(f"ERROR: Template file not found: {path}")
29:         sys.exit(1)
30:     except OSError as e:
31:         print(f"ERROR: Could not read {path}: {e}")
32:         sys.exit(1)
33: 
34: 
35: def _send_payload(action: str, params: dict = None) -> dict:
36:     """Send a payload to Anki-Connect and return the parsed response."""
37:     payload = {
38:         "action": action,
39:         "version": 6,
40:         "params": params or {},
41:     }
42:     req = urllib.request.Request(
43:         ANKI_CONNECT_URL,
44:         data=json.dumps(payload).encode("utf-8"),
45:         headers={"Content-Type": "application/json"},
46:     )
47:     try:
48:         with urllib.request.urlopen(req, timeout=10) as response:
49:             result = json.loads(response.read().decode("utf-8"))
50:     except urllib.error.URLError as e:
51:         print(f"ERROR: Could not connect to Anki-Connect. Is Anki running with the add-on installed? {e}")
52:         sys.exit(1)
53:     except Exception as e:
54:         print(f"ERROR: Anki-Connect request failed: {e}")
55:         sys.exit(1)
56: 
57:     if result.get("error"):
58:         print(f"ERROR: Anki-Connect returned: {result['error']}")
59:         sys.exit(1)
60:     return result
61: 
62: 
63: def snapshot_live_state():
64:     """Pull the live model from Anki into backups/<timestamp>/ before pushing.
65: 
66:     Guard against clobbering unnoticed Anki-side edits: the snapshot keeps the
67:     exact state that is about to be overwritten, so any manual change made in
68:     the Anki UI stays recoverable. Failures here abort the sync (never push
69:     over a state we failed to back up).
70:     """
71:     templates = _send_payload("modelTemplates", {"modelName": MODEL_NAME})
72:     styling = _send_payload("modelStyling", {"modelName": MODEL_NAME})
73: 
74:     tpls = templates.get("result") or {}
75:     sty = styling.get("result") or {}
76:     if not tpls or not isinstance(tpls, dict) or not sty.get("css"):
77:         print("ERROR: live Anki state looks empty (model missing?) — aborting sync")
78:         sys.exit(1)
79: 
80:     stamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
81:     dest = os.path.join(BACKUP_DIR, stamp)
82:     os.makedirs(dest, exist_ok=True)
83:     for card_name, pair in tpls.items():
84:         safe = card_name.replace(os.sep, "_")
85:         with open(os.path.join(dest, f"{safe}.front.anki"), "w", encoding="utf-8") as f:
86:             f.write(pair.get("Front", ""))
87:         with open(os.path.join(dest, f"{safe}.back.anki"), "w", encoding="utf-8") as f:
88:             f.write(pair.get("Back", ""))
89:     with open(os.path.join(dest, "style.css"), "w", encoding="utf-8") as f:
90:         f.write(sty.get("css", ""))
91:     print(f"Backup:        {os.path.relpath(dest, SCRIPT_DIR)}/")
92:     return dest
93: 
94: 
95: def sync_to_anki():
96:     """
97:     Reads local template files and pushes them to Anki via Anki-Connect.
98:     This automates the manual copy-paste process for faster iteration.
99:     """
100:     # 1. Read local files (UTF-8 for proper Japanese text handling)
101:     front_html = _read_file(FRONT_FILE)
102:     back_html = _read_file(BACK_FILE)
103:     css_content = _read_file(CSS_FILE)
104: 
105:     # 2. Snapshot the live Anki state we are about to overwrite
106:     snapshot_live_state()
107: 
108:     # 3. Update Templates (Front/Back HTML)
109:     _send_payload("updateModelTemplates", {
110:         "model": {
111:             "name": MODEL_NAME,
112:             "templates": {
113:                 "Card 1": {
114:                     "Front": front_html,
115:                     "Back": back_html
116:                 }
117:             }
118:         }
119:     })
120:     print("Template Sync: Success")
121: 
122:     # 4. Update Styling (CSS)
123:     _send_payload("updateModelStyling", {
124:         "model": {
125:             "name": MODEL_NAME,
126:             "css": css_content
127:         }
128:     })
129:     print("Styling Sync:  Success")
130: 
131: 
132: if __name__ == "__main__":
133:     sync_to_anki()

(End of file - total 133 lines)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: read
**Status:** completed
**Title:** release_apkg.py

**Input:**
```json
{
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/release_apkg.py"
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/release_apkg.py</path>
<type>file</type>
<content>
1: #!/usr/bin/env python3
2: """Export the sample deck to dist/anki-japanese-template.apkg via Anki-Connect.
3: 
4: Called by finish.sh; can also be run standalone. The real Anki-Connect action
5: is `exportPackage` (params: deck, path, includeSched). The apkg is gitignored
6: (`*.apkg` in .gitignore) — it is distributed via GitHub Releases, never the
7: repo itself.
8: """
9: import os
10: import sys
11: import json
12: import urllib.request
13: import urllib.error
14: 
15: ANKI_CONNECT_URL = "http://127.0.0.1:8765"
16: DECK_NAME = "My Life Decks::Japanese::anki-japanese-template"
17: SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
18: EXPORT_PATH = os.path.join(SCRIPT_DIR, "dist", "anki-japanese-template.apkg")
19: 
20: 
21: def main() -> int:
22:     os.makedirs(os.path.dirname(EXPORT_PATH), exist_ok=True)
23:     payload = {
24:         "action": "exportPackage",
25:         "version": 6,
26:         "params": {"deck": DECK_NAME, "path": EXPORT_PATH, "includeSched": False},
27:     }
28:     
29:     req = urllib.request.Request(
30:         ANKI_CONNECT_URL,
31:         data=json.dumps(payload).encode("utf-8"),
32:         headers={"Content-Type": "application/json"},
33:     )
34:     
35:     try:
36:         with urllib.request.urlopen(req, timeout=180) as response:
37:             result = json.loads(response.read().decode("utf-8"))
38:     except urllib.error.URLError:
39:         print("ERROR: cannot reach Anki-Connect (is Anki running with the add-on?)")
40:         return 1
41:     except Exception as e:
42:         print(f"ERROR: export request failed: {e}")
43:         return 1
44: 
45:     if result.get("error") or not result.get("result"):
46:         print(f"ERROR: Anki-Connect export failed: {result.get('error') or 'unknown error'}")
47:         return 1
48: 
49:     if not os.path.isfile(EXPORT_PATH) or os.path.getsize(EXPORT_PATH) == 0:
50:         print(f"ERROR: expected export missing or empty: {EXPORT_PATH}")
51:         return 1
52: 
53:     print(f"Export OK: {EXPORT_PATH} ({os.path.getsize(EXPORT_PATH) / 1e6:.1f} MB)")
54:     return 0
55: 
56: 
57: if __name__ == "__main__":
58:     sys.exit(main())

(End of file - total 58 lines)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: read
**Status:** completed
**Title:** verify

**Input:**
```json
{
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/verify"
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/verify</path>
<type>file</type>
<content>
1: #!/usr/bin/env bash
2: # verify — repository's complete mandatory LOCAL quality gate.
3: #
4: # Side-effect free: runs checks only. Never touches Anki, never exports,
5: # never commits, never releases. Run it before declaring any task complete:
6: #
7: #   ./verify
8: #
9: # finish.sh step 0 delegates to this script, and CI re-runs it on every
10: # push — the three can never disagree. See TEST_STRATEGY.md for the
11: # layering (tiny test → targeted suite → ./verify → CI).
12: set -euo pipefail
13: 
14: cd "$(dirname "$0")"
15: 
16: if [ ! -d tests ]; then
17:   echo "(no tests/ directory — nothing to verify)"
18:   exit 0
19: fi
20: 
21: echo "==> verify: compactor regression tests"
22: python3 tests/test_compactor.py
23: echo "==> verify: template structural invariants"
24: python3 tests/test_templates.py
25: echo "==> verify: front-mode resolver behavior (listening semantics)"
26: python3 tests/test_front_modes.py
27: echo "==> verify: headless layout checks (skipped gracefully without Chrome)"
28: python3 tests/test_layout.py
29: echo "verify: OK"

(End of file - total 29 lines)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: read
**Status:** completed
**Title:** finish.sh

**Input:**
```json
{
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/finish.sh"
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/finish.sh</path>
<type>file</type>
<content>
1: #!/usr/bin/env bash
2: # =============================================================================
3: # finish.sh — single-command post-change routine.
4: #
5: # Run this at the end of ANY template change instead of remembering 5 steps:
6: #   ./finish.sh "<commit message>"
7: #
8: # Flags:
9: #   --local          Review mode: sync + export + commit only. Skips push and
10: #                    GitHub release. Use while iterating; finish the batch with
11: #                    a full run (no flag) to publish.
12: #   --minor          Bump the MINOR version segment (v1.x.0) instead of the
13: #                    patch segment. Use for multi-feature releases.
14: #   --prompt "text"  Append the user prompt to chat_history/opencode_prompts.txt
15: #                    BEFORE anything else runs (AGENTS.md rule 3), so the log
16: #                    lands in the same commit.
17: #
18: #   It executes, in order:
19: #   0. ./verify — local quality gate (compactor CSS + template invariants
20: #                 + layout; skipped silently when tests/ is absent)
21: #   1. version stamp  — compute the next release tag and rewrite the CSS
22: #                        header Version: line (full runs only; the stamp is
23: #                        what Anki receives in step 2, so it never lags)
24: #   2. sync_to_anki.py — push templates+CSS into Anki via Anki-Connect
25: #                        (also snapshots live Anki state into backups/)
26: #   3. release_apkg.py — export sample deck to dist/*.apkg via Anki-Connect
27: #   4. git commit     — stage everything (incl. chat_history log) & commit
28: #   5. GitHub release — auto-bump tag (v1.x.y) + apkg
29: #   6. git push       — push commit to origin/main; fetch the release tag
30: #                        (gh creates it remotely; local syncs for next bump)
31: #
32: # Any failure stops the chain with a clear message (set -e). Requires: Anki
33: # running with Anki-Connect, gh CLI authenticated (full mode only).
34: # =============================================================================
35: set -euo pipefail
36: 
37: cd "$(dirname "$0")"
38: 
39: # ---------- flag parsing ----------
40: LOCAL=0
41: BUMP_KIND=patch
42: PROMPT_TEXT=""
43: COMMIT_MSG=""
44: 
45: while [ $# -gt 0 ]; do
46:   case "$1" in
47:     --local)  LOCAL=1 ;;
48:     --minor)  BUMP_KIND=minor ;;
49:     --prompt) shift; PROMPT_TEXT="${1:?--prompt requires a text argument}" ;;
50:     -h|--help)
51:       sed -n '2,30p' "$0"; exit 0 ;;
52:     *)
53:       if [ -z "$COMMIT_MSG" ]; then
54:         COMMIT_MSG="$1"
55:       else
56:         echo "ERROR: unexpected extra argument: $1 (commit message already set)" >&2
57:         exit 1
58:       fi ;;
59:   esac
60:   shift
61: done
62: 
63: [ -n "$COMMIT_MSG" ] || { echo 'Usage: ./finish.sh "<commit message>" [--local] [--minor] [--prompt "text"]' >&2; exit 1; }
64: 
65: # ---------- optional prompt archiving (before anything else) ----------
66: if [ -n "$PROMPT_TEXT" ]; then
67:   printf '\n---\n\n%s\n' "$PROMPT_TEXT" >> chat_history/opencode_prompts.txt
68:   echo "    (prompt archived to chat_history/opencode_prompts.txt)"
69: fi
70: 
71: # ---------- step 0: regression tests (delegates to ./verify, the local gate) ----------
72: if [ -d tests ]; then
73:   echo "==> [0/6] Running regression tests (./verify)"
74:   ./verify
75: fi
76: 
77: # ---------- step 1: version stamp (BEFORE the sync so Anki gets the new tag) ----------
78: # Local runs skip it: no release is published, so the stamp stays at the
79: # last released version and the working tree is not polluted.
80: NEW_TAG=""
81: if [ "$LOCAL" -eq 0 ]; then
82:   git fetch origin "refs/tags/*:refs/tags/*" --quiet
83:   # Auto-bump version from the latest existing tag (v<major>.<minor>.<patch>)
84:   LATEST_TAG="$(git tag --sort=-v:refname | grep -E '^v[0-9]+\.[0-9]+\.[0-9]+$' | head -1 || true)"
85:   if [ -z "$LATEST_TAG" ]; then
86:     NEW_TAG="v1.0.1"
87:   else
88:     NEW_TAG="$(python3 - "$LATEST_TAG" "$BUMP_KIND" <<'PY'
89: import sys
90: major, minor, patch = sys.argv[1][1:].split(".")
91: if sys.argv[2] == "minor":
92:     print(f"v{major}.{int(minor) + 1}.0")
93: else:
94:     print(f"v{major}.{minor}.{int(patch) + 1}")
95: PY
96: )"
97:   fi
98:   # Rewrite the Version: line in the CSS header comment. The stamp is what
99:   # step 2 pushes to Anki and what step 4 commits — tag, tree and the live
100:   # template can never disagree.
101:   python3 - "$NEW_TAG" <<'PY'
102: import re, sys
103: tag = sys.argv[1]
104: path = "Card 1 - Style.css"
105: css = open(path, encoding="utf-8").read()
106: new, n = re.subn(
107:     r"( \* Version: )v[0-9]+\.[0-9]+\.[0-9]+[^\n]*",
108:     rf"\g<1>{tag} — auto-bumped by finish.sh; matches the GitHub release tag",
109:     css, count=1)
110: if n and new != css:
111:     open(path, "w", encoding="utf-8").write(new)
112:     print(f"    (stamped {tag} into Card 1 - Style.css header)")
113: PY
114: fi
115: 
116: echo "==> [1/6] Syncing templates to Anki (Anki-Connect)"
117: python3 sync_to_anki.py
118: 
119: echo "==> [2/6] Exporting sample deck to dist/"
120: python3 release_apkg.py
121: 
122: echo "==> [3/6] Committing changes"
123: git add -A
124: CHANGED=0
125: if git diff --cached --quiet; then
126:   echo "    (nothing to commit)"
127: else
128:   git commit -m "$COMMIT_MSG"
129:   CHANGED=1
130: fi
131: 
132: if [ "$LOCAL" -eq 1 ]; then
133:   echo ""
134:   echo "Local run complete (synced, exported, committed)."
135:   exit 0
136: fi
137: 
138: if [ "$CHANGED" -eq 0 ]; then
139:   echo "    No changes detected. Nothing to push or release."
140:   exit 0
141: fi
142: 
143: echo "==> [4/6] Creating GitHub release"
144: NOTES="Automated release from commit: $COMMIT_MSG
145: 
146: Install: import the .apkg in Anki, then delete the sample cards — the note type is retained."
147: gh release create "$NEW_TAG" dist/anki-japanese-template.apkg \
148:   --title "$NEW_TAG" \
149:   --notes "$NOTES" \
150:   --latest
151: 
152: echo "==> [5/6] Pushing to origin/main"
153: git push origin main
154: # The release tag was created on the REMOTE by gh above; fetch it so local
155: # tag bookkeeping stays in sync for the next run's version bump.
156: git fetch origin "refs/tags/*:refs/tags/*" --quiet
157: 
158: echo "==> [6/6] Done"
159: echo ""
160: echo "All done: synced, exported, committed, pushed, released as $NEW_TAG"

(End of file - total 160 lines)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: read
**Status:** completed
**Title:** tests/test_compactor.py

**Input:**
```json
{
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/tests/test_compactor.py"
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/tests/test_compactor.py</path>
<type>file</type>
<content>
1: #!/usr/bin/env python3
2: """Definition Compactor regression tests.
3: 
4: Extracts the `display:none` rules from section 6b of the REAL
5: `Card 1 - Style.css` and applies them (simulated via DOM removal) to the
6: fixtures in tests/fixtures/. This catches:
7:   - CSS regressions (selector typos, accidental scoping changes)
8:   - Yomitan markup drift (fixture updates from real mined cards)
9: 
10: Run directly:  python3 tests/test_compactor.py
11: Also wired as finish.sh step 0 (auto-skipped when this file is absent).
12: 
13: Dependencies: beautifulsoup4 + soupsieve (pure Python, no Anki needed).
14: """
15: import os
16: import re
17: import sys
18: 
19: from bs4 import BeautifulSoup
20: import soupsieve as sv
21: 
22: HERE = os.path.dirname(os.path.abspath(__file__))
23: ROOT = os.path.dirname(HERE)
24: CSS = os.path.join(ROOT, "Card 1 - Style.css")
25: FIXTURES = os.path.join(HERE, "fixtures")
26: 
27: PASS = 0
28: FAIL = 0
29: 
30: 
31: def check(name, cond):
32:     global PASS, FAIL
33:     tag = "PASS" if cond else "FAIL"
34:     print(f"[{tag}] {name}")
35:     if cond:
36:         PASS += 1
37:     else:
38:         FAIL += 1
39: 
40: 
41: def load_hide_selectors():
42:     """Pull every display:none rule from the 6b compactor section."""
43:     with open(CSS, encoding="utf-8") as f:
44:         css = f.read()
45:     # Anchor on the first rule's comment, not the section banner (the banner
46:     # comment wraps the "6b." marker itself and would leak header text).
47:     start = css.index("/* --- Collapse all dictionary entries after the first --- */")
48:     end = css.index("7. CIRCULAR AUDIO BUTTON")
49:     block = css[start:end]
50:     block = re.sub(r"/\*.*?\*/", "", block, flags=re.S)
51:     selectors = []
52:     for rule in re.findall(r"([^{}]+)\{[^{}]*display:\s*none[^{}]*\}", block):
53:         sel = " ".join(rule.split())
54:         if sel and not sel.startswith("@"):
55:             for part in sel.split(","):
56:                 part = part.strip()
57:                 if part:
58:                     selectors.append(part)
59:     if not selectors:
60:         raise RuntimeError("no compactor display:none rules found in CSS")
61:     return selectors
62: 
63: 
64: def visible_text(html):
65:     """Text after applying all hide rules (hidden subtrees removed)."""
66:     soup = BeautifulSoup(html, "html.parser")
67:     for sel in load_hide_selectors():
68:         for el in sv.select(sel, soup):
69:             el.decompose()
70:     return " ".join(soup.get_text().split())
71: 
72: 
73: def fixture(name):
74:     with open(os.path.join(FIXTURES, name), encoding="utf-8") as f:
75:         return f.read().strip()
76: 
77: 
78: def main():
79:     # --- 1. Verbatim Yomitan structured entry (大辞林 + 大辞泉) ---
80:     field = f'<div class="definition-box primary-definition">{fixture("yomitan_daijirin_daijisen.html")}</div>'
81:     out = visible_text(field)
82:     check("D1 headword kept (澄ます・清ます)", "澄ます" in out and "清ます" in out)
83:     check("D1 sense ① kept", "水などを濁りのない状態にする" in out)
84:     check("D1 sense ② kept", "雑念を払って、心を落ち着かせる" in out)
85:     check("D1 sense ③+ hidden", "一つのことに注意を向ける" not in out)
86:     check("D1 sense ④-⑨ hidden", "洗い清める" not in out and "道理を明らかにする" not in out)
87:     check("D1 sub-sense ㋐ hidden", "一心に…する" not in out)
88:     check("D1 補説G hidden", "に対する他動詞" not in out)
89:     check("D1 可能形 hidden", "すませる" not in out)
90:     check("D1 accent [2] hidden", "[2]" not in out)
91:     check("D2 (大辞泉) fully hidden", "汲み置いて井戸水を" not in out)
92:     check("D2 類語 commentary hidden", "類語" not in out)
93:     check("exactly 2 senses visible overall",
94:           out.count("。") <= 10 and "①" in out and "②" in out and "③" not in out)
95: 
96:     # --- 2. Plain-gloss dictionary (JMdict-style merged list) ---
97:     field = f'<div class="definition-box primary-definition">{fixture("yomitan_plain_gloss.html")}</div>'
98:     out = visible_text(field)
99:     check("plain: gloss 1 kept", "to clear up (a liquid)" in out)
100:     check("plain: gloss 2 kept", "to concentrate (attention)" in out)
101:     check("plain: gloss 3+ hidden", "to look unconcerned" not in out and "fifth gloss" not in out)
102:     check("plain: second dictionary hidden", "Proper name entry" not in out)
103: 
104:     # --- 2b. Dictionary labels / sub-entries (会社 sample) ---
105:     field = f'<div class="definition-box primary-definition">{fixture("yomitan_dict_label.html")}</div>'
106:     out = visible_text(field)
107:     check("label: <i>(大辞林　第四版)</i> hidden", "(大辞林　第四版)" not in out)
108:     check("label: sub-entry <i>(子, ...)</i> hidden", "(子," not in out)
109:     check("label: sub-entry word 会社員 hidden", "会社員" not in out)
110:     check("label: headword kept", "会社" in out)
111:     check("label: sense kept", "営利を目的とする社団法人" in out)
112: 
113:     # --- 2c. Extended-definition FALLBACK box (when Definition is absent)
114:     #     must be compacted identically (it also carries primary-definition) ---
115:     field = f'<div class="definition-box primary-definition">{fixture("yomitan_dict_label.html")}</div>'
116:     out_fallback = visible_text(field)
117:     check("fallback: compacted like main Definition",
118:           "(大辞林　第四版)" not in out_fallback and "会社員" not in out_fallback
119:           and "営利を目的とする社団法人" in out_fallback)
120: 
121:     # --- 3. Extended definition control (must be UNTOUCHED) ---
122:     ext = fixture("extended_definition_control.html")
123:     out = visible_text(ext)
124:     check("ext: third sense still visible", "THIS THIRD SENSE MUST REMAIN VISIBLE." in out)
125:     check("ext: second dictionary still visible", "SECOND DICTIONARY MUST REMAIN VISIBLE." in out)
126: 
127:     # --- 4. Scope guard: selectors must all be prefixed .primary-definition ---
128:     leaked = [s for s in load_hide_selectors() if not s.startswith(".primary-definition")]
129:     check("all hide rules scoped to .primary-definition", not leaked)
130: 
131:     print()
132:     print(f"{PASS} passed, {FAIL} failed")
133:     return 1 if FAIL else 0
134: 
135: 
136: if __name__ == "__main__":
137:     sys.exit(main())

(End of file - total 137 lines)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: read
**Status:** completed
**Title:** tests/test_templates.py

**Input:**
```json
{
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/tests/test_templates.py"
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/tests/test_templates.py</path>
<type>file</type>
<content>
1: #!/usr/bin/env python3
2: """Template & CSS structural invariant tests.
3: 
4: Verifies the source files BEFORE they are pushed to Anki:
5:   - Front card never renders a furigana-bearing field (back-card-only rule)
6:   - Front is a pure retrieval surface (no tags/badges/metadata UI)
7:   - Listening is a hidden-by-default resolver: #listening tag or classic
8:     audio-only fields activate it; the sentence front is the fallback
9:   - Secondary back information is collapsed behind "More ▾"
10:   - Audio buttons carry aria-labels; controller is restart-only
11:   - Lightbox closes only on backdrop clicks (not on the enlarged image)
12:   - Anki template conditionals are balanced
13:   - CSS contains the accessibility/portability rules
14: 
15: Run directly:  python3 tests/test_templates.py
16: Wired into finish.sh step 0 alongside test_compactor.py.
17: 
18: Pure standard library — no dependencies.
19: """
20: import os
21: import re
22: import shutil
23: import subprocess
24: import sys
25: 
26: HERE = os.path.dirname(os.path.abspath(__file__))
27: ROOT = os.path.dirname(HERE)
28: 
29: FRONT = os.path.join(ROOT, "Card 1 - Front.template.anki")
30: BACK = os.path.join(ROOT, "Card 1 - Back.template.anki")
31: CSS = os.path.join(ROOT, "Card 1 - Style.css")
32: 
33: PASS = 0
34: FAIL = 0
35: 
36: 
37: def check(name, cond):
38:     global PASS, FAIL
39:     tag = "PASS" if cond else "FAIL"
40:     print(f"[{tag}] {name}")
41:     if cond:
42:         PASS += 1
43:     else:
44:         FAIL += 1
45: 
46: 
47: def main():
48:     front = open(FRONT, encoding="utf-8").read()
49:     back = open(BACK, encoding="utf-8").read()
50:     css = open(CSS, encoding="utf-8").read()
51: 
52:     # --- 1. Front card: furigana is back-card only ---
53:     furigana_fields = re.findall(r"\{\{[^}]*furigana[^\d}][^}]*\}\}", front)
54:     # allowed: none. Front uses plain Sentence/Expression only.
55:     check("Front renders no furigana: filter or furigana-bearing field",
56:           not furigana_fields and "Sentence (furigana)" not in front)
57:     check("Front renders the raw Sentence/Expression fields",
58:           "{{edit:Sentence}}" in front and "{{edit:Expression}}" in front)
59: 
60:     # --- 1b. Template scripts must be syntactically valid JavaScript ---
61:     # A SyntaxError in a card script kills the WHOLE script block: no
62:     # reveal, no mature mode, no listening resolver — the card hangs
63:     # hidden. Structural string checks cannot catch an unbalanced brace,
64:     # so parse every <script> body with node (skipped if node absent).
65:     node = shutil.which("node")
66:     if node:
67:         import tempfile as _tempfile
68:         for name, src in (("Front", front), ("Back", back)):
69:             bodies = re.findall(r"<script>(.*?)</script>", src, re.S)
70:             all_ok = True
71:             for body in bodies:
72:                 with _tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as tf:
73:                     tf.write(body)
74:                     tmp_path = tf.name
75:                 try:
76:                     rc = subprocess.run([node, "--check", tmp_path],
77:                                         capture_output=True, timeout=30).returncode
78:                     if rc != 0:
79:                         all_ok = False
80:                 finally:
81:                     os.unlink(tmp_path)
82:             check(f"{name}: all {len(bodies)} script block(s) parse as valid JavaScript", all_ok)
83:     else:
84:         print("[SKIP] node not found — template script syntax check skipped")
85: 
86:     # --- 2. Audio buttons: aria-labels present ---
87:     # Front is sentence-audio-only (1) + Back has word + sentence (2) = 3 total.
88:     # (Word-audio fallback was removed from the front listening mode.)
89:     buttons = re.findall(r"<button[^>]*circular-audio-btn[^>]*>", front + back)
90:     check(f"all {len(buttons)} audio buttons have aria-label",
91:           len(buttons) >= 3 and all("aria-label" in b for b in buttons))
92: 
93:     # --- 3. Audio controller: native-only (no HTML5 Audio path) ---
94:     for name, src in (("Front", front), ("Back", back)):
95:         check(f"{name}: no is-paused state remnants",
96:               "is-paused" not in src)
97:         check(f"{name}: resetAudioState defined",
98:               "window.resetAudioState = function" in src)
99:         check(f"{name}: native-only playback (no new Audio garbage-loads on AnkiDroid)",
100:               "new Audio(" not in src)
101:         check(f"{name}: delegates to Anki replay link",
102:               "nativeReplay.click()" in src)
103:         check(f"{name}: replay link resolved via wrapper scope (not nested in button)",
104:               "closest('.audio-btn-wrapper')" in src)
105:         check(f"{name}: re-tap debounce (native audio can't be stopped)",
106:               "window.currentActiveBtn === btn" in src)
107:         # restart-only: every click path goes through resetAudioState first
108:         check(f"{name}: playCircularAudio starts with resetAudioState",
109:               re.search(r"window\.playCircularAudio = function\(btn\) \{\s*(/\*.*?\*/\s*)*if \(window\.currentActiveBtn === btn\) return;\s*window\.resetAudioState\(\);", src, re.S) is not None)
110: 
111:     # --- 3b. Audio markup: valid + clickable on AnkiDroid ---
112:     for name, src in (("Front", front), ("Back", back)):
113:         check(f"{name}: replay source lives OUTSIDE the button (sibling span)",
114:               re.search(r"</button>\s*<span class=\"raw-audio-source\"", src) is not None)
115:         check(f"{name}: no display:none audio source (breaks .click() playback)",
116:               "raw-audio-source\" style=\"display:none" not in src)
117:         check(f"{name}: no div-inside-button (invalid HTML, breaks AnkiDroid taps)",
118:               '<div class="audio-btn-content">' not in src)
119:     check("CSS: raw-audio-source visually hidden but present (no display:none)",
120:           re.search(r"\.raw-audio-source\s*\{[^}]*position:\s*absolute", css) is not None
121:           and ".raw-audio-source" in css)
122: 
123:     # --- 2c. Cloze fallback: bold-less Sentence rebuilt from cloze trio ---
124:     check("Front: hidden cloze probe with plain prefix/body/suffix fields",
125:           'class="cloze-probe"' in front
126:           and "{{cloze-prefix}}" in front and "{{cloze-body}}" in front
127:           and "{{cloze-suffix}}" in front)
128:     check("Front: probe uses plain fields (no edit: filter, stays furigana-free)",
129:           "edit:cloze" not in front)
130:     check("Front: reconstruction only fires when sentence lacks bold",
131:           "querySelector('b, strong')" in front)
132:     check("Front: reconstruction requires the complete trio (no partial rebuild)",
133:           "clozePre && clozeMid && clozeSuf" in front)
134:     check("Front: rebuilt term uses <b> (inherits sentence-display styling)",
135:           "createElement('b')" in front)
136: 
137:     # --- 4. Lightbox: backdrop-only close ---
138:     check("lightbox closes only on backdrop click (e.target === overlay)",
139:           "if (e.target === overlay) closeOverlay()" in back)
140:     check("lightbox overlay has dialog semantics",
141:           "setAttribute('role', 'dialog')" in back and "setAttribute('aria-modal', 'true')" in back)
142:     check("lightbox clone preserves alt text", "img.alt" in back)
143: 
144:     # --- 5. Anki conditionals balanced ({{#field}} and {{^field}} both open) ---
145:     for name, src in (("Front", front), ("Back", back)):
146:         opens = len(re.findall(r"\{\{[#^][A-Za-z]", src))
147:         closes = len(re.findall(r"\{\{/[A-Za-z]", src))
148:         check(f"{name}: balanced field conditionals ({opens} open / {closes} close)",
149:               opens == closes)
150: 
151:     # --- 6. CSS invariants ---
152:     check("CSS: :focus-visible keyboard indicator present",
153:           ":focus-visible" in css)
154:     check("CSS: prefers-reduced-motion present",
155:           "prefers-reduced-motion: reduce" in css)
156:     check("CSS: content-driven card sizing (no forced viewport fill)",
157:           "min-height: 100vh" not in css and "min-height: 100dvh" not in css
158:           and "container-type: inline-size" in css)
159:     check("CSS: container-query media fallback for the context grid",
160:           re.search(r"@media \(min-width: 768px\)[\s\S]{0,200}\.context-grid", css) is not None)
161: 
162:     # --- 6b. Minimal redesign: noise is gone, hierarchy is present ---
163:     check("Back: no sticky tags bar (tags are behavioral metadata)",
164:           "tags-container" not in back and "tags-list" not in back
165:           and "tag-pill" not in back)
166:     check("Back: no frequency badge machinery (noise without retrieval value)",
167:           "frequency-badge" not in back and "renderFrequencyIndicator" not in back)
168:     check("CSS: no frequency badge styling remains",
169:           "frequency-badge" not in css and "--freq-" not in css)
170:     check("Back: secondary info is collapsed behind More by default",
171:           'class="more-section" hidden' in back
172:           and "more-toggle" in back)
173:     check("Back: More toggle has aria state + one-way reveal",
174:           'aria-expanded="false"' in back
175:           and "toggleMore" in back)
176:     check("Back: retrieval-state label present but hidden by default",
177:           'class="retrieval-state" data-state="context" hidden' in back)
178:     check("Back: state label reads the front decision store",
179:           "__ajtFrontState" in back)
180:     check("Front: front-state store written for the back label",
181:           "window.__ajtFrontState" in front)
182:     check("Back: keyboard F toggles full-card furigana (back only)",
183:           "furigana-mode" in back and "'f'" in back)
184:     check("Back: keyboard T reveals the translation",
185:           "'t'" in back and "translation-box" in back)
186:     check("CSS: full-card furigana mode rule exists",
187:           ".card-wrapper.furigana-mode ruby rt" in css)
188:     check("Front: listening resolver driven by #listening tag probe",
189:           'class="tags-probe"' in front and "hasListeningTag" in front)
190:     check("Front: listening resolver also accepts classic audio-only fields",
191:           "probe-def" in front and "probe-ext" in front and "probe-freq" in front)
192: 
193:     # --- 6c. Listening mode invariants (hidden-by-default resolver) ---
194:     check("Front: listening markup gated behind Sentence Audio only",
195:           re.search(r"\{\{#Sentence Audio\}\}\s*<div class=\"listening-view\">", front) is not None)
196:     check("Front: listening resolver runs synchronously before the reveal",
197:           "LISTENING RESOLVER" in front)
198:     check("Front: sentence front is the universal fallback (renders in the audio branch too)",
199:           re.search(r"\{\{#Sentence Audio\}\}\s*<div class=\"sentence-display\">", front) is not None)
200:     check("CSS: listening-view inert until .listening-mode activates it",
201:           ".card-wrapper.listening-mode .listening-view" in css)
202:     check("CSS: listening mode hides the sentence/word fronts",
203:           ".card-wrapper.listening-mode .sentence-display" in css)
204:     check("Front: active listening removes the sentence display",
205:           "sd.remove()" in front)
206: 
207:     # --- 7. Font sizing source-of-truth ---
208:     check("Back: no JS font-scaler overriding CSS (inline fontSize ban)",
209:           "el.style.fontSize" not in back and "autoScaleBackSentence" not in back)
210:     check("CSS: .sentence-japanese clamp() is the sizing authority",
211:           re.search(r"\.sentence-japanese\s*\{[^}]*font-size:\s*clamp\(", css) is not None)
212: 
213:     # --- 8. (removed) Frequency visualizer retired with the minimal redesign ---
214: 
215:     # --- 8b. Mature Word Mode invariants (interval-gated front) ---
216:     check("Front: LONG_INTERVAL_DAYS threshold constant defined",
217:           re.search(r"const\s+LONG_INTERVAL_DAYS\s*=\s*365", front) is not None
218:           and "interval >= LONG_INTERVAL_DAYS" in front)
219:     check("Front: threshold not hard-coded elsewhere (single const definition)",
220:           len(re.findall(r"LONG_INTERVAL_DAYS\s*=\s*365", front)) == 1
221:           and len(re.findall(r">=\s*365", front)) == 0)
222:     check("Front: word probe div present with Expression",
223:           re.search(r'class="front-word-display">\s*\{\{edit:Expression\}\}', front) is not None)
224:     check("Front: desktop flow guiCurrentCard -> cardsInfo -> interval",
225:           "guiCurrentCard" in front and "cardsInfo" in front
226:           and re.search(r"cardsInfo.*?interval", front, re.S) is not None)
227:     check("Front: previewer fallback via content search (findCards)",
228:           "findCards" in front and "content search" in front)
229:     check("Front: no nonexistent Anki-Connect actions",
230:           "getCardsInfo" not in front)
231:     check("Front: no card-id-from-URL guess (no URLSearchParams)",
232:           "URLSearchParams" not in front)
233:     check("Front: AnkiDroid JS API with verified contract",
234:           "ankiGetCardInterval" in front and 'new AnkiDroidJS(' in front)
235:     check("Front: supports constructor + direct bridge APIs",
236:           "apiKind" in front and "'constructor'" in front and "'direct'" in front)
237:     check("Front: never invokes new-reviewer stub bridge (signal:jsapi guard)",
238:           "signal" in front and "jsapi" in front
239:           and "ankiDroid-stub" in front)
240:     check("Front: accepts AnkiDroid {success,value} shape (official wiki contract)",
241:           "parseDroidInterval" in front
242:           and "hasOwnProperty" in front
243:           and "'value'" in front)
244:     check("Front: rejects {success:false} failure defaults (number => -1)",
245:           "success === false" in front)
246:     check("Front: parses numeric strings + JSON-encoded responses",
247:           "JSON.parse" in front and "Number.isFinite" in front)
248:     check("Front: bridge call has its own timeout (never hangs the card)",
249:           "withBridgeTimeout" in front)
250:     check("Front: never fetches AnkiConnect from mobile WebViews (downloadfile.bin toast)",
251:           "isMobile" in front and "no-bridge-mobile" in front
252:           and "127.0.0.1" in front)
253:     check("Front: one deferred bridge retry on mobile while still hidden",
254:           "bridgeAvailable" in front)
255:     check("Front: polls for late-injected bridge with a firm deadline",
256:           "waitForBridge" in front)
257:     check("Front: bridge poll capped short (fast preview fallback)",
258:           "waitForBridge(700" in front)
259:     check("Front: platform-exclusive retrieval (mobile bridge vs desktop AnkiConnect)",
260:           "Platform-exclusive retrieval" in front and "DESKTOP-ONLY" in front)
261:     check("Front: retrieval latency is measured and logged",
262:           "performance.now" in front and "elapsedMs" in front
263:           and "[Mature Word Mode] source=" in front)
264:     check("Front: safety reveal cap bounds worst-case hidden time",
265:           "setTimeout(reveal, 1200)" in front)
266:     check("Front: AnkiConnect calls fail fast when Anki is wedged (safe sentence fallback)",
267:           "AnkiConnect timeout" in front and "')), 500)" in front)
268:     check("Front: temporary toast diagnostic removed (no TEMP-DIAG remnants)",
269:           "TEMP-DIAG" not in front and "ankiShowToast" not in front)
270:     check("Front: on-card debug diagnostic present (mwm-debug)",
271:           "DEBUG_MATURE_MODE" in front and "mwm-debug" in front
272:           and "Mature mode: " in front)
273:     check("Front: skips ALL retrieval on listening cards (no needless JS-API calls)",
274:           "isListening" in front)
275:     check("Front: anti-flash visibility gate present",
276:           'style="visibility: hidden;"' in front
277:           and "container.style.visibility = 'visible'" in front)
278:     check("Front: word-mode class applied to card wrapper",
279:           "wrapper.classList.toggle('word-mode'" in front)
280:     check("Front: retrieval failure falls back to sentence (try/catch + typed interval check)",
281:           "catch" in front and "typeof interval === 'number'" in front)
282:     check("CSS: word-mode display rules present",
283:           ".card-wrapper.word-mode .sentence-display" in css
284:           and ".card-wrapper.word-mode .front-word-display" in css)
285:     check("CSS: word mode leaves listening view untouched",
286:           ".listening-view" not in css.split("5b. MATURE-CARD WORD MODE")[1].split("6. BACK CARD")[0]
287:           if "5b. MATURE-CARD WORD MODE" in css else False)
288:     check("Front: no \"note:\" search clause ({{Type}} is scheduling type, not model)",
289:           "NOTE_TYPE" not in front
290:           and re.search(r"findCards[^\n]*note:", front) is None
291:           and 'escQuery(NOTE_TYPE)' not in front)
292: 
293:     # --- 10. Empty-field collapse (QUALITY.md: no UI survives an empty field) ---
294:     # 10a. Static proof over the raw templates (comments/scripts stripped):
295:     # every rendered field lives inside an Anki conditional, except the
296:     # documented allowlist (attribute / hidden probe / gated probe).
297:     TOKEN = re.compile(r"\{\{\s*([#^/]?)\s*([^}]*?)\s*\}\}")
298:     ALLOW_BARE = {
299:         ("Front", "cloze-prefix"), ("Front", "cloze-body"), ("Front", "cloze-suffix"),  # hidden probe
300:         ("Front", "Expression"),  # front-word-display: display:none default, word-mode gate only (§8b)
301:     }
302:     bare = []
303:     for name, src in (("Front", front), ("Back", back)):
304:         clean = re.sub(r"<!--.*?-->", "", src, flags=re.S)
305:         clean = re.sub(r"<script.*?</script>", "", clean, flags=re.S)
306:         stack = []
307:         for m in TOKEN.finditer(clean):
308:             sig, body = m.group(1), m.group(2).strip()
309:             if sig in ("#", "^"):
310:                 stack.append(body)
311:             elif sig == "/":
312:                 if stack:
313:                     stack.pop()
314:             elif body:
315:                 field = body.split(":")[-1].strip()
316:                 if not stack and (name, field) not in ALLOW_BARE:
317:                     bare.append(f"{name}:{{{{{body}}}}}")
318:     check("every rendered field is conditional (or allowlisted)" + (f" — bare: {bare}" if bare else ""),
319:           not bare)
320: 
321:     # 10b. Unconditional shells collapse when all conditional children absent.
322:     check("CSS: empty .audio-row collapses (no button => gone)",
323:           re.search(r"\.audio-row:not\(:has\(\.circular-audio-btn\)\)\s*\{\s*display:\s*none", css) is not None)
324:     check("Back: More section + toggle self-remove when secondary content is absent",
325:           "btn.remove()" in back and "section.remove()" in back)
326: 
327:     # 10c. Degenerate content removes itself instead of leaving chrome behind.
328:     check("Back: blank definition box is removed (no bordered void)",
329:           "box.remove()" in back)
330:     check("Front: blank sentence block is removed after cloze fixup",
331:           "sd.remove()" in front)
332: 
333:     # --- 9. Sync tooling invariants ---
334:     sync = open(os.path.join(ROOT, "sync_to_anki.py"), encoding="utf-8").read()
335:     check("sync_to_anki.py: zero third-party imports (standard lib only)",
336:           "import requests" not in sync and "import urllib.request" in sync)
337:     check("sync_to_anki.py: microsecond backup timestamps",
338:           "%H%M%S-%f" in sync)
339:     finish = open(os.path.join(ROOT, "finish.sh"), encoding="utf-8").read()
340:     check("finish.sh: no-op run cannot publish a release",
341:           "Nothing to push or release" in finish)
342: 
343:     print()
344:     print(f"{PASS} passed, {FAIL} failed")
345:     return 1 if FAIL else 0
346: 
347: 
348: if __name__ == "__main__":
349:     sys.exit(main())

(End of file - total 349 lines)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: read
**Status:** completed
**Title:** tests/test_front_modes.py

**Input:**
```json
{
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/tests/test_front_modes.py"
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/tests/test_front_modes.py</path>
<type>file</type>
<content>
1: #!/usr/bin/env python3
2: """Front-mode resolver behavioral tests (listening semantics).
3: 
4: Extracts the LISTENING RESOLVER block verbatim from the real
5: `Card 1 - Front.template.anki` and runs it in headless Chrome against
6: six front-state harnesses, asserting the resolved mode:
7: 
8:   1. classic audio-only (no Definition/Extended/Frequency + audio)
9:      -> listening front: sentence removed, listening-view visible
10:   2. #listening tag + glosses -> listening front (deliberate exercise)
11:   3. sentence audio + glosses, no tag -> sentence front (regular card)
12:   4. no audio at all -> sentence front
13:   5. Frequency legacy probe -> sentence front (never the audio button)
14:   6. tag but no Sentence Audio -> sentence front (markup is gated on
15:      Sentence Audio existing)
16: 
17: Run directly:  python3 tests/test_front_modes.py
18: Wired into ./verify alongside the other suites. Skipped gracefully
19: without Chrome.
20: 
21: Dependencies: headless Chrome only (same as test_layout.py).
22: """
23: import json
24: import os
25: import re
26: import shutil
27: import subprocess
28: import sys
29: import tempfile
30: 
31: HERE = os.path.dirname(os.path.abspath(__file__))
32: ROOT = os.path.dirname(HERE)
33: FRONT = os.path.join(ROOT, "Card 1 - Front.template.anki")
34: CHROME = shutil.which("google-chrome-stable") or shutil.which("chromium")
35: 
36: PASS = 0
37: FAIL = 0
38: 
39: 
40: def check(name, cond, detail=""):
41:     global PASS, FAIL
42:     tag = "PASS" if cond else "FAIL"
43:     print(f"[{tag}] {name}" + (f" ({detail})" if detail and not cond else ""))
44:     if cond:
45:         PASS += 1
46:     else:
47:         FAIL += 1
48: 
49: 
50: def load_resolver():
51:     """Extract the resolver block verbatim from the real front template."""
52:     with open(FRONT, encoding="utf-8") as f:
53:         front = f.read()
54:     m = re.search(
55:         r"/\* --- LISTENING RESOLVER.*?"
56:         r"console\.warn\('\[Listening Resolver\]', listenErr\);\s*\}\n",
57:         front, re.S)
58:     if not m:
59:         raise RuntimeError("listening resolver block not found in front template")
60:     return m.group(0)
61: 
62: 
63: # (name, tags-probe text or None, probe classes, has sentence, has audio)
64: CASES = [
65:     ("classic audio-only", "", [], True, True),
66:     ("#listening tag with glosses", "je listening", ["def"], True, True),
67:     ("audio with glosses, no tag", "je", ["def"], True, True),
68:     ("no audio", "", [], True, False),
69:     ("frequency legacy", "", ["freq"], True, True),
70:     ("tag but no sentence audio", "listening", ["def"], True, False),
71: ]
72: 
73: 
74: def build_html(resolver, tags, probes, sentence, audio):
75:     tags_html = f'<div class="tags-probe" hidden>{tags}</div>' if tags is not None else ""
76:     probe_html = "".join(f'<span class="probe-{p}" hidden></span>' for p in probes)
77:     sent_html = f'<div class="sentence-display">{sentence}</div>' if sentence else ""
78:     audio_html = (
79:         '<div class="listening-view">'
80:         '<button type="button" class="circular-audio-btn large-audio-btn">文</button>'
81:         "</div>"
82:     ) if audio else ""
83:     # Minimal stand-ins for the probes' surrounding context. The real
84:     # template defines container/wrapper before the resolver runs.
85:     return f"""<!doctype html><html><head><meta charset="utf-8">
86: <script>/* prevent Anki-style fetches from mattering */</script>
87: <style>.front-word-display{{display:none}}</style></head><body>
88: <div class="card"><div class="card-wrapper"><div class="card-container">
89: <div class="front-word-display">不公平</div>
90: {tags_html}{probe_html}{sent_html}{audio_html}
91: </div></div></div>
92: <script>
93: var report = {{}};
94: try {{
95:   var container = document.querySelector('.card-container');
96:   var wrapper = document.querySelector('.card-wrapper');
97: {resolver}
98: report.listening = isListening;
99: report.cls = wrapper.className;
100: report.sentences = container.querySelectorAll('.sentence-display').length;
101: var lv = container.querySelector('.listening-view');
102: report.viewVisible = !!lv && getComputedStyle(lv).display !== 'none';
103: }} catch(e) {{ report.err = String(e && e.stack || e); }}
104: document.title = JSON.stringify(report);
105: </script></body></html>"""
106: 
107: 
108: def render(html):
109:     with tempfile.TemporaryDirectory() as td:
110:         path = os.path.join(td, "front.html")
111:         with open(path, "w", encoding="utf-8") as f:
112:             f.write(html)
113:         try:
114:             out = subprocess.run(
115:                 [CHROME, "--headless=new", "--disable-gpu",
116:                  "--no-sandbox", "--hide-scrollbars",
117:                  "--window-size=1440,900",
118:                  "--virtual-time-budget=1500",
119:                  "--dump-dom", f"file://{path}"],
120:                 capture_output=True, text=True, timeout=60,
121:             ).stdout
122:         except subprocess.TimeoutExpired:
123:             return None
124:     m = re.search(r"<title>(.*?)</title>", out, re.S)
125:     if not m:
126:         return None
127:     try:
128:         return json.loads(m.group(1))
129:     except json.JSONDecodeError:
130:         return None
131: 
132: 
133: def main():
134:     if not CHROME:
135:         print("[SKIP] no headless Chrome found — front-mode checks skipped")
136:         return 0
137:     resolver = load_resolver()
138: 
139:     for name, tags, probes, sentence, audio in CASES:
140:         r = render(build_html(resolver, tags, probes,
141:                                "世の中って<b>不公平</b>よね", audio))
142:         check(f"{name}: probe returned", r is not None)
143:         if not r:
144:             continue
145:         if "err" in r:
146:             check(f"{name}: resolver ran without errors", False, r["err"])
147:             continue
148:         check(f"{name}: resolver ran without errors", True)
149:         if audio and "listening" in tags:
150:             # deliberate exercise -> listening front
151:             check(f"{name}: listening front active (view visible, sentence gone)",
152:                   r["listening"] is True and r["viewVisible"] and r["sentences"] == 0,
153:                   json.dumps(r))
154:         elif audio and not probes:
155:             # classic audio-only -> listening front
156:             check(f"{name}: listening front active (view visible, sentence gone)",
157:                   r["listening"] is True and r["viewVisible"] and r["sentences"] == 0,
158:                   json.dumps(r))
159:         else:
160:             # every other shape -> sentence front, listening inert
161:             check(f"{name}: sentence front (listening inert)",
162:                   r["listening"] is False and r["sentences"] >= 1,
163:                   json.dumps(r))
164: 
165:     print()
166:     print(f"{PASS} passed, {FAIL} failed")
167:     return 1 if FAIL else 0
168: 
169: 
170: if __name__ == "__main__":
171:     sys.exit(main())

(End of file - total 171 lines)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: read
**Status:** completed
**Title:** tests/test_layout.py

**Input:**
```json
{
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/tests/test_layout.py",
  "limit": 200
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/tests/test_layout.py</path>
<type>file</type>
<content>
1: #!/usr/bin/env python3
2: """Headless layout verification for the density pass.
3: 
4: Renders the REAL stylesheet plus template-shaped HTML in Chrome headless
5: (google-chrome-stable is available on this machine) and asserts layout
6: invariants that pure text tests cannot catch:
7: 
8:   - card height is content-driven (back card < 90% of viewport height
9:     on a rich desktop card, i.e. no viewport fill)
10:   - no horizontal overflow / clipping
11:   - furigana (rt) never overlaps the line above it
12:   - hierarchy: headword font > sentence font > definition font > notes
13:   - truncator: a long definition clamps at 3 lines until expanded
14:   - listening front keeps the audio button a comfortable target
15:   - definition expand still works (JS one-way expand)
16: 
17: Usage: python3 tests/test_layout.py
18: Requires: google-chrome-stable on PATH. Skipped gracefully if absent
19:         (finish.sh runs it as part of step 0 when present).
20: """
21: import json
22: import os
23: import shutil
24: import subprocess
25: import sys
26: import tempfile
27: 
28: HERE = os.path.dirname(os.path.abspath(__file__))
29: ROOT = os.path.dirname(HERE)
30: CSS = os.path.join(ROOT, "Card 1 - Style.css")
31: CHROME = shutil.which("google-chrome-stable") or shutil.which("chromium")
32: 
33: PASS = 0
34: FAIL = 0
35: 
36: 
37: def check(name, cond, detail=""):
38:     global PASS, FAIL
39:     tag = "PASS" if cond else "FAIL"
40:     print(f"[{tag}] {name}" + (f" ({detail})" if detail and not cond else ""))
41:     if cond:
42:         PASS += 1
43:     else:
44:         FAIL += 1
45: 
46: 
47: # ---------------------------------------------------------------- HTML fixture
48: # Back card with every block populated: furigana headword, pitch, audio,
49: # long definition, furigana sentence, picture, More section (translation,
50: # extended definition, notes), source footer. New minimal hierarchy:
51: # word → meaning → context (sentence + picture) → More ▾.
52: BACK_CARD = """<!doctype html><html><head><meta charset="utf-8">
53: <style>
54: html,body{margin:0;padding:0;}
55: /* minimal Anki stand-ins: replay link + fonts so JS runs like in Anki */
56: </style>
57: <style>
58: __CSS__
59: </style></head><body>
60: <div class="card back-card">
61: <div class="card-wrapper back-card">
62:   <div class="card-container">
63:     <div class="retrieval-state" data-state="context"><span class="retrieval-state-label">Context</span></div>
64:     <div class="word-display" id="word"><ruby>澄<rt>す</rt></ruby>ます</div>
65:     <div class="pitch-quiet">[0]</div>
66:     <div class="definition-box primary-definition" id="def">
67:       <div class="yomitan-glossary"><ol>
68:         <li><div data-sc-name="語義G">水などを濁りのない状態にする。とても長い定義のテキストで、三行を超えることを保証するためにさらに文字を追加している。三行目に入ってもまだ続くほど十分に長い定義であることを確認するための文です。全幅レイアウトでも確実に三行を超えるように、さらに追加の検証用テキストをここに置く。この文が折り返して四行目に達すれば、切り詰め機能が正しく発動するはずである。</div>
69:         <div data-sc-name="語義G">雑念を払って、心を落ち着かせる。二番目の語義。</div>
70:         <div data-sc-name="語義G">一つのことに注意を向ける。三番目の語義（隠れるはず）。</div>
71:         <div data-sc-name="補説G">supplementary (hidden)</div></li>
72:       </ol></div>
73:       <!-- Font-independent overflow guarantee: CI runners have Chrome but
74:            no CJK fonts, so the Japanese text above renders with fallback
75:            tofu metrics and may fit within the 3-line cap. The fixed-height
76:            spacer makes scrollHeight > clientHeight true in EVERY
77:            environment, so the truncator checks never depend on font
78:            availability. -->
79:       <div style="height:140px"></div>
80:     </div>
81:     <div class="audio-row">
82:       <span class="audio-btn-wrapper">
83:         <button type="button" class="circular-audio-btn small-audio-btn"><span class="audio-btn-content"><span class="audio-btn-label">言葉</span></span></button>
84:         <span class="raw-audio-source"><a class="replay-button" href="#">replay</a></span>
85:       </span>
86:       <span class="audio-btn-wrapper">
87:         <button type="button" class="circular-audio-btn small-audio-btn"><span class="audio-btn-content"><span class="audio-btn-label">文</span></span></button>
88:         <span class="raw-audio-source"><a class="replay-button" href="#">replay</a></span>
89:       </span>
90:     </div>
91:     <div class="context-grid">
92:       <div class="context-main">
93:         <div class="sentence-japanese" id="sentence"><ruby>心<rt>こころ</rt></ruby>を<ruby>澄<rt>す</rt></ruby>ませて、<b>音楽</b>を聴く。長い文章が二行に折り返される場合の検証も兼ねている。</div>
94:       </div>
95:       <div class="context-picture">
96:         <div class="picture-container"><img id="pic" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='800' height='600'%3E%3Crect width='100%25' height='100%25' fill='%2338bdf8'/%3E%3C/svg%3E"></div>
97:       </div>
98:     </div>
99:     <div class="more-section" hidden>
100:       <div class="translation-box"><div class="translation-hint">Translation</div>
101:         <div class="translation-text">To clear one's mind and listen to music.</div></div>
102:       <div class="html-content secondary-block">Additional context paragraph.</div>
103:       <div class="html-content secondary-block">漢字のメモ: 澗 — radical 水.</div>
104:       <div class="html-content secondary-block extended-full">Full extended definition text that stays untruncated.</div>
105:     </div>
106:     <button type="button" class="more-toggle" aria-expanded="false">More <span class="more-caret">▾</span></button>
107:     <div class="source-footer">SOURCE — some novel</div>
108:   </div>
109: </div>
110: </div>
111: <script>
112: window.expandDefinition = function(element) {
113:   if (element.classList.contains('is-expanded')) return;
114:   element.classList.add('is-expanded');
115: };
116: window.initDefinitionTruncation = function() {
117:   document.querySelectorAll('.primary-definition').forEach(function(box) {
118:     const overflows = box.scrollHeight > box.clientHeight + 2;
119:     box.classList.toggle('is-truncated', overflows);
120:   });
121: };
122: window.initDefinitionTruncation();
123: </script>
124: </body></html>"""
125: 
126: FRONT_SENTENCE = """<!doctype html><html><head><meta charset="utf-8">
127: <style>__CSS__</style></head><body>
128: <div class="card"><div class="card-wrapper">
129:   <div class="card-container">
130:     <div class="sentence-display" id="sent">彼は<b>約束</b>を<ruby>守<rt>まも</rt></ruby>らなかった。</div>
131:   </div>
132: </div></div>
133: </body></html>"""
134: 
135: FRONT_LISTENING = """<!doctype html><html><head><meta charset="utf-8">
136: <style>__CSS__</style></head><body>
137: <div class="card"><div class="card-wrapper listening-mode">
138:   <div class="card-container">
139:     <div class="listening-view" id="listening">
140:       <div class="audio-btn-wrapper">
141:         <button type="button" class="circular-audio-btn large-audio-btn"><span class="audio-btn-content"><span class="audio-btn-label">文</span></span></button>
142:       </div>
143:     </div>
144:   </div>
145: </div></div>
146: </body></html>"""
147: 
148: 
149: # ---------------------------------------------------------------- probing JS
150: PROBE = """(() => {
151:   const r = {};
152:   const wrapper = document.querySelector('.card-wrapper');
153:   const card = document.querySelector('.card');
154:   r.wrapperH = wrapper.getBoundingClientRect().height;
155:   r.viewportH = window.innerHeight;
156:   r.docScrollW = document.documentElement.scrollWidth;
157:   r.docClientW = document.documentElement.clientWidth;
158:   // overflow-x anywhere?
159:   r.hOverflow = r.docScrollW > r.docClientW + 1;
160:   // furigana overlap: rt boxes vs previous line — collect any rt whose
161:   // top is above the previous sibling line's bottom is hard generically;
162:   // instead verify every rt's top >= its ruby's parent's top (rt never
163:   // escapes the container) AND that rt boxes do not overlap the element
164:   // above: compare first rt top vs sentence/word container top.
165:   const word = document.querySelector('.word-display');
166:   if (word) {
167:     const rb = word.getBoundingClientRect();
168:     const rt = word.querySelector('rt');
169:     r.wordFont = parseFloat(getComputedStyle(word).fontSize);
170:     if (rt) { const rtb = rt.getBoundingClientRect();
171:       r.wordRtInside = rtb.top >= rb.top - 0.5 && rtb.bottom <= rb.bottom + 0.5; }
172:   }
173:   const sent = document.querySelector('#sentence, .sentence-japanese');
174:   if (sent) {
175:     r.sentFont = parseFloat(getComputedStyle(sent).fontSize);
176:     const rt = sent.querySelector('rt');
177:     const sb = sent.getBoundingClientRect();
178:     if (rt) { const rtb = rt.getBoundingClientRect();
179:       r.sentRtInside = rtb.top >= sb.top - 0.5; }
180:     r.sentH = sb.height;
181:   }
182:     const def = document.querySelector('#def');
183:   if (def) {
184:     r.defFont = parseFloat(getComputedStyle(def).fontSize);
185:     const cs = getComputedStyle(def);
186:     r.defLineH = parseFloat(cs.lineHeight) || parseFloat(cs.fontSize) * 1.5;
187:     r.defPadTop = parseFloat(cs.paddingTop) || 0;
188:     r.defClampedH = def.getBoundingClientRect().height;
189:     r.defScrollH = def.scrollHeight;
190:     r.defTruncated = def.classList.contains('is-truncated');
191:     // expand and re-measure
192:     window.expandDefinition(def);
193:     r.defExpandedH = def.getBoundingClientRect().height;
194:   }
195:   const notes = document.querySelector('.secondary-block');
196:   if (notes && def) {
197:     r.notesFont = parseFloat(getComputedStyle(notes).fontSize);
198:     r.hierarchy = r.wordFont > r.sentFont && r.sentFont > r.defFont && r.defFont >= r.notesFont;
199:   }
200:   const pic = document.querySelector('#pic');

(Showing lines 1-200 of 345. Use offset=201 to continue.)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: read
**Status:** completed
**Title:** tests/test_layout.py

**Input:**
```json
{
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/tests/test_layout.py",
  "offset": 201
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/tests/test_layout.py</path>
<type>file</type>
<content>
201:   if (pic) { const pb = pic.getBoundingClientRect(); r.picH = pb.height; r.picW = pb.width; }
202:   const listening = document.querySelector('#listening');
203:   if (listening) {
204:     const lb = listening.getBoundingClientRect();
205:     const btn = listening.querySelector('.circular-audio-btn');
206:     r.listenH = lb.height;
207:     r.listenBtn = btn.getBoundingClientRect().height;
208:   }
209:   // Context grid: picture beside the sentence on wide screens.
210:   const ctxPic = document.querySelector('.context-picture');
211:   const ctxMain = document.querySelector('.context-main');
212:   if (ctxPic && ctxMain && innerWidth >= 768) {
213:     r.twoCol = ctxPic.getBoundingClientRect().left > ctxMain.getBoundingClientRect().right;
214:     r.sideW = ctxPic.getBoundingClientRect().width;
215:     r.mainW = ctxMain.getBoundingClientRect().width;
216:   }
217:   // Secondary info collapsed by default; More toggle present.
218:   const more = document.querySelector('.more-section');
219:   const moreBtn = document.querySelector('.more-toggle');
220:   if (more && moreBtn) {
221:     r.moreCollapsed = more.hidden === true
222:       && moreBtn.getAttribute('aria-expanded') === 'false';
223:     r.moreBelowFold = more.getBoundingClientRect().height;
224:   }
225:   const footer = document.querySelector('.source-footer');
226:   if (footer && wrapper) {
227:     r.footerInside = footer.getBoundingClientRect().bottom <= wrapper.getBoundingClientRect().bottom + 1;
228:   }
229:   return r;
230: })()"""
231: 
232: 
233: def render(html, width, height):
234:     """Chrome headless screenshot + JS probe via --dump-dom is awkward;
235:     use the DevTools-free trick: virtual-time + console.log of the probe,
236:     captured from chrome's stderr? No — instead write the probe result
237:     into the DOM title and read it from the dumped DOM."""
238:     probe_html = html.replace(
239:         "</body>",
240:         f"<script>document.title = JSON.stringify({PROBE});</script></body>",
241:     )
242:     with tempfile.TemporaryDirectory() as td:
243:         path = os.path.join(td, "card.html")
244:         with open(path, "w", encoding="utf-8") as f:
245:             f.write(probe_html)
246:         try:
247:             out = subprocess.run(
248:                 [CHROME, "--headless=new", "--disable-gpu",
249:                  "--no-sandbox", "--hide-scrollbars",
250:                  f"--window-size={width},{height}",
251:                  "--virtual-time-budget=2000",
252:                  "--dump-dom", f"file://{path}"],
253:                 capture_output=True, text=True, timeout=60,
254:             ).stdout
255:         except subprocess.TimeoutExpired:
256:             return None
257:     import re
258:     m = re.search(r"<title>(.*?)</title>", out, re.S)
259:     if not m:
260:         return None
261:     try:
262:         return json.loads(m.group(1))
263:     except json.JSONDecodeError:
264:         return None
265: 
266: 
267: def main():
268:     if not CHROME:
269:         print("[SKIP] no headless Chrome found — layout checks skipped")
270:         return 0
271:     css = open(CSS, encoding="utf-8").read()
272: 
273:     # ---- Desktop back card (1440x900, rich card) ----
274:     back = render(BACK_CARD.replace("__CSS__", css), 1440, 900)
275:     check("desktop back: probe returned", back is not None)
276:     if back:
277:         check("desktop back: content-driven card (rich card < 100% viewport)",
278:               back["wrapperH"] < back["viewportH"],
279:               f"wrapper={back['wrapperH']:.0f} viewport={back['viewportH']}")
280:         check("desktop back: no horizontal overflow", not back["hOverflow"])
281:         check("desktop back: word furigana stays inside its line box",
282:               back.get("wordRtInside", True))
283:         check("desktop back: sentence furigana stays inside its block",
284:               back.get("sentRtInside", True))
285:         check("desktop back: hierarchy word > sentence > definition > notes",
286:               back.get("hierarchy", False),
287:               f"word={back.get('wordFont')} sent={back.get('sentFont')} "
288:               f"def={back.get('defFont')} notes={back.get('notesFont')}")
289:         check("desktop back: long definition IS truncated by JS",
290:               back.get("defTruncated", False))
291:         check("desktop back: clamped height ≈ pad + 3 line-heights",
292:               abs(back["defClampedH"] - (back["defPadTop"] + 3 * back["defLineH"])) <= 8,
293:               f"clamped={back['defClampedH']:.0f} expected={back['defPadTop'] + 3*back['defLineH']:.0f}")
294:         check("desktop back: expand grows the definition (one-way)",
295:               back.get("defExpandedH", 0) > back.get("defClampedH", 0) + 4)
296:         check("desktop back: image height capped (<= 40vh)",
297:               back.get("picH", 0) <= 0.40 * back["viewportH"] + 2,
298:               f"picH={back.get('picH', 0):.0f}")
299:         check("desktop back: context grid engaged (picture beside sentence)",
300:               back.get("twoCol", False),
301:               f"main={back.get('mainW', 0):.0f} pic-col={back.get('sideW', 0):.0f}")
302:         check("desktop back: picture column is the minority width",
303:               back.get("sideW", 1) < back.get("mainW", 0))
304:         check("desktop back: secondary info collapsed behind More by default",
305:               back.get("moreCollapsed", False))
306:         check("desktop back: footer inside the card wrapper",
307:               back.get("footerInside", False))
308: 
309:     # ---- Mobile back card (A50-ish 412x892) ----
310:     mob = render(BACK_CARD.replace("__CSS__", css), 412, 892)
311:     check("mobile back: probe returned", mob is not None)
312:     if mob:
313:         check("mobile back: no horizontal overflow", not mob["hOverflow"])
314:         check("mobile back: stacked (no context-grid columns)", not mob.get("twoCol", False))
315:         check("mobile back: no forced viewport fill",
316:               mob["wrapperH"] < 0.95 * mob["viewportH"],
317:               f"wrapper={mob['wrapperH']:.0f} viewport={mob['viewportH']}")
318:         check("mobile back: sentence font stays >= 1rem", mob.get("sentFont", 1) >= 16)
319: 
320:     # ---- Front sentence card ----
321:     fr = render(FRONT_SENTENCE.replace("__CSS__", css), 1440, 900)
322:     check("front sentence: probe returned", fr is not None)
323:     if fr:
324:         check("front sentence: no horizontal overflow", not fr["hOverflow"])
325:         check("front sentence: content-driven (wrapper < 50% viewport)",
326:               fr["wrapperH"] < 0.5 * fr["viewportH"],
327:               f"wrapper={fr['wrapperH']:.0f}")
328: 
329:     # ---- Front listening card ----
330:     fl = render(FRONT_LISTENING.replace("__CSS__", css), 1440, 900)
331:     check("front listening: probe returned", fl is not None)
332:     if fl:
333:         check("front listening: button is a comfortable target (>= 64px)",
334:               fl.get("listenBtn", 0) >= 64, f"btn={fl.get('listenBtn')}")
335:         check("front listening: view height in 20-35vh band",
336:               0.20 * fl["viewportH"] <= fl.get("listenH", 0) <= 0.36 * fl["viewportH"],
337:               f"listenH={fl.get('listenH', 0):.0f}")
338: 
339:     print()
340:     print(f"{PASS} passed, {FAIL} failed")
341:     return 1 if FAIL else 0
342: 
343: 
344: if __name__ == "__main__":
345:     sys.exit(main())

(End of file - total 345 lines)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: bash
**Status:** completed
**Title:** fd . docs/adr

**Input:**
```json
{
  "command": "fd . docs/adr"
}
```

**Output:**
```
docs/adr/001-mature-word-mode-interval.md
docs/adr/002-definition-compactor-css.md
docs/adr/003-native-audio-delegation.md
docs/adr/004-single-command-release.md

```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: read
**Status:** completed
**Title:** docs/adr/001-mature-word-mode-interval.md

**Input:**
```json
{
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/docs/adr/001-mature-word-mode-interval.md"
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/docs/adr/001-mature-word-mode-interval.md</path>
<type>file</type>
<content>
1: # ADR 001 — Mature Word Mode interval retrieval
2: 
3: Date: 2026-09 (records the as-built decision).
4: 
5: ## Context
6: 
7: Anti-overlearning requires the front to show only the Expression once a
8: card is mature (interval ≥ `LONG_INTERVAL_DAYS`). No `{{Interval}}` marker
9: exists, and new fields / add-ons / review-time Python are all rejected.
10: 
11: ## Options considered
12: 
13: 1. Bake the interval into a field at mining time — stale the next day.
14: 2. Guess the card id from the URL — no stable id is exposed.
15: 3. Single live-read path for both platforms — mobile has no AnkiConnect and
16:    the refused fetch surfaces as `Failed to load 'downloadfile.bin'`.
17: 4. **Platform-exclusive live read (chosen).**
18: 
19: ## Decision
20: 
21: Desktop reads AnkiConnect only (`guiCurrentCard`→`cardsInfo`, `findCards`
22: content-search fallback for the Browse previewer). Mobile reads the AnkiDroid
23: JS bridge only (`ankiGetCardInterval()`, both constructor and direct shapes,
24: stub guard, timeouts, short late-injection poll). Listening fronts skip all
25: retrieval. Any failure degrades to the sentence front behind an anti-flash
26: gate.
27: 
28: ## Consequences
29: 
30: Preview screens without a bridge correctly show the sentence front. Two
31: platform paths must both be covered by `test_templates.py` §8b on every
32: change.

(End of file - total 32 lines)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: read
**Status:** completed
**Title:** docs/adr/002-definition-compactor-css.md

**Input:**
```json
{
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/docs/adr/002-definition-compactor-css.md"
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/docs/adr/002-definition-compactor-css.md</path>
<type>file</type>
<content>
1: # ADR 002 — Definition Compactor as structural CSS
2: 
3: ## Context
4: 
5: Yomitan mines the full multi-dictionary gloss into `Definition`, far too
6: verbose for the main card, while `Extended definition` must stay complete.
7: 
8: ## Options considered
9: 
10: 1. Trim at mining time (Yomitan settings/handlers) — fragile per-dictionary,
11:    lost on re-mine.
12: 2. Trim in JS at render time — flash of full text, more failure modes.
13: 3. **Structural CSS hiding (chosen).**
14: 
15: ## Decision
16: 
17: CSS §6b collapses to the first dictionary, ≤2 senses, no appendices, matched
18: on structure (`data-sc-*`, glossary lists) — never dictionary names — and
19: scoped strictly to `.primary-definition`.
20: 
21: ## Consequences
22: 
23: Dictionary-agnostic and flash-free; Yomitan markup drift is caught by
24: `test_compactor.py` fixtures taken from real mined cards.

(End of file - total 24 lines)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: read
**Status:** completed
**Title:** docs/adr/003-native-audio-delegation.md

**Input:**
```json
{
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/docs/adr/003-native-audio-delegation.md"
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/docs/adr/003-native-audio-delegation.md</path>
<type>file</type>
<content>
1: # ADR 003 — Native-only audio delegation
2: 
3: ## Context
4: 
5: Custom circular buttons (`文` / `言葉`) must play audio on Desktop and
6: AnkiDroid without overlapping playback.
7: 
8: ## Options considered
9: 
10: 1. HTML5 `new Audio(filename)` — AnkiDroid render links carry no usable
11:    filename (old builds emit `playsound:q:0`), causing bogus-file loads.
12: 2. Nest the replay link inside `<button>` — invalid HTML, Android WebView
13:    mishandles taps.
14: 3. **`playCircularAudio` delegating to the sibling native replay link
15:    (chosen).**
16: 
17: ## Decision
18: 
19: The `.raw-audio-source` span lives **outside** the button, visually hidden
20: but kept in layout (never `display:none`, which breaks programmatic
21: `.click()`). Every play path resets state first; re-taps on the playing
22: button are ignored (native audio can't be stopped); the ring is a decorative
23: pulse.
24: 
25: ## Consequences
26: 
27: No filenames are ever constructed in JS. Markup/JS contract is pinned by
28: `test_templates.py` §§2–3b.

(End of file - total 28 lines)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: read
**Status:** completed
**Title:** docs/adr/004-single-command-release.md

**Input:**
```json
{
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/docs/adr/004-single-command-release.md"
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/docs/adr/004-single-command-release.md</path>
<type>file</type>
<content>
1: # ADR 004 — Single-command release with pre-sync snapshots
2: 
3: ## Context
4: 
5: Multi-step endings (test → sync → export → commit → push → release) were
6: dropped late in sessions when run manually.
7: 
8: ## Decision
9: 
10: `finish.sh` runs the full chain and stops on first failure; `./verify` is
11: the side-effect-free subset it delegates to. `sync_to_anki.py` snapshots the
12: live Anki state to `backups/<timestamp>/` (microsecond stamps) before
13: overwriting and aborts on empty live state. `release_apkg.py` uses the only
14: verified export action (`exportPackage`) into gitignored `dist/`; the apkg
15: ships as a GitHub Release asset, never in the repo. No-op runs never publish.
16: 
17: ## Consequences
18: 
19: One command to remember; snapshots make Anki-side overwrites recoverable;
20: tag, tree, and live templates agree (CSS header is stamped before sync).

(End of file - total 20 lines)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: bash
**Status:** completed
**Title:** ./verify

**Input:**
```json
{
  "command": "./verify"
}
```

**Output:**
```
==> verify: compactor regression tests
[PASS] D1 headword kept (澄ます・清ます)
[PASS] D1 sense ① kept
[PASS] D1 sense ② kept
[PASS] D1 sense ③+ hidden
[PASS] D1 sense ④-⑨ hidden
[PASS] D1 sub-sense ㋐ hidden
[PASS] D1 補説G hidden
[PASS] D1 可能形 hidden
[PASS] D1 accent [2] hidden
[PASS] D2 (大辞泉) fully hidden
[PASS] D2 類語 commentary hidden
[PASS] exactly 2 senses visible overall
[PASS] plain: gloss 1 kept
[PASS] plain: gloss 2 kept
[PASS] plain: gloss 3+ hidden
[PASS] plain: second dictionary hidden
[PASS] label: <i>(大辞林　第四版)</i> hidden
[PASS] label: sub-entry <i>(子, ...)</i> hidden
[PASS] label: sub-entry word 会社員 hidden
[PASS] label: headword kept
[PASS] label: sense kept
[PASS] fallback: compacted like main Definition
[PASS] ext: third sense still visible
[PASS] ext: second dictionary still visible
[PASS] all hide rules scoped to .primary-definition

25 passed, 0 failed
==> verify: template structural invariants
[PASS] Front renders no furigana: filter or furigana-bearing field
[PASS] Front renders the raw Sentence/Expression fields
[PASS] Front: all 1 script block(s) parse as valid JavaScript
[PASS] Back: all 1 script block(s) parse as valid JavaScript
[PASS] all 3 audio buttons have aria-label
[PASS] Front: no is-paused state remnants
[PASS] Front: resetAudioState defined
[PASS] Front: native-only playback (no new Audio garbage-loads on AnkiDroid)
[PASS] Front: delegates to Anki replay link
[PASS] Front: replay link resolved via wrapper scope (not nested in button)
[PASS] Front: re-tap debounce (native audio can't be stopped)
[PASS] Front: playCircularAudio starts with resetAudioState
[PASS] Back: no is-paused state remnants
[PASS] Back: resetAudioState defined
[PASS] Back: native-only playback (no new Audio garbage-loads on AnkiDroid)
[PASS] Back: delegates to Anki replay link
[PASS] Back: replay link resolved via wrapper scope (not nested in button)
[PASS] Back: re-tap debounce (native audio can't be stopped)
[PASS] Back: playCircularAudio starts with resetAudioState
[PASS] Front: replay source lives OUTSIDE the button (sibling span)
[PASS] Front: no display:none audio source (breaks .click() playback)
[PASS] Front: no div-inside-button (invalid HTML, breaks AnkiDroid taps)
[PASS] Back: replay source lives OUTSIDE the button (sibling span)
[PASS] Back: no display:none audio source (breaks .click() playback)
[PASS] Back: no div-inside-button (invalid HTML, breaks AnkiDroid taps)
[PASS] CSS: raw-audio-source visually hidden but present (no display:none)
[PASS] Front: hidden cloze probe with plain prefix/body/suffix fields
[PASS] Front: probe uses plain fields (no edit: filter, stays furigana-free)
[PASS] Front: reconstruction only fires when sentence lacks bold
[PASS] Front: reconstruction requires the complete trio (no partial rebuild)
[PASS] Front: rebuilt term uses <b> (inherits sentence-display styling)
[PASS] lightbox closes only on backdrop click (e.target === overlay)
[PASS] lightbox overlay has dialog semantics
[PASS] lightbox clone preserves alt text
[PASS] Front: balanced field conditionals (24 open / 24 close)
[PASS] Back: balanced field conditionals (25 open / 25 close)
[PASS] CSS: :focus-visible keyboard indicator present
[PASS] CSS: prefers-reduced-motion present
[PASS] CSS: content-driven card sizing (no forced viewport fill)
[PASS] CSS: container-query media fallback for the context grid
[PASS] Back: no sticky tags bar (tags are behavioral metadata)
[PASS] Back: no frequency badge machinery (noise without retrieval value)
[PASS] CSS: no frequency badge styling remains
[PASS] Back: secondary info is collapsed behind More by default
[PASS] Back: More toggle has aria state + one-way reveal
[PASS] Back: retrieval-state label present but hidden by default
[PASS] Back: state label reads the front decision store
[PASS] Front: front-state store written for the back label
[PASS] Back: keyboard F toggles full-card furigana (back only)
[PASS] Back: keyboard T reveals the translation
[PASS] CSS: full-card furigana mode rule exists
[PASS] Front: listening resolver driven by #listening tag probe
[PASS] Front: listening resolver also accepts classic audio-only fields
[PASS] Front: listening markup gated behind Sentence Audio only
[PASS] Front: listening resolver runs synchronously before the reveal
[PASS] Front: sentence front is the universal fallback (renders in the audio branch too)
[PASS] CSS: listening-view inert until .listening-mode activates it
[PASS] CSS: listening mode hides the sentence/word fronts
[PASS] Front: active listening removes the sentence display
[PASS] Back: no JS font-scaler overriding CSS (inline fontSize ban)
[PASS] CSS: .sentence-japanese clamp() is the sizing authority
[PASS] Front: LONG_INTERVAL_DAYS threshold constant defined
[PASS] Front: threshold not hard-coded elsewhere (single const definition)
[PASS] Front: word probe div present with Expression
[PASS] Front: desktop flow guiCurrentCard -> cardsInfo -> interval
[PASS] Front: previewer fallback via content search (findCards)
[PASS] Front: no nonexistent Anki-Connect actions
[PASS] Front: no card-id-from-URL guess (no URLSearchParams)
[PASS] Front: AnkiDroid JS API with verified contract
[PASS] Front: supports constructor + direct bridge APIs
[PASS] Front: never invokes new-reviewer stub bridge (signal:jsapi guard)
[PASS] Front: accepts AnkiDroid {success,value} shape (official wiki contract)
[PASS] Front: rejects {success:false} failure defaults (number => -1)
[PASS] Front: parses numeric strings + JSON-encoded responses
[PASS] Front: bridge call has its own timeout (never hangs the card)
[PASS] Front: never fetches AnkiConnect from mobile WebViews (downloadfile.bin toast)
[PASS] Front: one deferred bridge retry on mobile while still hidden
[PASS] Front: polls for late-injected bridge with a firm deadline
[PASS] Front: bridge poll capped short (fast preview fallback)
[PASS] Front: platform-exclusive retrieval (mobile bridge vs desktop AnkiConnect)
[PASS] Front: retrieval latency is measured and logged
[PASS] Front: safety reveal cap bounds worst-case hidden time
[PASS] Front: AnkiConnect calls fail fast when Anki is wedged (safe sentence fallback)
[PASS] Front: temporary toast diagnostic removed (no TEMP-DIAG remnants)
[PASS] Front: on-card debug diagnostic present (mwm-debug)
[PASS] Front: skips ALL retrieval on listening cards (no needless JS-API calls)
[PASS] Front: anti-flash visibility gate present
[PASS] Front: word-mode class applied to card wrapper
[PASS] Front: retrieval failure falls back to sentence (try/catch + typed interval check)
[PASS] CSS: word-mode display rules present
[PASS] CSS: word mode leaves listening view untouched
[PASS] Front: no "note:" search clause ({{Type}} is scheduling type, not model)
[PASS] every rendered field is conditional (or allowlisted)
[PASS] CSS: empty .audio-row collapses (no button => gone)
[PASS] Back: More section + toggle self-remove when secondary content is absent
[PASS] Back: blank definition box is removed (no bordered void)
[PASS] Front: blank sentence block is removed after cloze fixup
[PASS] sync_to_anki.py: zero third-party imports (standard lib only)
[PASS] sync_to_anki.py: microsecond backup timestamps
[PASS] finish.sh: no-op run cannot publish a release

100 passed, 0 failed
==> verify: front-mode resolver behavior (listening semantics)
[PASS] classic audio-only: probe returned
[PASS] classic audio-only: resolver ran without errors
[PASS] classic audio-only: listening front active (view visible, sentence gone)
[PASS] #listening tag with glosses: probe returned
[PASS] #listening tag with glosses: resolver ran without errors
[PASS] #listening tag with glosses: listening front active (view visible, sentence gone)
[PASS] audio with glosses, no tag: probe returned
[PASS] audio with glosses, no tag: resolver ran without errors
[PASS] audio with glosses, no tag: sentence front (listening inert)
[PASS] no audio: probe returned
[PASS] no audio: resolver ran without errors
[PASS] no audio: sentence front (listening inert)
[PASS] frequency legacy: probe returned
[PASS] frequency legacy: resolver ran without errors
[PASS] frequency legacy: sentence front (listening inert)
[PASS] tag but no sentence audio: probe returned
[PASS] tag but no sentence audio: resolver ran without errors
[PASS] tag but no sentence audio: sentence front (listening inert)

18 passed, 0 failed
==> verify: headless layout checks (skipped gracefully without Chrome)
[PASS] desktop back: probe returned
[PASS] desktop back: content-driven card (rich card < 100% viewport)
[PASS] desktop back: no horizontal overflow
[PASS] desktop back: word furigana stays inside its line box
[PASS] desktop back: sentence furigana stays inside its block
[PASS] desktop back: hierarchy word > sentence > definition > notes
[PASS] desktop back: long definition IS truncated by JS
[PASS] desktop back: clamped height ≈ pad + 3 line-heights
[PASS] desktop back: expand grows the definition (one-way)
[PASS] desktop back: image height capped (<= 40vh)
[PASS] desktop back: context grid engaged (picture beside sentence)
[PASS] desktop back: picture column is the minority width
[PASS] desktop back: secondary info collapsed behind More by default
[PASS] desktop back: footer inside the card wrapper
[PASS] mobile back: probe returned
[PASS] mobile back: no horizontal overflow
[PASS] mobile back: stacked (no context-grid columns)
[PASS] mobile back: no forced viewport fill
[PASS] mobile back: sentence font stays >= 1rem
[PASS] front sentence: probe returned
[PASS] front sentence: no horizontal overflow
[PASS] front sentence: content-driven (wrapper < 50% viewport)
[PASS] front listening: probe returned
[PASS] front listening: button is a comfortable target (>= 64px)
[PASS] front listening: view height in 20-35vh band

25 passed, 0 failed
verify: OK

```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: bash
**Status:** completed
**Title:** rtk ruff check .

**Input:**
```json
{
  "command": "rtk ruff check ."
}
```

**Output:**
```
Ruff: 32 issues in 7 files (16 fixable)
Top rules:
  FURB167 (9x)
  SIM115 (6x)
  EXE001 (5x)
  BLE001 (4x)
  PLW1510 (3x)
  I001 (3x)
  DTZ005 (1x)
  RUF013 (1x)

Top files:
  tests/test_templates.py (12 issues)
    SIM115 (5)
    FURB167 (5)
    EXE001 (1)
  sync_to_anki.py (4 issues)
    BLE001 (1)
    I001 (1)
    DTZ005 (1)
  tests/test_front_modes.py (4 issues)
    FURB167 (2)
    PLW1510 (1)
    EXE001 (1)
  tests/test_layout.py (4 issues)
    PLW1510 (1)
    EXE001 (1)
    FURB167 (1)
  release_apkg.py (3 issues)
    I001 (1)
    BLE001 (1)
    EXE001 (1)
  tests/test_compactor.py (3 issues)
    EXE001 (1)
    I001 (1)
    FURB167 (1)
  fetch_anki_fields.py (2 issues)
    BLE001 (2)

Violations:
  fetch_anki_fields.py:38:12 BLE001 Do not catch blind exception: `Exception`
  fetch_anki_fields.py:58:12 BLE001 Do not catch blind exception: `Exception`
  release_apkg.py:1:1 EXE001 Shebang is present but file is not executable
  release_apkg.py:9:1 I001 Import block is un-sorted or un-formatted
  release_apkg.py:41:12 BLE001 Do not catch blind exception: `Exception`
  sync_to_anki.py:1:1 I001 Import block is un-sorted or un-formatted
  sync_to_anki.py:35:40 RUF013 PEP 484 prohibits implicit `Optional`
  sync_to_anki.py:53:12 BLE001 Do not catch blind exception: `Exception`
  sync_to_anki.py:80:13 DTZ005 `datetime.datetime.now()` called without a `tz` argument
  tests/test_compactor.py:1:1 EXE001 Shebang is present but file is not executable
  tests/test_compactor.py:15:1 I001 Import block is un-sorted or un-formatted
  tests/test_compactor.py:50:51 FURB167 Use of regular expression alias `re.S`
  tests/test_front_modes.py:1:1 EXE001 Shebang is present but file is not executable
  tests/test_front_modes.py:57:16 FURB167 Use of regular expression alias `re.S`
  tests/test_front_modes.py:114:19 PLW1510 `subprocess.run` without explicit `check` argument
  tests/test_front_modes.py:124:49 FURB167 Use of regular expression alias `re.S`
  tests/test_layout.py:1:1 EXE001 Shebang is present but file is not executable
  tests/test_layout.py:247:19 PLW1510 `subprocess.run` without explicit `check` argument
  tests/test_layout.py:258:49 FURB167 Use of regular expression alias `re.S`
  tests/test_layout.py:271:11 SIM115 Use a context manager for opening files
  tests/test_templates.py:1:1 EXE001 Shebang is present but file is not executable
  tests/test_templates.py:48:13 SIM115 Use a context manager for opening files
  tests/test_templates.py:49:12 SIM115 Use a context manager for opening files
  tests/test_templates.py:50:11 SIM115 Use a context manager for opening files
  tests/test_templates.py:69:65 FURB167 Use of regular expression alias `re.S`
  tests/test_templates.py:76:26 PLW1510 `subprocess.run` without explicit `check` argument
  tests/test_templates.py:109:177 FURB167 Use of regular expression alias `re.S`
  tests/test_templates.py:226:57 FURB167 Use of regular expression alias `re.S`
  tests/test_templates.py:304:54 FURB167 Use of regular expression alias `re.S`
  tests/test_templates.py:305:65 FURB167 Use of regular expression alias `re.S`
  tests/test_templates.py:334:12 SIM115 Use a context manager for opening files
  tests/test_templates.py:339:14 SIM115 Use a context manager for opening files

[hint] Run `ruff check --fix` to auto-fix 16 issues

```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: bash
**Status:** completed
**Title:** rtk pyright

**Input:**
```json
{
  "command": "rtk pyright"
}
```

**Output:**
```
/home/mohamed/Desktop/Github/anki-japanese-template/sync_to_anki.py
  /home/mohamed/Desktop/Github/anki-japanese-template/sync_to_anki.py:35:47 - error: Expression of type "None" cannot be assigned to parameter of type "dict[Unknown, Unknown]"
    "None" is not assignable to "dict[Unknown, Unknown]" (reportArgumentType)
  /home/mohamed/Desktop/Github/anki-japanese-template/sync_to_anki.py:50:19 - error: "error" is not a known attribute of module "urllib" (reportAttributeAccessIssue)
/home/mohamed/Desktop/Github/anki-japanese-template/tests/test_front_modes.py
  /home/mohamed/Desktop/Github/anki-japanese-template/tests/test_front_modes.py:114:19 - error: No overloads for "run" match the provided arguments (reportCallIssue)
  /home/mohamed/Desktop/Github/anki-japanese-template/tests/test_front_modes.py:115:18 - error: Argument of type "list[str | None]" cannot be assigned to parameter "args" of type "_CMD" in function "run"
    Type "str | None" is not assignable to type "StrOrBytesPath"
      Type "None" is not assignable to type "StrOrBytesPath"
        "None" is not assignable to "str"
        "None" is not assignable to "bytes"
        "None" is incompatible with protocol "PathLike[str]"
          "__fspath__" is not present
        "None" is incompatible with protocol "PathLike[bytes]"
          "__fspath__" is not present (reportArgumentType)
/home/mohamed/Desktop/Github/anki-japanese-template/tests/test_layout.py
  /home/mohamed/Desktop/Github/anki-japanese-template/tests/test_layout.py:247:19 - error: No overloads for "run" match the provided arguments (reportCallIssue)
  /home/mohamed/Desktop/Github/anki-japanese-template/tests/test_layout.py:248:18 - error: Argument of type "list[str | None]" cannot be assigned to parameter "args" of type "_CMD" in function "run"
    Type "str | None" is not assignable to type "StrOrBytesPath"
      Type "None" is not assignable to type "StrOrBytesPath"
        "None" is not assignable to "str"
        "None" is not assignable to "bytes"
        "None" is incompatible with protocol "PathLike[str]"
          "__fspath__" is not present
        "None" is incompatible with protocol "PathLike[bytes]"
          "__fspath__" is not present (reportArgumentType)
6 errors, 0 warnings, 0 informations

```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: bash
**Status:** completed
**Title:** fd . .github

**Input:**
```json
{
  "command": "fd . .github"
}
```

**Output:**
```
.github/workflows/
.github/workflows/verify.yml

```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: read
**Status:** completed
**Title:** .github/workflows/verify.yml

**Input:**
```json
{
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/.github/workflows/verify.yml"
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/.github/workflows/verify.yml</path>
<type>file</type>
<content>
1: name: verify
2: 
3: on:
4:   push:
5:   pull_request:
6: 
7: jobs:
8:   verify:
9:     runs-on: ubuntu-latest
10:     steps:
11:       - uses: actions/checkout@v4
12:       - uses: actions/setup-python@v5
13:         with:
14:           python-version: "3.x"
15:       - name: Install test-only deps (compactor)
16:         run: pip install beautifulsoup4 soupsieve
17:       - name: Run local quality gate
18:         run: ./verify

(End of file - total 18 lines)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: bash
**Status:** completed
**Title:** rtk git log --oneline -15

**Input:**
```json
{
  "command": "rtk git log --oneline -15"
}
```

**Output:**
```
fb0f27f test_layout: font-independent overflow guarantee (CI has no CJK fonts)
75d9e9b Minimal redesign: pure retrieval front, quiet hierarchical back
ced9584 Empty-field collapse everywhere: shell guards, degenerate-content removal, enclosure test and QUALITY rule
9d038b8 Adopt self-describing methodology: PRODUCT/MVP/ARCHITECTURE/QUALITY/TEST_STRATEGY/PLAN, slim AGENTS.md, verif...
3ba5da7 Density pass: content-driven card height (viewport fill removed, sticky side dropped), tightened spacing toke...
2d8317b finish.sh v2 flow: version stamps into CSS before the Anki sync so the live template always matches the relea...
b0433bc finish.sh: stamp version into CSS before the Anki sync (live template could lag one version); move tag bump+s...
63a299b finish.sh: release tag is remote-only (gh); fetch it instead of pushing a nonexistent local tag
20ebbfe Word header: word + frequency/pitch/audio now share one row on wide screens (space-between, baseline-aligned)...
e6408b2 Widescreen fluid layout: body text (definition/translation/notes/extended) now scales with viewport via clamp...
c77b3ad Cap side picture at 40vw so it shrinks with the window (main column keeps the majority); block-level img remo...
e118ffa Fix back card layout: side columns now shrink-wrap to the displayed image width via min-content grid tracks
f1db5aa Rewrite README: shorter, current (modes, compactor, truncator, live fields)
fc24a51 Front: rebuild bold-less Sentence from cloze trio via JS
faeb471 fetch_anki_fields.py: include Anki field descriptions in snapshot

```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: bash
**Status:** completed
**Title:** fd . chat_history conversations

**Input:**
```json
{
  "command": "fd . chat_history conversations"
}
```

**Output:**
```
chat_history/definition-truncation-handoff.md
chat_history/gemini_cli_prompts.txt
chat_history/opencode_prompts.txt
conversations/20260909-13-38-47-Dynamic-layout-for-wide-screen.md
conversations/20260910-15-42-11-New-session-2026-09-10T14-42-1.md
conversations/20260910-19-58-16-Reading-codebase.md
conversations/20260912-01-55-22-Anki-Japanese-card-template-vi.md
conversations/images/
conversations/images/20260909-13-38-47-Dynamic-layout-for-wide-screens-0.png

```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

#### 🔧 Tool: read
**Status:** completed
**Title:** chat_history/opencode_prompts.txt

**Input:**
```json
{
  "limit": 50,
  "offset": 1,
  "filePath": "/home/mohamed/Desktop/Github/anki-japanese-template/chat_history/opencode_prompts.txt"
}
```

**Output:**
```
<path>/home/mohamed/Desktop/Github/anki-japanese-template/chat_history/opencode_prompts.txt</path>
<type>file</type>
<content>
1: read my code base, and think of any possbile way to imporve it, either functionality, finiding bugs, improving design, etc
2: 
3: ---
4: 
5: if you are confident you can fix any issue you underlined go for it I trust you, always use git so i can go back if things don't work, also connect things to anki via anki connect so i can see the changes once you are done
6: 
7: ---
8: 
9: one is of them is an old file left from earlier devloppement feel free to delete it(i don't remember which)
10: 
11: ---
12: 
13: A 1 ok 2 ok
14: 
15: ---
16: 
17: go
18: 
19: ---
20: 
21: good job on what you did but i meant all the previous git history stored locally not the 1.0 but what comes before it
22: 
23: ---
24: 
25: how to export opencode's chat history, only my prompts, same with gemini cli(used it at the start) and store everything in github in a dedicated file/folder
26: 
27: ---
28: 
29: in the read me add a mention on the tools used open code and gemini cli used to cerate this and the all the model called with % (say the main model is X with Y%)
30: 
31: ---
32: 
33: don't halluicante the numbers(in %) calclaute them effectively
34: 
35: ---
36: 
37: how would i update it locally without breaking git, also how to synchornize my changes to github
38: do I update inside anki, but then everything will stay local and git will break
39: 
40: ---
41: 
42: a very small bug remains , hovering over furigana shows furrigana as it should but the whole ext moves by a few pixels to make room for the furigna that will apprer on top making an unpleasant effect each time I hover
43: inceasing the spacing between lines will obviously solve this, but I need you to come with a clever dynamic solution that works at every screen size and is the minimal added distance necsary as I said multiple time screen real estate is really precious, espacially on mobile
44: Another thing, from now on always update not only via sync and git but alos push to github.
45: From now on always update my rpompt into chat_history in the appriote folder(and add a mention of it in the md file so future agents do the same)
46: Also, update the Gemini.md(rename btw to amore universal name) with a mention to github(for future agents), add a quick section in readme about what you just told me about github.
47: 
48: 
49: ---
50: 

(Showing lines 1-50 of 2249. Use offset=51 to continue.)
</content>
```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

💭 **Reasoning:**

<details>
<summary>Click to expand reasoning</summary>

**Deep dive into project aspects**

Initial assessment focuses on dissecting the repository across product design, technical architecture, card template implementation (HTML/JS/Anki engine integration), and CSS styling. The aim is to understand each component's role and how they integrate to deliver the final product.


**Examining the initial card template**

The front card template employs an anti-flash gate, initially hiding the content and revealing it after a delay. Field presence checks are utilized before conditional logic, suggesting field resolvers are used to determine what content to display. Nested conditionals drive the display logic, including fallback mechanisms for various field combinations.


**Analyzing template duplication and global scope**

The HTML duplication likely stems from Mustache limitations, resulting in verbose conditional branching; however, the mutually exclusive nature of the conditions ensures only one section renders, confirming static rendering behavior. Identical global function definitions within front and back templates raise concern; since front and back share the context, this could introduce unintended side effects.


**Investigating AnkiConnect integration**

The AnkiConnect interval retrieval leverages `guiCurrentCard` and `cardsInfo` to fetch review data. Desktop Anki interaction involves communication via the `fetch` API, potentially over port 8765, where CORS is typically handled. However, an API key configuration for AnkiConnect would cause the retrieval to fail if it isn't included in the request.

**Examining application settings and parsing logic**

The `DEBUG_MATURE_MODE` setting is hardcoded, suggesting a compile-time configuration. The `parseDroidInterval` function includes a robust loop for parsing interval data, implying careful error handling for varied data formats. Preview search utilizes an expression-based query, suggesting the handling of text input with escaping.


**Analyzing Anki template field usage**

The Anki search syntax confirms field matching via the colon, including handling field names with spaces. Examination of back card templates reveals the use of `{{edit:furigana:Expression}}` and its impact. It appears the template utilizes a filter to handle brackets, or display plain text. The application of `edit:` to definition fields, and its potential interference with existing `onclick` behavior requires further investigation, as the `edit:` prefix typically originates from an addon.


**Investigating card template event handling**

Observed that `onclick` on an editable field container potentially triggers an unintended interaction when editing and expanding a definition. The translation reveal/hide behavior uses `toggle` which is appropriate, in contrast to the one-way expansion. Further, a keyboard listener bound to the `document` could cause unintended side-effects. This is because the underlying platform's WebView reuses the `window` and `document` objects when reviewing cards.


**Diagnosing DOM Re-use Bug in Webview**

The root cause appears to be the re-use of the Webview's `window` and `document` objects when displaying the next card. Each card review results in the addition of a new keydown listener to the `document`. Since the existing `wrapper` does not have the flag set, a new listener is added.

Within each listener, a query selects the current `wrapper`. Pressing the 'f' key triggers toggling a class on the wrapper. With multiple listeners, this leads to toggling an even number of times, effectively canceling out the change. This behavior will be confirmed.


**Confirming DOM Listener Accumulation**

The keydown listener accumulation on the `document` object across card reviews is verified; the listener is added to `document`, not the per-card `wrapper`, which is why each card adds a new listener. This explains the observed issue where the `furigana-mode` toggle does nothing after the second card. `window.currentActiveTimer` and `window.currentActiveBtn` which are stored on the `window` are intended to persist across cards, so their persistence is expected.


**Investigating persistent event handlers**

The keyboard event listener attached to the document is correctly removed on close. However, the `document.fonts.ready` promise `.then()` callback calls a function which is re-executed on each card. This will likely cause performance issues or unexpected behavior.

**Examining style sheet inconsistencies**

The style sheet uses `.nightMode` for desktop and `.night_mode` for the AnkiDroid, indicating platform-specific styling. The CSS hides the sentence display in word mode, but no unique styling exists for the `.front-word-display` element; it is styled in a shared manner.


**Reviewing CSS style discrepancies**

The `.front-word-display` element in word mode explicitly hides content, so furigana headroom is not needed on the front. Formatting inconsistency noted in line 965; a typo detected in the URL on line 999.

**Analyzing SVG backdrop embedding**

Two large data URLs for SVG images are embedded directly in CSS for dark and light modes, increasing CSS size. The `.back-card::before` selector's multiple `--backdrop-image` declarations appear redundant.




</details>

#### 🔧 Tool: bash
**Status:** completed
**Title:** rtk rg "back-card"

**Input:**
```json
{
  "command": "rtk rg \"back-card\""
}
```

**Output:**
```
...output truncated...

Full output saved to: /home/mohamed/.local/share/opencode/tool-output/tool_096dced21001YwLytIiA42SVk3

Also check `.back-card::before` backdrop uses position: fixed full-viewport — unaffected by wrapper height. Fine.
1177: .card.back-card {
1181: .card.back-card::before {
1197: .back-card::before {
1201: .card:not(.nightMode):not(.night_mode) .card.back-card::before {
1205: .back-card .card-container {
11: <div class="card-wrapper back-card">
Let me now also double-check: removing min-height 100vh from .card-wrapper — does anything depend on the wrapper being full height? `.back-card::before` backdrop is `position: fixed` → viewport-sized regardless. `.card-container` flex-grow removal — wrapper is flex column; container is sole child; no visual change when content-sized. The tags bar sticky top:0 — sticky within the scrolling review area; fine.
  "content": "#!/usr/bin/env python3\n\"\"\"Headless layout verification for the density pass.\n\nRenders the REAL stylesheet plus template-shaped HTML in Chrome headless\n(google-chrome-stable is available on this machine) and asserts layout\ninvariants that pure text tests cannot catch:\n\n  - card height is content-driven (back card < 90% of viewport height\n    on a rich desktop card, i.e. no viewport fill)\n  - no horizontal overflow / clipping\n  - furigana (rt) never overlaps the line above it\n  - hierarchy: headword font > sentence font > definition font > notes\n  - truncator: a long definition clamps at 3 lines until expanded\n  - listening front keeps the audio button a comfortable target\n  - definition expand still works (JS one-way expand)\n\nUsage: python3 tests/test_layout.py\nRequires: google-chrome-stable on PATH. Skipped gracefully if absent\n        (finish.sh runs it as part of step 0 when present).\n\"\"\"\nimport json\nimport os\nimport shutil\nimport subprocess\nimport sys\nimport tempfile\n\nHERE = os.path.dirname(os.path.abspath(__file__))\nROOT = os.path.dirname(HERE)\nCSS = os.path.join(ROOT, \"Card 1 - Style.css\")\nCHROME = shutil.which(\"google-chrome-stable\") or shutil.which(\"chromium\")\n\nPASS = 0\nFAIL = 0\n\n\ndef check(name, cond, detail=\"\"):\n    global PASS, FAIL\n    tag = \"PASS\" if cond else \"FAIL\"\n    print(f\"[{tag}] {name}\" + (f\" ({detail})\" if detail and not cond else \"\"))\n    if cond:\n        PASS += 1\n    else:\n        FAIL += 1\n\n\n# ---------------------------------------------------------------- HTML fixture\n# Back card with every block populated: furigana headword, badges, audio,\n# long definition, furigana sentence, translation, context, side column\n# with picture + kanji notes + extended accordion, source footer.\nBACK_CARD = \"\"\"<!doctype html><html><head><meta charset=\"utf-8\">\n<style>\nhtml,body{margin:0;padding:0;}\n/* minimal Anki stand-ins: replay link + fonts so JS runs like in Anki */\n</style>\n<style>\n__CSS__\n</style></head><body>\n<div class=\"card back-card\">\n<div class=\"card-wrapper back-card\">\n  <div class=\"tags-container\"><div class=\"tags-list\">\n    <span class=\"tag-pill\">noun</span><span class=\"tag-pill\">n1</span>\n  </div></div>\n  <div class=\"card-container\">\n   <div class=\"back-grid\">\n    <div class=\"main-content\">\n      <div class=\"card-block word-header\">\n        <div class=\"word-display-row\">\n          <div class=\"word-display\"><ruby>澄<rt>す</rt></ruby>ます</div>\n          <div class=\"word-meta-row\">\n            <div class=\"frequency-badge freq-common\" data-freq=\"1200\">\n              <div class=\"frequency-bar-track\"><div class=\"frequency-bar-fill\"></div></div>\n              <span class=\"frequency-stars\"></span></div>\n            <div class=\"pitch-accent-badge\"><span>[0]</span></div>\n            <div class=\"audio-row\">\n              <span class=\"audio-btn-wrapper\">\n                <button type=\"button\" class=\"circular-audio-btn small-audio-btn\"><span class=\"audio-btn-content\"><span class=\"audio-btn-label\">言葉</span></span></button>\n                <span class=\"raw-audio-source\"><a class=\"replay-button\" href=\"#\">replay</a></span>\n              </span>\n              <span class=\"audio-btn-wrapper\">\n                <button type=\"button\" class=\"circular-audio-btn small-audio-btn\"><span class=\"audio-btn-content\"><span class=\"audio-btn-label\">文</span></span></button>\n                <span class=\"raw-audio-source\"><a class=\"replay-button\" href=\"#\">replay</a></span>\n              </span>\n            </div>\n          </div>\n        </div>\n        <div class=\"definition-box primary-definition\" id=\"def\">\n          <div class=\"yomitan-glossary\"><ol>\n            <li><div data-sc-name=\"語義G\">水などを濁りのない状態にする。とても長い定義のテキストで、三行を超えることを保証するためにさらに文字を追加している。</div>\n            <div data-sc-name=\"語義G\">雑念を払って、心を落ち着かせる。二番目の語義。</div>\n            <div data-sc-name=\"語義G\">一つのことに注意を向ける。三番目の語義（隠れるはず）。</div>\n            <div data-sc-name=\"補説G\">supplementary (hidden)</div></li>\n          </ol></div>\n        </div>\n      </div>\n      <div class=\"card-block sentence-block\">\n        <div class=\"sentence-japanese\" id=\"sentence\"><ruby>心<rt>こころ</rt></ruby>を<ruby>澄<rt>す</rt></ruby>ませて、<b>音楽</b>を聴く。長い文章が二行に折り返される場合の検証も兼ねている。</div>\n        <div class=\"translation-box\"><div class=\"translation-hint\">👁️ Translation</div>\n          <div class=\"translation-text\">To clear one's mind and listen to music.</div></div>\n        <div class=\"context-block\"><div class=\"html-content\">Additional context paragraph.</div></div>\n      </div>\n    </div>\n    <div class=\"side-content\">\n      <div class=\"card-block picture-block\">\n        <div class=\"picture-container\"><img id=\"pic\" src=\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='800' height='600'%3E%3Crect width='100%25' height='100%25' fill='%2338bdf8'/%3E%3C/svg%3E\"></div>\n      </div>\n      <div class=\"card-block\"><div class=\"html-content\">漢字のメモ: 澗 — radical 水.</div></div>\n      <div class=\"details-wrapper\">\n        <details class=\"modern-details\"><summary class=\"modern-summary\"><span>Extended Definition</span><span>▼</span></summary>\n        <div class=\"extended-def-content\">Full extended definition text that stays untruncated.</div></details>\n      </div>\n    </div>\n   </div>\n   <div class=\"source-footer\">SOURCE — some novel</div>\n  </div>\n</div>\n</div>\n<script>\nwindow.expandDefinition = function(element) {\n  if (element.classList.contains('is-expanded')) return;\n  element.classList.add('is-expanded');\n};\nwindow.initDefinitionTruncation = function(root) {\n  const scope = root || document;\n  scope.querySelectorAll('.primary-definition').forEach(function(box) {\n    const overflows = box.scrollHeight > box.clientHeight + 2;\n    box.classList.toggle('is-truncated', overflows);\n  });\n};\nwindow.initDefinitionTruncation();\n</script>\n</body></html>\"\"\"\n\nFRONT_SENTENCE = \"\"\"<!doctype html><html><head><meta charset=\"utf-8\">\n<style>__CSS__</style></head><body>\n<div class=\"card\"><div class=\"card-wrapper\">\n  <div class=\"card-container\">\n    <div class=\"sentence-display\" id=\"sent\">彼は<b>約束</b>を<ruby>守<rt>まも</rt></ruby>らなかった。</div>\n  </div>\n</div></div>\n</body></html>\"\"\"\n\nFRONT_LISTENING = \"\"\"<!doctype html><html><head><meta charset=\"utf-8\">\n<style>__CSS__</style></head><body>\n<div class=\"card\"><div class=\"card-wrapper\">\n  <div class=\"card-container\">\n    <div class=\"listening-view\" id=\"listening\">\n      <div class=\"audio-btn-wrapper\">\n        <button type=\"button\" class=\"circular-audio-btn large-audio-btn\"><span class=\"audio-btn-content\"><span class=\"audio-btn-label\">文</span></span></button>\n      </div>\n    </div>\n  </div>\n</div></div>\n</body></html>\"\"\"\n\n\n# ---------------------------------------------------------------- probing JS\nPROBE = \"\"\"(() => {\n  const r = {};\n  const wrapper = document.querySelector('.card-wrapper');\n  const card = document.querySelector('.card');\n  r.wrapperH = wrapper.getBoundingClientRect().height;\n  r.viewportH = window.innerHeight;\n  r.docScrollW = document.documentElement.scrollWidth;\n  r.docClientW = document.documentElement.clientWidth;\n  // overflow-x anywhere?\n  r.hOverflow = r.docScrollW > r.docClientW + 1;\n  // furigana overlap: rt boxes vs previous line — collect any rt whose\n  // top is above the previous sibling line's bottom is hard generically;\n  // instead verify every rt's top >= its ruby's parent's top (rt never\n  // escapes the container) AND that rt boxes do not overlap the element\n  // above: compare first rt top vs sentence/word container top.\n  const word = document.querySelector('.word-display');\n  if (word) {\n    const rb = word.getBoundingClientRect();\n    const rt = word.querySelector('rt');\n    r.wordFont = parseFloat(getComputedStyle(word).fontSize);\n    if (rt) { const rtb = rt.getBoundingClientRect();\n      r.wordRtInside = rtb.top >= rb.top - 0.5 && rtb.bottom <= rb.bottom + 0.5; }\n  }\n  const sent = document.querySelector('#sentence, .sentence-japanese');\n  if (sent) {\n    r.sentFont = parseFloat(getComputedStyle(sent).fontSize);\n    const rt = sent.querySelector('rt');\n    const sb = sent.getBoundingClientRect();\n    if (rt) { const rtb = rt.getBoundingClientRect();\n      r.sentRtInside = rtb.top >= sb.top - 0.5; }\n    r.sentH = sb.height;\n  }\n  const def = document.querySelector('#def');\n  if (def) {\n    r.defFont = parseFloat(getComputedStyle(def).fontSize);\n    const cs = getComputedStyle(def);\n    r.defLineH = parseFloat(cs.lineHeight) || parseFloat(cs.fontSize) * 1.5;\n    r.defClampedH = def.getBoundingClientRect().height;\n    r.defScrollH = def.scrollHeight;\n    r.defTruncated = def.classList.contains('is-truncated');\n    // expand and re-measure\n    window.expandDefinition(def);\n    r.defExpandedH = def.getBoundingClientRect().height;\n  }\n  const notes = document.querySelector('.html-content');\n  if (notes && def) {\n    r.notesFont = parseFloat(getComputedStyle(notes).fontSize);\n    r.hierarchy = r.wordFont > r.sentFont && r.sentFont > r.defFont && r.defFont > r.notesFont;\n  }\n  const pic = document.querySelector('#pic');\n  if (pic) { const pb = pic.getBoundingClientRect(); r.picH = pb.height; r.picW = pb.width; }\n  const listening = document.querySelector('#listening');\n  if (listening) {\n    const lb = listening.getBoundingClientRect();\n    const btn = listening.querySelector('.circular-audio-btn');\n    r.listenH = lb.height;\n    r.listenBtn = btn.getBoundingClientRect().height;\n  }\n  const side = document.querySelector('.side-content');\n  const main = document.querySelector('.main-content');\n  if (side && main && innerWidth >= 768) {\n    r.twoCol = side.getBoundingClientRect().left > main.getBoundingClientRect().right;\n    r.sideW = side.getBoundingClientRect().width;\n    r.mainW = main.getBoundingClientRect().width;\n  }\n  const footer = document.querySelector('.source-footer');\n  if (footer && wrapper) {\n    r.footerInside = footer.getBoundingClientRect().bottom <= wrapper.getBoundingClientRect().bottom + 1;\n  }\n  return r;\n})()\"\"\"\n\n\ndef render(html, width, height):\n    \"\"\"Chrome headless screenshot + JS probe via --dump-dom is awkward;\n    use the DevTools-free trick: virtual-time + console.log of the probe,\n    captured from chrome's stderr? No — instead write the probe result\n    into the DOM title and read it from the dumped DOM.\"\"\"\n    probe_html = html.replace(\n        \"</body>\",\n        f\"<script>document.title = JSON.stringify({PROBE});</script></body>\",\n    )\n    with tempfile.TemporaryDirectory() as td:\n        path = os.path.join(td, \"card.html\")\n        with open(path, \"w\", encoding=\"utf-8\") as f:\n            f.write(probe_html)\n        try:\n            out = subprocess.run(\n                [CHROME, \"--headless=new\", \"--disable-gpu\",\n                 \"--no-sandbox\", \"--hide-scrollbars\",\n                 f\"--window-size={width},{height}\",\n                 \"--virtual-time-budget=2000\",\n                 \"--dump-dom\", f\"file://{path}\"],\n                capture_output=True, text=True, timeout=60,\n            ).stdout\n        except subprocess.TimeoutExpired:\n            return None\n    import re\n    m = re.search(r\"<title>(.*?)</title>\", out, re.S)\n    if not m:\n        return None\n    try:\n        return json.loads(m.group(1))\n    except json.JSONDecodeError:\n        return None\n\n\ndef main():\n    if not CHROME:\n        print(\"[SKIP] no headless Chrome found — layout checks skipped\")\n        return 0\n    css = open(CSS, encoding=\"utf-8\").read()\n\n    # ---- Desktop back card (1440x900, rich card) ----\n    back = render(BACK_CARD.replace(\"__CSS__\", css), 1440, 900)\n    check(\"desktop back: probe returned\", back is not None)\n    if back:\n        check(\"desktop back: no forced viewport fill (content-driven height)\",\n              back[\"wrapperH\"] < 0.9 * back[\"viewportH\"],\n              f\"wrapper={back['wrapperH']:.0f} viewport={back['viewportH']}\")\n        check(\"desktop back: no horizontal overflow\", not back[\"hOverflow\"])\n        check(\"desktop back: word furigana stays inside its line box\",\n              back.get(\"wordRtInside\", True))\n        check(\"desktop back: sentence furigana stays inside its block\",\n              back.get(\"sentRtInside\", True))\n        check(\"desktop back: hierarchy word > sentence > definition > notes\",\n              back.get(\"hierarchy\", False),\n              f\"word={back.get('wordFont')} sent={back.get('sentFont')} \"\n              f\"def={back.get('defFont')} notes={back.get('notesFont')}\")\n        check(\"desktop back: long definition IS truncated by JS\",\n              back.get(\"defTruncated\", False))\n        check(\"desktop back: clamped height ≈ 3 line-heights\",\n              abs(back[\"defClampedH\"] - 3 * back[\"defLineH\"]) <= 6,\n              f\"clamped={back['defClampedH']:.0f} 3lines={3*back['defLineH']:.0f}\")\n        check(\"desktop back: expand grows the definition (one-way)\",\n              back.get(\"defExpandedH\", 0) > back.get(\"defClampedH\", 0) + 4)\n        check(\"desktop back: image height capped (<= 40vh)\",\n              back.get(\"picH\", 0) <= 0.40 * back[\"viewportH\"] + 2,\n              f\"picH={back.get('picH', 0):.0f}\")\n        check(\"desktop back: two-column grid engaged\",\n              back.get(\"twoCol\", False),\n              f\"main={back.get('mainW', 0):.0f} side={back.get('sideW', 0):.0f}\")\n        check(\"desktop back: side column is the minority width\",\n              back.get(\"sideW\", 1) < back.get(\"mainW\", 0))\n        check(\"desktop back: footer inside the card wrapper\",\n              back.get(\"footerInside\", False))\n\n    # ---- Mobile back card (A50-ish 412x892) ----\n    mob = render(BACK_CARD.replace(\"__CSS__\", css), 412, 892)\n    check(\"mobile back: probe returned\", mob is not None)\n    if mob:\n        check(\"mobile back: no horizontal overflow\", not mob[\"hOverflow\"])\n        check(\"mobile back: stacked (no two-column)\", not mob.get(\"twoCol\", False))\n        check(\"mobile back: no forced viewport fill\",\n              mob[\"wrapperH\"] < 0.95 * mob[\"viewportH\"],\n              f\"wrapper={mob['wrapperH']:.0f} viewport={mob['viewportH']}\")\n        check(\"mobile back: touch targets >= 36px\",\n              mob.get(\"listenBtn\", 0) == 0 or True)  # no listening btn here\n        small_btn = 44  # enforced by CSS floor; probe small-audio instead\n        check(\"mobile back: small audio buttons keep 44px floor\", small_btn >= 44)\n        check(\"mobile back: sentence font stays >= 1rem\", mob.get(\"sentFont\", 1) >= 16)\n\n    # ---- Front sentence card ----\n    fr = render(FRONT_SENTENCE.replace(\"__CSS__\", css), 1440, 900)\n    check(\"front sentence: probe returned\", fr is not None)\n    if fr:\n        check(\"front sentence: no horizontal overflow\", not fr[\"hOverflow\"])\n        check(\"front sentence: content-driven (wrapper < 50% viewport)\",\n              fr[\"wrapperH\"] < 0.5 * fr[\"viewportH\"],\n              f\"wrapper={fr['wrapperH']:.0f}\")\n\n    # ---- Front listening card ----\n    fl = render(FRONT_LISTENING.replace(\"__CSS__\", css), 1440, 900)\n    check(\"front listening: probe returned\", fl is not None)\n    if fl:\n        check(\"front listening: button is a comfortable target (>= 64px)\",\n              fl.get(\"listenBtn\", 0) >= 64, f\"btn={fl.get('listenBtn')}\")\n        check(\"front listening: view height in 20-35vh band\",\n              0.20 * fl[\"viewportH\"] <= fl.get(\"listenH\", 0) <= 0.36 * fl[\"viewportH\"],\n              f\"listenH={fl.get('listenH', 0):.0f}\")\n\n    print()\n    print(f\"{PASS} passed, {FAIL} failed\")\n    return 1 if FAIL else 0\n\n\nif __name__ == \"__main__\":\n    sys.exit(main())\n",
Pragmatic: keep the back-card desktop assertion as wrapper < viewport * 1.3 (pathological fixture allowed to scroll, but not 2x viewport)? That's weak sauce. Alternative: reduce fixture sentence length so the rich card fits (realistic card) and assert < 90%. Plus keep a pathological variant asserting truncator/scroll affordances instead of height. Actually simpler: the fixture sentence wraps to 2 lines at 72px — realistic cards DO look like this on 1440px wide. 948px tall on a 813 inner-height window — the user's actual Arch desktop is likely 1080p+ (inner ~1000+). At 1440x900 Chrome inner 813... real Anki on 1080p: inner ≈ 950. 948 ≈ fits.
<div class="card back-card"><div class="card-wrapper back-card">
  "command": "rtk python3 - <<'PY'\nimport sys, json\nsys.path.insert(0, 'tests')\nfrom test_layout import render, PROBE\n# light card: short sentence, short definition, no context — typical mined note\nHTML = \"\"\"<!doctype html><html><head><meta charset=\"utf-8\"><style>%s</style></head><body>\n<div class=\"card back-card\"><div class=\"card-wrapper back-card\">\n  <div class=\"card-container\"><div class=\"back-grid\">\n    <div class=\"main-content\">\n      <div class=\"card-block word-header\">\n        <div class=\"word-display-row\">\n          <div class=\"word-display\"><ruby>約束<rt>やくそく</rt></ruby></div>\n          <div class=\"word-meta-row\"><div class=\"audio-row\">\n            <span class=\"audio-btn-wrapper\"><button type=\"button\" class=\"circular-audio-btn small-audio-btn\"><span class=\"audio-btn-content\"><span class=\"audio-btn-label\">言葉</span></span></button></span>\n          </div></div>\n        </div>\n        <div class=\"definition-box primary-definition\" id=\"def\">promise; arrangement</div>\n      </div>\n      <div class=\"card-block sentence-block\">\n        <div class=\"sentence-japanese\" id=\"sentence\"><b>約束</b>を守る。</div>\n      </div>\n    </div>\n    <div class=\"side-content\">\n      <div class=\"card-block picture-block\"><div class=\"picture-container\"><img id=\"pic\" src=\"data:image/svg+xml,%%3Csvg xmlns='http://www.w3.org/2000/svg' width='800' height='600'%%3E%%3Crect width='100%%25' height='100%%25' fill='%%2338bdf8'/%%3E%%3C/svg%%3E\"></div></div>\n    </div>\n  </div></div>\n</div></div></body></html>\"\"\" % open('Card 1 - Style.css').read().replace('%','%%')\nr = render(HTML, 1440, 900)\nprint(json.dumps({k: r.get(k) for k in ('wrapperH','sentH','picH','sideW','mainW','hOverflow','twoCol')}, indent=1))\nPY",
<div class="card back-card"><div class="card-wrapper back-card">
  "command": "rtk python3 - <<'PY'\nimport sys, json\nsys.path.insert(0, 'tests')\nfrom test_layout import render\ncss = open('Card 1 - Style.css', encoding='utf-8').read()\nSVG = \"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='800' height='600'%3E%3Crect width='100%25' height='100%25' fill='%2338bdf8'/%3E%3C/svg%3E\"\nHTML = f\"\"\"<!doctype html><html><head><meta charset=\"utf-8\"><style>{css}</style></head><body>\n<div class=\"card back-card\"><div class=\"card-wrapper back-card\">\n  <div class=\"card-container\"><div class=\"back-grid\">\n    <div class=\"main-content\">\n      <div class=\"card-block word-header\">\n        <div class=\"word-display-row\">\n          <div class=\"word-display\"><ruby>約束<rt>やくそく</rt></ruby></div>\n          <div class=\"word-meta-row\"><div class=\"audio-row\">\n            <span class=\"audio-btn-wrapper\"><button type=\"button\" class=\"circular-audio-btn small-audio-btn\"><span class=\"audio-btn-content\"><span class=\"audio-btn-label\">言葉</span></span></button></span>\n          </div></div>\n        </div>\n        <div class=\"definition-box primary-definition\" id=\"def\">promise; arrangement</div>\n      </div>\n      <div class=\"card-block sentence-block\">\n        <div class=\"sentence-japanese\" id=\"sentence\"><b>約束</b>を守る。</div>\n      </div>\n    </div>\n    <div class=\"side-content\">\n      <div class=\"card-block picture-block\"><div class=\"picture-container\"><img id=\"pic\" src=\"{SVG}\"></div></div>\n    </div>\n  </div></div>\n</div></div></div></body></html>\"\"\"\nr = render(HTML, 1440, 900)\nprint(json.dumps({k: r.get(k) for k in ('wrapperH','sentH','picH','sideW','mainW','hOverflow','twoCol')}, indent=1) if r else 'PROBE FAILED')\nPY",
<div class="card back-card"><div class="card-wrapper back-card">
  "command": "rtk python3 - <<'PY'\nimport sys, json\nsys.path.insert(0, 'tests')\nfrom test_layout import render\ncss = open('Card 1 - Style.css', encoding='utf-8').read()\nSVG = \"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='800' height='600'%3E%3Crect width='100%25' height='100%25' fill='%2338bdf8'/%3E%3C/svg%3E\"\nHTML = f\"\"\"<!doctype html><html><head><meta charset=\"utf-8\"><style>{css}</style></head><body>\n<div class=\"card back-card\"><div class=\"card-wrapper back-card\">\n  <div class=\"card-container\"><div class=\"back-grid\">\n    <div class=\"main-content\">\n      <div class=\"card-block word-header\">\n        <div class=\"word-display-row\">\n          <div class=\"word-display\"><ruby>約束<rt>やくそく</rt></ruby></div>\n          <div class=\"word-meta-row\"><div class=\"audio-row\">\n            <span class=\"audio-btn-wrapper\"><button type=\"button\" class=\"circular-audio-btn small-audio-btn\"><span class=\"audio-btn-content\"><span class=\"audio-btn-label\">言葉</span></span></button></span>\n          </div></div>\n        </div>\n        <div class=\"definition-box primary-definition\" id=\"def\">promise; arrangement</div>\n      </div>\n      <div class=\"card-block sentence-block\">\n        <div class=\"sentence-japanese\" id=\"sentence\"><b>約束</b>を守る。</div>\n      </div>\n    </div>\n    <div class=\"side-content\">\n      <div class=\"card-block picture-block\"><div class=\"picture-container\"><img id=\"pic\" src=\"{SVG}\"></div></div>\n    </div>\n  </div></div>\n</div></div></div></body></html>\"\"\"\nr = render(HTML, 1440, 900)\nprint('RESULT:', json.dumps({k: r.get(k) for k in ('wrapperH','sentH','picH','sideW','mainW','hOverflow','twoCol')}, indent=1) if r else 'PROBE FAILED')\n# no-def variant: same card without the definition box\nHTML2 = HTML.replace('<div class=\"definition-box primary-definition\" id=\"def\">promise; arrangement</div>', '')\nr2 = render(HTML2, 1440, 900)\nprint('NO-DEF:', json.dumps({k: r2.get(k) for k in ('wrapperH','picH','sideW','twoCol')}, indent=1) if r2 else 'PROBE FAILED')\nPY",
<div class="card back-card"><div class="card-wrapper back-card">
  "command": "rtk python3 - <<'PY'\nimport sys, json\nsys.path.insert(0, 'tests')\nfrom test_layout import render\ncss = open('Card 1 - Style.css', encoding='utf-8').read()\nSVG = \"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='800' height='600'%3E%3Crect width='100%25' height='100%25' fill='%2338bdf8'/%3E%3C/svg%3E\"\ndef card(with_def):\n    d = '<div class=\"definition-box primary-definition\" id=\"def\">promise; arrangement</div>' if with_def else ''\n    return f\"\"\"<!doctype html><html><head><meta charset=\"utf-8\"><style>{css}</style></head><body>\n<div class=\"card back-card\"><div class=\"card-wrapper back-card\">\n  <div class=\"card-container\"><div class=\"back-grid\">\n    <div class=\"main-content\">\n      <div class=\"card-block word-header\">\n        <div class=\"word-display-row\">\n          <div class=\"word-display\"><ruby>約束<rt>やくそく</rt></ruby></div>\n          <div class=\"word-meta-row\"><div class=\"audio-row\">\n            <span class=\"audio-btn-wrapper\"><button type=\"button\" class=\"circular-audio-btn small-audio-btn\"><span class=\"audio-btn-content\"><span class=\"audio-btn-label\">言葉</span></span></button></span>\n          </div></div>\n        </div>\n        {d}\n      </div>\n      <div class=\"card-block sentence-block\">\n        <div class=\"sentence-japanese\" id=\"sentence\"><b>約束</b>を守る。</div>\n      </div>\n    </div>\n    <div class=\"side-content\">\n      <div class=\"card-block picture-block\"><div class=\"picture-container\"><img id=\"pic\" src=\"{SVG}\"></div></div>\n    </div>\n  </div></div>\n</div></div></div></body></html>\"\"\"\nr = render(card(True), 1440, 900)\nprint('WITH-DEF:', json.dumps({k: r.get(k) for k in ('wrapperH','sentH','picH','sideW','mainW','twoCol','hOverflow')}, indent=1) if r else 'PROBE FAILED')\nPY",
<div class="card back-card"><div class="card-wrapper back-card">
  "command": "rtk python3 - <<'PY'\nimport subprocess, tempfile, os, re, json\ncss = open('Card 1 - Style.css', encoding='utf-8').read()\nSVG = \"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='800' height='600'%3E%3Crect width='100%25' height='100%25' fill='%2338bdf8'/%3E%3C/svg%3E\"\nhtml = f\"\"\"<!doctype html><html><head><meta charset=\"utf-8\"><style>{css}</style></head><body>\n<div class=\"card back-card\"><div class=\"card-wrapper back-card\">\n  <div class=\"card-container\"><div class=\"back-grid\">\n    <div class=\"main-content\">\n      <div class=\"card-block word-header\">\n        <div class=\"word-display-row\">\n          <div class=\"word-display\"><ruby>約束<rt>やくそく</rt></ruby></div>\n        </div>\n        <div class=\"definition-box primary-definition\" id=\"def\">promise; arrangement</div>\n      </div>\n    </div>\n  </div></div>\n</div></div></div></body></html>\"\"\"\nwith tempfile.TemporaryDirectory() as td:\n    p = os.path.join(td, 'x.html')\n    open(p, 'w').write(html)\n    out = subprocess.run(['google-chrome-stable','--headless=new','--disable-gpu','--no-sandbox',\n        '--window-size=1440,900','--virtual-time-budget=2000','--dump-dom', f'file://{p}'],\n        capture_output=True, text=True, timeout=60)\n    print('STDOUT tail:', out.stdout[-300:])\n    print('STDERR tail:', out.stderr[-500:])\nPY",
<div class="card back-card"><div class="card-wrapper back-card">
  "command": "rtk python3 - <<'PY'\nimport subprocess, tempfile, os, re, json\ncss = open('Card 1 - Style.css', encoding='utf-8').read()\nSVG = \"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='800' height='600'%3E%3Crect width='100%25' height='100%25' fill='%2338bdf8'/%3E%3C/svg%3E\"\nhtml = f\"\"\"<!doctype html><html><head><meta charset=\"utf-8\"><style>{css}</style></head><body>\n<div class=\"card back-card\"><div class=\"card-wrapper back-card\">\n  <div class=\"card-container\"><div class=\"back-grid\">\n    <div class=\"main-content\">\n      <div class=\"card-block word-header\">\n        <div class=\"word-display-row\">\n          <div class=\"word-display\"><ruby>約束<rt>やくそく</rt></ruby></div>\n          <div class=\"word-meta-row\"><div class=\"audio-row\">\n            <span class=\"audio-btn-wrapper\"><button type=\"button\" class=\"circular-audio-btn small-audio-btn\"><span class=\"audio-btn-content\"><span class=\"audio-btn-label\">言葉</span></span></button></span>\n          </div></div>\n        </div>\n        <div class=\"definition-box primary-definition\" id=\"def\">promise; arrangement</div>\n      </div>\n      <div class=\"card-block sentence-block\">\n        <div class=\"sentence-japanese\" id=\"sentence\"><b>約束</b>を守る。</div>\n      </div>\n    </div>\n    <div class=\"side-content\">\n      <div class=\"card-block picture-block\"><div class=\"picture-container\"><img id=\"pic\" src=\"{SVG}\"></div></div>\n    </div>\n  </div></div>\n</div></div></div></body></html>\"\"\"\nprobe = \"<script>document.title = JSON.stringify({h: document.querySelector('.card-wrapper').getBoundingClientRect().height, s: document.querySelector('#sentence').getBoundingClientRect().height, p: document.querySelector('#pic').getBoundingClientRect().height});</script>\"\nhtml = html.replace('</body>', probe + '</body>')\nwith tempfile.TemporaryDirectory() as td:\n    p = os.path.join(td, 'x.html')\n    open(p, 'w').write(html)\n    out = subprocess.run(['google-chrome-stable','--headless=new','--disable-gpu','--no-sandbox',\n        '--window-size=1440,900','--virtual-time-budget=2000','--dump-dom', f'file://{p}'],\n        capture_output=True, text=True, timeout=60).stdout\n    m = re.search(r'<title>(.*?)</title>', out, re.S)\n    print('title:', m.group(1) if m else 'NONE')\n    print('stdout tail:', out[-200:])\nPY",
<div class="card back-card"><div class="card-wrapper back-card">
  "command": "rtk python3 - <<'PY'\nimport subprocess, tempfile, os, re, json\ncss = open('Card 1 - Style.css', encoding='utf-8').read()\nSVG = \"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='800' height='600'%3E%3Crect width='100%25' height='100%25' fill='%2338bdf8'/%3E%3C/svg%3E\"\nhtml = f\"\"\"<!doctype html><html><head><meta charset=\"utf-8\"><style>{css}</style></head><body>\n<div class=\"card back-card\"><div class=\"card-wrapper back-card\">\n  <div class=\"tags-container\"><div class=\"tags-list\"><span class=\"tag-pill\">noun</span><span class=\"tag-pill\">n1</span></div></div>\n  <div class=\"card-container\"><div class=\"back-grid\">\n    <div class=\"main-content\">\n      <div class=\"card-block word-header\">\n        <div class=\"word-display-row\">\n          <div class=\"word-display\"><ruby>澄<rt>す</rt></ruby>ます</div>\n          <div class=\"word-meta-row\">\n            <div class=\"frequency-badge freq-common\" data-freq=\"1200\"><div class=\"frequency-bar-track\"><div class=\"frequency-bar-fill\"></div></div><span class=\"frequency-stars\"></span></div>\n            <div class=\"pitch-accent-badge\"><span>[0]</span></div>\n            <div class=\"audio-row\">\n              <span class=\"audio-btn-wrapper\"><button type=\"button\" class=\"circular-audio-btn small-audio-btn\"><span class=\"audio-btn-content\"><span class=\"audio-btn-label\">言葉</span></span></button></span>\n              <span class=\"audio-btn-wrapper\"><button type=\"button\" class=\"circular-audio-btn small-audio-btn\"><span class=\"audio-btn-content\"><span class=\"audio-btn-label\">文</span></span></button></span>\n            </div>\n          </div>\n        </div>\n      </div>\n      <div class=\"card-block sentence-block\">\n        <div class=\"sentence-japanese\" id=\"sentence\"><ruby>心<rt>こころ</rt></ruby>を<ruby>澄<rt>す</rt></ruby>ませて、<b>音楽</b>を聴く。長い文章が二行に折り返される場合の検証も兼ねている。</div>\n        <div class=\"translation-box\"><div class=\"translation-text\" style=\"display:block\">To clear one's mind and listen to music.</div></div>\n      </div>\n    </div>\n    <div class=\"side-content\">\n      <div class=\"card-block picture-block\"><div class=\"picture-container\"><img id=\"pic\" src=\"{SVG}\"></div></div>\n      <div class=\"card-block\"><div class=\"html-content\">漢字のメモ: 澗 — radical 水. Short note.</div></div>\n    </div>\n  </div></div>\n</div></div></div></body></html>\"\"\"\nprobe = \"\"\"<script>document.title = JSON.stringify((() => {\n  const g = s => document.querySelector(s).getBoundingClientRect();\n  return {wrap: g('.card-wrapper').height, word: g('.word-display').height,\n          wordRow: g('.word-display-row').height, sent: g('#sentence').height,\n          sentFont: parseFloat(getComputedStyle(document.querySelector('#sentence')).fontSize),\n          pic: g('#pic').height, side: g('.side-content').height, main: g('.main-content').height};\n})());</script>\"\"\"\nhtml = html.replace('</body>', probe + '</body>')\nwith tempfile.TemporaryDirectory() as td:\n    p = os.path.join(td, 'x.html')\n    open(p, 'w').write(html)\n    out = subprocess.run(['google-chrome-stable','--headless=new','--disable-gpu','--no-sandbox',\n        '--window-size=1440,900','--virtual-time-budget=2000','--dump-dom', f'file://{p}'],\n        capture_output=True, text=True, timeout=60).stdout\n    m = re.search(r'<title>(.*?)</title>', out, re.S)\n    print(m.group(1) if m else 'NONE')\nPY",
<div class="card back-card"><div class="card-wrapper back-card">
  "command": "rtk python3 - <<'PY'\nimport subprocess, tempfile, os\ncss = open('Card 1 - Style.css', encoding='utf-8').read()\nSVG = \"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='800' height='600'%3E%3Crect width='100%25' height='100%25' fill='%2338bdf8'/%3E%3C/svg%3E\"\nhtml = f\"\"\"<!doctype html><html><head><meta charset=\"utf-8\"><style>{css}</style></head><body>\n<div class=\"card back-card\"><div class=\"card-wrapper back-card\">\n  <div class=\"tags-container\"><div class=\"tags-list\"><span class=\"tag-pill\">noun</span><span class=\"tag-pill\">n1</span></div></div>\n  <div class=\"card-container\"><div class=\"back-grid\">\n    <div class=\"main-content\">\n      <div class=\"card-block word-header\">\n        <div class=\"word-display-row\">\n          <div class=\"word-display\"><ruby>澄<rt>す</rt></ruby>ます</div>\n          <div class=\"word-meta-row\">\n            <div class=\"frequency-badge freq-common\" data-freq=\"1200\"><div class=\"frequency-bar-track\"><div class=\"frequency-bar-fill\"></div></div><span class=\"frequency-stars\"></span></div>\n            <div class=\"pitch-accent-badge\"><span>[0]</span></div>\n            <div class=\"audio-row\">\n              <span class=\"audio-btn-wrapper\"><button type=\"button\" class=\"circular-audio-btn small-audio-btn\"><span class=\"audio-btn-content\"><span class=\"audio-btn-label\">言葉</span></span></button></span>\n              <span class=\"audio-btn-wrapper\"><button type=\"button\" class=\"circular-audio-btn small-audio-btn\"><span class=\"audio-btn-content\"><span class=\"audio-btn-label\">文</span></span></button></span>\n            </div>\n          </div>\n        </div>\n        <div class=\"definition-box primary-definition\">水などを濁りのない状態にする。雑念を払って、心を落ち着かせる。</div>\n      </div>\n      <div class=\"card-block sentence-block\">\n        <div class=\"sentence-japanese\"><ruby>心<rt>こころ</rt></ruby>を<ruby>澄<rt>す</rt></ruby>ませて、<b>音楽</b>を聴く。</div>\n      </div>\n    </div>\n    <div class=\"side-content\">\n      <div class=\"card-block picture-block\"><div class=\"picture-container\"><img src=\"{SVG}\"></div></div>\n      <div class=\"card-block\"><div class=\"html-content\">漢字のメモ: 澗 — radical 水.</div></div>\n    </div>\n  </div></div>\n  <div class=\"source-footer\">SOURCE — some novel</div>\n</div></div></div></body></html>\"\"\"\nimport re\nprobe = \"\"\"<script>document.title = JSON.stringify((() => {\n  const rows = [];\n  const wrap = document.querySelector('.card-wrapper');\n  const wrapRect = wrap.getBoundingClientRect();\n  // vertical gaps between consecutive major blocks in the main column\n  const blocks = [...document.querySelectorAll('.main-content > *, .card-wrapper > .tags-container, .card-wrapper > .card-container > .source-footer')];\n  const rects = blocks.map(b => b.getBoundingClientRect());\n  const gaps = [];\n  for (let i = 1; i < rects.length; i++) {\n    const gap = rects[i].top - rects[i-1].bottom;\n    if (gap > 0) gaps.push(Math.round(gap));\n  }\n  return {cardH: Math.round(wrapRect.height), gaps: gaps,\n          spareBelow: Math.round(window.innerHeight - wrapRect.bottom)};\n})());</script>\"\"\"\nhtml = html.replace('</body>', probe + '</body>')\nwith tempfile.TemporaryDirectory() as td:\n    p = os.path.join(td, 'x.html')\n    open(p, 'w').write(html)\n    for w, h, name in ((1440, 900, 'desktop'), (412, 892, 'mobile')):\n        out = subprocess.run(['google-chrome-stable','--headless=new','--disable-gpu','--no-sandbox',\n            '--hide-scrollbars', f'--window-size={w},{h}','--virtual-time-budget=2000','--dump-dom', f'file://{p}'],\n            capture_output=True, text=True, timeout=60).stdout\n        m = re.search(r'<title>(.*?)</title>', out, re.S)\n        print(name, ':', m.group(1) if m else 'NONE')\nPY",
 <div class="card-wrapper back-card">
13: <div class="card-wrapper back-card">
1198: .card.back-card {
1202: .card.back-card::before {
1218: .back-card::before {
1222: .card:not(.nightMode):not(.night_mode) .card.back-card::before {
1226: .back-card .card-container {
5:   - Front card never renders a furigana-bearing field (back-card-only rule)
47:     # --- 1. Front card: furigana is back-card only ---
59: <div class="card back-card">
60: <div class="card-wrapper back-card">
46. Let me reconsider `.card-container` width 98% and `.back-card .card-container { position: relative; z-index:1 }`. Fine.
13: <div class="card-wrapper back-card">
1198: .card.back-card {

```

*[step-finish part]*

### 🤖 Assistant
*2026-09-12 19:24:58*

*[step-start part]*

💭 **Reasoning:**

<details>
<summary>Click to expand reasoning</summary>

**Examining back card styling**

The HTML for the back card contains a wrapper class, and the associated CSS defines backdrop opacity and a `::before` pseudo-element for styling. This is the likely location for controlling the back card's appearance. The backdrop image and its styling are defined within the CSS.


**Identifying CSS selector discrepancies**

The provided CSS selectors appear incorrect when compared to the generated Anki HTML. The selector `.card.back-card` and its pseudo-element variant won't match any real elements. The selector `.back-card::before` targets the correct wrapper's pseudo-element, however, due to the failure of the prior selectors to find an associated element, the pseudo-element is not guaranteed to be created. This likely explains why the backdrop styling might not be applied as intended. The test's passing is now in question.


**Confirming test environment discrepancies**

The test environment likely includes an incorrect HTML structure with the combined class on a single element, leading to a false positive. Examining the Anki code reveals this is a compound selector requiring both classes on one element. This explains the observed visual inconsistency between the test and real Anki behavior. The test's matching selector in the test harness is an intersection selector which does not occur.


**Identifying test vulnerabilities**

The test suite relies heavily on brittle techniques for template testing. The layout test uses a hand-rolled HTML fixture which masks the selector issue. Several tests extract and validate content via regex, specifically comments or exact string fragments, in the template files. These approaches introduce high coupling to implementation details, thus becoming fragile.


**Analyzing release script robustness**

The release script updates version numbers and commits before attempting the release, potentially resulting in a partially-released state if the release step fails. The script stages all working tree changes with `git add -A`, potentially including unintended files. Failure of a template sync operation aborts the commit, which provides a safety check.

**Investigating Anki integration script**

Scripts connect to a local Anki instance. The first script fetches Anki fields and uses simplistic error handling. A template syncing script reads and overwrites Anki templates, performing a backup before overwriting. The script also has a safety check to abort on potentially empty Anki state. The final script exports an Anki package.


**Evaluating codebase architecture**

The codebase exhibits a high degree of upfront architectural planning, documented comprehensively with well-defined artifacts. It appears to be a personal project, given the deck name, yet the level of rigor in specification strongly resembles established software engineering methodologies.

**Recognizing disciplined specifications**

The documentation structure, adhering to spec-driven engineering principles, indicates a deliberate effort to define requirements, design the system, and ensure quality. The existence of an `IMPLEMENTATION_PLAN.md` with dependency DAG suggests deliberate project management. `QUALITY.md` explicitly lists invariants.


**Identifying event listener accumulation**

The Anki WebView re-use could lead to a keydown event listener leak due to repeated `document.addEventListener` calls without removing existing listeners. This could potentially cause performance issues and unexpected behavior over time. The root cause is likely the repeated attaching of listeners to the `document` object.

**Detecting selector mismatches**

The CSS selector used for the backdrop system is incorrect, potentially using the class `.card.back-card` or equivalent in the existing codebase when the actual class structure is slightly different. There may be a need to identify the correct selectors for all cases in order to achieve the desired backdrop styling. In one example, the correct class is `.card-wrapper.back-card` or even `body.card`, rather than the former, and thus requires investigation.

**Assessing testing brittleness**

The tests are heavily dependent on string matching and regexes, particularly in tests that parse source files using regex, increasing fragility. These techniques tightly couple the tests to the implementation details, making refactoring or even code style changes a major burden. Asserting exact regex implementation details makes refactoring extremely painful, and should be minimized.

**Uncovering environment assumption weaknesses**

The release pipeline makes explicit assumptions about the Anki environment, including the deck name and AnkiConnect address, limiting its reusability. The hardcoded AnkiConnect configuration lacks authentication or API key support, introducing a security risk. The release script's inflexibility restricts others from using it without the author's deck structure.

**Evaluating release script atomicity**

The release script has atomicity and safety issues: it stages untracked files blindly, commits before release, and contains partial failure state handling. The release process can be left in an inconsistent state if the release operation fails. `git add -A` blindly stages all changes, and if the release operation fails, the partial commit causes a release in an unknown state.

**Examining code duplication**

The code duplicates logic between Front and Back templates. Duplicate code includes the audio controller and functions like `resetAudioState` and `playCircularAudio`, which may lead to conflicts or inconsistencies as Anki transitions between the front and back of a card. Duplicated logic raises the potential for collision.

**Analyzing static analysis reports**

The codebase has multiple static analysis issues identified by the linter and type checker. These include bare `except Exception:` blocks, unclosed file handles, incorrect regex flags, and naive timezone handling, which can introduce bugs and maintainability problems. The type errors in a certain script indicate possible runtime issues.


**Identifying keydown listener memory leak**

The `keydown` event listener is repeatedly attached to the `document` object on each card, leading to a memory leak because the old card's DOM element is detached, but the listener still references it. This creates a situation where pressing keys triggers multiple, increasingly numerous listeners, many of which reference detached nodes. The growing number of listeners increases execution time and consumes memory.

**Assessing perceived performance impact**

A 1200ms anti-flash gate for card presentation in Mature Word Mode may degrade the user experience in high-volume SRS sessions. This delay needs further evaluation. The anti-flash gate's impact on workflow needs to be determined.

**Analyzing Yomitan integration brittleness**

The Yomitan definition compactor's reliance on the Yomitan HTML output structure introduces a point of failure, since the structure isn't versioned. An update to Yomitan could break the integration. The assumption on Yomitan's HTML introduces brittleness.

**Formulating roadmap recommendations**

A roadmap should include addressing the memory leak by removing event listeners, improving test robustness, refactoring the release script for greater atomicity and reusability, and mitigating duplication. The product's ergonomics should consider the anti-flash gate and interval fetching latency. These steps should be taken to move toward a more robust and distributable software solution.


**Proposing listener management strategy**

The listener leak can be fixed by attaching the `keydown` listener once to the `window` or `document` and toggling a class on the active wrapper using the `querySelector` API. This eliminates the repeated attachment of listeners. The key is to manage a single listener that toggles the `furigana-mode` class.

**Verifying CSS selector mismatch**

The provided CSS rule `.card.back-card` does not match any existing elements in the Anki DOM because the classes are applied separately to the `body` and a nested `div`. The `.card` class exists on the `body` while the `.back-card` class is present on a child element, `<div class="card-wrapper back-card">`. This selector will not find an element since the `card` and `back-card` classes do not co-exist on the same node.


**Verifying selector and test environment**

The CSS selector intended for the backdrop, `.card.back-card::before`, will not match any elements because the HTML structure uses distinct classes on separate elements. A test case incorrectly validates this by simulating the erroneous HTML structure. The backdrop styling is not rendered in Anki. The test does not accurately reflect the expected environment.

**Confirming code duplication**

The JavaScript templates for front and back cards exhibit code duplication. Functions such as audio control functions are replicated. The circumference calculations for the circular progress bars also vary between the front and back template. This logic duplication introduces the possibility of inconsistencies.


**Analyzing audio function shadowing**

The front and back card scripts both define global functions `window.playCircularAudio` and `window.resetAudioState`. Flipping cards overwrites these functions. In the event of a global variable shadowing, front and back card logic are mixed. The varying fallback audio values introduce state inconsistencies.

**Verifying Anki sound replacement**

The JavaScript accesses a `.replaybutton` element to play audio. Anki's sound replacement feature converts `[sound:xxx.mp3]` into HTML elements such as `<a class="replaybutton">`. This method efficiently reuses Anki's existing sound playback mechanism.


**Investigating audio playback limitations**

Creation of `new Audio()` objects fails within AnkiDroid due to a path masking issue. Triggering Anki's replay link leverages the internal audio player and represents an effective workaround.

**Evaluating CSS definition compactor**

CSS sibling combinators are employed to hide definition senses beyond the second. This approach eliminates layout flashes and relies on pure CSS data manipulation, an elegant solution.

**Analyzing Mature Word Mode's design**

Mature Word Mode hides sentences on the front of cards with long intervals to prevent context dependency. This reduces a failure mode and is implemented via an AnkiConnect bridge dynamically, avoiding manual card manipulation, though the operational drawbacks remain to be seen.


**Evaluating anti-flash gate performance**

The anti-flash mechanism introduces a potentially noticeable delay due to the network fetch and timeout. The inherent jitter in local network requests, combined with Anki's processing, could lead to perceptible pauses. The 1200ms timeout might become an ergonomics bottleneck in high-volume review sessions.

**Assessing repository hygiene**

The repository lacks standard Python dependency management tools and formatting/linting configurations. Absence of dependency files may hinder reproducibility. The untracked directory and substantial conversation logs suggest a need for cleanup.

**Analyzing high-level project verdict**

The project reflects a sophisticated design approach, exhibiting strong engineering principles. It is a highly ambitious personal tool, with an emphasis on engineering rigor, and the high-level code quality. The project’s engineering rigor should be balanced with the goal of usability.


**Summarizing codebase highlights**

The code demonstrates elegant CSS solutions, like zero-reflow furigana and a definition compactor using CSS sibling combinators. Audio is handled natively through DOM traversal rather than new Audio objects. The mature word mode implementation showcases effective anti-overlearning design.

**Identifying critical bug assessment**

There are significant issues: memory leaks in keydown listeners due to Anki WebView reuse, backdrop CSS selector mismatches masked by a test fixture, and brittle tests relying on string matching. Latency is introduced by an anti-flash gate on every card, and code duplication exists.

**Recognizing further architectural flaws**

Global scope collisions from duplicated scripts across platforms, and environment lock-in due to hardcoded deck names and missing API key support were noted. Dependency management is also incomplete, and an atomicity issue exists.




</details>

Here is my honest, unfiltered review of your repository from the perspective of a **Senior Software Engineer**.

---

### Executive Summary

This is easily in the **top 1% of Anki card templates in existence** in terms of engineering discipline and UX ambition. Most Anki card templates are messy snippets of unmaintained HTML/CSS copied from Reddit or forums. In contrast, you have:
- A formal specification hierarchy (`PRODUCT.md`, `MVP.md`, `ARCHITECTURE.md`, `QUALITY.md`, `TEST_STRATEGY.md`).
- Documented Architectural Decision Records (`docs/adr/`).
- Automated local test suites (`tests/`) verifying layout, HTML parsing, and CSS invariants via headless Chromium and BeautifulSoup.
- A single-command CI/release pipeline (`finish.sh`).

**However, wearing a rigorous Senior SE hat:** the codebase exhibits classic symptoms of a **hyper-engineered personal system**. Underneath the impressive documentation, there is a **serious event listener memory leak** caused by Anki's WebView DOM lifecycle, a **CSS selector bug that silently breaks the backdrop feature in real Anki** (masked because the test fixture didn't mirror real Anki DOM), **brittle white-box tests coupled to exact source code strings**, and **card review latency trade-offs** that need re-evaluating.

---

### 1. What is Genuinely Brilliant (Strengths)

1. **CSS Sibling Combinator Definition Compactor (`§6b`)**
   Truncating and filtering Yomitan dictionaries using pure CSS (`div[data-sc-name="語義G"] ~ div[data-sc-name="語義G"] ~ div[data-sc-name="語義G"] { display: none; }`) instead of runtime JS is a stroke of genius. It eliminates layout shift (CLS), eliminates JavaScript execution overhead on low-end mobile devices, and degrades gracefully.
2. **Zero-Reflow Absolute Furigana Architecture**
   Reserving vertical headroom via `--furigana-headroom: calc(0.55em + 2px)` and positioning `ruby rt` absolutely with hover/focus opacity solves the notorious furigana line-jumping issue on mobile and desktop without layout reflows.
3. **Native Audio Delegation (ADR 003)**
   Bypassing the HTML5 `Audio()` API and delegating click events directly to Anki’s native replay links avoids Android WebView audio sandboxing bugs and filename resolution failures on AnkiDroid.
4. **Mature Word Mode (ADR 001)**
   Solving "context overlearning" (where you memorize the sentence rather than the target vocabulary) by dynamically stripping context after $365$ days of retention is a top-tier SRS UX innovation.

---

### 2. Critical Bugs & Architectural Flaws

#### Bug 1: WebView DOM Re-use & Event Listener Memory Leak (High Severity)
In `Card 1 - Back.template.anki` (lines 382–404):
```javascript
window.initCardShortcuts = function() {
  var wrapper = document.querySelector('.card-wrapper.back-card');
  if (!wrapper || wrapper.dataset.shortcutsBound) return;
  wrapper.dataset.shortcutsBound = '1';
  document.addEventListener('keydown', function(e) {
    ...
    if (key === 'f') {
      wrapper.classList.toggle('furigana-mode');
    }
    ...
  });
};
```
* **The Root Cause:** In Anki Desktop (Qt6 WebEngine), moving to the next card **does not reload the page**. Anki reuses the `window` and `document`, dynamically replacing `#qa`.
* **The Failure Mode:**
  1. On Card 1, `document.addEventListener` binds a listener closing over Card 1's `wrapper`.
  2. On Card 2, the new card DOM does not have `dataset.shortcutsBound`. `initCardShortcuts()` runs again and binds a **second** listener to `document`.
  3. After 100 card reviews, `document` has **100 keydown listeners** holding onto 99 detached DOM tree wrappers in memory (classic garbage collection leak).
  4. Furthermore, because each listener closes over its specific card's `wrapper`, pressing `F` on Card 50 executes 50 closures.
* **The Fix:** Attach the event listener **once** to `window` or `document` (e.g. guard with `if (window.__ajtShortcutsBound) return; window.__ajtShortcutsBound = true;`) and dynamically query the *currently active* wrapper inside the handler:
  ```javascript
  const activeWrapper = document.querySelector('.card-wrapper.back-card');
  if (activeWrapper) activeWrapper.classList.toggle('furigana-mode');
  ```

---

#### Bug 2: The Invisible Backdrop Bug & Synthetic Test Masking
In `Card 1 - Style.css` (lines 1027–1052):
```css
.card.back-card { --backdrop-opacity: 0.5; }
.card.back-card::before { content: ""; position: fixed; ... }
.card:not(.nightMode):not(.night_mode) .card.back-card::before { ... }
```
* **The Root Cause:** In real Anki, Anki renders `<body class="card nightMode">`, and inside it is your template root `<div class="card-wrapper back-card">`.
* **The Failure Mode:** `.card.back-card` is a compound selector requiring **both** classes on the same HTML element. There is **no element** in real Anki with both `.card` and `.back-card`. Therefore, `::before` is never created in real Anki, and the Fuji backdrop was silently never rendering!
* **Why did the test pass?** In `tests/test_layout.py` (line 60), the test author manually constructed the HTML fixture as:
  `<div class="card back-card"><div class="card-wrapper back-card">`
  The test fixture deviated from real Anki DOM, masking the bug in CI while failing in production.
* **The Fix:** Use `.card-wrapper.back-card::before` or simply `.back-card::before`.

---

#### Bug 3: Brittle White-Box Test Anti-Pattern
In `tests/test_templates.py`, `tests/test_compactor.py`, and `tests/test_front_modes.py`, tests frequently parse source code using regexes against exact code strings:
- `load_hide_selectors()` uses `css.index("/* --- Collapse all dictionary entries...")` and `css.index("7. CIRCULAR AUDIO BUTTON")`.
- `load_resolver()` slices code between `/* --- LISTENING RESOLVER` and `console.warn('[Listening Resolver]', listenErr);`.
- `test_templates.py` asserts exact string matches like `re.search(r"window\.playCircularAudio = ...")` or checks whether a specific variable name exists.
* **Why this is problematic:** These are not contract tests; they are **change-detector tests**. If you rename an internal variable, refactor a function, or change a comment header, your tests break even if the template works flawlessly.
* **The Fix:** Shift verification towards **behavioral assertions** using headless Chrome evaluation on real DOM fixtures (like `test_front_modes.py` does for card states) rather than regexing source strings.

---

#### Bug 4: Card Review Latency Trade-Offs (Mature Word Mode)
In `Card 1 - Front.template.anki`:
- Every front render executes an async `fetch('http://127.0.0.1:8765')` to AnkiConnect.
- While fetching, the card is hidden via `visibility: hidden` behind an anti-flash gate.
- The safety reveal timeout is set to **1200ms**, and the fetch timeout is **500ms**.
* **The Problem:** In fast-paced SRS sessions, users review 10–20 cards per minute (3–5 seconds per card). Any network jitter on `127.0.0.1` or delay while Anki is doing a database sync can cause cards to take up to 500ms–1200ms to reveal.
* **The Fix:** Cache card intervals in `sessionStorage` or local memory, or evaluate whether the interval check can be done non-blocking or pre-fetched.

---

#### Bug 5: Code Duplication & Global Scope Collisions
`window.resetAudioState` and `window.playCircularAudio` are defined in **both** `Card 1 - Front.template.anki` and `Card 1 - Back.template.anki`, but with **different hardcoded fallback constants**:
- Front uses `226.19` (circumference for radius 36).
- Back uses `119.38` (circumference for radius 19).
Because Anki's WebEngine maintains global state across front and back card renders, these functions constantly overwrite each other on `window`. If state gets out of sync, one template uses the other's fallback radius.

---

### 3. Tooling, Packaging & Portability

1. **Hardcoded User Paths / Decks:**
   In `release_apkg.py`:
   `DECK_NAME = "My Life Decks::Japanese::anki-japanese-template"`
   Anyone cloning the repository cannot run `release_apkg.py` or `./finish.sh` without editing the script because they do not have your exact personal deck tree.
2. **AnkiConnect Authentication:**
   Both `fetch_anki_fields.py`, `sync_to_anki.py`, and the front template assume AnkiConnect has no `apiKey`. If a user protects AnkiConnect with a token, the scripts fail with unhandled errors.
3. **`finish.sh` Safety:**
   `finish.sh` uses `git add -A` and immediately commits. If there are temporary files, test dumps, or scratch files in the working directory, they will be silently committed and pushed to GitHub Releases.
4. **Code Quality Metrics:**
   Running `ruff` and `pyright` identifies:
   - 32 lint issues (e.g., bare `except Exception:`, unclosed file handles `open()` without `with`, naive `datetime.now()`).
   - 6 static type errors in `sync_to_anki.py` (e.g., `import urllib.request` without importing `urllib.error`, causing pyright attribute errors).

---

### 4. Repository Hygiene

- **Cruft in Root:** There is an empty directory `New Folder/` in the workspace.
- **Conversation Dumps:** `conversations/` and `chat_history/` contain megabytes of raw agent transcripts committed into git. Consider archiving these in a dedicated branch or `.gitignored` directory so the repository itself remains lean and clean for external users.
- **Missing Project Descriptor:** There is no `pyproject.toml` or `requirements.txt` documenting the test dependencies (`beautifulsoup4`, `soupsieve`).

---

### Summary Checklist for Next Improvements

| Priority | Item | Impact |
|---|---|---|
| 🚨 **P0** | **Fix keydown listener memory leak** in Back card | Prevents browser memory bloat and event storms during long review sessions |
| 🚨 **P0** | **Fix `.card.back-card` CSS selector** | Restores the Fuji backdrop in real Anki |
| 🟡 **P1** | **Import `urllib.error` in `sync_to_anki.py`** & clean ruff/pyright warnings | Prevents runtime `AttributeError` on failed connection |
| 🟡 **P1** | **Refactor regex white-box tests** into DOM-based contract assertions | Prevents test fragility during refactoring |
| 🟢 **P2** | **Externalize Deck & Note Type configs** from scripts into a config file | Allows other Japanese learners to use the sync/release scripts |
| 🟢 **P2** | **Clean up repository root** (remove `New Folder/`, add `requirements-dev.txt`) | Professional presentation |

*[step-finish part]*
