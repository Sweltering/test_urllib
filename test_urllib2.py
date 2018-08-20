from urllib import request, parse

# 1、Request类的用法
# 没有头部信息，网站会识别这个请求是爬虫发来的，会返回一段没用的数据给你
# url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
# # resp = request.urlopen(url)
# # print(resp.read())

# # 增加chorms的请求头部，还是会请求失败，需要将头部伪装的更像浏览器
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
# }
# req = request.Request(url, headers=headers)
# resp = request.urlopen(req)
# print(resp.read())


# url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
#     'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
# }
# data = {
#     'first': 'true',
#     'pn': 1,
#     'kd': 'python'
# }
# req = request.Request(url, headers=headers, data=parse.urlencode(data).encode('utf-8'), method='POST')
# resp = request.urlopen(req)
# print(resp.read().decode('utf-8'))


# 2、ProxyHandler处理器（代理设置）的用法
# 很多网站会检测每一段时间某个IP的访问次数，如果访问次数过多，会禁止这个IP的访问，可以设置一些代理服务器，每隔一段时间换一个
# 代理，就算IP被禁止了，依然可以换别的IP继续爬取。urllib通过ProxyHandler来设置使用代理服务器。
# IP代理服务商：https://www.kuaidaili.com/free/
# 查看当前请求的一些参数:http://httpbin.org
# 不使用代理
from urllib import request

# url = 'http://httpbin.org/ip'
# resp = request.urlopen(url)
# print(resp.read())

# 使用代理
# url = 'http://httpbin.org/ip'
# # 1、使用ProxyHandler，传入代理构建一个handler
# handler = request.ProxyHandler({'http': '183.158.203.51:9000'})
# # 2、使用handler构建一个opener
# opener = request.build_opener(handler)
# # 3、使用opener发送请求
# resp = opener.open(url)
# print(resp.read())


# 3、cookie
# 在网站中，http请求是无状态的，也就是说即使第一次和服务器连接成功后，第二次请求服务器依然不知道当前请求是哪一个用户，cookie
# 的出现就是为了解决这个问题，第一次在用户登录之后服务器会返回一些数据（cookie）信息给浏览器，然后浏览器将信息保存在本地，
# 当用户第一次请求的时候，会带着cookie信息发送给服务器，这样服务器通过cookie就可以判断用户是否连接过。cookie存储的数据量是
# 有限的，不同浏览器有不同的存储大小，但一般不超过4KB。
# cookie格式：set-Cookie: NAME=VALUE; Expires/Max-age=DATE; Path=PATH; Domain=DOMAIN_NAME; SECURE
# NAME: cookie的名字；VALUE：cookie的值；Expires：cookie过期时间；Path：cookie作用的路径；Domain：cookie作用的域名；SECURE：是否只在https协议下起作用

# 保存cookie到本地，可以使用cookiejar的save方法，并且需要指定一个文件名
# 保存百度的cookie到本地
from urllib import request
from http.cookiejar import MozillaCookieJar

# cookiejar = MozillaCookieJar('cookie.txt')
# handler = request.HTTPCookieProcessor(cookiejar)
# opener = request.build_opener(handler)
#
# resp = opener.open('http://www.baidu.com/')
# cookiejar.save()

# http://httpbin.org/cookies/set?course=abc
# cookiejar = MozillaCookieJar('cookie.txt')
# handler = request.HTTPCookieProcessor(cookiejar)
# opener = request.build_opener(handler)
#
# resp = opener.open('http://httpbin.org/cookies/set?course=abc')
# # ignore_discard=True将即将过期的cookie保存在本地
# cookiejar.save(ignore_discard=True)

# 从指定的文件加载cookie信息
cookiejar = MozillaCookieJar('cookie.txt')
# ignore_discard=True将即将过期的cookie保存在本地
cookiejar.load(ignore_discard=True)
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

opener.open('http://httpbin.org/cookies')
for cookie in cookiejar:
    print(cookie)

