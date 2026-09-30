# GENERAL

1. Creacion de features:
   1. Discusión y diseño con la IA
   2. Escribir el test primero
   3. Implementar feature hasta que pase el test
   4. Si aplica, se anotan cosas aquí
   5. Commit (Si es el ultimo commit de una fase, hacer tag)

# FASE 0

1. Se usaron convoluciones en ves de bucles dentro de bucles para mejorar rendimiento. Al hacer esto pasamos de 400seg a 2seg en que se termine de ejecutar
   todo el codigo (osea cuando toda la grilla esta incendiada). Esto pasa porque las convoluciones corren en C, no en python.

2. Se combinan las 8 direcciones usando la generalización de $1-(1-p)^n$ para probabilidades distintas: $1 - prod(1 - p_i)$. Cada $p_i$ es la probabilidad
   de esa dirección específica, que varía según su alineación con el viento (ver decisión 4... o la que corresponda al viento). No es la fórmula con
   p y n iguales para las 8 direcciones, sino el producto de complementos con p_i distinto por dirección.

3. Se usa la convencion fila, columna (osea, y,x) en la programación del simulador del incendio para mantener la consistencia con numpy.

4. Se decide que cada celda es equivalente a 1m

5. El fuego siempre se extendera, aunque todo vaya en contra (a excepción de si una celda no se puede encender, osea, que sea un combustible).
   La probabilidad minima que una celda puede tener si es un combustible es igual a la variable: `base_probability`
