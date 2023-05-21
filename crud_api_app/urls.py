from django.urls import path
from .views import GetAllUsersView, CreateUserView, DeleteUserView, GetUserView, EditUserView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('view', GetAllUsersView.as_view(), name='get_all_users'),
    path('viewuser/<str:name>', GetUserView.as_view(), name='get_user'),
    path('create', csrf_exempt(CreateUserView.as_view()), name='create_user'),
    path('delete/<str:name>', csrf_exempt(DeleteUserView.as_view()), name='delete_user'),
    path('edit/<str:name>', csrf_exempt(EditUserView.as_view()), name='edit_user'),
]