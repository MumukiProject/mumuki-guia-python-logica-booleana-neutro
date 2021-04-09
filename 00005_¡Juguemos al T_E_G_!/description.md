¿Y si basta con que una de varias condiciones se cumpla para afirmar que una expresión es verdadera? Podemos utilizar otro de los operadores que ya conoces, ¡la disyunción lógica `or`! :bulb:

En el juego T.E.G., un jugador puede ganar de dos formas: cumpliendo su objetivo secreto o alcanzando el objetivo general de conquistar 30 países:

```python
def gano(cumplio_objetivo_secreto, cantidad_de_paises_conquistados):
  return cumplio_objetivo_secreto or cantidad_de_paises_conquistados >= 30

```

> Prueba en la consola las siguientes expresiones:
>
``` python
ム gano(True, 25)
ム gano(False, 30)
ム gano(False, 20)
ム gano(True, 31)
```

> ¿Te animas a construir la tabla de verdad de la disyunción lógica?
