from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import psycopg2

from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)
CORS(app=app)

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{os.getenv('DB_USERNAME')}:\
                                                       {os.getenv('DB_PASSWORD')}@\
                                                       {os.getenv('DB_HOST')}:\
                                                       {os.getenv('DB_PORT')}/\
                                                       {os.getenv('DB_NAME')}"

db = SQLAlchemy(app)


class CarPart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_name = db.Column(db.String(100))
    part_name = db.Column(db.String(100))
    interval = db.Column(db.String(50))
    last_replacement = db.Column(db.Date)
    notes = db.Column(db.Text)


@app.route("/api/data/car-parts", methods=["GET"])
def get_car_parts():
    parts = CarPart.query.all()
    return jsonify(
        [
            {
                "id": part.id,
                "car_name": part.car_name,
                "part_name": part.part_name,
                "interval": part.interval,
                "last_replacement": part.last_replacement,
                "notes": part.notes,
            }
            for part in parts
        ]
    )


@app.route("/api/data/car-parts", methods=["POST"])
def add_car_part():
    try:
        # 1. JSON adatok fogadása
        data = request.get_json()

        # 2. Adatellenőrzés
        required_fields = ["car_name", "part_name", "interval", "last_replacement"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        # 3. Új objektum létrehozása
        new_part = CarPart(
            car_name=data["car_name"],
            part_name=data["part_name"],
            interval=data["interval"],
            last_replacement=data["last_replacement"],
            notes=data.get("notes", ""),  # Nem kötelező mező
        )

        # 4. Mentés az adatbázisba
        db.session.add(new_part)
        db.session.commit()

        # 5. Visszatérés az új objektum adataival
        return jsonify(
            {
                "message": "Car part added successfully",
                "part": {
                    "id": new_part.id,
                    "car_name": new_part.car_name,
                    "part_name": new_part.part_name,
                    "interval": new_part.interval,
                    "last_replacement": new_part.last_replacement,
                    "notes": new_part.notes,
                },
            }
        ), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def main():
    # passflasf
    app.run(debug=True, port=5000)
    # print(app.config["SQLALCHEMY_DATABASE_URI"])

    # print("DB_USERNAME:", os.getenv("DB_USERNAME"))
    # print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))
    # print("DB_HOST:", os.getenv("DB_HOST"))
    # print("DB_PORT:", os.getenv("DB_PORT"))
    # print("DB_NAME:", os.getenv("DB_NAME"))


if __name__ == "__main__":
    main()
