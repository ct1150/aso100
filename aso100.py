import requests, execjs, json
from mysqlcli import MysqlCli

class Aso100(object):
    def __init__(self):
        with open('encrypt_20190217.js', encoding='utf-8') as f:
            self.jsdata = execjs.compile(f.read())
        self.headers = {
            'Referer': 'https://www.qimai.cn/rank',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        }

    def crawler(self, url='', params={}, cookies={}):
        js_params = json.dumps(params)
        analysis = self.jsdata.call('get_analysis', url, js_params)
        form = json.loads(analysis)
        html = requests.get(url, params=form, headers=self.headers, cookies=cookies)
        return html.json()


if __name__ == '__main__':
    # 抓取应用实时排名
    url = 'https://api.qimai.cn/app/rank'
    params = {
        "appid": "1448664217",
        "country": "cn",
        "brand": "free"
    }
    # # 抓取搜索指数排行
    # url = 'https://api.qimai.cn/trend/keywordRank'
    # params = {
    #     "date": "2019-05-17",
    #     "page": 1,
    #     "minHints": "5000",
    #     "maxHints": "5005"
    # }
    mysqlcli = MysqlCli()
    mysqldata = mysqlcli.execute('select app_id from tread_rank where word="12306" ')
    print(mysqldata)
    cookies = {
        "PHPSESSID": "v4t2pr0deio23e4dtdqfa0a0n5",
        "USERINFO": "wKTVC3g7j0tpgTAusM46zyv13wtVPsH4RaKG%2B0QB0kbU%2BYsuNLIggTgEX4AwMRKHkfc6ls4mJo81XSHR8QgX09Ss2Q%2B65%2FJLJnzhh1j1PO9IbqndfZVHllKqRjPd%2FpNg%2FHfz4uGzzK8ajNKyYI%2F6MA%3D%3D"
    }
    aso100 = Aso100()
    #返回爬取结果
    data = aso100.crawler(url=url, params=params, cookies=cookies)
    print(data[realTimeRank][0])
    #插入到数据库
    #mysqlcli.execute('insert into tread_rank')
