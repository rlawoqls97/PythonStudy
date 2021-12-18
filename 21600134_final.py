from tkinter import *
import tkinter
from tkinter.filedialog import *
from tkinter import messagebox
from tkinter.scrolledtext import *
import tkinter.font as tkFont
import os.path
from tkinter import ttk
from functools import partial

root = Tk()
root.title("MEMO")
name_label = ttk.Label(root, text="File name: ")
pass_label = ttk.Label(root, text="Password: ")
def NewFile():
    srt.delete('1.0', 'end')
    srt.config(foreground="black")
    srt.configure(font=("Courier", 11))
    srt2.delete('1.0', 'end')
    srt2.config(foreground="black")
    srt2.configure(font=('Courier', 11))

ch = "{:'}'"
def OpenFile():
    global rl_n
    NewFile()
    try:
        name = askopenfilename()
        name_s = name.split(".")
        if os.path.isfile(name_s[0] + ".code"):
            inf2 = open(name_s[0] + ".code")
            rl = inf2.readline()
            rl_n = rl
            rl2 = ''.join( x for x in rl if x not in ch)
            rl_s = rl2.split('  ')
            inf = open(name, 'r')
            f = inf.read()
            name_label.config(text="File name: " + name)
            srt.insert(END, f)
            srt.configure(font=("Courier", 11))
            inf.close()
        else:
            messagebox.showerror("error", "No .code file")
    except Exception as err:
        messagebox.showerror("error", err)
        
def SaveFile():
    saveFilename = asksaveasfilename()
    
    try:
        outf = open(saveFilename, 'w')
        outf.write(srt2.get('1.0', 'end'))
        outf.close()
    except IOError as err:
        messagebox.showerror("error", err)



button = Button(root, text="New", fg="black", command=NewFile) 
button.pack(side=TOP, padx=10)

button1 = Button(root, text="Open", fg="black", command=OpenFile) 
button1.pack(side=TOP, padx=10)

button2 = Button(root, text="Save", fg="black", command=SaveFile) 
button2.pack(side=TOP, padx=10)

name_label = ttk.Label(root, text="File name: ")
name_label.pack()

srt = ScrolledText(root)
srt.pack()

pass_label = ttk.Label(root, text="Password: ")
pass_label.pack()

password = ''
entry = Entry(root)
entry.pack()
def Decode():
    try:
        passw = str(entry.get())
        encrypted_secret_codes = rl_n
        encrypted_secret_codes = encrypted_secret_codes.replace("{", "").replace("}", "").replace(":", "").replace(",", "").split(" ")
        print("Step1")
        print(rl_n)
        key2codes = 0
        for p in passw:
            key2codes += ord(p)

        key =[]
        value = []
        for i in range(len(encrypted_secret_codes)):
            encrypted_secret_codes[i] = int((encrypted_secret_codes[i])) - key2codes
            if i % 2 != 0:
                value.append(encrypted_secret_codes[i])
            else:
                key.append(chr(encrypted_secret_codes[i]))

        print("Step2")
        print(encrypted_secret_codes)
        print("Step3")
        secret_code = dict(zip(value, key))
        print(secret_code)

        decrypt = srt.get('1.0', 'end')
        dec_l = decrypt.split(",")

        coded_text = ''
        for c in dec_l:
            if c != '\n':
                coded_text += str(secret_code[int(c)])

        srt2.insert(END, coded_text)
    except IOError as err:
        messagebox.showerror("error", err)
button3 = Button(root, text="Decode", fg="black", command= Decode)
button3.pack()

srt2 = ScrolledText(root)
srt2.pack()


def FindIndex(a):
    cnt = 0
    if int(a) == 11:
        cnt = 0
    elif int(a) == 13:
        cnt = 1
    elif int(a) == 15:
        cnt = 2
    elif int(a) == 17:
        cnt = 3
    elif int(a) == 19:
        cnt = 4
    elif int(a) == 21:
        cnt = 5
    elif int(a) == 23:
        cnt = 6
    elif int(a) == 25:
        cnt = 7
    elif int(a) == 27:
        cnt = 8
    elif int(a) == 29:
        cnt = 9
    elif int(a) == 31:
        cnt = 10
    return cnt



def About():
    messagebox.showinfo('About', "이 프로그램은 텍스트를 입력할 수 있는 프로그램입니다.")

font = tkFont.Font(size= 11)   
menubar = Menu(root)
root.config(menu= menubar)
filemenu = Menu(menubar)
aboutmenu = Menu(menubar)
menubar.add_cascade(label= "File", menu= filemenu)
filemenu.add_command(label= "New", command=NewFile)
filemenu.add_command(label= "Open", command=OpenFile)
filemenu.add_command(label= "Save", command=SaveFile)
filemenu.add_separator()
filemenu.add_command(label= "Exit", command=root.destroy)
menubar.add_cascade(label= "About", menu=aboutmenu)
aboutmenu.add_command(label= "Info", command=About)



mainloop()