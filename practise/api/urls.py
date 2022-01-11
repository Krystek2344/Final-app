from django.urls import path
from . import views

app_name = 'practise'

urlpatterns = [
    path('acmodels/', views.ACModelListView.as_view(), name='acmodel_list'),
    path('acmodel/<pk>/', views.ACModelDetailView.as_view(), name='acmodel_detail'),

    path('aircrafts/', views.AircraftListView.as_view(), name='aircraft-list'),
    path('aircraft/<pk>', views.AircraftDetailView.as_view(), name='aircraft-detail'),
]