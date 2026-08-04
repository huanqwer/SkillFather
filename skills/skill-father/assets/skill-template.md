---
name: skill-name
description: |
  简洁描述该 Skill 的功能。
  必须包含：用户意图、同义表达、典型场景、上下文信号、排除条件。
---

# 目标

描述该 Skill 的核心目标。

---

# 核心原则

1. 规格驱动开发（Spec Driven Development, SDD）
2. 测试驱动开发（Test Driven Development, TDD）
3. JSON 强制约束优先于自然语言提示词
4. Skill 模块化
5. Skill 可组合

---

# 强制约束

强制约束使用 JSON 格式定义，存储在 `spec/` 目录下。

JSON 相较于自然语言提示词具有更强的约束力：机器可解析、无歧义、可程序化验证、可组合执行。

本 Skill 的强制约束定义在以下 JSON spec 文件中：

- **行为约束**：`spec/constraints.json` — 定义 must / must_not / preconditions / postconditions
- **输入输出 Schema**：`spec/schema.json` — 定义 input_schema 和 output_schema
- **状态转换规则**：`spec/transitions.json` — 定义状态机转换规则（与 workflows/state-machine.yaml 对应）

SKILL.md 中的自然语言描述仅为人类可读的补充说明，以 `spec/` 下的 JSON 文件为准。

---

# 工作流程

## Step 1：步骤名称

描述第一步的具体操作。

## Step 2：步骤名称

描述第二步的具体操作。

---

# 标准化目录结构

必须使用以下目录结构：

```
skill-name/
├── SKILL.md              # 必需：Skill 主文件（必须包含"强制约束"模块）
├── skill.yaml            # 必需：机器可读配置
├── spec/                 # 必需：强制约束（SDD，JSON 格式）
│   ├── constraints.json  #   行为约束：must / must_not / preconditions / postconditions
│   ├── schema.json       #   输入输出 JSON Schema
│   └── transitions.json  #   状态转换规则（机器可读）
├── evals/                # 必需：Eval 测试用例（TDD，JSON 格式）
│   ├── trigger_cases.json
│   ├── success_cases.json
│   ├── failure_cases.json
│   └── benchmarks.json
├── workflows/            # 必需：工作流定义（YAML 格式）
│   └── state-machine.yaml
├── scripts/              # 可选：可执行脚本
├── references/           # 可选：参考文档
├── assets/               # 可选：模板和静态资源
└── README.md             # 可选：Skill 说明
```

---

# 执行约束

禁止：
- 禁止事项1
- 禁止事项2
- 跳过强制约束定义（SDD）
- 跳过 Eval 定义（TDD）
- 使用自然语言替代 JSON 定义 spec 和 evals

必须：
- 必须事项1
- 必须事项2
- SDD：先定义 JSON 强制约束（spec/），再生成 Skill
- TDD：先定义 JSON Eval（evals/），再生成 Skill
- 使用标准化的 spec/ 目录结构（JSON 格式）
- 使用标准化的 evals/ 目录结构（JSON 格式）
- 使用标准化的 workflows/ 目录结构（YAML 格式）
- SKILL.md 必须包含"强制约束"模块并引用 spec/ 下的 JSON 文件

---

# 输出格式

描述输出结果的格式要求。

---

# 成功标准

定义成功的标准。

- 强制约束已定义（spec/ JSON 文件完整且有效）
- Eval 已定义（evals/ JSON 文件完整且有效）
