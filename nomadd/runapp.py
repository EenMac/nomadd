from flask import Flask, render_template

from controllers.countries_controller import countries_blueprint
from controllers.cities_controller import cities_blueprint

runapp = Flask(__name__)

runapp.register_blueprint(countries_blueprint)
runapp.register_blueprint(cities_blueprint)

@runapp.route("/")
def home():
    return render_template ('index.html')

if __name__ =='__main__':
    runapp.run(debug=True) 