from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np

def getHTML(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
    except AttributeError as e:
        return None
    return bs

def parseFatalities(str = None):
    my_list = []
    b = re.compile(r"(\d+)/(\d+)\((\d+)\)")
    my_tuple = re.findall(b, str)
    try:
        my_list = " ".join(my_tuple[0]).split(' ')
    except IndexError:
        pass
    return my_list
def get_page(count_first=1, count_last=2):

    # gets two parameters
    #
    # first param count_first
    #
    # second param count_last
    #
    # returns a pandas's data frame

    list = []
    for i in range(count_first, count_last + 1):
        url = 'http://planecrashinfo.com/' + str(i) + '/' + str(i) + '.htm'
        soup = getHTML(url)
        if soup == None:
            print('Invalid Data')
        else:
            table = soup.find('table')
            rows = table.findAll('tr')
            cells = []
            for row in rows:
                cells = row.findAll('td')
                rlist = [cell.text for cell in cells]
                common = rlist[:3] + parseFatalities(rlist[3])
                list.append(common)
    labels = ['Date', 'Location / Operator', 'Aircraft Type / Registration', 'Fatalities', 'Cruew', 'Zero']
    df = pd.DataFrame(list[1:], columns = labels)
    return df


print(get_page(1920, 2018))













