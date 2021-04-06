from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.countries import Countries
import repositories.countries_repo as countries_repo
import repositories.cities_repo as cities_repo

countries_blueprint = Blueprint("Countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = countries_repo.select_all()
    return render_template("countries/countries.html", countries = countries)

@countries_blueprint.route("/countries/<id>")
def show(id):
    countries = countries_repo.select(id)
    return render_template("countries/show.html", countries = countries)

