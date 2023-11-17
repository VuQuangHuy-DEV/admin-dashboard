from  constants import car_brand
import uuid
import  json

brands = car_brand.brands

for brand in brands:
    brand["id"] = str(uuid.uuid4())
    for model in brand["models"]:
        model["id"] = str(uuid.uuid4())

file_path = "brands.json"
with open(file_path,"w", encoding="utf-8") as json_file:
    json.dump(brands, json_file, indent=2, ensure_ascii=False)