from django.test import TestCase
from .models import Url

class URLTests(TestCase):
    def test_testhomepage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_testencodepage(self):
        response = self.client.get("/encode")
        self.assertEqual(response.status_code, 200)

    def test_testdecodepage(self):
        response = self.client.get("/decode")
        self.assertEqual(response.status_code, 200)
    
class ModelTests(TestCase):
    def test_model_url1(self):
        url = Url.objects.create(original_url = "https://yello.co/resource/?_sft_resource_type=webinar", encoded_url = "http://short.est/1")
        self.assertEqual(str(url.original_url) , "https://yello.co/resource/?_sft_resource_type=webinar")
        self.assertEqual(str(url.encoded_url) , "http://short.est/1")
        
    def test_model_url2(self):
        url = Url.objects.create(original_url = "https://github.com/sganas360/yello_url_shortener", encoded_url = "http://short.est/2")
        self.assertEqual(str(url.original_url) , "https://github.com/sganas360/yello_url_shortener")
        self.assertEqual(str(url.encoded_url) , "http://short.est/2")
