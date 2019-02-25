import requests
import json

# 02597388477758e6824b2547d01f0fef
# address = input('输入地点：')
headers = {"apikey":"002597388477758e6824b2547d01f0fef"}
url = 'http://apis.baidu.com/xiaogg/citylocation/citylocation?city=%E5%8C%97%E4%BA%AC'
res = requests.get(url, headers=headers)
print(res.text)



