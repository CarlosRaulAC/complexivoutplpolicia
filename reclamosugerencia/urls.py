from django.urls import path
from .views import ReclamoSugerenciaAdd, ReclamoSugerenciaView
from .reportes import reporte_reclamosugerencia

urlpatterns = [
    path('rs/add',ReclamoSugerenciaAdd.as_view(), name='rs_add'),
    path('rs/',ReclamoSugerenciaView.as_view(), name='rs_list'),

    path('rs/listado',reporte_reclamosugerencia, name='rs_print_all')

]