from xml.etree import ElementTree as ET
import pprint

file_path = '/Users/Pippen/downloads/python/data-wrangling/data/chp3'
file_name = 'data-text.xml'
file_full_path = file_path + '/' + file_name

tree = ET.parse(file_full_path)
root = tree.getroot()
data = root.find('Data')
all_data = []
for observation in data:
    record = {}
    for item in observation:
        lookup_key = item.attrib.keys()[0]  # dic.keys()[0], the first key of a dictionary
        if lookup_key == 'Numeric':
            rec_key = 'NUMERIC'
            rec_value = item.attrib[lookup_key]
        else:
            rec_key = item.attrib[lookup_key]  # the value of a dictionary
            rec_value = item.attrib['Code']
        #print rec_key, rec_value
        record[rec_key] = rec_value
    all_data.append(record)
pprint.pprint(all_data)


