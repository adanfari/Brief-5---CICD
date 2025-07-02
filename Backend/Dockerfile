FROM python:3.11-slim

WORKDIR /app

# Dépendances
RUN pip install --no-cache-dir fastapi 'uvicorn[standard]' pydantic loguru

# Copie du code
COPY backend/ ./backend/

# Port exposé
EXPOSE 8000

# Lancement de l'API
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]