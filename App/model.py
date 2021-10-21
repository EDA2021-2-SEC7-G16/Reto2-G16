"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.DataStructures.arraylist import firstElement
import config as cf

from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from datetime import *
assert cf
import time

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    """ Inicializa el catálogo de libros

    Crea una lista vacia para guardar todos los libros

    Se crean indices (Maps) por los siguientes criterios:
    Autores
    ID libros
    Tags
    Año de publicacion

    Retorna el catalogo inicializado.
    """
    catalog = {'artworks': None,
               'artists': None, 
               'nationalitiesList': None,
               'departmentsList': None,
               'artworksMedium': None,
               'Nationality': None,
               'BornDate': None}

    """
    Esta lista contiene todo los libros encontrados
    en los archivos de carga.  Estos libros no estan
    ordenados por ningun criterio.  Son referenciados
    por los indices creados a continuacion.
    """
    catalog['artworks'] = lt.newList('SINGLE_LINKED')

    catalog['artists'] = lt.newList('SINGLE_LINKED')

    catalog['nationalitiesList'] = lt.newList('ARRAY_LIST',
                                   cmpfunction=comparedepartments)

    catalog['departmentsList'] = lt.newList('ARRAY_LIST')

    """
    A continuacion se crean indices por diferentes criterios
    para llegar a la informacion consultada.  Estos indices no
    replican informacion, solo referencian los libros de la lista
    creada en el paso anterior.
    """

    """
    Este indice crea un map cuya llave es el identificador del libro
    """
    catalog['artworksMedium'] = mp.newMap(300,
                                          maptype='CHAINING',
                                          loadfactor=4.0)

    catalog['Nationality'] = mp.newMap(80,
                                          maptype='CHAINING',
                                          loadfactor=4.0)

    catalog['BornDate'] = mp.newMap(200,
                                          maptype='CHAINING',
                                          loadfactor=4.0)                                                                                   

    catalog['ArtworksByArtist'] = mp.newMap(1500,
                                          maptype='CHAINING',
                                          loadfactor=4.0)   
    return catalog                                      


# Funciones para agregar informacion al catalogo

def addArtwork(catalog, artwork):
    """
    Esta funcion adiciona un obra a la lista de obras,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Adicionalmente se guarda en el indice de artistas, una referencia
    al la obra.
   
    """
    lt.addLast(catalog['artworks'], artwork)
    addArtworkMedium(catalog, artwork)
    addArtworkNationality(catalog, artwork)

def addArtist(catalog, artist):
    """
    Esta funcion adiciona un obra a la lista de obras,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Adicionalmente se guarda en el indice de artistas, una referencia
    al la obra.
   
    """
    lt.addLast(catalog['artists'], artist)
    addArtistByDate(catalog, artist)

def addNationalities(catalog):
    for artwork in lt.iterator(catalog['artworks']):
        addNationalityToList(catalog, artwork)
    sa.sort(catalog['nationalitiesList'], compareSizes)
    
def addNationalityToList(catalog, artwork):
    nationalitiesList = catalog['nationalitiesList']
    for artist in lt.iterator(catalog['artists']): 
        if artist['ConstituentID'] in artwork['ConstituentID']:
            if artist['Nationality'] == None:
                nationalityName = 'Nationality unknown'
            else:
                nationalityName = artist['Nationality']
            posNationality = lt.isPresent(nationalitiesList, nationalityName)
            if posNationality > 0:
                nationality = lt.getElement(nationalitiesList, posNationality)
            else:
                nationality = newNationality(nationalityName)
                lt.addLast(nationalitiesList, nationality)
            lt.addLast(nationality['artworks'], artwork)

def addNationality(catalog, country):
    """
    Esta funcion adiciona un obra a la lista de obras,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Adicionalmente se guarda en el indice de artistas, una referencia
    al la obra.
   
    """
    sa.sort
    lt.addLast(catalog['Nationality'], country)
           
    
def addArtworkMedium(catalog, artwork):
    """
    Esta funcion adiciona un libro a la lista de libros que
    fueron publicados en un año especifico.
    Los años se guardan en un Map, donde la llave es el año
    y el valor la lista de libros de ese año.
    """
  
    mediums = catalog['artworksMedium']
    if (artwork['Medium'] != ''):
        artworkmedium = artwork['Medium']
            
    else:
        artworkmedium = ''
    existmedium = mp.contains(mediums, artworkmedium)
    if existmedium:
        entry = mp.get(mediums, artworkmedium)
        medium = me.getValue(entry)
    else:
        medium = newMedium(artworkmedium)
        mp.put(mediums, artworkmedium, medium)
    lt.addLast(medium['artworks'], artwork)

