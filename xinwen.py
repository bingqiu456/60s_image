import httpx
import time
import date


def get_news():
    text = ""
    try:
        a = httpx.get(
            url=f"https://news.baidu.com/widget?id=LocalNews&ajax=json&t={int(time.time())}",
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/96.0.4664.110 Safari/537.36"
            }
        ).json()

        s = []
        k = a["data"]["LocalNews"]["data"]["rows"]["first"]
        for i in range(min(20, len(k))):
            text += k[i]["title"]+"\n"
            s.append(k[i]["title"])

        a = httpx.get(
            url="https://gw.m.163.com/search/api/v1/pc-wap/rolling-word",
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/96.0.4664.110 Safari/537.36"
            }
        ).json()
        k = a["data"]["rollHotWordList"]
        for i in range(min(20, len(k))):
            text += k[i]["hotWord"]+"\n"
            s.append(k[i]["hotWord"])
        with open(f"./data/file/rubbish/xinwen_{date.get_year()}-{date.get_month()}-{date.get_day()}.txt", "w+", encoding="utf_8") as f:
            f.write(text)
            f.close()
        return s
    except (httpx.ConnectError, httpx.ConnectTimeout, IndexError):
        return ["新闻获取失败，请检查网络"]
