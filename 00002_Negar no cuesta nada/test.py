  
  def test_alguien_de_20_anios_es_mayor_de_edad(self):
    self.assertTrue(es_mayor_de_edad(20))
  
  
  def test_alguien_de_18_anios_es_mayor_de_edad(self):
    self.assertTrue(es_mayor_de_edad(18))
  
  
  def test_alguien_de_17_anios_no_es_mayor_de_edad(self):
    self.assertFalse(es_mayor_de_edad(17))
  
  
  def test_alguien_de_16_anios_no_es_mayor_de_edad(self):
    self.assertFalse(es_mayor_de_edad(16))
  
  
  def test_alguien_de_20_anios_no_es_menor_de_edad(self):
    self.assertFalse(es_menor_de_edad(20))
  
  
  def test_alguien_de_18_anios_no_es_menor_de_edad(self):
    self.assertFalse(es_menor_de_edad(18))
  
  
  def test_alguien_de_17_anios_es_menor_de_edad(self):
    self.assertTrue(es_menor_de_edad(17))
  
  
  def test_alguien_de_16_anios_es_menor_de_edad(self):
    self.assertTrue(es_menor_de_edad(16))
  
