from django.db import models


class PyArticles(models.Model):

    title = models.CharField(max_length=120)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.title