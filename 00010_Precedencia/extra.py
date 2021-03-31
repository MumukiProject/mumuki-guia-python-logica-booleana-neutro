def listo(): 
  pass

def cuotas(tarjeta):
  return {
    'visa': 6,
    'mastercard': 2,
  }.get(tarjeta, 1)

def paga_con_tarjeta(se_cobra_interes, tarjeta, efectivo_disponible):
  return not se_cobra_interes and cuotas(tarjeta) >= 3 or efectivo_disponible < 100

