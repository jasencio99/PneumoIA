from .deteccion import deteccion_neumonia
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def deteccion_neumonia_view(request):
    if request.method == 'POST':
        imagen = request.FILES.get('imagen')

        if imagen:
            resultado = deteccion_neumonia(imagen)

            response_data = {'resultado': resultado}

            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'No se proporcionó una imagen válida.'}, status=400)

    return JsonResponse({'error': 'Esta vista solo admite solicitudes POST.'}, status=405)