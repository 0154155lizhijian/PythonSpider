import requests
from bs4 import BeautifulSoup

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Cookie': '''uuid=7019cd27-f7f5-400a-884d-0af5cc1da841; ganji_uuid=5618080997316080002709; d1390049-4b04-4e1d-ae01-251e172d6125_views=1; financeCityDomain=jian; 7019cd27-f7f5-400a-884d-0af5cc1da841_views=2; 93536afc-2806-4a37-cd87-7bfa2e065506_views=1; Hm_lvt_e6e64ec34653ff98b12aab73ad895002=1540871139,1540975832; clueSourceCode=10103000312%2300; antipas=474011RO01848g243369678d6V; sessionid=86d133eb-c822-4f63-e1f7-eabe796cd291; lg=1; cainfo=%7B%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22tbmkbturl%22%2C%22ca_i%22%3A%22-%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22scode%22%3A%2210103000312%22%2C%22ca_transid%22%3Anull%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22ca_b%22%3A%22-%22%2C%22ca_a%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%227019cd27-f7f5-400a-884d-0af5cc1da841%22%2C%22sessionid%22%3A%2286d133eb-c822-4f63-e1f7-eabe796cd291%22%7D; close_finance_popup=2018-11-13; cityDomain=nc; preTime=%7B%22last%22%3A1542101969%2C%22this%22%3A1540799270%2C%22pre%22%3A1540799270%7D'''
    }

url='https://www.guazi.com/nc/?ca_s=pz_baidu&ca_n=tbmkbturl&scode=10103000312'
html = requests.get(url, headers=headers)
content = BeautifulSoup(html,'lxml')
print(content)






