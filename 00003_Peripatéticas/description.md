Otro de los operadores con el que ya te encontraste es la conjunción lógica (también llamada _and_), que sólo retorna verdadero cuando las dos expresiones que opera son verdaderas.

Podemos encadenar varias de ellas mediante el operador `and` y si alguna es falsa toda la expresión resultará falsa.

Por ejemplo, si cuento con la función...

```python
 def es_cantante_prolifico(cds_editados, recitales_realizados, grabo_algun_dvd):
  return cds_editados >= 10 and recitales_realizados > 25 and grabo_algun_dvd
```

...basta con que un cantante no haya grabado un DVD para no ser considerado prolífico, incluso aunque haya editado más de 10 CDs y dado más de 25 recitales. :guitar:

> Definí una función `es_peripatetica` que tome el área en que se desempeña una persona, su país de origen y la cantidad de kilómetros que camina por día. Una persona es petipatética cuando se desempeña en filosofía, su país de origen es Grecia y le gusta pasear (camina más de 2 kilómetros por día). Ejemplo:
>
> ```python
> ム es_peripatetica("filosofía", "Grecia", 5)
True
> ム es_peripatetica("ingeniería", "Uruguay", 1)
False
> ```
