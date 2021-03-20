# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import requests
from bs4 import BeautifulSoup
import re
import json
import os

base_url = 'https://eatasmr.com'
cookie = os.environ.get("cookie_eatASMR")


def getLoginUrl():
    url = 'https://eatasmr.com/tasks/attendance'
    headers = {
        "cookie": cookie,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36 Edg/80.0.361.69",
        "referer": "https://eatasmr.com/"

    }
    res = requests.get(url, headers=headers).text
    loginUrl = re.findall(r"(/tasks/attendance\?a=check&__v=..........)", res)
    print(loginUrl)
    for i in range(0, len(loginUrl)):
        login(loginUrl[i])


def login(path):
    # url = base_url + path
    url = "https://eatasmr.com/tasks/attendance?a=check&__v=cd4993e6fe"
    print(url)
    headers = {
        "cookie": cookie,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36 Edg/80.0.361.69",
        "referer": "https://eatasmr.com/tasks/attendance"

    }
    data = {
        "check": "簽到"
    }
    res = requests.post(url, data=json.dumps(data), headers=headers).text
    print(res)


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    if cookie:
        print("----------eatASMR开始尝试签到----------")
        getLoginUrl()
        print("----------eatASMR签到执行完毕----------")
