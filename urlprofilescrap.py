import os
import time
from Config import *
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path

from selenium.common.exceptions import NoSuchElementException

# code for options, service, etc.
svc = Service(executable_path=binary_path)
options = Options()
options.add_argument('start-maximized')
options.add_experimental_option("excludeSwitches", ['enable-automation'])
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

# # Your LinkedIn credentials if used directly without a config page
# USERNAME = "your_username"
# PASSWORD = "your_password"

# Chrome web driver code:
driver = webdriver.Chrome(service=svc, options=options)
driver.get("https://www.linkedin.com/search/results/people/?geoUrn=%5B%22106164952%22%5D&keywords=%22%22CIO%22%22&origin=FACETED_SEARCH&sid=opq")
driver.maximize_window()
driver.implicitly_wait(40)
time.sleep(2)

# Log in code
Join = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/p/a")
Join.click()
Username = driver.find_element(By.ID, "username")
Username.click()
Username.send_keys(USERNAME)  # Replace with your external login
Password = driver.find_element(By.ID, "password")
Password.click()
Password.send_keys(PASSWORD)
Join = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[3]/button")
Join.click()

# Data storage
data = {'Contact Person': [], 'Designation': [], 'City': [], 'LinkedIn URL': []}

# code to scrape contact person, designation, city, and LinkedIn URL
for d in range(20):
    for i in range(1, 11):
        try:
            contact_person_xpath = f'/html/body/div[4]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li[{i}]/div/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]'
            designation_xpath = f'/html/body/div[4]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li[{i}]/div/div/div/div[2]/div[1]/div[2]'
            city_xpath = f'/html/body/div[4]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li[{i}]/div/div/div/div[2]/div[1]/div[3]'
            linkedin_url_xpath = f'/html/body/div[4]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li[{i}]/div/div/div/div[1]/div/a'

            contact_person = driver.find_element(By.XPATH, contact_person_xpath).text
            designation = driver.find_element(By.XPATH, designation_xpath).text
            city = driver.find_element(By.XPATH, city_xpath).text
            linkedin_url = driver.find_element(By.XPATH, linkedin_url_xpath).get_attribute('href')

            data['Contact Person'].append(contact_person)
            data['Designation'].append(designation)
            data['City'].append(city)
            data['LinkedIn URL'].append(linkedin_url)

            print(f"Contact Person: {contact_person}\nDesignation: {designation}\nCity: {city}\nLinkedIn URL: {linkedin_url}\n---")

        except NoSuchElementException as e:
            print(f'Error Occurred: {e}')


    try:
        join = driver.find_element(By.CSS_SELECTOR, ".artdeco-pagination__button.artdeco-pagination__button--next.artdeco-button.artdeco-button--muted.artdeco-button--icon-right.artdeco-button--1.artdeco-button--tertiary.ember-view")
        join.click()
        time.sleep(2)  # Add a short delay to allow the page to load before scraping again
    except NoSuchElementException:
        print("Next button not found")

# Save data to CSV
df = pd.DataFrame(data)
df.to_csv('linkedin_results.csv', index=False)

# Close the driver when done
driver.quit()