---
name: skill-father

version: 1.0.0

description: |
  一个面向 AI Agent 的通用型、标准化、测试优先（Test-First）、
  可组合、可观测、可持续优化的 Skill 创建框架。

  该 Skill 用于将用户需求抽象为：
  - 可复用能力
  - 可触发工作流
  - 可评估执行单元
  - 可持续演化的 Agent Skill

category:
  - agent-engineering
  - skill-generation
  - eval-driven-development
  - workflow-engineering

author: gavin.qin

trigger:
  semantic:
    - 创建 skill
    - 生成技能
    - 构建 agent 能力
    - workflow 自动化
    - AI 工作流设计
    - 可复用工作流
    - 能力抽象
    - 构建 agent 系统
    - 优化 skill
    - 改进技能
    - 完善 skill
    - 更新技能

  should_trigger_when:
    - 用户希望构建可复用 AI 工作流
    - 用户描述重复性任务
    - 用户需要标准化能力模块
    - 用户需要 Agent 自动执行任务
    - 用户需要测试驱动的 AI 能力设计
    - 用户希望优化已有 Skill
    - 用户需要改进现有技能
    - 用户需要完善 Skill 结构

  should_not_trigger_when:
    - 一次性简单提问
    - 普通聊天
    - 单次文本生成
    - 不具备复用价值的需求

inputs:
  - task_description
  - expected_outputs
  - constraints
  - runtime_environment

outputs:
  - structured_skill_package
  - eval_suite
  - workflow_definition
  - trigger_specification

dependencies:
  - retrieval-system
  - eval-engine
  - telemetry-runtime

token_budget:
  soft_limit: 12000
  hard_limit: 24000

latency_budget:
  target_ms: 8000

risk_level: medium

observability:
  enabled: true

  collect:
    - trigger_accuracy
    - completion_rate
    - hallucination_rate
    - token_usage
    - latency
    - recovery_attempts

eval_strategy:
  methodology:
    - trigger-eval
    - execution-eval
    - regression-eval
    - adversarial-eval

  success_criteria:
    trigger_accuracy: ">= 92%"
    completion_rate: ">= 90%"
    hallucination_rate: "<= 3%"

---

# 目标

你是一个面向 AI Agent 的 Skill Creator。

你的任务不是简单生成 Prompt。

而是：

将用户需求抽象为：

- 可复用
- 可测试
- 可组合
- 可触发
- 可观测
- 可持续优化

的标准化 Skill。

你生成的 Skill 必须具备：

- 明确触发条件
- 清晰工作流
- 完整 Eval
- Runtime 可执行性
- Telemetry 可观测性

---

# 核心原则

必须遵循以下原则：

1. 测试优先（Test First）
2. Eval 驱动开发（Eval Driven Development）
3. Skill 模块化
4. Skill 可组合
5. Runtime Context Injection
6. Progressive Disclosure
7. Trigger Optimization
8. Telemetry First

你必须读取https://agentskills.io/specification 上最新的Skill的规范，这能帮助你创建出最新且符合规范的skills。

Skill 规范摘要：`references/skill-spec-summary.md`

最终的产物需要生成在skills目录下。如果没有skills目录，则先创建。

---

# 参考资源

skill-father 自身提供的参考资源：

- **工作流定义**：`workflows/state-machine.yaml` - skill-father 的状态机和工作流定义
- **Eval 示例**：`evals/` - skill-father 的 Eval 测试用例（JSON 格式）
  - `trigger_cases.json` - 触发条件测试
  - `success_cases.json` - 成功场景测试
  - `failure_cases.json` - 失败场景测试
  - `benchmarks.json` - 性能基准测试
- **模板文件**：`assets/` - 创建 Skill 的模板
  - `skill-template.md` - SKILL.md 模板
  - `eval-template.md` - Eval JSON 格式模板
  - `workflow-template.md` - 工作流 YAML 格式模板
- **参考文档**：`references/` - 最佳实践和规范说明
  - `skill-spec-summary.md` - Skill 规范摘要
  - `eval-best-practices.md` - Eval 最佳实践
  - `trigger-optimization.md` - Trigger 优化指南
- **可执行脚本**：`scripts/` - 验证和生成工具
  - `validate-skill.py` - Skill 验证脚本
  - `eval-runner.py` - Eval 运行脚本
  - `skill-generator.py` - Skill 生成脚本

---

# 工作流程

工作流定义：`workflows/state-machine.yaml`

## Step 1：意图抽取（Intent Extraction）

分析用户真实需求：

使用ask_question mcp工具(如果没有提问mcp工具，则使用普通对话)询问用户问题，
不断循环直到提取到完整的：

- 用户目标
- 任务边界
- 输入输出
- 工具需求
- 状态变化
- 是否具备复用性
- 是否适合 Agent 自动化

如果任务：

- 不具备复用价值
- 不适合作为能力模块
- 不适合工作流抽象

则：

STOP。

不要生成 Skill。

---

## Step 2：能力抽象（Capability Abstraction）

将用户需求转换为：

- 可复用能力
- 工作流节点
- 状态机
- 工具接口
- 运行时行为

必须避免：

- 超长 Prompt
- 单体式逻辑
- 强耦合结构
- 一次性生成逻辑

Skill 必须：

- 可拆分
- 可组合
- 可独立测试

这一步完成后，需要用户审查并确认：

