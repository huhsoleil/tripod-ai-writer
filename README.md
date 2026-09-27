# tripod-ai-writer

An Agent Skill that audits and writes clinical prediction-model manuscripts
(regression, machine learning, deep learning) according to the
**TRIPOD+AI** reporting guideline
([Collins et al., BMJ 2024;385:e078378](https://doi.org/10.1136/bmj-2023-078378)).

TRIPOD+AI 보고지침에 따라 예측모형(회귀, 머신러닝, 딥러닝) 논문을 점검하고
작성하는 Agent Skill입니다.

## What it does

The skill uses a two-stage workflow so that missing information is surfaced
before any prose is written.

| Stage | Input | Output |
|---|---|---|
| 1. Audit | `method.md`, `results.md` | `tripod_ai_checklist.md` (52 main + 13 abstract audit units), `issues_to_resolve.md` (Critical / Major / Minor / Information required), `author_responses.md` form |
| Gate | `author_responses.md` and/or revised inputs | Re-audit; proceeds only when no Critical issue remains |
| 2. Draft | All of the above | `manuscript.md`, updated checklist with manuscript locations, remaining issues |

Key rules:

- The bundled checklist, transcribed verbatim from the TRIPOD+AI
  publication, is the only source of item numbers and wording.
- No study-specific fact or number is invented; gaps become
  `[INFORMATION REQUIRED: …]` placeholders.
- Methods–Results consistency, data leakage, validation terminology,
  calibration, uncertainty, overfitting, and overstated conclusions are
  checked explicitly.
- A random split of one dataset is never called external validation.

## Install

With the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/huhsoleil/tripod-ai-writer --skill tripod-ai-writer
```

As a Claude Code plugin marketplace:

```bash
/plugin marketplace add huhsoleil/tripod-ai-writer
/plugin install tripod-ai-writer@tripod-ai-writer
```

Manually: copy `skills/tripod-ai-writer/` into `~/.claude/skills/` (Claude
Code) or zip that folder and upload it under Settings → Capabilities →
Skills (Claude apps).

## Usage

Put `method.md` (methods) and `results.md` (numerical results) in the
working directory, then ask, for example:

```
Write our deep learning prediction paper following TRIPOD+AI.
TRIPOD+AI에 따라 method.md와 results.md로 논문 작성을 진행해 주세요.
```

1. The skill returns the checklist, the issue list, and a gate status
   (`BLOCKED (n critical unresolved)` or `READY FOR STAGE 2`).
2. Answer the issues in `author_responses.md` by issue ID, or revise the
   input files.
3. Ask it to continue; it re-audits and drafts `manuscript.md` once no
   Critical issue remains. You can override the gate explicitly; the draft
   is then marked `DRAFT — NOT SUBMITTABLE`.

For an existing manuscript, ask for an audit only.

## Repository layout

```
.
├── .claude-plugin/marketplace.json     # Claude Code plugin marketplace manifest
├── skills/
│   └── tripod-ai-writer/
│       ├── SKILL.md                    # Instructions (frontmatter: name, description)
│       ├── references/
│       │   ├── tripod_ai_checklist.md  # Authoritative TRIPOD+AI checklist (verbatim)
│       │   ├── audit_rules.md
│       │   ├── deep_learning_details.md
│       │   └── output_templates.md
│       ├── assets/author_responses_template.md
│       ├── scripts/check_audit_coverage.py
│       └── evals/                      # Test prompts and synthetic fixtures (skill-creator format)
├── LICENSE
├── THIRD_PARTY_NOTICES.md
└── README.md
```

## Validate and test

```bash
# Frontmatter and structure (skill-creator validator)
python path/to/skill-creator/scripts/quick_validate.py skills/tripod-ai-writer

# Coverage check on a produced audit
python skills/tripod-ai-writer/scripts/check_audit_coverage.py tripod_ai_checklist.md issues_to_resolve.md
```

`skills/tripod-ai-writer/evals/evals.json` contains three test cases in the
[skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)
format. The fixtures in `evals/files/` are **synthetic** and contain planted
reporting problems (validation mislabelling, fold-number conflict,
preprocessing leakage, missing event counts, overstated conclusions).

## Limitations

- The skill supports transparent reporting; it does not assess risk of bias
  (use PROBAST / PROBAST+AI) and does not replace statistical review.
- For clustered or multicentre data, also consult TRIPOD-Cluster.
- Journal-specific requirements override the default manuscript structure.



## License

Skill instructions and code: Apache License 2.0 (see `LICENSE`).
The TRIPOD+AI checklist text is © the TRIPOD+AI authors and reproduced
under CC BY 4.0; see `THIRD_PARTY_NOTICES.md`. This project is not
affiliated with or endorsed by the TRIPOD group or BMJ.

## Skill.sh   search
[![skills.sh](https://skills.sh/b/huhsoleil/tripod-ai-writer)](https://skills.sh/huhsoleil/tripod-ai-writer)
