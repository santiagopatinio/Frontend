from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from threading import Thread
load_dotenv()
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME") or "santiagopatio_WXSDwP"
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY") or "WCps4RqRzCBG44bjuVFE"
URL = os.environ.get("URL") or "https://hub.browserstack.com/wd/hub"
BUILD_NAME = "browserstack-build-1"
capabilities = [
    {
        "browserName": "Chrome",
        "browserVersion": "latest",
        "os": "Windows",
        "osVersion": "10",
        "sessionName": "BStack Python sample parallel", # test name
        "buildName": BUILD_NAME,  # Your tests will be organized within this build
    },
    {
        "browserName": "Firefox",
        "browserVersion": "latest",
        "os": "Windows",
        "osVersion": "11",
        "sessionName": "BStack Python sample parallel",
        "buildName": BUILD_NAME,
    },
    {
        "browserName": "Edge",
        "browserVersion": "latest",
        "os": "Windows",
        "osVersion": "7",
        "sessionName": "BStack Python sample parallel",
        "buildName": BUILD_NAME,
    },
]
def get_browser_option(browser):
    switcher = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions(),
        "edge": EdgeOptions(),
        "safari": SafariOptions(),
    }
    return switcher.get(browser, ChromeOptions())
def run_session(cap):
    bstack_options = {
        "osVersion" : cap["osVersion"],
        "buildName" : cap["buildName"],
        "sessionName" : cap["sessionName"],
        "userName": BROWSERSTACK_USERNAME,
        "accessKey": BROWSERSTACK_ACCESS_KEY
    }
    if "os" in cap:
      bstack_options["os"] = cap["os"]
    options = get_browser_option(cap["browserName"].lower())
    if "browserVersion" in cap:
      options.browser_version = cap["browserVersion"]
    options.set_capability('bstack:options', bstack_options)
    driver = webdriver.Remote(
        command_executor=URL,
        options=options)
    try:
        # Entra a la pagina
        driver.get("http://ise.onrender.com/login")

        # Ingresa email
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.ID, 'email'))).send_keys('profesor@gmail.com')

        # Ingresa password
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.ID, 'password'))).send_keys('123456789')

        # Ingresa ingresar
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.ID, 'ingresar'))).click()

        # Ingresa a matematica
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.ID, 'Matematica'))).click()

        # Ingresa a parciales
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.ID, 'botonParciales'))).click()

        # Crea una evaluacion
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.ID, 'crearEvaluacion'))).click()

        # Modifica una evaluacion una evaluacion
        #WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        #    (By.ID, 'inputNuevo'))).send_keys('Trabajo investigacion')

        # Elimminca una evaluacion
        #WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        #    (By.ID, 'eliminarEvaluacion'))).click()

    except NoSuchElementException:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some elements failed to load"}}')
    except Exception:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some exception occurred"}}')
    # Stop the driver
    driver.quit()
for cap in capabilities:
  Thread(target=run_session, args=(cap,)).start()