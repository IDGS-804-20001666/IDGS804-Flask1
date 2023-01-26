from flask import Flask

app = Flask(__name__)

# Decorador
@app.route("/")
def index():
    return "¡Hola mundo! \nMensaje 5"

if __name__ == "__main__":
    app.run(debug=True, port=8000)