# 🏥 CEMA Health Information System – API

A basic Django-based health information management system for registering clients, managing health programs (e.g., TB, HIV), enrolling clients, and exposing client profiles via an API.

---

## ✅ Features

- Create and manage health programs
- Register clients with details (name, age, gender, contact)
- Enroll clients in one or more programs
- View client profiles including program history
- Expose client profiles and health programs via REST API

---

## 🔧 Built With

- Django (Backend framework)
- Django REST Framework (API layer)
- SQLite (default database)
- Python 3

---

## 🚀 How to Run the Project

```bash
# Clone the repo
git clone https://github.com/Coskleakey/cema-health-system.git
cd cema-health-system

# Set up virtual environment
python -m venv venv
venv\Scripts\activate  # Or: source venv/bin/activate (Linux/Mac)

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Start the server
python manage.py runserver
