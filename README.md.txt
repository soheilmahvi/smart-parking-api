Ich lege das gleich hier im Codeformat ab. Du kannst es direkt in deinem Projektordner unter dem Namen README.md abspeichern:

markdown

# 🚗 Smart Parking API

Ein Backend-System zur Verwaltung von Garagen, Parkplätzen und Reservierungen – ideal für digitale Parkraummanagement-Lösungen wie bei **Arivo**.

## 🔧 Features

- ✅ Benutzerregistrierung und Login mit JWT (Token-basierte Authentifizierung)
- ✅ Verwaltung von Garagen & Parkplätzen
- ✅ Parkplatz-Reservierungen: Starten und Beenden
- ✅ REST API mit Swagger-Dokumentation
- ✅ Reservierungs-Validierung: Ein Parkplatz kann nicht doppelt reserviert werden
- ✅ Logging aller Reservierungen mit Zeitstempel
- ✅ Swagger & Redoc Dokumentation
- ✅ Docker Support (inkl. Buildfile)
- ✅ Unit Tests (z. B. für Reservierungslogik)

---

## 🛠️ Tech Stack

| Bereich            | Technologie                          |
|--------------------|---------------------------------------|
| Backend            | Python, Django, Django REST Framework |
| Datenbank          | SQLite (für Dev) → PostgreSQL möglich |
| Authentifizierung  | JWT (`SimpleJWT`)                     |
| API Docs           | Swagger UI & ReDoc (`drf-yasg`)       |
| Containerization   | Docker                                |
| Testing            | Django Unit Tests                     |

---

## 🚀 Schnellstart

1. Projekt klonen:
   ```bash
   git clone https://github.com/dein-benutzer/smart-parking.git
   cd smart-parking
Virtuelle Umgebung aktivieren:

bash

python -m venv venv
venv\Scripts\activate  # Windows
Abhängigkeiten installieren:

bash

pip install -r requirements.txt
Datenbankmigrations ausführen:

bash

python manage.py migrate
Server starten:

bash

python manage.py runserver
API im Browser testen:

Swagger UI: http://localhost:8000/swagger/

ReDoc: http://localhost:8000/redoc/

🔐 Authentifizierung
User registrieren:
POST /api/register/
Payload:

json

{
  "username": "soheil",
  "password": "securepass123",
  "email": "soheil@example.com"
}
Token erhalten:
POST /api/token/

Token verwenden:
Header:

makefile

Authorization: Bearer <dein_access_token>
🧪 Tests ausführen
bash

python manage.py test parking
🐳 Docker (optional)
bash

docker build -t smart_parking_app .
docker run -p 8000:8000 smart_parking_app
📷 Screenshots
Beispiel	Beschreibung
Swagger UI Übersicht
ReDoc Übersicht
👤 Autor
Soheil Mahvi Khomami

Email: mahvisoheyl@gmail.com

