from flask import Flask
from flask_restful import Api
from controllers.book import Book, BookList
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

api.add_resource(BookList, '/books')
api.add_resource(Book, '/books/<int:book_id>')

if __name__ == '__main__':
    app.run(debug=True)