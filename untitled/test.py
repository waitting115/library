from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# import pymysql
url = 'https://sjz.lianjia.com/ershoufang/rs/'
bq = webdriver.Chrome()
bq.get(url)
#定位小区搜索框
input_loc = bq.find_element_by_css_selector('#searchInput')
#将小区名称输入到搜索框中
input_loc.send_keys('佳')
#设置强制延时，避免突然点击回车无法切换
time.sleep(3)
#敲击回车
input_loc.send_keys(Keys.ENTER)
time.sleep(10)
#定位房源信息，定位的其中一部分，价格等其他信息需要额外定位抓取
house_info = bq.find_elements_by_css_selector('div.houseInfo')
house_price = bq.find_elements_by_css_selector('.totalPrice span')
for x in house_info:
    print(x.text)
for y in house_price:
    print(y.text)