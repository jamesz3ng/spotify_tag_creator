import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def generate_spotify_code(spotify_link, download_path = "spotify_code.png"):
    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(options = options)

    driver.get("https://www.spotifycodes.com/#create")
    
    wait = WebDriverWait(driver, 15)

    spotify_link_input = wait.until(EC.presence_of_element_located((By.ID, "playlist-code")))

    spotify_link_input.clear()
    spotify_link_input.send_keys(spotify_link)

def main():
    generate_spotify_code(123132312)

if __name__ == "__main__":
    main()