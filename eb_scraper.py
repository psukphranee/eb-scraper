from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
import csv

#define a sleep function that prints a count down
def wait_for_it(sec):
    print('Waiting {} seconds\n.'.format(sec))
    for i in range(sec, 0, -1):
        print(i, end='')
        time.sleep(1)
        print('\b')
    print("\n")

def get_events_on_page():

    events = driver.find_element_by_class_name('search-main-content__events-list').find_elements_by_tag_name('li')
    print('Begin to loop through events')
    wait_for_it(5)

    #get list of event URLs on page
    with open("event_brite_url.csv", 'a') as f:
        event_writer = csv.writer(f, delimiter=',')

        current_page_urls = return_urls(events)

        event_writer.writerow(current_page_urls)

    return current_page_urls

#define function to get URLs
def return_urls(events):
    event_len = len(events)
    print("there are ", event_len, "events.")
    event_links = []

    int_i = 0

    for event in events:
        int_i = int_i + 1
        print("event ", int_i, " of ", event_len)
        print('Click share button in:')
        wait_for_it(2)
        #click the share button
        event.find_elements_by_tag_name('button')[0].click()
        print('Share button clicked.', 'Getting the share URL.')
        wait_for_it(2)
        str = driver.find_elements_by_tag_name('input')[-2].get_attribute('value')
        event_links.append(str)
        print('Share Url: {} appended'.format(str))
        print('Click close button in')
        wait_for_it(1)
        #close the overlay
        driver.find_element_by_class_name('eds-modal__close-button').click()

    return event_links

## Initiation
#navigate to homepage
print('Defining driver objects and navigating to EventBrite')
eventbrite_homepage_url = 'https://www.eventbrite.com'
driver = Chrome()
driver.get(eventbrite_homepage_url)

#get nav bar
print('starting to wait 30 seconds for page to load to get nav-bar')
wait_for_it(30)
nav_bar = WebDriverWait(driver, 120).until(lambda d: d.find_element(By.TAG_NAME, 'nav'))
nav_buttons = nav_bar.find_elements(By.TAG_NAME, 'button')

#get music button
print('starting to wait 15 seconds to click the "Music" button')
wait_for_it(15)
music_button = [x for x in nav_buttons if x.text == 'Music'][0]
music_button.click()

#want to navigate and click the "See more" link. first get a list of all links
print('starting to wait 10 seconds to click "See More" link')
wait_for_it(10)
current_links = WebDriverWait(driver, 120).until(lambda d: d.find_elements(By.TAG_NAME, 'a'))
see_more = [x for x in current_links if x.text == 'See more'][0]
see_more.click()

#list of lists, one list for each page
event_links = []

#get the number of to loop thru
num_of_pages = int(driver.find_element_by_class_name('eds-pagination__navigation-group').text.split()[2])


for i in range(num_of_pages):
    print("-------------------------Page ", i, " of ", num_of_pages, '-------------------------')
    print('getting events on page in... ')
    wait_for_it(10)
    event_links.append(get_events_on_page())

    #wait and click next page button
    driver.find_element_by_class_name('eds-pagination__navigation-group').find_elements_by_tag_name('button')[-1].click()
