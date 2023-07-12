from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.
#home test
class test_Home(SimpleTestCase):
    def test_status_code(self):
        url=reverse('home')
        response=self.client.get (url)
        self.assertEqual (response.status_code,200)
        
    def test_Template(self):
        url=reverse('home')
        response=self.client.get(url)
        self.assertTemplateUsed(response,'home.html')

#about -test

class Test_About(SimpleTestCase):
    def test_status_code(self):
        url=reverse('about')
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
    def test_Template(self):
        url=reverse('about')
        response=self.client.get(url)
        self.assertTemplateUsed(response,'about.html')


