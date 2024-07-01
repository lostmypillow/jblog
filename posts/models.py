from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)  # Example field

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    body = models.TextField()
    tags = models.JSONField()  # Storing tags as a JSON array
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
