from newspaper import Article



class SafeArticle:

    def __init__(self, url):
        self.article = self.make_it_safe(url)
        #self.text = self.article.text
        #self.authors = self.article.authors
        #self.pub_date = self.article.publish_date

    def make_it_safe(self, url):
        raw_article = Article(url)
        raw_article.download()
        raw_article.parse()

        self.set_title(raw_article.title.replace("/", "\\"))
        self.set_text(raw_article.text.split("\n"))
        self.set_authors(raw_article.authors)
        self.set_pub_date(raw_article.publish_date)

    def set_title(self, title):
        self.title = title

    def set_text(self, text):
        self.text = text

    def set_authors(self, authors):
        self.authors = authors

    def set_pub_date(self, pub_date):
        self.pub_date = pub_date




