# FASE 0

1. Se usaron convoluciones en ves de bucles dentro de bucles para mejorar rendimiento. Al hacer esto pasamos de 400seg a 2seg en que se termine de ejecutar
   todo el codigo (osea cuando toda la grilla esta incendiada). Esto pasa porque las convoluciones corren en C, no en python.

2. Se combinan las 8 direcciones usando la generalización de 1-(1-p)^n para probabilidades distintas: 1 - prod(1 - p_i). Cada p_i es la probabilidad
   de esa dirección específica, que varía según su alineación con el viento (ver decisión 4... o la que corresponda al viento). No es la fórmula con
   p y n iguales para las 8 direcciones, sino el producto de complementos con p_i distinto por dirección.

3. Se usa la convencion fila, columna. (osea, y,x) para mantener la consistencia con numpy.
