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

def printArtworkData(artwork):
    print('Título de la obra: ' + artwork['Title'])
    print('Nombre(s) de autor(es): ')
    printAuthorNames(artwork)
    print('Año de creación: ' + artwork['Date'])
    print('Técnica usada: ' + artwork['Medium'])
    print('Dimensiones de la obra: ' + artwork['Dimensions'] + '\n')

def printAuthorNames(artwork):
    for artist in lt.iterator(cont['artists']):
        if artist['ConstituentID'] in artwork['ConstituentID']:
            print(artist['DisplayName'])
        # for cID in artwork['ConstituentID']:
        #     print(cID, artwork['ConstituentID'])
        #     if cID == artist['ConstituentID']:
        #         print(artist['DisplayName'])

def fThreePiecesRq2(list):
    print('\n Primeras 3 obras del rango: \n')
    printArtworkData(list['elements'][1])
    printArtworkData(list['elements'][2])
    printArtworkData(list['elements'][3])

def lThreePiecesRq2(list, size):
    print('Últimas 3 obras del rango: \n')
    printArtworkData(list['elements'][size - 3])
    printArtworkData(list['elements'][size - 2])
    printArtworkData(list['elements'][size - 1])

def fThreePiecesRq4(list):
    print('\nPrimeras 3 obras del país con mayor número de obras: \n')
    printArtworkData(list['elements'][1])
    printArtworkData(list['elements'][2])
    printArtworkData(list['elements'][3])

def lThreePiecesRq4(list):
    size = lt.size(list)
    print('Últimas 3 obras del país con mayor número de obras: \n')
    printArtworkData(list['elements'][size - 3])
    printArtworkData(list['elements'][size - 2])
    printArtworkData(list['elements'][size - 1])

def printAmmountByDA(dAList):
    print('Obras adquiridas por fecha de compra: \n')
    for dateDict in lt.iterator(dAList):
        print('En la fecha de ' + dateDict['date'] + ', se adquirió ' + str(lt.size(dateDict['pieces'])) + ' obra(s).')

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

def topTenCountries(catalog):
    n = 1
    while n <= 10:
        nationality = lt.getElement(catalog['nationalitiesList'], n)
        print('La nacionalidad', nationality['nationality'], 'tiene un total de', str(lt.size(nationality['artworks'])), 'obras.')
        n += 1

def topCountryArtworks(catalog):
    nationality = lt.getElement(catalog['nationalitiesList'], 1)
    fThreePiecesRq4(nationality['artworks'])
    lThreePiecesRq4(nationality['artworks'])

def printArtworksSizebyNationality(nationality):
    
    n = controller.artworksizebynationality(cont,nationality)
    print(n)
    pass



def printMenu():
    print("Bienvenido")
    print("1- Inicializar catálogo")
    print("2- Cargar información en el catálogo")
    print("3- Consultar las n obras más antiguas para un medio específico")
    print("4- Consultar las n obras por nacionalidad")

    print("6- Listar cronológicamente las adquisiciones")

    print("8- Clasificar obras por nacionalidad")

cont = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Inicializando catálogo...")
        cont = controller.initCatalog()
        
    elif int(inputs[0]) == 2:
        controller.loadData(cont)
        controller.loadNationalitiesList(cont)
        print('Obras cargadas: ' + str(controller.artworksSize(cont)))
        
    elif int(inputs[0]) == 3:
        n = int(input('Digite el numero de obras'))
        medio = input('Digite el el medio a usar')
        
        
        obras = controller.getArtworksByMedium(cont, medio)

        for x in obras['first']['next']:
            print(x)

        printArtworks_Medium_oldestDate(n,obras)

        pass

    elif int(inputs[0]) == 4:
        nationality = input('Digite la nacionalidad a contar')
        

        printArtworksSizebyNationality(nationality)

        pass

    elif int(inputs[0]) == 6:
        startDate = input('Escriba la fecha inicial del rango en el siguiente formato (AAAA-MM-DD): ')
        endDate = input('Escriba la fecha final del rango en el siguiente formato (AAAA-MM-DD): ')
        answer = controller.listByAcquireDate(cont, startDate, endDate)
        
        print('\n Total de obras en el rango: ' + str(answer[0]))
        printAmmountByDA(answer[2])
        fThreePiecesRq2(answer[1])
        lThreePiecesRq2(answer[1], answer[0])

    elif int(inputs[0]) == 8:
        topTenCountries(cont)
        topCountryArtworks(cont)
        
    else:
        sys.exit(0)
sys.exit(0)
