from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('technic/', views.SelectPageView.as_view(), name="technic"),
    #
    # # add sth to base
    # path('add_wo/', views.AddWorkOrderView.as_view(), name="add_workorders"),
    # path('add_aircraft/', views.AddAircraftView.as_view(), name="add-aircraft"),
    # path('add_acmodel/', views.AddAircraftModelView.as_view(), name="add-model"),
    # path('add_task/', views.AddTaskView.as_view(), name="add-task"),
    # path('add_customer/', views.AddCustomerView.as_view(), name="add-customer"),
    # path('add_workcontent/', views.AddWorkContentView.as_view(), name="add-workcontent"),
    #
    # # list objects from base
    # path('aircraft_list/', views.AllAircraftView.as_view(), name="all-aircrafts"),
    # path('wo_list/', views.AllWorkOrderView.as_view(), name="all-workorders"),
    # path('acmodel_list/', views.AllAircraftModelView.as_view(), name="all-models"),
    # path('customer_list/', views.AllCustomerView.as_view(), name="all-customers"),
    #
    # # show specific type
    # path('show_wo/<int:wo_id>/', views.ShowWorkOrder.as_view(), name="show-workorder"),
    # path('show_aircraft/<int:aircraft_id>/', views.ShowAircraft.as_view(), name="show-aircraft"),
    # path('show_tasks/<int:model>/', views.ShowModelTasks.as_view(), name="show-tasks"),
    #
    # # update/edit specific type
    # path('update_wo/<int:wo_id>/', views.UpdateWorkOrderView.as_view(), name="update-workorder"),
    # path('update_aircraft/<int:aircraft_id>/', views.UpdateAircraftView.as_view(), name="update-aircraft"),
    #
    # # delete items
    # path('delete_wo/<int:wo_id>/', views.DeleteWorkOrderView.as_view(), name="delete-workorder"),
    # path('delete_aircraft/<int:aircraft_id>/', views.DeleteAircraftView.as_view(), name="delete-aircraft"),
    # path('delete_acmodel/<int:model_id>/', views.DeleteAircraftModelView.as_view(), name="delete-model"),

]