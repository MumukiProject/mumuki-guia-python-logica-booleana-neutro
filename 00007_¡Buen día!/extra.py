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

juan_perez = {
  'nombre': "Juan Perez"
}

maria_rodriguez = {
  'nombre': "Maria Rodriguez"
}

dora_ramirez = {
  'nombre': "Dora Ramirez"
}

felipe_perez = {
  'nombre': "Felipe Perez",
  'madre': maria_rodriguez,
  'padre': juan_perez
}

martin_perez = {
  'nombre': "Martín Perez",
  'madre': dora_ramirez,
  'padre': juan_perez
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

