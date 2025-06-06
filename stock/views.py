from django.shortcuts import render, get_object_or_404, redirect
from .models import Piece
from .forms import PieceForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
# import openpyxl
from django.http import HttpResponse

def est_admin(user):
    return user.is_staff

from django.db.models import Q

# TODO Faire revoir cette partie parceque disponible et reducion ne fonctionne pas
def liste_pieces(request):
    query = request.GET.get('q', '').strip()
    sort   = request.GET.get('sort', 'designation')
    direction = request.GET.get('dir', 'asc')

    # 1. QuerySet de base, filtrage SQL sur les vrais champs
    qs = Piece.objects.all()
    is_num = False
    num_val = None

    if query:
        filt = (
            Q(designation__icontains=query) |
            Q(voiture__icontains=query)
        )
        # test si c'est un nombre (pour quantite et prix_vente)
        try:
            num_val = float(query)
            is_num = True
            filt |= Q(quantite=num_val) | Q(prix_vente=num_val)
        except ValueError:
            pass

        qs = qs.filter(filt)

    # 2. On passe en liste pour filtrer ensuite sur les propriétés Python
    pieces = list(qs)

    if query:
        # disponibilité
        if query.lower() in ('oui', 'non'):
            want = query.lower() == 'oui'
            pieces = [p for p in pieces if p.est_disponible == want]
        # prix réduit
        elif is_num:
            # tolérance pour flottants
            pieces = [
                p for p in pieces
                if abs(float(p.prix_vente_reduction) - num_val) < 1e-2
            ]

    # 3. Tri (QuerySet.order_by ne marche plus sur liste pour les proprietés)
    reverse = (direction == 'desc')
    if sort == 'prix_vente_reduction':
        pieces = sorted(pieces, key=lambda p: p.prix_vente_reduction, reverse=reverse)
    elif sort == 'disponible':
        pieces = sorted(pieces, key=lambda p: p.est_disponible,      reverse=reverse)
    else:
        # tri générique sur attributs Django
        pieces = sorted(pieces, key=lambda p: getattr(p, sort), reverse=reverse)

    # Colonnes pour l’en-tête
    columns = [
        ('designation', 'Désignation'),
        ('voiture',     'Voiture'),
        ('quantite',    'Quantité'),
        ('prix_vente',  'Prix vente'),
        ('prix_vente_reduction', 'Prix réduit'),
        ('disponible',  'Disponible'),
    ]

    return render(request, 'stock/piece_liste.html', {
        'pieces': pieces,
        'query': query,
        'sort': sort,
        'direction': direction,
        'columns': columns,
    })


@user_passes_test(est_admin)
def ajouter_piece(request):
    form = PieceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('stock:liste_pieces')
    return render(request, 'stock/piece_form.html', {'form': form, 'title': 'Ajouter une pièce'})

@user_passes_test(est_admin)
def modifier_piece(request, pk):
    piece = get_object_or_404(Piece, pk=pk)
    form = PieceForm(request.POST or None, instance=piece)
    if form.is_valid():
        form.save()
        return redirect('stock:liste_pieces')
    return render(request, 'stock/piece_form.html', {'form': form, 'title': 'Modifier la pièce'})

@user_passes_test(est_admin)
def supprimer_piece(request, pk):
    piece = get_object_or_404(Piece, pk=pk)
    if request.method == 'POST':
        piece.delete()
        return redirect('stock:liste_pieces')
    return render(request, 'stock/confirm_delete.html', {'piece': piece})

# def import_excel(request):
#     try:
#         if request.method == 'POST' and request.FILES['excel_file']:
#             # On récupère le fichier Excel
#             excel_file = request.FILES['excel_file']
            
#             # On charge le fichier Excel
#             wb = openpyxl.load_workbook(excel_file)
#             sheet = wb.active  # On récupère la première feuille

#             # On parcourt toutes les lignes de la feuille
#             for row in sheet.iter_rows(min_row=2, values_only=True):  # On ignore la première ligne (les entêtes)
#                 designation = row[0]
#                 voiture = row[1]
#                 quantite = row[2]
#                 prix_vente = row[3]
#                 prix_vente_reduction = row[4]
#                 disponible = row[5].lower() == 'oui'  # Si "oui", on considère la pièce disponible

#                 # Crée une nouvelle instance de Piece et enregistre-la
#                 Piece.objects.create(
#                     designation=designation,
#                     voiture=voiture,
#                     quantite=quantite,
#                     prix_vente=prix_vente,
#                     prix_vente_reduction=prix_vente_reduction,
#                     disponible=disponible
#                 )

#             # Rediriger vers la liste des pièces ou afficher un message de succès
#             return redirect('stock:liste_pieces')  # Change cette URL en fonction de ton app

#         else:
#             # Si ce n'est pas un POST, on affiche un formulaire vide
#             form = ImportExcelForm()
#             return render(request, 'stock/import_excel.html', {'form': form})
#     except Exception as e:
#     # Gérer l'exception et informer l'utilisateur
#         return HttpResponse(f"Une erreur s'est produite lors de l'importation : {str(e)}")
