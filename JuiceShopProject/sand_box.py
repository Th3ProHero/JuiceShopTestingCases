from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# Ruta al ejecutable del WebDriver
DRIVER_PATH = "D:\\Work\\PythonSelenium\\drivers\\chromedriver-win64\\chromedriver.exe"  # Asegúrate de especificar el archivo ejecutable

# Crear una instancia del Service
service = Service(DRIVER_PATH)

# Inicializar el WebDriver con el Service
driver = webdriver.Chrome(service=service)

try:
    # Abrir la URL de registro
    driver.get("http://192.168.1.68:4000/#/register")

    # Esperar hasta que el botón de bienvenida esté presente y visible
    welcome_banner_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='mat-dialog-0']/app-welcome-banner/div/div[2]/button[2]"))
    )

    # Hacer clic en el botón de bienvenida
    welcome_banner_button.click()

    # Esperar unos segundos para que el banner desaparezca (puedes ajustar este tiempo)
    time.sleep(2)

    # Esperar hasta que el elemento del listbox esté presente y visible
    listbox_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='mat-select-0']/div/div[2]/div"))
    )

    # Hacer clic en el elemento del listbox para desplegar las opciones
    listbox_element.click()

    # Esperar hasta que todas las opciones del listbox estén presentes
    options = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//mat-option"))
    )

    # Seleccionar una opción aleatoria
    random_option = random.choice(options)
    random_option.click()

    # Mantener el navegador abierto por unos segundos para observar cualquier cambio
    time.sleep(5)

except Exception as e:
    print("Error:", str(e))

finally:
    # Cerrar el navegador
    driver.quit()
