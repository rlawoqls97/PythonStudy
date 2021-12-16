from tkinter import *
from tkinter import scrolledtext
from tkinter.filedialog import *
from tkinter import messagebox
from tkinter.scrolledtext import *
import tkinter.font as tkFont
import os.path



root = Tk()
root.title("MEMO")
srt = ScrolledText(root, width=50, height=10)
srt.pack()

from tkinter.colorchooser import *
def callback():
    global res
    res = askcolor(title = "Color chooser")
    res = res[1]
    srt.config(foreground=res)
    button.config(fg=res)
    
button = Button(root, text="Choose Color", fg="black", command=callback) 
button.pack(side=LEFT, padx=10)


def sized(e):
    srt.configure(font=("Courier", sizevar.get()))
    sizevar.get()


from tkinter import ttk
size_label = ttk.Label(root, text="Choose Size")
size_label.pack()

sizevar = StringVar()
size = ttk.Combobox(textvariable=sizevar)
size.bind('<<ComboboxSelected>>', sized)
size['values'] = (11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31)
size.current(0)
size.pack()

ch = "{:'}'"

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

def NewFile():
    srt.delete('1.0', 'end')
    srt.config(foreground="black")
    srt.configure(font=("Courier", 11))
    size.current(0)
    button.config(fg="black")

def OpenFile():
    NewFile()
    try:
        name = askopenfilename()
        name_s = name.split(".")
        if os.path.isfile(name_s[0] + ".edit"):
            inf2 = open(name_s[0] + ".edit")
            rl = inf2.readline()
            rl = ''.join( x for x in rl if x not in ch)
            rl_s = rl.split('  ')
            inf3 = open(name, 'r')
            f2 = inf3.read()
            srt.insert(END, f2)
            srt.configure(font=("Courier", int(rl_s[1])))
            srt['fg'] = rl_s[0]
            ind = FindIndex(int(rl_s[1]))
            size.current(ind)
            button.config(fg=rl_s[0])
            inf2.close()
        else:
            inf = open(name, 'r')
            f = inf.read()
            srt.insert(END, f)
            srt.configure(font=("Courier", 11))
            inf.close()
    except Exception as err:
        messagebox.showerror("error", err)

def SaveFile():
    saveFilename = asksaveasfilename()
    if ".edit" in saveFilename:
        messagebox.showerror("error", ".edit은 확장자명으로 사용할 수 없습니다.")
    else:
        try:
            outf = open(saveFilename, 'w')
            outf.write(srt.get('1.0', 'end'))
            outf.close()
            saveFilename_s = saveFilename.split(".")
            outf2 = open(saveFilename_s[0] + ".edit", 'w')
            outf2.write('{' + srt['fg'] + ' : ' + sizevar.get() + '}')
            outf2.close()
        except IOError as err:
            messagebox.showerror("error", err)


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
