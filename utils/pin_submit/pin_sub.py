#!/usr/bin/python2
# -*- coding: utf-8 -*-
import re, os, datetime
#from random import randint # generate random int

import unicodedata # normalize unicode to string

# PAUZE
import time as pauze

import json

# SELENIUM
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import FirefoxOptions

# =========================================================================================================================================================

# Geckodriver path
gecko_path = '/bin/'

# Give the location of the .xlsx file
input_loc = "/home/svabis/web/utils/pin_submit/pin_temp/train.xlsx"

# URL OF PAGE
# 1- login
# 2- PIN enter
url_1 = "https://prebooking.bct.lv/login"
#url_1 = "https://prebooking.bct.lv"
url_2 = "https://prebooking.bct.lv/visits/add-outgate"

results = []
errors = []
exit = False
driver = None

# =========================================================================================================================================================

# kill Firefox & Geckodriver
def kill_mozzila():
    os.system("killall -v firefox > /dev/null 2>&1 || true")
    pauze.sleep(1)
    os.system("killall -v geckodriver > /dev/null 2>&1 || true")
    pauze.sleep(2)


# INPUT PIN INTO FIELD
def input_pin(pin, kont):
    global driver
   # Define Respose Message
    resp = ""

    try:
       # enter PIN
        element = driver.find_element_by_id("outgate_booking_nr")
        element.send_keys( pin )
        element.send_keys(Keys.RETURN)
        pauze.sleep(6)

       # TEST RESPONSE for Used or Incorect Pin
        try:
            element = driver.find_element_by_id("outgateQueryMessage")
            if element.text == "Please check your BOOKING number.":
                resp = "Please check your BOOKING number."
                return ([pin, kont, resp])
        except:
            pass

       # Select carrier
        selectOption = Select( driver.find_element_by_id("book_outbound_carrier_id") )
        selectOption.select_by_visible_text("Rail")

       # Select "SRR Logistics, SIA"
        pauze.sleep(3)
        selectOption = Select( driver.find_element_by_id("book_rail_forwarder") )
        selectOption.select_by_visible_text("SRR Logistics, SIA")

       # Date
        pauze.sleep(3)
        element = driver.find_element_by_name("operations_date")
        element.send_keys( datetime.datetime.now().strftime("%Y-%m-%d") )
        element.send_keys(Keys.RETURN)

       # Iterate container list
        pauze.sleep(3)
        element = driver.find_elements_by_css_selector("div.listbox div.listbox_item a")
        for e in element:
            if kont in e.text:
               # Add container
                e.click()
                pauze.sleep(3)

               # "Confirm visit"
                conf = driver.find_element_by_id("ask_button").click()
                pauze.sleep(5)

               # Get response
                el = driver.find_element_by_css_selector("div#content")
                temp_str = unicodedata.normalize('NFKD', el.text).encode('ascii','ignore')
                resp = temp_str.split("\n")[1]
                return ([pin, kont, resp ])

       # Container not found in PIN containers list
        return ([pin, kont, "Container Not Found"])

   # Error ocured
    except:
        return ([pin, kont, "Some Error ocured"])


# CHECK FOOTER
def chk_footer():
    global driver
    global errors
    global exit
    try:
        wait = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.ID, "gdpr-usr")) )
    except TimeoutException:
        errors.append( "FOOTER_TimeoutException" )
        exit = True
    except NoSuchElementException:
        errors.append( "FOOTER_NoSuchElementException" )
        exit = True
    except OtherExceptions:
        errors.append( "FOOTER_OtherExceptions" )
        exit = True


# LOGIN
def login(user, pasw):
    global driver
    global errors
    global exit
    try:
        element = driver.find_element_by_name("login")
        element.send_keys( user )

        element = driver.find_element_by_name("password")
        element.send_keys( pasw )
        element.send_keys(Keys.RETURN)
    except:
        errors.append( "LoginError" )
        exit = True


def read_xlsx():
    global results
    global input_loc
    import xlrd
   # array for xlsx data
    temp = []
   # Read xlsx file
    wb = xlrd.open_workbook(input_loc)
    sheet = wb.sheet_by_index(0)
   # append data to array
    for i in range(0, sheet.nrows):
      try:
        temp.append( [ str(sheet.cell_value(i, 1)).split(";")[1], str(sheet.cell_value(i, 0))] )
      except:
        pass
    return temp

# !!!!! MAIN !!!!!
# =========================================================================================================================================================
def pin_reader():
    global driver
    global url_1
    global url_2
    global results
    global errors
    global exit

   # Reset variables
    results = []
    errors = []
    exit = False
    driver = None

   # Read .xlsx
    pin_array = read_xlsx()
   # stop Firefox
#    kill_mozzila()

   # start new browser
    opts = FirefoxOptions()
    opts.add_argument( "--headless" )

    driver = webdriver.Firefox( gecko_path, firefox_options=opts )
#    driver = webdriver.Firefox(firefox_options=opts)
    driver.get( url_1 )

    try:
        wait = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.ID, "login_error")) )
    except TimeoutException:
        errors.append( "TimeoutException" )
        exit = True
    except NoSuchElementException:
        errors.append( "NoSuchElementException" )
        exit = True
    except OtherExceptions:
        errors.append( "OtherExceptions" )
        print("OTHER EXCEPTION")
        exit = True
    finally:
        if exit != True:
       # FILL LOGIN FIELDS
           # id=name="login" jsaulitis3
           # id=name="password" Reinisisthebestbt
            login("jsaulitis3", "Reinisisthebestbt")

        if exit != True:
           # Check footer
            chk_footer()

        if exit != True:
           # Press "Accept"
            pauze.sleep(10)
            try:
                element = driver.find_element_by_css_selector(".btn-accept").click()
            except TimeoutException:
                errors.append( "ACCEPT_PRESS_TimeoutException" )
                exit = True
            except NoSuchElementException:
                pass
            except OtherExceptions:
                errors.append( "ACCEPT_PRESS_OtherExceptions" )
                exit = True

        if exit != True:
            c_count = 0
           # Iterate PIN
            for p in pin_array:
              try:
                driver.get( url_2 )
               # Check footer
                chk_footer()

                if exit != True:
                   # if no errors submit PIN and add Container
                    temp = input_pin( p[0], p[1] )
#                    print temp
                    results.append( temp )
                    c_count += 1
              except:
#                pass
                results.append( [p[0], p[1], "BIG Error ocured"] )

             # Append results to file
              with open("/www/kuvalda/static/cont/pin_results.json", 'wb') as outfile:
                  json.dump( results, outfile )
             # Write progresbar status
              f = open("/www/kuvalda/static/cont/pin_progress.json","w")
              f.write('{"progress": "' + str( int((float(c_count)/len(pin_array)) * 100 )) + '"}\r\n')
              f.close()


# kill resuming proceses & exit
    driver.quit()
#    kill_mozzila()

#    if len(errors) > 0:
#        print errors
#    print datetime.datetime.now()


#pin_reader()
