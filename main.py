from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from pathlib import Path

import xinwen
import date
import random

image_path = f"./data/file/Picture/60s_{date.get_year()}-{date.get_month()}-{date.get_day()}.jpg"

# 加载一言文件
with open("./data/yiyan.txt", "r+", encoding="utf_8") as r:
    r_ = r.readlines()
    r.close()

# 加载字体素材
# 加载字体2素材
font_ = ImageFont.truetype(font=str(Path.cwd()) + "./data/file/data_week/ttf/oppo.ttf", size=25)
font_mao = ImageFont.truetype(font=str(Path.cwd()) + "./data/miaozimeiweiti.ttf", size=25)

# 打开底图 以及星期图
image_main: Image = Image.open("./data/file/data_week/yes.jpg")  # 底图
date_week: Image = Image.open(f"./data/file/data_week/{date.get_week()}.jpg")

# 插入星期几的图片
min_ = ImageDraw.Draw(image_main)
image_main.paste(date_week, (40, 40))

# 输入今天的新闻
xw = xinwen.get_news()
p = 770
for i in range(len(xw)):
    min_.text(text=f"{i + 1}." + xw[i], xy=(40, p), font=font_, fill="#000000")
    p += 35

# 日期信息
min_.text(text="欢迎你，感谢阅读冰月日报", fill="#000000", font=font_, xy=(40, 558))
min_.text(text=f"现在时间是 {date.get_date()} {date.get_week_()}", fill="#000000", font=font_, xy=(40, 558 + 35))
min_.text(
    text=f"今年是{date.get_year_()} 属{date.get_shu_year()}年 {date.get_festival(date.get_month(), date.get_day())}",
    fill="#000000", font=font_, xy=(40, 558 + 35 + 35))
min_.text(text=f"在这里小冰带你60s读日报", fill="#000000", font=font_, xy=(40, 558 + 35 + 35 + 35))
min_.text(text=f"一言:{random.choice(r_)[:-1]}", fill="#000000", font=font_, xy=(40, 558 + 35 + 35 + 35 + 35))

# 关于信息
min_.text(text=f"<(￣︶￣)> 新闻渠道:百度+网易 环境Pycharm 配图:网络 <(￣︶￣)>", fill="#000000", font=font_mao,
          xy=(98, p + 30))
min_.text(text=f"Created in Bingyue", fill="#000000", font=font_mao, xy=(348, p + 30 + 30))

# 保存图片
image_main.save(image_path)
image_main.save("./out.jpg")
print("图片生成成功，在out.jpg了")
