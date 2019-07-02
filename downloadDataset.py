# No partimos con un dataset de kaagle. En cambio, descargamos uno scrapeando la página web de la CNMV.
# Este código utiliza Selenium para descargar unos archivos zip con la información que buscamos.

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from difflib import SequenceMatcher
import os
import time

# Es una pequeña función para buscar similiridad entre la query del usuario y las opciones de un select de la página.
# No es lo más correcto, porque puede dar fallos. Debería hacer un listado con las 35 empresas eligiendo el <option> que queremos.
# Por ahorro de tiempo lo he hecho así, pero, seguramente, con algunas empresas fallará. Por ejemplo, hay varias <option> del Banco Santander.
# Seguramente con este último, los datos no serían los correctos.
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Se crea el driver para Selenium
class PageGetter:
    driver = False
    def __init__(self, defaultBrowser='firefox'):
        if defaultBrowser == 'firefox':
            # Se configura un perfil con una carpeta de descarga para Selenium
            self.profile = webdriver.FirefoxProfile()
            self.profile.set_preference("browser.download.folderList", 2)
            self.profile.set_preference("browser.download.manager.showWhenStarting", False)
            # Carpeta destino:
            self.profile.set_preference("browser.download.dir", os.path.dirname(os.path.realpath(__file__))+"/download-data/")
            # Se le dice a Selenium que no pregunte cuando se descarge .zips
            self.profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip")

            self.driver = webdriver.Firefox(self.profile)
        elif defaultBrowser == 'chrome':
            self.driver = webdriver.Chrome()
        else:
            raise Exception('Not a valid browser')
    
    # La función getPage recorre los elementos de la página de la CNMV y va pinchando en donde nos interesa.
    # He puesto algunos time.sleep() porque cuando la conexión es lenta, Selenium hace click antes de que el elemento se cargue y pueda haber error.

    def getPage(self, url, query):
        if not self.driver:
            raise Exception("You should start a browser connection")
        print ("Scrapeando la web de la CNMV...")
        self.driver.get(url)
        self.driver.find_element_by_id('lkDescarga').click()
        time.sleep(2)
        self.driver.find_element_by_id('wDescargas_rbTipoBusqueda_3').click()
        time.sleep(3)
        self.driver.find_element_by_name('wDescargas$drpEntidades').click()
        
        elem = self.driver.find_element_by_name('wDescargas$drpEntidades')

        for options in elem.find_elements_by_tag_name('option'):
            if similar(options.text, query) >= 0.8 or similar(options.get_attribute('value'), query) >= 0.8:
                options.click()
                break
        else:
            raise ValueError("La compañía no ha sido encontrada")

        self.driver.find_element_by_id('wDescargas_btnBuscar').click()
        time.sleep(3)
        # Empieza la descarga
        self.driver.find_element_by_xpath("//input[@id='wDescargas_Listado_btnDescargar']").click()
        
        print ("Comenzando descarga...")
        # Mientras que no aparezca el archivo .zip en nuestra carpeta, Selenium sigue abierto
        while not os.path.isfile(os.path.dirname(os.path.realpath(__file__))+"/download-data/Informes.zip"):
            time.sleep(5)
        # Mientras que la descarga está activa, aparece un archivo con .part. Cuando finaliza la descarga, este archivo desaparece.
        # Hasta que este archivo no desaparezca, Selenium sigue abierto. De esta forma nos aseguramos la descarga del archivo.
        while os.path.isfile(os.path.dirname(os.path.realpath(__file__))+"/download-data/Informes.zip.part"):
            time.sleep(5)
    
    def close(self):
        self.driver.quit()