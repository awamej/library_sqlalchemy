from flask import Flask, abort, make_response, request, jsonify
from app import app, db
from app.models import Book, Author, Lend
from sqlalchemy import create_engine, MetaData

engine = create_engine('sqlite:///books_authors.db', convert_unicode=True)
metadata = MetaData(bind=engine)
con = engine.connect()


def books_list():
    return jsonify(Book.query.all())