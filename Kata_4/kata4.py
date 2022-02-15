#Ejercicio 1
from __future__ import division


text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
partes = text.split(". ")
palabras = ["average", "temperature", "distance"]
for parte in partes:
  for palabra in palabras:
    if palabra in parte:
      print(parte.replace(" C", " Celsius"))
      break
# Ejercicio 2
name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"
titulo = f'la gravedad en {planet}'
nueva_plantilla = """
Datos de Gravedad sobre: {name}
-------------------------------------------------------------------------------
Nombre del planeta: {planet}
Gravedad en {name}: {gravity} m/s2
"""
print(nueva_plantilla.format(name=name, planet=planet, gravity=gravity*1000))