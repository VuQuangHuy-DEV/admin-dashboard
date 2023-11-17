import uuid
import json

from constants.cities import cities
from constants.vehicles import vehicles
from constants.car_brand import brands


def load_brands():
    for brand in brands:
        brand["id"] = str(uuid.uuid4())
        for model in brand["models"]:
            model["id"] = str(uuid.uuid4())

    file_path = "constants/data/brands.json"
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(brands, json_file, indent=2, ensure_ascii=False)


def load_vehicles():
    for x in vehicles:
        x["id"] = str(uuid.uuid4())

    file_path = "constants/data/vehicles.json"
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(vehicles, json_file, indent=2, ensure_ascii=False)



def load_cities():
    for x in cities:
        x["id"] = str(uuid.uuid4())

    file_path = "constants/data/location.json"
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(cities, json_file, indent=2, ensure_ascii=False)


load_brands()
load_vehicles()
load_cities()