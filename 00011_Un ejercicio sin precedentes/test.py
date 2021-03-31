  
  def test_una_mujer_de_62_anios_con_40_anios_de_aportes_puede_jubilarse(self):
    self.assertTrue(puede_jubilarse(62, 'F', 40))
  
  
  def test_una_mujer_de_63_anios_con_25_anios_de_aportes_no_puede_jubilarse(self):
    self.assertFalse(puede_jubilarse(63, 'F', 25))
  
  
  def test_una_mujer_de_58_anios_con_35_anios_de_aportes_no_puede_jubilarse(self):
    self.assertFalse(puede_jubilarse(58, 'F', 35))
  
  
  def test_una_mujer_de_69_anios_con_40_anios_de_aportes_puede_jubilarse(self):
    self.assertTrue(puede_jubilarse(69, 'F', 40))
  
  
  def test_un_hombre_de_66_anios_con_40_anios_de_aportes_puede_jubilarse(self):
    self.assertTrue(puede_jubilarse(66, 'M', 40))
  
  
  def test_un_hombre_de_63_anios_con_35_anios_de_aportes_no_puede_jubilarse(self):
    self.assertFalse(puede_jubilarse(63, 'M', 35))
  
  
  def test_un_hombre_de_68_anios_con_26_anios_de_aportes_no_puede_jubilarse(self):
    self.assertFalse(puede_jubilarse(68, 'M', 26))
  
  
  def test_un_hombre_de_58_anios_con_35_anios_de_aportes_no_puede_jubilarse(self):
    self.assertFalse(puede_jubilarse(58, 'M', 35))
  
