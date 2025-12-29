from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_submit_empty_input():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000")

    # Submit without any input
    submit_button = driver.find_element(By.NAME, "submit")
    submit_button.click()
    
    time.sleep(2)

    # Check if proper message is shown
    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "Not Provided" in body_text or "Please enter input" in body_text

    driver.quit()
