# Trabajo Práctico 2: Problema de Empaquetamiento

## Integrantes

- 105774 - Nicolas Zulaica - nzulaica@fi.uba.ar
- 104007 - Lautaro Barrionuevo - lebarrionuevo@fi.uba.ar

## Definición del problema

Dado un conjunto de n objetos cuyos tamaños son {T1, T2, · · · , Tn}, con Ti ∈ (0, 1], se debe empaquetarlos usando la mínima cantidad de envases de capacidad 1.
## Ejecucion

TODO

## Demostracion que el problema de empaquetamiento es NP-Completo

Para demostrar que un problema es NP-Completo primero debemos demostrar que ese mismo problema sea NP. Es decir, que haya una solución que podamos revisarla en tiempo polinomial.

En nuestro caso podemos ver que la validación del problema es lineal ya que se puede recorrer el conjunto e ir armando paquetes sin pasarse de 1 entre la suma de cada objeto.

Luego debemos poder reducir otro problema NP-Completo a este. Vamos a utilizar el problema de la mochila.

Si tenemos que cada objeto va a tener un mismo peso y valor correspondiente entre (0;1] y se irán agregando en mochilas con capacidad de 1 para usar la minima cantidad de mochilas, podemos reducir el problema al de empaquetamiento.

## Implementaciones

## Implentacion Exacta (E)

TODO
## Implentacion Aproximada Propuesta (A1)

TODO

## Implentacion Aproximada Propia (A2)

TODO

## Comparacion

TODO
