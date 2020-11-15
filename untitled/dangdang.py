from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pymysql

def find_book(book):
    bw = webdriver.Chrome()
    url = 'http://www.dangdang.com/'
    print('正在打开网页...')
    bw.get(url)
    input = bw.find_element_by_id('key_S')
    input.send_keys(book)
    time.sleep(3)
    input.send_keys(Keys.ENTER)
    currentUrl = bw.current_url

    bookTitleList = []
    bookPriceList = []
    bookAuthor_time_pressList = []
    bookContentList = []
    print('正在爬取数据...')

    for k in range(2):
        url = str(currentUrl) + '&page_index=' + str(k+1)
        bw.get(url)
        bookTitle = bw.find_elements_by_css_selector('p.name')
        bookPrice = bw.find_elements_by_css_selector('p.price span.search_now_price')
        bookAuthor_time_press = bw.find_elements_by_css_selector('p.search_book_author span')
        bookContent = bw.find_elements_by_css_selector('p.detail')

        for i in range(len(bookTitle)):
            bookTitleList.append(bookTitle[i].text)
            bookPriceList.append(bookPrice[i].text)
            bookAuthor_time_pressList.append(bookAuthor_time_press[i].text)
            bookContentList.append(bookContent[i].text)

    bookObj = {
        'bookTitleList': bookTitleList,
        'bookPriceList': bookPriceList,
        'bookAuthor_time_pressList': bookAuthor_time_pressList,
        'bookContentList': bookContentList
    }
    print("数据爬取成功 !")
    return bookObj

def connect_mysql(dbTableName, bookObj):
    # 连接数据库
    db = pymysql.connect(host='localhost', user='root', password='012345', port=3306,database='dangdang')

    # 创建游标
    cursor = db.cursor()

    # 使用 execute() 方法执行 SQL，如果表存在则删除
    sql = "DROP TABLE IF EXISTS " + dbTableName
    cursor.execute(sql)

    # 创建数据表
    sql = "create table " + dbTableName + " (title  varchar(500) not null,price  varchar(100) not null,author varchar(200) not null,content varchar(500) not null)"
    cursor.execute(sql)

    # print(bookObj['bookTitleList'][0])
    print("正在向数据库添加数据...")
    for x in range(len(bookObj['bookTitleList'])):
        # 添加数据
        sql = "insert into " + dbTableName + " (title, price, author, content) \
           values ('%s', '%s',  '%s', '%s')" % \
           (pymysql.escape_string(bookObj['bookTitleList'][x]), pymysql.escape_string(bookObj['bookPriceList'][x]), pymysql.escape_string(bookObj['bookAuthor_time_pressList'][x]) , pymysql.escape_string(bookObj['bookContentList'][x]))

        cursor.execute(sql)
        db.commit()

    # 关闭数据库连接
    db.close()
    print('数据存储成功！')

def find_sql_book(dbTableName, queryWord):
    # 连接数据库
    db = pymysql.connect(host='localhost', user='root', password='012345', port=3306, database='dangdang')

    # 创建游标
    cursor = db.cursor()

    sql = "select * from " + dbTableName + " where title like '%" + queryWord +"%'"
    print("正在查询数据...")
    cursor.execute(sql)
    selectResult = cursor.fetchall()
    db.close()
    return list(selectResult)

def main_fun():
    bookName = input("请输入您要搜索什么类型的书：")
    findWord = input("请输入您心仪的书的关键字：")
    # 爬
    paRes = find_book(bookName)
    # 存
    connect_mysql(bookName, paRes)
    # 查
    queryRes = find_sql_book(bookName, findWord)
    # print(queryRes)
    print("数据查询成功 ! 您查询的数据为：")
    for x in queryRes:
         print(x)

main_fun()