# Importamos la libreria que ayudara a crear el grafo
import networkx as nx
import matplotlib.pyplot as plt

#importamos pygame
import pygame as pg

# Creamos un grafo
Grafo = nx.Graph()

# Añadimos los nodos
Grafo.add_node("San Andres")
Grafo.add_node("Armenia")
Grafo.add_node("Barranquilla")
Grafo.add_node("Bucaramanga")
Grafo.add_node("Bogotá")
Grafo.add_node("Cali")
Grafo.add_node("Cartagena")
Grafo.add_node("Cúcuta")
Grafo.add_node("Leticia")
Grafo.add_node("Medellin")
Grafo.add_node("Monteria")
Grafo.add_node("Neiva")
Grafo.add_node("Pereira")
Grafo.add_node("Pasto")
Grafo.add_node("Riohacha")
Grafo.add_node("Santa Marta")
Grafo.add_node("Valledupar")
Grafo.add_node("Villavicencio")

# Añadimos las aristas
Grafo.add_edge("San Andres", "Armenia", weight=1112)
Grafo.add_edge("San Andres", "Barranquilla", weight=770)
Grafo.add_edge("San Andres", "Bucaramanga", weight=1118)
Grafo.add_edge("San Andres", "Bogotá", weight=1211)
Grafo.add_edge("San Andres", "Cali", weight=1163)
Grafo.add_edge("San Andres", "Cartagena", weight=720)
Grafo.add_edge("San Andres", "Cúcuta", weight=1133)
Grafo.add_edge("San Andres", "Leticia", weight=2273)
Grafo.add_edge("San Andres", "Medellin", weight=973)
Grafo.add_edge("San Andres", "Monteria", weight=765)
Grafo.add_edge("San Andres", "Neiva", weight=1283)
Grafo.add_edge("San Andres", "Pereira", weight=1087)
Grafo.add_edge("San Andres", "Pasto", weight=1354)
Grafo.add_edge("San Andres", "Riohacha", weight=962)
Grafo.add_edge("San Andres", "Santa Marta", weight=828)
Grafo.add_edge("San Andres", "Valledupar", weight=950)
Grafo.add_edge("San Andres", "Villavicencio", weight=1290)
Grafo.add_edge("Armenia", "San Andres", weight=1112)
Grafo.add_edge("Armenia", "Barranquilla", weight=721)
Grafo.add_edge("Armenia", "Bogotá", weight=181)
Grafo.add_edge("Armenia", "Bucaramanga", weight=412)
Grafo.add_edge("Armenia", "Cali", weight=153)
Grafo.add_edge("Armenia", "Cartagena", weight=651)
Grafo.add_edge("Armenia", "Cúcuta", weight=512)
Grafo.add_edge("Armenia", "Medellin", weight=190)
Grafo.add_edge("Armenia", "Monteria", weight=469)
Grafo.add_edge("Armenia", "Neiva", weight=176)
Grafo.add_edge("Armenia", "Pasto", weight=411)
Grafo.add_edge("Armenia", "Santa Marta", weight=764)
Grafo.add_edge("Armenia", "Velledupar", weight=712)
Grafo.add_edge("Armenia", "Villavicencio", weight=231)
Grafo.add_edge("Barranquilla", "San Andres", weight=770)
Grafo.add_edge("Barranquilla", "Armenia", weight=721)
Grafo.add_edge("Barranquilla", "Bucaramanga", weight=467)
Grafo.add_edge("Barranquilla", "Bogotá", weight=715)
Grafo.add_edge("Barranquilla", "Cali", weight=859)
Grafo.add_edge("Barranquilla", "Cartagena", weight=106)
Grafo.add_edge("Barranquilla", "Cúcuta", weight=424)
Grafo.add_edge("Barranquilla", "Leticia", weight=1773)
Grafo.add_edge("Barranquilla", "Medellin", weight=535)
Grafo.add_edge("Barranquilla", "Monteria", weight=277)
Grafo.add_edge("Barranquilla", "Neiva", weight=890)
Grafo.add_edge("Barranquilla", "Pereira", weight=695)
Grafo.add_edge("Barranquilla", "Pasto", weight=1122)
Grafo.add_edge("Barranquilla", "Santa Marta", weight=69)
Grafo.add_edge("Barranquilla", "Valledupar", weight=176)
Grafo.add_edge("Barranquilla", "Villavicencio", weight=771)
Grafo.add_edge("Bucaramanga", "San Andres", weight=1118)
Grafo.add_edge("Bucaramanga", "Armenia", weight=412)
Grafo.add_edge("Bucaramanga", "Barranquilla", weight=467)
Grafo.add_edge("Bucaramanga", "Bogotá", weight=299)
Grafo.add_edge("Bucaramanga", "Cali", weight=554)
Grafo.add_edge("Bucaramanga", "Cartagena", weight=450)
Grafo.add_edge("Bucaramanga", "Cúcuta", weight=110)
Grafo.add_edge("Bucaramanga", "Leticia", weight=1308)
Grafo.add_edge("Bucaramanga", "Medellin", weight=289)
Grafo.add_edge("Bucaramanga", "Monteria", weight=354)
Grafo.add_edge("Bucaramanga", "Neiva", weight=518)
Grafo.add_edge("Bucaramanga", "Pereira", weight=383)
Grafo.add_edge("Bucaramanga", "Pasto", weight=802)
Grafo.add_edge("Bucaramanga", "Santa Marta", weight=475)
Grafo.add_edge("Bucaramanga", "Valledupar", weight=373)
Grafo.add_edge("Bucaramanga", "Villavicencio", weight=334)
Grafo.add_edge("Bogotá", "San Andres", weight=1211)
Grafo.add_edge("Bogotá", "Armenia", weight=181)
Grafo.add_edge("Bogotá", "Barranquilla", weight=715)
Grafo.add_edge("Bogotá", "Bucaramanga", weight=299)
Grafo.add_edge("Bogotá", "Cali", weight=300)
Grafo.add_edge("Bogotá", "Cartagena", weight=663)
Grafo.add_edge("Bogotá", "Cúcuta", weight=406)
Grafo.add_edge("Bogotá", "Leticia", weight=1082)
Grafo.add_edge("Bogotá", "Medellin", weight=248)
Grafo.add_edge("Bogotá", "Monteria", weight=503)
Grafo.add_edge("Bogotá", "Neiva", weight=224)
Grafo.add_edge("Bogotá", "Pereira", weight=181)
Grafo.add_edge("Bogotá", "Pasto", weight=518)
Grafo.add_edge("Bogotá", "Santa Marta", weight=740)
Grafo.add_edge("Bogotá", "Valledupar", weight=659)
Grafo.add_edge("Bogotá", "Villavicencio", weight=70)
Grafo.add_edge("Cali", "San Andres", weight=1360)
Grafo.add_edge("Cali", "Armenia", weight=153)
Grafo.add_edge("Cali", "Barranquilla", weight=859)
Grafo.add_edge("Cali", "Bucaramanga", weight=554)
Grafo.add_edge("Cali", "Bogotá", weight=300)
Grafo.add_edge("Cali", "Cartagena", weight=779)
Grafo.add_edge("Cali", "Cúcuta", weight=664)
Grafo.add_edge("Cali", "Leticia", weight=1124)
Grafo.add_edge("Cali", "Medellin", weight=327)
Grafo.add_edge("Cali", "Monteria", weight=593)
Grafo.add_edge("Cali", "Neiva", weight=145)
Grafo.add_edge("Cali", "Pereira", weight=176)
Grafo.add_edge("Cali", "Pasto", weight=264)
Grafo.add_edge("Cali", "Santa Marta", weight=903)
Grafo.add_edge("Cali", "Valledupar", weight=859)
Grafo.add_edge("Cali", "Villavicencio", weight=330)
Grafo.add_edge("Cartagena", "San Andres", weight=720)
Grafo.add_edge("Cartagena", "Armenia", weight=1015)
Grafo.add_edge("Cartagena", "Barranquilla", weight=106)
Grafo.add_edge("Cartagena", "Bucaramanga", weight=450)
Grafo.add_edge("Cartagena", "Bogotá", weight=663)
Grafo.add_edge("Cartagena", "Cali", weight=779)
Grafo.add_edge("Cartagena", "Cúcuta", weight=432)
Grafo.add_edge("Cartagena", "Leticia", weight=1737)
Grafo.add_edge("Cartagena", "Medellin", weight=461)
Grafo.add_edge("Cartagena", "Monteria", weight=186)
Grafo.add_edge("Cartagena", "Neiva", weight=822)
Grafo.add_edge("Cartagena", "Pereira", weight=621)
Grafo.add_edge("Cartagena", "Pasto", weight=1039)
Grafo.add_edge("Cartagena", "Santa Marta", weight=173)
Grafo.add_edge("Cartagena", "Valledupar", weight=248)
Grafo.add_edge("Cartagena", "Villavicencio", weight=724)
Grafo.add_edge("Cúcuta", "San Andres", weight=1133)
Grafo.add_edge("Cúcuta", "Armenia", weight=512)
Grafo.add_edge("Cúcuta", "Barranquilla", weight=424)
Grafo.add_edge("Cúcuta", "Bucaramanga", weight=110)
Grafo.add_edge("Cúcuta", "Bogotá", weight=406)
Grafo.add_edge("Cúcuta", "Cali", weight=664)
Grafo.add_edge("Cúcuta", "Cartagena", weight=432)
Grafo.add_edge("Cúcuta", "Leticia", weight=1376)
Grafo.add_edge("Cúcuta", "Medellin", weight=386)
Grafo.add_edge("Cúcuta", "Monteria", weight=383)
Grafo.add_edge("Cúcuta", "Neiva", weight=627)
Grafo.add_edge("Cúcuta", "Pereira", weight=492)
Grafo.add_edge("Cúcuta", "Pasto", weight=913)
Grafo.add_edge("Cúcuta", "Santa Marta", weight=417)
Grafo.add_edge("Cúcuta", "Valledupar", weight=298)
Grafo.add_edge("Cúcuta", "Villavicencio", weight=435)
Grafo.add_edge("Leticia", "San Andres", weight=2273)
Grafo.add_edge("Leticia", "Barranquilla", weight=1773)
Grafo.add_edge("Leticia", "Bucaramanga", weight=1308)
Grafo.add_edge("Leticia", "Bogotá", weight=1082)
Grafo.add_edge("Leticia", "Cali", weight=1124)
Grafo.add_edge("Leticia", "Cartagena", weight=1737)
Grafo.add_edge("Leticia", "Cúcuta", weight=1376)
Grafo.add_edge("Leticia", "Medellin", weight=1321)
Grafo.add_edge("Leticia", "Monteria", weight=1585)
Grafo.add_edge("Leticia", "Pereira", weight=1189)
Grafo.add_edge("Leticia", "Santa Marta", weight=1782)
Grafo.add_edge("Medellin", "San Andres", weight=973)
Grafo.add_edge("Medellin", "Armenia", weight=190)
Grafo.add_edge("Medellin", "Barranquilla", weight=535)
Grafo.add_edge("Medellin", "Bucaramanga", weight=298)
Grafo.add_edge("Medellin", "Bogotá", weight=248)
Grafo.add_edge("Medellin", "Cali", weight=327)
Grafo.add_edge("Medellin", "Cartagena", weight=461)
Grafo.add_edge("Medellin", "Cúcuta", weight=386)
Grafo.add_edge("Medellin", "Leticia", weight=1321)
Grafo.add_edge("Medellin", "Monteria", weight=281)
Grafo.add_edge("Medellin", "Neiva", weight=362)
Grafo.add_edge("Medellin", "Pereira", weight=160)
Grafo.add_edge("Medellin", "Pasto", weight=591)
Grafo.add_edge("Medellin", "Santa Marta", weight=577)
Grafo.add_edge("Medellin", "Valledupar", weight=535)
Grafo.add_edge("Medellin", "Villavicencio", weight=317)
Grafo.add_edge("Monteria", "San Andres", weight=765)
Grafo.add_edge("Monteria", "Armenia", weight=469)
Grafo.add_edge("Monteria", "Barranquilla", weight=277)
Grafo.add_edge("Monteria", "Bucaramanga", weight=354)
Grafo.add_edge("Monteria", "Bogotá", weight=503)
Grafo.add_edge("Monteria", "Cali", weight=593)
Grafo.add_edge("Monteria", "Cartagena", weight=186)
Grafo.add_edge("Monteria", "Cúcuta", weight=383)
Grafo.add_edge("Monteria", "Leticia", weight=1585)
Grafo.add_edge("Monteria", "Medellin", weight=281)
Grafo.add_edge("Monteria", "Neiva", weight=643)
Grafo.add_edge("Monteria", "Pereira", weight=439)
Grafo.add_edge("Monteria", "Pasto", weight=853)
Grafo.add_edge("Monteria", "Santa Marta", weight=333)
Grafo.add_edge("Monteria", "Valledupar", weight=346)
Grafo.add_edge("Monteria", "Villavicencio", weight=569)
Grafo.add_edge("Neiva", "San Andres", weight=1283)
Grafo.add_edge("Neiva", "Armenia", weight=176)
Grafo.add_edge("Neiva", "Barranquilla", weight=890)
Grafo.add_edge("Neiva", "Bucaramanga", weight=518)
Grafo.add_edge("Neiva", "Bogotá", weight=224)
Grafo.add_edge("Neiva", "Cali", weight=145)
Grafo.add_edge("Neiva", "Cartagena", weight=822)
Grafo.add_edge("Neiva", "Cúcuta", weight=627)
Grafo.add_edge("Neiva", "Medellin", weight=362)
Grafo.add_edge("Neiva", "Monteria", weight=643)
Grafo.add_edge("Neiva", "Pereira", weight=206)
Grafo.add_edge("Neiva", "Pasto", weight=296)
Grafo.add_edge("Neiva", "Santa Marta", weight=925)
Grafo.add_edge("Neiva", "Valledupar", weight=861)
Grafo.add_edge("Neiva", "Villavicencio", weight=225)
Grafo.add_edge("Pereira", "San Andres", weight=1087)
Grafo.add_edge("Pereira", "Barranquilla", weight=695)
Grafo.add_edge("Pereira", "Bucaramanga", weight=383)
Grafo.add_edge("Pereira", "Bogotá", weight=181)
Grafo.add_edge("Pereira", "Cali", weight=176)
Grafo.add_edge("Pereira", "Cartagena", weight=621)
Grafo.add_edge("Pereira", "Cúcuta", weight=492)
Grafo.add_edge("Pereira", "Leticia", weight=1189)
Grafo.add_edge("Pereira", "Medellin", weight=160)
Grafo.add_edge("Pereira", "Monteria", weight=439)
Grafo.add_edge("Pereira", "Neiva", weight=206)
Grafo.add_edge("Pereira", "Pasto", weight=438)
Grafo.add_edge("Pereira", "Santa Marta", weight=735)
Grafo.add_edge("Pereira", "Valledupar", weight=684)
Grafo.add_edge("Pereira", "Villavicencio", weight=240)
Grafo.add_edge("Pasto", "San Andres", weight=1354)
Grafo.add_edge("Pasto", "Armenia", weight=411)
Grafo.add_edge("Pasto", "Barranquilla", weight=1122)
Grafo.add_edge("Pasto", "Bucaramanga", weight=802)
Grafo.add_edge("Pasto", "Bogotá", weight=518)
Grafo.add_edge("Pasto", "Cali", weight=264)
Grafo.add_edge("Pasto", "Cartagena", weight=1039)
Grafo.add_edge("Pasto", "Cúcuta", weight=913)
Grafo.add_edge("Pasto", "Medellin", weight=591)
Grafo.add_edge("Pasto", "Monteria", weight=853)
Grafo.add_edge("Pasto", "Neiva", weight=296)
Grafo.add_edge("Pasto", "Pereira", weight=438)
Grafo.add_edge("Pasto", "Santa Marta", weight=1167)
Grafo.add_edge("Pasto", "Valledupar", weight=1122)
Grafo.add_edge("Pasto", "Villavicencio", weight=521)
Grafo.add_edge("Riohacha", "San Andres", weight=962)
Grafo.add_edge("Riohacha", "Armenia", weight=837)
Grafo.add_edge("Riohacha", "Barranquilla", weight=213)
Grafo.add_edge("Riohacha", "Bucaramanga", weight=493)
Grafo.add_edge("Riohacha", "Bogotá", weight=783)
Grafo.add_edge("Riohacha", "Cali", weight=984)
Grafo.add_edge("Riohacha", "Cartagena", weight=313)
Grafo.add_edge("Riohacha", "Cúcuta", weight=408)
Grafo.add_edge("Riohacha", "Leticia", weight=1782)
Grafo.add_edge("Riohacha", "Medellin", weight=659)
Grafo.add_edge("Riohacha", "Monteria", weight=450)
Grafo.add_edge("Riohacha", "Neiva", weight=987)
Grafo.add_edge("Riohacha", "Pereira", weight=809)
Grafo.add_edge("Riohacha", "Pasto", weight=1247)
Grafo.add_edge("Riohacha", "Santa Marta", weight=145)
Grafo.add_edge("Riohacha", "Valledupar", weight=126)
Grafo.add_edge("Riohacha", "Villavicencio", weight=826)
Grafo.add_edge("Santa Marta", "San Andres", weight=828)
Grafo.add_edge("Santa Marta", "Armenia", weight=764)
Grafo.add_edge("Santa Marta", "Barranquilla", weight=69)
Grafo.add_edge("Santa Marta", "Bucaramanga", weight=475)
Grafo.add_edge("Santa Marta", "Bogotá", weight=740)
Grafo.add_edge("Santa Marta", "Cali", weight=903)
Grafo.add_edge("Santa Marta", "Cartagena", weight=173)
Grafo.add_edge("Santa Marta", "Cúcuta", weight=417)
Grafo.add_edge("Santa Marta", "Leticia", weight=1782)
Grafo.add_edge("Santa Marta", "Medellin", weight=577)
Grafo.add_edge("Santa Marta", "Monteria", weight=333)
Grafo.add_edge("Santa Marta", "Neiva", weight=925)
Grafo.add_edge("Santa Marta", "Pereira", weight=735)
Grafo.add_edge("Santa Marta", "Pasto", weight=1167)
Grafo.add_edge("Santa Marta", "Valledupar", weight=135)
Grafo.add_edge("Santa Marta", "Villavicencio", weight=792)
Grafo.add_edge("Valledupar", "San Andres", weight=950)
Grafo.add_edge("Valledupar", "Armenia", weight=712)
Grafo.add_edge("Valledupar", "Barranquilla", weight=176)
Grafo.add_edge("Valledupar", "Bucaramanga", weight=373)
Grafo.add_edge("Valledupar", "Bogotá", weight=659)
Grafo.add_edge("Valledupar", "Cali", weight=859)
Grafo.add_edge("Valledupar", "Cartagena", weight=248)
Grafo.add_edge("Valledupar", "Cúcuta", weight=298)
Grafo.add_edge("Valledupar", "Medellin", weight=535)
Grafo.add_edge("Valledupar", "Monteria", weight=346)
Grafo.add_edge("Valledupar", "Neiva", weight=861)
Grafo.add_edge("Valledupar", "Pereira", weight=684)
Grafo.add_edge("Valledupar", "Pasto", weight=1122)
Grafo.add_edge("Valledupar", "Santa Marta", weight=135)
Grafo.add_edge("Valledupar", "Villavicencio", weight=704)
Grafo.add_edge("Villavicencio", "San Andres", weight=1290)
Grafo.add_edge("Villavicencio", "Armenia", weight=231)
Grafo.add_edge("Villavicencio", "Barranquilla", weight=771)
Grafo.add_edge("Villavicencio", "Bucaramanga", weight=334)
Grafo.add_edge("Villavicencio", "Bogotá", weight=70)
Grafo.add_edge("Villavicencio", "Cali", weight=330)
Grafo.add_edge("Villavicencio", "Cartagena", weight=724)
Grafo.add_edge("Villavicencio", "Cúcuta", weight=435)
Grafo.add_edge("Villavicencio", "Medellin", weight=317)
Grafo.add_edge("Villavicencio", "Monteria", weight=569)
Grafo.add_edge("Villavicencio", "Neiva", weight=225)
Grafo.add_edge("Villavicencio", "Pereira", weight=240)
Grafo.add_edge("Villavicencio", "Pasto", weight=521)
Grafo.add_edge("Villavicencio", "Santa Marta", weight=792)
Grafo.add_edge("Villavicencio", "Valledupar", weight=704)

#Creamos nuestra interfaz

#Algoritmo de dijkstra
djk_path = nx.dijkstra_path(Grafo, source="Leticia", target="Riohacha", weight="weight")

#Mostramos la solucion en pantalla
print("La ruta mas corta es: ", djk_path)