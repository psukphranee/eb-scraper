import os
import csv

f = open('event_ids.csv')
reader = csv.reader(f, delimiter=',')
event_ids = list(reader)[0]

#find non-numbers and move them into another list
non_numbers = []

for event_id in event_ids:
    try:
        print(int(event_id))
    except:
        non_numbers.append(event_id)
        event_ids.remove(event_id)
        print("Non-number found: ", event_id)
