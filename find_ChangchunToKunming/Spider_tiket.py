from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS()
driver.set_window_size(1200, 1600)

url = u'https://sjipiao.fliggy.com/flight_search_result.htm?_input_charset=utf-8&\
spm=181.7091613.a1z67.1001&searchBy=1280&tripType=0&depCityName=%E9%95%BF%E6%98%A5&depCity\
=&depDate=2017-07-14&arrCityName=%E6%98%86%E6%98%8E&arrCity=&arrDate='


def parser_html():
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    for item in soup.select('.flight-list-item'):
        name = item.select('.J_line')
        begin_time = item.select('.flight-time-deptime')
        price = item.select('.J_FlightListPrice')
        return (name+price+begin_time)
