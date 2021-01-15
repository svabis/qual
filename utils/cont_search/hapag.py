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
def hapag_search(search):
    import time as pauze
    hapag_url = "https://www.hapag-lloyd.com/en/online-business/tracing/tracing-by-container.html?container="

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
        driver.get( hapag_url + i )
        pauze.sleep(3)
        try:
            element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID, "to-top")) )
            html = driver.page_source
        except TimeoutException:
#            results.append( [i, "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR"] )
#            with open("/www/kuvalda/static/results.json", 'wb') as outfile:
#              json.dump(results, outfile)
            continue

        except NoSuchElementException:
            results.append( [i, "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR"] )
            continue
            with open("/www/kuvalda/static/cont/results.json", 'wb') as outfile:
              json.dump(results, outfile)

        finally:
            html = driver.page_source
            temp = []
            error = False

            try:
                size = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[1]/div/div/div/div[2]/form/div[5]/div[2]/div/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/div/table/tbody/tr/td[5]/table/tbody/tr/td[2]").get_attribute("innerHTML").split("'")[0]
            except:
                size = "---"

           # Last entry: "Discharge"
            try:
              info = re.search("(?<=Discharge)(.*?)(</td></tr></tbody></table>)", html).group(1)
              data = info.split("</span>")
              temp.append(i)

              temp.append(size)

              temp.append(data[-5].split(">")[-1])
              temp.append(data[-4].split(">")[-1])
              temp.append(data[-3].split(">")[-1])
              temp.append(data[-2].split(">")[-1])
              temp.append(data[-6].split(">")[-1])
              temp.append("Hapag-Lloyd")
            except:
              temp = [i, "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR"]
              error = True
           # Last entry: "Vessel arrived"
            if error == True:
                try:
                  temp = []
                  info = re.search("(?<=Vessel\s{1}arrived)(.*?)(</td></tr></tbody></table>)", html).group(1)
                  data = info.split("</span>")
                  temp.append(i)

                  temp.append(size)

                  temp.append(data[-5].split(">")[-1])
                  temp.append(data[-4].split(">")[-1])
                  temp.append(data[-3].split(">")[-1])
                  temp.append(data[-2].split(">")[-1])
                  temp.append(data[-6].split(">")[-1])
                  temp.append("Hapag-Lloyd")
                except:
                  temp = [i, "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR"]
                  error = True
           # Last entry: "Vesel arival"
            if error == True:
                try:
                  temp = []
                  info = re.search("(?<=Vessel\s{1}arrival)(.*?)(</td></tr></tbody></table>)", html).group(1)
                  data = info.split("</span>")
                  temp.append(i)

                  temp.append(size)

                  temp.append(data[-5].split(">")[-1])
                  temp.append(data[-4].split(">")[-1])
                  temp.append(data[-3].split(">")[-1])
                  temp.append(data[-2].split(">")[-1])
                  temp.append(data[-6].split(">")[-1])
                  temp.append("Hapag-Lloyd")
                except:
                  temp = [i, "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR"]

            results.append( temp )
            with open("/www/kuvalda/static/cont/results.json", 'wb') as outfile:
              json.dump(results, outfile)

    driver.quit()

   # kill resuming proceses
    os.system("killall -v firefox > /dev/null 2>&1 || true")
    pauze.sleep(1)
    os.system("killall -v geckodriver > /dev/null 2>&1 || true")

#hapag_search( ["GESU3645245"] )
