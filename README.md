Clone the project and navigate to backend folder.
Create virtual environment.
Install dependencies(pip install -r requirements.txt)
Configure database(Works with SQLite)
Run migrations(python manage.py makemigrations,
python manage.py migrate)
Start development server(python manage.py runserver)
API Endpoints -:
GET /api/doctors/ - List all doctors
GET /api/appointments/ - List all appointments (filterable by doctor and date)
POST /api/appointments/ - Create a new appointment




