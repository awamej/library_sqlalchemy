from app import app, routes
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
app.add_url_rule('/', view_func=routes.books_insert, methods=["POST"])
app.add_url_rule('/<int:book_id>', view_func=routes.get_book, methods=["GET"])
app.add_url_rule('/authors', view_func=routes.authors_list, methods=["GET"])
app.add_url_rule('/authors', view_func=routes.authors_insert, methods=["POST"])
app.add_url_rule('/<int:book_id>/add_author', view_func=routes.add_author, methods=["POST"])


if __name__ == "__main__":
    app.run(debug=True)
