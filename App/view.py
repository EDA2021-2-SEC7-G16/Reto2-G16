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
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
import time

default_limit = 1000 
sys.setrecursionlimit(default_limit*100)
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

def printArtistByDate(anio_inicial,anio_final):
    
    n = controller.artistByDate(cont, anio_inicial,anio_final)
    
    size = lt.size(n)
    
    print('El total de artistas en este rango es de: ',lt.size(n))

    if lt.size(n)>6:

        elementos = (1,2,3,size-2,size-1,size)

        for x in elementos:

            print(x,')')

            if lt.getElement(n,x)['DisplayName'] != '':
                print('Nombre: ',lt.getElement(n,x)['DisplayName'])
            else:
                print('Nombre: Unknown')

            if lt.getElement(n,x)['BeginDate'] != str(0):
                print('Año de nacimiento: ',lt.getElement(n,x)['BeginDate'])
            else:
                rint('Año de nacimiento: Unknown')

            if lt.getElement(n,x)['EndDate'] != str(0):
                print('Año de fallecimiento: ',lt.getElement(n,x)['EndDate'])
            else:
                print('Año de fallecimiento: Unknown')  

            if lt.getElement(n,x)['Nationality'] != '':
                print('Nacionalidad: ',lt.getElement(n,x)['Nationality'])
            else:
                print('Nacionalidad: Unknown')

            if lt.getElement(n,x)['Gender'] != '':
                print('Genero: ',lt.getElement(n,x)['Gender'])
            else:
                print('Genero: Unknown')                
       
    else:

        for x in range(1,lt.size(n)+1):
            print(x,')')

            if lt.getElement(n,x)['DisplayName'] != '':
                print('Nombre: ',lt.getElement(n,x)['DisplayName'])
            else:
                print('Nombre: Unknown')

            if lt.getElement(n,x)['BeginDate'] != str(0):
                print('Año de nacimiento: ',lt.getElement(n,x)['BeginDate'])
            else:
                rint('Año de nacimiento: Unknown')

            if lt.getElement(n,x)['EndDate'] != str(0):
                print('Año de fallecimiento: ',lt.getElement(n,x)['EndDate'])
            else:
                print('Año de fallecimiento: Unknown')  

            if lt.getElement(n,x)['Nationality'] != '':
                print('Nacionalidad: ',lt.getElement(n,x)['Nationality'])
            else:
                print('Nacionalidad: Unknown')

            if lt.getElement(n,x)['Gender'] != '':
                print('Genero: ',lt.getElement(n,x)['Gender'])
            else:
                print('Genero: Unknown')        

             


        

def printArtworksbyArtistMedium(artist_name):
    
    map,lista_medios, n_obras = controller.artworksbyArtistMedium(cont,artist_name)
    print('El total de obras para este artista es de: ',n_obras)
    print('El total de medios utilizados por este artista es de: ', mp.size(map))

    n_biggest_medium = 0
    bigget_medium = ''
    

    for x in lt.iterator(lista_medios):
        
        if lt.size(mp.get(map,x)['value']['artworks']) > n_biggest_medium:
            n_biggest_medium = lt.size(mp.get(map,x)['value']['artworks'])
            bigget_medium = x

    print('El medio mas utilizado es: ', bigget_medium)        

    listartworks_biggest_medium = mp.get(map,bigget_medium)['value']['artworks']

    if n_biggest_medium > 6:
        elemntos = (1,2,3, n_biggest_medium-2, n_biggest_medium-1, n_biggest_medium)
        for y in elemntos:
            print('obra ', y)
            print('Titulo: ',lt.getElement(listartworks_biggest_medium,y)['Title'])
            print('Fecha de la obra: ', lt.getElement(listartworks_biggest_medium,y)['Date'])
            print('Medio: ',lt.getElement(listartworks_biggest_medium,y)['Medium'])
            print('Dimensiones: ',lt.getElement(listartworks_biggest_medium,y)['Dimensions'])

    else:

        
        for y in range(1, n_biggest_medium+1):
            print('obra ', y)
            print('Titulo: ',lt.getElement(listartworks_biggest_medium,y)['Title'])
            print('Fecha de la obra: ', lt.getElement(listartworks_biggest_medium,y)['Date'])
            print('Medio: ',lt.getElement(listartworks_biggest_medium,y)['Medium'])
            print('Dimensiones: ',lt.getElement(listartworks_biggest_medium,y)['Dimensions'])



    

def printMenu():
    print("Bienvenido")
    print("1- Inicializar catálogo")
    print("2- Cargar información en el catálogo")
    print("3- Consultar las n obras más antiguas para un medio específico")
    print("4- Consultar las n obras por nacionalidad")
    print('5- Listar cronologicamente los artistas')

    print("6- Listar cronológicamente las adquisiciones")
    print("7- Clasificar las obras de un artista por tecnica")

    print("8- Clasificar obras por nacionalidad")
    print("9- Transportar obras de un departamento")

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

        

    elif int(inputs[0]) == 5:
        anio_inicial = input('Ingrese el año inicial')
        anio_final = input('Ingrese el año final')
        startTime = time.process_time()
        printArtistByDate(anio_inicial,anio_final)
        stopTime = time.process_time()
        elapsedTime = (stopTime - startTime) * 1000
        print('El tiempo que se demoró en ejecutar fue de ' + str(elapsedTime) + ' ms.')

        pass

    elif int(inputs[0]) == 6:
        startDate = input('Escriba la fecha inicial del rango en el siguiente formato (AAAA-MM-DD): ')
        endDate = input('Escriba la fecha final del rango en el siguiente formato (AAAA-MM-DD): ')
        startTime = time.process_time()
        answer = controller.listByAcquireDate(cont, startDate, endDate)
        
        print('\n Total de obras en el rango: ' + str(answer[0]))
        printAmmountByDA(answer[2])
        fThreePiecesRq2(answer[1])
        lThreePiecesRq2(answer[1], answer[0])
        stopTime = time.process_time()
        elapsedTime = (stopTime - startTime) * 1000
        print('El tiempo que se demoró en ejecutar fue de ' + str(elapsedTime) + ' ms.')

    elif int(inputs[0]) == 8:
        startTime = time.process_time()
        topTenCountries(cont)
        topCountryArtworks(cont)
        stopTime = time.process_time()
        elapsedTime = (stopTime - startTime) * 1000
        print('El tiempo que se demoró en ejecutar fue de ' + str(elapsedTime) + ' ms.')

    elif int(inputs[0]) == 9:
        department = input('Escriba el nombre del departamento del museo: ')
        depList = controller.transportDepartment(cont, department)

    elif int(inputs[0]) == 7:
        startTime = time.process_time()
        artist_name = input('Digite el nombre del artista')
        stopTime = time.process_time()
        elapsedTime = (stopTime - startTime) * 1000
        print('El tiempo que se demoró en ejecutar fue de ' + str(elapsedTime) + ' ms.')
        

        printArtworksbyArtistMedium(artist_name)
        print('El tiempo que se demoró en ejecutar fue de ' + str(elapsedTime) + ' ms.')


    else:
        sys.exit(0)
sys.exit(0)
