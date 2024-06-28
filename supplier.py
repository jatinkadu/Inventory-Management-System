from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class Supplier_class:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title(" Inventory Management System")
        self.root.config(bg = "White")
        self.root.focus_force()

        #-------------------------
        #-------All Variable-----------

        self.var_searchby = StringVar()
        self.var_searchtext = StringVar()

        self.var_supp_invoice = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()

   #----------Search Frame------------
        #--------option--------

        lbl_Search = Label(self.root,text = "Invoice no.",bg = "white",font = ("goudy old style",15,"bold"))
        lbl_Search.place(x = 700, y= 80)

        text_search = Entry(self.root,textvariable = self.var_searchtext,font =("Goudy old style",15), bg = "Light yellow").place(x = 810,y = 80, width = 160)
        btn_search = Button(self.root,text = "Search",command = self.search ,font =("Goudy old style",15), bg = "Green",cursor = "hand2").place(x = 980,y = 80,width = 100,height = 28)

       #----------details--------------

        title = Label(self.root,text = "Manage Supplier Details",font =("Goudy old style",20,"bold"), bg = "#0f4d7d",fg = "white").place(x = 50,y = 10,width = 1000,height = 40)

      #------Content------------------

      #------------row 1-------------

        lbl_supplier_invoice = Label(self.root,text = "Invoice No.",font =("Goudy old style",15), bg = "white").place(x = 50,y = 80) 
        txt_supplier_invoice = Entry(self.root,textvariable =self.var_supp_invoice,font =("Goudy old style",15), bg = "light yellow").place(x = 180,y = 80,width = 180) 

      #------------row 2-------------

        lbl_name   = Label(self.root,text = "Name",font =("Goudy old style",15), bg = "white").place(x = 50,y = 120) 
        txt_name    = Entry(self.root,textvariable = self.var_name,font =("Goudy old style",15), bg = "light yellow").place(x = 180,y = 120,width = 180) 
       
      #------------row 3-------------

        lbl_contact = Label(self.root,text = "Contact",font =("Goudy old style",15), bg = "white").place(x = 50,y = 160) 
        txt_contact = Entry(self.root,textvariable = self.var_contact,font =("Goudy old style",15), bg = "light yellow").place(x = 180,y = 160,width = 180) 
       
      #------------row 4-------------

        lbl_text_desc  = Label(self.root,text = "Description",font =("Goudy old style",15), bg = "white").place(x = 50,y = 200) 
        self.text_desc = Text(self.root,font =("Goudy old style",15), bg = "light yellow")
        self.text_desc.place(x = 180,y = 200,width = 470,height = 120) 
        
#----------Buttons--------------

        btn_add = Button(self.root,text = "Save",command = self.add,font =("Goudy old style",15), bg = "#2196f3",cursor = "hand2").place(x = 180,y = 370,width = 110,height = 35)
        btn_update = Button(self.root,text = "Update",command = self.update,font =("Goudy old style",15), bg = "#4caf50",cursor = "hand2").place(x = 300,y = 370,width = 110,height = 35)
        btn_delete = Button(self.root,text = "Delete",command = self.delete,font =("Goudy old style",15), bg = "#f44336",cursor = "hand2").place(x = 420,y = 370,width = 110,height = 35)
        btn_clear = Button(self.root,text = "Clear",command = self.clear,font =("Goudy old style",15), bg = "#607d8b",cursor = "hand2").place(x = 540,y = 370,width = 110,height = 35)
    
#----------Employee Details--------------

        emp_frame = Frame(self.root, bd = 3,relief = RIDGE)
        emp_frame.place(x = 700,y = 120,width = 380,height = 350) 

        scrolly = Scrollbar(emp_frame,orient = VERTICAL)
        scrollx = Scrollbar(emp_frame,orient = HORIZONTAL)

        self.SupplierTable = ttk.Treeview(emp_frame,columns= ("Invoice","Name","Contact","Description"),yscrollcommand = scrolly.set,xscrollcommand = scrollx.set )
        scrollx.pack(side = BOTTOM,fill = X)
        scrolly.pack(side = RIGHT,fill = Y)
        scrollx.config(command = self.SupplierTable.xview)
        scrolly.config(command = self.SupplierTable.yview)

       
        self.SupplierTable.heading("Invoice",text = "Invoice No.")
        self.SupplierTable.heading("Name",text = "Name")
        self.SupplierTable.heading("Contact",text = "Contact")
        self.SupplierTable.heading("Description",text = "Description")
        self.SupplierTable["show"] = "headings"
        self.SupplierTable.pack(fill = BOTH,expand = 1)


        self.SupplierTable.column("Invoice",width = 90)
        self.SupplierTable.column("Name",width = 100)
        self.SupplierTable.column("Contact",width = 100)
        self.SupplierTable.column("Description",width = 100)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

