# FastAI MLOps Template – Calcul du carré

Ce dépôt illustre une architecture MLOps minimale :
- **Backend** : API FastAPI (`/`, `/health`, `/calcul`)
- **Frontend** : Streamlit
- **CI/CD** : GitHub Actions
- **Conteneurs** : Docker & Compose

## Lancement local

```bash
docker-compose up --build