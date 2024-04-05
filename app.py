# from flask import Flask, request, jsonify
# from flask_restful import Resource, Api
# from flasgger import Swagger, swag_from

# app = Flask(__name__)
# api = Api(app)

# swagger = Swagger(app)

# # Exemplo de dados em memória (substitua por um banco de dados em um ambiente de produção)
# books = {}


# class Book(Resource):
#     @swag_from('swagger/get_book.yml')
#     def get(self, book_id):
#         return jsonify({book_id: books.get(book_id)})

#     @swag_from('swagger/update_book.yml')
#     def put(self, book_id):
#         books[book_id] = request.json
#         return jsonify({book_id: books[book_id]})

#     @swag_from('swagger/delete_book.yml')
#     def delete(self, book_id):
#         del books[book_id]
#         return '', 204


# class BookList(Resource):
#     @swag_from('swagger/get_books.yml')
#     def get(self):
#         return jsonify(books)

#     @swag_from('swagger/create_book.yml')
#     def post(self):
#         book_id = len(books) + 1
#         books[book_id] = request.json
#         return jsonify({book_id: books[book_id]}), 201


# api.add_resource(BookList, '/books')
# api.add_resource(Book, '/books/<int:book_id>')

# if __name__ == '__main__':
#     app.run(debug=True)
