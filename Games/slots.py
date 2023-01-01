class Article:
    def __init__(self, date, writer):
        self.date = date
        self.writer = writer
article = Article("2020-06-01","xiaoxu")
print(article.__dict__)

print(Article.__dict__)

article.reviewer = "jojo"
print(article.__dict__)