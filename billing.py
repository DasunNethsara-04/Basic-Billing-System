#imports
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import datetime

#main UI
root = Tk()
root.title('Tech SARA LK Billing System')
root.geometry('1520x1024+30+70')
root.config(bg='black')
root.resizable(0, 0)
img = PhotoImage(file='logo.png')
root.iconphoto(False, img)

msg1 = 'Tech SARA LK Billing System'

msg2 = '''Thank you for choosing our Software for your Shop. 

Faced any trouble? Contact the Programmer.

Name\t\t- Dasun Nethsara
Email\t\t- techsaralk.pro@gmail.com
Telegram\t\t- https://t.me/techsara_lk
'''

#functions
def getTime():
	date = datetime.date.today().strftime('%d.%m.%Y')
	time = datetime.datetime.now().strftime('%I:%M:%S %p')
	lbl.config(text=date)
	timelbl.config(text=time)
	lbl.after(1000, getTime)

def calc():
	try:
		a = entry1.get()
		b = entry2.get()
		c = entry3.get()
		d = entry4.get()
		e = entry5.get()
		f = entry6.get()
		g = entry7.get()
		h = entry8.get()
		i = entry9.get()
		j = entry10.get()
		
		if a == '':
			entry1.insert(0, '0')
		if b == '':
			entry2.insert(0, '0')
		if c == '':
			entry3.insert(0, '0')
		if d == '':
			entry4.insert(0, '0')
		if e == '':
			entry5.insert(0, '0')
		if f == '':
			entry6.insert(0, '0')
		if g == '':
			entry7.insert(0, '0')
		if h == '':
			entry8.insert(0, '0')
		if i == '':
			entry9.insert(0, '0')
		if j == '':
			entry10.insert(0, '0')
		
		a = int(entry1.get())
		b = int(entry2.get())
		c = int(entry3.get())
		d = int(entry4.get())
		e = int(entry5.get())
		f = int(entry6.get())
		g = int(entry7.get())
		h = int(entry8.get())
		i = int(entry9.get())
		j = int(entry10.get())
		
		rs = str((a * 15) + (b * 35) + (c * 20) + (d * 35) + (e * 20) + (f * 55) + (g * 45) + (h * 15) + (i * 30) + (j * 100))
		bill_lbl.config(text=f'Rs.{rs}/=')
		messagebox.showinfo('Done', 'Bill Calculated')
		
	except:
		messagebox.showerror('Error', 'An Error Occerrd!')
		pass

def clear():
	en1.set('')
	en2.set('')
	en3.set('')
	en4.set('')
	en5.set('')
	en6.set('')
	en7.set('')
	en8.set('')
	en9.set('')
	en10.set('')

def help1():
	global msg, img, msg2
	win = Toplevel(root)
	win.title('Get Help')
	win.config(bg='black')
	win.geometry('500x430+530+400')
	win.iconphoto(False, img)
	win.resizable(0, 0)
	Label(win, image=img, bd=0).pack(pady=5)
	Label(win, text=msg1, justify='left', font=('Calibri', 30, 'bold'), fg='white', bg='black').pack()
	Label(win, text=msg2, justify='left', font=('Calibri', 15, 'bold'), fg='white', bg='black').pack(pady=20)
	Button(win, text='Close', font='Times 15', bd=0, fg='white', bg='red', command=win.destroy, width=7).place(x=400, y=380)
	win.mainloop()
	
#Important variables
en1 = StringVar()
en2 = StringVar() 
en3 = StringVar() 
en4 = StringVar() 
en5 = StringVar() 
en6 = StringVar() 
en7 = StringVar() 
en8 = StringVar() 
en9 = StringVar() 
en10 = StringVar() 

#header
Label(root, text='Tech SARA LK Billing System', font=('Calibri', 60), bg='#306ad8',fg='white').pack(side=TOP, fill=X)
frm = Frame(root, height=100, bg='black')
frm.place(x=0, y=110, width=2224)

lbl = Label(frm, font=('DS-Digital', 75), fg='red', bg='black')
lbl.place(x=50, y=0)

img = Image.open('logo.png')
img = img.resize((120, 120))
img = ImageTk.PhotoImage(img)
Label(root, image=img, bd=0).pack(pady=5)

timelbl = Label(frm, font=('DS-Digital', 75), fg='red', bg='black')
timelbl.place(x=1030, y=0)


#Frames
frm1 = Frame(root, width=450, height=650, bg='#62dd7d')
frm1.place(x=60, y=270)
frm2 = Frame(root, width=450, height=650, bg='#848fe1')
frm2.place(x=540, y=270)
frm3 = Frame(root, width=450, height=650, bg='#e28385')
frm3.place(x=1020, y=270)


#############################################  frm1   ############################################
Label(frm1, text='MENU', font=('Agency FB', 30, 'underline bold'), bg='#62dd7d').place(x=180, y=10)

