#!/usr/bin/python2
# -*- coding: utf-8 -*-
import re, os, datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver import FirefoxOptions

import json

gecko_path = '/bin/'


# !!!!! search maersk !!!!!
def cma_search(search):
    import time as pauze
    cma_url = "http://www.cma-cgm.com/ebusiness/tracking/search"

    os.system("killall -v firefox > /dev/null 2>&1 || true")
    pauze.sleep(1)
    os.system("killall -v geckodriver > /dev/null 2>&1 || true")
    pauze.sleep(2)

   # start new browser
    opts = FirefoxOptions()
    opts.add_argument( "--headless" )

    driver = webdriver.Firefox( gecko_path, firefox_options=opts )

    results = []
   # start checking process...
    for i in search:
        driver.get( cma_url )
#        pauze.sleep(5)
        try:
            element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID, "Reference")) )
            html = driver.page_source
        except TimeoutException:
            results.append( [i, "TIMEOUT", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR"] )
            with open("/www/kuvalda/static/cont/results.json", 'wb') as outfile:
              json.dump(results, outfile)
            continue

        except NoSuchElementException:
            results.append( [i, "NO ELEMENT", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR"] )
            with open("/www/kuvalda/static/cont/results.json", 'wb') as outfile:
              json.dump(results, outfile)
            continue

        finally:
            temp = [i, "NO_DATA", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "CMA CGM"]

           # fill form and submit
            element = driver.find_element_by_name("Reference")
            element.clear()
            element.send_keys( i )
            element.send_keys(Keys.RETURN);

           # wait for results to load
            pauze.sleep(5)
#            print("clicked "+i)

            try:
                element = WebDriverWait(driver, 15).until( EC.presence_of_element_located((By.ID, "c-footer")) )
                html = driver.page_source
            except TimeoutException:
                pass

            try:
                temp[1] = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/h1/span/span/abbr").get_attribute("innerHTML").split(" ")[0]
            except:
                temp[1] = "---"

            try:
#            if True:
                row = driver.find_element_by_xpath("(//table/tbody/tr)[last()]")
                col = row.find_elements_by_css_selector('td')
                count = 0
                for c in col:
                    t = c.get_attribute("innerHTML").lstrip()
#                    print( str(count)+":\n"+ t)
                   # DATE & TIME
                    if count == 0:
                        r = t.split(" ")
                        temp[2] = r[1] +" "+ r[2] +" "+ r[3]
                        temp[3] = r[4] + r[5]
                   # SHIP
                    if count == 4:
                        temp[4] = t
                   # VOYAGE
                    if count == 5:
                        temp[5] = t.split(">")[1].split("<")[0]
                    if count == 3:
                        temp[6] = t
                    count += 1
#                print("DATI par "+i+"\n")
                results.append( temp )
                with open("/www/kuvalda/static/cont/results.json", 'wb') as outfile:
                  json.dump(results, outfile)

            except:
                results.append( temp )
                with open("/www/kuvalda/static/cont/results.json", 'wb') as outfile:
                  json.dump(results, outfile)

    driver.quit()

   # kill resuming proceses
    os.system("killall -v firefox > /dev/null 2>&1 || true")
    pauze.sleep(1)
    os.system("killall -v geckodriver > /dev/null 2>&1 || true")



#cma_search( ["APHU6931774", "BMOU6577497", "TEMU5310771"] )
#cma_search( ["BMOU6577497"] )
