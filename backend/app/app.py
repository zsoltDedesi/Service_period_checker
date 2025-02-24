# import psycopg2

from flask import Flask
from flask_cors import CORS

from config import EnvData
from routes.car_parts import car_parts


def main():
    flask_app = Flask(__name__)
    flask_app.register_blueprint(car_parts, url_prefix="/api/data")

    CORS(app=flask_app)

    flask_app.config["SQLALCHEMY_DATABASE_URI"] = EnvData.DATABASE_URL
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


    flask_app.run(debug=True, port=5000)


if __name__ == "__main__":
    main()
