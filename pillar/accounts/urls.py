from django.urls import include, path, re_path

from accounts.views import UserFormApiView, UserFormCreateApiView, UserUpdateApiView
app_name = "accounts"

urlpatterns = [
    path("", UserFormApiView.as_view(), name="user-api"),
    path("user_create_form", UserFormCreateApiView.as_view(), name="user-create-form-api"),
    path("user/<int:pk>/update", UserUpdateApiView.as_view(), name='user_update_api'),
    
]
