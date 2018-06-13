from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import pandas as pd

# dfldfldkf

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
    labels = table.find('tr').findAll('td')
    rows = table.findAll('tr')
    cells = []
    for row in rows:
        cells = row.findAll('td')
        list.append(cells)


 






    #     for i in range(len(cells)):
    #         lst.append(cells[i].text)
    # print(lst)




    # table_headers = soup.find('table', {'id' : 'giftList'}).find('tr').findAll('th')
    # for header in table_headers:
    #     print(header.get_text())


    # df.to_csv('plcrash.csv')


    # try:
    #     with open('aircr.csv', 'w', newline = '') as file:
    #         csv_writer = csv.writer(file)
    #         for item in lst:
    #             csv_writer.writerow([item])
    # except ValueError:
    #     print('!!!')
    # finally:
    #     file.close()



