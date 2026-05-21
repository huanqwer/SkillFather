---

# Agent Skills Specification

Agent Skills 是一种开放标准，用于给 AI Agent 提供可复用的能力、工作流和领域知识。

官方定义：

> 一个 Skill 本质上是一个包含 `SKILL.md` 的目录。
> Agent 会按需加载这些技能，实现“渐进式上下文加载（Progressive Disclosure）”。

---

# 1. Skill Directory Structure

一个 Skill 至少必须包含：

```text
skill-name/
├── SKILL.md          # Required
├── scripts/          # Optional
├── references/       # Optional
├── assets/           # Optional
└── ...
```

---

# 2. SKILL.md Format

`SKILL.md` 必须包含：

1. YAML Frontmatter
2. Markdown Body

结构：

```markdown
---
name: skill-name
description: Description here
---

# Instructions

Actual skill instructions...
```

---

# 3. YAML Frontmatter Specification

## Required Fields

| Field         | Required | Description |
| ------------- | -------- | ----------- |
| `name`        | Yes      | Skill 名称    |
| `description` | Yes      | Skill 描述    |

---

## Optional Fields

| Field           | Required | Description           |
| --------------- | -------- | --------------------- |
| `license`       | No       | License 信息            |
| `compatibility` | No       | 环境兼容性说明               |
| `metadata`      | No       | 任意 Key-Value Metadata |
| `allowed-tools` | No       | 允许调用的工具（实验性）          |

---

# 4. name Field Rules

## Constraints

`name` 必须：

* 长度 1~64
* 仅允许：

  * `a-z`
  * `0-9`
  * `-`
* 不能：

  * 以 `-` 开头
  * 以 `-` 结尾
  * 包含连续 `--`
* 必须与父目录名一致

---

## Valid Examples

```yaml
name: pdf-processing
```

```yaml
name: data-analysis
```

```yaml
name: code-review
```

---

## Invalid Examples

```yaml
name: PDF-Processing
```

原因：

* 包含大写字母

---

```yaml
name: -pdf
```

原因：

* 不能以 `-` 开头

---

```yaml
name: pdf--processing
```

原因：

* 不允许连续 `--`

---

# 5. description Field Rules

## Constraints

* 长度：1~1024
* 必须非空
* 应描述：

  * Skill 做什么
  * 什么时候使用

---

## Good Example

```yaml
description: Extracts text and tables from PDF files, fills PDF forms, and merges multiple PDFs. Use when working with PDF documents or when the user mentions PDFs, forms, or document extraction.
```

---

## Poor Example

```yaml
description: Helps with PDFs.
```

---

# 6. license Field

推荐保持简短。

Example:

```yaml
license: Apache-2.0
```

或者：

```yaml
license: Proprietary. LICENSE.txt has complete terms
```

---

# 7. compatibility Field

用于描述运行环境需求。

例如：

```yaml
compatibility: Requires Python 3.14+ and uv
```

```yaml
compatibility: Requires git, docker, jq, and internet access
```

---

# 8. metadata Field

任意键值对。

Example:

```yaml
metadata:
  author: example-org
  version: "1.0"
```

---

# 9. allowed-tools Field

实验性字段。

用于声明：

Agent 可直接调用哪些工具。

Example:

```yaml
allowed-tools: Bash(git:*) Bash(jq:*) Read
```

---

# 10. Markdown Body

YAML Frontmatter 后面的正文部分：

没有强制格式限制。

推荐包含：

* Step-by-step Instructions
* Input / Output Examples
* Edge Cases
* Failure Handling
* Constraints

---

# 11. Optional Directories

---

## scripts/

可执行代码。

建议：

* 自包含
* 有错误处理
* 依赖明确

常见语言：

* Python
* Bash
* JavaScript

---

## references/

额外文档。

例如：

```text
references/
├── REFERENCE.md
├── FORMS.md
└── finance.md
```

原则：

* 小文件
* 按需加载
* 避免巨大上下文

---

## assets/

静态资源：

* Templates
* Images
* Schemas
* Lookup Tables

---

# 12. Progressive Disclosure Model

Agent Skills 的核心机制：

## Stage 1 — Discovery

Agent 启动时：

只读取：

```yaml
name
description
```

用于判断：

“什么时候该激活这个 Skill”。

---

## Stage 2 — Activation

任务匹配后：

加载整个：

```text
SKILL.md
```

---

## Stage 3 — Resource Loading

只有真正需要时：

才会读取：

* scripts/
* references/
* assets/

---

# 13. Recommended Size Limits

官方建议：

| Part        | Recommended Limit |
| ----------- | ----------------- |
| Metadata    | ~100 tokens       |
| SKILL.md    | < 5000 tokens     |
| File Length | < 500 lines       |

超长内容：

应拆分到：

```text
references/
```

---

# 14. File References

推荐使用：

相对路径。

Example:

```markdown
See [reference guide](references/REFERENCE.md)

Run:

scripts/extract.py
```

---

## Recommendation

避免：

```text
深层嵌套引用链
```

推荐：

```text
SKILL.md
  -> references/*
```

而不是：

```text
A -> B -> C -> D
```

---

# 15. Validation

官方验证工具：

```bash
skills-ref validate ./my-skill
```

用于检查：

* Frontmatter
* 命名规范
* 结构合法性

---

# 16. Minimal Complete Example

```markdown
---
name: pdf-processing
description: Extract text, fill forms, merge PDFs.
license: Apache-2.0

metadata:
  author: example-org
  version: "1.0"

compatibility: Requires Python 3.12+

allowed-tools: Bash(python:*) Read
---

# PDF Processing Skill

## Purpose

Handle PDF extraction and manipulation tasks.

## Workflow

1. Detect PDF files
2. Extract text
3. Validate OCR quality
4. Generate structured output

## Edge Cases

- Corrupted PDFs
- Password protected PDFs
- Scanned documents

## Scripts

Use:

scripts/extract.py

## References

See:

references/REFERENCE.md
```

---

# 17. Design Philosophy

Agent Skills 的核心理念：

## 轻量化

只有：

```text
SKILL.md
```

是强制的。

---

## 可移植

同一个 Skill：

可跨：

* Claude Code
* Cursor
* Codex
* Copilot
* OpenAI Agents
* 自定义 Agent Runtime

使用。

---

## Progressive Context Loading

避免：

一次性塞入大量上下文。

---

## Human Readable

本质：

就是 Markdown + YAML。

不是 DSL。

不是复杂 AST。

不是 Workflow Engine。

---

# 18. 与 AGENTS.md 的区别

社区目前通常：

| Format      | 用途             |
| ----------- | -------------- |
| `AGENTS.md` | 项目级 Agent 行为规范 |
| `SKILL.md`  | 可复用技能模块        |

---

## AGENTS.md

偏：

```text
Project-level behavior
```

例如：

* Coding style
* Repo conventions
* Team workflow

---

## SKILL.md

偏：

```text
Reusable capability package
```

例如：

* PDF extraction
* SQL optimization
* PR review
* Kubernetes debugging

---

# 19. 核心思想总结

Agent Skills 本质：

不是“Prompt”。

而是：

```text
Portable Procedural Context
```

即：

可移植的过程化知识包。

---

参考来源：

* [Agent Skills Specification](https://agentskills.io/specification?utm_source=chatgpt.com)
* [Agent Skills Overview](https://agentskills.io/?utm_source=chatgpt.com)
* [GitHub Repository](https://github.com/agentskills/agentskills?utm_source=chatgpt.com)
