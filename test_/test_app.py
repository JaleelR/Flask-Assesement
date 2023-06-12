from app import app 
from unittest import TestCase
class viewFunctionsTestCase(TestCase):
    def test_home(self):
        with app.test_client as client:
         resp = client.get('/')
        html = resp.get_data(as_text=True)

        self.assertEqual(resp.status_code, 200)
        self.assertIn('<h1> Converting </h1> ', html)

    def test_converter(self):
        with app.test_client() as client:
            resp = client.post("/convert",
            data = {
               "from": "USD", 
            })
        html = resp.get_data(as_text=True)
        self.assertEqual(resp.status_code, 200)
        self.assertIn("Converting USD", html)

    
    def test_redirection(self):
         with app.test_client() as client:
            resp = client.get("/convert")

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "http://localhost/")


            