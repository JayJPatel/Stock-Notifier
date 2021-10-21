# Stock-Notifier

A script that helps get high-in-demand products in the hands of consumers by immediately notifying you via email when an item on Best Buy's site is in stock. Helps save you the time and stress of worrying when a product will be in stock for you to purchase it. Made with Python 3.9.6

## Installing & Running

1. Download Python 3.9.6 (or newer) from [here](https://www.python.org/downloads/)
2. Download the latest version of Google Chrome from [here](https://www.google.com/chrome/)
3. Download this project
   - The bundled webdriver works **only** with Google Chrome v94. If you're using a different version of Chrome, download the appropriate webdriver [here](https://chromedriver.chromium.org/downloads).
4. Run [setup.bat](setup.bat) to install any dependencies
5. Obtain an API key from [SendGrid](https://sendgrid.com/). This will be used to send a notification email once the script has detected that the product is in stock
   - You will need to create an account and verify your email for the api call to work
   - To acquire your api key, navigate to the settings tab once you've verified your email
   - (Optional) For cleaner email links, disable click tracking in SendGrid's settings > email tab
6. Edit settings in the [.env](.env) file
7. Start the bot by running start.bat **or** by typing the following in a terminal _(in this project's root directory)_:
   **`python main.py`**

## License and copyright

© 2021 Jay J Patel  
Licensed under the [Apache License](LICENSE)
