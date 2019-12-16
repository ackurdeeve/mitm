# coding=utf-8
import joker
from grammarly import gram


addons = [
    joker.Joker(),
    gram.Response(),
]

# mitmweb -s addons.py -p 2080
# mitmweb --mode upstream:http://127.0.0.1:1081 -s addons.py -p 2080
# mitmweb --mode socks -s addons.py -p 2080

