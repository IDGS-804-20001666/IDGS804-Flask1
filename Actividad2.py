from flask import Flask, render_template
from flask import request
import math

app = Flask(__name__)

@app.route("/distancia")
def distancia():
    return render_template('distancia.html')

@app.route("/resultado", methods=["POST"])
def resultado():
    x1 = float(request.form.get('txtX1'))
    x2 = float(request.form.get('txtX2'))
    y1 = float(request.form.get('txtY1'))
    y2 = float(request.form.get('txtY2'))
    coordenadas = [x1, x2, y1, y2]
    resultado = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return render_template('resultadodistancia.html', resultado = resultado, coordenadas = coordenadas)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
