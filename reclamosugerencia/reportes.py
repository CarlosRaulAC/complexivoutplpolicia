from django.forms import IntegerField
from django.utils import timezone
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from .models import ReclamoSugerencia
from django.shortcuts import render
from .models import ReclamoSugerencia
from datetime import datetime, timedelta
from django.db.models import Count
from django.db.models import Count, Sum, Case, When

def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path=result[0]
    else:
        sUrl = settings.STATIC_URL        # Typically /static/
        sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL         # Typically /media/
        mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

        # make sure that file exists
        if not os.path.isfile(path):
            raise RuntimeError(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path
    
def reporte_reclamosugerencia1(request):
    template_path = 'reclamosugerencia/reclamosugerencia_print_all.html'
    today = timezone.now()

    reclamosugerencia = ReclamoSugerencia.objects.all()
    context = {
        'obj': reclamosugerencia,
        'today': today,
        'request': request
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline'; filename="todos_reclamosugerencia.pdf"
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response 

def reporte_reclamosugerencia(request):
    template_path = 'reclamosugerencia/reclamosugerencia_print_all.html'
    fecha_inicio_str = request.GET.get('fecha_inicio', None)
    fecha_fin_str = request.GET.get('fecha_fin', None)

    if fecha_inicio_str and fecha_fin_str:
        # Convierte las cadenas de fecha a objetos datetime
        fecha_inicio = datetime.strptime(fecha_inicio_str, '%d/%m/%Y')
        fecha_fin = datetime.strptime(fecha_fin_str, '%d/%m/%Y')

        #Realiza la consulta filtrando por las fechas proporcionadas y agrupa por tipo, circuito y subcircuito
        reclamos_sugerencias = ReclamoSugerencia.objects.filter(
            fc__range=[fecha_inicio, fecha_fin + timedelta(days=1)]
        ).values(
            'tipo', 'circuito__nombre', 'subcircuito__nombre',
        ).annotate(
            total=Count('id'),
        ).order_by('subcircuito__nombre', 'tipo')

        reporte = []
        for d in reclamos_sugerencias:
            reporte.append([
                fecha_inicio, 
                fecha_fin,
                d['total'],
                d['tipo'],
                d['circuito__nombre'],
                d['subcircuito__nombre'],
            ])
    
        #reclamos_sugerencias = ReclamoSugerencia.objects.all()

        # Renderiza el template del reporte con los totales
        context = {
            'obj': reclamos_sugerencias,
            'today': datetime.now(),
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin,
            'request': request
        }
        print("Contexto:", context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline'; filename="todos_reclamosugerencia.pdf"
        template = get_template(template_path)
        html = template.render(context)

        # crea el documento pdf
        pisa_status = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
        # if error then show some funny view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response 
    else:
        # Maneja el caso cuando las fechas no están disponibles
        return HttpResponse("Por favor, proporciona fechas de inicio y fin.")
