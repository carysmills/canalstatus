from bs4 import BeautifulSoup  
import sched, time
import csv
from splinter import Browser

def checkCanal():
	with Browser("phantomjs") as browser:
	    browser.driver.set_window_size(1280, 1024)
	    browser.visit("http://ncc-ccn.gc.ca/rideau-canal-skateway")
	    html = browser.html

        soup = BeautifulSoup(html)
        conditions = soup.find("div", id="canal-conditions")
        readyText = soup.find("div", id="canal-header").find("h1").text

        if "partially open" in readyText:
            ready = "partially open"
        elif "open" in readyText:
            ready = "open"
        else:
            ready = "closed"


        info = conditions.find("p").text
        infoformatted = info.encode('ascii', 'ignore')
        datetime = (time.strftime("%d/%m/%Y %H:%M:%S"))
        
        with open('/var/www/canalstatus/canalstatus/canaldata.csv', 'a') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter="|")
            csvwriter.writerow([ready, infoformatted, datetime])
        
checkCanal();
