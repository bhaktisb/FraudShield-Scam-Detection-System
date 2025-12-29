from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

def test_submit_audio_file():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000")

    # Upload a valid .wav file (make sure this file exists in your project directory)
    audio_path = os.path.abspath("test_audio.wav")
    audio_input = driver.find_element(By.NAME, "audio_file")
    audio_input.send_keys(audio_path)

    submit_button = driver.find_element(By.NAME, "submit")
    submit_button.click()

    time.sleep(3)

    # Check for Scam/Legit prediction
    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "Scam" in body_text or "Legit" in body_text

    driver.quit()
