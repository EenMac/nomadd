from db.run_sql import run_sql
from models.cities import Cities
from models.countries import Countries
import repositories.countries_repo as countries_repo
# what functions do I want:

# what functions do I want:
# SET UP THE SQL STATEMENT
# Cennect to db
# execute sql
# commit the changes to the database
# get the saved destination back with its ID


# SAVE
def save(city):
    sql = "INSERT INTO cities (city_name, visited, country_id) VALUES (%s, %s, %s) RETURNING id"
    values = [city.city_name, city.visited,  city.country.id]
    result = run_sql(sql, values)
    id = result[0]['id']
    city.id = id
    return city


# SELECT_ALL cities
def select_all():
    cities = []
# create an empty array called cities
    sql= "SELECT * FROM cities"
    # sql command we want to run in the database
    result = run_sql(sql)
# variable that will execute the sql statement and return a value

# for loop - that searches through all the possible returned ids from the database and append them to to empty array; cities
    for row in result:
        country = countries_repo.select(row['country_id'])
        city = Cities(row['city_name'], country, row['visited'], row['id'])
        cities.append(city)
    return cities


# Select
def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = countries_repo.select(result['country_id'])
        city= Cities(result['city_name'], country, result['visited'], result['id'])
    return city
#delete-all
def delete_all():
    sql = "Delete FROM cities"
    run_sql(sql)
#delete
def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)