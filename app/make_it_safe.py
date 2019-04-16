from newspaper import Article, build, news_pool
from urllib.parse import urlsplit, urlunsplit


class SafeArticle:

    def __init__(self, url):
        self.raw_article = self.make_it_safe(url)
        self.title = self.raw_article.title.replace("/", "\\")
        self.text = self.raw_article.text.split("\n")
        self.authors = self.raw_article.authors
        self.pub_date = self.raw_article.publish_date
        self.top_img = self.raw_article.top_image
        self.source = self.set_source(url)

    def make_it_safe(self, url):
        raw_article = Article(url)
        raw_article.download()
        raw_article.parse()
        return raw_article

    def set_source(self, url):
        split_url = urlsplit(self.raw_article.url)
        base_url = (split_url[0], split_url[1], "", "", "")
        raw_source = build(urlunsplit(base_url))
        sauce = [raw_source]
        news_pool.set(sauce, threads_per_source=4)
        news_pool.join()
        for article in raw_source.articles:
            article.parse()
        return raw_source
