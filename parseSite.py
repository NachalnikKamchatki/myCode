from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import pandas as pd
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



url = 'http://planecrashinfo.com/1920/1920.htm'
list = []
soup = getHTML(url)
if soup == None:
    print('Invalid Data')
else:
    table = soup.find('table')
    # labels = table.find('tr').findAll('td')
    rows = table.findAll('tr')
    cells = []
    for row in rows:
        cells = row.findAll('td')
        rlist = [cell.text for cell in cells]
        list.append(rlist)
    print(list)
    df = pd.DataFrame(list)
    print(df)













