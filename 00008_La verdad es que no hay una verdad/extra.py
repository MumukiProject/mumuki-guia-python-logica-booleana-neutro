maria_de_los_remedios = {
  'nombre': "María De Los Remedios"
}

pedro_ternera = {
  'nombre': "Pedro Ternera"
}

sofia_montiel = {
  'nombre': "Sofía Montiel"
}

arturo_de_la_piedad = {
  'nombre': "Arturo De La Piedad"
}

pilar_ternera = {
  'nombre': "Pilar Ternera",
  'madre': maria_de_los_remedios,
  'padre': pedro_ternera
}

ursula_iguaran = {
  'nombre': "Úrsula Iguarán"
}

jose_arcadio_padre = {
  'nombre': "José Arcadio"
}

jose_arcadio = {
  'nombre': "José Arcadio",
  'madre': ursula_iguaran,
  'padre': jose_arcadio_padre
}

coronel_aureliano = {
  'nombre': "Coronel Aureliano",
  'madre': ursula_iguaran,
  'padre': jose_arcadio_padre
}

sofia_de_la_piedad = {
  'nombre': "Sofía De La Piedad",
  'madre': sofia_montiel,
  'padre': arturo_de_la_piedad
}

arcadio = {
  'nombre': "Arcadio",
  'madre': pilar_ternera,
  'padre': jose_arcadio
}

aureliano_jose = {
  'nombre': "Arcadio",
  'madre': pilar_ternera,
  'padre': coronel_aureliano
}

aureliano_segundo = {
  'nombre': "Aureliano Segundo",
  'madre': sofia_de_la_piedad,
  'padre': arcadio
}

remedios = {
  'nombre': "Remedios",
  'madre': sofia_de_la_piedad,
  'padre': arcadio
}

def madre_de(persona):
  return persona['madre']['nombre']


def padre_de(persona):
  return persona['padre']['nombre']

def tienen_el_mismo_padre(una, otra):
  return padre_de(una) == padre_de(otra)


def tienen_la_misma_madre(una, otra):
  return madre_de(una) == madre_de(otra)


def son_medio_hermanos(una, otra):
  return tienen_la_misma_madre(una, otra) and not tienen_el_mismo_padre(una, otra) or not tienen_la_misma_madre(una, otra) and tienen_el_mismo_padre(una, otra)

