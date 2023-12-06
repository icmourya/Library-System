# Library-System
Running the Application:
1. Install Flask: pip install Flask  
2. Run the application: python app.py
3. Access the API:
Retrieve All Books: GET /api/books
Add a New Book: POST /api/books (JSON payload required)
Update Book Details: PUT /api/books/{id} (JSON payload required)

Seeding the Database:
To seed the database with mock data, you can create a separate script (e.g., seed.py):

# seed.py
from app import db, Book

# Create some sample books
sample_books = [
    {'title': 'Book 1', 'author': 'Author 1', 'published_year': 2020},
    {'title': 'Book 2', 'author': 'Author 2', 'published_year': 2021},
    {'title': 'Book 3', 'author': 'Author 3', 'published_year': 2022},
]

# Add books to the database
for book_data in sample_books:
    book = Book(**book_data)
    db.session.add(book)

# Commit the changes
db.session.commit()

print('Database seeded successfully!')
Run the seeding script:
python seed.py
