#!/usr/bin/env python3
"""
Skill 生成脚本

根据模板生成新的 Skill 目录结构。
"""

import os
import sys
import shutil
from pathlib import Path
from typing import Dict, Any


def copy_template(src: Path, dst: Path, replacements: Dict[str, str]):
    """复制模板文件并替换占位符"""
    content = src.read_text(encoding='utf-8')
    
    for key, value in replacements.items():
        content = content.replace(key, value)
    
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(content, encoding='utf-8')


def create_skill(skill_name: str, description: str, output_dir: Path):
    """创建新的 Skill"""
    skill_dir = output_dir / skill_name
    
    if skill_dir.exists():
        print(f"错误: 目录已存在: {skill_dir}")
        sys.exit(1)
    
    # 创建目录结构
    skill_dir.mkdir(parents=True)
    (skill_dir / "scripts").mkdir()
    (skill_dir / "references").mkdir()
    (skill_dir / "assets").mkdir()
    (skill_dir / "spec").mkdir()
    (skill_dir / "evals").mkdir()
    (skill_dir / "workflows").mkdir()
    
    # 替换占位符
    replacements = {
        "{{SKILL_NAME}}": skill_name,
        "{{DESCRIPTION}}": description,
    }
    
    # 从模板复制 SKILL.md
    template_path = Path(__file__).parent.parent / "assets" / "skill-template.md"
    if template_path.exists():
        copy_template(template_path, skill_dir / "SKILL.md", replacements)
    else:
        # 如果模板不存在，创建基本结构
        basic_skill = f"""---
name: {skill_name}
description: |
  {description}
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

---

# 执行约束

禁止：
- 禁止事项1
- 跳过强制约束定义（SDD）
- 跳过 Eval 定义（TDD）
- 使用自然语言替代 JSON 定义 spec 和 evals

必须：
- 必须事项1
- SDD：先定义 JSON 强制约束（spec/），再生成 Skill
- TDD：先定义 JSON Eval（evals/），再生成 Skill

---

# 输出格式

描述输出结果的格式要求。

---

# 成功标准

定义成功的标准。

- 强制约束已定义（spec/ JSON 文件完整且有效）
- Eval 已定义（evals/ JSON 文件完整且有效）
"""
        (skill_dir / "SKILL.md").write_text(basic_skill, encoding='utf-8')
    
    # 复制其他模板文件
    eval_template = Path(__file__).parent.parent / "assets" / "eval-template.md"
    if eval_template.exists():
        copy_template(eval_template, skill_dir / "assets" / "eval-template.md", replacements)
    
    workflow_template = Path(__file__).parent.parent / "assets" / "workflow-template.md"
    if workflow_template.exists():
        copy_template(workflow_template, skill_dir / "assets" / "workflow-template.md", replacements)
    
    # 生成 spec/ JSON 文件
    _generate_spec_files(skill_dir, skill_name, description)
    
    # 生成 evals/ JSON 文件
    _generate_eval_files(skill_dir, skill_name)
    
    print(f"Skill 创建成功: {skill_dir}")
    print(f"目录结构:")
    print(f"  {skill_dir}/")
    print(f"    SKILL.md")
    print(f"    spec/ (constraints.json, schema.json, transitions.json)")
    print(f"    evals/ (trigger_cases.json, success_cases.json, failure_cases.json)")
    print(f"    workflows/")
    print(f"    scripts/")
    print(f"    references/")
    print(f"    assets/")


def _generate_spec_files(skill_dir: Path, skill_name: str, description: str):
    """生成 spec/ 目录下的 JSON 文件"""
    import json
    
    # spec/constraints.json
    constraints = {
        "skill_name": skill_name,
        "version": "1.0.0",
        "constraints": {
            "must": [
                {"id": "must-001", "rule": "必须先验证输入再执行", "validation": "input_validation_required"}
            ],
            "must_not": [
                {"id": "must-not-001", "rule": "禁止跳过输入验证", "validation": "no_skip_validation"}
            ],
            "preconditions": [
                {"id": "pre-001", "condition": "用户意图已确认", "check": "intent_confirmed"}
            ],
            "postconditions": [
                {"id": "post-001", "condition": "输出包含所有必需字段", "check": "output_complete"}
            ]
        }
    }
    (skill_dir / "spec" / "constraints.json").write_text(
        json.dumps(constraints, indent=2, ensure_ascii=False), encoding='utf-8')
    
    # spec/schema.json
    schema = {
        "skill_name": skill_name,
        "input_schema": {
            "type": "object",
            "required": ["task_description"],
            "properties": {
                "task_description": {"type": "string"}
            }
        },
        "output_schema": {
            "type": "object",
            "required": ["result"],
            "properties": {
                "result": {"type": "string"}
            }
        }
    }
    (skill_dir / "spec" / "schema.json").write_text(
        json.dumps(schema, indent=2, ensure_ascii=False), encoding='utf-8')
    
    # spec/transitions.json
    transitions = {
        "skill_name": skill_name,
        "transitions": [
            {"from": "idle", "to": "processing", "condition": "request_received", "required_checks": ["input_valid"]}
        ]
    }
    (skill_dir / "spec" / "transitions.json").write_text(
        json.dumps(transitions, indent=2, ensure_ascii=False), encoding='utf-8')


def _generate_eval_files(skill_dir: Path, skill_name: str):
    """生成 evals/ 目录下的 JSON 文件"""
    import json
    
    # evals/trigger_cases.json
    trigger_cases = {
        "skill_name": skill_name,
        "eval_type": "trigger",
        "description": "验证 Skill 的触发条件",
        "should_trigger": [],
        "should_not_trigger": [],
        "success_criteria": {
            "trigger_accuracy": ">= 92%",
            "false_positive_rate": "<= 5%",
            "false_negative_rate": "<= 8%"
        }
    }
    (skill_dir / "evals" / "trigger_cases.json").write_text(
        json.dumps(trigger_cases, indent=2, ensure_ascii=False), encoding='utf-8')
    
    # evals/success_cases.json
    success_cases = {
        "skill_name": skill_name,
        "eval_type": "success",
        "description": "验证 Skill 在正常情况下的正确输出",
        "test_cases": [],
        "success_criteria": {
            "completion_rate": ">= 90%",
            "output_quality": "符合 Skill 规范",
            "workflow_completeness": "7 个步骤全部执行"
        }
    }
    (skill_dir / "evals" / "success_cases.json").write_text(
        json.dumps(success_cases, indent=2, ensure_ascii=False), encoding='utf-8')
    
    # evals/failure_cases.json
    failure_cases = {
        "skill_name": skill_name,
        "eval_type": "failure",
        "description": "验证 Skill 在异常情况下的处理能力",
        "test_cases": [],
        "success_criteria": {
            "error_handling": "优雅处理异常情况",
            "stop_condition": "在应该停止时正确停止",
            "information_collection": "在需要更多信息时正确询问"
        }
    }
    (skill_dir / "evals" / "failure_cases.json").write_text(
        json.dumps(failure_cases, indent=2, ensure_ascii=False), encoding='utf-8')


def main():
    if len(sys.argv) < 3:
        print("用法: python skill-generator.py <skill-name> <description> [output-dir]")
        print("示例: python skill-generator.py pdf-processing '处理PDF文件' ./skills")
        sys.exit(1)
    
    skill_name = sys.argv[1]
    description = sys.argv[2]
    output_dir = Path(sys.argv[3]) if len(sys.argv) > 3 else Path.cwd() / "skills"
    
    create_skill(skill_name, description, output_dir)


if __name__ == "__main__":
    main()
