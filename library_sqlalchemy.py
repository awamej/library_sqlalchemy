from app import app, db
# from app.models import Book, Author, Lend
from app import routes
from sqlalchemy import create_engine, MetaData


# @app.shell_context_processor
# def make_shell_context():
#     return {
#        "db": db,
#        "Book": Book,
#        "Author": Author,
#        "Lend": Lend
#    }


engine = create_engine('sqlite:///books_authors.db', convert_unicode=True)
metadata = MetaData(bind=engine)
con = engine.connect()

app.add_url_rule('/', view_func=routes.books_list, methods=["GET"])


if __name__ == "__main__":
    app.run(debug=True)