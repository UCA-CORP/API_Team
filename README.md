# API_Team

Le client appelle une route
→ la route reçoit la demande
→ la route appelle une fonction métier
→ la fonction métier parle à la base
→ la fonction renvoie le résultat
→ la route renvoie la réponse HTTP

les endpoints pour la collection tint_raw_data
GET /partie
GET /partie/{id}
GET /partie/{id}/tours
GET /partie/{id}/tours/{tour}/actions

pour tester
uvicorn src.main:app --reload