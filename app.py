#!/usr/bin/env python3
"""WorkBuddy 写代码演示：一个最小可运行脚本。"""

import sys
from datetime import datetime


def greet(name: str = "WorkBuddy") -> str:
    return f"你好，{name}！当前时间：{datetime.now():%Y-%m-%d %H:%M:%S}"


if __name__ == "__main__":
    who = sys.argv[1] if len(sys.argv) > 1 else "WorkBuddy"
    print(greet(who))
