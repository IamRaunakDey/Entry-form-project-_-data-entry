from csv import *
from tkinter import *
from tkinter import messagebox

window=Tk()
window.configure(bg = "White")
window.title("Data Entry")
window.geometry("700x350")
main_lst=[]



for i in range(50):
    window.columnconfigure(i, weight=1)
    window.rowconfigure(i, weight=1)

def Add():
   lst=[name.get(),age.get(),contact.get(),address.get(),Department.get()]
   main_lst.append(lst)
   messagebox.showinfo("Information","The data has been added successfully")

def Save():
   with open("data_entry.csv","w") as file:
      Writer=writer(file)
      Writer.writerow(["Name","Age","Contact","Address","Department"])
      Writer.writerows(main_lst)
      messagebox.showinfo("Information","Saved succesfully")

def Clear():
   name.delete(0,END)
   age.delete(0,END)
   contact.delete(0,END)
   address.delete(0,END)
   Department.set("")

# 3 labels, 4 buttons,3 entry fields
label1=Label(window,text="Name: ",padx=39,pady=10,background="white",foreground="black")
label2=Label(window,text="Age: ",padx=43.9,pady=10,background="white",foreground="black")
label3=Label(window,text="Contact: ",padx=34,pady=10,background="white",foreground="black")
label4=Label(window,text="Address: ",padx=34,pady=10,background="white",foreground="black")
label5=Label(window,text="Department: ",padx=23.4,pady=10,background="white",foreground="black")





name=Entry(window,width=30,borderwidth=3)
age=Entry(window,width=30,borderwidth=3)
contact=Entry(window,width=30,borderwidth=3)
address = Entry(window,width = 30 , borderwidth = 4)
# Department = Entry(window,width = 30,borderwidth = 3)
Department = StringVar(window)
Department.set("Select Your Department")
drop_menu = OptionMenu(window, Department,"Computer Science and Engineering", "Information Technology","Python","JavaScript","Rust","GoLang")
#drop.pack()

save=Button(window,text="Save",font="Arial 12",padx=15,pady=5,background="Blue",foreground="White",command=Save)
add=Button(window,text="Add",font="Arial 12",padx=15,pady=5,background="Blue",foreground="White",command=Add)
clear=Button(window,text="Clear",font = "Arial 12",padx=15,pady=5,background="Blue",foreground="White",command=Clear)
Exit=Button(window,text="Exit",font="Arial 12",padx=15,pady=5,background="Blue",foreground="White",command=window.quit)

label1.grid(row=0,column=20)
label2.grid(row=1,column=20)
label3.grid(row=2,column=20)
label4.grid(row =3, column=20)
label5.grid(row = 4,column=20)

name.grid(row=0,column=25)
age.grid(row=1,column=25)
contact.grid(row=2,column=25)
address.grid(row=3,column=25)
drop_menu.grid(row=4,column=25)
save.grid(row=14,column=27,columnspan=2)
add.grid(row=14,column=25,columnspan=2)
clear.grid(row=18,column=27,columnspan=2)
Exit.grid(row=18,column=25,columnspan=2)


window.mainloop()
print(list)
print(main_lst)



