from django.shortcuts import render,get_object_or_404  
from django.http import HttpResponse,JsonResponse,HttpResponseBadRequest
from .utils.scrapper import Scraper
from .utils.call_procedure import call_Procedure
import os
import requests
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from .models  import paises_detalle
# Create your views here.

def hello(request):
    return HttpResponse("<h1> Como estas pa </h1> ") 


def get_paises_api(request):
    if request.method == 'GET':
        countries = list(paises_detalle.objects.values())
        return JsonResponse(countries, safe=False)


@csrf_exempt
def del_paises_api(request, country_id):
    if request.method == 'DELETE':
        if country_id:
            try:
                country = get_object_or_404(paises_detalle, id=country_id)
                country.is_active = False
                country.save()
                return JsonResponse({"message": "Pais logicamente eliminado exitosamente"})
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=400)
        else:
            return HttpResponseBadRequest("UUID del pais es necesario")
    else:
        return HttpResponseBadRequest("Metodo erroneo, usa DELETE")

@csrf_exempt
def undo_delete_api(request, country_id):
    if request.method == 'PUT':
        try:
            country = get_object_or_404(paises_detalle, id=country_id)
            country.is_active = True
            country.save()
            return JsonResponse({"message": "Pais logicamente activado exitosamente"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return HttpResponseBadRequest("Metodo erroneo, usa PUT")





        


    
