# Utilise une image Python
FROM python:3.9

# Définit le répertoire de travail de l'image
WORKDIR /app

# Copie les fichiers requis dans le conteneur
COPY . .

RUN pip3 install -r requirements.txt

# Expose le port 8080
EXPOSE 5000

# Commande pour démarrer le serveur Python
CMD ["python", "app.py"]
