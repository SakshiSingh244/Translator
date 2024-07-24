from tkinter import *
from tkinter import ttk
from googletrans import Translator , LANGUAGES 

def change(text="type", src="English",dest="Hindi"):
           text1 = text
           src1 = src
           dest1 = dest
           trans= Translator()
           trans1 = trans.translate(text,src=src1,dest=dest1)
           return trans1.text

def data():
            s = comb_sor.get()
            d = comb_dest.get()
            masg = Sor_txt.get(1.0,END)
            textget = change(text = masg, src = s, dest = d)
            dest_txt.delete(1.0 , END)
            dest_txt.insert(END, textget)
            

root = Tk()
root.title("Lets Translate")
root.geometry("500x700")
root.config(bg='black')

lab_txt = Label(root, text="Hey, User", font=("Times New Roman", 20, "bold"), bg="white")
lab_txt.place(x=100,y=40,height=55,width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root, text="Source Text", font=("Times New Roman", 15, "bold"), fg="blue")
lab_txt.place(x=100,y=110,height=35,width=300)

Sor_txt = Text(frame,font=("Time New Roman",10,"bold"),wrap=WORD)
Sor_txt.place(x=10,y=160,height=170,width=480)

list_text = list(LANGUAGES.values())

comb_sor =ttk.Combobox(frame,value=list_text)
comb_sor.place(x=10,y=350,height=30,width=150)
comb_sor.set("English")

button_change = Button(frame,text="Translate",relief=RAISED,command = data)
button_change.place(x=170,y=350,height=30,width=150)


comb_dest =ttk.Combobox(frame,value=list_text)
comb_dest.place(x=330,y=350,height=30,width=150)
comb_dest.set("English")

lab_txt = Label(root, text="Dest Text", font=("Times New Roman", 15, "bold"), fg="blue")
lab_txt.place(x=100,y=400,height=35,width=300)

dest_txt = Text(frame,font=("Time New Roman",10,"bold"),wrap=WORD)
dest_txt.place(x=10,y=450,height=170,width=480)


root.mainloop()