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

version: 1.0.0

description: |
  {description}

category:
  - category-name

author: {author}

trigger:
  semantic:
    - 触发关键词1
    - 触发关键词2

  should_trigger_when:
    - 应该触发的情况1

  should_not_trigger_when:
    - 不应该触发的情况1

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

---

# 执行约束

禁止：
- 禁止事项1

必须：
- 必须事项1

---

# 输出格式

描述输出结果的格式要求。

---

# 成功标准

定义成功的标准。
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
