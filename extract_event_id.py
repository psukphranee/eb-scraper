import csv
import os

f = open('event_brite_url_reshape.csv','r')
reader = csv.reader(f)
urls_list = list(reader)[0]

event_ids = []
for url in urls_list:
    first_half = url.split('?')


for url in urls_list:
    first_half = url.split('?')[0]
    event_id = first_half.split('-')[-1]
    event_ids.append(event_id)

f.close()
f = open('event_ids.csv','w')
writer = csv.writer(f, delimiter=',')
writer.writerow(event_ids)
f.close()
