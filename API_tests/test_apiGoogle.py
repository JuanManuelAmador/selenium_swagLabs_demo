import unittest
from apiGoogle_page import APIGoogle


import requests
import unittest
from apiGoogle_page import APIGoogle

class TestapiGoogle(unittest.TestCase):
    
    def setUp(self):
        self.api = APIGoogle("https://google-translate1.p.rapidapi.com")

    def test_get_connection(self):
        print("Test connection")
        endpoint = "/language/translate/v2/languages"
        r = self.api.get(endpoint)
        if r.status_code == 200:
            print("Connection successful")
        else:
            print("Connection failed")
            
    def test_get_response(self):
        print("Test response")
        endpoint = "/language/translate/v2/languages"
        r = self.api.get(endpoint)
        if r.status_code == 200:
            print("Response successful")
        else:
            print("Response failed")
            
    def test_get_InvalidApiKey(self):
        print("Test bad token")
        endpoint = "/language/translate/v2/languages"
        r = self.api.get(endpoint, token="")
        assert r.status_code == 401
        assert r.json()["message"] == "Invalid API key. Go to https://docs.rapidapi.com/docs/keys for more info."
        
            
    def test_get_NotSuscribedToApi(self):
        print("Test not suscribed token")
        endpoint = "/language/translate/v2/languages"
        r = self.api.get(endpoint, token="aaaaa")
        assert r.status_code == 403
        assert r.json()["message"] == "You are not subscribed to this API."
        
    def test_get_OptionalParamEmpty(self):
        print("Test empty optional param")
        endpoint = "/language/translate/v2/languages"
        r = self.api.get(endpoint, encoding="")
        assert r.status_code == 200
        
            
    def tearDown(self):
        #print("Cleanup of test environment")
        self.api = None
        
if __name__ == '__main__':
    unittest.main()
