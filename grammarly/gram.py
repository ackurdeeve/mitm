# coding=utf-8
from mitmproxy import http
import json


class Response:
    def __init__(self):
        self.num = 0

    def response(self, flow: http.HTTPResponse) -> None:
        # print(flow.response.content)
        # print(flow.request.url)
        print(flow.request.host)
        # if flow.request.url == "https://subscription.grammarly.com/api/v1/subscription":
        if flow.request.host == "subscription.grammarly.com":
            print('-' * 30)
            # print("==========发出 %d 个请求=========" % self.num)
            print('*****链接****')
            # print(flow.request.url)
            # print(flow.request.host)
            print('!!!!!hit website!!!')
            # text = flow.request.content
            # text1 = flow.response
            # print(text)
            # print(text1)
            text2 = flow.response.text
            parsed_json = json.loads(text2)
            # print(parsed_json["isPremium"])

            parsed_json["isPremium"] = True
            parsed_json["isAppleSubscription"] = True
            parsed_json["isGooglePlaySubscription"] = True
            print(parsed_json["isPremium"])
            # text2 = text2.replace('"isPremium":false', '"isPremium":True')
            text2 = json.dumps(parsed_json)
            # print(text2)
            flow.response.set_text(text2)
            print('-' * 30)

        if flow.request.host == "f-log-editor.grammarly.io":
            self.num = self.num + 1
            print(flow.request.host)
            print('!!!!!hit website!!!')
            text3 = flow.request.text
            print(text3)
            # parsed_json3 = json.loads(text3)
            # parsed_json3['context']['user']['type'] = "Premium"
            # text3 = json.dumps(parsed_json3)
            # flow.request.set_text(text3)
            print('-' * 30)

        if flow.request.host == "auth.grammarly.com":
            text4 = flow.response.text
            parsed_json4 = json.loads(text4)
            parsed_json4["free"] = False
            parsed_json4["grammarlyEdu"] = True
            parsed_json4["type"] = "Premium"
            parsed_json4["subscriptionFree"] = False

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


# {
#     "application": "editor",
#     "context": {
#         "containerId": "jpjs9je4etk44o2",
#         "sessionId": "v29iDbhQfGWTeO",
#         "user": {
#             "id": "899829875",
#             "type": "free"
#         },
#         "userAgent": {
#             "browser": "chrome",
#             "os": "windows",
#             "raw": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
#             "type": "desktop",
#             "version": "78"
#         },
#         "visibilityState": "visible"
#     },
#     "env": "prod",
#     "extra": {},
#     "level": "INFO",
#     "logger": "editor.events.tracking",
#     "message": "myGrammarly-page-show",
#     "version": "1.5.43-2182+master"
# }