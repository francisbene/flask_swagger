from flask import jsonify, request
from flask_restful import Resource
from flasgger import swag_from
from models.book import books

class Book(Resource):
    @swag_from('../swagger/get_book.yml')
    def get(self, book_id):
        return jsonify({book_id: books.get(book_id)})

    @swag_from('../swagger/update_book.yml')
    def put(self, book_id):
        books[book_id] = request.json
        return jsonify({book_id: books[book_id]})

    @swag_from('../swagger/delete_book.yml')
    def delete(self, book_id):
        del books[book_id]
        return '', 204


class BookList(Resource):
    @swag_from('../swagger/get_books.yml')
    def get(self):
        return jsonify(books)

    @swag_from('../swagger/create_book.yml')
    def post(self):
        book_id = len(books) + 1
        books[book_id] = request.json
        return jsonify({book_id: books[book_id]}), 201