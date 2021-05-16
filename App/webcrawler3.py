import requests
from bs4 import BeautifulSoup
import mysql.connector

recipes = []

def meal_spider():
    mydb = mysql.connector.connect(host="localhost", user="root", password="pA$$123", database="khelperdb")
    mycursor = mydb.cursor()
    mycursor.execute("select * from urls")
    myresult = mycursor.fetchall()
        
    url = myresult[1][1]
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html.parser')
    
    for link in soup.findAll('p', {'class': 'more-from-category'}):
        for lin in link.findAll('a'):
             get_recipe(lin.get('href'))
    recipeList =(get_recipe2(recipes))
    
    return (recipeList)
       


def get_recipe(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html.parser')

    for link in soup.findAll('a', {'class': 'entry-title-link'}):
        recipes.append(link.get('href'))
    
def get_recipe2(lis):
    new_list = []
    for i in lis:
        ingredients = []
        dish = []
        method = []
        source_code = requests.get(i)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,'html.parser')
        for t in soup.findAll('h2', {'class':'tasty-recipes-title'}):
            dish.append(t.text.strip())
        for i in soup.findAll('div', {'class': 'tasty-recipes-ingredients-body'}):
            ingredients.append(i.ul.text.strip())
        for m in soup.findAll('div', {'class': 'tasty-recipes-instructions-body'}):
            try:
                method.append(m.ol.text.strip())
            except AttributeError:
                method.append(m.ul.text.strip())
        if (dish != [] and ingredients != [] and method != []):
            new_list.append([dish,ingredients,method])
    return(new_list) 

    


#meal_spider(1)
#get_recipe2([1,2])


