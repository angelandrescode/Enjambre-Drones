# FASE 0

1. Se usaron convoluciones en ves de bucles dentro de bucles para mejorar rendimiento. Al hacer esto pasamos de 400seg a 2seg en que se termine de ejecutar todo el codigo (osea cuando toda la grilla esta incendiada)
2. Se uso la formula 1-(1-p)^n. Esta formula da la probabilidad de que suceda un evento con probabilidad p que suceda en n intentos. Se puede interpretar como: P es la probabilidad de que un evento suceda y N el factor que usamos para que ese evento tenga mas probabilidad de suceder. En nuestro caso, p es la probabilidad base de que una celda se incendie, y n es la cantidad de vecinos, los cuales mientras mas haya mas aumenta la probabilidad de que una celda se incendie.
3. Se usan 8 convoluciones por direccion para tener la capacidad de comparar cada dirección con el viento y sacar una probabilidad total entre si con la formula de antes (1-(1-p)^n) pero ahora n es un numero fijo, que es 8.
4. Se usa la convencion fila, columna. (osea, y,x) para mantener la consistencia con numpy.
