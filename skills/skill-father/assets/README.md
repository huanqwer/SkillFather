# Assets 目录

本目录包含 skill-father 的模板文件和静态资源。

---

## 目录结构

```
assets/
├── skill-template.md      # Skill 模板
├── eval-template.md       # Eval 测试模板
├── workflow-template.md   # 工作流模板
└── README.md              # 本文件
```

---

## 文件说明

### skill-template.md

**用途**：创建新 Skill 的基础模板

**包含内容**：
- YAML Frontmatter 模板（name、description、category、trigger 等）
- Markdown Body 结构（目标、核心原则、工作流程、执行约束等）
- 完整的字段说明和示例

**使用场景**：
- 使用 `scripts/skill-generator.py` 创建新 Skill 时会自动使用此模板
- 手动创建 Skill 时可作为参考

**关键字段**：
- `name`：Skill 名称（必须符合规范）
- `description`：Skill 描述（包含用户意图、触发场景、排除条件）
- `trigger`：触发条件（semantic、should_trigger_when、should_not_trigger_when）
- `eval_strategy`：评估策略（methodology、success_criteria）

---

### eval-template.md

**用途**：Eval 测试用例模板（引导使用 JSON 格式）

**包含内容**：
- 标准化 Eval 文件结构说明
- trigger_cases.json 模板
- success_cases.json 模板
- failure_cases.json 模板
- benchmarks.json 模板
- Adversarial Eval 集成方式

**使用场景**：
- 了解 Eval 的 JSON 格式规范
- 参考 JSON 模板创建 Eval 文件
- 遵循测试优先（Test First）原则

**重要提示**：
- Eval 测试用例必须使用 JSON 格式
- 存储在 `evals/` 目录下
- 参考模板了解具体格式要求

---

### workflow-template.md

**用途**：工作流定义模板（引导使用 YAML 格式）

**包含内容**：
- 标准化工作流文件结构说明
- state-machine.yaml 模板
- 状态机定义（状态、转换、条件、动作）
- 错误处理和遥测配置
- Mermaid 工作流图（可选）

**使用场景**：
- 了解工作流的 YAML 格式规范
- 参考 YAML 模板创建工作流文件
- 定义清晰的状态转换

**重要提示**：
- 工作流定义必须使用 YAML 格式
- 存储在 `workflows/state-machine.yaml`
- 参考模板了解具体格式要求

---

## 使用指南

### Agent 使用建议

1. **创建新 Skill 时**：
   - 读取 `skill-template.md` 了解标准格式
   - 使用 `scripts/skill-generator.py` 自动生成目录结构
   - 根据需求修改模板内容

2. **定义 Eval 时**：
   - 读取 `eval-template.md` 了解 JSON 格式规范
   - 在 `evals/` 目录下创建 JSON 文件
   - 遵循测试优先原则

3. **设计工作流时**：
   - 读取 `workflow-template.md` 了解 YAML 格式规范
   - 在 `workflows/` 目录下创建 state-machine.yaml
   - 定义清晰的状态转换

### 文件引用

在 SKILL.md 中引用模板：
```markdown
参见模板：assets/skill-template.md
使用工作流模板：assets/workflow-template.md
定义 Eval：assets/eval-template.md
```

---

## 注意事项

- 模板文件应保持简洁，避免过长
- 模板应包含完整的字段说明
- 模板应遵循 Skill 规范
- 模板应支持渐进式披露（Progressive Disclosure）
