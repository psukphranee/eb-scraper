from eventbrite import Eventbrite
import csv
import os

url_pre = 'https://www.eventbriteapi.com/v3/events/'
url_post = '/?expand=ticket_classes'

eb = Eventbrite('IM2AEVS63P2EB6BYY7GH')
f = open('event_ids_cleaned.csv','r')
rd = csv.reader(f, delimiter=',')
event_ids = [id for id in rd] #turns out to be a list of lists
event_ids = event_ids[0]

#convert IDs to integers
event_ids_int = [int(id) for id in event_ids]
