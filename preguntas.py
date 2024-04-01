"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
from itertools import count
from operator import itemgetter


datos = open("data.csv","r").readlines()
datos = [z.replace("\n","") for z in datos]


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    col2=[z[2] for z in datos]
    suma = sum([int(numero) for numero in col2])

    return suma
    

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    col1=[z[0] for z in datos]
    col1.sort()
    l=[(x ,col1.count(x)) for x in col1]
    diccionario = {key:valor for key, valor in l}
    lista = []
    [lista.append(item) for item in diccionario.items()]
    return lista

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    col1=[z[0] for z in datos]
    col2=[int(z[2]) for z in datos]
    zipped=list(zip(col1, col2))
    f=itemgetter(0)
    zipped = sorted(zipped,key=f)
    contador={}
    for key,value in zipped:
        contador[key]= contador.get(key,0)+value

    return [(key,contador[key]) for key in contador]

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    col3=[z[9:11] for z in datos]
    col3.sort()
    l=[(x ,col3.count(x)) for x in col3]
    diccionario = {key:valor for key, valor in l}
    lista = []
    [lista.append(item) for item in diccionario.items()]

    return lista



def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    col1=[z[0] for z in datos]
    col2=[int(z[2]) for z in datos]
    zipped=list(zip(col1, col2))
    f=itemgetter(0)
    zipped = sorted(zipped,key=f)
    d_mayor={}
    d_menor= {}
    for i in zipped:
        if i[0] in d_mayor:
            if d_mayor[i[0]]<i[1]:
                d_mayor[i[0]]=i[1]
        else:
            d_mayor[i[0]]=i[1]
    for i in zipped:
        if i[0] in d_menor:
            if d_menor[i[0]]>i[1]:
                d_menor[i[0]]=i[1]
        else:
            d_menor[i[0]]=i[1]
    lista = []

    for i in zipped:
        lista.append ((i[0],d_mayor[i[0]],d_menor[i[0]]))
    lista=list(set(lista)) #Limpiando repetidos

    f=itemgetter(0)
    lista = sorted(lista,key=f)

    return lista


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    datos6=[z.replace("\t",";") for z in datos]
    datos6=[z.split(";") for z in datos6]
    col6= [z[4] for z in datos6]
    col6= [z.split(",") for z in col6]
    mayor={}
    menor={}
    for palabras in col6:
        for i in palabras:
            if i[0:3] in mayor:
                if mayor[i[0:3]]<int(i[4:]):
                    mayor[i[0:3]]=int(i[4:])
            else:
                mayor[i[0:3]]=int(i[4:])
        for i in palabras:
            if i[0:3] in menor:
                if menor[i[0:3]]>int(i[4:]):
                    menor[i[0:3]]=int(i[4:])
            else:
                menor[i[0:3]]=int(i[4:])     
    
    lista = [(i,menor[i],mayor[i]) for i in mayor]

    f=itemgetter(0)
    lista = sorted(lista,key=f)

    return lista


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    col1=[z[0] for z in datos] #letras col 1
    col2=[int(z[2]) for z in datos] #numero col 2
    zipped=list(zip(col1, col2)) #Col 1 + Col 2
    d={}
    for i in zipped:
        if i[1] in d:
            d[i[1]]+=i[0]
            
        else:
            d[i[1]]=i[0]
    lista = [(i,list(d[i])) for i in d]
    f=itemgetter(0)
    lista = sorted(lista,key=f)
    return lista



def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    col1=[z[0] for z in datos] #letras col 1
    col2=[int(z[2]) for z in datos] #numero col 2
    zipped=list(zip(col1, col2)) #Col 1 + Col 2
    d={}
    d1={}
    for i in zipped:
        if i[1] in d:
            d[i[1]]+=i[0]       
        else:
            d[i[1]]=i[0]
                
    d = [(z, sorted(list(set(list(d[z]))))) for z in d]
    f=itemgetter(0)
    d = sorted(d,key=f)

    return d


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    datos6=[z.replace("\t",";") for z in datos]
    datos6=[z.split(";") for z in datos6]
    col6= [z[4] for z in datos6]
    col6= [z.split(",") for z in col6]
    diccionario={}
    for elemento in col6:
        for i in elemento:
            if i[0:3] in diccionario:
                diccionario[i[0:3]]+=1
            else:
                diccionario[i[0:3]]=1
    f=itemgetter(0)
    diccionario = sorted(diccionario.items(),key=f)
    diccionario1 = {valor: numero for valor, numero in diccionario}

    return diccionario1


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    datos6=[z.replace("\t",";") for z in datos]
    datos6=[z.split(";") for z in datos6]
    ejercicio=[(z[0],len(z[3].split(",")),len(z[4].split(","))) for z in datos6]

    return ejercicio


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    datos6=[z.replace("\t",";") for z in datos]
    datos6=[z.split(";") for z in datos6]
    ejercicio=[(((z[1]),z[3].split(","))) for z in datos6]
    valor=0
    d={}
    for tupla in ejercicio:
        for elemento in tupla:
            valor=int(tupla[0])
            if elemento == tupla[1]:
                for letra in elemento:
                    if letra in d:
                        d[letra]+=valor
                    else:
                        d[letra]=valor
    f=itemgetter(0)
    d = sorted(d.items(),key=f)
    d1 = {valor: numero for valor, numero in d}
    return d1



def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    datos6=[z.replace("\t",";") for z in datos]
    datos6=[z.split(";") for z in datos6]
    col1=[z[0] for z in datos6]
    col5= [z[4] for z in datos6]
    col5= [z.split(",") for z in col5]
    zipped=list(zip(col1,col5))
    d={}
    for tupla in zipped:
        d[tupla[0]]=0
    for tupla in zipped:
        if tupla[0] in d:
            for valor in tupla[1]:
                d[tupla[0]]+=int(valor[4:])

    f=itemgetter(0)
    d = sorted(d.items(),key=f)
    d1 = {valor: numero for valor, numero in d}
    return d1

