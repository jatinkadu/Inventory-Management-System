from tkinter import *
from PIL import Image,ImageTk
from employee import Employee_class
from supplier import Supplier_class
from product import productClass
from category import categoryClass
from sales import salesClass
import os
import login
import time
import sqlite3
from tkinter import messagebox

class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title(" Inventory Management System")
        self.root.config(bg = "White")
        #----------Title------------

        title = Label(self.root,text = "INVENTORY MANAGEMENT SYSTEM",font = ("Times new roman",40,"bold"),bg = "#010c48", fg = "White",anchor = "w" ,padx = 20 ).place(x = 0,y = 0,relwidth = 1,height = 70)

        #-----------Logout----------------

        button_logout = Button(self.root,text = "Logout",command = self.logout,font = ("Times new roman",15,"bold"),bg = "Yellow", cursor = "hand2").place(x = 1100,y = 10,width = 150,height = 50)

        #---------Clock---------------
 

        self.lbl_clock = Label(self.root,text = "Welcome to Inventory Management System \t \t DATE {str(date_)} \t\t Time: {str(time_)}",font = ("Times new roman",15),bg = "#4d636d", fg = "White" )
        self.lbl_clock.place(x = 0,y = 70,relwidth = 1,height = 30)

    #---------Left MEnu----------

        Left_menu = Frame(self.root,bd = 2,relief = RIDGE,bg = "White")
        Left_menu.place(x= 0,y = 102,width = 200,height = 565)
        Label_menu = Label(Left_menu,text = "Menu",height = 2,font = ("Times new roman",15),bg= "Black", fg ="White").pack(side = TOP,fill =X)
        
                   #-----------Buttons----------

        button_employee = Button(Left_menu,text = "Employee",height = 2 ,command = self.employee,font = ("Times new roman",20,"bold"),bg= "White",bd = 1,cursor = "hand2").pack(side = TOP,fill =X)
        button_supplier = Button(Left_menu,text = "Supplier",height = 2,command = self.supplier,font = ("Times new roman",20,"bold"),bg= "White",bd = 1,cursor = "hand2").pack(side = TOP,fill =X)
        button_category = Button(Left_menu,text = "Category",height = 2,command = self.category,font = ("Times new roman",20,"bold"),bg= "White",bd = 1,cursor = "hand2").pack(side = TOP,fill =X)
        button_product = Button(Left_menu,text = "Products",height = 2,command = self.product ,font = ("Times new roman",20,"bold"),bg= "White",bd = 1,cursor = "hand2").pack(side = TOP,fill =X)
        button_sales = Button(Left_menu,text = "Sales",height = 2,command = self.sales ,font = ("Times new roman",20,"bold"),bg= "White",bd = 1,cursor = "hand2").pack(side = TOP,fill =X)
        button_exit = Button(Left_menu,text = "Exit",height = 2,command = self.exit ,font = ("Times new roman",20,"bold"),bg= "White",bd = 1,cursor = "hand2").pack(side = TOP,fill =X)

        #-----------Footer-------------------

        Label_footer = Label(self.root,text = "Contact us : 98xxxxx",font = ("Times new roman",15),bg= "#010c48", fg ="White").pack(side = BOTTOM,fill =X)

        #-----------Blocks--------------------
       # self.employee_logo = Image.open("Python_Sem_Project/employee-icon.webp")
       # self.employee_logo = self.employee_logo.resize((300,150),Image.ANTIALIAS)
       # self.employee_logo = ImageTk.PhotoImage(self.employee_logo)
        self.lbl_employee = Label(self.root,text = "Total Employee\n [0]",font = ("Times new roman",15,"bold"),bg= "#33bbf9",bd = 1,relief = RIDGE,cursor = "hand2")
        self.lbl_employee.place(x=300,y=220,height = 150,width = 300 )

        self.lbl_supplier = Label(self.root,text = "Total Supplier\n [0]",font = ("Times new roman",15,"bold"),bg= "#ff5722",bd = 1,relief = RIDGE,cursor = "hand2")
        self.lbl_supplier.place(x=650,y=220,height = 150,width = 300 )

        self.lbl_category = Label(self.root,text = "Total Category\n [0]",font = ("Times new roman",15,"bold"),bg= "#009688",bd = 1,relief = RIDGE,cursor = "hand2")
        self.lbl_category.place(x=1000,y=220,height = 150,width = 300 )

        self.lbl_product = Label(self.root,text = "Total Product\n [0]",font = ("Times new roman",15,"bold"),bg= "#607d8b",bd = 1,relief = RIDGE,cursor = "hand2")
        self.lbl_product.place(x=300,y=400,height = 150,width = 300 )

        self.lbl_Sales = Label(self.root,text = "Total Sales\n [0]",font = ("Times new roman",15,"bold"),bg= "#ffc107",bd = 1,relief = RIDGE,cursor = "hand2")
        self.lbl_Sales.place(x=650,y=400,height = 150,width = 300 )

        self.update_content()
        
#-------------------------------------------------------------
    def employee(self):
        self.new_wind = Toplevel(self.root)
        self.new_obj = Employee_class(self.new_wind) 

#-------------------------------------------------------------
    def supplier(self):
        self.new_wind = Toplevel(self.root)
        self.new_obj = Supplier_class(self.new_wind) 

#-------------------------------------------------------------
    def category(self):
        self.new_wind = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_wind) 


#-------------------------------------------------------------
    def product(self):
        self.new_wind = Toplevel(self.root)
        self.new_obj = productClass(self.new_wind)

#-------------------------------------------------------------
    def sales(self):
        self.new_wind = Toplevel(self.root)
        self.new_obj = salesClass(self.new_wind)


#-------------------------------------------------------------
    def exit(self):
       self.root.destroy()

#-------------------------------------------------------------
    def logout(self):
        self.root.destroy()
        os.system("python login.py")

#--------------Update time-------------------------------

    def update_content(self):
        con = sqlite3.connect(database = r'test.db')
        cur = con.cursor()
        try:
            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f"Total Suppliers\n[ {str(len(supplier))} ]")
            
            
            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f"Total Category\n[ {str(len(category))} ]")
            
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f"Total Product\n[ {str(len(product))} ]")
        

            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f"Total Employee\n[ {str(len(employee))} ]")

        
            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%D-%M-%Y")
            self.lbl_clock.config(text=f"Welcome to Inventory Management System \t\t Date:{str(date_) }\t\t time:{str(time_) }")
            self.lbl_clock.after(200,self.update_content)

            bill=len(os.listdir('bill'))
            self.lbl_Sales.config(text=f'Total Sales [{str(bill)}]') 

            #==video 14 time:17:12min par aa ==bhai idhar time update karna hai so go in billing file 
            #=== copy paste  def update_date_time part ka below 
            #after cp call update_content function instead of  update_date_time      
        
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to:{str(ex)}",parent = self.root)
         


if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
