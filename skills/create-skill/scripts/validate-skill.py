#!/usr/bin/env python3
"""
Skill 验证脚本

验证 Skill 目录结构和 SKILL.md 格式是否符合规范。
"""

import os
import sys
import re
from pathlib import Path

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


def validate_skill_name(name: str) -> tuple[bool, str]:
    """验证 Skill 名称是否符合规范"""
    if not name:
        return False, "名称不能为空"
    
    if len(name) < 1 or len(name) > 64:
        return False, "名称长度必须在 1-64 字符之间"
    
    if not re.match(r'^[a-z0-9]([a-z0-9-]*[a-z0-9])?$', name):
        return False, "名称只能包含小写字母、数字和连字符，不能以连字符开头或结尾，不能包含连续连字符"
    
    return True, "名称格式正确"


def validate_description(description: str) -> tuple[bool, str]:
    """验证描述是否符合规范"""
    if not description:
        return False, "描述不能为空"
    
    if len(description) < 1 or len(description) > 1024:
        return False, "描述长度必须在 1-1024 字符之间"
    
    return True, "描述格式正确"


def validate_frontmatter(frontmatter: dict) -> list[str]:
    """验证 YAML Frontmatter"""
    errors = []
    
    # 检查必需字段
    if 'name' not in frontmatter:
        errors.append("缺少必需字段: name")
    else:
        valid, msg = validate_skill_name(frontmatter['name'])
        if not valid:
            errors.append(f"name 字段错误: {msg}")
    
    if 'description' not in frontmatter:
        errors.append("缺少必需字段: description")
    else:
        valid, msg = validate_description(frontmatter['description'])
        if not valid:
            errors.append(f"description 字段错误: {msg}")
    
    return errors


def validate_skill_file(skill_path: Path) -> list[str]:
    """验证单个 Skill 文件"""
    errors = []
    
    # 检查 SKILL.md 是否存在
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        errors.append(f"缺少必需文件: SKILL.md")
        return errors
    
    # 读取文件内容
    content = skill_md.read_text()
    
    # 检查是否包含 YAML Frontmatter
    if not content.startswith('---'):
        errors.append("SKILL.md 必须以 YAML Frontmatter 开头")
        return errors
    
    # 提取 Frontmatter
    try:
        frontmatter_end = content.find('---', 3)
        if frontmatter_end == -1:
            errors.append("YAML Frontmatter 格式错误：缺少结束标记")
            return errors
        
        frontmatter_text = content[3:frontmatter_end]
        
        if HAS_YAML:
            frontmatter = yaml.safe_load(frontmatter_text)
            
            if not isinstance(frontmatter, dict):
                errors.append("YAML Frontmatter 必须是字典格式")
                return errors
            
            # 验证 Frontmatter
            errors.extend(validate_frontmatter(frontmatter))
            
            # 检查目录名与 name 字段是否一致
            if 'name' in frontmatter:
                if skill_path.name != frontmatter['name']:
                    errors.append(f"目录名 '{skill_path.name}' 与 name 字段 '{frontmatter['name']}' 不一致")
        else:
            # 没有 yaml 时进行基本验证
            errors.append("警告: 未安装 pyyaml，跳过 YAML Frontmatter 详细验证")
            # 简单检查是否包含 name 和 description
            if 'name:' not in frontmatter_text:
                errors.append("缺少必需字段: name")
            if 'description:' not in frontmatter_text:
                errors.append("缺少必需字段: description")
    
    except Exception as e:
        errors.append(f"解析错误: {e}")
    
    return errors


def validate_skill_directory(skill_path: Path) -> list[str]:
    """验证 Skill 目录结构"""
    errors = []
    
    # 检查目录是否存在
    if not skill_path.exists():
        errors.append(f"目录不存在: {skill_path}")
        return errors
    
    if not skill_path.is_dir():
        errors.append(f"路径不是目录: {skill_path}")
        return errors
    
    # 验证 SKILL.md
    errors.extend(validate_skill_file(skill_path))
    
    # 检查可选目录
    optional_dirs = ['scripts', 'references', 'assets']
    for dir_name in optional_dirs:
        dir_path = skill_path / dir_name
        if dir_path.exists() and not dir_path.is_dir():
            errors.append(f"{dir_name} 必须是目录")
    
    return errors


def main():
    if len(sys.argv) < 2:
        print("用法: python validate-skill.py <skill-path>")
        sys.exit(1)
    
    skill_path = Path(sys.argv[1])
    
    errors = validate_skill_directory(skill_path)
    
    if errors:
        print(f"验证失败，发现 {len(errors)} 个错误：")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)
    else:
        print("验证通过！Skill 符合规范。")
        sys.exit(0)


if __name__ == "__main__":
    main()
