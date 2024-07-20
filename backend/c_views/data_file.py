import csv
import json
import os
import pandas as pd
from io import StringIO 
from django.http import HttpResponse,JsonResponse,HttpResponseBadRequest
import requests
from ..utils.call_procedure import call_Procedure
from ..utils.scrapper import Scraper 
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def json_to_csv(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Convertimos JSON a Dataframe
            df = pd.DataFrame(data)
            
            # Eliminamos columnas innecesarias
            df = df.drop(columns=['id', 'is_active'])
            
            # Creamos un buffer para el csv
            csv_buffer = StringIO()
            df.to_csv(csv_buffer, index=False)
            
            csv_buffer.seek(0)
            
            # Creamos una respuesta http con el archicvo
            response = HttpResponse(csv_buffer, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="data.csv"'
            return response
        
        except json.JSONDecodeError as e:
            return JsonResponse({"error": "Datos JSON Invalidos"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Metodo Request Invalido, usa POST"}, status=405)

@csrf_exempt
def random_delete(request, num_rows):
    if request.method == 'DELETE':
        print(type(num_rows))
        db = call_Procedure()
        try: 
            db.call_procedure('delete_random_rows', num_rows)
            db.close()
            return JsonResponse({"message": f"{num_rows} filas aleatorias eliminadas exitosamente"})
        except Exception as e:
            db.close()
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return HttpResponseBadRequest("Metodo Request Erroneo, usa DELETE")
    
def store_countries(request): 
    url = "https://www.scrapethissite.com/pages/simple/"
    file_path = os.path.join(os.path.dirname(__file__), 'storage\scraped_countries.txt')
    # Inicializamos las dependencias
    scraper = Scraper(url, file_path)
    db = call_Procedure()
    
    try:
        #Obtenemos los datos realizados por el webscrapping
        data = scraper.scrape_and_store()
        #insertamos los datos con la clase llamada
        for country in data:
            db.call_procedure(
                'insert_verif_country',
                country['name'],
                country['capital'],
                country['population'],
                country['area']
            ) 
        db.close()
        return JsonResponse({"message": "Datos obtenidos y guardados"})
    
    except requests.HTTPError as e:
        db.close()
        return HttpResponse(f"Fracaso al obtener la pagina: {e}", status=e.response.status_code) 