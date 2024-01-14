from django.urls import path
from .views import * 

urlpatterns = [

    #url para provincia
    path('provincia/',ProvinciaView.as_view(), name='provincia_list'),
    path('provincia/add',ProvinciaAdd.as_view(), name='provincia_add'),
    path('provincia/update/<int:pk>',ProvinciaUpdate.as_view(), name='provincia_update'),
    path('provincia/inactivate/<int:id>',provincia_inactivate, name='provincia_inactivate'),

    #url para distrito
    path('distrito/',DistritoView.as_view(), name='distrito_list'),
    path('distrito/add',DistritoAdd.as_view(), name='distrito_add'),
    path('distrito/update/<int:pk>',DistritoUpdate.as_view(), name='distrito_update'),
    path('distrito/inactivate/<int:id>',distrito_inactivate, name='distrito_inactivate'),

    #url para canton
    path('canton/',CantonView.as_view(), name='canton_list'),
    path('canton/add',CantonAdd.as_view(), name='canton_add'),
    path('canton/update/<int:pk>',CantonUpdate.as_view(), name='canton_update'),
    path('canton/inactivate/<int:id>',canton_inactivate, name='canton_inactivate'),

    #url para circuito
    path('circuito/',CircuitoView.as_view(), name='circuito_list'),
    path('circuito/add',CircuitoAdd.as_view(), name='circuito_add'),
    path('circuito/update/<int:pk>',CircuitoUpdate.as_view(), name='circuito_update'),
    path('circuito/inactivate/<int:id>',circuito_inactivate, name='circuito_inactivate'),

    #url para subcircuito
    path('subcircuito/',SubcircuitoView.as_view(), name='subcircuito_list'),
    path('subcircuito/add',SubcircuitoAdd.as_view(), name='subcircuito_add'),
    path('subcircuito/update/<int:pk>',SubcircuitoUpdate.as_view(), name='subcircuito_update'),
    path('subcircuito/inactivate/<int:id>',subcircuito_inactivate, name='subcircuito_inactivate'),


]