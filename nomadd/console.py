from flask import Flask, render_template
import pdb
from models.countries import Countries
from models.cities import Cities


import repositories.countries_repo as countries_repo
import repositories.cities_repo as cities_repo


Country1 = Countries("Ireland", None)
countries_repo.save(Country1)
Country2 = Countries("Germany", None)
countries_repo.save(Country2)
Country3 = Countries("Scotland", None)
countries_repo.save(Country3)
City1 = Cities("Dublin", Country1)
cities_repo.save(City1)
City2 = Cities("Berlin", Country2)
cities_repo.save(City2)
City3 = Cities("Edinburgh", Country3)
cities_repo.save(City3)



pdb.set_trace()
