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

def msc_search(search):
    import time as pauze
    msc_url = "https://www.msc.com/track-a-shipment?agencyPath=lva"

    os.system("killall -v firefox > /dev/null 2>&1 || true")
    pauze.sleep(1)
    os.system("killall -v geckodriver > /dev/null 2>&1 || true")
    pauze.sleep(2)

   # start new browser
    opts = FirefoxOptions()
    opts.add_argument( "--headless" )

    driver = webdriver.Firefox( gecko_path, firefox_options=opts )
    driver.get( msc_url )

    try:
        element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.ID, "subFooter")) )
    except TimeoutException:
        for _ in search:
          results = ["TIMEOUT", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "MSC"]
        with open("/www/kuvalda/static/cont/results.json", 'wb') as outfile:
          json.dump(results, outfile)
        return

    except NoSuchElementException:
        for _ in search:
          results = ["NO_ELEMENT", "subFooter", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "MSC"]
        with open("/www/kuvalda/static/cont/results.json", 'wb') as outfile:
          json.dump(results, outfile)

        return

    finally:
       # press button "No, Thanks"
        pauze.sleep(10)
        try:
            element = driver.find_element_by_link_text("No, Thanks")
            element.click()
        except NoSuchElementException:
#            for _ in search:
#              results = ["NO_SUCH_ELEMENT", "BUTTON", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "MSC"]
#            with open("/www/kuvalda/static/results.json", 'wb') as outfile:
#              json.dump(results, outfile)
            pass
        pauze.sleep(5)

        results = []

        for i in search:
            temp = [i, "NO_DATA", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "MSC"]

           # fill form and submit
            element = driver.find_element_by_name("ctl00$ctl00$plcMain$plcMain$TrackSearch$txtBolSearch$TextField")
            element.clear()
            element.send_keys( i )
            element.send_keys(Keys.RETURN);

           # wait for results to load
            pauze.sleep(5)
            html = driver.page_source
            html = html.replace("&nbsp;", " ")

            try:
                size = driver.find_element_by_xpath("/html/body/form/div[4]/div/div[2]/main/div/div[2]/div/div/div[2]/dl/dd/div/dl/dd/div/table[1]/tbody/tr[2]/td[1]/span").get_attribute("innerHTML").split("'")[0]
            except:
                size = "---"

            try:
                data = re.findall('(?<=class="responsiveTd">\s).*?(?=</span)', html)

                results.append( [i, size, data[2].lstrip(), "-", data[3].lstrip(), data[4].lstrip(), data[0].lstrip(), "MSC"] )
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

#msc_search( ["MEDU8626230"] )
