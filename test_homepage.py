from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest
import time


class Test_automationpractice:
    @pytest.fixture()
    def test_setup(self):
        #Drivers
        global driver
        caps = DesiredCapabilities.CHROME
        driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=caps)
        #Getting started
        driver.get('http://automationpractice.com/index.php')
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield
        # The end of test
        driver.close()
        driver.quit()


    def test_homepage(self, test_setup):
        #Phone number
        driver.find_element(By.CLASS_NAME, 'shop-phone')
        number = driver.find_element(By.XPATH, '//strong[contains(text(),"0123-456-789")]')
        assert number.text == '0123-456-789'
        print('Номер телефона корректен')

        #Contacts Page
        driver.find_element(By.ID, 'contact-link').click()
        assert driver.title == 'Contact us - My Store'
        driver.find_element(By.XPATH, '//div[@id="header_logo"]//a').click()
        print('Выполнен переход на страницу контактов')

        #Login Page
        driver.find_element(By.XPATH, '//a[@class="login"]').click()
        assert driver.title == 'Login - My Store'
        print('Выполнен переход на страницу входа')
        driver.find_element(By.XPATH, '//div[@id="header_logo"]//a').click()

        #homepage
        driver.find_element(By.XPATH, '//img[@class="logo img-responsive"]').click()
        assert driver.title == 'My Store'
        print('Выполнен переход на главную страницу')

        #Search
        driver.find_element(By.ID, 'search_query_top').clear()
        driver.find_element(By.ID, 'search_query_top').send_keys('test')
        time.sleep(2)
        driver.find_element(By.NAME, 'submit_search').click()
        assert driver.title == 'Search - My Store'
        print('Выполнен переход на страницу поиска')
        driver.find_element(By.XPATH, '//div[@id="header_logo"]//a').click()

        #Shopping cart
        driver.find_element(By.XPATH, '//b[contains(text(), "Cart")]').click()
        assert driver.title == 'Order - My Store'
        print('Выполнен переход в корзину')
        driver.find_element(By.XPATH, '//div[@id="header_logo"]//a').click()
        print('Тестирование главной страницы завершено')
        time.sleep(5)
