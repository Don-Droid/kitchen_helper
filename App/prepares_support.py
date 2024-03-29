#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Apr 29, 2021 01:51:36 PM EDT  platform: Windows NT

import sys
import recipe_support
import json
import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(host="localhost", user="root", password="pA$$123", database="khelperdb")
mycursor = mydb.cursor()

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


def set_Tk_var():
    global pItems
    pItems = tk.StringVar()
    pItems.set(setter())
    global ingredients
    ingredients = tk.StringVar()
    ingredients = recipe_support.ingre
    global qty
    qty = tk.StringVar()
    qty.set('1')
    global unit
    unit = tk.StringVar()
    unit.set('unit')
    global method
    method = tk.StringVar()
    method = recipe_support.method
    global title
    title = tk.StringVar()
    title.set(recipe_support.title.get())
    global message
    message = tk.StringVar()
    

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def back():
    destroy_window()
    sys.stdout.flush()

def use():
    conList = convert(float(qty.get()),unit.get())
    quantity1 = conList[0]
    unit1 = conList[1]
    items = w.Scrolledlistbox3.get('active')
    state1 = ("select * from pantry where item = " + "'" + items + "' and unit2 = 'unit'")
    state2 = ("select * from pantry where item = " + "'" + items + "' and unit2 = 'oz'")
    if (unit1 == 'unit'):
        mycursor.execute(state1)
    else:
        mycursor.execute(state2)
    myresult = mycursor.fetchall()
    if myresult == []:
        message.set("Invalid Unit Selected")
    else:
        sunit = myresult[0][3]
        amountIn = float(myresult[0][6])
        balance = amountIn - quantity1
        message.set(qty.get()+ ' ' + unit.get() + ' of ' + items + ' taken from pantry')
        conList2 = convert2(float(balance),myresult[0][3])
        mycursor.execute("update pantry set quantity = " + str(conList2[0]) + ", quantity2 = " +  str(balance) + " where item = " + "'" + items + "'")
        mydb.commit()
        updateUsed(items, quantity1, myresult[0][7])
    sys.stdout.flush()

def convert(quan,unit):
    if (unit == 'tsp'):
        q = quan * 0.16667
        u = 'oz'
    elif unit == 'tbsp':
        q = quan * 0.5
        u = 'oz'
    elif unit == 'cup':
        q = quan * 8.11537
        u = 'oz'
    elif unit == 'oz':
        q = quan * 1
        u = 'oz'
    elif unit == 'pinch':
        q = quan * 0.013
        u = 'oz'
    elif unit == 'lb':
        q = quan * 16
        u = 'oz'
    elif unit == 'kg':
        q = quan * 35.274
        u = 'oz'
    elif unit == 'litre':
        q = quan * 33.814
        u = 'oz'
    elif (unit == 'unit'):
        q = quan * 1
        u = 'unit'
    else:
        u = 'Invalid Unit'
    return [q,u]

    
def convert2(quan, unit):
    if (unit == 'oz'):
        q = quan * 1
    elif unit == 'gram':
        q = quan * 28.3495
    elif unit == 'kg':
        q = quan * 0.0283495
    elif unit == 'lb':
        q = quan * 0.0625
    elif unit == 'ml':
        q = quan * 29.5735
    elif unit == 'litre':
        q = quan * 0.0295735
    elif unit == 'unit':
        q = quan * 1
    else:
        unit = 'Invalid Unit'
    return [q,unit]

def updateUsed (item,qty,unit):
    date = datetime.today().strftime('%d-%m-%Y')
    mycursor.execute("Create table IF NOT EXISTS food_used(id INT AUTO_INCREMENT PRIMARY KEY, item varchar(200), quantity DEC(10,5), unit varchar(10), date varchar (20))")
    sqlform = "Insert into food_used(item,quantity,unit,date) values(%s,%s,%s,%s)"
    entry = [item, qty, unit, date]
    mycursor.execute(sqlform, entry)
    mydb.commit()

def setter():
    newList = json.loads(recipe_support.lis[recipe_support.index][2])
    pItems = json.loads(recipe_support.lis[recipe_support.index][4])
    newList2 = []
    for i in newList:
        for p in pItems:
            if p in i or p.lower() in i or p.lower() in i.lower() or p in i.lower():
                newList2.append(p)
    return newList2

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import prepares
    prepares.vp_start_gui()




