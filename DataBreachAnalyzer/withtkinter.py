import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import time

# Function to check email compromise
def check_email_compromise(email):
    driver = None  # Initialize driver variable outside the try block
    # Setup Edge WebDriver options
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (optional)
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    # Path to Edge WebDriver (adjust if not in PATH)
    webdriver_path = "C:\\drivers\\msedgedriver.exe"  # Replace with your correct path
    service = Service(webdriver_path)

    try:
        # Initialize WebDriver
        driver = webdriver.Edge(service=service, options=options)

        # Navigate to 'Have I Been Pwned' website
        driver.get("https://haveibeenpwned.com/")

        # Locate the search box and enter the email address
        search_box = driver.find_element(By.ID, "Account")
        search_box.clear()
        search_box.send_keys(email)
        search_box.send_keys(Keys.RETURN)

        # Wait for results to load
        time.sleep(5)

        # Check the results on the page
        try:
            compromised = driver.find_element(By.XPATH, "//div[contains(@class, 'pwnedAccount')]")
            return "Your email has been compromised!"
        except NoSuchElementException:
            return "Good news! Your email appears to be safe."
    except WebDriverException as e:
        return f"Error interacting with the website: {e}"
    finally:
        # Clean up and close the browser, only if driver is initialized
        if driver:
            driver.quit()

# GUI callback function for checking email
def on_check_button_click():
    email = email_entry.get()  # Get the email from the input field
    if email:
        result = check_email_compromise(email)
        messagebox.showinfo("Result", result)  # Show result in a message box
    else:
        messagebox.showwarning("Input Error", "Please enter an email address.")

# Create the main window
window = tk.Tk()
window.title("Email Compromise Checker")

# Set window size and background color for a modern look
window.geometry("500x300")
window.config(bg="#2C3E50")  # Dark background

# Add a futuristic font and color theme
header_label = tk.Label(window, text="Email Compromise Checker", font=("Helvetica", 20, "bold"), fg="#ECF0F1", bg="#2C3E50")
header_label.pack(pady=20)

# Create the email label and entry field with modern design
email_label = tk.Label(window, text="Enter your email address:", font=("Helvetica", 14), fg="#ECF0F1", bg="#2C3E50")
email_label.pack(pady=10)

email_entry = tk.Entry(window, font=("Helvetica", 14), width=35, bd=0, relief="solid", highlightthickness=2, highlightbackground="#3498DB")
email_entry.pack(pady=10)

# Create the Check button with rounded edges and color styling
check_button = tk.Button(window, text="Check Email", command=on_check_button_click, font=("Helvetica", 14), fg="white", bg="#3498DB", bd=0, relief="solid", width=20, height=2)
check_button.pack(pady=20)

# Add a footer label to make the UI look complete
footer_label = tk.Label(window, text="Made By Raj Bhawsar 48 submitted to Nidhi Nigam Mam", font=("Helvetica", 10), fg="#BDC3C7", bg="#2C3E50")
footer_label.pack(side="bottom", pady=10)

# Run the Tkinter event loop
window.mainloop() 
