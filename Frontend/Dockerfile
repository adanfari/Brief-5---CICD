FROM python:3.11-slim

WORKDIR /app

# Dépendances
RUN pip install --no-cache-dir streamlit requests loguru

# Copie du code
COPY frontend/ ./frontend/

EXPOSE 8501

CMD ['streamlit', 'run', 'frontend/app.py', '--server.port', '8501', '--server.address', '0.0.0.0']