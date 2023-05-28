# Trabajo Práctico 2: Problema de Empaquetamiento

## Integrantes

- 105774 - Nicolas Zulaica - nzulaica@fi.uba.ar
- 104007 - Lautaro Barrionuevo - lebarrionuevo@fi.uba.ar

## Definición del problema

Dado un conjunto de n objetos cuyos tamaños son {T1, T2, · · · , Tn}, con Ti ∈ (0, 1], se debe empaquetarlos usando la mínima cantidad de envases de capacidad 1.
## Ejecucion

```bash
python3 .\tdatp.py E|A|A2 <items_file>
```

> Ejemplo: `python3 .\tdatp.py E .\data\items_10.txt`


## Demostracion que el problema de empaquetamiento es NP-Completo

Para demostrar que un problema es NP-Completo primero debemos demostrar que ese mismo problema sea NP. Es decir, que haya una solución que podamos revisarla en tiempo polinomial.

En nuestro caso podemos ver que la validación del problema es lineal ya que se puede recorrer el conjunto e ir revisando los paquetes para ver que las sumas no se pasan de 1 en ninguno de ellos.

Luego debemos poder reducir otro problema NP-Completo a este. Vamos a utilizar el problema de la mochila.

Si tenemos que cada objeto va a tener un mismo peso y valor correspondiente entre (0;1] y se irán agregando en mochilas con capacidad de 1 para usar la minima cantidad de mochilas, podemos reducir el problema al de empaquetamiento.

## Implementaciones

El codigo de las implementaciones puede encontrarse en el archivo `packing.py`

### Implentacion Exacta (E)

Complejidad: `O(N!)`
> Evalua la heuristica A para cada permutacion de los elementos.

### Implentacion Aproximada Propuesta (A)

Complejidad: `O(N)`
> Itera los elementos, agregandolos al ultimo envase si este tiene espacio, o creando uno nuevo en caso contrario.

Aproximacion: `2`
> En el peor de los casos tendremos elementos con el siguiente formato: [m,M,m,M,...,m,M], 
> donde hay 2N elementos, m+M > 1 y m*N < 1.
> - la heuristica propuesta creara 2N envases (uno con cada elemento)
> - la solucion optima creara N (uno por cada elemento M y uno con todos los m)

### Implentacion Aproximada Propia (A2)

Complejidad: `O(N^2)`
> Mientras haya elementos, los itera intentando agregarlos al envase actual, si no entra ninguno crea un nuevo envase.

Aproximacion: `3/2`
> En el peor de los casos, se conforma un paquete utilizando 2 elementos mas pequeños que podrian haberse emparejado con elementos mas grandes que ahora ocupan un paquete individualmente
>
> Eg: [0.5, 0.4, 0.5, 0.6] -> [ [0.5, 0.4], [0.5], [0.6] ] ( podemos pensar en estos elementos como agrupaciones de elementos mas pequeños )


### Comparacion

TODO
