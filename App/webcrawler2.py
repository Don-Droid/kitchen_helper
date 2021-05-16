import requests
from bs4 import BeautifulSoup
import mysql.connector



def meal_spider():
    mydb = mysql.connector.connect(host="localhost", user="root", password="pA$$123", database="khelperdb")
    mycursor = mydb.cursor()
    mycursor.execute("select * from urls")
    myresult = mycursor.fetchall()
    recipes = []
    recipesLinks = []
    url = myresult[2][1]
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html.parser')
    for link in soup.findAll('a', {'class': 'card__titleLink manual-link-behavior'}):
        href = link.get('href')
        recipesLinks.append(href)
    for i, element in enumerate(recipesLinks):
        if(i % 2 == 0):
            recipes.append(get_recipe(element))
    return (recipes)
    
    
    
def get_recipe(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html.parser')
    ingredients = []
    ing = ""
    met = ""
    method = []
    dish = []
    for link in soup.findAll('ul', {'class': 'ingredients-section'}):
        for lin in link.findAll('span', {'class':'ingredients-item-name'}):
            ing = (ing + lin.text + '\n')
        ingredients.append(ing)    
    for lin in soup.findAll('h1', {'class':'headline heading-content'}):
        dish.append(lin.text)
    for lin in soup.findAll('div', {'class':'paragraph'}):
        met = met + lin.text
    method.append(met)
    
    return([dish,ingredients,method])


