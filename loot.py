import time
import requests
import os
import warnings
import random
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

email='mmater343@gmail.com'
password='xonB23Y5#'
url = "https://discord.com/api/webhooks/1037869989748813876/DN1NWSkRVCzz_hAgA7W7487kcHmPUkPYVOCqtFF5FOMt0eUStBFln1MFB_ZgXrmjIal8"
random_videos=['https://loot.tv/video/671788','https://loot.tv/video/671973', 'https://loot.tv/video/671838', 'https://loot.tv/video/671716','https://loot.tv/video/671965','https://loot.tv/video/672037','https://loot.tv/video/672420']

#email = input('Email: ')
#password = input('Password: ')

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
    else:
        driver = webdriver.Chrome(os.path.abspath("chromedriver"),options=chrome_options)
        chrome_options.add_argument('--no-sandbox')
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
    driver.get(random.choice(random_videos))
    print('Started watching '+driver.current_url)
    images=1
    screenshot_image='screenshot'+str(images)+'.png'
    driver.save_screenshot('screenshot{0}.png'.format(images))
    # posts 1st screenshot
    files = { "file" : (screenshot_image, open(screenshot_image, 'rb')) }
    result = requests.post(url, files=files)
    # time flag is 0
    time_flag=0
    while True:
        # if the time on the same URL >= 15 minutes
        if time_flag >= 30: # 30 = 30 x 20 seconds = 600 seconds = 10 minutes
            driver.get(random.choice(random_videos))
            
            images+=1
            screenshot_image='screenshot'+str(images)+'.png'
            driver.save_screenshot('screenshot{0}.png'.format(images))
            url = "https://discord.com/api/webhooks/1037869989748813876/DN1NWSkRVCzz_hAgA7W7487kcHmPUkPYVOCqtFF5FOMt0eUStBFln1MFB_ZgXrmjIal8"
            files = { "file" : (screenshot_image, open(screenshot_image, 'rb')) }
            result = requests.post(url, files=files)
    
            print('Switched video because of delay')
            time_flag=0
            
        url=driver.current_url
        time.sleep(20)
        # if the url is not the same url
        if driver.current_url != url:
            print("Switched to video: "+driver.current_url)
            images+=1
            driver.save_screenshot('screenshot{0}.png'.format(images))
            screenshot_image='screenshot'+str(images)+'.png'
            files = { "file" : (screenshot_image, open(screenshot_image, 'rb')) }
            url = "https://discord.com/api/webhooks/1037869989748813876/DN1NWSkRVCzz_hAgA7W7487kcHmPUkPYVOCqtFF5FOMt0eUStBFln1MFB_ZgXrmjIal8"
            result = requests.post(url, files=files)
        # if the URl stays the same (20 seconds have passed and URL is still the same)
        else:
            time_flag+=1
            pass
        


    
