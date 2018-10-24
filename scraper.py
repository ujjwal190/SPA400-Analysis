import httplib, urllib2, re, sys, time, requests, base64, requests, re, mechanize, bs4
from bs4 import BeautifulSoup
from array import *

file = open('SP500Abbrevs.txt', 'r')
#for line in file:
#    print line

page100 = 'http://finance.yahoo.com/q/bs?s=NKE+Balance+Sheet&annual'
page200 = open('intelBalanceSheet.html', 'r')
page300 = open('BalanceSheetItems.txt', 'r')
page400 = open('SP500Abbrevs.txt', 'r')
page500 = open('MainBalanceSheetItems.txt', 'r')
page600 = open('/Users/Chris/Desktop/sp500.txt', 'r+')
#page600 = open('/Users/Chris/Desktop/sp500BalancSheets.txt')

#GETS ACCOUNTS
accounts = []
for line in page300:
   accounts.append(line.strip())
   #print line

#GETS MAIN ACCOUNTS
mainAccounts = []
for line in page500:
    mainAccounts.append(line.strip())

#GETS ABBREVS
counter = 0
abbrevs = []
for line in page400:
    abbrevs.append(line.strip())
    counter += 1

#r = requests.get(page200)
#browser = mechanize.Browser()
#browser.open(page100)
#length = abbrevs.len
#print length

for elm in range(0, counter-1):
    site = 'http://finance.yahoo.com/q/bs?s='+abbrevs[elm]+'+Balance+Sheet&annual'
    r = requests.get(site)
    #soup = BeautifulSoup(page200)
    soup = BeautifulSoup(r.text)
    rows = soup.find_all(align="right", text=re.compile("[,-]"))
    mains = soup.find_all('strong', text=re.compile("[,-]"))


    data = []
    counter = 0
    for row in rows:
        data.append(row.text.strip())
        counter += 1


    data2 = []
    for row in mains:
        data2.append(row.text.strip())
        #print row.text.strip()

    #print counter
    length = counter/3
    length2 = counter/2
    #print length


    if counter > 65:

        for el in range(0,length):
            print abbrevs[elm], ",", accounts[el], ",", data[el*3], ",", data[(el*3)+1], ",", data[(el*3)+2]
            text = abbrevs[elm], ",", accounts[el], ",", data[el*3], ",", data[(el*3)+1], ",", data[(el*3)+2], "\n"
            #text = str(text)
            #page600.write(text)

        for el2 in range(0,6):
            print abbrevs[elm], ",", mainAccounts[el2], ",", data2[el2*3], ",", data2[(el2*3)+1], ",", data2[(el2*3)+2]
            #text = abbrevs[elm], ",", mainAccounts[el2], ",", data2[el2*3], ",", data2[(el2*3)+1], ",", data2[(el2*3)+2]
            #page600.write(text)
    else:
        for el in range(0,length2):
            print abbrevs[elm], ",", accounts[el], ",", data[el*2], ",", data[(el*2)+1]
            #text = abbrevs[elm], ",", accounts[el], ",", data[el*2], ",", data[(el*2)+1]
            #page600.write(text)

        for el2 in range(0,6):
            print abbrevs[elm], ",", mainAccounts[el2], ",", data2[el2*2], ",", data2[(el2*2)+1]
            #text = abbrevs[elm], ",", mainAccounts[el2], ",", data2[el2*2], ",", data2[(el2*2)+1]
            #page600.write(text)










