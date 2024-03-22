from django.urls import path
from .views import *

urlpatterns = [

    #url para movilizaicon
    path('orden/',CombustibleView.as_view(), name='orden_list'),
    path('orden/new',CombustibleAdd.as_view(), name='orden_add'),
    path('orden/update/<int:pk>',CombustibleUpdate.as_view(), name='orden_update'),
    path('orden/inactivate/<int:id>',combustible_inactivate, name='orden_inactivate'),
]