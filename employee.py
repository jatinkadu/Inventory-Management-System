from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class Employee_class:
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

        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()        
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()


   #----------Search Frame------------

        Search_Frame = LabelFrame(self.root,text = "Search something",font = ("goudy old style",12,"bold"),bg = "white", bd =2,relief = RIDGE)
        Search_Frame.place(x = 250,y = 20,width = 600,height = 70 )

        #--------option--------

        cmb_Search = ttk.Combobox(Search_Frame,textvariable = self.var_searchby,values = ("Search","Name","Email","Contact"),state = 'Readonly',justify = CENTER,font = ("goudy old style",15,"bold"))
        cmb_Search.place(x = 10, y= 10, width = 180)
        cmb_Search.current(0)

        text_search = Entry(Search_Frame,textvariable = self.var_searchtext,font =("Goudy old style",15), bg = "Light yellow").place(x = 200,y = 10,width = 260,height =30)
        btn_search = Button(Search_Frame,text = "Search",command = self.search,font =("Goudy old style",15), bg = "Green",cursor = "hand2").place(x = 470,y = 5,width = 120,height = 35)

       #----------details--------------

        title = Label(self.root,text = "Employee Details",font =("Goudy old style",15), bg = "#0f4d7d").place(x = 50,y = 100,width = 1000)

      #------Content------------------

        lbl_empid    = Label(self.root,text = "Emp ID",font =("Goudy old style",15), bg = "white").place(x = 50,y = 150) 
        lbl_Gender   = Label(self.root,text = "Gender",font =("Goudy old style",15), bg = "white").place(x = 350,y = 150) 
        lbl_Contact  = Label(self.root,text = "Contact",font =("Goudy old style",15), bg = "white").place(x = 750,y = 150) 

        txt_empid    = Entry(self.root,textvariable = self.var_emp_id,font =("Goudy old style",15), bg = "light yellow").place(x = 150,y = 150,width = 180) 
        cmb_Gender = ttk.Combobox(self.root,textvariable = self.var_gender,values = ("Search","Male","Female","Others"),state = 'Readonly',justify = CENTER,font = ("goudy old style",15))
        cmb_Gender.place(x = 500, y= 150, width = 180)
        cmb_Gender.current(0)
        txt_Contact  = Entry(self.root,textvariable = self.var_contact,font =("Goudy old style",15), bg = "light yellow").place(x = 850,y = 150,width = 180) 

      #------------row 2-------------

        lbl_name   = Label(self.root,text = "Name",font =("Goudy old style",15), bg = "white").place(x = 50,y = 190) 
        lbl_dob   = Label(self.root,text = "DOB",font =("Goudy old style",15), bg = "white").place(x = 350,y = 190) 
        lbl_doj  = Label(self.root,text = "DOJ",font =("Goudy old style",15), bg = "white").place(x = 750,y = 190) 

        txt_name    = Entry(self.root,textvariable = self.var_name,font =("Goudy old style",15), bg = "light yellow").place(x = 150,y = 190,width = 180) 
        txt_dob    =  Entry(self.root,textvariable = self.var_dob,font =("Goudy old style",15), bg = "light yellow").place(x = 500,y = 190,width = 180) 
        txt_doj    =  Entry(self.root,textvariable = self.var_doj,font =("Goudy old style",15), bg = "light yellow").place(x = 850,y = 190,width = 180) 

      #------------row 3-------------

        lbl_email   = Label(self.root,text = "Email ID",font =("Goudy old style",15), bg = "white").place(x = 50,y = 230) 
        lbl_pass = Label(self.root,text = "Password",font =("Goudy old style",15), bg = "white").place(x = 350,y = 230) 
        lbl_utype  = Label(self.root,text = "User Type",font =("Goudy old style",15), bg = "white").place(x = 750,y = 230) 

        txt_email    = Entry(self.root,textvariable = self.var_email,font =("Goudy old style",15), bg = "light yellow").place(x = 150,y = 230,width = 180) 
        txt_pass    =  Entry(self.root,textvariable = self.var_pass,font =("Goudy old style",15), bg = "light yellow").place(x = 500,y = 230,width = 180) 
        cmb_utype = ttk.Combobox(self.root,textvariable = self.var_utype,values = ("Admin","Employee"),state = 'Readonly',justify = CENTER,font = ("goudy old style",15))
        cmb_utype.place(x = 850,y = 230,width = 180)
        cmb_utype.current(0)

