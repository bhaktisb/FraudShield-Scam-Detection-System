from selenium import webdriver
from selenium.webdriver.common.by import By

def test_homepage_loads():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000")
    
    assert "FraudShield" in driver.title
    
    driver.quit()
