# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    published_year = db.Column(db.Integer, nullable=False)

# Endpoint 1: Retrieve All Books
@app.route('/api/books', methods=['GET'])
def get_all_books():
    books = Book.query.all()
    book_list = []
    for book in books:
        book_list.append({
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'published_year': book.published_year
        })
    return jsonify(book_list)

# Endpoint 2: Add a New Book
@app.route('/api/books', methods=['POST'])
def add_new_book():
    data = request.get_json()
    if not data or 'title' not in data or 'author' not in data or 'published_year' not in data:
        return jsonify({'error': 'Invalid request'}), 400

    new_book = Book(title=data['title'], author=data['author'], published_year=data['published_year'])
    db.session.add(new_book)
    try:
        db.session.commit()
        return jsonify({'message': 'Book added successfully'}), 201
    except:
        db.session.rollback()
        return jsonify({'error': 'Error adding the book'}), 500

# Endpoint 3: Update Book Details
@app.route('/api/books/<int:id>', methods=['PUT'])
def update_book_details(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    data = request.get_json()
    if not data or 'title' not in data or 'author' not in data or 'published_year' not in data:
        return jsonify({'error': 'Invalid request'}), 400

    book.title = data['title']
    book.author = data['author']
    book.published_year = data['published_year']

    try:
        db.session.commit()
        return jsonify({'message': 'Book updated successfully'}), 200
    except:
        db.session.rollback()
        return jsonify({'error': 'Error updating the book'}), 500

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create tables
    app.run(debug=True)
