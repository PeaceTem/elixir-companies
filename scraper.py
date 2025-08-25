from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

import pandas as pd

# # --- Setup Chrome ---
# options = Options()
# options.add_argument("--headless")  # Run in background
# options.add_argument("--disable-gpu")
# service = Service("/path/to/chromedriver")  # Change this to your chromedriver path
# driver = webdriver.Chrome(service=service, options=options)
print("Started!")
driver = webdriver.Edge()

url = "https://elixir-companies.com/en/companies"
driver.get(url)
print("Started Scraping!")

time.sleep(10)
# --- Infinite Scroll ---
last_height = driver.execute_script("return document.body.scrollHeight")
k=9
while k:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)  # wait for new content
    
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

    k -= 1

# --- Scrape Companies ---
companies = driver.find_elements(By.CSS_SELECTOR, ".company.box")
print(companies[0])
data = []
for company in companies:
    name = company.find_elements(By.CSS_SELECTOR, "p > a")[0].text.strip()
    company_type = ""
    link = ""
    github_link = ""
    location = company.find_elements(By.CSS_SELECTOR, "div.content.company-info > p")[0].text.strip()
    desc = company.find_elements(By.CSS_SELECTOR, "div.content.company-description > p")[0].text.strip()
    links = company.find_elements(By.CSS_SELECTOR, "div.content.company-info > p > a")
    if len(links) > 0:
        company_type = links[0].text.strip()

    if len(links) > 1:
        link = links[1].get_attribute("href")

    if len(links) > 2:
        github_link = links[2].get_attribute("href")
        

    data.append({"name": name, "company_type": company_type, "url": link, "github_url": github_link, "location": location, "description": desc})

# --- Show results ---
for c in data:
    print(c)

print(f"Total companies scraped: {len(data)}")
df = pd.DataFrame(data)
df.index = df.index + 1
df.index.name = 'ID'
# Save to CSV
df.to_csv("data/companies.csv")

# Save to Excel
df.to_excel("data/companies.xlsx")

time.sleep(10)
driver.quit()
#company-100starlings > div > div.content.company-info.has-text-left > p > a:nth-child(8)
#company-100starlings > div > div.content.company-info.has-text-left > p