Label(frm1, text='Bun\t-\tRs.15/=', font=('Lucida Calligraphy', 20), bg='#62dd7d').place(x=10, y=100)
Label(frm1, text='Pastery\t-\tRs.35/=', font=('Lucida Calligraphy', 20), bg='#62dd7d').place(x=10, y=150)
Label(frm1, text='Roll\t-\tRs.20/=', font=('Lucida Calligraphy', 20), bg='#62dd7d').place(x=10, y=200)
Label(frm1, text='Biscuits\t-\tRs.35/=', font=('Lucida Calligraphy', 20), bg='#62dd7d').place(x=10, y=250)
Label(frm1, text='Tea Cake\t-\tRs.20/=', font=('Lucida Calligraphy', 20), bg='#62dd7d').place(x=10, y=300)
Label(frm1, text='Bread\t-\tRs.55/=', font=('Lucida Calligraphy', 20), bg='#62dd7d').place(x=10, y=350)
Label(frm1, text='Cookies\t-\tRs.45/=', font=('Lucida Calligraphy', 20), bg='#62dd7d').place(x=10, y=400)
Label(frm1, text='Plain Tea\t-\tRs.15/=', font=('Lucida Calligraphy', 20), bg='#62dd7d').place(x=10, y=450)
Label(frm1, text='Tea\t-\tRs.30/=', font=('Lucida Calligraphy', 20), bg='#62dd7d').place(x=10, y=500)
Label(frm1, text='Coffee\t-\tRs.100/=', font=('Lucida Calligraphy', 20), bg='#62dd7d').place(x=10, y=550)


#############################################  frm2   ############################################
Label(frm2, text='Billing Area', font=('Agency FB', 30, 'underline bold'), bg='#848fe1').place(x=150, y=10)

Label(frm2, text='Bun', font=('Calibri', 20), bg='#848fe1').place(x=10, y=100)
Label(frm2, text='Pastery', font=('Calibri', 20), bg='#848fe1').place(x=10, y=150)
Label(frm2, text='Roll', font=('Calibri', 20), bg='#848fe1').place(x=10, y=200)
Label(frm2, text='Biscuits', font=('Calibri', 20), bg='#848fe1').place(x=10, y=250)
Label(frm2, text='Tea Cake', font=('Calibri', 20), bg='#848fe1').place(x=10, y=300)
Label(frm2, text='Bread', font=('Calibri', 20), bg='#848fe1').place(x=10, y=350)
Label(frm2, text='Cookies', font=('Calibri', 20), bg='#848fe1').place(x=10, y=400)
Label(frm2, text='Plain Tea', font=('Calibri', 20), bg='#848fe1').place(x=10, y=450)
Label(frm2, text='Tea', font=('Calibri', 20), bg='#848fe1').place(x=10, y=500)
Label(frm2, text='Coffee', font=('Calibri', 20), bg='#848fe1').place(x=10, y=550)

entry1 = Entry(frm2, bd=1, font=('Times', 18, 'bold'), justify='center', textvariable=en1)
entry1.place(x=160, y=100)
entry2 = Entry(frm2, bd=1, font=('Times', 18, 'bold'), justify='center', textvariable=en2)
entry2.place(x=160, y=150)
entry3 = Entry(frm2, bd=1, font=('Times', 18, 'bold'), justify='center', textvariable=en3)
entry3.place(x=160, y=200)
entry4 = Entry(frm2, bd=1, font=('Times', 18, 'bold'), justify='center', textvariable=en4)
entry4.place(x=160, y=250)
entry5 = Entry(frm2, bd=1, font=('Times', 18, 'bold'), justify='center', textvariable=en5)
entry5.place(x=160, y=300)
entry6 = Entry(frm2, bd=1, font=('Times', 18, 'bold'), justify='center', textvariable=en6)
entry6.place(x=160, y=350) 
entry7 = Entry(frm2, bd=1, font=('Times', 18, 'bold'), justify='center', textvariable=en7)
entry7.place(x=160, y=400)
entry8 = Entry(frm2, bd=1, font=('Times', 18, 'bold'), justify='center', textvariable=en8)
entry8.place(x=160, y=450)
entry9 = Entry(frm2, bd=1, font=('Times', 18, 'bold'), justify='center', textvariable=en9)
entry9.place(x=160, y=500)
entry10 = Entry(frm2, bd=1, font=('Times', 18, 'bold'), justify='center', textvariable=en10)
entry10.place(x=160, y=550)


#############################################  frm3   ############################################
Label(frm3, text='Total', font=('Agency FB', 30, 'underline bold'), bg='#e28385').place(x=195, y=10)

bill_lbl = Label(frm3, text='', bg='#e28385', font=('Calibri', 60, 'bold'))
bill_lbl.place(x=80, y=250)

Button(root, text='Help', font=('Calibri', 25), bg='#34d8e0', fg='white', bd=0, width=10, command=help1).place(x=150, y=940)
Button(root, text='Calculate', font=('Calibri', 25), bg='#dd3769', fg='white', bd=0, width=10, command=calc).place(x=540, y=940)
Button(root, text='Clear', font=('Calibri', 25), bg='#e7df7c', fg='white', bd=0, width=10, command=clear).place(x=815, y=940)
Button(root, text='Close', font=('Calibri', 25), bg='#ff0000', fg='white', bd=0, width=10, command=root.destroy).place(x=1200, y=940)


getTime()






root.mainloop()