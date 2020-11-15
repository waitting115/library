from selenium import webdriver
from selenium.webdriver.common.keys import Keys

bw = webdriver.Chrome()
#浏览器自动输入该网址并进入
url = 'https://bj.lianjia.com/?utm_source=baidu&utm_medium=pinzhuan&utm_term=biaoti&utm_content=biaotimiaoshu&utm_campaign=wybeijing'
bw.get(url)
#找到该id的元素(现在是百度首页的搜索框)
input = bw.find_element_by_id('keyword-box')
#在input元素中输入Python关键字
input.send_keys('北京')
#在input元素上执行enter(回车)
input.send_keys(Keys.ENTER)
print(bw.find_element_by_class_name('houseInfo').text)