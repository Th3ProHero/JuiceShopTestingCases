from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login")

    def enter_username(self, username: str):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password: str):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        
class RegistrationPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.email_input = (By.XPATH, "//*[@id='registration-form']/mat-form-field[1]/div/div[1]/div/input")
        self.password_input = (By.XPATH, "//*[@id='passwordControl']")
        self.confirm_password_input = (By.XPATH, "//*[@id='repeatPasswordControl']")
        self.security_question_listbox = (By.XPATH, "//*[@id='mat-select-0']/div/div[2]/div")
        self.answer_input = (By.XPATH, "//*[@id='securityAnswerControl']")
        self.register_button = (By.XPATH, "//*[@id='registerButton']")
        self.disclaimer_button_xpath = "//*[@id='mat-dialog-0']/app-welcome-banner/div/div[2]/button[2]"

    def close_disclaimer(self):
        # Esperar hasta que el botón del disclaimer esté presente y visible
        disclaimer_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.disclaimer_button_xpath))
        )
        # Hacer clic en el botón para cerrar el disclaimer
        disclaimer_button.click()

    def enter_email(self, email: str):
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_password(self, password: str):
        self.driver.find_element(*self.password_input).send_keys(password)

    def enter_confirm_password(self, confirm_password: str):
        self.driver.find_element(*self.confirm_password_input).send_keys(confirm_password)

    def select_random_security_question(self):
        # Hacer clic en el listbox para desplegar las opciones
        self.driver.find_element(*self.security_question_listbox).click()
        # Esperar hasta que todas las opciones del listbox estén presentes
        options = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//mat-option"))
        )
        # Seleccionar una opción aleatoria
        random_option = random.choice(options)
        # Usar JavaScript para hacer clic en la opción seleccionada
        self.driver.execute_script("arguments[0].click();", random_option)
        return random_option.text  # Devuelve el texto de la opción seleccionada

    def enter_answer(self, answer: str):
        self.driver.find_element(*self.answer_input).send_keys(answer)

    def click_register(self):
        self.driver.find_element(*self.register_button).click()

    def register(self, email: str, password: str, confirm_password: str, answer: str):
        self.close_disclaimer()
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        selected_question = self.select_random_security_question()
        self.enter_answer(answer)
        self.click_register()
        return selected_question
