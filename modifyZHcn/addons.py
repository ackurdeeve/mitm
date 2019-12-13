# coding=utf-8
import zhcn


addons = [
    zhcn.Zhcn(),
]

# mitmweb -s addons.py -p 2080
# mitmweb  --no-web-open-browser -p 2080 --anticache -m upstream:http://127.0.0.1:1081 -s addons.py
