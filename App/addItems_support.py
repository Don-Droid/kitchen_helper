#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Apr 05, 2021 01:55:15 PM EDT  platform: Windows NT

import sys
import os
import mysql.connector
import ypantry
import ypantry_support
from datetime import datetime

mydb = mysql.connector.connect(host="localhost", user="root", password="pA$$123", database="khelperdb")


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
    global item
    item = tk.StringVar()
    global qty
    qty = tk.StringVar()
    qty.set('qty')
    global price
    price = tk.StringVar()
    global unit
    unit = tk.StringVar()
    unit.set('unit')
    global message
    message = tk.StringVar()
    message.set('')

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def add():
    item1 = item.get()
    qty1 = qty.get()
    unit1 = unit.get()
    price1 = price.get()
    date1 = datetime.today().strftime('%d-%m-%Y')

    regex = "!@#$%^*()_+1234567890<>/\}{;:.,~`[]|?= "
    regex2 = "!@#$%^*()_+abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ<>/\}{;:,~`[]|?= "

    legit = 0
    error=""
    if item1 != "" and containsAny(item1,regex) == 0:
        legit += 1
    else:
        error = "Invalid Item"
    if qty1 != "" and containsAny(qty1,regex2) == 0:
        legit += 1
        qty1 = float(qty1)
    else:
        error = "Invalid Quantity" 
    if price1 != "" and containsAny(price1,regex2) == 0:
        legit += 1
        price1 = float(price1)
    else:
        error = "Invalid Price"
    if (legit == 3):
        if (mydb):
            mycursor = mydb.cursor()
            mycursor.execute("Create table IF NOT EXISTS pantry(id INT AUTO_INCREMENT PRIMARY KEY, item varchar(200), quantity DEC(10,2), unit varchar(10), price DECIMAL(10,2), date varchar (20), quantity2 DEC(10,2), unit2 varchar(10))")
            sqlform = "Insert into pantry(item,quantity,unit,price,date,quantity2,unit2) values(%s,%s,%s,%s,%s,%s,%s)"
            con = converter(unit1, qty1)
            qty2 = con[0]
            unit2 = con[1]
            entry = [item1, qty1, unit1, price1, date1, qty2, unit2]
            mycursor.execute(sqlform, entry)
            mydb.commit()
            msg = item1 + ' was added to your pantry'
            message.set(msg)
            item.set("")
            qty.set("")
            unit.set("")
            price.set("")
    else:
        message.set('No Item was added, ' + error)
    sys.stdout.flush()

def converter(unit, q):
    if (unit == 'ml'):
        q = (q * 0.0338)
        unit = "oz"
    elif (unit == 'litre'):
        q = (q * 33.814)
        unit = "oz"
    elif(unit == 'kg'):
        q = (q * 35.275)
        unit = "oz"
    elif (unit == 'gram'):
        q = (q * 0.035274)
        unit = "oz"
    elif (unit == 'lb'):
        q = (q * 16)
        unit = "oz"
    elif (unit == 'oz'):
        q = (q * 1)
        unit = "oz"
    else:
        q = (q * 1)
        unit = "unit"
    return(q,unit)
        
    
        

#regex
def containsAny(string, regex):
    for i in regex:
        if i in string: return 1
    return 0

def clear():
    item.set("")
    qty.set("")
    unit.set("")
    price.set('')
    message.set('')
    sys.stdout.flush()

def back():
    ypantry.create_Toplevel1(root)
    

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import addItems
    addItems.vp_start_gui()

