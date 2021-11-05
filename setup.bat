@ECHO Installing required packages for Stock-Notifier...

@ECHO Installing Selenium...
cmd /c "pip3 install selenium"

@ECHO Installing dotENV...
cmd /c "pip3 install python-dotenv"

@ECHO Installing Sendgrid...
cmd /c "pip3 install sendgrid"

@ECHO Installing undetected_chromedriver
cmd /c "pip3 install undetected_chromedriver"

@ECHO Process finished 
@pause