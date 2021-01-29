from datetime import datetime

from app import db


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
    if_lend = db.relationship('Lend', backref='books', lazy='dynamic')

    def __str__(self):
        return f"<Book {self.title}>"

    def __repr__(self):
        return f"<Book {self.title}>"


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50), index=True)

    def __str__(self):
        return f"<Author {self.name} {self.surname}>"

    def __repr__(self):
        return f"<Author {self.name} {self.surname}>"


class Lend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lend_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __str__(self):
        return f"<Date and time of lend: {self.lend_date}>"

    def __repr__(self):
        return f"<Date and time of lend: {self.lend_date}>"
