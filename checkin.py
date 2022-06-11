# -*- coding: utf-8 -*-
import logging
import requests
import os
result = b'success\n'
# url
url = "https://glados.rocks/api/user/checkin"
# cookie
cookie = os.environ["COOKIE"]

payload = {
  "token": "glados.network"
}
headers = {
  'authority': 'glados.rocks',
  'accept': 'application/json, text/plain, */*',
  'dnt': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47',
  'content-type': 'application/json;charset=UTF-8',
  'origin': 'https://glados.rocks',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://glados.rocks/console/checkin',
  'accept-language': 'zh-CN,zh;q=0.9',
  'cookie': cookie
}
def do_action():
    logger = logging.getLogger()
    requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
    response = requests.post(url, headers=headers, json = payload, timeout=3)
    response.close()
    result = response.text.encode('utf8')
    logger.info(result)
    print(result)
    return result


if __name__ == '__main__':
    do_action()
