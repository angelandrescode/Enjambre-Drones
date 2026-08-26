# FASE 0

1. Se usaron convoluciones en ves de bucles dentro de bucles para mejorar rendimiento.
2. Se uso la formula 1-(1-p)^n. Esta formula da la probabilidad de que suceda un evento con probabilidad p que suceda en n intentos. Se puede interpretar como: P es la probabilidad de que un evento suceda y N el factor que usamos para que ese evento tenga mas probabilidad de suceder. En nuestro caso, p es la probabilidad base de que una celda se incendie, y n es la cantidad de vecinos, los cuales mientras mas haya mas aumenta la probabilidad de que una celda se incendie.
