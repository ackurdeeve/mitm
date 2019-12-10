# coding=utf-8
import requests


class Zhcn:
    def __init__(self):
        self.num = 0

    def response(self, flow) -> None:
        # print(flow.request.url)
        # print(flow.request.host)
        if flow.request.host == "www.ackurdeeve.com":
            html = requests.get("https://www.ackurdeeve.com")
            print('encoding:', html.encoding)
            print('apparent_encoding:', html.apparent_encoding)
            html.encoding = ('utf8')
            text = html.text
            text = text.replace("扶墙机场推荐-GLaDOS 通用网络游戏加速器", "Hello World")
            # print(html.text)
            flow.response.set_text(text)
            print('-' * 30)

        if flow.request.host == "www.so.com":
            html = flow.response.text
            print(html)
            print('-' * 30)
