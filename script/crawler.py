import re
import urllib.request
from bs4 import BeautifulSoup
import selenium

#获取网页源代码
def acquire():
    url='https://www.szwego.com/static/index.html?t=1594487852188#/shop_detail/A2017122810495318707'
    head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
		  'Cookie':'sajssdk_2015_cross_new_user=1; UM_distinctid=1733ede66d34a5-0b2b7919718ac4-7373e61-e1000-1733ede66d4a8c; CNZZDATA1275056938=98452460-1594487620-https%253A%252F%252Fwww.wegooooo.com%252F%7C1594487620; token=NTBBNTc0RDE0QTE1NTk0NDdBMzExOEM1NjJERjA5M0MyMDEzMUEwMUZFNEY3QzU3QjJBMTIyQUQ3RDVDN0I4M0FCMDk0RkQyNTZCNkE2QkExREI3QkJEMTU1RkEyQzc2; JSESSIONID=8BCD27926401909BC8249E1E81EB0CB1; client_type=net; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22A202006301135358910159322%22%2C%22first_id%22%3A%221733ede65e67ad-05517c91066ac8-7373e61-921600-1733ede65e741a%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221733ede65e67ad-05517c91066ac8-7373e61-921600-1733ede65e741a%22%7D'}
    red=urllib.request.Request(url=url,headers=head)
    read=urllib.request.urlopen(red).read()
    soup = BeautifulSoup(read, 'html.parser')
    print("获取网页源代码成功")
    print("-"*100)
    return soup
print(acquire())


