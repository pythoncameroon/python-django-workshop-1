# Guide de Contribution - ActiveShare Platform

Bienvenue ! Nous sommes ravis que vous souhaitiez contribuer à ce projet. 🎉

## 🎯 Objectif du Projet

Ce projet a pour but de vous permettre d'apprendre Django tout en pratiquant le **vibecoding** avec l'éditeur **Antigravity**. 

> **⚠️ IMPORTANT** : Le vibecoding ne signifie pas coder sans réfléchir ! L'objectif est de **comprendre ce que vous faites** tout en utilisant les capacités de l'IA pour accélérer votre développement.

## 📋 Fonctionnalités à Implémenter

### 1. Modèles Django (Priorité Haute)

Implémentez les modèles suivants avec leurs relations :

#### Modèles à créer :
- **Shareholder** (Actionnaire)
- **Buyer** (Acheteur)
- **Share** (Action)

#### Règles d'intégrité :
- Chaque `Shareholder` et `Buyer` doit être lié à un utilisateur Django (`User`)
- Un `Shareholder` peut créer **une ou plusieurs** `Share`
- Un `Buyer` peut acheter **aucune ou plusieurs** `Share`
- Une `Share` est créée par **un et un seul** `Shareholder`
- Une `Share` peut être achetée par **un ou plusieurs** `Buyer`

#### Contraintes techniques :
- Utilisez les relations Django appropriées (`ForeignKey`, `ManyToManyField`, etc.)
- Implémentez les méthodes `__str__()` pour une meilleure lisibilité
- Ajoutez des `Meta` classes avec `verbose_name` et `ordering`
- Pensez aux `related_name` pour faciliter les requêtes inverses

### 2. Interface Web (Priorité Haute)

Créez une interface utilisateur **moderne et attrayante** en HTML, CSS et JavaScript.

#### Pages à créer :
- 🏠 **Page d'accueil** : Présentation de la plateforme
- 📝 **Page d'inscription** : Création de compte (avec choix du rôle : Shareholder/Buyer)
- 🔐 **Page de connexion** : Authentification
- 👤 **Page de profil utilisateur** : Détails selon le type d'utilisateur (Shareholder/Buyer)
- ➕ **Page de création de Share** : Formulaire pour les Shareholders
- 📊 **Page de détails d'une Share** : Informations complètes sur une action
- 🛒 **Page de liste des Shares** : Catalogue des actions disponibles
- 📈 **Tableau de bord** : Vue d'ensemble des actions possédées/créées

#### Exigences de design :
- ✨ Interface **moderne et professionnelle**
- 📱 Design **responsive** (mobile, tablette, desktop)
- 🎨 Palette de couleurs cohérente
- ♿ Accessibilité de base (labels, contraste, navigation au clavier)
- 🚀 Animations subtiles et transitions fluides

> **Note** : Dans un premier temps, vous pouvez créer des maquettes statiques (mockups) avant l'intégration avec Django.

### 3. Vues Django et Intégration (Priorité Haute)

Implémentez les vues Django et intégrez-les aux templates.

#### Exigences :
- Utilisez les **Django Forms** pour la validation des données
- Implémentez les vues basées sur les classes (CBV) ou fonctions (FBV) selon le contexte
- Gérez les permissions (seuls les Shareholders peuvent créer des Shares)
- Ajoutez des messages de feedback utilisateur (succès, erreurs)
- Implémentez la pagination pour les listes
- Gérez les cas d'erreur (404, 403, etc.)

## 🏗️ Architecture et Bonnes Pratiques

### Structure du Code
- Suivez la structure Django standard
- Séparez la logique métier des vues (utilisez des services si nécessaire)
- Gardez vos vues simples et lisibles
- Utilisez des serializers ou forms pour la validation

### Qualité du Code
- ✅ Respectez la PEP 8 (style Python)
- 📝 Commentez le code complexe
- 🧪 Écrivez des tests unitaires (bonus)
- 🔒 Validez toujours les données côté serveur
- 🚫 N'exposez jamais de données sensibles

### Git et Commits
- 📌 Commits atomiques et descriptifs
- 💬 Messages de commit clairs en français ou anglais
  - Format recommandé : `type: description courte`
  - Exemples : 
    - `feat: ajout du modèle Shareholder`
    - `fix: correction de la validation du formulaire Share`
    - `style: amélioration du design de la page d'accueil`

## 🔄 Processus de Contribution

### 1. Préparation

```bash
# Forkez le projet sur GitHub, puis clonez votre fork
git clone <votre-fork-url>
cd python-django-workshop

# Ajoutez le repo original comme remote
git remote add upstream <repo-original-url>

# Créez une branche pour votre fonctionnalité
git checkout -b feat/nom-de-la-fonctionnalite
```

### 2. Développement

- ⚠️ **Avant de commencer** : Synchronisez avec la branche principale
  ```bash
  git fetch upstream
  git rebase upstream/main
  ```
- 💻 Développez votre fonctionnalité
- 🧪 Testez localement
- 📝 Committez régulièrement

### 3. Pull Request (PR)

#### Règles importantes :
- ✅ **Une PR = Une fonctionnalité**
- ❌ **Pas de PR longues** (évitez les PR de 500+ lignes)
- 🔄 **Synchronisez avant chaque PR**
  ```bash
  git fetch upstream
  git rebase upstream/main
  git push origin feat/nom-de-la-fonctionnalite
  ```

#### Template de PR :

```markdown
## Description
Brève description de ce que fait cette PR.

## Type de changement
- [ ] Nouveau modèle
- [ ] Nouvelle vue
- [ ] Nouveau template
- [ ] Correction de bug
- [ ] Amélioration de design

## Checklist
- [ ] Mon code respecte les conventions du projet
- [ ] J'ai testé localement
- [ ] J'ai synchronisé avec la branche principale
- [ ] Mes commits sont clairs et atomiques
- [ ] J'ai mis à jour la documentation si nécessaire

## Captures d'écran (si applicable)
Ajoutez des captures d'écran pour les changements visuels.
```

### 4. Review

- Les mainteneurs (@yokwejuste et @Edmond22-prog) revieweront votre PR
- Soyez réactif aux commentaires
- Effectuez les modifications demandées
- Une fois approuvée, votre PR sera mergée ! 🎉

## ❓ Questions et Support

Si vous avez des questions ou rencontrez des difficultés :

1. 🔍 Consultez d'abord la documentation Django
2. 💬 Créez une **Issue** sur GitHub avec :
   - Un titre clair
   - Une description détaillée du problème
   - Les étapes pour reproduire (si bug)
   - Votre environnement (OS, version Python, etc.)
3. 🏷️ Taguez **@yokwejuste** et **@Edmond22-prog**

## 💡 Nouvelles Idées

Vous avez une idée de fonctionnalité supplémentaire ? Super !

1. Créez une **Issue** avec le label `enhancement`
2. Décrivez votre proposition
3. Attendez les retours avant de commencer l'implémentation

## 📚 Ressources Utiles

- [Documentation Django](https://docs.djangoproject.com/)
- [Django Girls Tutorial](https://tutorial.djangogirls.org/)
- [MDN Web Docs - HTML/CSS/JS](https://developer.mozilla.org/)
- [PEP 8 - Style Guide](https://pep8.org/)

## 🙏 Remerciements

Merci de contribuer à ce projet et de faire partie de la communauté Python Cameroon ! 🇨🇲

---

**Happy Coding! 🚀**
