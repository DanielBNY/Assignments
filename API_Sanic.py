from sanic import Sanic
from sanic.response import json
import jwt
import datetime
import os
import json as json_manipulation
from sanic.response import text

app = Sanic("API_Sanic")

SECRET_KEY = os.urandom(24)


def encode_new_token(user_name):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, hours=1),
        'iat': datetime.datetime.utcnow(),
        'sub': user_name
    }
    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm='HS256'
    )


def validate_user_and_password(user_name, password):
    with open(os.path.join(os.getcwd(), 'conf.json')) as json_file:
        json_data = json_manipulation.load(json_file)
        if json_data["user_name"] == user_name and \
                json_data["password"] == password:
            return True
    return False


@app.route("/login", methods=["POST"])
async def login(request):
    user_name = request.json["user_name"]
    password = request.json["password"]
    if validate_user_and_password(user_name=user_name, password=password):
        auth_token = encode_new_token(user_name=user_name)
        return json({"token": auth_token})
    return text("401 Unauthorized", status=401)


if __name__ == '__main__':
    app.run()
