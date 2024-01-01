import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# Path to your Chrome webdriver executable
webdriver_path = 'path/to/chromedriver'

# Path to your Excel file containing the seller information
excel_file_path = 'path/to/seller_info.xlsx'

# Load the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Start the Chrome browser
driver = webdriver.Chrome(webdriver_path)

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    store_link = row['Store Link']
    
    # Visit the store's URL
    driver.get(store_link)
    time.sleep(2)  # Wait for the page to load
    
    try:
        # Find the message button and click on it
        message_button = driver.find_element_by_xpath("//button[contains(text(), 'Message')]")
        message_button.click()
        time.sleep(2)  # Wait for the message dialog to open
        
        try:
            # Find the message input field and clear any existing text
            message_input = driver.find_element_by_xpath("//textarea[@id='message-to-seller']")
            message_input.clear()
            
            # Replace the template message with your desired message
            message = "Hello, I am interested in your products. Can you please provide more information?"
            
            # Type the message into the input field
            message_input.send_keys(message)
            
            # Send the message by pressing Enter
            message_input.send_keys(Keys.RETURN)
            
            time.sleep(2)  # Wait for the message to be sent
            
            print(f"Message sent to {store_link}")
        except NoSuchElementException:
            print(f"Message input field not found for {store_link}. Skipping...")
    except NoSuchElementException:
        print(f"Message button not found for {store_link}. Skipping...")
    except Exception as e:
        print(f"Error sending message to {store_link}: {str(e)}")

# Close the browser
driver.quit()
