#!/usr/bin/python2
# -*- coding: utf-8 -*-
import re, os, datetime
import unicodedata # normalize unicode to string


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

def one_search(search):
    import time as pauze
    results = []
    one_url = "https://www.one-line.com/"

    os.system("killall -v firefox > /dev/null 2>&1 || true")
    pauze.sleep(1)
    os.system("killall -v geckodriver > /dev/null 2>&1 || true")
    pauze.sleep(2)

   # start new browser
    opts = FirefoxOptions()
    opts.add_argument( "--headless" )

    driver = webdriver.Firefox( gecko_path, firefox_options=opts )
#    driver = webdriver.Firefox( firefox_options=opts )
    driver.get( one_url )

    try:
        element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.ID, "ctrack-field")) )
    except TimeoutException:
        for _ in search:
          results.append( ["TIMEOUT", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ONE"] )
        with open("/www/kuvalda/static/cont/results.json", 'wb') as outfile:
          json.dump(results, outfile)
        return

    except NoSuchElementException:
        for _ in search:
          results.append( ["NO_ELEMENT", "ctrack-field", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ONE"] )
        with open("/www/kuvalda/static/cont/results.json", 'wb') as outfile:
          json.dump(results, outfile)
        return

    finally:
        pauze.sleep(5)

       # fill form and submit
        element = driver.find_element_by_id("ctrack-field")
        element.send_keys( search[0] )
        element.send_keys(Keys.RETURN)

        pauze.sleep(10)

# ============= start second tab ===================
        print( len(driver.window_handles) )
        driver.close()

        driver.switch_to.window( driver.window_handles[0] )
#        driver.switch_to.window( driver.window_handles[-1] )

        print( len(driver.window_handles) )
#        try:
#            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
#            driver.switch_to.window( driver.window_handles[-1] )
#            driver.switch_to.window( driver.window_handles[0] )
#        except:
#            driver.quit()
#            print( "NAV!" )
        pauze.sleep(10)

    try:
        element = WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.ID, "btnSearch")) )
    except TimeoutException:
        for _ in search:
          results.append( ["TIMEOUT", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ONE"] )
        with open("/www/kuvalda/static/cont/results.json", 'wb') as outfile:
          json.dump(results, outfile)
        return

    except NoSuchElementException:
        for _ in search:
          results.append( ["NO_ELEMENT", "btnSearch", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ONE"] )
        with open("/www/kuvalda/static/cont/results.json", 'wb') as outfile:
          json.dump(results, outfile)
        return

    finally:
      pauze.sleep(3)
     # Iterate search
      for i in search:
        pauze.sleep(3)

        try:
           # CHANGE TYPE
            element =  driver.find_element_by_name("searchType")
            element.click()
            pauze.sleep(1)

           # SELECT "Container No."
            element = driver.find_element_by_xpath("//option[@value='C']")
            element.click()
            pauze.sleep(1)
        except:
            results.append( ["NO_ELEMENT", "searchType", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ONE"] )
            with open("/www/kuvalda/static/cont/results.json", 'wb') as outfile:
              json.dump(results, outfile)
            return

        finally:
            temp = [i, "NO_DATA", "-", "-", "-", "-", "-", "ONE"]

           # fill form and submit
            element = driver.find_element_by_name("searchName")
            element.clear()
            element.send_keys( i )

            element = driver.find_element_by_id("btnSearch")
            element.click()

           # wait for results to load
            pauze.sleep(8)
            html = driver.page_source
            html = html.replace("&nbsp;", " ")

           # CONTAINER SIZE
            try:
                size = driver.find_element_by_xpath("//div[@id='statusInfo']/table/tbody/tr[1]/td[3]").get_attribute("innerHTML")
                size = size.split("<br>")[1].split("'")[0]
            except:
                size = "---"

            try:
                table_id = driver.find_element_by_css_selector("table#sailing tbody")
                rows = table_id.find_elements(By.TAG_NAME, "td")
                data = []

                try:
                  element = driver.find_element_by_css_selector("div.ui-dialog-buttonpane div.ui-dialog-buttonset button")
                  element.click()
                except:
                  pass

                for r in rows:
                  d = unicodedata.normalize('NFKD', r.text).encode('ascii','ignore')
                  data.append( d )

               # DATE & TIME
                try:

                    date = ""
                    time = ""
                    datv = ""

                    tr = driver.find_elements_by_xpath("//div[@id='detailInfo']/table/tbody/tr")
                    for e in tr:
                        td  = e.find_elements_by_css_selector("td")[2].get_attribute("innerHTML")
                        tdx = e.find_elements_by_css_selector("td")[3].get_attribute("innerHTML")
                        if td.startswith( "RIGA" ):
                            date = tdx.split(">")[2].split(" ")[1]
                            time = tdx.split(">")[2].split(" ")[2]
                            datv = tdx.split(">")[1].split("<")[0]
                            break
                except:
                    date = data[-1].split(" ")[1]
                    time = data[-1].split(" ")[2]
                    datv = data[-1].split(" ")[0]

               # RESULTS
#                print [i, size, date, time, data[-5], datv, data[-2], "ONE"]
                results.append( [i, size, date, time, data[-5], datv, data[-2], "ONE"] )
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


#one_search( ["DRYU4299382", "NYKU4961366", "NYKU4941776", "TCLU9468433", "GLDU9364025", "KKTU8076330", "MOAU1412037", "DRYU4250340", "TEMU2542794", "KKTU8261195", "TEMU0180612"] )
