from distutils.debug import DEBUG


class Config:
    # NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines/sources?/{}?&language=en&from=2022-04-16&apiKey={}'
    NEWS_API_BASE_URL= 'https://newsapi.org/v2/top-headlines/sources?category={}&language=en&from=2022-04-16&apiKey={}'
    ARTICLES_API_BASE_URl = 'https://newsapi.org/v2/everything?q={}&sortBy=popularity&apiKey={}'
class ProdConfig(Config):
    pass

class DevConfig(Config):
    '''
        Class to define the environment
    '''
DEBUG = True

