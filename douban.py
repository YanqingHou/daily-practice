from requests_html import HTMLSession
import csv
import time

"""
爬取豆瓣top250电影数据并保存
"""

# 初始化session
session = HTMLSession()

# 初始化csv文件

with open('douban.csv', 'w', encoding='utf-8') as fd:
    # 设置字段名
    fieldname = ['电影名称', '电影图片', '电影排名', '电影评分', '电影作者', '电影简介']
    writer = csv.DictWriter(fd, fieldnames=fieldname)
    writer.writeheader()

    # 开始爬取
    for i in range(10):

        url = f'https://movie.douban.com/top250?start={i*25}'
        headers = {
            'uesr-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}
        response = session.get(url=url, headers=headers)

        # 根据xpath解析需要的内容
        dom = response.html
        for j in range(1,26):
            name = dom.xpath(f'//*[@id="content"]/div/div[1]/ol/li[{j}]/div/div[2]/div[1]/a/span[1]/text()',first=True)
            photo = dom.xpath(f'//*[@id="content"]/div/div[1]/ol/li[{j}]/div/div[1]/a/img/@src', first=True)
            rank = dom.xpath(f'//*[@id="content"]/div/div[1]/ol/li[{j}]/div/div[1]/em/text()', first=True)
            point = dom.xpath(f'//*[@id="content"]/div/div[1]/ol/li[{j}]/div/div[2]/div[2]/div/span[2]/text()', first=True)
            author = dom.xpath(f'//*[@id="content"]/div/div[1]/ol/li[{j}]/div/div[2]/div[2]/p[1]/text()[1]', first=True)
            intro = dom.xpath(f'//*[@id="content"]/div/div[1]/ol/li[{j}]/div/div[2]/div[2]/p[2]/span/text()', first=True)

            # 数据持久化

            writer.writerow({'电影名称':name, '电影图片':photo, '电影排名':rank, '电影评分':point, '电影作者':author, '电影简介':intro})

        print(i+1)
        time.sleep(5)

    print('over')