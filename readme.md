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
