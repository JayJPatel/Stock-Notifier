from bstbuy import BSTBUY_BOT
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC 
from dotenv import load_dotenv

load_dotenv() 

try: 
    tool = BSTBUY_BOT()
except WebDriverException as err: 
    print(err)
    print("\nPlease download the appropriate webdriver version for your current version of Chrome/Chromium\
        @\nhttps://sites.google.com/a/chromium.org/chromedriver/downloads")
    exit()

tool.startup()

try :  
    tool.check_in_stock() 
    tool.send_email()
    tool.close()

except Exception as err: 
    print(err)
    tool.close()
    