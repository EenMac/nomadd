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

@countries_blueprint.route("/countries/new", methods=['GET'])
def new_country():
    countries = countries_repo.select_all()
    return render_template("countries/new.html", countries = countries)

@countries_blueprint.route("/countries", methods = ['POST'])
def create_country():
    country_name = request.form['country_name']
    # creates a dictionary - key is country_name
    country = Countries(country_name)
    # create an instance
    countries_repo.save(country)
    return redirect('/countries')

@countries_blueprint.route("/countries/<id>")
def show(id):
    countries = countries_repo.select(id)
    return render_template("countries/show.html", countries = countries)


@countries_blueprint.route("/countries/<id>/delete", methods = ['POST'])
def delete_country(id):
    countries_repo.delete(id)
    return redirect('/countries')

@countries_blueprint.route("/countries/<id>", methods = ['GET'])
def show_country(id):
    country = countries_repo.select(id)
    return render_template('countries/show.html', country = country)

