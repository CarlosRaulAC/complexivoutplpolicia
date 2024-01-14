from django.urls import path
from .views import *

urlpatterns = [

    #url para flota vehicular
    path('vehicular/',FlotaVehicularView.as_view(), name='vehicular_list'),
    path('vehicular/add',FlotaVehicularAdd.as_view(), name='vehicular_add'),
    path('vehicular/update/<int:pk>',FlotaVehicularUpdate.as_view(), name='vehicular_update'),
    path('vehicular/inactivate/<int:id>',flotavehicular_inactivate, name='vehicular_inactivate'),
        


]