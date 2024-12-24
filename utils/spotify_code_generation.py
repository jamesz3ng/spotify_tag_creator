import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from PIL import Image
import vtracer

def generate_spotify_code(spotify_link, download_path = "spotify_code.png"):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options = options)

    driver.get("https://www.spotifycodes.com/#create")
    
    short_wait = WebDriverWait(driver, 5)
    standard_wait = WebDriverWait(driver, 15)

    # Click the cookie accept cookie button
    
    #try:
        # time.sleep(3)
        # accept_cookies_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    accept_cookies_button = standard_wait.until(EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler")))
    accept_cookies_button.click()

    # except:
    #     print("No cookies button found")

    spotify_link_input = standard_wait.until(EC.presence_of_element_located((By.ID, "playlist-code")))
    spotify_link_input.clear()
    spotify_link_input.send_keys(spotify_link)

    get_spotify_code_button = driver.find_element(By.CLASS_NAME, "l-btn")
    get_spotify_code_button.click()

    # Scroll until we reach required height to click acknowledgement "continue button"

    scroll_bar = driver.find_element(By.ID, "modal-content")
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", scroll_bar)


    # Check for continue button
    try:
        # continue_box = standard_wait.until(EC.presence_of_element_located((By.CLASS_NAME, "accept-button l-btn")))
        continue_box = standard_wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div/section/div[3]/div/div[3]/button")))
        continue_box.click()
        print(1)
    except:
        print("There is no continue box")

    # Download the spotify code
    try:
        time.sleep(4)
        download_box = standard_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#create > section > div.container > div > div > div.workshop__canvas > a')))
        image_url = download_box.get_attribute("href")
        print(image_url)
    except:
        print("Download box not found")

    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(download_path, "wb") as f:
            for chunk in response.iter_content(chunk_size = 8192):
                f.write(chunk)

    print("Image sucessfully generated")
    driver.quit()


def main():
    generate_spotify_code("https://open.spotify.com/track/6efJhdddUNkrpjl0NCzp2G?si=287f48c72a034737", "assets/spotify_code.png")


if __name__ == "__main__":
    main()