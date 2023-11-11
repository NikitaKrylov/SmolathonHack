from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.generic import DetailView, TemplateView, ListView, FormView
# from account.models import CheckInURL
from posts.models import HistoryPost, EventPost, PlaceTest, PlaceTestResult
from posts.forms import PostSearchForm
from posts.repository.smoladmin import SmoladminRepository


class HomeView(TemplateView):
    template_name = 'posts/home.html'
    repository: SmoladminRepository = SmoladminRepository()


class CHistoryPostListView(ListView):
    model = HistoryPost


class EventPostListView(ListView):
    model = EventPost


class HistoryPostDetailView(DetailView):
    model = HistoryPost
    template_name = "posts/culture_detail.html"
    context_object_name = "post"


class EventPostDetailView(DetailView):
    model = EventPost
    template_name = "posts/event_detail.html"
    context_object_name = "post"


class PlaceTestView(DetailView):
    model = PlaceTest
    template_name = 'posts/play.html'
    context_object_name = 'test'

    def get_object(self, queryset=None):
        return PlaceTest.objects.filter(id=self.kwargs['id']).first()


class PlaceTestPreview(DetailView):
    model = PlaceTest
    template_name = 'posts/qr.html'
    context_object_name = 'test'

    def get_object(self, queryset=None):
        return PlaceTest.objects.filter(id=self.kwargs['id']).first()


class SearchResultListView(ListView):
    model = EventPost
    paginate_by = 30
    form_class = PostSearchForm
    context_object_name = 'posts'
    template_name = "posts/search.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = self.form_class(data={'search_text': self.request.GET.get('search_text', '')})
        return context

    def get_queryset(self):
        search_text = self.request.GET.get('search_text', '')
        print(search_text)
        return EventPost.objects.filter(self._build_query(search_text))

    def _build_query(self, search_text: str) -> Q:
        query = Q()

        for word in search_text.split():
            query |= Q(title__icontains=word)
            query |= Q(description__contains=word)
            query |= Q(category__contains=word)
            query |= Q(category__contains=word)

        return query


def get_search_suggestions(request, *args, **kwargs):
    # all_categories = set(EventPost.objects.values_list('category', flat=True)) | set(EventPost.objects.values_list('subcategory', flat=True) )
    search_text = request.GET.get('text').split()[0]
    # result = all_categories & search_text
    query = Q()
    query |= Q(title__icontains=search_text)
    query |= Q(description__icontains=search_text)
    query |= Q(category__icontains=search_text)
    query |= Q(category__icontains=search_text)

    result = [(post.title, post.get_absolute_url()) for post in EventPost.objects.filter(query)]

    return JsonResponse(result, safe=False, content_type="application/json; encoding=utf-8")


@xframe_options_exempt
def render_test(request, *args, **kwargs):
    return render(request, 'posts/test.html')


@xframe_options_exempt
def render_after(request, *args, **kwargs):
    return render(request, 'posts/afterPlay.html')



