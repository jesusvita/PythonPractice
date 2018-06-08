import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# declaring the chrome driver
chromedriver = r"C:\Users\Jesus\Desktop\python\driver\chromedriver.exe"

# creating a chrome driver
driver = webdriver.Chrome(chromedriver)

# timeout if not loaded
driver.set_page_load_timeout(30)

# website I want to get
driver.get("http://profile.benihana.com/registration/")

# how to get a screenshot
# driver.get_screenshot_as_file("ChefTableForm.png")

# setting a wait time
driver.implicitly_wait(30)

# get elements
f_name = driver.find_element_by_id('First_Nm').send_keys('Julian')
l_name = driver.find_element_by_id('Last_Nm').send_keys('Javier')
email_address = driver.find_element_by_id('Email_Address').send_keys('JulianJavier@gmail.com')
email_address_confirm = driver.find_element_by_id('Cnfm_Email_Address').send_keys('JulianJavier@gmail.com')
address_line_1 = driver.find_element_by_id('AddressLine1').send_keys('3261 SW 160th Ave')
address_line_2 = driver.find_element_by_id('AddressLine2').send_keys('')
city = driver.find_element_by_id('City').send_keys(' Miramar')
state = Select(driver.find_element_by_id('State')).select_by_value("FL")
zip_code = driver.find_element_by_id('Zip').send_keys('33027')
birthdate_month = Select(driver.find_element_by_id('bdaymonth')).select_by_value("07")
birthdate_day = Select(driver.find_element_by_id('bdayday')).select_by_value("7")
birthdate_year = Select(driver.find_element_by_id('bdayyear')).select_by_value("1990")
favorite_location = Select(driver.find_element_by_id('store_code')).select_by_value("1053")
phone_number_1 = driver.find_element_by_id('phonenum-1').send_keys('954')
phone_number_2 = driver.find_element_by_id('phonenum-2').send_keys('663')
phone_number_3 = driver.find_element_by_id('phonenum-3').send_keys('2294')
