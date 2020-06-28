from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    poll_no = models.IntegerField(default=0)
    anon = models.BooleanField(default=False)

    def __str__(self):
            return self.content[:5]

    @property
    def number_of_comments(self):
        return Comment.objects.filter(post_id=self).count()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    comment = models.TextField(max_length=150)    
