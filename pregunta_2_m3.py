# -*- coding: utf-8 -*-
"""pregunta 2 M3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YCRGFda9lJTK_ieCL0zpr8AtvnHoQjKO
"""

class Vehiculo:
    def arrancar(self):
        print("El vehículo está en marcha")


class Coche(Vehiculo):
    def arrancar(self):
        print("El coche está en marcha")

if __name__ == "__main__":

    mi_coche = Coche()

    mi_coche.arrancar()

"""# Nueva sección"""