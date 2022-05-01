from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

def page(url):
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=opts)
    driver.get(url)
    
    # time.sleepが少ないとhtmlを読み取れないことがある
    time.sleep(5)
    html = driver.page_source.encode('utf-8')
    driver.quit()
    return html

if __name__ == '__main__':
    import chromedriver_binary
    from bs4 import BeautifulSoup

    url = 'https://ieeexplore.ieee.org'
    html = page(url)
    soup = BeautifulSoup(html, 'html.parser')
    p = soup.find('p').text
    print(p)
