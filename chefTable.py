import time
import datetime
import random
from random import randint
import tkinter as tk
from tkinter import *
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
import pyautogui


# Functions
def chef_table_fill_out():


    def phone_number_included():
        phone_number_1 = driver.find_element_by_id('phonenum-1').send_keys(random.choice(area_codes))
        phone_number_2 = driver.find_element_by_id('phonenum-2').send_keys(str(n.randint(100, 999)))
        phone_number_3 = driver.find_element_by_id('phonenum-3').send_keys(str(n.randint(1000, 9999)))



    # gonna make it work in both mac and pc
    chromedriver = r"/Users/jesus/Desktop/PythonPractice/driver/chromedriver 2"
    # chromedriver = r"C:\Users\Jesus\Desktop\python\driver\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver)

    # timeout if not loaded
    driver.set_page_load_timeout(30)

    driver.get("http://profile.benihana.com/registration/")

    # setting a wait time before inputting to make sure everything is loaded
    driver.implicitly_wait(30)

    area_codes = ["786", "305", "954", "754"]
    time = datetime.datetime.now()
    name_list = open("names.txt").read().splitlines()
    line = random.choice(name_list)
    name_regex = re.compile(r'(\w*),\s(\w*)')
    names = name_regex.search(line)

    # have it set to put the date the day after today
    bmonth = str(time.month)
    bday = str(time.day + 1)
    n = random.SystemRandom()

    house_number = str(n.randint(100, 9999))
    directions = ['E', 'N', 'W', 'S', 'SE','NE','SW','NW']
    street_number = str(n.randint(1, 190))
    street_type = ['AVE', 'BLVD', 'CT', 'PL', 'ST', 'TER', 'LN']

    address = house_number + " " + random.choice(directions) + " " + street_number + " " + random.choice(street_type)

    pyautogui.moveTo(1000, 150)
    pyautogui.click()
    f_name = driver.find_element_by_id('First_Nm').send_keys(str(names.group(2)))
    l_name = driver.find_element_by_id('Last_Nm').send_keys(str(names.group(1)))
    email_address = driver.find_element_by_id('Email_Address').send_keys(str(email_entry.get()))
    email_address_confirm = driver.find_element_by_id('Cnfm_Email_Address').send_keys(str(email_entry.get()))

    # Address
    address_line_1 = driver.find_element_by_id('AddressLine1').send_keys(address)
    address_line_2 = driver.find_element_by_id('AddressLine2').send_keys('')
    city = driver.find_element_by_id('City').send_keys('Miami')
    state = Select(driver.find_element_by_id('State')).select_by_value('FL')
    zip_code = driver.find_element_by_id('Zip').send_keys(str(n.randint(33101, 33299)))

    # Birthdate
    birthdate_month = Select(driver.find_element_by_id('bdaymonth')).select_by_value("0" + bmonth)
    birthdate_day = Select(driver.find_element_by_id('bdayday')).select_by_value(bday)
    birthdate_year = Select(driver.find_element_by_id('bdayyear')).select_by_value(str(n.randint(1979, 1999)))

    # always set to coral springs
    favorite_location = Select(driver.find_element_by_id('store_code')).select_by_value("1065")

    driver.find_element_by_xpath("//*[@id='chefRegi']/fieldset[2]/div/div[1]/label[3]/label/span").click()
    driver.find_element_by_xpath("//*[@id='chefRegi']/fieldset[2]/div/div[2]/span[2]/label/label/span").click()
    Select(driver.find_element_by_id('visitFreq')).select_by_value("1M")
    driver.find_element_by_xpath("//*[@id='favoriteDishesSortableList']/li[1]/label/label/span").click()
    driver.find_element_by_xpath("//*[@id='chefRegi']/fieldset[2]/div/div[5]/label[2]/label/span").click()
    driver.find_element_by_xpath("//*[@id='chefRegi']/fieldset[2]/div/div[6]/span[3]/label/label/span").click()
    driver.find_element_by_xpath("//*[@id='chefRegi']/fieldset[2]/div/div[7]/label[2]/label/span").click()



    # add option to include or not
    # need a button that can be turn on and off so that I can create a statement to
    # determine whether or not to run is pice of code

def display():

    # labels
    # f_name_label = tk.Label(text = "First Name: ").grid(column=0, row=0)
    # l_name_label = tk.Label(text = "Last Name: ").grid(column=0, row=1)
    email_label = tk.Label(text = "Email Address: ").grid(column=0, row=2)
    # address_label = tk.Label(text = "Address: ").grid(column=0, row=3)
    # city_label = tk.Label(text = "City: ").grid(column=0, row=4)
    # state_label = tk.Label(text = "State: ").grid(column=0, row=5)
    # zip_code_label = tk.Label(text = "Zip Code: ").grid(column=0, row=6)
    # birthdate_label = tk.Label(text = "Birthdate: (mm/dd/yyyy)").grid(column=0, row=7)
    # favorite_location_label = tk.Label(text = "Favorite Location: ").grid(column=0, row=8)
    # phone_number_label = tk.Label(text = "Phone Number: (###-###-####)").grid(column=0, row=9)

# create an organize list that will keep all information the user will input to be used to write to the website
user_input = []
States = [
"AK","AL","AR","AZ","CA","CO","CT","DC","DE","FL","GA","GU","HI","IA","ID", "IL","IN","KS","KY","LA","MA","MD","ME","MH","MI"
,"MN","MO","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY", "OH","OK","OR","PA","PR","PW","RI","SC","SD","TN","TX","UT","VA"
,"VI","VT","WA","WI","WV","WY"
]


# GUI
window = tk.Tk()
window.title("Chef's Table Filler")
window.geometry("400x400")

display()
#f_name_entry = tk.Entry()
#l_name_entry = tk.Entry()
email_entry = tk.Entry()
#address_entry = tk.Entry()
#city_entry = tk.Entry()
#state_entry = ttk.Combobox(window)
#state_entry["values"] = States
#state_entry.current(9)
#zip_code_entry = tk.Entry()
#birthdate_entry = tk.Entry()
#favorite_location_entry = tk.Entry()
#phone_number_entry = tk.Entry()
#f_name_entry.grid(column=1, row=0)
#l_name_entry.grid(column=1, row=1)
email_entry.grid(column=1, row=2)
#address_entry.grid(column=1, row=3)
#city_entry.grid(column=1, row=4)
#state_entry.grid(column=1, row=5)
#zip_code_entry.grid(column=1, row=6)
#birthdate_entry.grid(column=1, row=7)
#favorite_location_entry.grid(column=1, row=8)
#phone_number_entry.grid(column=1, row=9)


button = Button(window, command = chef_table_fill_out, text="OK").grid(column = 0, row = 10)

# can just pick the first option for the later section, but we should make it random


window.mainloop()


#chef_table_fill_out()

# how to get a screenshot
# driver.get_screenshot_as_file("ChefTableForm.png")
