class Calculos():
    # Propiedades de clase
    cantBoletos = 0
    tarjeta = "false"
    resultado = 0
    precioBoleto = 12

    def __init__(self, cantCompradores, cantBoletos, tarjeta):
        self.cantCompradores = cantCompradores
        self.cantBoletos = cantBoletos
        self.tarjeta = tarjeta

    def generarPrecio(self):
        maxBoletos = self.cantCompradores * 7
        if(self.cantBoletos > maxBoletos):
            self.resultado = 0
            return
        
        self.resultado = self.cantBoletos * self.precioBoleto

        # Descuentos
        if self.cantBoletos > 5:
          self.resultado = self.resultado - self.resultado * 0.15
        elif self.cantBoletos >= 3 and self.cantBoletos <= 5:
          self.resultado = self.resultado - self.resultado * 0.10
        
        if self.tarjeta == "true":
          self.resultado = self.resultado * 0.90

        