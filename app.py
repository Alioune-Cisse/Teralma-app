from flask import Flask, render_template, request
from basics import optimiser_depense, getdata, repartition

donnees = getdata()

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)















