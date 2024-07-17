from django.urls import path, include
from . import views
app_name = "osn"
urlpatterns = [
path('main',views.index),
path('main/<int:my_id>/', views.infbook),
path('main/add', views.add),
path('main/<int:my_id>/upd', views.upd,name="upd"),
path('main/<int:my_id>/del', views.deli,name="del"),
path('main/<int:my_id>/t', views.te,name="t"),
path('main/books', views.bookq,name="book"),
]