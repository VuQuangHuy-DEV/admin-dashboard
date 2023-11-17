import uuid
import mysql.connector

from constants.cities import cities
from constants.vehicles import vehicles
from constants.car_brand import brands

# db_config = {
#     'host': '103.245.249.96',
#     'user': 'bixso',
#     'password': 'Bixso@1234',
#     'database': 'bixso_xeoi_uat',
#     'port': 3306,
# }

db_config = {
    'host': '103.245.249.96',
    'user': 'bixso',
    'password': 'Bixso@1234',
    'database': 'bixso_xeoi_dev',
    'port': 3307,
}


def init_vehicles():
    try:
        with mysql.connector.connect(**db_config) as connection:
            cursor = connection.cursor()

            for vehicle in vehicles:
                check_query = "SELECT COUNT(*) FROM general_vehicle WHERE name = %s"
                check_value = (vehicle["name"],)
                cursor.execute(check_query, check_value)
                count = cursor.fetchone()[0]

                if count == 0:
                    query = "INSERT INTO general_vehicle (id, name, image_url, position) VALUES (%s, %s, %s, %s)"
                    values = (
                        vehicle["id"].replace('-',''), vehicle["name"], vehicle["image_url"], vehicle["position"])
                    cursor.execute(query, values)

            connection.commit()
    except mysql.connector.Error as error:
        print(f"{error}")


def init_locations():
    try:
        with mysql.connector.connect(**db_config) as connection:
            cursor = connection.cursor()

            for location in cities:
                check_query = "SELECT COUNT(*) FROM general_cities WHERE name = %s"
                check_value = (location["name"],)
                cursor.execute(check_query, check_value)
                count = cursor.fetchone()[0]

                if count == 0:
                    query = ("INSERT INTO general_cities (id, name,division_type, image_url, position) VALUES (%s, %s,"
                             "%s, %s, %s)")
                    values = (
                        location["id"].replace('-',''),
                        location["name"],
                        location["division_type"],
                        location["image_url"],
                        location["position"])
                    cursor.execute(query, values)

            connection.commit()
    except mysql.connector.Error as error:
        print(f"{error}")

def init_car_brand():
    try:
        with mysql.connector.connect(**db_config) as connection:
            cursor = connection.cursor()

            brand_list = [x for x in brands]

            for brand in brand_list:
                check_query = "SELECT COUNT(*) FROM rental_brand WHERE name = %s"
                check_value = (brand["name"],)
                cursor.execute(check_query, check_value)
                count = cursor.fetchone()[0]

                if count == 0:
                    # Add branch

                    query = "INSERT INTO rental_brand (id,name) VALUES (%s,%s)"
                    values = (
                        brand["id"].replace('-',''),
                        brand["name"],)
                    cursor.execute(query, values)

                    # Add models
                    for model_name in brand["models"]:
                        insert_model_sql = "INSERT INTO rental_model (id,name, brand_id) VALUES (%s,%s, %s);"
                        cursor.execute(insert_model_sql, [model_name["id"].replace('-',''),model_name["name"],  brand["id"].replace('-','')])

            connection.commit()
    except mysql.connector.Error as error:
        print(f"{error}")


init_vehicles()
init_locations()
init_car_brand()