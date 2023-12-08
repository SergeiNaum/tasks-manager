from django.urls import path

from tasks import views


urlpatterns = [
    path('', views.TasksListView.as_view(), name='tasks'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='task_show'),
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/update/', views.TaskEditView.as_view(), name='task_update'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'), # noqa E501

]

app_name = "tasks"
