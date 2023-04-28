from django.urls import re_path
from menus.views import IndexView

app_name = 'menus'

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),
    re_path(r'^(.*)/$', IndexView.as_view(), name='index'),
]
