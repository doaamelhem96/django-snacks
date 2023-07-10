from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.
#home test
class Test_Home(SimpleTestCase):
    def Test_status_code(self):
        url=reverse('home')
        response=self.client.get (url)
        self.assertEqual (response.status_code,200)
        
    def Test_Template(self):
        url=reverse('home')
        response=self.client.get(url)
        self.assertTemplateUsed(response,'home.html')

#about -test

class Test_About(SimpleTestCase):
    def Test_status_code(self):
        url=reverse('about')
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
    def Test_Template(self):
        url=reverse('about')
        response=self.client.get(url)
        self.assertTemplateUsed(response,'about.html')


