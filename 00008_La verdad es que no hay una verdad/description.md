Ahora pensemos cómo sería la tabla de verdad que representa el comportamiento de la función que acabás de hacer.

Las proposiciones serán `tienen_la_misma_madre` y `tienen_el_mismo_padre`, y los valores de verdad que porten dependerán de qué dos personas estén evaluando.

El booleano final resultará de operarlas mediante `son_medio_hermanos`:

<table class="table table-striped table-bordered table-condensed text-center">
  <tr>
    <th class ="text-center" style="padding: 5px 8px">tienen la misma madre</th>
    <th class ="text-center" style="padding: 5px 8px">tienen el mismo padre</th>
    <th class ="text-center" style="padding: 5px 8px">son medios hermanos</th>
  </tr>
  <tr>
    <td>True</td>
    <td>True</td>
    <td>False</td>
  </tr>
  <tr>
    <td>True</td>
    <td>False</td>
    <td>True</td>
  </tr>
  <tr>
    <td>False</td>
    <td>True</td>
    <td>True</td>
  </tr>
  <tr>
    <td>False</td>
    <td>False</td>
    <td>False</td>
  </tr>
</table>

> Probá tu función `son_medio_hermanos` con los siguientes valores y comprobá si se comporta como la tabla:
>
```python
ム son_medio_hermanos(aureliano_segundo, remedios)
ム son_medio_hermanos(aureliano_jose, remedios)
ム son_medio_hermanos(arcadio, aureliano_jose)
```