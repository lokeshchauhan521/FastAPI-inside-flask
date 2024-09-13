from flask import Flask, jsonify, Response
# from asgi_to_wsgi import fastapi_wsgi
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware

app = Flask(__name__)

items = [
    {"id": 1, "name": "Item 1", "price": 100},
    {"id": 2, "name": "Item 2", "price": 200},
    {"id": 3, "name": "Item 3", "price": 300},
]

@app.route("/")
def first():
    return "<p>Welcome to Flask</p>"

@app.route("/items", methods=['GET'])
def get_items():
    return jsonify(items)

fastapi_app = FastAPI()

@fastapi_app.get("/data")
async def get_fastapi_items():
    return items

fastapi_app.mount("/flask", WSGIMiddleware(app))
