from django.urls import path
from . import views

app_name = "stock"

urlpatterns = [
    path('', views.liste_pieces, name='liste_pieces'),
    path('ajouter/', views.ajouter_piece, name='ajouter_piece'),
    path('modifier/<int:pk>/', views.modifier_piece, name='modifier_piece'),
    path('supprimer/<int:pk>/', views.supprimer_piece, name='supprimer_piece'),
    # path('import_excel/', views.import_excel, name='import_excel'),
]
