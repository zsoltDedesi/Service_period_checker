from flask import Blueprint, request, jsonify

from models.database_handler import DataBaseHandler
from models.models import CarPart
from config import EnvData


db_handler = DataBaseHandler(EnvData.DATABASE_URL)
db_handler.init_db()

car_parts = Blueprint('car_parts', __name__)


@car_parts.route("/car-parts", methods=["GET"])
def get_all_car_parts():
    with db_handler.session() as session:
        car_parts = session.query(CarPart).all()  # 🔹 Minden rekord lekérése

        # 🔹 JSON formátumra alakítás
        result = [
            {
                "id": part.id,
                "car_name": part.car_name,
                "part_name": part.part_name,
                "interval": part.interval,
                "last_replacement": str(part.last_replacement),
                "notes": part.notes,
            }
            for part in car_parts
        ]

        return jsonify(result)


@car_parts.route("/car-parts", methods=["POST"])
def add_car_part():
    try:
        # 1. JSON adatok fogadása
        data = request.get_json()
        print(f"POST DATA: {data}")

        # 2. Adatellenőrzés
        required_fields = ["car_name", "part_name", "interval", "last_replacement"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        with db_handler.session() as session:
            # 3. Új objektum létrehozása
            new_part = CarPart(
                car_name=data["car_name"],
                part_name=data["part_name"],
                interval=data["interval"],
                last_replacement=data["last_replacement"],
                notes=data.get("notes", ""),  # Nem kötelező mező
            )
            session.add(new_part)
            session.commit()

            # 5. Visszatérés az új objektum adataival
            return jsonify(
                {
                    "message": "Car part added successfully",
                    "part": {
                        "id": new_part.id,
                        "car_name": new_part.car_name,
                        "part_name": new_part.part_name,
                        "interval": new_part.interval,
                        "last_replacement": str(new_part.last_replacement),
                        "notes": new_part.notes,
                    },
                }
            ), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@car_parts.route("/car-parts/<int:id>", methods=["PATCH"])
def update_car_part(id):
    print(f"Updating car part with ID: {id}")
    with db_handler.session() as session:
        car_parts = session.get(CarPart, id)
        print(car_parts)
    return jsonify({"message": "No Content"}, 204)


@car_parts.route("/car-parts/<int:id>", methods=["DELETE"])
def delete_car_part(id):
    print(f"Delete car part with ID: {id}")
    with db_handler.session() as session:
        part = session.get(CarPart, id)
        if part is None:
            return jsonify({"error": "Car part not found"}), 404
        
        session.delete(part)
        session.commit()

    return jsonify({"message": "Car part deleted successfully"}), 200