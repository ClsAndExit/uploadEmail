# coding:utf-8
#@Time    :2019/4/6 16:14
import datetime

def strDate(day):
    str_day = str(day).replace('-', '')
    return str_day

def today():
    return datetime.date.today()


def daysBeforeToday(days):
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=days)
    return tomorrow


if __name__ == "__main__":
    aa = daysBeforeToday(2)
    print(strDate(aa))