from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://the-internet.herokuapp.com/add_remove_elements/"


#Проверка наличия кнопки "AddElements"
def check_button():
    browser = webdriver.Chrome()
    browser.get(link)
    try:
        button = browser.find_element(By.TAG_NAME, "button")
    except:
        return False

    browser.quit()
    return bool(button)


#Добавление одного элемента
def add_one_element():
    browser = webdriver.Chrome()
    browser.get(link)
    try:
        button = browser.find_element(By.TAG_NAME, "button")
        button.click()
        added_elements = browser.find_elements(By.CLASS_NAME, "added-manually")
    except:
        return False

    browser.quit()
    return len(added_elements)


#Удаление одного элемента
def delete_one_element():
    browser = webdriver.Chrome()
    browser.get(link)
    try:
        button = browser.find_element(By.TAG_NAME, "button")
        button.click()
        added_element = browser.find_element(By.CLASS_NAME, "added-manually")
        added_element.click()
        deleted_elements = browser.find_elements(By.CLASS_NAME, "added-manually")
    except:
        return False

    browser.quit()
    return len(deleted_elements)


#Добавление 10ти элементов
def add_ten_elements():
    browser = webdriver.Chrome()
    browser.get(link)
    try:
        button = browser.find_element(By.TAG_NAME, "button")
        for _ in range(10):
            button.click()
        added_elements = browser.find_elements(By.CLASS_NAME, "added-manually")
    except:
        return False

    browser.quit()
    return len(added_elements)


#Удаление 10ти элементов
def delete_ten_elements():
    browser = webdriver.Chrome()
    browser.get(link)
    try:
        button = browser.find_element(By.TAG_NAME, "button")
        for _ in range(10):
            button.click()
        for _ in range(10):
            added_element = browser.find_element(By.CLASS_NAME, "added-manually")
            added_element.click()
        delete_element = browser.find_elements(By.CLASS_NAME, "added-manually")
    except:
        return False

    browser.quit()
    return len(delete_element)


#Добавление больше 10ти елементов
def add_more_elements():
    browser = webdriver.Chrome()
    browser.get(link)
    try:
        button = browser.find_element(By.TAG_NAME, "button")
        for _ in range(11):
            button.click()
        added_elements = browser.find_elements(By.CLASS_NAME, "added-manually")
    except:
        return False

    browser.quit()
    return len(added_elements)


def test_check_button():
    assert check_button()


def test_add_element():
    assert add_one_element() == 1


def test_delete_one_element():
    assert delete_one_element() == 0


def test_add_ten_elements():
    assert add_ten_elements() == 10


def test_delete_ten_elements():
    assert delete_ten_elements() == 0


def test_add_more_elements():
    assert add_more_elements() <= 10