#--------------------Add Function------------------------------------

    def add(self):
        con = sqlite3.connect(database = r'test.db')
        cur = con.cursor()

        try:
            if self.var_supp_invoice.get() == "":
                messagebox.showerror("Error","Invoice must be required",parent = self.root)
            else:
                cur.execute("Select *from supplier where invoice=?",(self.var_supp_invoice.get(),))
                row = cur.fetchone()

                if row!= None:
                    messagebox.showerror("Error","This Invoice no. is already assigned",parent = self.root )
                else:
                    cur.execute("Insert into supplier(invoice ,name ,contact,desc) values(?,?,?,?)",(
                        self.var_supp_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.text_desc.get('1.0',END),
                    ))
                    con.commit()
                    self.show()
                    messagebox.showinfo("Success","Supplier added Succesfully",parent = self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent = self.root)


#--------------------Show Function------------------------------------

    def show(self):
        con = sqlite3.connect(database = r'test.db')
        cur = con.cursor()

        try:
         cur.execute("Select * from supplier")
         rows = cur.fetchall() 

         self.SupplierTable.delete(*self.SupplierTable.get_children())

         for row in rows:
             self.SupplierTable.insert('',END,values = row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent = self.root)


#--------------------Get Data Function------------------------------------

    def get_data(self,ev):

        f = self.SupplierTable.focus()
        content = (self.SupplierTable.item(f)) 
        row = content['values']

        self.var_supp_invoice.set(row[0]),
        self.var_name.set(row[1]),
        self.var_contact.set(row[2]),
        self.text_desc.delete('1.0',END),
        self.text_desc.insert(END,row[3]),
      

#--------------------Update Function------------------------------------

    def update(self):
        con = sqlite3.connect(database = r'test.db')
        cur = con.cursor()

        try:
            if self.var_supp_invoice.get() == "":
                messagebox.showerror("Error","Invoice must be required",parent = self.root)
            else:
                cur.execute("Select *from supplier where invoice=?",(self.var_supp_invoice.get(),))
                row = cur.fetchone()

                if row== None:
                    messagebox.showerror("Error","Invalid Invoice No",parent = self.root )
                else:
                    cur.execute("UPDATE supplier set name=?,contact=?,desc=? WHERE invoice =?",(
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.text_desc.get('1.0',END),
                        self.var_supp_invoice.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Updated Succesfully",parent = self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent = self.root)


#--------------------Delete Function------------------------------------

    def delete(self):
        con = sqlite3.connect(database = r'test.db')
        cur = con.cursor()

        try:
            if self.var_supp_invoice.get() == "":
                messagebox.showerror("Error","Invoice no. must be required",parent = self.root)
            else:
                cur.execute("Select *from supplier where invoice=?",(self.var_supp_invoice.get(),))
                row = cur.fetchone()

                if row== None:
                    messagebox.showerror("Error","Invalid Invoice no.",parent = self.root )
                else:
                    op = messagebox.askyesno("Confirm","Are you realy want to delete?",parent = self.root)
                    if op == True:
                        cur.execute("Delete from supplier where invoice = ?",(self.var_supp_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier Deleted Succesfully",parent = self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent = self.root)            


#--------------------Clear Function------------------------------------

    def clear(self):

        self.var_supp_invoice.set(""),
        self.var_name.set(""),
        self.var_contact.set(""),
        self.text_desc.delete('1.0',END),
        self.var_searchtext.set("")
        self.show()


#--------------------Search Function------------------------------------

    def search(self):
        con = sqlite3.connect(database = r'test.db')
        cur = con.cursor()

        try:
            if self.var_searchtext.get()=="":
              messagebox.showerror("Error","Invoice no. required",parent = self.root)
            
            else:
              cur.execute("Select * from supplier where invoice = ?",(self.var_searchtext.get(),))
              row = cur.fetchone() 

              if row!=None:
                self.SupplierTable.delete(*self.SupplierTable.get_children())
                self.SupplierTable.insert('',END,values = row)
              else:
                  messagebox.showinfo("Error","No record found",parent = self.root)
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to:{str(ex)}",parent = self.root)

#--------------------Main Function------------------------------------



if __name__ == "__main__":
    root = Tk()
    obj =Supplier_class(root)
    root.mainloop()
