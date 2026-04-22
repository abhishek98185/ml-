from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Path to ChromeDriver (download ChromeDriver for your Chrome version)
driver_path = "C:/path/to/chromedriver.exe"

# Function to automate the steps
def automate_website(url):
    # Open Chrome
    driver = webdriver.Chrome(executable_path=driver_path)
    
    # Open website
    driver.get(url)
    time.sleep(3)  # wait for page to load
    
    # Refresh the page
    driver.refresh()
    time.sleep(2)
    
    # Click anywhere (example: body element)
    driver.find_element(By.TAG_NAME, "body").click()
    time.sleep(2)
    
    # Close browser
    driver.quit()
    time.sleep(1)
    
    # Reopen and repeat
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get(url)
    time.sleep(3)
    
    # Click again
    driver.find_element(By.TAG_NAME, "body").click()
    time.sleep(2)
    
    # Close browser finally
    driver.quit()

# Use the function
automate_website("https://hackathonmanager.vercel.app/")
