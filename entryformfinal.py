from csv import *
from tkinter import *
from tkinter import messagebox
import os
import random

window=Tk()
window.configure(bg = "lightblue")
window.title("Data Entry")
window.geometry("700x350")
main_lst=[]






for i in range(50):
    window.columnconfigure(i, weight=1)
    window.rowconfigure(i, weight=1)

def Save():
   num=random.random()
   x=round(num,7)
   x=10000000*x
   lst=[name.get(),age.get(),contact.get(),address.get(),collagename.get(),Department.get(),x]
   main_lst.append(lst)
   messagebox.showinfo("Information","The data has been added successfully")
   
   messagebox.showinfo("Unique Token No",x )
   
   
   with open("data_entry.csv","w") as file:
      Writer=writer(file)
      Writer.writerow(["Name","Age","Contact","Address","Collage Name","Department","Token Number"])
      Writer.writerows(main_lst)
      messagebox.showinfo("Information","Saved Succesfully")

def Clear():
   name.delete(0,END)
   age.delete(0,END)
   contact.delete(0,END)
   address.delete(0,END)
   collagename.delete(0,END)
   Department.set("")




# Headding level

# Create a heading label
heading_label = Label(window, text="Data Entry project By GROUP 6", font=("italicbold", 20),activebackground="lightblue", bg="lightblue", fg="black")

# Center the alignment of the heading label
heading_label.grid(row=0,column = 25, padx= 20, pady=10)


# 3 labels, 4 buttons,3 entry fields
label1=Label(window,text="Name: ",padx=10,pady=10,background="lightblue",foreground="black")
label2=Label(window,text="Age: ",padx=10,pady=10,background="lightblue",foreground="black")
label3=Label(window,text="Contact: ",padx=10,pady=10,background="lightblue",foreground="black")
label31=Label(window,text="Address:",padx=10,pady=11,background="lightblue",foreground="black")
label4=Label(window,text="Collage name: ",padx=10,pady=10,background="lightblue",foreground="black")
label5=Label(window,text="Department: ",padx=10,pady=10,background="lightblue",foreground="black")


name=Entry(window,width=30,borderwidth=3)
age=Entry(window,width=30,borderwidth=3)
contact=Entry(window,width=30,borderwidth=3)
address = Entry(window,width = 30 , borderwidth = 4)
collagename=Entry(window,width=30,borderwidth=3)



# Department = Entry(window,width = 30,borderwidth = 3)
Department = StringVar(window)
Department.set("Select Your Department")
drop_menu = OptionMenu(window, Department,"Computer Science and Engineering(CSE)", "Information Technology(IT)","Electronics and Communication Engineering(ECE)","Electrical Engineering(EE)","Artificial Intelligence and Machine Learning(AI&ML)")
#drop.pack()



save=Button(window,text="Save",font="Arial 12",padx=7,pady=5,background="Blue",foreground="White",command=Save)
#add=Button(window,text="Add",font="Arial 12",padx=7,pady=5,background="Blue",foreground="White",command=Add)
clear=Button(window,text="Clear",font = "Arial 12",padx=7,pady=5,background="Blue",foreground="White",command=Clear)
Exit=Button(window,text="Exit",font="Arial 12",padx=7,pady=5,background="red",foreground="White",command=window.quit)

label1.grid(row=10,column=24)
label2.grid(row=12,column=24)
label3.grid(row=14,column=24)
label31.grid(row=16,column=24)
label4.grid(row =18, column=24)
label5.grid(row = 20,column=24)

name.grid(row=10,column=25)
age.grid(row=12,column=25)
contact.grid(row=14,column=25)
address.grid(row=16,column=25)
collagename.grid(row=18,column=25)
drop_menu.grid(row=20,column=25)
save.grid(row=25,column=26,columnspan=2)
clear.grid(row=26,column=26,columnspan=2)
Exit.grid(row=26,column=25,columnspan=2)
def Add_detail():
    pass 
def DataFile():
    os.startfile("data_entry.csv")
    pass 

menubar = Menu(window)
 
# ManuBar 1 :
filemenu = Menu(menubar, tearoff = 2)
menubar.add_cascade(label = 'Options', menu = filemenu)
#filemenu.add_command(label = "Add details", command = Add)
filemenu.add_command(label = "Open the data  file", command = DataFile)

window.config(menu=menubar)

window.mainloop()
print(list)
print(main_lst)