import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Фикстура для запуска и закрытия браузера
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_successful_login(driver):
    """Тест: Успешная авторизация на SauceDemo"""
    # 1. Открываем страницу
    driver.get("https://www.saucedemo.com/")
    
    # 2. Вводим логин и пароль
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    
    # 3. Нажимаем кнопку "Login"
    driver.find_element(By.ID, "login-button").click()
    
    # 4. Ждем, пока загрузится страница, и проверяем заголовок
    header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "title"))
    )
    assert header.text == "Products", "Не удалось войти в систему!"

def test_locked_out_user(driver):
    """Тест: Попытка входа заблокированного пользователя"""
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Проверяем, что появилось сообщение об ошибке
    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert "Sorry, this user has been locked out" in error_message.text
