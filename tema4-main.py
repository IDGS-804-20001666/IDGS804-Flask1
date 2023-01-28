from flask import Flask
from flask import request

app = Flask(__name__)

# Decorador
@app.route("/suma", methods=["GET", "POST"])
def sumar():
    if request.method == "POST":
        numeroUno = request.form.get("numeroUno")
        numeroDos = request.form.get("numeroDos")
        return "<h1> La suma es: {} </h1>".format(str(int(numeroUno) + int(numeroDos)))
    else:
        return '''
            <form action="/suma" method="POST">
                <label>Número uno:</label><br>
                <input type="text" name="numeroUno"><br>
                <label>Número dos:</label><br>
                <input type="text" name="numeroDos"><br>
                <br>
                <input type="submit" value="Calcular">
            </form> 
        '''

if __name__ == "__main__":
    app.run(debug=True, port=8000)