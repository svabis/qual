#!/usr/bin/python2
# -*- coding: utf-8 -*-
import json

import re, os, datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver import FirefoxOptions

# disable LOG
import logging
from selenium.webdriver.remote.remote_connection import LOGGER

#LOGGER.setLevel(logging.WARNING)
LOGGER.setLevel(logging.ERROR)
#LOGGER.stop()

gecko_path = '/bin/'

# !!!!! search maersk !!!!!
def maersk_search(search):
    import time as pauze
    maersk_url = "https://my.maerskline.com/tracking/#tracking/search?searchNumber="

    os.system("killall -v firefox > /dev/null 2>&1 || true")
    pauze.sleep(2)
    os.system("killall -v geckodriver > /dev/null 2>&1 || true")
    pauze.sleep(3)

   # start new browser
    opts = FirefoxOptions()
    opts.add_argument( "--headless" )

    driver = webdriver.Firefox( gecko_path, firefox_options=opts )
#    driver = webdriver.Firefox( firefox_options=opts )

    results = []
   # start checking process...
    try:
      for i in search:
        driver.get( maersk_url + i )
        pauze.sleep(3)
        try:
#            element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID, "footerData")) )
            element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID, "ign-footer")) )
            html = driver.page_source
        except TimeoutException:
            pass
            results.append( [i,"TIMEOUT ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR"] )
            with open("/www/kuvalda/static/cont/results.json", 'wb') as outfile:
              json.dump(results, outfile)
            continue

        except NoSuchElementException:
            results.append( [i,"ELEMENT_ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR"] )
            with open("/www/kuvalda/static/cont/results.json", 'wb') as outfile:
              json.dump(results, outfile)
            continue

        finally:
            html = driver.page_source
            temp = []

            try:
                try:
                    size = re.findall("<span>(\d{2})ft Dry Container</span>", html)[0]
                except:
                    size = "---"

                date = re.findall("(\d{2}\s{1}[A-Z]\w{2}\s{1}\d{4})", html) # ALL MATCH ARRAY
#                time = re.findall("(\d{2}\:\d{2})", html)
                terminal = re.findall('(?<=td\s{1}data-th="Location"\s{1}class="timeline__event-table__cell\s{1}timeline__event-table__cell--heading">).*(?=</td>)', html)[-1]
                ship = re.findall("(?<=Load\son\s).*?(?=<br)", html)
                voyage = re.findall("(?<=Voyage\s{1}No.).*?(?=\s)", html)

                results.append( [i, size, date[0], "-", ship[-1], voyage[-1], terminal.replace('<br>', ' '), "Maersk" ] )
                with open("/www/kuvalda/static/cont/results.json", 'wb') as outfile:
                  json.dump(results, outfile)

            except:
                results.append( [i, "-", "-", "-", "-", "-", "-", "Maersk"] )
                with open("/www/kuvalda/static/cont/results.json", 'wb') as outfile:
                  json.dump(results, outfile)

#            print( results )

    except:
      pass

    driver.quit()
   # kill resuming proceses
    os.system("killall -v firefox > /dev/null 2>&1 || true")
    pauze.sleep(1)
    os.system("killall -v geckodriver > /dev/null 2>&1 || true")


#maersk_search( ["MSKU1042177", "TLLU2498630"] )
