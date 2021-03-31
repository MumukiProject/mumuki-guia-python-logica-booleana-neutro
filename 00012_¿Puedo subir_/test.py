  
  def test_una_persona_que_mide_1_5m_no_esta_acompaniada_por_un_adulto_y_no_tiene_afecciones_cardiacas_puede_subirse_a_la_atraccion(self):
    self.assertTrue(puede_subirse(1.5, False, False))
  
  def test_una_persona_que_mide_1_7m_no_esta_acompaniada_por_un_adulto_y_tiene_afecciones_cardiacas_no_puede_subirse_a_la_atraccion(self):
    self.assertFalse(puede_subirse(1.7, False, True))
  
  def test_una_persona_que_mide_1_2m_esta_acompaniada_por_un_adulto_y_no_tiene_afecciones_cardiacas_puede_subirse_a_la_atraccion(self):
    self.assertTrue(puede_subirse(1.2, True, False))
  
  def test_una_persona_que_mide_1_2m_no_esta_acompaniada_por_un_adulto_y_no_tiene_afecciones_cardiacas_no_puede_subirse_a_la_atraccion(self):
    self.assertFalse(puede_subirse(1.2, False, False))
  
  def test_una_persona_que_mide_1_1m_esta_acompaniada_por_un_adulto_y_no_tiene_afecciones_cardiacas_no_puede_subirse_a_la_atraccion(self):
    self.assertFalse(puede_subirse(1.1, True, False))
  
