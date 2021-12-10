1
from django.urls import path
from .views import ListUser,index,comends, show_img, register_trainers, level, wizard_register_trainer, list_user,update_training,training,now_training,new_day, UserDelete, UserUpdate
from django.urls import include


app_name = "home"

urlpatterns = [
    path('index/', index, name='index'),


    path('new_day/', new_day, name='new_day'),
    path('now_training/', now_training, name='now_training'),
    path('training/', training, name='training'),
    path('wizard_register_trainer/', wizard_register_trainer, name='wizard_register_trainer'),
    path('comends/', comends, name="comends"),
    path('user/delete/', UserDelete.as_view(), name="delete-user"),
    path('user/update/<int:pk>/', UserUpdate.as_view(), name="update-user"),
    
    path('register_trainers/', register_trainers, name="register_trainers"),
    path('level/', level, name="level"),
    path('list_user/', ListUser.as_view(), name="list_user"),
    
    path('show_img/', show_img, name="img"),
    path('update_training/', update_training, name="update_training"),
]

#https://demos.creative-tim.com/black-dashboard-django/docs/1.0/getting-started/getting-started-django.html