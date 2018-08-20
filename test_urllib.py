from urllib import request
from urllib import parse

# 1、urlopen函数的用法，爬取url访问的网站内容
# resp = request.urlopen('http://www.baidu.com')
# print(resp.read())
# print(resp.readline())
# print(resp.readlines())
# print(resp.getcode())


# 2、urlretrieve函数的用法， 将爬取到的数据存储到本地
# request.urlretrieve(
#     'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1534744293519&di=6487025765b16ab2e98f3580bab4c035&imgtype=0&src=http%3A%2F%2Fwww.people.com.cn%2Fmediafile%2Fpic%2F20170705%2F71%2F16627762923965534195.jpg',
#     'wzry.jpg')


# 3、urlencode函数的用法， url编码
# params = {'name': '张三', 'age': 20, 'greet': 'hello world'}
# result = parse.urlencode(params)
# print(result)


# url = 'https://www.baidu.com/s'
# params = {'wd': '迪丽热巴'}
# qs = parse.urlencode(params)
# url = url + '?' + qs
# resp = request.urlopen(url)
# print(resp.read())


# 4、parse_qs函数的用法， url解码
# params = {'name': '张三', 'age': 20, 'greet': 'hello world'}
# qs = parse.urlencode(params)
# print(qs)
# qs = parse.parse_qs(qs)
# print(qs)


# 5、urlparse, urlsplit函数的用法， 解析url的结构
# url = 'http://www.baidu.com/s?wd=python&username=abc#1'
# result1 = parse.urlparse(url)
# result2 = parse.urlsplit(url)
# print(result1)
# print(result2)
# print(result1.scheme)
# print(result2.scheme)
