from django.urls import path   
from . import views  
from .c_views import data_file
urlpatterns = [ 
    path('getcsv/', data_file.json_to_csv, name='json_to_csv'), # Crear y descargar un archivo csv en base a un json enviado 
                                                                
    path('scrap/', data_file.store_countries, name='store_countries'), # ruta para iniciar el webscrapping y rellenar la base de datos
                                                                       
    path('del_random/<int:num_rows>', data_file.random_delete, name='random_delete'), # eliminar datos random de la BD en base a una cantidad definida
                                                                                      
    path('paises/', views.get_paises_api, name='paises_api'),# obtener ls datos guardados en la bd
                                                                
    path('paises/<uuid:country_id>/', views.del_paises_api, name='del_paises_api'), # eliminar logicamente un registro
                                                                                   
    path('paises_activate/<uuid:country_id>/', views.undo_delete_api, name='undo_delete_api'), # activar nuevamente un registro
]