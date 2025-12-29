from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_submit_text_only():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000")

    # Find the text input field and submit
    text_input = driver.find_element(By.NAME, "text_input")
    text_input.send_keys("You've won a prize!")

    submit_button = driver.find_element(By.NAME, "submit")
    submit_button.click()

    time.sleep(3)  # Wait for the response

    # Check if result contains "Scam" or "Legit"
    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "Scam" in body_text or "Legit" in body_text

    driver.quit()
