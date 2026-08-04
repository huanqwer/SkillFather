# Eval 最佳实践

## SDD + TDD 方法论

SkillFather 采用 **SDD（Spec Driven Development）+ TDD（Test Driven Development）** 双驱动开发模式：

1. **SDD（规格驱动开发）**：先定义 JSON 强制约束（`spec/` 目录），明确 Skill 的行为规格
2. **TDD（测试驱动开发）**：再定义 JSON Eval 测试用例（`evals/` 目录），明确成功标准
3. **最后生成 Skill**：基于 spec 和 evals 生成 SKILL.md 和其他文件

### 为什么 JSON > Prompt？

JSON 相较于自然语言提示词具有更强的约束力：

- **机器可解析**：JSON 是结构化数据，可被程序直接解析和验证，不依赖 LLM 的"理解"
- **无歧义性**：自然语言存在多重解读，JSON 的字段和值是精确的
- **可程序化验证**：JSON spec 可以通过脚本自动校验，Prompt 只能靠人工审查
- **可组合执行**：JSON 约束可以被 runtime 直接加载和执行，Prompt 只能被"建议遵守"
- **可量化测试**：JSON evals 可以通过断言精确判断通过/失败，Prompt evals 依赖主观判断

因此：
- **Spec 必须使用 JSON**：`spec/constraints.json`、`spec/schema.json`、`spec/transitions.json`
- **Evals 必须使用 JSON**：`evals/trigger_cases.json`、`evals/success_cases.json` 等
- **SKILL.md 中的自然语言描述仅为人类可读的补充说明**，以 JSON 文件为准

---

## Eval 驱动开发（Eval Driven Development）

Eval 驱动开发是创建高质量 Skill 的核心方法论。

在 SkillFather 中，Eval 驱动开发与 SDD 紧密结合：
- SDD 定义"Skill 应该做什么"（spec/）
- TDD 定义"如何验证 Skill 做对了"（evals/）
- 两者都使用 JSON 格式，确保机器可解析、可验证

---

## 为什么 Eval 优先？

1. **明确成功标准**：在编写 Skill 之前先定义什么是"成功"
2. **覆盖边界情况**：提前考虑失败场景和异常情况
3. **可验证性**：每个 Skill 都有明确的测试标准
4. **持续优化**：通过 Eval 数据持续改进 Skill

---

## Eval 类型

### 1. Trigger Eval

**目的**：验证 Skill 是否在正确的时间被触发

**应该触发的情况**：
- 用户明确表达相关需求
- 上下文包含关键信号
- 任务匹配 Skill 的能力范围

**不应该触发的情况**：
- 不相关的任务
- 一次性简单提问
- 普通聊天

### 2. Success Eval

**目的**：验证 Skill 在正常情况下的正确性

**包含内容**：
- 正确输出示例
- 边界情况处理
- 性能要求

**测试用例设计原则**：
- 覆盖所有主要场景
- 包含典型输入
- 包含边界输入

### 3. Failure Eval

**目的**：验证 Skill 在异常情况下的处理能力

**包含内容**：
- 失败案例
- 错误处理
- 降级策略

**测试用例设计原则**：
- 覆盖所有失败场景
- 验证错误信息的清晰性
- 验证恢复机制

### 4. Adversarial Eval

**目的**：验证 Skill 的安全性和鲁棒性

**包含内容**：

#### Prompt Injection
- 尝试注入恶意指令
- 尝试覆盖系统指令
- 尝试获取敏感信息

#### 模糊输入
- 不明确的输入
- 歧义输入
- 格式错误的输入

#### 幻觉诱导
- 诱导生成虚假信息
- 诱导生成不存在的内容
- 诱导过度自信

#### 上下文污染
- 注入无关上下文
- 注入冲突信息
- 注入过时信息

#### Token Overload
- 超长输入
- 重复内容
- 嵌套结构

---

## Eval 编写流程

### Step 1: 定义成功标准

明确：
- 什么样的输出是正确的？
- 什么样的输出是错误的？
- 性能要求是什么？

### Step 2: 编写测试用例

为每个场景编写具体的测试用例：
- 输入
- 预期输出
- 判断标准

### Step 3: 覆盖边界情况

考虑：
- 空输入
- 超长输入
- 特殊字符
- 并发场景

### Step 4: 编写对抗性测试

模拟恶意用户和异常情况

---

## Eval 指标

### 触发准确率（Trigger Accuracy）

```
触发准确率 = 正确触发次数 / 总触发次数
```

目标：>= 92%

### 完成率（Completion Rate）

```
完成率 = 成功完成任务次数 / 总尝试次数
```

目标：>= 90%

### 幻觉率（Hallucination Rate）

```
幻觉率 = 产生幻觉次数 / 总输出次数
```

目标：<= 3%

---

## 无法定义 Eval 的情况

如果无法为 Skill 定义清晰的 Eval，说明：

1. Skill 的目标不明确
2. Skill 的边界不清晰
3. Skill 不适合作为可复用能力模块

**在这种情况下，不要生成 Skill。**

---

## 持续优化

通过收集 Eval 数据：

1. 识别失败模式
2. 优化 Trigger 条件
3. 改进工作流
4. 更新 Eval 用例

形成闭环：
```
定义 JSON Spec（SDD） -> 定义 JSON Eval（TDD） -> 实现 Skill -> 运行 Eval -> 分析结果 -> 优化 Skill
```
