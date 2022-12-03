from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

def getproducts(word, page):
    productlist = []
    url = f'https://www.myntra.com/{word}?p={page}'
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, 'lxml')
    for element in soup.findAll('li', attrs={'class': 'product-base'}):
        try:
            link = element.find('a')['href']
            category = link.split('/')[0]
        except Exception as e:
            category = None
        #For products which don't have a rating, otherwise code would take the next span tag which is size    
        rating = element.find('span').text
        if rating[0] == 'U':
            rating = None
        
        product = {            
        'pname' : element.find('h4', attrs={'class':'product-product'}).text,
        'prating': rating,
        'pcategory': category    
        }
        
    
        productlist.append(product)
           
    return category, productlist

total_productlist = []
for x in range(1, 5):
    category, productlist = getproducts('shoes', x)
    total_productlist.append(productlist)
    
#print(total_productlist)

search_term = "Sneakers"
selected_product = []
for element in productlist:
    if search_term in element['pname']:
        selected_product.append(element)

#print(selected_product)

df = pd.DataFrame(selected_product)
df.to_csv('sneakers.csv', index=False)
df = pd.DataFrame(total_productlist)
df.to_csv('shoes.csv',index=False )

print('fin')

