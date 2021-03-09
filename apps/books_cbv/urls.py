from django.urls import path
from django.urls import include
from rest_framework import routers
  
from . import views

app_name = 'books_cbv'

router = routers.DefaultRouter()
router.register(r"books", views.BookViewSet)

urlpatterns = [
  path('', views.BookList.as_view(), name='book_list'),
  path('new/', views.BookCreate.as_view(), name='book_new'),
  path('edit/<int:pk>/', views.BookUpdate.as_view(), name='book_edit'),
  path('delete/<int:pk>/', views.BookDelete.as_view(), name='book_delete'),
  path("api/", include(router.urls)),
]
