﻿"""
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


import config as cf

from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog = {'pieces': None,
               'artists': None,
               'departments': None}
    catalog['pieces'] = mp.newMap(150000,
                                  maptype='CHAINING',
                                  loadfactor=4.0)
    catalog['artists'] = mp.newMap(16000,
                                   maptype='CHAINING',
                                   loadfactor=4.0)
    catalog['departments'] = mp.newMap(20,
                                   maptype='CHAINING',
                                   loadfactor=4.0)
    return catalog

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
               'artworksMedium': None,
               'Nationality': None}

    """
    Esta lista contiene todo los libros encontrados
    en los archivos de carga.  Estos libros no estan
    ordenados por ningun criterio.  Son referenciados
    por los indices creados a continuacion.
    """
    catalog['artworks'] = lt.newList('SINGLE_LINKED')

    catalog['artists'] = lt.newList('SINGLE_LINKED')

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
    

def addNationality(catalog, country):
    """
    Esta funcion adiciona un obra a la lista de obras,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Adicionalmente se guarda en el indice de artistas, una referencia
    al la obra.
   
    """
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
    
    
    
    

def newMedium(pubyear):
    """
    Esta funcion crea la estructura de libros asociados
            a un año.
    """
    entry = {'medium': "", 'artworks': None}
    entry['medium'] = pubyear
    entry['artworks'] = lt.newList('SINGLE_LINKED')
    return entry

def newNationality(nationality):
    """
    Esta funcion crea la estructura de libros asociados
            a un año.
    """
    entry = {'nationality': "", "artworks": None}
    entry['nationality'] = nationality
    entry['artworks'] = lt.newList('SINGLE_LINKED')
    return entry
# Funciones para creacion de datos



# Funciones de consulta

def artworksSize(catalog):
    """
    Numero de autores en el catalogo
    """
    return mp.size(catalog['artworks'])

def artworksizebynationality(catalog, nationality):   

    return mp.size(catalog['Nationality'][nationality])


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


# Funciones utilizadas para comparar elementos dentro de una lista
def comparedepartments(department1, department2):
    if (department1.lower() in department2['name'].lower()):
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


# Funciones de ordenamiento



