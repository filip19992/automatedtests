from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

chrome_driver_path = '/path/to/chromedriver'

chrome_options = webdriver.ChromeOptions()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
chrome_options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

    message_input = driver.find_element(By.ID, "user-message")
    show_message_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='showInput();']")

    test_message = "Hello, Selenium!"
    message_input.send_keys(test_message)
    show_message_button.click()
    time.sleep(1)

    displayed_message = driver.find_element(By.ID, "display").text
    assert displayed_message == test_message, f"Expected message '{test_message}' but got '{displayed_message}'"
    print("Test 1 Passed: Message is displayed correctly")

    driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")

    checkbox = driver.find_element(By.ID, "isAgeSelected")
    checkbox.click()
    time.sleep(1)

    checkbox_message = driver.find_element(By.ID, "txtAge").text
    assert checkbox_message == "Success - Check box is checked", f"Expected message 'Success - Check box is checked' but got '{checkbox_message}'"
    print("Test 2 Passed: Checkbox is checked and message displayed")

    driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")

    male_radio = driver.find_element(By.CSS_SELECTOR, "input[value='Male'][name='optradio']")
    get_checked_value_button = driver.find_element(By.ID, "buttoncheck")

    male_radio.click()
    get_checked_value_button.click()
    time.sleep(1)

    radio_message = driver.find_element(By.CSS_SELECTOR, ".radiobutton").text
    assert radio_message == "Radio button 'Male' is checked", f"Expected message 'Radio button 'Male' is checked' but got '{radio_message}'"
    print("Test 3 Passed: Radio button 'Male' is checked and message displayed")

    driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")

    select_day = Select(driver.find_element(By.ID, "select-demo"))
    select_day.select_by_visible_text("Friday")
    time.sleep(1)

    selected_day_message = driver.find_element(By.CLASS_NAME, "selected-value").text
    assert selected_day_message == "Day selected :- Friday", f"Expected message 'Day selected :- Friday' but got '{selected_day_message}'"
    print("Test 4 Passed: Dropdown selection is displayed correctly")

    driver.get("https://www.seleniumeasy.com/test/input-form-demo.html")

    driver.find_element(By.NAME, "first_name").send_keys("John")
    driver.find_element(By.NAME, "last_name").send_keys("Doe")
    driver.find_element(By.NAME, "email").send_keys("john.doe@example.com")
    driver.find_element(By.NAME, "phone").send_keys("1234567890")
    driver.find_element(By.NAME, "address").send_keys("123 Main St")
    driver.find_element(By.NAME, "city").send_keys("Anytown")
    state_select = Select(driver.find_element(By.NAME, "state"))
    state_select.select_by_visible_text("California")
    driver.find_element(By.NAME, "zip").send_keys("12345")
    driver.find_element(By.NAME, "website").send_keys("http://example.com")
    driver.find_element(By.CSS_SELECTOR, "input[value='yes']").click()
    driver.find_element(By.NAME, "comment").send_keys("This is a test comment.")

    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    time.sleep(2)

    success_message = driver.find_element(By.CSS_SELECTOR, ".alert-success").text
    assert "Success" in success_message, f"Expected a success message but got '{success_message}'"
    print("Test 5 Passed: Form submission success message is displayed")

finally:
    # Close the browser
    driver.quit()
