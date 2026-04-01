import unittest
from app.app import app

class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_print_health_check(self):
        response = self.app.get('/health-check')
        self.assertEqual(200, response.status_code, "Erro no test_http_code!")
        self.assertEqual("<h1>Hello, I'm Alive!</h1>", response.get_data(as_text=True)
                          , "Erro no test_print_health_check!")

    def test_print_hello_success(self):
        response = self.app.get("/hello", query_string={"name": "Micael"})
        self.assertEqual(200, response.status_code, "Erro no test_print_hello_success!")
        self.assertEqual(f"Hello, Micael!", response.get_data(as_text=True), "Erro no test_print_hello_success!")

    def test_print_hello_error(self):
        response = self.app.get("/hello")
        self.assertEqual(400, response.status_code, "Erro no test_print_hello_error!")
        self.assertEqual("Nome não informado", response.get_data(as_text=True), "Erro no test_print_hello_success!")
