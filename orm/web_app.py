import logging

from flask import Flask, request
from pydantic import ValidationError

from orm.model import User

app = Flask(__name__)
logger = logging.getLogger(name=__name__)


@app.route("/person/new", methods=["POST"])
def new_user():
    try:
        data = request.json
        user = User(**data)
        user.save()
        return user.pk
    except ValidationError as err:
        logger.error(msg=str(err.errors()))
        return "Bad request.", 400


@app.route("/person/<pk>/delete", methods=["DELETE"])
def delete_user(pk: int):
    user = User.get(pk=pk)
    User.delete(pk=pk)
    return f"User {user.username} deleted.", 204


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
