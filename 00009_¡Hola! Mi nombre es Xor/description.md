Ahora cambiemos las funciones `tienen_la_misma_madre` y `tienen_el_mismo_padre` por proposiciones genéricas **A** y **B**. Además, representemos la operación que realiza `son_medio_hermanos` con el símbolo **⊻**. Lo que obtenemos es... ¡una nueva tabla! :tada:

<table class="table table-striped table-bordered table-condensed text-center">
  <tr>
    <th class ="text-center" style="width: 75px">A</th>
    <th class ="text-center" style="width: 75px">B</th>
    <th class ="text-center" style="width: 100px">A ⊻ B</th>
  </tr>
  <tr>
    <td>Verdadero</td>
    <td>Verdadero</td>
    <td>Falso</td>
  </tr>
  <tr>
    <td>Verdadero</td>
    <td>Falso</td>
    <td>Verdadero</td>
  </tr>
  <tr>
    <td>Falso</td>
    <td>Verdadero</td>
    <td>Verdadero</td>
  </tr>
  <tr>
    <td>Falso</td>
    <td>Falso</td>
    <td>Falso</td>
  </tr>
</table>

Este comportamiento existe como un operador dentro de la lógica y se lo denomina `xor` o disyunción lógica excluyente.

A diferencia del `and`, `or` y `not`, el `xor` no suele estar definido en los lenguajes. :cry: Sin embargo, ahora que sabés cómo funciona, si alguna vez lo necesitás podés definirlo a mano. :wink:

> Veamos si se entiende: definí la función genérica `xor`, que tome dos booleanos y devuelva el valor de verdad correspondiente.
