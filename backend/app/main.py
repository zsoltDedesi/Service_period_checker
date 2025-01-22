from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import psycopg2

from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{os.getenv("DB_USERNAME")}:\
                                                       {os.getenv("DB_PASSWORD")}@\
                                                       {os.getenv("DB_HOST")}:\
                                                       {os.getenv("DB_PORT")}/\
                                                       {os.getenv("DB_NAME")}'

db = SQLAlchemy(app)


class CarPart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_name = db.Column(db.String(100))
    part_name = db.Column(db.String(100))
    interval = db.Column(db.String(50))
    last_replacement = db.Column(db.Date)
    notes = db.Column(db.Text)

@app.route('/car-parts', methods=['GET'])
def get_car_parts():
    parts = CarPart.query.all()
    return jsonify([{
        'id': part.id,
        'car_name': part.car_name,
        'part_name': part.part_name,
        'interval': part.interval,
        'last_replacement': part.last_replacement,
        'notes': part.notes
    } for part in parts])


def main():
    # passflasf
    app.run(debug=True, port=5000)
    print(app.config['SQLALCHEMY_DATABASE_URI'])

    # print("DB_USERNAME:", os.getenv("DB_USERNAME"))
    # print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))
    # print("DB_HOST:", os.getenv("DB_HOST"))
    # print("DB_PORT:", os.getenv("DB_PORT"))
    # print("DB_NAME:", os.getenv("DB_NAME"))






if __name__ == '__main__':
    main()
