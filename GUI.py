

import tkinter as tk

def get_entry():
    value=name.get()
    if value:
        print(value)
    else:
        print('Empty Entry')

def delete_entry():
    name.delete(0)
# def say_hello():
#     print('Hello')
#
#
# def add_label():
#     label = tk.Label(win, text='new', font=('Arial', 14, 'bold'))
#     label.pack()
#
#
# def counter():
#     global count
#     count += 1
#     btn4['text'] = f'Counter:{count}'


# count = 0


win = tk.Tk()
win.title('My 1st GUI')
photo = tk.PhotoImage(file='funny-1.png')
win.iconphoto(False, photo)
win.config(bg='#DEDBE4')
win.geometry('400x400+700+400')
win.minsize(300, 400)
win.maxsize(700, 800)

tk.Label(win,text='Name:').grid(row=0,column=1, stick='w')
tk.Label(win,text='Password:').grid(row=1,column=0, stick='w')
name=tk.Entry(win)
password = tk.Entry(win, show = '*')
name.grid(row=0,column=1)
password.grid(row=1, column=1)

tk.Button(win,text='get', command=get_entry).grid(row=2, column =0, stick='we' )
tk.Button(win,text='delete', command=delete_entry).grid(row=2, column =1, stick='we' )
tk.Button(win,text='insert', command=lambda: name.insert(1,'hello'))\
    .grid(row=2, column =2, stick='we' )

# win.resizable(True, True)  # if will be False , False you can not move window's size left -right up and down
# btn1 = tk.Button(win, text='Hello',
#                  command=say_hello
#                  )
# btn2 = tk.Button(win, text='Add new label',
#                  command=add_label
#                  )
# btn3 = tk.Button(win, text='Add new label lambda',
#                  command=lambda: tk.Label(win, text='new lambda').pack()
#                  )
# btn4 = tk.Button(win, text='Counter: {count}',
#                  command=counter,
#                  activebackground='blue',
#                  bg='gray',
#                  state=tk.NORMAL
#                  )
# btn5 = tk.Button(win, text='space')
# btn6 = tk.Button(win, text='shift')
#
# btn1.grid(row=0, column=0)
# btn2.grid(row=0, column=1)
# btn3.grid(row=1, column=0)
# btn4.grid(row=1, column=1)
# btn5.grid(row=2,column=0, columnspan=2, stick='we')
# btn6.grid(row=0,column=3, rowspan=3, stick='ns')

win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)

win.mainloop()
