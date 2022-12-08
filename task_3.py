from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://the-internet.herokuapp.com/login"


#Вход с валидными данными
def valid_login():
    browser = webdriver.Chrome()
    browser.get(link)
    try:
        result = None
        login = browser.find_element(By.XPATH, "//em[1]").text
        password = browser.find_element(By.XPATH, "//em[2]").text
        #Вставка логина в поле логина
        add_login = browser.find_element(By.ID, "username")
        add_login.send_keys(login)
        #Вставка пароля в поле пароля
        add_password = browser.find_element(By.ID, "password")
        add_password.send_keys(password)

        button = browser.find_element(By.TAG_NAME, "button")
        button.click()
        try:
            #Поиск сообщения об успешной регистрации
            suc_message = browser.find_element(By.CLASS_NAME, "success")
            if suc_message:
                result = True
            else:
                result = False
        except:
            return False
    except:
        return False
    finally:
        browser.quit()

    return result


#Вход с невалидными данными
def not_valid_login(login, password):
    browser = webdriver.Chrome()
    browser.get(link)
    try:
        result = None
        # Вставка логина в поле логина
        add_login = browser.find_element(By.ID, "username")
        add_login.send_keys(login)
        # Вставка пароля в поле пароля
        add_password = browser.find_element(By.ID, "password")
        add_password.send_keys(password)

        button = browser.find_element(By.TAG_NAME, "button")
        button.click()
        try:
            # Поиск сообщения об успешной регистрации
            message = browser.find_element(By.CLASS_NAME, "error")
            if message:
                result = True
            else:
                result = False
        except:
            return False
    except:
        return False
    finally:
        browser.quit()

    return result


def test_valid_login():
    valid_login()


#Тест при вводе только цифр
def test_not_valid_1():
    not_valid_login('111', '111')


#Тест при вводе русских букв
def test_not_valid_2():
    not_valid_login('йцукемв', 'йцукен')


#Тест при вводе латинских букв
def test_not_valid_3():
    not_valid_login('qwerty', 'qwerty')


#Тест при вводе символов
def test_not_valid_4():
    not_valid_login('!@#$%', '!@#$%')
