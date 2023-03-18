from django.db import models


class Post(models.Model):
    article = models.CharField(
        max_length=50,
    )
    text = models.TextField()
    time_in = models.DateTimeField(
        auto_now_add=True
    )
    name_author = models.TextField()


    def __str__(self):
        return f'{self.article.title()}: {self.text[:20]}'



