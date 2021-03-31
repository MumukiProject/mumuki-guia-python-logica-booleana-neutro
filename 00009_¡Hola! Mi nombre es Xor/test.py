  
  def test_la_disyuncion_logica_excluyente_entre_True_y_True_da_False(self):
    self.assertFalse(xor(True, True))
  
  
  def test_la_disyuncion_logica_excluyente_entre_True_y_False_da_True(self):
    self.assertTrue(xor(True, False))
  
  
  def test_la_disyuncion_logica_excluyente_entre_False_y_True_da_True(self):
    self.assertTrue(xor(False, True))
  
  
  def test_la_disyuncion_logica_excluyente_entre_False_y_False_da_False(self):
    self.assertFalse(xor(False, False))
  
