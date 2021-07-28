import requests 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options




def formatclassname(listeClass):
    return '.'.join(str(e) for e in listeClass)

def filterWeb(driver,kpi,count,num):
    liste = formatclassname(kpi["class"])
    try:
        for i in range(count):
            driver.find_elements_by_class_name(liste)[num].click()
    except:
        return False
    else:
        return driver

def getKpi(driver, classKpi,className,num,time):
    tab = driver.find_elements_by_class_name("h7vnx2-2.bFpGkc.cmc-table>tbody")[0]
    row =  tab.find_elements_by_tag_name("tr")
    listeName = []
    listeKpi = []
    for i in range(10):
        cellKpi =  row[i].find_elements_by_class_name(formatclassname(classKpi["class"]))
        nameKpi = row[i].find_element_by_class_name(formatclassname(className["class"]))
        listeName.append(nameKpi.text)
        listeKpi.append(cellKpi[num].text)
     
    return  {
        "time" : time,
        "name": listeName,
        "kpi": listeKpi 
    }

def lauchDriver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
    return driver

def kpi24h():
    
    driver = lauchDriver()
    buttonDay = {"class" : ["gDYBnF","sc-1eb5slv-0"]}
    classKpi={"class":["sc-15yy2pl-0"]}
    className={"class":["sc-1eb5slv-0","iJjGCS"]}
    url = 'https://coinmarketcap.com/'
    driver.get(url)
    driver = filterWeb(driver,buttonDay,1,3)
    liste = getKpi(driver, classKpi,className,0,"24h")
    return liste

def kpi7j():
    driver = lauchDriver()
    buttonDay = {"class" : ["gDYBnF","sc-1eb5slv-0"]}
    classKpi={"class":["sc-15yy2pl-0"]}
    className={"class":["sc-1eb5slv-0","iJjGCS"]}
    url = 'https://coinmarketcap.com/'
    driver.get(url)
    driver = filterWeb(driver,buttonDay,1,4)
    liste = getKpi(driver, classKpi,className,1,"7d")
    return liste

def top10Kpi(time):
    driver = lauchDriver()
    buttonDay = {"class" : ["gDYBnF","sc-1eb5slv-0"]}
    classKpi={"class":["sc-15yy2pl-0"]}
    className={"class":["sc-1eb5slv-0","iJjGCS"]}
    url = 'https://coinmarketcap.com/'
    driver.get(url)
    listeBetter = {}
    listeWorst = {}
    if(time=="24h"):
        driver = filterWeb(driver,buttonDay,1,3)
        listeBetter = getKpi(driver, classKpi,className,0,time)
        driver = filterWeb(driver,buttonDay,1,3)
        listeWorst= getKpi(driver, classKpi,className,0,time)
    elif(time=="7d"):
        driver = filterWeb(driver,buttonDay,1,4)
        listeBetter = getKpi(driver, classKpi,className,1,time)
        driver = filterWeb(driver,buttonDay,1,4)
        listeWorst = getKpi(driver, classKpi,className,1,time)
    return {
        "Better": listeBetter,
        "Worst" : listeWorst
    }







# html_text = requests.get(url).text
# soup = BeautifulSoup(html_text,'html.parser')
# print(soup.title)