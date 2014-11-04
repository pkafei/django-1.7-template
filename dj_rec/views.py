from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response, get_object_or_404
from .models import Blog_Rec
from django.template import Context, loader
from haystack.forms import ModelSearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView, search_view_factory


def index(request):
    return render_to_response('templates/index.html', {
        'recommendations': Blog_Rec.objects.all()[:5]
    })



'''
sqs = SearchQuerySet().filter(author='Portia')


urlpatterns = patterns('haystack.views',
    url(r'^$', search_view_factory(
        view_class=SearchView,
        template = 'templates/index.html',
        searchqueryset=sqs,
        form_class=ModelSearchForm
    ), name='haystack_search'),
)

class FacetedSearchView(SearchView):
    def extra_context(self):
        extra = super(FacetedSearchView, self).extra_context()

        if self.results == []:
            extra['facets'] = self.form.search().facet_counts()
        else:
            extra['facets'] = self.results.facet_counts()

        return extra
'''