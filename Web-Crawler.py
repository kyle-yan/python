import requests # requests用于调取网页上的数据
from bs4 import BeautifulSoup # beautifulSoup用于抓取网页上的信息


def get_content(content_url):  # 定义函数，参数是内容的url
    source_code = requests.get(content_url)  # 从输入的url获取网页的源代码
    plain_text = source_code.text   # 讲网页源代码储存成普通文字
    soup = BeautifulSoup(plain_text, "html.parser")  # 用beautifulSoup抓取网页源代码中的内容
    for item_name in soup.findAll('div', {'class': 'news-title'}):  # 抓取所有div中class = news-title的项
        print(item_name.string)  # 输出结果


def news(max_pages):
    page = 185
    while page >= 186 - max_pages:  # 结合新闻网的特点，遍历新闻网新闻的页数
        url = 'http://news.nankai.edu.cn/nkyw/system/more/32000000/0001/32000000_00000' + str(page) + '.shtml'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a', {'class': 'news'}):  #所有的链接
            href = link.get('href')
            #title = link.string
            #print(href)
            #print(title)
            get_content(href)
        page -= 1


news(3)
