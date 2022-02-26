from django.urls import path

from . import views

urlpatterns = [
    path('get_table', views.TableAPIView.as_view()),
]
