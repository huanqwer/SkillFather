# Assets 目录

本目录包含 skill-creator 的模板文件和静态资源。

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

**用途**：定义 Skill 的 Eval 测试用例

**包含内容**：
- Trigger Eval：应该/不应该触发的情况
- Success Eval：正确输出示例和测试用例
- Failure Eval：失败案例和处理
- Adversarial Eval：对抗性测试（Prompt Injection、模糊输入、幻觉诱导等）

**使用场景**：
- 为新 Skill 定义完整的 Eval 测试
- 遵循测试优先（Test First）原则

**Eval 类型**：
1. **Trigger Eval**：验证触发条件
2. **Success Eval**：验证成功场景
3. **Failure Eval**：验证失败场景
4. **Adversarial Eval**：验证安全性和鲁棒性

---

### workflow-template.md

**用途**：定义 Skill 的工作流和状态机

**包含内容**：
- Mermaid 工作流图
- 状态机定义（状态、转换、动作）
- 执行步骤说明

**使用场景**：
- 为 Skill 定义清晰的工作流程
- 支持状态管理和错误处理

**状态机元素**：
- 状态：idle、processing、success、failure
- 转换：状态之间的触发条件和动作
- 执行步骤：初始化、执行、完成

---

## 使用指南

### Agent 使用建议

1. **创建新 Skill 时**：
   - 读取 `skill-template.md` 了解标准格式
   - 使用 `scripts/skill-generator.py` 自动生成目录结构
   - 根据需求修改模板内容

2. **定义 Eval 时**：
   - 读取 `eval-template.md` 了解 Eval 类型
   - 为每个 Skill 定义完整的测试用例
   - 遵循测试优先原则

3. **设计工作流时**：
   - 读取 `workflow-template.md` 了解状态机模式
   - 使用 Mermaid 图可视化工作流
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
