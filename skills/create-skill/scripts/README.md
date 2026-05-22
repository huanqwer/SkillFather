# Scripts 说明

本目录包含 Skill Creator 的辅助脚本。

---

## validate-skill.py

**功能**：验证 Skill 目录结构和 SKILL.md 格式是否符合规范。

**用法**：
```bash
python validate-skill.py <skill-path>
```

**示例**：
```bash
python validate-skill.py ./skills/my-skill
```

**验证内容**：
- SKILL.md 文件是否存在
- YAML Frontmatter 格式是否正确
- name 字段是否符合规范
- description 字段是否符合规范
- 目录名与 name 字段是否一致

---

## eval-runner.py

**功能**：运行 Skill 的 Eval 测试用例，生成评估报告。

**用法**：
```bash
python eval-runner.py <skill-path> [output-path]
```

**示例**：
```bash
python eval-runner.py ./skills/my-skill
python eval-runner.py ./skills/my-skill ./reports/eval-report.json
```

**Eval 类型**：
- Trigger Eval：验证触发条件
- Success Eval：验证成功场景
- Failure Eval：验证失败场景
- Adversarial Eval：验证对抗性场景

**输出**：
- 控制台打印评估报告
- 生成 JSON 格式的详细报告

---

## skill-generator.py

**功能**：根据模板生成新的 Skill 目录结构。

**用法**：
```bash
python skill-generator.py <skill-name> <description> <author> [output-dir]
```

**示例**：
```bash
python skill-generator.py pdf-processing "处理PDF文件" "your-name" ./skills
```

**生成内容**：
- SKILL.md（基于模板）
- scripts/ 目录
- references/ 目录
- assets/ 目录
- eval-template.md
- workflow-template.md

---

## 依赖

所有脚本都需要 Python 3.7+。

额外依赖：
```bash
pip install pyyaml
```

---

## 注意事项

1. 脚本需要从 `skills/create-skill` 目录运行
2. 生成的 Skill 需要通过 `validate-skill.py` 验证
3. 建议在生成后运行 `eval-runner.py` 进行评估
