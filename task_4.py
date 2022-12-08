from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


#Получение пути до каталога
basedir = os.path.abspath(os.getcwd())
link = "http://the-internet.herokuapp.com/upload"


def upload_file():
    browser = webdriver.Chrome()
    browser.get(link)
    try:
        result = None
        browser.find_element(By.ID, "file-upload").send_keys(f"{basedir}/README.md")
        time.sleep(2)
        browser.find_element(By.ID, "file-submit").click()
        time.sleep(2)
        file_upload = browser.find_elements(By.ID, "uploaded-files")
        if len(file_upload) == 1:
            result = True
        else:
            result = False
    except:
        return False
    finally:
        browser.quit()
        
    return result


def test_upload_file():
    upload_file()
