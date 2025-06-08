from django.urls import path
from . import views

app_name = "stock"

urlpatterns = [
    path('', views.liste_pieces, name='liste_pieces'),
    path('ajouter/', views.ajouter_piece, name='ajouter_piece'),
    path('modifier/<int:pk>/', views.modifier_piece, name='modifier_piece'),
    path('supprimer/<int:pk>/', views.supprimer_piece, name='supprimer_piece'),
    path('login/', views.user_login, name='login'),
    path('inscription/', views.inscription, name='inscription'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),

    # path('import_excel/', views.import_excel, name='import_excel'),
]
