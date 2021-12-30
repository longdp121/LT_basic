import sqlite3
import newspaper
from newspaper import Article

def get_all(query):
    conn = sqlite3.connect('database/data.db')
    data = conn.execute(query).fetchall()
    conn.close()

    return data

def get_news_by_id(news_id):
    conn = sqlite3.connect('database/data.db')
    '''
    N as news
    C as catalogs
    '''
    sql = '''
    SELECT N.subject, N.description, N.image, N.ori_url, C.name
    FROM news N INNER JOIN catalogs C ON N.catalogy_id=C.id
    WHERE N.id =?
    '''
    news = conn.execute(sql, (news_id, )).fetchall()
    conn.close()
    return news

def add_comment(news_id, content):
    conn = sqlite3.connect('database/data.db')
    sql = '''
    INSERT INTO comment(content, news_id) VALUES (?, ?)
    '''
    conn.execute(sql, (content, news_id))
    conn.commit()
    conn.close()

def add_news(conn, url, catalogy_id):
    sql = '''
    INSERT INTO news(subject, description, image, ori_url, catalogy_id)
    VALUES (?, ?, ?, ?, ?)
    '''
    article = Article(url)
    article.download()
    article.parse()

    conn.execute(sql, (article.title, article.text, article.top_img, article.url, catalogy_id))
    conn.commit()
    conn.close()

def get_news_url():
    cats = get_all('SELECT * FROM catalogs')
    conn = sqlite3.connect('database/data.db')
    for cat in cats:
        cat_id = cat[0]
        url = cat[2]
        cat_paper = newspaper.build(url)
        for article in cat_paper.articles:
            try:
                print('===', article.url)
                add_news(conn, article.url, cat_id)
            except Exception as ex:
                print('Error' + str(ex))
                pass

    conn.close()

if __name__ == '__main__':
    pass
    # add_comment(50, 'Hello')
    # print(get_news_by_id(52))
    #get_news_url()
    #print(get_all('SELECT * FROM catalogs'))