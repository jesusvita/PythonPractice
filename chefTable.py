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
def get_email(name):
    return name.group(2) + name.group(1) + str(n.randint(1, 999)) + "@gmail.com"

def get_random_name():
    name_list = open("names.txt").read().splitlines()
    random_line = random.choice(name_list)
    name_regex = re.compile(r'(\w*),\s(\w*)')
    return name_regex.search(random_line)

def random_phone_number():
        phone_number_1 = random.choice(area_codes)
        phone_number_2 = str(n.randint(100, 999))
        phone_number_3 = str(n.randint(1000, 9999))
        return phone_number_1 + phone_number_2 + phone_number_3

def get_driver(x):
    if x == 'w':
        return webdriver.Chrome(r"C:\Users\Jesus\Desktop\python\driver\chromedriver.exe")
    else:
        return webdriver.Chrome(r"/Users/jesus/Desktop/PythonPractice/driver/chromedriver 2")

def chef_table_fill_out():

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

    driver.get("https://acfp.myguestaccount.com/guest/enroll?card-template=ktYylJhNj2k%3d")

    # setting a wait time before inputting to make sure everything is loaded
    driver.implicitly_wait(30)

    # Random name
    name = get_random_name()

    # Birthdate
    #time = datetime.datetime.now()
    #bmonth = str(time.month)
    #bday = str(time.day + 1)

    # Name information
    driver.find_element_by_xpath("//*[@id='firstName']").send_keys(str(name.group(2)))
    driver.find_element_by_xpath("//*[@id='lastName']").send_keys(str(name.group(1)))

    # Favorite Store
    Select(driver.find_element_by_xpath("//*[@id='favoriteStoreState']")).select_by_value("110")
    time.sleep(5)
    Select(driver.find_element_by_xpath("//*[@id='favoriteStore']")).select_by_value(random.choice(Stores))

    # Zip code
    driver.find_element_by_xpath("//*[@id='postalCode']").send_keys(str(n.randint(33101, 33299)))

    # Phone number
    driver.find_element_by_xpath("//*[@id='mobilePhone']").send_keys(random_phone_number())

    # Birthdate
    driver.find_element_by_xpath("//*[@id='dateOfBirthMonth']").send_keys("01")
    driver.find_element_by_xpath("//*[@id='dateOfBirthDay']").send_keys("12")
    driver.find_element_by_xpath("//*[@id='dateOfBirthYear']").send_keys("1995")

    # Email
    driver.find_element_by_xpath("//*[@id='email']").send_keys(get_email(name))

    # Password
    driver.find_element_by_xpath("//*[@id='password']").send_keys(name.group(2) + "123!")
    driver.find_element_by_xpath("//*[@id='confirmPassword']").send_keys(name.group(2) + "123!")

    # Anti-detection
    # backspace()

    # Submit
    # driver.find_element_by_xpath("//*[@id='submit-btn']").click()

def run():
    emails = get_emails()
    for i in emails:
        chef_table_fill_out(i)

States = ["AK","AL","AR","AZ","CA","CO","CT","DC","DE","FL","GA","GU","HI","IA","ID", "IL","IN","KS","KY","LA","MA","MD","ME","MH","MI"
,"MN","MO","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY", "OH","OK","OR","PA","PR","PW","RI","SC","SD","TN","TX","UT","VA"
,"VI","VT","WA","WI","WV","WY"]
Stores = ["1012", "1061", "1018", "1030", "1025", "1047", "1015", "1017", "1026", "1066", "1010", "1034", "1029", "1065", "1064"]
area_codes = ["786", "305", "954", "754"]
n = random.SystemRandom()

# GUI
window = tk.Tk()
window.title("Chef's Table Filler")
window.geometry("400x400")

button = Button(window, command = chef_table_fill_out, text="OK", width = 10, height = 4).grid(row=5, column=0)




window.mainloop()
