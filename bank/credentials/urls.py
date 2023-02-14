from django.urls import path
from . import views
app_name = 'credentials'

urlpatterns =[
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('create_account/', views.user_account, name='user_account'),
    path('ajax/load_branches/', views.load_branch, name='ajax_load_branches'),
]