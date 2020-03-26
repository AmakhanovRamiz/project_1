
from django.urls import path
from news.views import news_list, new_single

urlpatterns = [
    path('', news_list, name = 'list_news'),
    path('single/<int:pk>', new_single, name = 'new_single')
]