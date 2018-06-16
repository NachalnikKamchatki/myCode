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

url = 'http://planecrashinfo.com/1920/1920.htm'
list = []
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
    print(list)
    labels = ['Date', 'Location / Operator', 'Aircraft Type / Registration', 'Fatalities', 'Cruew', 'Zero']
    df = pd.DataFrame(list[1:], columns = labels)
    print(df)


print(parseFatalities('5/2(0)'))










