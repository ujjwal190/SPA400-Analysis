import httplib, urllib2, re, sys, time, requests, base64, requests, re, mechanize, bs4

file = open('CompaniesAlreadyDone.txt')
f = open('/Users/Chris/Desktop/numbers.txt', 'r+')

for comp in file:
   company = comp.strip()
   r = requests.get('http://ichart.finance.yahoo.com/table.csv?s='+company+'&amp;d=8&amp;e=23&amp;f=2013&amp;g=d&amp;a=1&amp;b=1&amp;c=2003&amp;ignore=.csv')
   f.write(comp)
   f.write(r.text)
   #print comp
   #print r.text



'''
page = 'http://www.nasdaq.com/symbol/fb/historical'
browser = mechanize.Browser()
browser.open(page)


#for form in browser.forms():
#    print "Form name:", form.name
#    print form

'''
'''
browser.select_form("quotenav")

counter = 0
for control in browser.form.controls:
        if counter == 2:
            control.disabled = False
            control.readonly = False
            #control.value = "10y"
            print control.id

        counter += 1
        #print control
        #print control.type

#response = browser.submit()
#print response.read()
'''