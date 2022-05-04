class Articles:
    
    def __init__(self, author, title, description, url, urlToImage, publishedAt, content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content  

class Source:
    """
    News source class to define the objects
    """
    def __init__(self,id,name,description,url,category):
        self.id=id
        self.name=name
        self.description=description
        self.url=url
        self.category=category