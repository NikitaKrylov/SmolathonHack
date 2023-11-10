from django.urls import path
from .views import HistoryPostDetailView, EventPostDetailView, HomeView, SearchResultListView, get_search_suggestions

urlpatterns = [
    path('posts/history/<int:pk>/detail/', HistoryPostDetailView.as_view(), name="history_post_detail"),
    path('posts/events/<int:pk>/detail/', EventPostDetailView.as_view(), name="event_post_detail"),
    path('posts/search/', SearchResultListView.as_view(), name="search"),
    path('posts/search/suggestions/', get_search_suggestions, name="search_suggestions"),
    path('', HomeView.as_view(), name="home")

]