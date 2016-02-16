# get_rt22.py
#
# From the notes.  Access the CTA website and fetch information
# about route 22 buses.  Write to a file 'rt22.xml'.

# For Python 3, change import urllib to urllib.request

import urllib

u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data = u.read()
print 'reading xml file online'
# print data
print 'reading completed'

f = open('rt22.xml', 'w')
f.write(data)
f.close()

with open('rt22.xml', 'r') as f:
    print f.read()
