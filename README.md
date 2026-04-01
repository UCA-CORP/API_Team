# API_Team

# URL pour acceder au swager ou API 

# http://127.0.0.1:8000/docs

Le client appelle une route
→ la route reçoit la demande
→ la route appelle une fonction métier
→ la fonction métier parle à la base
→ la fonction renvoie le résultat
→ la route renvoie la réponse HTTP

les endpoints pour la collection tint_raw_data
GET /parties    # Lister toutes les parties
GET /parties/{id}  # Lister les informations d'une partie à partir de son id
GET /parties/{id}/tours  # Lister les tours d'une partie
GET /parties/{id}/tours/{id}   # Lister les informations d'un tour d'une partie à partir de leur id
GET /parties/{id}/tours/{tour}/actions  # Lister les actions d'un tour
GET /parties/{id}/tours/{tour}/statistiques   # Lister les statistiques d'un tour

pour lancer le serveur
uvicorn src.main:app --reload

outils et technologie: 
mongo compass : pour la gestion de la base de données
vscode : IDE pour le developpement des endpoints
python : le langage de programmation utilisé
requirements.txt : ensembles des parckages installé dans le projet




Notes importantes :

# Les champs dans les models doivent être les mêmes que dans la base de données


