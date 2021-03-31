¿Y si delegamos? Podríamos separar la lógica de la siguiente manera:

```python
def puede_jubilarse(edad, sexo, anios_aportes):
  return cumple_edad_minima(edad, sexo) and tiene_suficientes_aportes(anios_aportes)
```

**Al delegar correctamente**, hay veces en las que no es necesario alterar el orden de precedencia, ¡otro punto a favor de la delegación! :muscle:
