#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    May 16, 2021 10:59:21 AM EDT  platform: Windows NT

import sys
import mysql.connector
import diet
import meals

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
    clear()
    global rpantry
    rpantry = tk.StringVar()
    global hprotein
    hprotein = tk.IntVar()
    global hcarbs
    hcarbs = tk.IntVar()
    global hiron
    hiron = tk.IntVar()
    global hvit
    hvit = tk.IntVar()
    global hfat
    hfat = tk.IntVar()
    global lprotein
    lprotein = tk.IntVar()
    global lcarbs
    lcarbs = tk.IntVar()
    global liron
    liron = tk.IntVar()
    global lvit
    lvit = tk.IntVar()
    global lfat
    lfat = tk.IntVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def find():
    mycursor.execute("Create table IF NOT EXISTS diet_pantry(id INT, item varchar(200), quantity DEC(10,2), unit varchar(10), price DECIMAL(10,2), date varchar (20), quantity2 DEC(10,2), unit2 varchar(10))")
    nlist = getfood(select())
    for i in nlist:
        try:
            mycursor.execute("insert into diet_pantry select * from pantry where item ='" + i + "'")
        except mysql.connector.errors.ProgrammingError:
            pass
    mydb.commit()
    meals.create_Toplevel1(root)
    sys.stdout.flush()

def clear():
    mycursor.execute("drop table if exists diet_pantry")
    mydb.commit()

def pantry():
    rpantry.set(getfood(select()))
    sys.stdout.flush()

def track():
    diet.create_Toplevel1(root)
    sys.stdout.flush()

def select():
    nutrients = []
    vol = []
    
    if hprotein.get() == 1:
        nutrients.append('protein')
        vol.append('high')
    if hcarbs.get() == 1:
        nutrients.append('carbs')
        vol.append('high')
    if hiron.get() == 1:
        nutrients.append('iron')
        vol.append('high')   
    if hvit.get() == 1:
        nutrients.append('vitamin')
        vol.append('high')
    if hfat.get() == 1:
        nutrients.append('fat')
        vol.append('high')
    if lprotein.get() == 1:
        nutrients.append('protein')
        vol.append('low')
    if lcarbs.get() == 1:
        nutrients.append('carbs')
        vol.append('low')
    if liron.get() == 1:
        nutrients.append('iron')
        vol.append('low')
    if lvit.get() == 1:
        nutrients.append('vitamin')
        vol.append('low')   
    if lfat.get() == 1:
        nutrients.append('fat')
        vol.append('low')
    else:
        return([nutrients, vol])
    return [nutrients, vol]

def getfood(nList):
    flist = nList[0]
    vlist = nList[1]
    newList = []
    r = len(flist)
    for i in range(r):
        if flist[i] == 'protein' and vlist[i] == 'high':     
            statement = "select * from foods where protein > '15000'"
            mycursor.execute(statement)
            myfoods = mycursor.fetchall()
            for row in myfoods:
                newList.append(row[1])                
        elif flist[i] == 'protein' and vlist[i] == 'low':
            statement = "select * from foods where protein < '10000'"
            mycursor.execute(statement)
            myfoods = mycursor.fetchall()
            for row in myfoods:
                newList.append(row[1])
        elif flist[i] == 'carbs' and vlist[i] == 'high':
            statement = "select * from foods where carbohydrates > '50000'"
            mycursor.execute(statement)
            myfoods = mycursor.fetchall()
            for row in myfoods:
                newList.append(row[1])
        elif flist[i] == 'carbs' and vlist[i] == 'low':
            statement = "select * from foods where carbohydrates < '20000'"
            mycursor.execute(statement)
            myfoods = mycursor.fetchall()
            for row in myfoods:
                newList.append(row[1])
        elif flist[i] == 'iron' and vlist[i] == 'high':
            statement = "select * from foods where iron > '5'"
            mycursor.execute(statement)
            myfoods = mycursor.fetchall()
            for row in myfoods:
                newList.append(row[1])
        elif flist[i] == 'iron' and vlist[i] == 'low':
            statement = "select * from foods where iron < '0.5'"
            mycursor.execute(statement)
            myfoods = mycursor.fetchall()
            for row in myfoods:
                newList.append(row[1])
        elif flist[i] == 'vitamin' and vlist[i] == 'high':
            statement = "select * from foods where vitamin > '50'"
            mycursor.execute(statement)
            myfoods = mycursor.fetchall()
            for row in myfoods:
                newList.append(row[1])
        elif flist[i] == 'vitamin' and vlist[i] == 'low':
            statement = "select * from foods where vitamin < '10'"
            mycursor.execute(statement)
            myfoods = mycursor.fetchall()
            for row in myfoods:
                newList.append(row[1])
        elif flist[i] == 'fat' and vlist[i] == 'high':
            statement = "select * from foods where fat > '40000'"
            mycursor.execute(statement)
            myfoods = mycursor.fetchall()
            for row in myfoods:
                newList.append(row[1])
        elif flist[i] == 'fat' and vlist[i] == 'low':
            statement = "select * from foods where fat < '500'"
            mycursor.execute(statement)
            myfoods = mycursor.fetchall()
            for row in myfoods:
                newList.append(row[1])
        else:
            statement = "select * from pantry"
            mycursor.execute(statement)
            myfoods = mycursor.fetchall()
            for row in myfoods:
                newList.append(row[1])
        
    return newList

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import diets
    diets.vp_start_gui()




