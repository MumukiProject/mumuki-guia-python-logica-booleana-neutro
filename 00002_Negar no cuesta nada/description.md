Empecemos por algo sencillo, ¿te acordás del operador `not` ? Se lo denomina negación o complemento lógico y sirve para negar un valor booleano. Si tengo el booleano representado por `tiene_hambre`, el complemento será `not tiene_hambre`. :no_mouth:

No parece una idea muy interesante pero puede servir para reutilizar la lógica de una función que ya tenemos definida.

Por ejemplo, si contamos con una función `es_par`, basta con negarla para saber si un número es impar.

```python
def es_impar(numero):
  return not es_par(numero)

```

> ¡Ahora te toca a vos! Definí la función `es_mayor_de_edad` y luego `es_menor_de_edad` a partir de ella.
