from selenium import webdriver
from bs4 import BeautifulSoup
import time


#driver = webdriver.PhantomJS()
#driver.set_window_size(1200, 1600)
url = 'https://sjipiao.fliggy.com/flight_search_result.htm?_input_charset=utf-8&spm=181.7091613.a1z67.1001&searchBy=1280&tripType=0&depCityName=%E9%95%BF%E6%98%A5&depCity=&depDate=2018-01-13&arrCityName=%E6%98%86%E6%98%8E&arrCity=KMG&arrDate='

#def parser_html():
#    strq = u'来自飞猪\n'
#    driver.get(url)
#    time.sleep(2)
#    html = driver.page_source
#    soup = BeautifulSoup(html,'html.parser')

#    for item in soup.select('.flight-list-item'):
#        name = item.select('.J_line')[0].text
#        begin_time = item.select('.flight-time-deptime')[0].text
#        price = item.select('.J_FlightListPrice')[0].text
#        strq += name+" - "+price+" $ "+u" 起飞时间"+begin_time
#        strq +='\n'
#    driver.quit()
#    return strq

def load_html(url):
     try:
        driver = webdriver.PhantomJS()
        driver.set_window_size(1200, 1600)
        driver.get(url)
        time.sleep(2)
        return driver.page_source
     finally:
        driver.quit()
#虽然目前这两个函数分离开了，但是应该是没有分离开的必要。这里这里增加了复杂度，待改进

def load_massage(url):
    massage = []
    soup = BeautifulSoup(load_html(url),"html.parser")
    for item in soup.select('.flight-list-item'):
        name = item.select('.J_line')[0].text
        begin_time = item.select('.flight-time-deptime')[0].text
        price = item.select('.J_FlightListPrice')[0].text
        massage.append( name+" - "+price+" $ "+u" 起飞时间"+begin_time)
    return "\n".join(massage)


#if __name__ =='__main__':
#    print(parser_html())




