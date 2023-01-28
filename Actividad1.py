from flask import Flask
from flask import request

app = Flask(__name__)

# Decorador
@app.route("/operacion", methods=["GET", "POST"])
def operar():
    if request.method == "POST":
        numeroUno = request.form.get("numeroUno")
        numeroDos = request.form.get("numeroDos")
        operacion = request.form.get("operacion")
        if(operacion == "sumar"):
            return "<h1> El resultado es: {} </h1>".format(str(int(numeroUno) + int(numeroDos)))
        elif(operacion == "restar"):
            return "<h1> El resultado es: {} </h1>".format(str(int(numeroUno) - int(numeroDos)))
        elif(operacion == "multiplicar"):
            return "<h1> El resultado es: {} </h1>".format(str(int(numeroUno) * int(numeroDos)))
        elif(operacion == "dividir"):
            return "<h1> El resultado es: {} </h1>".format(str(int(numeroUno) / int(numeroDos)))
    else:
        return '''
            <form action="/operacion" method="POST">
                <label>Número uno:</label><br>
                <input type="text" name="numeroUno"><br>
                <label>Número dos:</label><br>
                <input type="text" name="numeroDos"><br>
                <br>
                <label>Sumar:</label>
                <input type="radio" id="html" name="operacion" value="sumar">
                <br>
                <label>Restar:</label>
                <input type="radio" id="html" name="operacion" value="restar">
                <br>
                <label>Multiplicar:</label>
                <input type="radio" id="html" name="operacion" value="multiplicar">
                <br>
                <label>Dividir:</label>
                <input type="radio" id="html" name="operacion" value="dividir">
                <br>
                <input type="submit" value="Calcular">
            </form> 
        '''
if __name__ == "__main__":
    app.run(debug=True, port=8000)