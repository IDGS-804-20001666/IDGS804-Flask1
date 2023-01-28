from flask import Flask

app = Flask(__name__)

# Decorador
@app.route("/")
def index():
    return "¡Hola mundo! \nMensaje 5"

# Se pasa un string por la url
@app.route("/user/<string:user>/")
def user(user):
    return "¡Hola! " + str(user)

# Se pasa un int por la url
@app.route("/numero/<int:numero>/")
def numero(numero):
    return "Número: {}".format(numero)

# Se pasa más de un parámetro por la url
@app.route("/user/<int:id>/<string:username>/")
def usern(id, username):
    return "ID: {}, Nombre: {}".format(id, username)


# Se pasa un int por la url
@app.route("/suma/<float:n1>/<float:n2>")
def sumar(n1, n2):
    return "Suma: {}".format(n1 + n2)

if __name__ == "__main__":
    app.run(debug=True, port=8000)