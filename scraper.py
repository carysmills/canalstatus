# import libraries
from bs4 import BeautifulSoup  
import sched, time
import csv
from splinter import Browser

def checkCanal():
	with Browser("phantomjs") as browser:
	    browser.driver.set_window_size(1280, 1024)
	    browser.visit("http://rcs.ncc-ccn.ca")
	    button = browser.find_by_css(".feature-conditions")
	    button.click()
	    html = browser.html

    # find the right info
	soup = BeautifulSoup(html)
	conditions = soup.find("div", class_="conditions-status")
	status = conditions.find("div", class_="content")
	ready = status.find("h4").text
	info = status.find("p", class_="rcs-general-notice").text
	infoformatted = info.encode('ascii', 'ignore')

	datetime = (time.strftime("%d/%m/%Y %H:%M:%S"))

	with open('canaldata.csv', 'a') as csvfile:
		csvwriter = csv.writer(csvfile, delimiter="|")
		csvwriter.writerow([ready, infoformatted, datetime])


checkCanal();	