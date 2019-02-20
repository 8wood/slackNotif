import requests
import json

web_hook_url = 'https://hooks.slack.com/services/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'

def send_message(message):
    slack_msg = {'text':message}
    requests.post(web_hook_url, data=json.dumps(slack_msg))

