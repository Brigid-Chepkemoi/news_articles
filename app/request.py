from unicodedata import category
from app import app
from app.models.news_source import Source
import urllib.request,json
from app.instance.config import NEWS_API_KEY

News = Source

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
    
    return news_results_list;

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