#------------row 4-------------

        lbl_address   = Label(self.root,text = "Address",font =("Goudy old style",15), bg = "white").place(x = 50,y = 270) 
        lbl_salary = Label(self.root,text = "Salary",font =("Goudy old style",15), bg = "white").place(x = 500,y = 270) 
       
        self.text_address = Text(self.root,font =("Goudy old style",15), bg = "light yellow")
        self.text_address.place(x = 150,y = 270,width = 300,height = 60) 
        txt_salary    =  Entry(self.root,textvariable = self.var_salary,font =("Goudy old style",15), bg = "light yellow").place(x = 600,y = 270,width = 180) 
        
#----------Buttons--------------

        btn_add = Button(self.root,text = "Save",command = self.add,font =("Goudy old style",15), bg = "#2196f3",cursor = "hand2").place(x = 500,y = 305,width = 110,height = 28)
        btn_update = Button(self.root,text = "Update",command = self.update,font =("Goudy old style",15), bg = "#4caf50",cursor = "hand2").place(x = 620,y = 305,width = 110,height = 28)
        btn_delete = Button(self.root,text = "Delete",command = self.delete,font =("Goudy old style",15), bg = "#f44336",cursor = "hand2").place(x = 740,y = 305,width = 110,height = 28)
        btn_clear = Button(self.root,text = "Clear",command = self.clear,font =("Goudy old style",15), bg = "#607d8b",cursor = "hand2").place(x = 860,y = 305,width = 110,height = 28)
    
#----------Employee Details--------------

        emp_frame = Frame(self.root, bd = 3,relief = RIDGE)
        emp_frame.place(x = 0,y = 350,relwidth = 1,height = 150) 

        scrolly = Scrollbar(emp_frame,orient = VERTICAL)
        scrollx = Scrollbar(emp_frame,orient = HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(emp_frame,columns= ("eid","name","email","gender","contact","dob","doj","pass","utype","salary","address"),yscrollcommand = scrolly.set,xscrollcommand = scrollx.set )
        scrollx.pack(side = BOTTOM,fill = X)
        scrolly.pack(side = RIGHT,fill = Y)
        scrollx.config(command = self.EmployeeTable.xview)
        scrolly.config(command = self.EmployeeTable.yview)

       
        self.EmployeeTable.heading("eid",text = "Emp ID")
        self.EmployeeTable.heading("name",text = "Name")
        self.EmployeeTable.heading("email",text = "Email")
        self.EmployeeTable.heading("gender",text = "Gender")
        self.EmployeeTable.heading("contact",text = "Contact")
        self.EmployeeTable.heading("pass",text = "Password")
        self.EmployeeTable.heading("dob",text = "D.O.B")
        self.EmployeeTable.heading("doj",text = "D.O.J")
        self.EmployeeTable.heading("utype",text = "User Type")
        self.EmployeeTable.heading("salary",text = "Salary")
        self.EmployeeTable.heading("address",text ="Address")
        self.EmployeeTable["show"] = "headings"
        self.EmployeeTable.pack(fill = BOTH,expand = 1)


        self.EmployeeTable.column("eid",width = 90)
        self.EmployeeTable.column("name",width = 100)
        self.EmployeeTable.column("email",width = 100)
        self.EmployeeTable.column("gender",width = 100)
        self.EmployeeTable.column("contact",width = 100)
        self.EmployeeTable.column("dob",width = 100)
        self.EmployeeTable.column("doj",width = 100)
        self.EmployeeTable.column("pass",width = 100)
        self.EmployeeTable.column("utype",width = 100)
        self.EmployeeTable.column("address",width = 100)
        self.EmployeeTable.column("salary",width = 100)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

#--------------------Add Function------------------------------------

    def add(self):
        con = sqlite3.connect(database = r'test.db')
        cur = con.cursor()

        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error","Employee ID must be required",parent = self.root)
            else:
                cur.execute("Select *from employee where eid=?",(self.var_emp_id.get(),))
                row = cur.fetchone()

                if row!= None:
                    messagebox.showerror("Error","This Employee ID is already assigned",parent = self.root )
                else:
                    cur.execute("Insert into employee(eid ,name ,email ,gender,contact,dob,doj ,pass,utype,address,salary) values(?,?,?, ?,?,?, ?,?,?, ?,?)",(
                        self.var_emp_id.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),       
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.text_address.get('1.0',END),
                        self.var_salary.get()
                    ))
                    con.commit()
                    self.show()
                    messagebox.showinfo("Success","Employee added Succesfully",parent = self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent = self.root)


