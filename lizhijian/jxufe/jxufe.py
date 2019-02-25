import requests
headers = {
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
res = requests.get('http://www.jxufe.edu.cn/',headers = headers)
print(res.content)

