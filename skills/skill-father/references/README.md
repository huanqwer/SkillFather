# References 目录

本目录包含 skill-father 的参考文档和最佳实践指南。

---

## 目录结构

```
references/
├── skill-spec-summary.md      # Skill 规范摘要
├── eval-best-practices.md     # Eval 最佳实践
├── trigger-optimization.md    # Trigger 优化指南
└── README.md                  # 本文件
```

**注意**：skill-father 的 Eval 定义已移至 `evals/` 目录，使用 JSON 格式。

---

## 文件说明

### skill-spec-summary.md

**用途**：Skill 规范的快速参考

**包含内容**：
- 核心概念和定义
- 目录结构要求
- SKILL.md 格式规范
- YAML Frontmatter 字段说明
- name 和 description 字段规则
- 渐进式披露模型
- 推荐大小限制
- 验证工具使用
- 设计理念

**使用场景**：
- 创建 Skill 时快速查阅规范
- 验证 Skill 格式是否符合标准
- 了解 Skill 的设计原则

**关键信息**：
- Skill 本质：包含 SKILL.md 的目录
- 必需字段：name、description
- 可选字段：license、compatibility、metadata、allowed-tools
- name 规则：1-64 字符，仅允许小写字母、数字、连字符
- description 规则：1-1024 字符，描述功能和触发场景

---

### eval-best-practices.md

**用途**：Eval 驱动开发的方法论指南

**包含内容**：
- Eval 驱动开发的核心思想
- 为什么 Eval 优先
- Eval 类型详解（Trigger、Success、Failure、Adversarial）
- Eval 编写流程
- Eval 指标（触发准确率、完成率、幻觉率）
- 持续优化方法

**使用场景**：
- 为 Skill 定义 Eval 时参考
- 理解 Eval 驱动开发流程
- 设计测试用例

**核心原则**：
- Eval 优先：在编写 Skill 之前先定义 Eval
- 覆盖边界：考虑所有成功和失败场景
- 对抗性测试：验证安全性和鲁棒性
- 持续优化：通过 Eval 数据改进 Skill

**Eval 指标**：
- 触发准确率：>= 92%
- 完成率：>= 90%
- 幻觉率：<= 3%

---

### trigger-optimization.md

**用途**：Trigger 优化的详细指南

**包含内容**：
- Trigger 的目标（提升检索准确率）
- description 优化（用户意图、同义表达、典型场景、上下文信号、排除条件）
- semantic trigger 优化（关键词选择原则）
- should_trigger_when 优化
- should_not_trigger_when 优化
- 检索质量优化（Precision 和 Recall）
- Trigger 评估方法
- 常见问题解答

**使用场景**：
- 优化 Skill 的 description
- 设计触发条件
- 提升检索准确率

**description 优化要点**：
- 包含用户意图
- 包含同义表达
- 包含典型场景
- 包含上下文信号
- 包含排除条件
- 目标是提升检索准确率，而非介绍 Skill

---

## 使用指南

### Agent 使用建议

1. **创建 Skill 时**：
   - 先读取 `skill-spec-summary.md` 了解规范
   - 参考 `eval-best-practices.md` 定义 Eval
   - 使用 `trigger-optimization.md` 优化 Trigger

2. **优化 Skill 时**：
   - 参考 `eval-best-practices.md` 的方法论
   - 使用 `trigger-optimization.md` 改进检索准确率
   - 参考 `evals/` 目录中的 JSON 格式 Eval 示例

3. **验证 Skill 时**：
   - 使用 `skill-spec-summary.md` 检查格式
   - 使用 `eval-best-practices.md` 验证 Eval 完整性
   - 使用 `trigger-optimization.md` 验证 Trigger 质量

### 文件引用

在 SKILL.md 中引用参考文档：
```markdown
参见规范：references/skill-spec-summary.md
参考 Eval 最佳实践：references/eval-best-practices.md
优化 Trigger：references/trigger-optimization.md
参考 Eval 示例：evals/trigger_cases.json
参考工作流示例：workflows/state-machine.yaml
```

---

## 文件大小限制

遵循渐进式披露原则：
- 每个文件 < 500 行
- 每个文件 < 5000 tokens
- 按需加载，避免一次性注入全部上下文

---

## 注意事项

- 参考文档应保持简洁，避免过长
- 参考文档应结构清晰，易于查找
- 参考文档应包含具体示例
- 参考文档应支持按需加载
