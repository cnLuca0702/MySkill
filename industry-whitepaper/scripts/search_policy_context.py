#!/usr/bin/env python3
"""
政策背景搜索脚本
用于搜索国家政策、战略规划、行业标准等背景信息
"""

import json
import sys
from datetime import datetime


def search_policy_context(keyword: str, policy_level: str = None):
    """
    搜索政策背景

    Args:
        keyword: 关键词（如"碳中和"、"数字化转型"）
        policy_level: 政策层级（national/provincial/city/industry）
    """
    level_map = {
        "national": ["国家", "国务院", "部委", "五年规划"],
        "provincial": ["省", "自治区", "直辖市"],
        "city": ["市", "区县"],
        "industry": ["行业", "协会", "标准"]
    }

    level_keywords = level_map.get(policy_level, []) if policy_level else []

    # 构建搜索查询
    if policy_level:
        query = f"{' '.join(level_keywords)} {keyword} 政策 文件"
    else:
        query = f"{keyword} 政策 支持 规划"

    print(f"🏛️ 政策搜索: {query}")
    print(f"📑 关键词: {keyword}")

    return {
        "query": query,
        "policy_types": [
            "国家五年规划",
            "国务院指导意见",
            "部委专项行动计划",
            "行业标准规范",
            "财政支持政策",
            "税收优惠政策"
        ],
        "key_elements_to_find": [
            "政策发布时间",
            "政策发布部门",
            "政策核心目标",
            "重点支持领域",
            "配套措施（资金/税收/土地）",
            "实施时间表"
        ]
    }


def main():
    if len(sys.argv) < 3:
        print("用法: python search_policy_context.py --keyword <关键词> [--level <policy_level>]")
        print("\n政策层级: national | provincial | city | industry")
        print("\n示例:")
        print("  python search_policy_context.py --keyword '碳中和' --level national")
        print("  python search_policy_context.py --keyword '智能制造'")
        sys.exit(1)

    args = sys.argv[1:]
    keyword = None
    level = None

    for i in range(len(args)):
        if args[i] == "--keyword" and i + 1 < len(args):
            keyword = args[i + 1]
        elif args[i] == "--level" and i + 1 < len(args):
            level = args[i + 1]

    if not keyword:
        print("错误: 必须指定 --keyword 参数")
        sys.exit(1)

    result = search_policy_context(keyword, level)
    print("\n" + "="*60)
    print("📋 政策搜索建议:")
    print("="*60)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