def addArtistByDate(catalog, artist):
    """
    Esta funcion adiciona un libro a la lista de libros que
    fueron publicados en un año especifico.
    Los años se guardan en un Map, donde la llave es el año
    y el valor la lista de libros de ese año.
    """
  
    bornDates = catalog['BornDate']
    if (artist['BeginDate'] != 0):
        artistBornDate = artist['BeginDate']
            
    else:
        artistBornDate = ''
    existBornDate = mp.contains(bornDates, artistBornDate)
    if existBornDate:
        entry = mp.get(bornDates, artistBornDate)
        BornDate = me.getValue(entry)
    else:
        BornDate = newBornDate(artistBornDate)
        mp.put(bornDates, artistBornDate, BornDate)
    lt.addLast(BornDate['artists'], artist)  
      
     

def addArtworkNationality(catalog, artwork):
    """
    Esta funcion adiciona un libro a la lista de libros que
    fueron publicados en un año especifico.
    Los años se guardan en un Map, donde la llave es el año
    y el valor la lista de libros de ese año.
    """
    
    nationalities = catalog['Nationality']
    artworkAuthor = ''
    artworkNationality = None

    if (artwork['ConstituentID'][0] != ''):
        artworkAuthor = artwork['ConstituentID'][0]

    for author in lt.iterator(catalog['artists']):
        if author['ConstituentID'] == artworkAuthor:
            if author['Nationality'] == '':
                artworkNationality = 'Nationality unknown'
            else:
                artworkNationality = author['Nationality']

    existNationality = mp.contains(nationalities, artworkNationality)
    if existNationality:
        entry = mp.get(nationalities, artworkNationality)
        nationality = me.getValue(entry)
    else:
        nationality = newNationality(artworkNationality)
        mp.put(nationalities, artworkNationality, nationality)
    lt.addLast(nationality['artworks'], artwork)
    
    
def artworksbyArtistMedium(catalog, artist_name): 
    
    obras = lt.newList("ARRAY_LIST")
    id_artist = ''

    for artist in lt.iterator(catalog['artists']):
        

        if artist['DisplayName'] == artist_name:
            id_artist = artist['ConstituentID']
            

           

    for artwork in lt.iterator(catalog['artworks']):

        
        
        if id_artist in artwork['ConstituentID']:
            
            lt.addLast(obras, artwork)

    total_obras = lt.size(obras)

    
                  
                  
    
    
    map, mediumslist = newMapArtistByMedium(obras)

    
    

    return map, mediumslist, total_obras

    
def newMapArtistByMedium(artworks):   

    artworks_bymediumArtist = mp.newMap(100,
                                maptype='CHAINING',
                                loadfactor=4.0) 

    mediums_list = lt.newList("ARRAY_LIST")       

                        

    for artwork in lt.iterator(artworks):

        

        if artwork['Medium'] != '':
            artworkMedium = artwork['Medium']
        else:
            artworkMedium = ''   

        existMedium = mp.contains(artworks_bymediumArtist, artworkMedium)

        if existMedium:
            entry = mp.get(artworks_bymediumArtist,artworkMedium)
            medium =  me.getValue(entry)   
        else:
            lt.addLast(mediums_list, artworkMedium)
            medium = newMedium(artworkMedium)
            mp.put(artworks_bymediumArtist, artworkMedium ,medium)
        lt.addLast(medium['artworks'], artwork)
    
      

    return artworks_bymediumArtist,mediums_list






def newMedium(pubyear):
    """
    Esta funcion crea la estructura de libros asociados
            a un año.
    """
    entry = {'medium': "", 'artworks': None}
    entry['medium'] = pubyear
    entry['artworks'] = lt.newList('SINGLE_LINKED')
    return entry

def newBornDate(date):
    """
    Esta funcion crea la estructura de libros asociados
            a un año.
    """
    entry = {'BornDate': "", 'artists': None}
    entry['BornDate'] = date
    entry['artists'] = lt.newList('ARRAY_LIST')
    return entry

def newNationality(nationality):
    """
    Esta funcion crea la estructura de libros asociados
            a un año.
    """
    entry = {'nationality': "", "artworks": None}
    entry['nationality'] = nationality
    entry['artworks'] = lt.newList('ARRAY_LIST',
                                   cmpfunction=compareSizes)
    return entry

def addAcquireDate(aDList, date, piece):
    posAcquireDate = lt.isPresent(aDList, date)
    if posAcquireDate > 0:
        acquireDate = lt.getElement(aDList, posAcquireDate)
    else:
        acquireDate = newAcquireDate(date)
        lt.addLast(aDList, acquireDate)
    lt.addLast(acquireDate['pieces'], piece['Title'])

# Funciones para creacion de datos

def newAcquireDate(date):
    acquireDate = {'date': "", 'pieces': None}
    acquireDate['date'] = str(date)
    acquireDate['pieces'] = lt.newList('ARRAY_LIST')
    return acquireDate

# Funciones de consulta

def artworksSize(catalog):
    """
    Numero de autores en el catalogo
    """
    return mp.size(catalog['artworks'])

