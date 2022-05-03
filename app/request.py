from unicodedata import category
from app import app
from app.models.news_source import Source
import urllib.request,json
from app.instance.config import NEWS_API_KEY, ARTICLES_API_BASE_URl
from app.models.news_article import Articles


# News = Source
# Artics = Articles

base_url = app.config['NEWS_API_BASE_URL']

def get_news(category):
    get_news_url = base_url.format(category,NEWS_API_KEY)

    #with urllib.request.urlopen(get_news_url).read()  as url:
        # get_news_data =url.read()
    get_news_data=urllib.request.urlopen(get_news_url).read()
    get_news_response = json.loads(get_news_data)

    if get_news_response['sources']:
        news_results_list= get_news_response['sources']
        #news_results = process_results(news_results_list)
    
    return news_results_list

# def process_results(news_list):
#     news_results = []
#     for news_item in news_list:
#         id = news_item.get('id')
#         name = news_item.get('name')
#         description = news_item.get('description')
#         url = news_item.get('url')
#         category = news_item.get('category')
#         if url:
#             news_object = News(id,name,description,url,category)
#             news_results.append(news_object)  
#     return news_results
def get_articles(source_id):
    '''
        Function that gets the json response to our url request using the source id
    '''
    get_articles_url = ARTICLES_API_BASE_URl.format(
        source_id, NEWS_API_KEY)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles_results(articles_results_list)
    print(articles_results)
    return articles_results

def process_articles_results(articles_list):
    '''
    Function to processes articles list result and transform them to a list of Objects
    '''
    articles_results = []
    for article_item in articles_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        if url:
            articles_object = Articles(
                author, title, description,url,urlToImage,publishedAt,content)
            articles_results.append(articles_object)

    return articles_results