from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://the-internet.herokuapp.com/dynamic_controls"


#Удаление checkbox
def delete_checkbox():
    browser = webdriver.Chrome()
    browser.get(link)
    try:
        result = None
        checkbox = browser.find_elements(By.ID, "checkbox")
        #Проверка наличия checkbox
        if len(checkbox) == 1:
            button = browser.find_element(By.XPATH, "//form/button")
            button.click()
            #Ожидание удаления checkbox
            time.sleep(5)
            deleted_checkbox = browser.find_elements(By.ID, "checkbox")
            #Проверка удаления checkbox
            if len(deleted_checkbox) == 0:
                result = True
            else:
                result = False
        else:
            return False
    except:
        return False

    browser.quit()
    return result


#Восстановление удаленного checkbox
def remove_checkbox():
    browser = webdriver.Chrome()
    browser.get(link)
    try:
        result = None
        button = browser.find_element(By.XPATH, "//form/button")
        button.click()
        # Ожидание удаления checkbox
        time.sleep(5)
        deleted_checkbox = browser.find_elements(By.ID, "checkbox")
        # Проверка удаления checkbox
        if len(deleted_checkbox) == 0:
            button_remove = browser.find_element(By.XPATH, "//form/button")
            button_remove.click()
            #Ожидание востановления checkbox
            time.sleep(5)
            removed_checkbox = browser.find_elements(By.ID, "checkbox")
            if len(removed_checkbox) == 1:
                result = True
            else:
                result = False
        else:
            result = False
    except:
        return False
    browser.quit()
    return result


def test_delete_checkbox():
    assert delete_checkbox()


def test_remove_checkbox():
    assert remove_checkbox()


