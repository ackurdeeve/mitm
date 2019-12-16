# coding=utf-8
import json


class Zhcn:
    def __init__(self):
        self.num = 0

    def response(self, flow) -> None:
        # print(flow.request.url)
        # print(flow.request.host)
        if flow.request.host == "subscription.grammarly.com":
            print('-' * 30)
            text2 = flow.response.text
            parsed_json = json.loads(text2)
            parsed_json["isPremium"] = True
            parsed_json["isAppleSubscription"] = True
            parsed_json["isGooglePlaySubscription"] = True
            print(parsed_json["isPremium"])
            text2 = json.dumps(parsed_json)
            flow.response.set_text(text2)
            print('-' * 30)

        if flow.request.host == "auth.grammarly.com":
            text4 = flow.response.text
            parsed_json4 = json.loads(text4)
            parsed_json4["free"] = False
            parsed_json4["grammarlyEdu"] = True
            parsed_json4["type"] = "Premium"
            parsed_json4["subscriptionFree"] = False
            parsed_json4["groups"] = ["Funnel","office-addin","mobile-ios","extension-chrome","payment_page_abandoned","desktop_editor_used","desktop_editor_windows","blog","webeditor","freemium-ping","mobile-app","desktopeditor","extension-installed","freemium","account","Premium"]
        
            text4 = json.dumps(parsed_json4)
            flow.response.set_text(text4)
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


addons=[
    Zhcn()
]