from datetime import datetime
from app import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field


helper_table = db.Table('help',
                        db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
                        db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True)
                        )


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), index=True, unique=True)
    description = db.Column(db.String(200), index=True)
    pages = db.Column(db.Integer)
    authors = db.relationship('Author', secondary=helper_table,
                              backref=db.backref('books', lazy='dynamic'), lazy='dynamic')
    if_lend = db.relationship('Lend', backref='book', lazy='dynamic')

    def __str__(self):
        return f"<Book {self.title}>"

    def __repr__(self):
        return str(self)

    def as_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "pages": self.pages,
            "authors": [a.surname for a in self.authors],
            "if_lend": [l.lend_date for l in self.if_lend]
        }


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50), index=True)

    def __str__(self):
        return f"<Author {self.name} {self.surname}>"

    def __repr__(self):
        return str(self)

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "books": [b.title for b in self.books]
        }


class Lend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lend_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __str__(self):
        return f"<Date and time of lend: {self.lend_date}>"

    def __repr__(self):
        return str(self)


class BookSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        include_relationships = True
        load_instance = True


class AuthorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Author
        include_relationships = True
        load_instance = True
