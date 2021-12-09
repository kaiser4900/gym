from django.urls import path
from django.urls import path
from .views import TaskDeleteView2,create_view, list_view, detail_view, update_view, delete_view, TaskListView

app_name = "ExerciseModel"

urlpatterns = [
    path('create/', create_view, name='create'),
    path('list/', TaskListView.as_view(), name='list'),
    path('<id>', detail_view ),
    path('<id>/update', update_view ),
    path('delete/<pk>', TaskDeleteView2.as_view(), name="delete"), 
]

#https://demos.creative-tim.com/black-dashboard-django/docs/1.0/getting-started/getting-started-django.html