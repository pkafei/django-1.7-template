from django.db import models
from django.contrib.auth.models import User


class Blog_Rec(models.Model):
	user = models.ForeignKey(User)
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title