#--------------------Show Function------------------------------------

    def show(self):
        con = sqlite3.connect(database = r'test.db')
        cur = con.cursor()

        try:
         cur.execute("Select * from employee")
         rows = cur.fetchall() 

         self.EmployeeTable.delete(*self.EmployeeTable.get_children())

         for row in rows:
             self.EmployeeTable.insert('',END,values = row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent = self.root)


#--------------------Get Data Function------------------------------------

    def get_data(self,ev):

        f = self.EmployeeTable.focus()
        content = (self.EmployeeTable.item(f)) 
        row = content['values']
        self.var_emp_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_dob.set(row[5]),
        self.var_doj.set(row[6]),       
        self.var_pass.set(row[7]),
        self.var_utype.set(row[8]),
        self.text_address.delete('1.0',END),
        self.text_address.insert(END,row[9]),
        self.var_salary.set(row[10])


#--------------------Update Function------------------------------------

    def update(self):
        con = sqlite3.connect(database = r'test.db')
        cur = con.cursor()

        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error","Employee ID must be required",parent = self.root)
            else:
                cur.execute("Select *from employee where eid=?",(self.var_emp_id.get(),))
                row = cur.fetchone()

                if row== None:
                    messagebox.showerror("Error","Invalid Employee ID",parent = self.root )
                else:
                    cur.execute("UPDATE employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? WHERE eid =? ;",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),       
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.text_address.get('1.0',END),
                        self.var_salary.get(),
                        self.var_emp_id.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Updated Succesfully",parent = self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent = self.root)


#--------------------Delete Function------------------------------------

    def delete(self):
        con = sqlite3.connect(database = r'test.db')
        cur = con.cursor()

        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error","Employee ID must be required",parent = self.root)
            else:
                cur.execute("Select *from employee where eid=?",(self.var_emp_id.get(),))
                row = cur.fetchone()

                if row== None:
                    messagebox.showerror("Error","Invalid Employee ID",parent = self.root )
                else:
                    op = messagebox.askyesno("Confirm","Are you realy want to delete?",parent = self.root)
                    if op == True:
                        cur.execute("Delete from employee where eid = ?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee Deleted Succesfully",parent = self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent = self.root)            


#--------------------Clear Function------------------------------------

    def clear(self):

        self.var_emp_id.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_contact.set(""),
        self.var_dob.set(""),
        self.var_doj.set(""),       
        self.var_pass.set(""),
        self.var_utype.set("Admin"),
        self.text_address.delete('1.0',END),
        self.var_salary.set("")
        self.var_searchby.set("Select")
        self.var_searchtext.set("")
        self.show()


#--------------------Search Function------------------------------------

    def search(self):
        con = sqlite3.connect(database = r'test.db')
        cur = con.cursor()

        try:
            if self.var_searchby.get()=="Select":
              messagebox.showerror("Error","Select Search by Option",parent = self.root)

            elif self.var_searchtext.get()=="":
              messagebox.showerror("Error","Search input required",parent = self.root)
            
            else:
              cur.execute("Select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtext.get()+"%'")
              rows = cur.fetchall() 

              if len(rows)!=0:
                self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                for row in rows:
                    self.EmployeeTable.insert('',END,values = row)
              else:
                  messagebox.showinfo("Error","No record found",parent = self.root)
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to:{str(ex)}",parent = self.root)

#--------------------Main Function------------------------------------



if __name__ == "__main__":
    root = Tk()
    obj = Employee_class(root)
    root.mainloop()
