from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_display_and_change_units():
    # Set up the Chrome browser
    driver = webdriver.Chrome()

    # Navigate to your app
    driver.get("https://solvedex-solution.vercel.app")

    # Find the input field and enter a test value
    input_field = driver.find_element(By.CLASS_NAME, "input")
    input_field.send_keys("New York")
    input_field.send_keys(Keys.RETURN)
    time.sleep(2)  # Wait for a second to see the changes

    # Wait until the label associated with the unit toggle switch is clickable and then click it
    wait = WebDriverWait(driver, 10)  # wait for up to 10 seconds
    unit_toggle_label = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='unitToggle']")))
    unit_toggle_label.click()
    time.sleep(5)
    unit_toggle_label.click()
    time.sleep(10)  # Wait for a second to see the changes

    # You can add assertions here to check if the units have changed as expected

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    test_display_and_change_units()
