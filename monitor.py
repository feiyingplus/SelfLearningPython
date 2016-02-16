# monitor the latitute change for the busid
import urllib

# from xml.etree.ElementTree import parse
from xml.etree.ElementTree import parse

candidates = ['1713', ]
office_lat = 41.980262
google_API_key = 'AIzaSyDnJ9fkfnURHv8wJb9CxAjJB-BmatEXoOQ'
# lon = ""
# lat = ""
url1 = "https://maps.googleapis.com/maps/api/staticmap?maptype=satellite&center="

url_trace1  = "https://www.google.com/maps/dir/"

def distance(lat1, lat2):
    # calculate the miles between two lats
    return 69 * abs(lat1 - lat2)


def monitor():
    u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
    doc = parse(u)
    for bus in doc.findall('bus'):
        busid = bus.findtext('id')
        if busid in candidates:
            lon = float(bus.findtext('lon'))
            lat = float(bus.findtext('lat'))
            dis = distance(lat, office_lat)
            #print(busid, lat, lon, dis, 'miles')
            url = url1 +str(lat)+ "," +str(lon)+ str("&zoom=18&size=800x600&key=") + google_API_key
            print "URL is "+ url
            # return [lat, lon]
    print ('-' * 30)


import time
while True:
    # geo_start = [[41.98290894248269,-87.66863736239347],]
    # #print 'monitor is '+ str(monitor())
    # geo_start.append(monitor())
    #print geo_start
    # with open('bus_location.txt', 'a') as bus_file:
    #     bus_file.write(str([monitor()]))
    #     bus_file.close
    monitor()
    time.sleep(60)