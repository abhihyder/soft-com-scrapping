from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import openpyxl
import argparse
# import gspread
# from google.oauth2.service_account import Credentials


# Clean up the URL to remove any trailing slashes
def clean_url(url):
    if url and url.endswith('/'):
        return url.rstrip('/')
    return url

def main():

    # Create the parser
    parser = argparse.ArgumentParser(description="Scrape company names and websites.")

    # Define the -s argument (optional search query)
    parser.add_argument("-s", "--search_query", type=str, help="The search query to use on Google Maps")

    # Parse the arguments
    args = parser.parse_args()

    search_query = args.search_query

    if not search_query:
        search_query = "Software company in dhaka"

    print(f"Searching for: {search_query}")

    # Google Sheets Setup
    # SHEET_NAME = "Your Google Sheet Name"
    # SERVICE_ACCOUNT_FILE = "your_service_account.json"

    # Authenticate with Google Sheets
    # scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    # creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scopes)
    # client = gspread.authorize(creds)
    # sheet = client.open(SHEET_NAME).sheet1

    # Excel Setup
    excel_file = "companies.xlsx"
    wb = openpyxl.Workbook()  # Create a new workbook
    ws = wb.active
    ws.append(["Company Name", "Website URL"])  # Add headers to the Excel sheet


    # Selenium Setup
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode
    driver = webdriver.Chrome(options=options)

    try:
        # Open Google Maps and search
        driver.get("https://www.google.com/maps")
        time.sleep(3)

        search_box = driver.find_element(By.ID, "searchboxinput")
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)

        # Select the feed element using role="feed" and class names
        feed_element = driver.find_element(By.CSS_SELECTOR, 'div[role="feed"].m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd')
        
        for _ in range(15):  # Adjust the number of scrolls
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", feed_element)
            time.sleep(3)


        # Extract Company Names and Websites
        companies = []
        company_elements = driver.find_elements(By.CSS_SELECTOR, ".Nv2PK")  # Adjust selector if needed
        print(f"Found {len(company_elements)} companies")

        for company in company_elements:
            try:
                name = company.find_element(By.CSS_SELECTOR, ".fontHeadlineSmall").text
                website_element = company.find_element(By.CSS_SELECTOR, ".S9kvJb")  # Website link
                website = website_element.get_attribute("href") if website_element else "N/A"

                # Add company only if a website is found
                if website:
                    website = clean_url(website)
                    companies.append([name, website])
            except Exception as e:
                print(f"Error processing company: {e}")
                continue

        # Store in Google Sheets
        # sheet.append_rows(companies)


        # Write to Excel
        for company in companies:
            ws.append(company)

        # Save the Excel file locally
        wb.save(excel_file)
        print(f"{len(companies)} companies saved to {excel_file}")

    finally:
        # Close the driver
        driver.quit()

if __name__ == "__main__":
    main()
