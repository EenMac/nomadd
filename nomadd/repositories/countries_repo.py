from db.run_sql import run_sql
from models.countries import Countries


# what functions do I want:
# SET UP THE SQL STATEMENT
# Cennect to db
# execute sql
# commit the changes to the database
# get the saved destination back with its ID

# SAVE
def save(country):
    sql = "INSERT INTO countries(country_name) VALUES (%s) RETURNING id"
    values = [country.country_name]
    # value for the %s 
    result = run_sql(sql, values)
    country.id = result[0]['id']
    # what the databae gives back
    return country

# SELECT_ALL
def select_all():
    countries = []

    sql= "SELECT * FROM countries ORDER BY country_name;"
    result = run_sql(sql)

    for row in result:
        country = Countries(row['country_name'], row['visited'],row['id'])
        countries.append(country)
    return countries

def select(id):
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        return Countries(result['country_name'], result['visited'], result['id'])

def delete_all():
    sql = "Delete FROM countries"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)


