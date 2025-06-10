1. Clone the project and navigate to backend folder.

2. Create virtual environment.

3. Install dependencies(pip install -r requirements.txt)

4. Configure database(Works with SQLite)

5. Run migrations(python manage.py makemigrations,
python manage.py migrate)

6. Start development server(python manage.py runserver)

7. API Endpoints -:

GET /api/doctors/ - List all doctors
GET /api/appointments/ - List all appointments (filterable by doctor and date)
POST /api/appointments/ - Create a new appointment




