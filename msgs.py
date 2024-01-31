from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time  # Import the time module

# Replace 'YourFriendName' with your friend's name as saved on WhatsApp
friend_name = "RTV ROX"

# Replace 'Your message' with the message you want to send
message = "HACKED"

# Number of times to send the message
num_messages = 10

# Delay between sending each message (in seconds)
delay_between_messages = 2  # Adjust this value as needed

# Path to the ChromeDriver executable (replace with your own path)
chromedriver_path = r"C:\Users\91812\PycharmProjects\pythonProject\wha\chromedriver_win32\chromedriver.exe"

# URL for WhatsApp Web
whatsapp_url = "https://web.whatsapp.com/"

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")  # Maximize the Chrome window

# Initialize Chrome WebDriver with updated options
driver = webdriver.Chrome(options=chrome_options)
driver.get(whatsapp_url)

# Wait for the user to scan the QR code and login
input("Scan the QR code and press Enter to continue...")

# Introduce a delay for initial page loading
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p'))
)

# Send friend's name to the search box
search_box = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
search_box.send_keys(friend_name)
search_box.send_keys(Keys.ENTER)

# Wait for the chat to load
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'))
)

# Send the message multiple times with delay
for i in range(num_messages):
    message_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)
    print(f"Message {i + 1} sent successfully!")
    time.sleep(delay_between_messages)  # Introduce delay

# Close the browser after sending the messages
driver.quit()
