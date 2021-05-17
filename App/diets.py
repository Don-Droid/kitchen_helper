#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    May 16, 2021 01:21:15 PM EDT  platform: Windows NT

import sys

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

import diets_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    diets_support.set_Tk_var()
    top = Toplevel1 (root)
    diets_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    diets_support.set_Tk_var()
    top = Toplevel1 (w)
    diets_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+380+100")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Diet")
        top.configure(background="#293250")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.037, rely=0.049, relheight=0.9, relwidth=0.925)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#293250")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Canvas1 = tk.Canvas(self.Frame1)
        self.Canvas1.place(relx=0.049, rely=0.054, relheight=0.891
                , relwidth=0.423)
        self.Canvas1.configure(background="#ffd55a")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")

        self.Checkbutton1 = tk.Checkbutton(self.Canvas1)
        self.Checkbutton1.place(relx=0.217, rely=0.028, relheight=0.069
                , relwidth=0.549)
        self.Checkbutton1.configure(activebackground="#ececec")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(anchor='w')
        self.Checkbutton1.configure(background="#ffd55a")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Checkbutton1.configure(foreground="#293250")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(selectcolor="#ffffff")
        self.Checkbutton1.configure(text='''High Protein''')
        self.Checkbutton1.configure(variable=diets_support.hprotein)

        self.Checkbutton1_1 = tk.Checkbutton(self.Canvas1)
        self.Checkbutton1_1.place(relx=0.217, rely=0.125, relheight=0.069
                , relwidth=0.549)
        self.Checkbutton1_1.configure(activebackground="#ececec")
        self.Checkbutton1_1.configure(activeforeground="#000000")
        self.Checkbutton1_1.configure(anchor='w')
        self.Checkbutton1_1.configure(background="#ffd55a")
        self.Checkbutton1_1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1_1.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Checkbutton1_1.configure(foreground="#293250")
        self.Checkbutton1_1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1_1.configure(highlightcolor="black")
        self.Checkbutton1_1.configure(justify='left')
        self.Checkbutton1_1.configure(selectcolor="#ffffff")
        self.Checkbutton1_1.configure(text='''High Carbs''')
        self.Checkbutton1_1.configure(variable=diets_support.hcarbs)

        self.Checkbutton1_2 = tk.Checkbutton(self.Canvas1)
        self.Checkbutton1_2.place(relx=0.217, rely=0.222, relheight=0.069
                , relwidth=0.549)
        self.Checkbutton1_2.configure(activebackground="#ececec")
        self.Checkbutton1_2.configure(activeforeground="#000000")
        self.Checkbutton1_2.configure(anchor='w')
        self.Checkbutton1_2.configure(background="#ffd55a")
        self.Checkbutton1_2.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1_2.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Checkbutton1_2.configure(foreground="#293250")
        self.Checkbutton1_2.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1_2.configure(highlightcolor="black")
        self.Checkbutton1_2.configure(justify='left')
        self.Checkbutton1_2.configure(selectcolor="#ffffff")
        self.Checkbutton1_2.configure(text='''High Iron''')
        self.Checkbutton1_2.configure(variable=diets_support.hiron)

        self.Checkbutton1_3 = tk.Checkbutton(self.Canvas1)
        self.Checkbutton1_3.place(relx=0.217, rely=0.319, relheight=0.069
                , relwidth=0.66)
        self.Checkbutton1_3.configure(activebackground="#ececec")
        self.Checkbutton1_3.configure(activeforeground="#000000")
        self.Checkbutton1_3.configure(anchor='w')
        self.Checkbutton1_3.configure(background="#ffd55a")
        self.Checkbutton1_3.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1_3.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Checkbutton1_3.configure(foreground="#293250")
        self.Checkbutton1_3.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1_3.configure(highlightcolor="black")
        self.Checkbutton1_3.configure(justify='left')
        self.Checkbutton1_3.configure(selectcolor="#ffffff")
        self.Checkbutton1_3.configure(text='''High Vitamin C''')
        self.Checkbutton1_3.configure(variable=diets_support.hvit)

        self.Checkbutton1_4 = tk.Checkbutton(self.Canvas1)
        self.Checkbutton1_4.place(relx=0.217, rely=0.416, relheight=0.069
                , relwidth=0.549)
        self.Checkbutton1_4.configure(activebackground="#ececec")
        self.Checkbutton1_4.configure(activeforeground="#000000")
        self.Checkbutton1_4.configure(anchor='w')
        self.Checkbutton1_4.configure(background="#ffd55a")
        self.Checkbutton1_4.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1_4.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Checkbutton1_4.configure(foreground="#293250")
        self.Checkbutton1_4.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1_4.configure(highlightcolor="black")
        self.Checkbutton1_4.configure(justify='left')
        self.Checkbutton1_4.configure(selectcolor="#ffffff")
        self.Checkbutton1_4.configure(text='''High Fat''')
        self.Checkbutton1_4.configure(variable=diets_support.hfat)

        self.Checkbutton1_5 = tk.Checkbutton(self.Canvas1)
        self.Checkbutton1_5.place(relx=0.217, rely=0.512, relheight=0.069
                , relwidth=0.549)
        self.Checkbutton1_5.configure(activebackground="#ececec")
        self.Checkbutton1_5.configure(activeforeground="#000000")
        self.Checkbutton1_5.configure(anchor='w')
        self.Checkbutton1_5.configure(background="#ffd55a")
        self.Checkbutton1_5.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1_5.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Checkbutton1_5.configure(foreground="#293250")
        self.Checkbutton1_5.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1_5.configure(highlightcolor="black")
        self.Checkbutton1_5.configure(justify='left')
        self.Checkbutton1_5.configure(selectcolor="#ffffff")
        self.Checkbutton1_5.configure(text='''Low Protein''')
        self.Checkbutton1_5.configure(variable=diets_support.lprotein)

        self.Checkbutton1_6 = tk.Checkbutton(self.Canvas1)
        self.Checkbutton1_6.place(relx=0.217, rely=0.609, relheight=0.069
                , relwidth=0.549)
        self.Checkbutton1_6.configure(activebackground="#ececec")
        self.Checkbutton1_6.configure(activeforeground="#000000")
        self.Checkbutton1_6.configure(anchor='w')
        self.Checkbutton1_6.configure(background="#ffd55a")
        self.Checkbutton1_6.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1_6.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Checkbutton1_6.configure(foreground="#293250")
        self.Checkbutton1_6.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1_6.configure(highlightcolor="black")
        self.Checkbutton1_6.configure(justify='left')
        self.Checkbutton1_6.configure(selectcolor="#ffffff")
        self.Checkbutton1_6.configure(text='''Low Carbs''')
        self.Checkbutton1_6.configure(variable=diets_support.lcarbs)

        self.Checkbutton1_7 = tk.Checkbutton(self.Canvas1)
        self.Checkbutton1_7.place(relx=0.217, rely=0.706, relheight=0.069
                , relwidth=0.549)
        self.Checkbutton1_7.configure(activebackground="#ececec")
        self.Checkbutton1_7.configure(activeforeground="#000000")
        self.Checkbutton1_7.configure(anchor='w')
        self.Checkbutton1_7.configure(background="#ffd55a")
        self.Checkbutton1_7.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1_7.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Checkbutton1_7.configure(foreground="#293250")
        self.Checkbutton1_7.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1_7.configure(highlightcolor="black")
        self.Checkbutton1_7.configure(justify='left')
        self.Checkbutton1_7.configure(selectcolor="#ffffff")
        self.Checkbutton1_7.configure(text='''Low Iron''')
        self.Checkbutton1_7.configure(variable=diets_support.liron)

        self.Checkbutton1_8 = tk.Checkbutton(self.Canvas1)
        self.Checkbutton1_8.place(relx=0.217, rely=0.803, relheight=0.069
                , relwidth=0.604)
        self.Checkbutton1_8.configure(activebackground="#ececec")
        self.Checkbutton1_8.configure(activeforeground="#000000")
        self.Checkbutton1_8.configure(anchor='w')
        self.Checkbutton1_8.configure(background="#ffd55a")
        self.Checkbutton1_8.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1_8.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Checkbutton1_8.configure(foreground="#293250")
        self.Checkbutton1_8.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1_8.configure(highlightcolor="black")
        self.Checkbutton1_8.configure(justify='left')
        self.Checkbutton1_8.configure(selectcolor="#ffffff")
        self.Checkbutton1_8.configure(text='''Low Vitamin C''')
        self.Checkbutton1_8.configure(variable=diets_support.lvit)

        self.Checkbutton1_9 = tk.Checkbutton(self.Canvas1)
        self.Checkbutton1_9.place(relx=0.217, rely=0.9, relheight=0.069
                , relwidth=0.549)
        self.Checkbutton1_9.configure(activebackground="#ececec")
        self.Checkbutton1_9.configure(activeforeground="#000000")
        self.Checkbutton1_9.configure(anchor='w')
        self.Checkbutton1_9.configure(background="#ffd55a")
        self.Checkbutton1_9.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1_9.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Checkbutton1_9.configure(foreground="#293250")
        self.Checkbutton1_9.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1_9.configure(highlightcolor="black")
        self.Checkbutton1_9.configure(justify='left')
        self.Checkbutton1_9.configure(selectcolor="#ffffff")
        self.Checkbutton1_9.configure(text='''Low Fat''')
        self.Checkbutton1_9.configure(variable=diets_support.lfat)

        self.Button1_1 = tk.Button(self.Frame1)
        self.Button1_1.place(relx=0.53, rely=0.054, height=45, width=235)
        self.Button1_1.configure(activebackground="#ececec")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#6dd47e")
        self.Button1_1.configure(command=diets_support.find)
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Button1_1.configure(foreground="#293250")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Find Recipe''')

        self.Button1_1_1 = tk.Button(self.Frame1)
        self.Button1_1_1.place(relx=0.53, rely=0.21, height=45, width=235)
        self.Button1_1_1.configure(activebackground="#ececec")
        self.Button1_1_1.configure(activeforeground="#000000")
        self.Button1_1_1.configure(background="#6dd47e")
        self.Button1_1_1.configure(command=diets_support.track)
        self.Button1_1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1_1.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Button1_1_1.configure(foreground="#293250")
        self.Button1_1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1_1.configure(highlightcolor="black")
        self.Button1_1_1.configure(pady="0")
        self.Button1_1_1.configure(text='''Track Diet''')

        self.Button1_2 = tk.Button(self.Frame1)
        self.Button1_2.place(relx=0.53, rely=0.365, height=45, width=235)
        self.Button1_2.configure(activebackground="#ececec")
        self.Button1_2.configure(activeforeground="#000000")
        self.Button1_2.configure(background="#6dd47e")
        self.Button1_2.configure(command=diets_support.pantry)
        self.Button1_2.configure(disabledforeground="#a3a3a3")
        self.Button1_2.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Button1_2.configure(foreground="#293250")
        self.Button1_2.configure(highlightbackground="#d9d9d9")
        self.Button1_2.configure(highlightcolor="black")
        self.Button1_2.configure(pady="0")
        self.Button1_2.configure(text='''Recommendation''')

        self.Scrolledlistbox1 = ScrolledListBox(self.Frame1)
        self.Scrolledlistbox1.place(relx=0.53, rely=0.585, relheight=0.358
                , relwidth=0.423)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(cursor="xterm")
        self.Scrolledlistbox1.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox1.configure(font="TkFixedFont")
        self.Scrolledlistbox1.configure(foreground="black")
        self.Scrolledlistbox1.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="blue")
        self.Scrolledlistbox1.configure(selectforeground="white")
        self.Scrolledlistbox1.configure(listvariable=diets_support.rpantry)

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.53, rely=0.523, height=21, width=235)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#293250")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Recommended Items''')

    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = tk.Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#ececec")
        Popupmenu1.configure(activeborderwidth="1")
        Popupmenu1.configure(activeforeground="#000000")
        Popupmenu1.configure(background="#d9d9d9")
        Popupmenu1.configure(borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3")
        Popupmenu1.configure(foreground="#000000")
        Popupmenu1.add_command(
                label="NewCommand")
        Popupmenu1.post(event.x_root, event.y_root)

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Listbox widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)
    def size_(self):
        sz = tk.Listbox.size(self)
        return sz

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