def artworksizebynationality(catalog, nationality):   

    return mp.size(catalog['Nationality'][nationality])



def artistByDate(catalog, anio_inicial,anio_final):   

    artistas = lt.newList('ARRAY_LIST')

    anios = mp.keySet(catalog['BornDate'])

    anios_ordenados = sortyears(anios)

    


    for anio in lt.iterator(anios_ordenados):

        
        
        if anio >= anio_inicial and anio <= anio_final:

            artist_list  = mp.get(catalog['BornDate'],anio)['value']['artists']

            
            

            for artist in lt.iterator(artist_list):


                lt.addLast(artistas,artist)

        pass
        

    return artistas   


def getArtworksByMedium(catalog, mediumname):
    """
    Retorna los libros de un medio especifico
    """
    medium = mp.get(catalog['artworksMedium'], mediumname)
    
    if medium:
        return me.getValue(medium)['artworks']
    return None     

def getOldestArtwork(obras):
    """
    Retorna los libros de un autor
    """
    oldest_artwork = ""
    oldest_date = 0
    for artwork in obras:
        print(type(obras))
        
        
        if int(artwork['Date']) > int(oldest_date):
            oldest_artwork =  obras[artwork] 
            oldest_date = obras[artwork]['Date']  


    return oldest_artwork   

def getNewest_Arwork(obras):
    """
    Retorna los libros de un autor
    """
    newest_Arwork = None
    newest_date = 0
    for artwork in obras:
        
        if int(artwork['Date']) < int(newest_date):
            newest_Arwork =  obras[artwork] 
            newest_date = obras[artwork]['Date']  


    return newest_Arwork

def listByAcquireDate(catalog, startDate, endDate):
    # Creación de las listas a retornar
    artworkList = lt.newList('ARRAY_LIST')
    byDatePurchase = lt.newList('ARRAY_LIST', cmpfunction=compareAD)

    for artwork in lt.iterator(catalog['artworks']):
        # Compara si la obra está dentro del rango de fechas
        if (artwork['DateAcquired'][0:3] >= startDate[0:3]) and (artwork['DateAcquired'][0:3] <= endDate[0:3]):
            if (artwork['DateAcquired'][5:6] >= startDate[5:6]) and (artwork['DateAcquired'][5:6] <= endDate[5:6]):
                if (artwork['DateAcquired'][8:9] >= startDate[8:9]) and (artwork['DateAcquired'][8:9] <= endDate[8:9]):
                    # Si la obra está dentro del rango, la anexa a la lista de obras dentro del rango
                    lt.addLast(artworkList, artwork)
                    # Anexa la obra a una lista con todas las obras adquiridas en una fecha
                    addAcquireDate(byDatePurchase, artwork['DateAcquired'], artwork)

    totalAmmount = lt.size(artworkList)
    return totalAmmount, artworkList, byDatePurchase

# Funciones utilizadas para comparar elementos dentro de una lista
def comparedepartments(department1, department2):
    if (department1.lower() in department2['nationality'].lower()):
        return 0
    return -1

def compareAD(aD1, aD2):
    if (aD1.lower() in aD2['date'].lower()):
        return 0
    return -1

def compareArtworkId(id1, id2):
    """
    Compara dos ids de dos libros
    """
    
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareSizes(item1, item2):
    return lt.size(item1['artworks']) > lt.size(item2['artworks'])

def compareArtworkDateMedium(id, tag):
    tagentry = me.getKey(tag)
    if (id == tagentry):
        return 0
    elif (id > tagentry):
        return 1
    else:
        return 0

def compareMediumNames(name, medium):
    mediumentry = me.getKey(medium)
    if (name == mediumentry):
        return 0
    elif (name > medium):
        return 1
    else:
        return -1    


def compareyears(year_1, year_2):

    

    return int(year_1) < int(year_2)
                
       

def compareAcquireDates(artwork1, artwork2):
    if artwork1['DateAcquired'][0:3] == artwork2['DateAcquired'][0:3]:
        if artwork1['DateAcquired'][5:6] == artwork2['DateAcquired'][5:6]:
            if artwork1['DateAcquired'][8:9] == artwork2['DateAcquired'][8:9]:
                return 0
            elif artwork1['DateAcquired'][8:9] > artwork2['DateAcquired'][8:9]:
                return 1
            else:
                return -1
        elif artwork1['DateAcquired'][5:6] > artwork2['DateAcquired'][5:6]:
            return 1
        else:
            return -1
    elif artwork1['DateAcquired'][0:3] > artwork2['DateAcquired'][0:3]:
        return 1
    else:
        return -1

# Funciones de ordenamiento

def sortyears(year_list):

    sorted_years = sa.sort(year_list, compareyears)

    return sorted_years


def sortByAcquireDate(catalog):
    sa.sort(catalog['artworks'], compareAcquireDates)

