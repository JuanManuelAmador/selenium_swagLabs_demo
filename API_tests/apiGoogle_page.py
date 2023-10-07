import requests

class APIGoogle:
    
    
    def __init__(self, base_url):
        self.base_url = base_url

    def test(self):
        print("aaa")

    def get(self, endpoint, token="88261a35abmsh67987703acbda67p11de0ajsn74a321048bf5", encoding="application/gzip"):
        # implementation for GET request
        url = self.base_url + endpoint

        headers = {
        	"Accept-Encoding": encoding,
        	"X-RapidAPI-Key": token,
        	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)

        return response

    def post(self, endpoint, data):
        # implementation for POST request
        pass

    def put(self, endpoint, data):
        # implementation for PUT request
        pass

    def delete(self, endpoint):
        # implementation for DELETE request
        pass

if __name__ == '__main__':
    
    api = APIGoogle("https://google-translate1.p.rapidapi.com")
    #assert api.get("/language/translate/v2/languages").status_code == 200
    r = api.get("/language/translate/v2/languages",token="")
    print(r.json())
    print(r.status_code)
    
    r = api.get("/language/translate/v2/languages",token="aaaaaa")
    print(r.json())
    print(r.status_code)