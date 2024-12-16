from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

cars_file = "cars.json"

def load_cars():
    if os.path.exists(cars_file):
        with open(cars_file, "r") as f:
            return json.load(f)
    return []

def save_cars(cars):
    with open(cars_file, "w") as f:
        json.dump(cars, f, indent=4)

cars = load_cars()

@app.route("/cars", methods=["GET"])
def get_cars():
    return jsonify(load_cars())

@app.route("/cars/<int:id>", methods=["GET"])
def get_car(id):
    car = next((car for car in cars if car["id"] == id), None)
    if car is None:
        return jsonify({"Error": "Car not found"}), 404
    return jsonify(car)

@app.route("/cars", methods=["POST"])
def add_car():
    data = request.json
    if not all(k in data for k in ("make", "model", "year", "price")):
        return jsonify({"Error": "Missing required fields"}), 400

    new_id = max((car["id"] for car in cars), default=0) + 1
    new_car = {
        "id": new_id,
        "make": data["make"],
        "model": data["model"],
        "year": data["year"],
        "price": data["price"]
    }
    cars.append(new_car)
    save_cars(cars)
    return jsonify(new_car), 201

@app.route("/cars/<int:id>", methods=["PUT"])
def update_car(id):
    data = request.json
    car = next((car for car in cars if car["id"] == id), None)
    if car is None:
        return jsonify({"Error": "Car not found"}), 404

    car.update({
        "make": data.get("make", car["make"]),
        "model": data.get("model", car["model"]),
        "year": data.get("year", car["year"]),
        "price": data.get("price", car["price"])
    })
    save_cars(cars)
    return jsonify(car)

@app.route("/cars/<int:id>", methods=["DELETE"])
def delete_car(id):
    global cars
    car = next((car for car in cars if car["id"] == id), None)
    if car is None:
        return jsonify({"Error": "Car not found"}), 404

    cars = [c for c in cars if c["id"] != id]
    save_cars(cars)
    return jsonify({"message": "Car deleted"})

if __name__ == "__main__":
    app.run(debug=True)
