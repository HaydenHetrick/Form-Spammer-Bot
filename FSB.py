from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome('C:\Users\Hetrick_Hayden\Desktop\chromedriver_win32\chromedriver.exe')

# Navigate to the Google Form
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdgSLozEfmb5gKE8d_hyxBVRiXpvuFFUXdTVlPOVuRLfDxySg/viewform')

# Get the start time
start_time = time.time()

# Loop to vote 1000 times
for i in range(1000):
    # Find the multiple-choice question and select an option
    question = driver.find_element(By.XPATH, '//*[@id="i1"]/span[1]')
    option = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div/div/div/div[2]/div/div/span/div/div[6]/label/div/div[2]/div/span')
    option.click()

    # Submit the form
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')
    submit_button.click()

    # Reload the form
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdgSLozEfmb5gKE8d_hyxBVRiXpvuFFUXdTVlPOVuRLfDxySg/viewform')

    # Get the current time
    current_time = time.time()

    # Calculate the elapsed time
    elapsed_time = current_time - start_time

    # If less than 60 seconds have passed, sleep for a while
    if elapsed_time < 60:
        time.sleep(60 - elapsed_time)

    # Reset the start time
    start_time = time.time()

# Close the browser
driver.quit()