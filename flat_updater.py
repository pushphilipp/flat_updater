from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random
import chromedriver_binary


config = {
    'login': {
        'username': 'kontakt@vdst-erlangen.de',  # Your email address
        'password': '1881-idvdstgw',  # Your password
    },
    'offer': {
        'id': '9981403',  # Your offer ID
        'interval': 10,  # Update interval in minutes
    },
}

screen = {
    'width': 640,
    'height': 480
}

def update_offer(interval):
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

update_offer(config['offer']['interval'])