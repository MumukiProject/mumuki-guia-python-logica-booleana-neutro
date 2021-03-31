En la lógica booleana, se puede definir el comportamiento de un operador con una _tabla de verdad_ donde **A** y **B** son las expresiones o valores de verdad a ser operados y el símbolo **^** representa la conjunción.

<table class="table table-striped table-bordered table-condensed text-center">
  <tr>
    <th class ="text-center" style="width: 75px">A</th>
    <th class ="text-center" style="width: 75px">B</th>
    <th class ="text-center" style="width: 100px">A ^ B</th>
  </tr>
  <tr>
    <td>Verdadero</td>
    <td>Verdadero</td>
    <td>Verdadero</td>
  </tr>
  <tr>
    <td>Verdadero</td>
    <td>Falso</td>
    <td>Falso</td>
  </tr>
  <tr>
    <td>Falso</td>
    <td>Verdadero</td>
    <td>Falso</td>
  </tr>
  <tr>
    <td>Falso</td>
    <td>Falso</td>
    <td>Falso</td>
  </tr>
</table>

En el mundo de la lógica estas expresiones se llaman _proposiciones_. Pero… ¿qué cosas pueden ser una proposición? :thought_balloon: Sólo hace falta que tengan un valor de verdad, es decir, cualquier expresión booleana puede ser una proposición.

> Para comprobarlo, probá en la consola tu función `es_peripatetica` con los siguientes valores y comprobá si se comporta como en la tabla:
>
> ```python
ム es_peripatetica("atletismo", "Argentina", 10)
ム es_peripatetica("filosofía", "Argentina", 3)
ム es_peripatetica("ingeniería", "Canadá", 1)
ム es_peripatetica("filosofía", "Grecia", 5)
```

