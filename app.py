from flask import Flask, render_template, request, jsonify
from basics import optimiser_depense, getdata, repartition
import json
import ast

donnees = getdata()

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return render_template('home.html', data=donnees)

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        budget = request.form['budget']
        services = request.form.getlist('choix')
        depenses = optimiser_depense(int(budget), services)
        repartitions = repartition(depenses)
        return render_template('after.html',
                               data2=optimiser_depense(int(budget), services),
                               data3=repartition(optimiser_depense(int(budget), services)),
                               zip=zip, round=round, sum=sum
                               )

    else:
        return render_template('after.html')
   

@app.route('/api/v1', methods=['GET', 'POST'])
def my_route():
  budget = request.args.get('budget', default = 1200000, type = int)
  services = request.args.get('services', default = ["Traiteur", "Photo"], type = str)
  services = ast.literal_eval(services)
  invites = request.args.get('invites', default=100, type=int)
  print(f'services = {services}\nTypes = {type(services)}')
  repartitions = repartition(optimiser_depense(int(budget),  services))
  print(repartitions)
  return jsonify(repartitions)


if __name__ == "__main__":
    app.run(debug=True)















