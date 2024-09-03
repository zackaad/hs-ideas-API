
from django.contrib import admin
from django.urls import path
from hs_ideas_main.views import MyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MyView.as_view(), name="my-view"),
]
