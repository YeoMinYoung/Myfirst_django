from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200) 
    #CharField max_length = 200  = 짧은 글
    created_at = models.DateTimeField(auto_now_add=True)
    #DateTimeField = 지금시간 자동으로 추가 허용
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()

    def __str__(self):
        return self.title
