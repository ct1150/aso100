from aso100 import Aso100
from mysqlcli import MysqlCli
import time

def crawler_app_rank():
    url = 'https://api.qimai.cn/app/rank'

    cookies = {
        "PHPSESSID": "v4t2pr0deio23e4dtdqfa0a0n5",
        "USERINFO": "wKTVC3g7j0tpgTAusM46zyv13wtVPsH4RaKG%2B0QB0kbU%2BYsuNLIggTgEX4AwMRKHkfc6ls4mJo81XSHR8QgX09Ss2Q%2B65%2FJLJnzhh1j1PO9IbqndfZVHllKqRjPd%2FpNg%2FHfz4uGzzK8ajNKyYI%2F6MA%3D%3D"
    }
    mysqlcli = MysqlCli()
    aso100 = Aso100()
    reslist = []
    #查询满足条件的appid
    appid_list = mysqlcli.execute('select app_id from tread_rank where app_id="564818797" ')
    #传入appid循环爬取
    for appid in appid_list:
        params = {
            "appid": appid[0],
            "country": "cn",
            "brand": "free"
        }
        data = aso100.crawler(url=url, params=params, cookies=cookies)
        time.sleep(1)
        reslist.append(data)
        #插入到数据库
        mysqlcli.execute('insert into tread_rank(xxx,xxx,xxx) VALUE (yyy,yyy,yyy)')

    print('write ok')
