# coding=utf-8
import requests


class Zhcn:
    def __init__(self):
        self.num = 0

    def response(self, flow) -> None:
        # print(flow.request.url)
        # print(flow.request.host)
        if flow.request.host == "www.ackurdeeve.com":
            url = flow.request.url
            print('-' * 30)
            print(url)
            html = requests.get(url)
            print('encoding:', html.encoding)
            print('apparent_encoding:', html.apparent_encoding)

            if html.encoding != 'None':
                html.encoding = ('utf8')
                text = html.text
                text = text.replace("畅游星海", "Hello World")
                # print(html.text)
                flow.response.set_text(text)
            print('-' * 30)

        if flow.request.host == "www.so.com":
            html = flow.response.text
            print(html)
            print('-' * 30)
