# Proyecto_IA
Integrantes:
- Jaime Ansorena
- Diego Oporto
- Dayan Sáez

## Breve descripción del problema que abordarán
Mario es un videojuego reconocido mundialmente que requiere de un jugador real si o si. No puedes visualizar como se juega de manera autonoma si lo deseas.

## Solución propuesta de manera clara
Permitir que Mario juegue de manera independiente, esto por medio de la implementación de un algoritmo de aprendizaje por refuerzo que logre esto.

## Descripción del ambiente
- **Parcialmente observable**: Agente no puede ver todo el entorno del juego simultáneamente.
- **Estocástico**: El resultado de las acciones tomadas por el agente no siempre es predecible debido a la aleatoriedad en el juego.
- **Secuencial**: Las acciones del agente tienen consecuencias a lo largo del tiempo.
- **Dinámico**: El entorno del juego cambia constantemente.
- **Discreto**: Las acciones y estados en el juego son discretos y pueden ser representados de manera finita.
- **Agente singular**: Solo hay un agente en el juego.
- **Representación concreta del estado del juego**: Se puede representar el estado del juego mediante una matriz de estados.

## Representación concreta del estado del juego, representada por una estructura de datos
Se puede representar por medio de una matriz de estados, donde:
- **0**: Representa vacio
- **1**: Representa un bloque no traspasable
- **2**: Representa un enemigo cualquiera
- **3**: Representa al jugador

### Estado de ejemplo
```math
\begin{bmatrix}
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 1 & 0 & 0 & 3 & 1 & 1 & 1 & 1 & 1 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1
\end{bmatrix}
```

## Descripción de las acciones que puede tomar el agente
El agente puede moverse en las direcciones izquierda, derecha y arriba (salto vertical). Tambien puede agacharse y saltar con dirección hacia la derecha o izquierda. Además, puede disparar si este alcanza su 3ra forma.

## Representación concreta de las acciones, representada por una estructura de datos
Los movimientos pueden encasillarse en izquierda, derecha, arriba y abajo, por lo que podria representarse como:
```math
\begin{bmatrix}
0 & 1 & 2 & 3
\end{bmatrix}
```
donde:
- 0: izquierda
- 1: derecha
- 2: arriba
- 3: abajo
