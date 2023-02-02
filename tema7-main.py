from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/operasBas")
def operasBas():
    return render_template('operasbas.html')

@app.route("/resultado", methods=["POST"])
def resultado():
    numeroUno = request.form.get('txtNumeroUno')
    numeroDos = request.form.get('txtNumeroDos')
    resultado = int(numeroUno) * int(numeroDos) 
    return render_template('resultado.html', numeroUno = numeroUno, numeroDos = numeroDos, resultado = resultado)

if __name__ == "__main__":
    app.run(debug=True, port=8000)