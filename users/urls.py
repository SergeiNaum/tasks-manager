from django.urls import path
from users import views

urlpatterns = [
    path("", views.UsersIndexView.as_view(), name="users_index"),
    path("create/", views.RegisterUser.as_view(), name="register"),
    path("create/done", views.RegisterDone.as_view(), name="register_done"),
    path("<int:pk>/update/", views.UserEditView.as_view(), name="edit_user"),
    path(
        "<int:pk>/delete/", views.UserDeleteView.as_view(), name="delete_user"
    ),  # noqa E501

]

app_name = "users"
