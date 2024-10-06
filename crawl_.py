from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd

# Path to the ChromeDriver
chrome_driver_path = "D:\Crawl_test\chromedriver-win64\chromedriver.exe"

# Function to load more posts by clicking the "Load More" button
def click_load_more_button(driver):
    load_more_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div[1]/div[3]/div[2]/button')
    load_more_button.click()

# Function to scroll through the page to ensure all data is loaded
def scroll_through_page(driver, num_segments):
    for i in range(num_segments):
        scroll_position = i * (1 / num_segments)
        driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight * {scroll_position});")
        time.sleep(0.5)  # Adjusted sleep time for more efficiency

# Function to extract table data
def extract_table_data(driver):
    try:
        table = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div[1]/div[3]/div[1]/div[3]')
        thead = table.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div[1]/div[3]/div[1]/div[3]/div/table/thead')
        headers = [header.text for header in thead.find_elements(By.TAG_NAME, 'th')]

        tbody = table.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div[1]/div[3]/div[1]/div[3]/div/table/tbody')
        rows = tbody.find_elements(By.TAG_NAME, 'tr')
        table_data = [[cell.text for cell in row.find_elements(By.TAG_NAME, 'td')] for row in rows]

        return pd.DataFrame(table_data, columns=headers)
    
    except NoSuchElementException:
        print("Table not found")
        return pd.DataFrame()

# Main function to run the entire process
def scrape_coinmarketcap_historical(url, output_csv, num_scroll_segments=4500):
    driver = webdriver.Chrome(chrome_driver_path)
    driver.get(url)
    time.sleep(5)
    
    while True:
        try:
            click_load_more_button(driver)
            time.sleep(1)
        except:
            break
            
    scroll_through_page(driver, num_scroll_segments)
    
    df = extract_table_data(driver)
    df = df.iloc[:, :-1]  # Remove the last column if necessary

    df.to_csv(output_csv, index=False)
    driver.close()

# Execution block
if __name__ == "__main__":
    # Parameters
    url = 'https://coinmarketcap.com/historical/20210627/'
    output_csv = '20210627.csv'
    
    # Run the scraper
    scrape_coinmarketcap_historical(url, output_csv)
