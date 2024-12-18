from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import time

def check_email_compromise(email):
    print("Initializing the WebDriver...")  # Debug print
    driver = None  # Initialize driver variable outside the try block to ensure it's always accessible
    # Setup Edge WebDriver options
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (optional)
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    # Path to Edge WebDriver (adjust if not in PATH)
    webdriver_path = "C:\\drivers\\msedgedriver.exe"  # Replace with the correct path
    service = Service(webdriver_path)

    try:
        print("Starting WebDriver...")  # Debug print
        # Initialize WebDriver
        driver = webdriver.Edge(service=service, options=options)

        # Navigate to 'Have I Been Pwned' website
        driver.get("https://haveibeenpwned.com/")
        print("Opened website...")  # Debug print

        # Locate the search box and enter the email address
        search_box = driver.find_element(By.ID, "Account")
        search_box.clear()
        search_box.send_keys(email)
        search_box.send_keys(Keys.RETURN)
        print(f"Searching for: {email}")  # Debug print

        # Wait for results to load
        time.sleep(5)

        # Check the results on the page
        try:
            compromised = driver.find_element(By.XPATH, "//div[contains(@class, 'pwnedAccount')]")
            print("Your email has been compromised! Details:")
            print(compromised.text)
        except NoSuchElementException:
            print("Good news! Your email appears to be safe.")
    except WebDriverException as e:
        print(f"Error interacting with the website: {e}")
    finally:
        # Clean up and close the browser, only if driver is initialized
        if driver:
            driver.quit()

if __name__ == "__main__":
    print("=== Email Compromise Checker ===")
    user_email = input("Enter your email address: ").strip()
    check_email_compromise(user_email)
