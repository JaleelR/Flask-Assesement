from app import app 
from unittest import TestCase
class viewFunctionsTestCase(TestCase):

    def test_home(self):
        with app.test_client() as client:
         resp = client.get('/')
        html = resp.get_data(as_text=True)

        self.assertEqual(resp.status_code, 200)
        self.assertIn('\n<h1>Converter!</h1>\n', html)

    def test_uppercase(self):
        with app.test_client() as client:
            resp = client.post("/convert",
            data = {
               "from": "usd", 
               "to": "USD",
               "amount": "1200"
            })
        html = resp.get_data(as_text=True)
        self.assertEqual(resp.status_code, 302)
        
    
    def test_incorrect_currency_code(self):
        with app.test_client() as client:
            resp = client.post("/convert",
            data = {
               "from": "USD", 
               "to": "ZZZ",
               "amount": "1200"
            })
        html = resp.get_data(as_text=True)
        self.assertEqual(resp.status_code, 302)
      

    def test_redirection(self):
         with app.test_client() as client:
            resp = client.post("/convert")

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "http://localhost/")


    

