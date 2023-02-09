from flask import Flask, render_template, request
from Signo import Signo
import datetime
import json

objSigno = Signo

app = Flask(__name__)

@app.route("/datosp")
def generarVistaDatosP():
    return render_template('datospersonales.html')

@app.route("/examen")
def generarVistaExamen():
    return render_template('examen.html')

@app.route("/resultado", methods=["POST"])
def generarResultado():
    datosp = json.loads(request.form.get('datosp'))
    examen = request.form.get('examen')

    type(datosp)
    type(examen)

    fechaNacimiento = datetime.date(int(datosp[5]), int(datosp[4]), int(datosp[3]))
    edad = objSigno.calcularEdad(fechaNacimiento)
    signo = objSigno.definirSigno(int(datosp[5]))

    return render_template('resultadopractica.html', datos = datosp, edad = edad, calificacion = examen, signo = signo)

if __name__ == "__main__":    
    app.run(debug=True, port=8000)
