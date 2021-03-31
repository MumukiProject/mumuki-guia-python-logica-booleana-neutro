  
  def test_es_necesario_que_filosofia_lleve_tilde_y_grecia_esté_en_mayusculas_para_saber_si_la_persona_es_peripatetica(self):
    self.assertFalse(es_peripatetica("filosofia", "Grecia", 3))
    self.assertTrue(es_peripatetica("filosofía", "Grecia", 3))
  
  def test_una_persona_que_se_desempena_en_filosofia_es_de_grecia_y_camina_3kms_al_dia_es_peripatetica(self):
    self.assertTrue(es_peripatetica("filosofia", "Grecia", 3) or es_peripatetica("filosofía", "Grecia", 3) or es_peripatetica("filosofía", "grecia", 3) or es_peripatetica("filosofia", "grecia", 3))
  
  def test_una_persona_que_se_desempena_en_filosofia_es_de_grecia_y_camina_2kms_al_dia_no_es_peripatetica(self):
    self.assertFalse((es_peripatetica("filosofia", "Grecia", 2) or es_peripatetica("filosofía", "Grecia", 2)))
  
  def test_una_persona_que_se_desempena_en_filosofia_es_de_argentina_y_camina_5kms_al_dia_no_es_peripatetica(self):
    self.assertFalse(es_peripatetica("filosofía", "Argentina", 5))
  
  def test_una_persona_que_se_desempena_en_atletismo_es_de_grecia_y_camina_10kms_al_dia_no_es_peripatetica(self):
    self.assertFalse(es_peripatetica("atleta", "Grecia", 10))
  
  def test_una_persona_que_se_desempena_en_ingenieria_es_de_colombia_y_camina_1kms_al_dia_no_es_peripatetica(self):
    self.assertFalse(es_peripatetica("profesor", "Colombia", 1))
  
