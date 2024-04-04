from datetime import datetime

y = datetime.now()


def get_day():
    """
    获取今天的日
    :return: int
    """
    return y.day


def get_week():
    """
    获取星期几 星期一对于0 星期日对于6
    :return: int
    """
    return y.weekday()


def get_week_():
    """
    转文字
    :return: str
    """
    s = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    return s[y.weekday()]


def get_month():
    """
    获取月份
    :return: int
    """
    return y.month


def get_year():
    """
    获取年份
    :return: int
    """
    return y.year


def get_year_():
    """
    计算平年 闰年
    :return: str
    """
    if get_year() % 4 == 0:
        return "闰年"
    else:
        return "平年"


def get_shu_year():
    """
    生肖计算
    :return: str
    """
    s = ["猴", "鸡", "狗", "猪", "鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊"]
    return s[get_year() % 12]


def get_date():
    """
    获取时间
    :return: str
    """
    return y.strftime('%Y-%m-%d %H:%M:%S')


def get_festival(month: int, day: int):
    """
    获取现在的节日
    :param month: int
    :param day: int
    :return: str | None
    """
    p = [
        (1, 1),
        (3, 8),
        (4, 4),
        (4, 5),
        (5, 1),
        (5, 4),
        (6, 1),
        (8, 1),
        (9, 10),
        (10, 1),
        (12, 24),
        (4, 1),
        (10, 31),
    ]
    s = [
        "元旦节",
        "妇女节",
        "清明节",
        "清明节",
        "劳动节",
        "青年节",
        "儿童节",
        "建党节",
        "教师节",
        "国庆节",
        "平安夜",
        "愚人节",
        "万圣节"
    ]
    if (month, day) in p:
        i = p.index((month, day))
        return s[i] + "快乐"
    else:
        return ""
