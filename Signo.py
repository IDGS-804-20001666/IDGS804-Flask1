import datetime

class Signo():
    def calcularEdad(fecha):
        today = datetime.date.today()
        return today.year - fecha.year - ((today.month, today.day) < (fecha.month, fecha.day))

    def definirSigno(añoNacimiento):
        signos = [
            "Mono", "Gallo", "Perro", "Cerdo", "Rata", "Buey", "Tigre", "Conejo", "Dragón", "Serpiente", "Caballo", "Cabra"
        ]
        return signos[(añoNacimiento - 1900) % 12]
