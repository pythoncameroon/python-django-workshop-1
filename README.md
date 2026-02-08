# ActiveShare Platform

Une plateforme web permettant aux entreprises d'émettre et de vendre des actions, et aux investisseurs de les acheter.

##  Description

Ce projet est une application développée avec Django qui facilite la gestion et l'échange d'actions d'entreprises. Le système met en relation deux types d'utilisateurs principaux :

*   **ShareHolders (Actionnaires/Entreprises)** : Ils peuvent créer et émettre des actions sur la plateforme.
*   **Buyers (Acheteurs/Investisseurs)** : Ils peuvent consulter et acheter les actions disponibles.

##  Fonctionnalités Clés

*   **Gestion des Utilisateurs** : Système d'authentification et de rôles (Acheteur vs Actionnaire).
*   **Émission d'Actions** : Les entreprises (ShareHolders) peuvent créer de nouvelles actions (1 ou plusieurs).
*   **Achat d'Actions** : Les investisseurs (Buyers) peuvent acquérir des actions (0 ou plusieurs).
*   **Tableau de Bord** : Vue d'ensemble des actifs pour les acheteurs et des émissions pour les entreprises.

##  Technologies Utilisées

*   **Backend** : Python, Django
*   **Base de données** : SQLite (par défaut pour le développement)
*   **Gestionnaire de paquets** : uv

##  Installation et Lancement

Ce projet utilise [uv](https://github.com/astral-sh/uv) pour la gestion des dépendances, ce qui est beaucoup plus rapide que pip standard.

### Prérequis

*   Python 3.x installé
*   `uv` installé (si ce n'est pas fait : `pip install uv` ou via PowerShell)

### Étapes d'installation

1.  **Cloner le dépôt :**

    ```bash
    git clone <votre-repo-url>
    cd python-django-workshop
    ```

2.  **Installer les dépendances et créer l'environnement virtuel :**

    ```bash
    uv sync
    ```
    *Cette commande crée le dossier `.venv` et installe tout ce qui est défini dans `pyproject.toml`.*

3.  **Activer l'environnement virtuel :**

    *   Sur Windows (PowerShell) :
        ```powershell
        .venv\Scripts\activate
        ```
    *   Sur macOS/Linux :
        ```bash
        source .venv/bin/activate
        ```

4.  **Appliquer les migrations :**

    ```bash
    python manage.py migrate
    ```

5.  **Lancer le serveur de développement :**

    ```bash
    python manage.py runserver
    ```

    L'application sera accessible sur `http://127.0.0.1:8000/`.

##  Structure du Projet

*   `core/` : Configuration principale du projet Django.
*   `active_share/` : Application gérant la logique des actions, des acheteurs et des vendeurs.
*   `manage.py` : Utilitaire de ligne de commande Django.

##  Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.
