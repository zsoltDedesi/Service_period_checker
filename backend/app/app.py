# import psycopg2

from flask import Flask
from flask_cors import CORS

from config import EnvData
from routes.car_parts import car_parts, db_handler


def create_app() -> Flask:
    """Application factory for the backend service."""
    app = Flask(__name__)
    app.register_blueprint(car_parts, url_prefix="/api/data")

    CORS(app=app)

    app.config["SQLALCHEMY_DATABASE_URI"] = EnvData.DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db_handler.init_db()
    return app


def main() -> None:
    """Run the development server."""
    app = create_app()
    app.run(debug=True, port=5000)


if __name__ == "__main__":
    main()
