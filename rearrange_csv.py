import csv

f = open('event_brite_url.csv', 'r')
urls = csv.reader(f, delimiter=',')
urls_list = list(urls)

url_reshape = []

for url_row in urls_list:
    for url in url_row:
        url_reshape.append(url)

f1 = open('event_brite_url_reshape.csv', 'w')
wr = csv.writer(f1, delimiter=',')

wr.writerow(url_reshape)

f.close()
f1.close()
