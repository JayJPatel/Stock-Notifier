import os
import time 
from bot import BOT
from dotenv import load_dotenv
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from sendgrid import SendGridAPIClient 
from sendgrid.helpers.mail import Mail 

load_dotenv()

#---------------------------------------------------------------------------
# Constants

URL = os.getenv("BSTBUY_PRODUCT_URL")
API_KEY = os.getenv("API_KEY")
TO_EMAIL = os.getenv("TO_EMAIL")
FROM_EMAIL = os.getenv("FROM_EMAIL")
REFRESH_TIMER = int(os.getenv("page_refresh_timer"))

# Webdriver Setup 
WD_PATH = os.getcwd() + "\\chromedriver.exe"
opt = Options()
opt.add_argument("--log-level=3") # Webdriver: Only log critical errors
#opt.add_argument("headless") 

#---------------------------------------------------------------------------
# CSS Selectors used in BSTBUY_BOT

SKU = "data-sku-id"
ADD_TO_CART = "add-to-cart-button"
ATC_STATE = "data-button-state"
PRODUCT_TITLE = "v-fw-regular"
#---------------------------------------------------------------------------
# CLASS - BSTBUY_BOT

class BSTBUY_BOT(BOT) : 
    # Constructor
    def __init__(self) : 
        self.driver = webdriver.Chrome(WD_PATH, options=opt)

    # Open browser & grab SKU 
    def startup(self) : 
        self.driver.get(URL)
        print("Opening Best Buy browser...")
        time.sleep(1)
        self.sku = self.driver.find_element_by_class_name(ADD_TO_CART).get_attribute(SKU)
        return

    # Checks if product is in stock
    def check_in_stock(self) :
        while(True) : 
            self.driver.refresh()
            time.sleep(1)
            if self.driver.find_element_by_class_name(ADD_TO_CART): 
                text = self.driver.find_element_by_class_name(ADD_TO_CART).get_attribute(ATC_STATE) 
                if (text == "SOLD_OUT") : 
                    print("Product not in stock")
                else : 
                    print("Product in stock!!! Sending email...")
                    return
            time.sleep(REFRESH_TIMER)
        
    # Generates Instant ATC Link 
    def makeIATCLink(self) : 
        IATC_Link = ("https://api.bestbuy.com/click/-/" + self.sku + "/cart/")
        return IATC_Link

    # Grabs product name 
    def grabProductName(self) : 
        PRODUCT_NAME = self.driver.find_element_by_class_name(PRODUCT_TITLE).text
        return PRODUCT_NAME

    # Generates email that the product is in stock
    def generate_email_contents(self) : 
        # Body of email 
        plainText = ('Stock_Notifier has detected that the product:\n' + self.grabProductName() +
                    '\nis now in stock!\n\nInstant Add To Cart Link: ' + self.makeIATCLink() + 
                    '\n\nProduct Link: ' + URL + '\n\n') 

        # Email content
        message = Mail(from_email=FROM_EMAIL, 
                        to_emails=TO_EMAIL,
                        subject='STOCK NOTIFIER: ITEM IN STOCK', 
                        plain_text_content=plainText)
        return message 

    # Sends email that product is in stock 
    def send_email(self) : 
        message = self.generate_email_contents() 
        try : 
            sndgrid = SendGridAPIClient(API_KEY)
            response = sndgrid.send(message)
            # print(response.status_code)
            # print(response.body) 
            # print(response.headers)
        except Exception as err:
            print(err) 
        
    # Exit webdriver session
    def close(self) : 
        self.driver.quit()
        return 
