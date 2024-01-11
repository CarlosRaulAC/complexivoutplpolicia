from django.urls import path
from .views import Tipo_VehiculoView, Tipo_VehiculoAdd, Tipo_VehiculoUpdate, tipo_vehiculo_inactivate
from .views import Tipo_MantenimientoView, Tipo_MantenimientoAdd, Tipo_MantenimientoUpdate, tipo_mantenimiento_inactivate
from .views import RangoView, RangoAdd, RangoUpdate, rango_inactivate

urlpatterns = [
    #url para tipo de vehiculo
    path('tipo_vehiculo/',Tipo_VehiculoView.as_view(), name='tipo_vehiculo_list'),
    path('tipo_vehiculo/add',Tipo_VehiculoAdd.as_view(), name='tipo_vehiculo_add'),
    path('tipo_vehiculo/update/<int:pk>',Tipo_VehiculoUpdate.as_view(), name='tipo_vehiculo_update'),
    path('tipo_vehiculo/inactivate/<int:id>',tipo_vehiculo_inactivate, name='tipo_vehiculo_inactivate'),

    #url para tipo de mantenimiento
    path('tipo_mantenimiento/',Tipo_MantenimientoView.as_view(), name='tipo_mantenimiento_list'),
    path('tipo_mantenimiento/add',Tipo_MantenimientoAdd.as_view(), name='tipo_mantenimiento_add'),
    path('tipo_mantenimiento/update/<int:pk>',Tipo_MantenimientoUpdate.as_view(), name='tipo_mantenimiento_update'),
    path('tipo_mantenimiento/inactivate/<int:id>',tipo_mantenimiento_inactivate, name='tipo_mantenimiento_inactivate'),

    #url para rango
    path('rango/',RangoView.as_view(), name='rango_list'),
    path('rango/add',RangoAdd.as_view(), name='rango_add'),
    path('rango/update/<int:pk>',RangoUpdate.as_view(), name='rango_update'),
    path('rango/inactivate/<int:id>',rango_inactivate, name='rango_inactivate'),

]
