
# API_Team

API REST développée avec **FastAPI** pour exposer les données de la collection `tint_raw_data` stockée dans **MongoDB**.

## Documentation interactive

Une fois le serveur lancé, la documentation Swagger est disponible à l’adresse :

```bash
http://127.0.0.1:8000/docs
````

---

## Objectif du projet

Cette API permet de :

* consulter les parties enregistrées
* consulter les tours d’une partie
* consulter les actions et statistiques par tour
* exposer des indicateurs analytiques globaux
* suivre l’évolution des scores

### Schéma général de fonctionnement

Le client appelle une route
→ la route reçoit la demande
→ la route appelle une fonction métier
→ la fonction métier interroge la base de données
→ la fonction métier renvoie le résultat
→ la route renvoie la réponse HTTP

---

## Technologies et outils utilisés

* **Python** : langage principal du projet
* **FastAPI** : framework API
* **Uvicorn** : serveur ASGI pour exécuter FastAPI
* **MongoDB** : base de données NoSQL
* **mongod** : serveur MongoDB
* **mongosh** : client MongoDB en ligne de commande
* **MongoDB Compass** : interface graphique pour explorer la base
* **VS Code** : IDE recommandé pour le développement
* **requirements.txt** : liste des dépendances Python du projet

---

## Prérequis

Avant de lancer le projet, vérifier que les outils suivants sont installés :

* Python 3.10 ou plus récent
* Git
* MongoDB
* mongosh
* pip

---

## Cloner le dépôt Git

Dans un terminal, placer-vous dans le dossier où vous voulez récupérer le projet, puis exécuter :

```bash
git clone https://github.com/UCA-CORP/API_Team.git
cd API_Team
```


---

## Créer l’environnement virtuel Python

Depuis la racine du projet :

```bash
python -m venv .venv
```

Cela crée un environnement virtuel nommé `.venv`.

---

## Activer l’environnement virtuel

### Sur Windows - PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Sur Windows - Invite de commandes (cmd)

```cmd
.venv\Scripts\activate
```

### Sur Linux / macOS

```bash
source .venv/Scripts/activate
```

Lorsque l’environnement est activé, son nom apparaît généralement au début de la ligne de commande.

---

## Installer les dépendances

Une fois l’environnement virtuel activé :

```bash
pip install -r requirements.txt
```

---

## Lancer MongoDB

Le projet nécessite que MongoDB soit démarré.

### Si MongoDB est lancé comme service

Il suffit de vérifier qu’il tourne déjà sur la machine.

### Si vous le lancez manuellement

Dans un autre terminal, vous pouvez ensuite ouvrir le client MongoDB :

```bash
mongosh
```

Puis sélectionner la base :

```javascript
use tint_db
```

La collection utilisée dans le projet est :

```javascript
tint_raw_data
```

---

## Lancer le serveur FastAPI

Depuis la racine du projet :

```bash
uvicorn src.main:app --reload
```

### Explication

* `src.main` : fichier `main.py` dans le dossier `src`
* `app` : instance FastAPI déclarée dans ce fichier
* `--reload` : recharge automatiquement le serveur à chaque modification du code

Une fois lancé, l’API est accessible sur :

```bash
http://127.0.0.1:8000
```

La documentation Swagger est disponible sur :

```bash
http://127.0.0.1:8000/docs
```

---

## Endpoints disponibles

### Endpoints sur la collection `tint_raw_data`

```http
GET /parties
```

Lister toutes les parties.

```http
GET /parties/{id}
```

Lister les informations d’une partie à partir de son identifiant.

```http
GET /parties/{id}/tours
```

Lister les tours d’une partie.

```http
GET /parties/{id}/tours/{id}
```

Lister les informations d’un tour d’une partie à partir de son identifiant.

```http
GET /parties/{id}/tours/{tour}/actions
```

Lister les actions d’un tour.

```http
GET /parties/{id}/tours/{tour}/statistiques
```

Lister les statistiques d’un tour.

### Endpoints analytiques

```http
GET /analytics/kpis/globaux
```

Retourne les KPI globaux, par exemple :

* score maximal
* nombre total de parties
* score final moyen

```http
GET /analytics/repartition/users-level
```

Retourne la répartition des utilisateurs par niveau.

```http
GET /analytics/evolution/score-final
```

Retourne l’évolution des scores finaux des utilisateurs selon les parties jouées.

```http
GET /analytics/evolution/performance
```

Retourne l’évolution de la performance par tour.

---



---

## Notes importantes

### 1. Correspondance entre modèles et base de données

Les champs définis dans les modèles Pydantic doivent avoir exactement les mêmes noms que les champs présents dans la base de données, sinon FastAPI peut renvoyer des erreurs de validation.

### 2. Vérification de la base

Dans `mongosh`, vous pouvez vérifier que vous utilisez la bonne base :

```javascript
use tint_db
show collections
```

### 3. Vérification des données

Pour afficher quelques documents de la collection :

```javascript
db.tint_raw_data.find().limit(5)
```


## Commandes utiles

### Désactiver l’environnement virtuel

```bash
deactivate
```

### Réinstaller les dépendances après modification du projet

```bash
pip install -r requirements.txt
```

### Lancer le serveur en mode développement

```bash
uvicorn src.main:app --reload
```

---


### Activation

Windows PowerShell :

```powershell
.venv\Scripts\Activate.ps1
```

Linux / macOS :

```bash
source .venv/bin/activate
```

### Installation et lancement

```bash
pip install -r requirements.txt
uvicorn src.main:app --reload
```

Puis ouvrir :

```bash
http://127.0.0.1:8000/docs
```

---



