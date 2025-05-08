# 📦 Gestion de Stock

Application Web de gestion de stock développée avec **Django**, **Bootstrap** et **SQLlite**, destinée à faciliter le suivi, l'importation, l'édition et la visualisation de pièces mécaniques (dans un contexte aéronautique).

---

## 🚀 Fonctionnalités

<!-- ### 🔐 Authentification

- Connexion, inscription, déconnexion des utilisateurs
- Accès limité aux fonctionnalités d'administration pour les utilisateurs staff -->

### 📋 Gestion des pièces

- Affichage de la liste des pièces
- Ajout, modification, suppression des pièces (réservé aux administrateurs)
- Champ "disponible" automatiquement basé sur la quantité
- Calcul automatique du **prix de vente avec réduction**
- Affichage dynamique des prix, quantité et disponibilité

### 🔍 Filtrage et Tri

- Barre de recherche dynamique
- Tri possible par : Désignation, Voiture, Quantité, Prix de vente, Prix réduit, Disponibilité
<!-- - Filtrage intelligent avec prise en charge de :
  - Texte (ex: nom de la pièce ou voiture)
  - Numérique (prix ou quantité)
  - Booléen (ex: disponible = oui / non) -->

### 📁 Import/Export Excel (en cours)

- Importation de pièces depuis un fichier Excel `.xlsx`
- Insertion directe dans la base de données après lecture du fichier
- Export possible à venir

<!-- ### 🎨 Interface utilisateur

- Design responsive avec **Bootstrap 5**
- Header avec navigation (Accueil, Historique, Importer, Connexion...)
- Utilisation d’une palette de couleurs agréable (ombres, arrondis, mise en forme claire) -->

---

## 🧰 Stack Technique

| Outil        | Rôle                         |
|--------------|------------------------------|
| Django       | Framework backend principal  |
| SQLlite        | Base de données|
| Bootstrap 5  | Mise en page responsive      |
| HTML / CSS   | Frontend                     |
| openpyxl     | Manipulation de fichiers Excel|
| Python 3.11+ | Langage principal             |

---
<!-- 
## 📂 Structure du projet

```
gestion\_stock/
│
├── stock/                # App principale
│   ├── models.py         # Modèle "Piece"
│   ├── views.py          # Vue liste, ajout, import...
│   ├── templates/        # Templates HTML (Bootstrap)
│   └── urls.py
│
├── media/                # Fichiers importés (Excel)
├── static/               # CSS / JS (si besoin)
├── db.sqlite3            # (ou connexion MySQL)
└── manage.py
```` -->

---

<!-- ## ▶️ Lancer le projet en local

1. **Cloner le projet :**

```bash
git clone https://github.com/votre-utilisateur/gestion-stock.git

cd gestion-stock
````

2. **Installer les dépendances :**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configurer la base de données dans `settings.py`**

4. **Migrer la base de données :**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Créer un superutilisateur :**

   ```bash
   python manage.py createsuperuser
   ```

6. **Lancer le serveur :**

   ```bash
   python manage.py runserver
   ```

--- -->

## ✍️ Auteur

Développé par `Shrek` - Projet de formation

---

## 📜 Licence

Projet open-source sous licence MIT.
