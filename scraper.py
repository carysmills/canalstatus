from bs4 import BeautifulSoup  
import sched, time
import csv
from splinter import Browser
import urllib2

def checkCanal():
	quote_page = "http://ncc-ccn.gc.ca/places-to-visit/rideau-canal-skateway/"
	page = urllib2.urlopen(quote_page)

	ready = "false"

	soup = BeautifulSoup(page)
	conditions = soup.find("div", attrs={"class": "card-content"})
	status = conditions.find("p").text
	infoformatted = status.encode('ascii', 'ignore')
	print infoformatted

	datetime = (time.strftime("%d/%m/%Y %H:%M:%S"))

	with open('canaldata.csv', 'a') as csvfile:
		csvwriter = csv.writer(csvfile, delimiter="|")
		csvwriter.writerow([ready, infoformatted, datetime])

checkCanal();	
