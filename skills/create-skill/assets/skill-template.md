---
name: skill-name

version: 1.0.0

description: |
  简洁描述该 Skill 的功能。
  必须包含：用户意图、同义表达、典型场景、上下文信号、排除条件。

category:
  - category-name

author: your-name

trigger:
  semantic:
    - 触发关键词1
    - 触发关键词2

  should_trigger_when:
    - 应该触发的情况1
    - 应该触发的情况2

  should_not_trigger_when:
    - 不应该触发的情况1
    - 不应该触发的情况2

inputs:
  - input1
  - input2

outputs:
  - output1
  - output2

dependencies:
  - dependency1

token_budget:
  soft_limit: 12000
  hard_limit: 24000

latency_budget:
  target_ms: 8000

risk_level: low

observability:
  enabled: true
  collect:
    - trigger_accuracy
    - completion_rate
    - token_usage

eval_strategy:
  methodology:
    - trigger-eval
    - execution-eval
    - adversarial-eval

  success_criteria:
    trigger_accuracy: ">= 90%"
    completion_rate: ">= 85%"

---

# 目标

描述该 Skill 的核心目标。

---

# 核心原则

列出该 Skill 遵循的核心原则。

---

# 工作流程

## Step 1：步骤名称

描述第一步的具体操作。

## Step 2：步骤名称

描述第二步的具体操作。

---

# 执行约束

禁止：
- 禁止事项1
- 禁止事项2

必须：
- 必须事项1
- 必须事项2

---

# 输出格式

描述输出结果的格式要求。

---

# 成功标准

定义成功的标准。
