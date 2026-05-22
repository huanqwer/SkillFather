# Skill 规范摘要

## 核心概念

Agent Skills 是一种开放标准，用于给 AI Agent 提供可复用的能力、工作流和领域知识。

一个 Skill 本质上是一个包含 `SKILL.md` 的目录。

---

## 目录结构

```
skill-name/
├── SKILL.md          # 必需
├── scripts/          # 可选：可执行代码
├── references/       # 可选：额外文档
├── assets/           # 可选：静态资源
└── ...
```

---

## SKILL.md 格式

### YAML Frontmatter（必需）

#### 必需字段

| 字段 | 说明 |
|-----|------|
| `name` | Skill 名称（1-64字符，仅允许小写字母、数字、连字符） |
| `description` | Skill 描述（1-1024字符，描述功能和触发场景） |

#### 可选字段

| 字段 | 说明 |
|-----|------|
| `license` | License 信息 |
| `compatibility` | 环境兼容性说明 |
| `metadata` | 任意 Key-Value Metadata |
| `allowed-tools` | 允许调用的工具（实验性） |

### Markdown Body

无强制格式限制，推荐包含：
- Step-by-step Instructions
- Input / Output Examples
- Edge Cases
- Failure Handling
- Constraints

---

## name 字段规则

- 长度：1~64
- 仅允许：`a-z`、`0-9`、`-`
- 不能以 `-` 开头或结尾
- 不能包含连续 `--`
- 必须与父目录名一致

---

## description 字段规则

- 长度：1~1024
- 必须非空
- 应描述：Skill 做什么、什么时候使用

---

## 渐进式披露模型

### Stage 1 — Discovery
Agent 启动时只读取 `name` 和 `description`，用于判断是否激活该 Skill。

### Stage 2 — Activation
任务匹配后加载整个 `SKILL.md`。

### Stage 3 — Resource Loading
只有真正需要时才读取 `scripts/`、`references/`、`assets/`。

---

## 推荐大小限制

| 部分 | 推荐限制 |
|-----|---------|
| Metadata | ~100 tokens |
| SKILL.md | < 5000 tokens |
| File Length | < 500 lines |

---

## 文件引用

推荐使用相对路径。

避免深层嵌套引用链，推荐：
```
SKILL.md -> references/*
```

而不是：
```
A -> B -> C -> D
```

---

## 验证

官方验证工具：
```bash
skills-ref validate ./my-skill
```

---

## 设计理念

- **轻量化**：只有 `SKILL.md` 是强制的
- **可移植**：可跨不同 Agent Runtime 使用
- **渐进式上下文加载**：避免一次性塞入大量上下文
- **人类可读**：本质是 Markdown + YAML，不是 DSL

---

## 与 AGENTS.md 的区别

| Format | 用途 |
|--------|------|
| `AGENTS.md` | 项目级 Agent 行为规范 |
| `SKILL.md` | 可复用技能模块 |
