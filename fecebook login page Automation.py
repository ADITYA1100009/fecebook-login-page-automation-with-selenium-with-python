from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
def open_facebook():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Optional

    # Automatically install and setup ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open Facebook   
    driver.get("https://www.facebook.com")
    #wait for the page to load
    time.sleep(2)
    #enter the email and password
    driver.find_element(By.ID,"email").send_keys("aadityabhardwaj053@gmail.con") # type: ignore
    driver.find_element(By.ID,"pass").send_keys("aadi0000") # type: ignore

    #click the login button
    driver.find_element(By.NAME,"login").click()  # type: ignore

    # Optional delay to view the page
    time.sleep(5)

    # Keep browser open or return driver
    #return driver

# Example usage
if __name__ == "__main__":
    open_facebook()
