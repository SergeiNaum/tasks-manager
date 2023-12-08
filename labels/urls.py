from django.urls import path

from labels import views

urlpatterns = [
    path('', views.LabelsListView.as_view(), name='all_labels'),
    path('create/', views.LabelCreateView.as_view(), name='label_create'),
    path('<int:pk>/update/', views.LabelEditView.as_view(), name='label_update'), # noqa E501
    path('<int:pk>/delete/', views.LabelDeleteView.as_view(), name='label_delete'), # noqa E501
]

app_name = 'labels'
