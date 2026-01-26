#!/usr/bin/env python3
"""
行业数据搜索脚本
用于白皮书生成时补充行业数据、市场规模、增长率等关键信息
"""

import json
import sys
import subprocess
from datetime import datetime


def search_industry_data(industry: str, topic: str = None, year: int = None):
    """
    搜索行业数据

    Args:
        industry: 行业名称（如"新能源汽车"、"人工智能"）
        topic: 具体主题（如"市场规模"、"增长率"、"产业链"）
        year: 年份（默认当年）
    """
    if year is None:
        year = datetime.now().year

    # 构建搜索查询
    if topic:
        query = f"{industry} {topic} {year} 数据 报告"
    else:
        query = f"{industry} 行业报告 {year} 市场规模 发展趋势"

    print(f"🔍 搜索查询: {query}")
    print(f"📊 行业: {industry}")
    print(f"📌 年份: {year}")

    # 使用WebSearch工具（通过MCP或直接调用）
    # 这里输出结构化提示，供Claude使用搜索工具
    return {
        "query": query,
        "search_suggestions": [
            f"{industry}市场规模{year}",
            f"{industry}增长率{year}",
            f"{industry}竞争格局{year}",
            f"{industry}政策支持{year}",
            f"{industry}技术突破{year}",
            f"{industry}投资融资{year}"
        ],
        "data_points_to_find": [
            "市场规模（亿元）",
            "同比增长率（%）",
            "主要企业市场份额",
            "政策文件名称",
            "技术里程碑",
            "投融资事件"
        ]
    }


def main():
    if len(sys.argv) < 3:
        print("用法: python search_industry_data.py --industry <行业名称> [--topic <主题>] [--year <年份>]")
        print("\n示例:")
        print("  python search_industry_data.py --industry '新能源汽车' --topic '市场规模'")
        print("  python search_industry_data.py --industry '人工智能' --year 2024")
        sys.exit(1)

    args = sys.argv[1:]
    industry = None
    topic = None
    year = None

    for i in range(len(args)):
        if args[i] == "--industry" and i + 1 < len(args):
            industry = args[i + 1]
        elif args[i] == "--topic" and i + 1 < len(args):
            topic = args[i + 1]
        elif args[i] == "--year" and i + 1 < len(args):
            year = int(args[i + 1])

    if not industry:
        print("错误: 必须指定 --industry 参数")
        sys.exit(1)

    result = search_industry_data(industry, topic, year)
    print("\n" + "="*60)
    print("📋 搜索建议:")
    print("="*60)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
