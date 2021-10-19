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
 """

import config as cf
import model
import csv
import model as model


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtworks(catalog)
    loadArtists(catalog)

def loadArtworks(catalog):
    """
    Carga los libros del archivo.  Por cada libro se indica al
    modelo que debe adicionarlo al catalogo.
    """
    artworksfile = cf.data_dir + 'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork) 

def loadArtists(catalog):
    """
    Carga los libros del archivo.  Por cada libro se indica al
    modelo que debe adicionarlo al catalogo.
    """
    artistsfile = cf.data_dir + 'Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)  
    

# Funciones de ordenamiento


    

# Funciones de consulta sobre el catálogo

def artworksSize(catalog):
    """
    Numero de obras cargados al catalogo
    """
    return model.artworksSize(catalog)

def getArtworksByMedium(catalog, medium):
    """
    Retorna los libros de un autor
    """
    mediumartworks = model.getArtworksByMedium(catalog, medium)
    return mediumartworks    

def getOldestArtwork(obras):
    """
    Retorna los libros de un autor
    """
    oldestArtowrk = model.getOldestArtwork(obras)
    return oldestArtowrk   

def getNewest_Arwork(obras):
    """
    Retorna los libros de un autor
    """
    newestArtowrk = model.getNewest_Arwork(obras)
    return newestArtowrk

def artworksizebynationality(catalog, nationality):  
    
    sizebynationality = model.artworksizebynationality(catalog, nationality)
    return sizebynationality

def listByAcquireDate(catalog, startDate, endDate):
    model.sortByAcquireDate(catalog)
    answer = model.listByAcquireDate(catalog, startDate, endDate)
    return answer

       