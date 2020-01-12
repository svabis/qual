#!/usr/bin/python2
# -*- coding: utf-8 -*-

# CONTAINER CHECK
import os # file system
import re # regular expresions
import mechanize # browser
import cookielib # browser cookies

import json

from time import sleep

# ========================================= Browser ========================================
# CMA
def cma_search(search):
    # Browser
    br = mechanize.Browser()
    # Cookie Jar
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    # Browser options
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    # User-Agent (this is cheating, ok?)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    cma_url = ["http://www.cma-cgm.com/ebusiness/tracking/search?SearchBy=Container&Reference=","&search=Search"]
    results = []

    for i in search:
        r = br.open(cma_url[0] + i + cma_url[1])
        html = r.read()
       # NOT FOUND
        temp = re.search("(\<h2>No\s{1}Results</h2>)", html)
        if temp:
            results.append( [i, "-", "-", "-", "-", "-", "CMA CGM"] )
            with open("/www/kuvalda/static/cont/results.json", 'wb') as outfile:
              json.dump(results, outfile)
       # FOUND
        else:
            try:
               # DATE & TIME
                date = re.findall("(\d{2}\s{1}[A-Z]\w{2}\s{1}\d{4})", html)
                time = re.findall("(\s{1}\d{2}\:\d{2})", html)
               # SHIP
#                temp_ship = re.findall('(?<="vessel" class="pv0-8 ph1">\r\s).*?(.*)', html)[-1].lstrip()
                temp_ship = re.findall('(?<=td data-label="Vessel">\r\s).*?(.*)', html)[-1].lstrip()
                if temp_ship.startswith('<'):
                    ship = temp_ship.split('>')[1].split('<')[0]
                else:
                    ship = temp_ship
               # VOYAGE
                voyage = re.findall('(?<=VoyageReference=).*?(?=")', html)[-1]
               # TERMINAL
#                terminal = re.findall('(?<="location" class="pv0-8 ph1">\r\s).*?(.*)', html)[-1].lstrip()
                terminal = re.findall('(?<=td data-label="Location">\r\s).*?(.*)', html)[-1].lstrip()

                results.append( [i, date[-1], time[-1], ship, voyage, terminal, "CMA CGM"] )
                with open("/www/kuvalda/static/cont/results.json", 'wb') as outfile:
                  json.dump(results, outfile)

            except:
                results.append( [i, "-", "-", "-", "-", "-", "CMA CGM"] )
                with open("/www/kuvalda/static/cont/results.json", 'wb') as outfile:
                  json.dump(results, outfile)
