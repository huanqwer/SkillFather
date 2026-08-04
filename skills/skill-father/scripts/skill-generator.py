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


def create_skill(skill_name: str, description: str, author: str, output_dir: Path):
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
        "{{AUTHOR}}": author,
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
    
    print(f"Skill 创建成功: {skill_dir}")
    print(f"目录结构:")
    print(f"  {skill_dir}/")
    print(f"    SKILL.md")
    print(f"    scripts/")
    print(f"    references/")
    print(f"    assets/")


def main():
    if len(sys.argv) < 4:
        print("用法: python skill-generator.py <skill-name> <description> <author> [output-dir]")
        print("示例: python skill-generator.py pdf-processing '处理PDF文件' 'your-name' ./skills")
        sys.exit(1)
    
    skill_name = sys.argv[1]
    description = sys.argv[2]
    author = sys.argv[3]
    output_dir = Path(sys.argv[4]) if len(sys.argv) > 4 else Path.cwd() / "skills"
    
    create_skill(skill_name, description, author, output_dir)


if __name__ == "__main__":
    main()
