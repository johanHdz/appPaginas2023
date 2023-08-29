from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class PruebasPaginaInicio(SimpleTestCase):
  def test_url_existe_ubicacion_correcta(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)
  
  def test_url_disponible_por_nombre(self):
    response = self.client.get(reverse('inicio'))
    self.assertEqual(response.status_code, 200)

  def test_plantilla_nombre_correcto(self):
    response = self.client.get(reverse('inicio'))
    self.assertTemplateUsed(response, 'inicio.html')

  def test_contenido_plantilla(self):
    response = self.client.get(reverse('inicio'))
    self.assertContains(response, '<h1>Página de inicio</h1>')

class PruebasPaginaAcercaDe(SimpleTestCase):
  def test_url_existe_ubicacion_actual(self):
    response = self.client.get('/acercade/')
    self.assertEqual(response.status_code, 200)
  
  def test_url_disponible_por_nombre(self):
    response = self.client.get(reverse('acercade'))
    self.assertEqual(response.status_code, 200)
  
  def test_url_plantilla_nombre_correcto(self):
    response = self.client.get(reverse('acercade'))
    self.assertTemplateUsed(response, 'acercade.html')
  
  def test_contenido_plantilla(self):
    response = self.client.get(reverse('acercade'))
    self.assertContains(response, '<h1>Acerca de...</h1>')
