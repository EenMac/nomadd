from flask import Flask, render_template, request, redirect
from flask import Blueprint 
from models.cities import Cities
import repositories.cities_repo as cities_repo
import repositories.countries_repo as countries_repo

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def city():
    cities = cities_repo.select_all()
    return render_template("cities/cities.html", cities = cities)


@cities_blueprint.route("/cities/new", methods=['GET'])
def new_city():
    countries = countries_repo.select_all()
    return render_template("cities/new.html", countries = countries)

@cities_blueprint.route("/cities", methods = ['POST'])
# create a new city
def create_city():
    city_name = request.form['city_name']
    country_id = request.form['country_name']
    country = countries_repo.select(country_id)
    print(f"Returned country id {country.id}")
    visited = request.form['visited']
    # creates a dictionary - key is country_name
    city = Cities(city_name, country, visited)
    # create an instance
    cities_repo.save(city)
    return redirect('/cities')

@cities_blueprint.route("/cities/<id>")
def show_cities(id):
    cities = cities_repo.select(id)
    return render_template("cities/show.html", cities = cities)

@cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    cities_repo.delete(id)
    return redirect('/cities')

@cities_blueprint.route("/cities/<id>", methods=['GET'])
def show_city(id):
    city = cities_repo.select(id)
    return render_template('cities/show.html', city = city)