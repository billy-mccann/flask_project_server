"""
This is the base entry point for the flask app that
will be used in a docker container to assist in app
development
"""

from random import randrange
from dataclasses import asdict

from flask import Flask, request, jsonify

from authhelper import MissingTokenError, DecodingError, InvalidTokenError
from user import create_random_user, create_random_rental, create_random_cell

import authhelper as ah

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/house")
def house():
    return {"username": "Big House", "location": "Paradise, Earth", "price": 499}


@app.route("/post/<int:post_id>")
def show_post(post_id):
    posts = []
    for i in range(post_id):
        posts.append({"id": i + 1, "post": "post " + str(i * 13)})
    return posts


@app.route("/users")
def users():
    num = randrange(100)
    user_list = []
    for _ in range(num):
        user_list.append(asdict(create_random_user()))
    return user_list


@app.route("/cells")
def cells():
    num = randrange(100)
    cell_list = []
    for i in range(num):
        cell_list.append(asdict(create_random_cell(i)))
    return cell_list


@app.route("/rentals")
def rentals():
    try:
        ah.validate_request(request)
        # Return requested data
        rental_properties = []
        for _ in range(10):
            rental_properties.append(asdict(create_random_rental()))
        return rental_properties
    except MissingTokenError as e:
        print(e)
        return (
            jsonify(
                {
                    "message": "Missing token error: no token was found in request headers"
                }
            ),
            401,
        )
    except DecodingError as e:
        print(e)
        return (
            jsonify(
                {"message": "Decoding error: An error occurred during token decoding"}
            ),
            401,
        )
    except InvalidTokenError as e:
        print(e)
        return jsonify({"message": "Invalid token error: token expired"}), 401
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(e)
        return jsonify({"message": "Invalid token"}), 401


@app.route("/login", methods=["GET"])
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    # Valid Credentials
    if ah.is_authorized_user(username, password):
        token = ah.create_auth_token(username)
        return jsonify({"token": token})

    # Credentials are invalid
    return jsonify({"message": "Invalid username or password"}), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
