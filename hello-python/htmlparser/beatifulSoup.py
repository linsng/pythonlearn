from bs4 import BeautifulSoup
import json
import datetime
import os

#https://www.cnblogs.com/panzi/p/6421826.html 参考网址


# 通过本地文件创建BeatifulSoup
with open('../hello.html', 'r', encoding='utf8') as foo_file:
    soup = BeautifulSoup(foo_file, 'html.parser')

#print(soup)

def createDir():
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    path = os.path.join('.', date)
    if(os.path.exists(path)):
        return path
    else:
        os.mkdir(path)
        return path

#定义一个article对象
class Article(object):
    def __init__(self, href, title, summary, author, author_url, pub_time, comment_num, view_num):
        self.href = href,
        self.title = title,
        self.summary = summary,
        self.author = author,
        self.author_url = author_url,
        self.pub_time = pub_time,
        self.comment_num = comment_num,
        self.view_num = view_num

items = soup.findAll('div', {'class': 'post_item'})
for item in items:

    item_body = item.find('div', {'class': 'post_item_body'})
    #获取标题
    item_title = item_body.find('a', {'class': 'titlelnk'})  #得到一个Tag 对象
    title = item_title.string
    title = title.replace('\n','').replace(' ','')
    #获取标题链接
    href = item_title['href'] #或link = item_title.attrs['href']

    #获取摘要
    item_summary = item_body.find('p', {'class': 'post_item_summary'})
    item_summary_a = item_summary.find('a');
    summary = item_summary_a.next_sibling #获取下一个兄弟元素
    summary = summary.replace('\n','').replace(' ','')

    #获取作者
    item_footer = item_body.find('div', {'class': 'post_item_foot'})
    item_footer_a = item_footer.find('a');
    author = item_footer_a.string

    author_url = item_footer_a['href']

    #文章发布时间
    pub_time = item_footer_a.next_sibling.string
    pub_time = pub_time.replace('发布于 ','').strip()

    #评论数 阅读量
    article_comment = item_footer.find('span', {'class': 'article_comment'})
    comment_num = article_comment.find('a').string.strip()

    article_view = item_footer.find('span', {'class': 'article_view'})
    view_num = article_view.find('a').string.strip()

    article_obj = dict(href = href,
                       title = title,
                       summary = summary,
                       author = author,
                       author_url = author_url,
                       pub_time = pub_time,
                       comment_num = comment_num,
                       view_num = view_num)
    #转换成json存储
    article_result_json = json.dumps(article_obj)
    path = createDir() + '/blog_1.txt'
    with open(path, 'a') as file:
        file.write(article_result_json)
        file.write('\n')

