# coding=utf-8
import json


class Zhcn:
    def __init__(self):
        self.num = 0

    def response(self, flow) -> None:
        # print(flow.request.url)
        # print(flow.request.host)

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


addons=[
    Zhcn()
]