from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from difflib import SequenceMatcher
import requests
import os
import time

company = "AENA"

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

class PageGetter:
    driver = False
    def __init__(self, defaultBrowser='firefox'):
        if defaultBrowser == 'firefox':
            self.profile = webdriver.FirefoxProfile()
            self.profile.set_preference("browser.download.folderList", 2)
            self.profile.set_preference("browser.download.manager.showWhenStarting", False)
            self.profile.set_preference("browser.download.dir", os.path.dirname(os.path.realpath(__file__))+"/download-data/")
            self.profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip")

            self.driver = webdriver.Firefox(self.profile)
        elif defaultBrowser == 'chrome':
            self.driver = webdriver.Chrome()
        else:
            raise Exception('Not a valid browser')
    
    def getPage(self, url):
        if not self.driver:
            raise Exception("You should start a browser connection")
        self.driver.get(url)
        self.driver.find_element_by_id('lkDescarga').click()
        self.driver.find_element_by_id('wDescargas_rbTipoBusqueda_3').click()
        self.driver.find_element_by_name('wDescargas$drpEntidades').click()
        
        elem = self.driver.find_element_by_name('wDescargas$drpEntidades')

        for options in elem.find_elements_by_tag_name('option'):
            if similar(options.text, company) >= 0.8 or similar(options.get_attribute('value'), company) >= 0.8:
                options.click()
                break

        self.driver.find_element_by_id('wDescargas_btnBuscar').click()
        self.driver.find_element_by_xpath("//input[@id='wDescargas_Listado_btnDescargar']").click()
        
        while not os.path.isfile(os.path.dirname(os.path.realpath(__file__))+"/download-data/Informes.zip"):
            time.sleep(5)
        while os.path.isfile(os.path.dirname(os.path.realpath(__file__))+"/download-data/Informes.zip.part"):
            time.sleep(5)
        
    
    def close(self):
        self.driver.quit()


    

pg = PageGetter('firefox')
soup1 = pg.getPage("https://www.cnmv.es/ipps/default.aspx")


#soup2 = pg.getPage("https://www.ironhack.com/es/cursos/web-development-bootcamp")
pg.close()