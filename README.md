# BookVibe 📚

BookVibe is a web-based book tracking application built with Django. It allows users to browse books by genre, search for specific titles, and manage their personal reading journey (To Read, Reading, Read).

## Features

- User authentication (Sign Up / Login)
- Book categorization by genres
- Search bar to find books
- Track books as "To Read", "Reading", or "Read"
- Clean and user-friendly interface

## Tech Stack

- Python
- Django
- HTML & CSS
- SQLite (default Django DB)

## Setup Instructions

1. Clone the repository  
   
2. Navigate into the project  
   `cd bookvibe-django`

3. Create virtual environment & activate  


python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows



4. Install dependencies  
`pip install -r requirements.txt`

5. Run migrations  
`python manage.py migrate`

6. Start the server  
`python manage.py runserver`

7. Open in browser  
`http://127.0.0.1:8000/`

