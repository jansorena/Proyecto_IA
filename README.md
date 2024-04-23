# Proyecto_IA

## Breve descripción del problema que abordarán
Mario es un videojuego reconocido mundialmente que requiere de un jugador real si o si. No puedes visualizar como se juega de manera autonoma si lo deseas.

## Solución propuesta de manera clara
Permitir que Mario juegue de manera independiente, esto por medio de la implementación de un algoritmo de aprendizaje por refuerzo que logre esto.

## Descripción del ambiente
Parcialmente observable
Estocástico
Secuencial
Dinámico
Discreto
Agente singular

## Representación concreta del estado del juego, representada por una estructura de datos
Se puede representar por medio de una matriz de estados, donde:
0: Representa vacio
1: Representa un bloque no traspasable
2: Representa un enemigo cualquiera
3: Representa al jugador

ESTADO DE EJEMPLO
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 3, 1, 1, 1, 1, 1, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

## Descripción de las acciones que puede tomar el agente

## Representación concreta de las acciones, representada por una estructura de datos
