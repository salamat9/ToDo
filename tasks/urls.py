from django.urls import path
from . import views


urlpatterns = [
    # category urls
    path('category/create/', views.create_category, name='create_category'),
    path('categories/', views.category_list, name='category_list'),
    path('category/<int:pk>/edit/', views.edit_category, name='category_edit'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),

    # tasks urls
    path('', views.task_list, name='task_list'),
    path('<int:category_pk>/', views.task_list, name='task_list_by_category'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('create/', views.create_task, name='task_create'),
    path('<int:pk>/delete/', views.delete_task, name='task_delete'),

    # tags urls
    path('tags/<int:pk>/', views.tag_detail, name='tag_detail')
]