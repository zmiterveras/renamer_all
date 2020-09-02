#!/usr/bin/env python3
"""
Переименновывает файлы в заданном каталоге, предустановленным способом
"""
import os, sys
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo, showwarning

def scrolledtext(info):
    def close_scroll():
        parent.destroy()
        showinfo('Info', 'Rename complete')
        
    parent = Toplevel()
    fr = Frame(parent)
    fr.pack()
    tx = Text(fr)
    tx.config(bg='#808080', font=14)
    scr = Scrollbar(fr, command=tx.yview)
    tx.config(yscrollcommand=scr.set)
    tx.pack(side=LEFT)
    scr.pack(side=RIGHT)
    for i in info:
        tx.insert(END, i + '\n')
    Button(parent, text='Ok', command=close_scroll).pack()
    

def renamer(dirname, count, name):
    info = []
    for (thisDir, subsHere, filesHere) in os.walk(dirname):
        for file in filesHere:
            figure = (4 - len(count))*'0' + count
            old = os.path.join(thisDir, file)
            resent, ext = os.path.splitext(file)
            if name != '':
                file = name + '_'  + figure  + ext
            else:
                file = figure + ext
            new = os.path.join(thisDir, file)
            os.renames(old, new)
            count = str(1 + int(figure))
            info.append((resent + ext + ' => ' + file))
    scrolledtext(info)
    
    
def quiry():
    def onFetch(dirname):
            count = ent1.get()
            name = ent2.get()
            if count == '':
                showwarning('Предупреждение', 'Не введен номер')
            else:
                try:
                    int(count)
                except ValueError:
                    showwarning('Предупреждение', 'Некорректно введен номер')
                else:
                    renamer(dirname, count, name)
                    add_win.destroy()
                    
    def add_win_close():
        add_win.destroy()
    
    dirname = askdirectory()
    add_win = Toplevel(root)
    new = ()
    add_win.title('Ввод значений')
    add_win.geometry('+300+300')
    Label(add_win, text='Номер').grid(row=0, column=0)
    Label(add_win, text='Имя').grid(row=0, column=1)
    ent1 = Entry(add_win, bd=2, width=4)
    ent1.grid(row=1, column=0)
    ent1.insert(0, '')
    ent2 = Entry(add_win, bd=2, width=20)
    ent2.grid(row=1, column=1)
    ent2.insert(0, '')
    Button(add_win, text='OK', bd=2, command=lambda: onFetch(dirname)).grid(row=2, column=0)
    Button(add_win, text='Отмена', bd=2, command=lambda:add_win_close()).grid(row=2,  column=1)
    add_win.focus_set()
    add_win.grab_set()
    add_win.wait_window()
    return new
    
def onHelp():
    showinfo('О программе', 'Переименновывает файлы в заданном каталоге,\nпредустановленным способом: имя_номер')
    
root = Tk()
root.geometry('400x315+300+300')
root.title('Renamer')
m = Menu(root)
root.config(menu=m)
fm = Menu(m)
m.add_cascade(label='Файл', menu=fm)
fm.add_command(label='Переименовать', command=quiry)
fm.add_command(label='Закрыть', command=root.destroy)
hm = Menu(m)
m.add_cascade(label='?', menu=hm)
hm.add_command(label='О ...', command=onHelp)
img = PhotoImage(file='renamer.png')
Label(root, image=img).pack()
Button(root, text='Переименовать', command=quiry).pack()
Button(root, text='Close', command=root.destroy).pack()
root.mainloop()

    
       