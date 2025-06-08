# Installation du projet Django - Guide étape par étape

## 1. Installer Python

* Télécharge et installe Python (version 3.8 ou supérieure) depuis le site officiel :
  [https://www.python.org/downloads/](https://www.python.org/downloads/)

* Vérifie l’installation dans un terminal (Invite de commandes ou PowerShell sous Windows) avec :

```bash
python --version
```

ou

```bash
python3 --version
```

  Tu dois voir la version installée s’afficher.

---

## 2. Vérifier et installer `pip`

* `pip` est l’outil de gestion des paquets Python (normalement installé avec Python).

* Vérifie qu’il est disponible :

```bash
pip --version
```

* Si ce n’est pas le cas, installe-le en suivant la documentation officielle :
  [https://pip.pypa.io/en/stable/installation/](https://pip.pypa.io/en/stable/installation/)

---

## 3. Installer Django

* Dans un terminal, installe Django via pip :

```bash
pip install django
```

* Vérifie l’installation :

```bash
django-admin --version
```

---

## 4. Cloner le projet depuis GitHub

* Ouvre un terminal et choisis un dossier où tu veux mettre le projet.

* Clone le projet depuis GitHub :

```bash
git clone https://github.com/TabarBaptiste/gestion_stock.git
```

* Accède au dossier du projet :

```bash
cd gestion_stock
```

---

## 5. Lancer le serveur de développement

* Lance le serveur Django :

```bash
python manage.py runserver
```

* Ouvre dans un navigateur :
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

* Tu peux maintenant utiliser le projet avec la base initialisée.
