#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os
import json

temp_results = []

# !!!!! MAERSK !!!!!
# ======================================
def maersk_mail_pin_search( file ):
    import re
    import textract

    text = textract.process( file )
    line = text.split("\n")

   # SEARCH "MAERSK" IN PDF
    maersk_str = re.findall("(Maersk)", text)
    sealand_str = re.findall("(Seago\ Latvija\ SIA)", text)
    print maersk_str

    if len(maersk_str) == 0 or len(sealand_str) > 0:
      return Null

    print "Procesing Maersk PDF..."

    # result array --> to be JSON
    results = []
    # date string "Valid to Date"
    valid = ""
    # array for line numbers containing containers in PDF text
    kont_line = []

    # Search "Valid to Date"
    valid_str = re.findall("(\w{4}\-\w{2}\-\w{2})", text)
    valid = valid_str[-1]

    # Search containers in pdf
    for i in range ( 0, len(line) ):
        kont = re.findall("(\w{4}\d{7})", line[i])
        if len(kont) > 0 and len(line[i]) == 11:
            kont_line.append(i)

    # Get pin numbers, append results to array
    for kl in kont_line:
        c = 0
        r1 = line[kl]
        for i in range (kl, kl+(10*len(kont_line)), len(kont_line)):
            if line[i] != "":
                c += 1
                if c == 5:
                   r2 = ";" + line[i]
        results.append([r1, r2, valid, "Maersk"])

    return results




# !!!!! SEALAND MAERSK !!!!!
# ======================================
def sealand_mail_pin_search( file ):
    import re
    import textract

    text = textract.process( file )
    line = text.split("\n")

   # SEARCH "SEALAND" IN PDF
    sealand_str = re.findall("(Seago\ Latvija\ SIA)", text)
    print sealand_str

    if len(sealand_str) == 0:
      return Null

    print "Procesing SEALAND PDF..."

    # result array --> to be JSON
    results = []
    # date string "Valid to Date"
    valid = ""
    # array for line numbers containing containers in PDF text
    kont_line = []

    # Search "Valid to Date"
    valid_str = re.findall("(\w{4}\-\w{2}\-\w{2})", text)
    valid = valid_str[-1]

    # Search containers in pdf
    for i in range ( 0, len(line) ):
        kont = re.findall("(\w{4}\d{7})", line[i])
        if len(kont) > 0 and len(line[i]) == 11:
            kont_line.append(i)

    count = len(kont_line)
    # Get pin numbers, append results to array
    for kl in kont_line:
        r1 = line[kl]
        r2 = ";" + line[kl + (4 * count) + 4]
        results.append([r1, r2, valid, "Sealand Maersk"])

    return results




# !!!!! CMA !!!!!
# ======================================
def cma_mail_pin_search( file ):
    import re
    import textract

    text = textract.process( file )
    line = text.split("\n")

    # result array --> to be JSON
    results = []
    # order nr
    order = ""
    # conatiner array
    kont = []
    # EXP DATE array
    date = []

    for i in range ( 0, len(line) ):
        if line[i] == "DELIVERY ORDER NO":
            for j in range (1,10):
              if line[i+j] != "":
                if line[i+j][0] == ":":
                  order = line[i+j].split(" ")[1]
                  break

    # Search containers in pdf
    for i in range ( 0, len(line) ):
        temp = re.findall("(\w{4}\d{7})", line[i])
        if len(temp) > 0 and len(line[i]) == 11:
            kont.append(line[i])
    kont = list(set(kont))

    # Find Expiration dates 28-FEB-19
    for i in range ( 0, len(line) ):
        temp = re.findall("(\EXP\s\DATE)", line[i])
        if len(temp) > 0:
            for j in range (1, len(line)):
                if j+i >= len(line):
                    break
                temp = re.findall("(\d{2}\-\w{3}\-\d{2})", line[i+j])
                if len(temp) > 0: # and len(line[i]) == 9:
                    date.append(line[i+j])
    i = 0
    for k in kont:
        results.append([k, ";" + order, date[i], "CMA"])
        i += 1

    return results


# !!!!! PRINT SEPARETED OUTPUT !!!!!
def output( array ):
    global temp_results
    for l in array:
        print l
        if l[2] != "":
#            print str(l[0]) + ";" +str(l[1]) + ";" + str(l[2]) + ";" + comp
            temp_results.append( l )
    with open("/www/kuvalda/static/cont/pdf_results.json", 'wb') as outfile:
        json.dump(temp_results, outfile)


# count files
def pdf_count():
  file = []
  path = "/home/svabis/web/utils/pdf_mail/temp/"
  for filename in os.listdir(path):
      file.append( path + filename )
  return len(file)

# main process
def pdf_process():
  global temp_results
  temp_results = []

  file = []

  path = "/home/svabis/web/utils/pdf_mail/temp/"
  for filename in os.listdir(path):
      file.append( path + filename )

  for f in file:
      try:
          output( maersk_mail_pin_search( f ) )
      except:
          pass

      try:
          output( sealand_mail_pin_search( f ) )
      except:
          pass

      try:
          output( cma_mail_pin_search( f ) )
      except:
          pass

#print pdf_count()
#pdf_process()
