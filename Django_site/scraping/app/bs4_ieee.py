import chromedriver_binary
from bs4 import BeautifulSoup
from .webDriver import page
import pandas as pd

def search(url):
    html = page(url)
    soup = BeautifulSoup(html, 'html.parser')
    elems = soup.find_all("div",class_='col result-item-align')
    key = soup.find("div",class_="Breadcrumb-collection js-collection Breadcrumb-collection-inline")
    key = key.text if key else None
    data = []
    for e in elems:
        h = e.find("h2",class_='text-md-md-lh')
        a = h.find("a") if h else None
        if a:
            href = a.get("href")
            url = "https://ieeexplore.ieee.org%s"%str(href)
            title = a.text
        else:
            title = None
        y = e.find("div",class_="publisher-info-container")
        y = y.find("span") if y else None
        year = y.text.split(':')[1] if y else None
        auth = e.find("p")
        auth = auth.text if auth else None
        data.append([url,year,auth,title])
    return key, data

def download(data,file):
    header = [['url','year','authors','title','','key word:',data[0]]]
    df = pd.DataFrame(header)
    df.to_csv(file,header=False,index=False)
    df = pd.DataFrame(data[1])
    df.to_csv(file,mode='a',header=False,index=False)

if __name__ == '__main__':
    url = 'https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=generative%20adversarial%20network&highlight=true&returnType=SEARCH&matchPubs=true&rowsPerPage=100&returnFacets=ALL&sortType=newest'

    key, data = search(url)
    print(len(data))
    for i in data:
        print(*i,sep='\n')

    download([key, data],'Reference_list.csv')


