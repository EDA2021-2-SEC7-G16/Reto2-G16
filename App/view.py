"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printArtworks_Medium_oldestDate(n,obras):
    """
    Imprime los libros que han sido publicados en un
    año
    """
    
    oldest_artwork = controller.getOldestArtwork(obras)
    newest_arwork = controller.getNewest_Arwork(obras)
    cont = 0
    for x in reversed(range(newest_arwork['Date'],oldest_artwork['Date']+1)):
        for y in obras:
            if lt.getElement(y,4) >= x:
                cont += 1
                print(lt.getElement(y,2))
            if cont == n:
                break

def printMenu():
    print("Bienvenido")
    print("1- Inicializar Catálogo")
    print("2- Cargar información en el catálogo")
    print("3- Consultar las n obras más antiguas para un medio específico")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        cont = controller.initCatalog()
        
    elif int(inputs[0]) == 2:
        controller.loadData(cont)
        print('Obras cargados: ' + str(controller.artworksSize(cont)))
        
    elif int(inputs[0]) == 3:
        n = int(input('Digite el numero de obras'))
        medio = input('Digite el el medio a usar')
        
        
        obras = controller.getArtworksByMedium(cont, medio)

        printArtworks_Medium_oldestDate(n,obras)

    else:
        sys.exit(0)
sys.exit(0)
