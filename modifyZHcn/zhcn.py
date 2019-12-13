# coding=utf-8
import json
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
                text = text.replace("扶墙机场推荐-GLaDOS", "Hello World")
                # print(html.text)
                flow.response.set_text(text)
            print('-' * 30)

        if flow.request.host == "www.so.com":
            html = flow.response.text
            print(html)
            print('-' * 30)

        if flow.request.host == "education.github.com":
            text5 = flow.response.text
            parsed_json5 = json.loads(text5)
            parsed_json5["student"] = True
            text5 = json.dumps(parsed_json5)
            flow.response.set_text(text5)
            print('-' * 30)

        if flow.request.url.startswith("https://api.termius.com/api/v3/bulk/account/"):
            obj = json.loads(flow.response.get_text())
            obj["account"]['pro_mode'] = True
            obj['account']['plan_type'] = "Premium"
            obj['account']['user_type'] = "Premium"
            obj['account']['current_period']['until'] = "2099-10-10T03:27:34"
            flow.response.set_text(json.dumps(obj))

