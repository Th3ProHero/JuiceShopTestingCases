import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common import RegistrationPage
from config import DRIVER_PATH

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        service = Service(DRIVER_PATH)
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://192.168.1.68:4000/#/register")
        self.registration_page = RegistrationPage(self.driver)

    def test_registration_success(self):
        selected_question = self.registration_page.register(
            email="newuser2@example.com",
            password="password123",
            confirm_password="password123",
            answer="John"
        )
        # Esperar hasta que el mensaje de bienvenida esté presente
        welcome_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-login/div/mat-card/h1"))
        )
        self.assertIsNotNone(welcome_message)
        print("Security question selected:", selected_question)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()