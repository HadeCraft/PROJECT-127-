from bs4 import BeautifulSoup
import requests
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome()
browser.get(START_URL)

def scrape():
    headers = ["V Mag.(mV)","Proper name","Bayer designation","Distance(ly)","Spectral class","Mass (M☉)","Radius (R☉)","Luminosity (L☉)"]
    its_an_empty_list = []

    for i in range(0,428):
        with open("SCRAPER.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(its_an_empty_list
    
scrape()