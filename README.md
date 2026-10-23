# Doctobot

API FastAPI (Python 3.12) avec SQLite, gérée avec Poetry.

## Commandes

| Commande       | Description                                              |
|----------------|----------------------------------------------------------|
| `make setup`   | Crée le venv `.venv` (Python 3.12) et installe les deps  |
| `make run`     | Lance l'API en local sur http://127.0.0.1:8000           |
| `make quality` | Formatage + lint (ruff) et vérification de types (mypy)  |
| `make test`    | Lance les tests pytest                                   |

Documentation Swagger : http://127.0.0.1:8000/docs (OpenAPI : `/openapi.json`).

La base SQLite est configurable via la variable `DATABASE_URL` (défaut : `sqlite:///./doctobot.db`).
Les tables sont créées au démarrage de l'application.

## Endpoints

| Méthode | Route                    | Description                                   |
|---------|--------------------------|-----------------------------------------------|
| POST    | `/doctors`               | Enregistrer un médecin robot (201)            |
| GET     | `/doctors`               | Lister les médecins                           |
| GET     | `/doctors/{doctor_id}`   | Consulter un médecin (404 si inconnu)         |
| POST    | `/patients`              | Enregistrer un patient (201, 409 si email pris) |
| GET     | `/patients`              | Lister les patients                           |
| GET     | `/patients/{patient_id}` | Consulter un patient (404 si inconnu)         |

## Structure

```
app/
  main.py          # application FastAPI + inclusion des routers
  config.py        # réglages (DATABASE_URL, ...)
  api/             # routers HTTP (un par ressource) + dépendances
  domain/          # modèles pydantic (validation métier)
  repositories/    # accès aux données
  db/              # moteur SQLAlchemy et tables
tests/
  api/             # tests des endpoints via TestClient
  domain/          # tests de validation des modèles
  repositories/    # tests de la couche d'accès aux données
```
