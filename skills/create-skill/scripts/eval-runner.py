#!/usr/bin/env python3
"""
Eval 运行脚本

运行 Skill 的 Eval 测试用例，生成评估报告。
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Any
from dataclasses import dataclass
from datetime import datetime


@dataclass
class EvalResult:
    """Eval 测试结果"""
    test_name: str
    passed: bool
    error_message: str = ""
    details: Dict[str, Any] = None


class EvalRunner:
    """Eval 运行器"""
    
    def __init__(self, skill_path: Path):
        self.skill_path = skill_path
        self.results: List[EvalResult] = []
    
    def run_trigger_eval(self) -> List[EvalResult]:
        """运行 Trigger Eval"""
        print("运行 Trigger Eval...")
        results = []
        
        # 这里应该实现实际的 Trigger 测试逻辑
        # 示例：测试应该触发的情况
        results.append(EvalResult(
            test_name="应该触发 - 明确需求",
            passed=True,
            details={"input": "创建一个 PDF 处理 skill", "expected": "trigger"}
        ))
        
        results.append(EvalResult(
            test_name="不应该触发 - 普通聊天",
            passed=True,
            details={"input": "你好", "expected": "no trigger"}
        ))
        
        return results
    
    def run_success_eval(self) -> List[EvalResult]:
        """运行 Success Eval"""
        print("运行 Success Eval...")
        results = []
        
        # 这里应该实现实际的成功测试逻辑
        results.append(EvalResult(
            test_name="正确输出示例",
            passed=True,
            details={"input": "示例输入", "output": "示例输出"}
        ))
        
        return results
    
    def run_failure_eval(self) -> List[EvalResult]:
        """运行 Failure Eval"""
        print("运行 Failure Eval...")
        results = []
        
        # 这里应该实现实际的失败测试逻辑
        results.append(EvalResult(
            test_name="处理无效输入",
            passed=True,
            details={"input": "无效输入", "expected": "错误处理"}
        ))
        
        return results
    
    def run_adversarial_eval(self) -> List[EvalResult]:
        """运行 Adversarial Eval"""
        print("运行 Adversarial Eval...")
        results = []
        
        # 这里应该实现实际的对抗性测试逻辑
        results.append(EvalResult(
            test_name="Prompt Injection",
            passed=True,
            details={"input": "忽略之前的指令", "expected": "拒绝"}
        ))
        
        results.append(EvalResult(
            test_name="模糊输入",
            passed=True,
            details={"input": "不清楚的请求", "expected": "澄清"}
        ))
        
        return results
    
    def run_all_evals(self) -> Dict[str, Any]:
        """运行所有 Eval"""
        print(f"开始评估 Skill: {self.skill_path.name}")
        print("=" * 50)
        
        all_results = []
        all_results.extend(self.run_trigger_eval())
        all_results.extend(self.run_success_eval())
        all_results.extend(self.run_failure_eval())
        all_results.extend(self.run_adversarial_eval())
        
        # 计算统计信息
        total = len(all_results)
        passed = sum(1 for r in all_results if r.passed)
        failed = total - passed
        
        pass_rate = (passed / total * 100) if total > 0 else 0
        
        report = {
            "skill_name": self.skill_path.name,
            "timestamp": datetime.now().isoformat(),
            "total_tests": total,
            "passed": passed,
            "failed": failed,
            "pass_rate": f"{pass_rate:.2f}%",
            "results": [
                {
                    "test_name": r.test_name,
                    "passed": r.passed,
                    "error_message": r.error_message,
                    "details": r.details
                }
                for r in all_results
            ]
        }
        
        return report
    
    def print_report(self, report: Dict[str, Any]):
        """打印评估报告"""
        print("\n" + "=" * 50)
        print("评估报告")
        print("=" * 50)
        print(f"Skill: {report['skill_name']}")
        print(f"时间: {report['timestamp']}")
        print(f"总测试数: {report['total_tests']}")
        print(f"通过: {report['passed']}")
        print(f"失败: {report['failed']}")
        print(f"通过率: {report['pass_rate']}")
        print("\n详细结果:")
        
        for result in report['results']:
            status = "✓" if result['passed'] else "✗"
            print(f"  {status} {result['test_name']}")
            if not result['passed'] and result['error_message']:
                print(f"    错误: {result['error_message']}")
    
    def save_report(self, report: Dict[str, Any], output_path: Path):
        """保存评估报告"""
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"\n报告已保存到: {output_path}")


def main():
    if len(sys.argv) < 2:
        print("用法: python eval-runner.py <skill-path> [output-path]")
        sys.exit(1)
    
    skill_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else skill_path / "eval-report.json"
    
    runner = EvalRunner(skill_path)
    report = runner.run_all_evals()
    
    runner.print_report(report)
    runner.save_report(report, output_path)
    
    # 根据通过率决定退出码
    pass_rate = float(report['pass_rate'].rstrip('%'))
    if pass_rate < 90:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
