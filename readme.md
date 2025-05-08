# 🔎 Démarche de conception de l'application de gestion de stock

Dans le cadre de ce projet, j’ai choisi de développer une **interface graphique web** plutôt que de me contenter d’un simple fichier Excel. Bien qu’Excel soit un outil accessible et pratique pour gérer de petites quantités de données, il devient vite limité dès que l'on souhaite **centraliser les informations**, **filtrer et trier dynamiquement les données**. Une application web permet d’offrir une **expérience utilisateur plus fluide**, une **meilleure ergonomie**, et surtout une **structure solide** pour faire évoluer le système.

## ⚙️ Pourquoi Python et Django ?

J’ai choisi **Python** car c’est un langage à la fois lisible, puissant et très populaire dans le domaine de l’automatisation. Il permet de se concentrer sur la logique métier sans perdre trop de temps avec des détails techniques complexes.

Pour structurer mon projet, j’ai utilisé le **framework Django**, qui repose sur Python. Django facilite le développement rapide d'applications web robustes grâce à ses nombreux outils intégrés :

* un système d’authentification prêt à l’emploi,
* une interface d’administration automatique,
* un ORM (Object Relational Mapper) pour manipuler la base de données sans écrire de SQL brut,
* et une structure MVC claire.

En utilisant Django, j’ai pu gagner du temps, sécuriser mon application et organiser mon code de façon propre et évolutive.

### 🗄️ Utilisation de SQLite

Pour la base de données, j’ai opté pour **SQLite**. Ce choix est justifié par le contexte du projet : une application locale, sans besoin de serveur distant ou de gestion multi-utilisateur complexe. SQLite est un moteur de base de données **léger**, **intégré directement dans Django** par défaut, et **suffisamment performant** pour ce type d’usage. Il m’a permis de me concentrer sur la logique métier sans me préoccuper de la configuration d’un serveur de base de données.

Parfait ! Voici un **nouveau paragraphe** que tu peux insérer dans ton rapport, expliquant clairement la **structure du code et les étapes de mise en place du projet Django** :

---

## 🧱 Mise en place du projet et structure du code

Avant de commencer le développement, j’ai dû m’assurer d’avoir **Python installé** sur ma machine. Python est le langage de programmation utilisé par Django. Une fois Python installé, j’ai vérifié que **`pip`**, le gestionnaire de paquets Python, était bien fonctionnel. Cela m’a permis d’installer facilement Django en exécutant la commande :

```bash
pip install django
```

Ensuite, j’ai créé mon projet Django avec la commande suivante :

```bash
django-admin startproject gestion_stock
```

Cette commande a généré la structure de base du projet avec les éléments suivants :

* un dossier principal `gestion_stock/` contenant les **fichiers de configuration du projet** (comme `settings.py`, `urls.py`) ;
* un fichier `manage.py` qui permet de lancer des commandes utiles comme démarrer le serveur, faire des migrations ou créer des utilisateurs.

Pour lancer le serveur de développement et tester que tout fonctionnait correctement, j’ai utilisé la commande :

```bash
python manage.py runserver
```

Une fois le projet fonctionnel, j’ai créé une **application interne nommée `stock`**, qui contient toute la logique métier spécifique à la gestion de pièces. La commande utilisée a été :

```bash
python manage.py startapp stock
```

Django fonctionne de manière modulaire : un projet peut contenir plusieurs applications, chacune responsable d’un domaine particulier. Dans mon cas, `stock` est l’application principale, chargée de gérer les **modèles**, **vues**, **formulaires** et **templates** liés aux pièces.

Très bien ! Voici une suite claire et structurée que tu peux intégrer à ton rapport, concernant la création du modèle, la migration de la base de données, la création d’un superutilisateur, l’utilisation de `admin.py`, et le fichier `models.py`.

---

## 📦 Modélisation des données et configuration de l’administration

### 1. Définition du modèle (`models.py`)

Dans le fichier `models.py` de l’application `stock`, j’ai défini la structure des données que l’application va manipuler. Ici, le modèle principal s’appelle `Piece` et représente une pièce détachée avec plusieurs attributs : désignation, voiture, quantité, prix, réduction, etc.

Voici un exemple simplifié de ce modèle :

