from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os
class salesClass:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("INVENTORY MANAGEMENT SYSTEM | Devloped by Royce,Jatin,Darsh")
        self.root.config(bg="white")
        self.root.focus_force()
        self.var_invoice=StringVar() #invoice no variable
        self.bill_list=[] #to store invoice no
        #title
        lbl_title=Label(self.root,text="View Customer Bill",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)

        
        lbl_invoice=Label(self.root,text="Invoice no",font=("times new roman",15),bg="white").place(x=50,y=100)
        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("times new roman",15),bg="lightyellow").place(x=160,y=100,width=180,height=28)#taking variable invoice number
        btn_search=Button(self.root,text="Search",command=self.search,font=("times new roman",15),bg="Red",cursor="hand2").place(x=360,y=100,width=180,height=28)#search button
        btn_clear=Button(self.root,text="Clear",command=self.Clear,font=("times new roman",15),bg="green",cursor="hand2").place(x=550,y=100,width=180,height=28) #clear button
        
        #===============BILL LIST======================#
        sales_frame=Frame(self.root,bd=3,relief=RIDGE) #creation of frame
        sales_frame.place(x=50,y=150,width=200,height=330) #placing the frame

        scrolly=Scrollbar(sales_frame,orient=VERTICAL) #scrollbar creation
        self.sales_list=Listbox(sales_frame,font=("goudy old style",15),bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y) #packing of scrollbar
        scrolly.config(command=self.sales_list.yview()) #configuration of scroll bar
        self.sales_list.pack(fill=BOTH,expand=1)
        self.sales_list.bind("<ButtonRelease-1>",self.get_data) #binding the fuction with sales_list

        #=============BILLING AREA=========#
        bill_frame=Frame(self.root,bd=3,relief=RIDGE) #creation of frame
        bill_frame.place(x=280,y=140,width=400,height=330) #placing the frame

        lbl_bill_title=Label(bill_frame,text=" Customer Bill",font=("goudy old style",20),bg="ORANGE").pack(side=TOP,fill=X)

        scrolly2=Scrollbar(bill_frame,orient=VERTICAL) #scrollbar creation
        self.bill_area=Text(bill_frame,bg="lightyellow",yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y) #packing of scrollbar

        scrolly2.config(command=self.bill_area.yview()) #configuration of scroll bar
        self.bill_area.pack(fill=BOTH,expand=1)
        #=======================IMAGE=============#

        self.bill_photo=Image.open("images/cat2.jpg") #open the image with Image.open("path")
        self.bill_photo=self.bill_photo.resize((450,400),Image.ANTIALIAS) #resize the image as its too big and Antialias doesnt alter the clarity
        self.bill_photo=ImageTk.PhotoImage(self.bill_photo)

        lbl_image=Label(self.root,image=self.bill_photo,bd=0)
        lbl_image.place(x=750,y=120)

        self.show()

#=====================================================================#

    def show(self): #fuction to extract the files from bill folder and check for txt files
        del self.bill_list[:]
        self.sales_list.delete(0,END)
        for i in os.listdir('bill'):
            if i.split('.')[-1]=='txt':
                self.sales_list.insert(END,i)
                self.bill_list.append(i.split('.')[0])#appending the split filename

# =====================Get Data==========================#


    def get_data(self,ev): #to get the name of the selcted file 
        index_=self.sales_list.curselection()
        file_name=self.sales_list.get(index_)
        #print(file_name)
        self.bill_area.delete('1.0',END) #to delete previously opened bill
        fp=open(f'bill/{file_name}','r') #open file with the given path and format is readable
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()

# =====================Search==========================#


    def search(self): #to search using filename
       if self.var_invoice.get()=="":
           messagebox.showerror("error","invoice no required",parent=self.root)
       else:
           if self.var_invoice.get() in self.bill_list:
                fp=open(f'bill_area/{self.var_invoice.get()}.txt','r') #open file with the given path and format is readable
                self.bill_area.delete('1.0',END) #cleaning the bill area to aviod overwrite
                for i in fp:
                    self.bill_area.insert(END,i) #to show the bill file in bill_area
                fp.close()
           else:
               messagebox.showerror("error","invallid invoice no",parent=self.root)
   
# =====================Clear==========================#
     
    def Clear(self):
        self.show()
        self.bill_area.delete('1.0',END)
if __name__=="__main__":
    root=Tk()
    obj=salesClass(root)
    root.mainloop()
    