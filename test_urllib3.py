# 1、爬取兰州城市学院首页的数据
# utl链接：http://www.lzcu.edu.cn/index.htm

# from urllib import request
#
# url = 'http://www.lzcu.edu.cn/index.htm'
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
#     'Referer' : 'http://www.lzcu.edu.cn/'
# }
#
# req = request.Request(url, headers=headers)
# resp = request.urlopen(req)
# print(resp.read().decode())

# 2、爬取人人网中大鹏的主页内容
from urllib import request

# dapeng_url = 'http://www.renren.com/880151247/profile'
# # 不使用cookie去爬取大鹏主页，看结果值爬取到了注册的页面
# # headers = {
# #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
# # }
# # 使用cookie
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
#     'Cookie': 'anonymid=jl1yh5ck-fxzrxp; depovince=BJ; _r01_=1; JSESSIONID=abc-s4a41fbAGfrTuowvw; ick_login=7233496a-0278-4492-b47d-171ff0e72457; ick=2e0a1b68-9919-4313-9cd6-7ebfc41ca3e3; t=9fdbd3b42f368a99d76303101badfe6b0; societyguester=9fdbd3b42f368a99d76303101badfe6b0; id=967643640; xnsid=a9c5b0db; XNESSESSIONID=f035cb985f66; WebOnLineNotice_967643640=1; jebecookies=9f1ef131-1851-445c-9a62-c2ab2e7ca29a|||||; ver=7.0; loginfrom=null; jebe_key=3f3d8456-cde6-42a9-a9e6-13204f73bccb%7Cb939033e6ecb601b13da2fa06ef0385f%7C1534750074374%7C1%7C1534750083069; wp_fold=0'
# }
# req = request.Request(url=dapeng_url, headers=headers)
# resp = request.urlopen(req)
# with open('renren.html', 'w', encoding='utf-8') as f:
#     # write函数必须写入一个str的数据类型，decode解码
#     f.write(resp.read().decode('utf-8'))


# http.cookiejar模块
# 利用http.cookiejar和request.HTTPCookieProcessor登录人人网
from urllib import request, parse
from http.cookiejar import CookieJar

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
}


def get_opener():
    # 1、登录
    # 1.1 创建一个cookiejar对象
    cookiejar = CookieJar()
    # 1.2 使用cookiejar创建一个HTTPCookieProcessor对象
    handler = request.HTTPCookieProcessor(cookiejar)
    # 1.3 使用handler创建一个opener
    opener = request.build_opener(handler)
    return opener


def login_renren(opener):
    # 1.4 使用opener发送登录的请求
    data = {
        'email': '13993601652',
        'password': 'w199548j?*'
    }
    login_url = 'http://www.renren.com/PLogin.do'
    req = request.Request(url=login_url, data=parse.urlencode(data).encode('utf-8'),
                          headers=headers)
    opener.open(req)


def visit_profile(opener):
    # 2、访问个人主页
    dapeng_url = 'http://www.renren.com/880151247/profile'
    req = request.Request(url=dapeng_url, headers=headers)
    resp = opener.open(req)
    with open('renren.html', 'w', encoding='utf-8') as f:
        f.write(resp.read().decode('utf-8'))


if __name__ == '__main__':
    opener = get_opener()
    login_renren(opener)
    visit_profile(opener)