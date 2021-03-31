¿Descifraste la precedencia de las operaciones booleanas? :thinking: Por las dudas acá tenemos un cuadro con la precedencia de ellas y de algunas operaciones que vimos (y otras que no):


<table class="table table-striped table-bordered table-condensed text-center">
  <tr>
    <th class ="text-center" style="width: 10px">Prioridad</th>
    <th class ="text-center" style="width: 75px">Operaciones</th>
    <th class ="text-center" style="width: 75px">Descripción</th>
  </tr>
  <tr>
    <td>1</td>
    <td>**</td>
    <td>Exponenciación</td>
  </tr>
  <tr>
    <td>2</td>
    <td>*,  /,  %</td>
    <td>Multiplicación, división, resto</td>
  </tr>
  <tr>
    <td>3</td>
    <td>+,  -</td>
    <td>Suma, resta</td>
  </tr>
  <tr>
    <td>4</td>
    <td>in,  <,  <=,  >,  >=,  ==,  !=</td>
    <td>Pertenencia, comparaciones</td>
  </tr>
  <tr>
    <td>5</td>
    <td>not</td>
    <td>Negación lógica</td>
  </tr>
  <tr>
    <td>6</td>
    <td>and</td>
    <td>Conjunción lógica</td>
  </tr>
  <tr>
    <td>7</td>
    <td>or</td>
    <td>Disyunción lógica</td>
  </tr>
</table>

En esta tabla la precedencia va de mayor a menor, es decir, la prioridad 1 es la mayor y la prioridad 7 es la menor. Por ejemplo, si hacemos...

``` python
8 + 2 * 3 < 15 and not 5 == 4
```

... obtendremos `True` ya que resuelve las operaciones en este orden:

1. `2 * 3` que retorna `6` entonces: `8 + 6 < 15 and not 5 == 4`
2. `8 + 6` que retorna `14` entonces: `14 < 15 and not 5 == 4`
3. `14 < 15` que retorna `True` entonces: `True and not 5 == 4`
4. `5 == 4` que retorna `False` entonces: `True and not False`
5. `not False` que retorna `True` entonces: `True and True`
6. `True and True` que finalmente retorna `True`.