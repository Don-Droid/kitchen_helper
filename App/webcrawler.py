import requests
from bs4 import BeautifulSoup
import mysql.connector



def meal_spider():
    mydb = mysql.connector.connect(host="localhost", user="root", password="pA$$123", database="khelperdb")
    mycursor = mydb.cursor()
    mycursor.execute("select * from urls")
    myresult = mycursor.fetchall()
    
    recipes = []
    url = myresult[0][1]
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html.parser')
    for link in soup.findAll('a', {'class': 'button'}):
        href = myresult[0][2] + str(link.get('href'))
        if ('.com/' in href):
            recipes.append(get_recipe(href))
    return recipes


    
def get_recipe(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html.parser')
    ingredients = []
    method = []
    dish = []
    for x in soup.findAll('h1', {'class': 'recipeTitle'}):
        dish.append(x.string)
    for r in soup.findAll('div', {'class': 'recipeIngredients'}):
        ingredients.append(r.ul.text.strip())
    for d in soup.findAll('div', {'class': 'recipeDesc'}):
        method.append(d.ul.text.strip())
    return([dish,ingredients,method])


