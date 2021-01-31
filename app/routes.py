from flask import request, jsonify
from app import db
from app.models import Book, Author, Lend, BookSchema, AuthorSchema
from sqlalchemy import create_engine, MetaData

engine = create_engine('sqlite:///books_authors.db', convert_unicode=True)
metadata = MetaData(bind=engine)
con = engine.connect()


def books_list():
    b_list = []
    for b in Book.query.all():
        b_list.append(b.as_dict())
    return jsonify(b_list)


def books_insert():
    book = {'id': request.json.get('id'), 'title': request.json.get('title'),
            'description': request.json.get('description'), 'pages': request.json.get('pages')}
    existing_title = Book.query.filter(Book.title == book.get('title')).one_or_none()
    if existing_title is None:
        schema = BookSchema()
        new_book = schema.load(book, session=db.session)
        db.session.add(new_book)
        db.session.commit()
        return schema.dump(new_book), 201


def get_book(book_id):
    book = Book.query.filter_by(id=book_id).first()
    return jsonify(book.as_dict())


def authors_list():
    a_list = []
    for a in Author.query.all():
        a_list.append(a.as_dict())
    return jsonify(a_list)


def authors_insert():
    author = {'id': request.json.get('id'), 'name': request.json.get('name'), 'surname': request.json.get('surname')}
    schema = AuthorSchema()
    new_author = schema.load(author, session=db.session)
    db.session.add(new_author)
    db.session.commit()
    return schema.dump(new_author), 201


def add_author(book_id):
    authors_book = Book.query.get(book_id)
    author = Author.query.get(request.json.get('id'))
    author.books.append(authors_book)
    db.session.add(author)
    db.session.commit()
    return jsonify(authors_book.as_dict())

