# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# # from flask_cors import CORS

# import psycopg2

# from dotenv import load_dotenv
# import os


# # class FlaskApp:
# #     def __init__(self):
# #         self.app = Flask(__name__)
# #         self.configure_app()
# #         self.enable_cors()

# #     def configure_app(self):
# #         load_dotenv()
# #         self.app.config["SQLALCHEMY_DATABASE_URI"] = (
# #             f"postgresql://{os.getenv('DB_USERNAME')}:\
# #                            {os.getenv('DB_PASSWORD')}@\
# #                            {os.getenv('DB_HOST')}:\
# #                            {os.getenv('DB_PORT')}/\
# #                            {os.getenv('DB_NAME')}"
# #         )

# #     def register_routes(self):
# #         pass

# #     def enable_cors(self):
# #         CORS(app=self.app)

# #     def run(self, host='localhost', port=5000, debug=True):
# #         self.app.run(debug=debug, port=port)


# # db = SQLAlchemy(app)


# # class CarPart(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     car_name = db.Column(db.String(100))
# #     part_name = db.Column(db.String(100))
# #     interval = db.Column(db.String(50))
# #     last_replacement = db.Column(db.Date)
# #     notes = db.Column(db.Text)


# # @app.route("api/data/car-parts", methods=["GET"])
# # def get_car_parts():
# #     parts = CarPart.query.all()
# #     return jsonify(
# #         [
# #             {
# #                 "id": part.id,
# #                 "car_name": part.car_name,
# #                 "part_name": part.part_name,
# #                 "interval": part.interval,
# #                 "last_replacement": part.last_replacement,
# #                 "notes": part.notes,
# #             }
# #             for part in parts
# #         ]
# #     )


# # def main():
# #     # passflasf
# #     app.run(debug=True, port=5000)
# #     # print(app.config["SQLALCHEMY_DATABASE_URI"])

# #     # print("DB_USERNAME:", os.getenv("DB_USERNAME"))
# #     # print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))
# #     # print("DB_HOST:", os.getenv("DB_HOST"))
# #     # print("DB_PORT:", os.getenv("DB_PORT"))
# #     # print("DB_NAME:", os.getenv("DB_NAME"))


# # if __name__ == "__main__":
# #     main()

# # app/__init__.py

# db = SQLAlchemy()


# def create_app():
#     app = Flask(__name__)

#     # app.config.from_object("config")

#     app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{os.getenv('DB_USERNAME')}:\
#                                                            {os.getenv('DB_PASSWORD')}@\
#                                                            {os.getenv('DB_HOST')}:\
#                                                            {os.getenv('DB_PORT')}/\
#                                                            {os.getenv('DB_NAME')}"

#     # db.init_app(app)

#     from .routes.auth import auth_bp
#     from .routes.api import api_bp

#     app.register_blueprint(auth_bp, url_prefix="/auth")
#     app.register_blueprint(api_bp, url_prefix="/api")

#     return app
