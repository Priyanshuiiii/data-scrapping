from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

# Set up the WebDriver
service = Service('path/to/chromedriver')  # Replace with your ChromeDriver path
driver = webdriver.Chrome(service=service)

# Open the Google Local Search results
driver.get('https://www.google.com/search?sca_esv=458dc05ad97e3dfc&tbm=lcl&q=electricians+in+los+angeles')

# Extract page content
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Scrape business listings
businesses = soup.find_all('div', class_='VkpGBb')  # Class name might need updating
for business in businesses:
    try:
        website = business.find('a', href=True)['href']
        print(website)
    except TypeError:
        continue

# Close the driver
driver.quit()