```python
from django.db import models
from decimal import Decimal

class Piece(models.Model):
    quantite = models.PositiveIntegerField()
    designation = models.CharField(max_length=50, unique=True)
    voiture = models.CharField(max_length=255, null=True, blank=True)
    
    prix_brut = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    prix_net = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    prix_montant = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    prix_vente = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    reduction = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))  # en pourcentage

    def __str__(self):
        return f"{self.designation} - {self.voiture} (x{self.quantite}) | {self.prix_vente_reduction}€"

    @property
    def prix_vente_reduction(self):
        """Prix de vente après application de la réduction."""
        return self.prix_vente * (1 - (self.reduction / 100))

    @property
    def est_disponible(self):
        """Retourne True si la pièce est disponible (quantité > 0)."""
        return self.quantite > 0
```

Ce modèle sera traduit automatiquement en table de base de données par Django grâce au système de **migrations**.

---

### 2. Migration de la base de données

Une fois le modèle défini, j’ai utilisé les commandes suivantes pour que Django crée la structure correspondante dans la base de données :

```bash
python manage.py makemigrations
python manage.py migrate
```

* `makemigrations` génère un fichier de migration (instructions de modification de la base).
* `migrate` exécute ces instructions sur la base de données (ici SQLite ou MySQL, selon la configuration).

---

### 3. Création du superutilisateur

Pour accéder à l’interface d’administration de Django (backend), j’ai créé un **superutilisateur** avec cette commande :

```bash
python manage.py createsuperuser
```

Django m’a alors demandé un nom d’utilisateur, un mot de passe, et une adresse email.

---

### 4. Configuration de l’administration (`admin.py`)

Django possède une interface d’administration très puissante. Pour que le modèle `Piece` soit visible et gérable dans l’interface admin, j’ai ajouté ce code dans `stock/admin.py` :

```python
from django.contrib import admin
from .models import Piece

admin.site.register(Piece)
```

Cela permet de :

* lister les pièces avec les colonnes personnalisées ;
* ajouter une barre de recherche dans l’admin ;
* éditer les objets en quelques clics via l’interface.

Parfait, continuons avec l’explication de la **structure de l’interface web**. Django utilise une architecture appelée **MTV** (Model – Template – View), ce qui est une variante du modèle MVC.

---

## 🖥️ Mise en place de l’interface web

L’objectif de cette partie du projet était de permettre à l’utilisateur de **visualiser, rechercher, trier, ajouter, modifier ou supprimer des pièces** via une interface graphique conviviale. Pour cela, j’ai utilisé :

* `urls.py` pour gérer les routes ;
* `views.py` pour le traitement logique ;
* `forms.py` pour les formulaires ;
* les fichiers `HTML` (templates) pour l’affichage ;
* Bootstrap pour le style.

---

### 1. `urls.py` – Définir les chemins de l’application

Dans le fichier `stock/urls.py`, j’ai défini toutes les URL liées à la gestion des pièces. Par exemple :

```python
from django.urls import path
from . import views

app_name = "stock"

urlpatterns = [
    path('', views.liste_pieces, name='liste_pieces'),
    path('ajouter/', views.ajouter_piece, name='ajouter_piece'),
    path('modifier/<int:pk>/', views.modifier_piece, name='modifier_piece'),
    path('supprimer/<int:pk>/', views.supprimer_piece, name='supprimer_piece'),
    path('import_excel/', views.import_excel, name='import_excel'),
]
```

Chaque URL est liée à une fonction dans le fichier `views.py`.

---

### 2. `views.py` – La logique métier

Les **vues** sont des fonctions Python qui récupèrent les données et les transmettent aux templates HTML. Par exemple :

```python
def liste_pieces(request):
    pieces = Piece.objects.all()
    return render(request, 'stock/piece_liste.html', {'pieces': pieces})
```

J’ai aussi implémenté un **formulaire de recherche et de tri**.

---

### 3. `forms.py` – Création des formulaires

Pour faciliter la création et la modification des objets `Piece`, j’ai utilisé un **formulaire Django** :

```python
from django import forms
from .models import Piece

class PieceForm(forms.ModelForm):
    class Meta:
        model = Piece
        fields = '__all__'
```

Ce fichier m’a permis de générer automatiquement les champs HTML dans les templates, avec validation et sécurité intégrée (CSRF, vérification des types, etc.).

---

### 4. Templates HTML – Affichage des pages

Django utilise un langage de template pour afficher les données. J’ai utilisé des fichiers `.html` dans le dossier `templates/stock/`, comme :

* `piece_liste.html` : pour afficher la liste des pièces avec tri et recherche.
* `piece_form.html` : pour ajouter ou modifier une pièce.
* `header.html` : entête pour uniformiser l’interface.

J’ai également intégré **Bootstrap 5** pour améliorer l’esthétique de l’interface : couleurs douces, bordures arrondies, ombres portées, boutons stylisés, etc.
