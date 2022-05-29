from django.test import TestCase
from django.test import client
from challenge.models import DataTable
from django.core.files import File
from django.urls import reverse

# Create your tests here.

class DataTableTestCase(TestCase):
    def setUp(self):
        self.client = client.Client()
        self.data_object = DataTable.objects.create(data_file=File(open('./census_2009b.dms')))

    def testCrateView_success_upload(self):
        with open('./census_2009b.dms') as f:  
            data = {
                "data_file" : f
            }
            response = self.client.post('/upload/', data)
        self.assertEqual(response.status_code, 302)
    
    def testCrateView_wrong_file(self):
        with open('./manage.py') as f:  
            data = {
                "data_file" : f
            }
            response = self.client.post('/upload/', data, follow=True)
        message = list(response.context.get('messages'))[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(message.message, "File is invalid, check format or file structure")

    def testDetailView(self):
        response = self.client.get(f'/{self.data_object.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Object ID 1', response.content)