import datetime
from haystack import indexes
from myapp.models import Blog_Rec


class Blog_Rec_Index(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    admin = indexes.CharField(model_attr='user')
    pub_date = indexes.DateTimeField(model_attr='pub_date')
    author = models.CharField(max_length=200)

    def get_model(self):
        return Blog_Rec

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