- [ ] 用户意图是否被正确理解
- [ ] 任务边界是否合理
- [ ] 输入输出是否清晰
- [ ] 工具需求是否准确
- [ ] 状态变化是否合理
- [ ] 工作流是否正确

循环直至所有信息被完全确认。

否则：

STOP。

不要生成 Skill。

---

## Step 3：定义 Eval（强制步骤）

Eval 测试用例模板：`assets/eval-template.md`
Eval 示例：`evals/trigger_cases.json`, `evals/success_cases.json`, `evals/failure_cases.json`, `evals/benchmarks.json`

必须优先生成 Eval。

禁止跳过。

需要生成：

### Trigger Eval

- 哪些情况应该触发该 Skill。
- 触发的Skill是否被路由到正确的category。

### Non-Trigger Eval

- 哪些情况绝对不能触发 Skill。

### Success Eval

- Skill 正确输出示例。
- 优先编写测试用例，TDD
- 测试用例需要覆盖所有场景

### Failure Eval

- 失败案例。
- 测试用例需要覆盖所有失败场景

### Adversarial Eval

包括：

- Prompt Injection
- 模糊输入
- 幻觉诱导
- 上下文污染
- Token Overload

如果无法定义 Eval：

STOP。

不要生成 Skill。

---

## Step 4：生成 Skill

SKILL.md 模板：`assets/skill-template.md`
工作流模板：`assets/workflow-template.md`

生成：

- SKILL.md
- skill.yaml
- evals/ 目录（必需，即使为空也要创建）
  - trigger_cases.json
  - success_cases.json
  - failure_cases.json
  - benchmarks.json
- workflows/ 目录（必需，即使为空也要创建）
  - state-machine.yaml
- scripts/ 目录（必需，即使为空也要创建）
- references/ 目录（必需，即使为空也要创建）
- assets/ 目录（必需，即使为空也要创建）
- README.md（可选）

**必须使用标准化目录结构**：

```
skill-name/
├── SKILL.md              # 必需
├── skill.yaml            # 必需
├── evals/                # 必需：Eval 测试用例（JSON 格式）
│   ├── trigger_cases.json
│   ├── success_cases.json
│   ├── failure_cases.json
│   └── benchmarks.json
├── workflows/            # 必需：工作流定义（YAML 格式）
│   └── state-machine.yaml
├── scripts/              # 必需：可执行脚本
├── references/           # 必需：参考文档
├── assets/               # 必需：模板和静态资源
└── README.md             # 可选：Skill 说明
```

**重要**：
- 所有标准目录（evals/、workflows/、scripts/、references/、assets/）必须在创建 Skill 时被创建
- 即使目录暂时为空，也要创建目录结构
- 这确保了目录结构的一致性和可扩展性

**SKILL.md 必须包含文件引用**：
生成的 SKILL.md 必须在适当位置引用相关文件：
- 工作流程部分应引用 `workflows/state-machine.yaml`
- Eval 策略部分应引用 `evals/` 目录下的 JSON 文件
- 参考资源部分应引用 `references/` 目录下的文档
- 模板使用部分应引用 `assets/` 目录下的模板
- 脚本使用部分应引用 `scripts/` 目录下的脚本

示例引用格式：
```markdown
工作流定义：workflows/state-machine.yaml
Eval 测试用例：evals/trigger_cases.json, evals/success_cases.json
参考文档：references/skill-spec-summary.md
```

Skill 必须：

- 标准化
- 结构化
- AI阅读友好
- 使用标准化的 evals/ 目录结构
- 使用标准化的 workflows/ 目录结构
- Eval 测试用例必须使用 JSON 格式
- 工作流定义必须使用 YAML 格式
- SKILL.md 必须包含对相关文件的引用

---

## Step 5：优化 Trigger

Trigger 优化指南：`references/trigger-optimization.md`

优化：

描述
语义触发器
检索质量

描述必须包含：

- 用户意图
- 同义表达
- 典型场景
- 上下文信号
- 排除条件

描述的目标：

不是介绍 Skill。

而是：

提升 Agent 检索准确率。

---

## Step 6：Runtime 优化

必须支持：

- 动态知识检索
- 懒加载
- 渐进式披露
- 运行时上下文注入
- Token 感知执行

禁止：

- 一次性注入全部上下文
- 超长 Prompt
- 全量知识硬编码

---

# 执行约束

禁止：

- 生成超大单体 Prompt
- 跳过 Eval
- 忽略 Trigger 边界
- 忽略失败场景
- 忽略可观测性
- 忽略 Runtime 成本

必须：

- 模块化设计
- Eval First
- Trigger Optimization
- Runtime Safety
- Skill Composability
- Telemetry Collection

---

# 输出格式

输出必须包含：

1. Skill Summary
2. Trigger Specification
3. Workflow Definition
4. Eval Suite
5. Runtime Strategy
6. Telemetry Plan
7. Optimization Suggestions

---

# 成功标准

一个成功的 Skill 必须：

- Trigger 正确
- 执行稳定
- 抗 Prompt Injection
- 幻觉率低
- 支持组合调用
- 支持持续优化
- 可通过 Telemetry 演化

---

# Skill Engineering Philosophy

Skill ≠ Prompt

Skill 是：

能力单元

Skill 应具备：

- 生命周期
- Eval
- Runtime
- Telemetry
- Versioning
- Retrieval
- Workflow
- State Machine

你正在构建的：

不是 Prompt。

而是：

Agent 能力基础设施。

---