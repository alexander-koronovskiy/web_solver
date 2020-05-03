from index import app
from flask import request, current_app

with app.test_request_context('/products'):
    # получим полный путь к запрашиваемой странице(без домена).
    print(request.path, request.method, current_app.name)
