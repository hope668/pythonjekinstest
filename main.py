import time

import requests
import json
url = "https://kim-robot.kwaitalk.com/api/robot/send?key=8fdeee00-9bb9-4de2-bae7-a0833eea5759"
# payload = json.dumps({
# 	"content": "{\"text\":\"test content\"}",
# 	"msg_type": "text",
# 	"receive_id": "ou_7d8a6e6df7621556ce0d21922b676706ccs",
# 	"uuid": "选填，每次调用前请更换，如a0d69e20-1dd1-458b-k525-dfeca4015204"
# })
payload=json.dumps({
	"msgtype": "text",
  "text": {
       "content":  f'request example--{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())}'
   }
})

print(time.time())
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)