from flask import Flask

app = Flask(__name__)

# Decorador
@app.route("/")
def iniciar():
    return "¡Hola mundo! \nMensaje 5"

@app.route("/hola")
def saludar():
    return "¡Hola IDGS804!"

if __name__ == "__main__":
    app.run(debug=True, port=8000)