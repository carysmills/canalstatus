from bs4 import BeautifulSoup  
import sched, time
import csv
from selenium import webdriver

def checkCanal():
    url = "http://ncc-ccn.gc.ca/rideau-canal-skateway"
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    html = driver.page_source

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
