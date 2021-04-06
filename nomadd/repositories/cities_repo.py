from db.run_sql import run_sql
from models.cities import Cities

# what functions do I want:

# SAVE
def save(city):
    sql = "INSERT INTO cities(city_name) VALUES (%s) RETURNING id"
    values = [city.city_name]
    result = run_sql(sql, values)
    city.id = result[0]['id']
    return city

# SELECT_ALL
def select_all():
    cities = []

    sql= "SELECT * FROM cities"
    result = run_sql(sql)

    for row in result:
        city = Cities(row['city_name'], row['id'])
        cities.append(city)
    return cities

def select(id):
    cities = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        city= Cities(result['city_name'], result['id'])
    return cities

def delete_all():
    sql = "Delete FROM cities"
    run_sql(sql)