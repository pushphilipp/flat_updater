from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import os
import time
import random



# Load configuration from external JSON file located next to this script.
CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.json")
with open(CONFIG_FILE, "r") as fh:
    config = json.load(fh)

screen = {
    'width': 640,
    'height': 480
}

def update_offer():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size={},{}'.format(screen['width'], screen['height']))
    driver = webdriver.Chrome(options=chrome_options)
    
    driver.get("http://www.wg-gesucht.de")
    
    try:
        driver.find_element(By.ID, "cmpbntyestxt").click()
    except:
        print("No cookie banner found")
    
    try:
        driver.execute_script("""
            document.getElementById("login_email_username").value = arguments[0];
            document.getElementById("login_password").value = arguments[1];
            document.getElementById("login_submit").click();
        """, config['login']['username'], config['login']['password'])
    except:
        print("Login failed")
    
    time.sleep(5)
    print("Login successful!")
    
    driver.get("https://www.wg-gesucht.de/angebot-bearbeiten.html?action=update_offer&offer_id=" + config['offer']['id'])
    
    time.sleep(5)
    print("WG-Gesucht ad loaded!")
    
    #Create random time shift between 0 and 120 seconds
    random_time_shift = random.randint(0, 120)
    time.sleep(random_time_shift)

    driver.execute_script("""
        document.getElementById("update_offer_nav").click();
    """)
    print("Ad last updated on: " + time.strftime("%c", time.localtime()))

    driver.quit()


def main():
    """Continuously update the offer at the configured interval."""
    while True:
        update_offer()
        wait_minutes = config['offer']['interval']
        print(f"Waiting {wait_minutes} minutes for next update...")
        time.sleep(wait_minutes * 60)


if __name__ == "__main__":
    main()
