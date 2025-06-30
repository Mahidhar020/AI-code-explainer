
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# CONFIGURATION
chrome_driver_path = "C:/WebDrivers/chromedriver.exe"  # 👉 Update to your path
website_url = "http://localhost:8501"  # 👉 Or your deployed Streamlit app URL

# SETUP
options = Options()
options.add_argument("--headless")  # Run in background
options.add_argument("--window-size=1366,768")

# CREATE DRIVER
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# LOAD WEBPAGE
driver.get(website_url)
time.sleep(3)  # Wait for app to fully load

# TAKE FIRST SCREENSHOT
driver.save_screenshot("dashboard_top.png")
print("✅ Saved: dashboard_top.png")

# SCROLL AND TAKE SECOND SCREENSHOT
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)
driver.save_screenshot("dashboard_bottom.png")
print("✅ Saved: dashboard_bottom.png")

# CLEANUP
driver.quit()
