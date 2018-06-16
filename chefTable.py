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
def get_emails():
    email_list = open("emails.txt").read()
    emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-] +              # username
        @                               # a symbol
        [a-zA-Z0-9.-]  +               # domain name
        \.[a-zA-Z]{2,4}  # dot-somthing
        )''', re.X)

    return emailRegex.findall(email_list)

def get_random_name():
    name_list = open("names.txt").read().splitlines()
    random_line = random.choice(name_list)
    name_regex = re.compile(r'(\w*),\s(\w*)')
    return name_regex.search(random_line)

def get_random_address():
    house_number = str(n.randint(100, 9999))
    directions = ['E', 'N', 'W', 'S', 'SE','NE','SW','NW']
    street_number = str(n.randint(1, 190))
    street_type = ['AVE', 'BLVD', 'CT', 'PL', 'ST', 'TER', 'LN']

    return house_number + " " + random.choice(directions) + " " + street_number + " " + random.choice(street_type)

def get_driver(x):
    if x == 'w':
        return webdriver.Chrome(r"C:\Users\Jesus\Desktop\python\driver\chromedriver.exe")
    else:
        return webdriver.Chrome(r"/Users/jesus/Desktop/PythonPractice/driver/chromedriver 2")

def chef_table_fill_out(email):

    # The website has some kind of detection to prevent fasle account maybe even prevent botting
    # Luckily with this I can trick it to letting me make an account 100%
    def backspace():
        driver.find_element_by_id('Email_Address').send_keys(str(Keys.BACKSPACE))
        driver.find_element_by_id('Email_Address').send_keys(str(Keys.BACKSPACE))
        driver.find_element_by_id('Email_Address').send_keys(str(Keys.BACKSPACE))
        driver.find_element_by_id('Email_Address').send_keys(str(Keys.BACKSPACE))
        pyautogui.PAUSE = 1
        pyautogui.press('.')
        pyautogui.PAUSE = 1
        pyautogui.press('c')
        pyautogui.PAUSE = 1
        pyautogui.press('o')
        pyautogui.PAUSE = 1
        pyautogui.press('m')

    driver = get_driver('w')

    # timeout if not loaded
    driver.set_page_load_timeout(30)

    driver.get("http://profile.benihana.com/registration/")

    # setting a wait time before inputting to make sure everything is loaded
    driver.implicitly_wait(30)

    # Random name
    name = get_random_name()

    # Birthdate
    time = datetime.datetime.now()
    bmonth = str(time.month)
    bday = str(time.day + 1)

    # Random address
    address = get_random_address()

    f_name = driver.find_element_by_id('First_Nm').send_keys(str(name.group(2)))
    l_name = driver.find_element_by_id('Last_Nm').send_keys(str(name.group(1)))
    email_address = driver.find_element_by_id('Email_Address').send_keys(str(email))
    email_address_confirm = driver.find_element_by_id('Cnfm_Email_Address').send_keys(str(email))

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

    # Survey
    driver.find_element_by_xpath("//*[@id='chefRegi']/fieldset[2]/div/div[1]/label[3]/label/span").click()
    driver.find_element_by_xpath("//*[@id='chefRegi']/fieldset[2]/div/div[2]/span[2]/label/label/span").click()
    Select(driver.find_element_by_id('visitFreq')).select_by_value("1M")
    driver.find_element_by_xpath("//*[@id='favoriteDishesSortableList']/li[1]/label/label/span").click()
    driver.find_element_by_xpath("//*[@id='chefRegi']/fieldset[2]/div/div[5]/label[2]/label/span").click()
    driver.find_element_by_xpath("//*[@id='chefRegi']/fieldset[2]/div/div[6]/span[3]/label/label/span").click()
    driver.find_element_by_xpath("//*[@id='chefRegi']/fieldset[2]/div/div[7]/label[2]/label/span").click()

    # Anti-detection
    backspace()

    # Submit
    # driver.find_element_by_xpath("//*[@id='submit-btn']").click()

def run():
    emails = get_emails()
    for i in emails:
        chef_table_fill_out(i)

States = ["AK","AL","AR","AZ","CA","CO","CT","DC","DE","FL","GA","GU","HI","IA","ID", "IL","IN","KS","KY","LA","MA","MD","ME","MH","MI"
,"MN","MO","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY", "OH","OK","OR","PA","PR","PW","RI","SC","SD","TN","TX","UT","VA"
,"VI","VT","WA","WI","WV","WY"]
n = random.SystemRandom()

# GUI
window = tk.Tk()
window.title("Chef's Table Filler")
window.geometry("400x400")

button = Button(window, command = run, text="OK", width = 10, height = 4).grid(row=5, column=0)




window.mainloop()
