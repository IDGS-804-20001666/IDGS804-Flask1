from flask import Flask, render_template
from flask import request
from Actividad3_calculos import Calculos
app = Flask(__name__)

@app.route("/cine")
def generarVistaCine():
    return render_template('cine.html')

@app.route("/resultado", methods=["POST"])
def generarResultado():
    nombre = str(request.form.get('txtNombre'))
    cantCompradores = int(request.form.get('txtCantidadP'))
    cantBoletos = int(request.form.get('txtCantidadB'))
    tarjeta = str(request.form.get('cineco'))
    datos = [nombre, cantBoletos, tarjeta]
    objCalculo = Calculos(cantCompradores = cantCompradores, cantBoletos=cantBoletos, tarjeta=tarjeta)
    objCalculo.generarPrecio()
    return render_template('resultadocine.html', pago = round(objCalculo.resultado, 2), datos = datos)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
