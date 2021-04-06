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

@cities_blueprint.route("/cities/<id>.")
def show_cities(id):
    cities = cities_repo.select(id)
    return render_template("cities/cities.html", cities = cities)