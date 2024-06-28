from tkinter import* # tkinter contain the various methods for making GUI
from tkinter import ttk,messagebox
import sqlite3
from category import categoryClass
from product import productClass
import time
import os
import tempfile

class Bill_class:
    def __init__(self,root): #default method
        self.root=root #the root obj now belongs to class
        self.root.geometry("1350x700+0+0")#geometry is a method which takes height,width,starting,ending pt.
        self.root.title("INVENTORY MANAGEMENT SYSTEM | Devloped by Royce,Jatin,Darsh") #give title to screen
        self.root.config(bg="white")
        self.cart_list = []
        self.chk_print = 0 
        #====Title====#

    
        self.icon_title=PhotoImage(file="images/logo1.png")# can be used only for png images
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("sacramento,cursive",40,"bold"),bg="#30D5C8",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=60)#Label is a part of tkinter class and takes attribute location,text,place defines the location in self.root frame,compound gives location of images

        #====btn__logout=====#
        btn__logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),command=self.logout,bg='yellow',cursor="hand2").place(x=1150,y=10,height=50,width=100) #button function takes various attributes diff is only the cursor attribute

        #=====clock====#
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System \t\t Date:DD:MM:YYYY \t\t time:HH:MM:SS",font=("sacramento,cursive",15,),bg="black",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=60)#placed on 2nd line in the self.root frame

        #==========Product Frame1====#
        self.var_search=StringVar()
        Product_frame1=Frame(self.root,relief=RIDGE,bd=3,bg="white")
        Product_frame1.place(x=6,y=110,width=410,height=550)

        ptitle=Label(Product_frame1,text="All Products",font=("times new Roman",15,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        #===============product search frame======#
        Product_frame2=Frame(Product_frame1,relief=RIDGE,bd=2,bg="white")
        Product_frame2.place(x=2,y=42,width=398,height=90)

        lbl_search=Label(Product_frame2,text="Search by | Name",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)
        lbl_search=Label(Product_frame2,text="product Name",font=("times new roman",15,"bold"),bg="white").place(x=5,y=45)

        txt_search=Entry(Product_frame2,textvariable=self.var_search,font=("times new roman",15,"bold"),bg="lightyellow").place(x=128,y=47,height=22,width=150)
        btn_search=Button(Product_frame2,text="search",command = self.search,cursor="hand2",font=("times new roman",15,"bold"),bg="#2196f3",fg="white").place(x=285,y=45,width=100,height=25)
        btn_showAll=Button(Product_frame2,text="show all",command = self.show,cursor="hand2",font=("times new roman",15,"bold"),bg="#083531",fg="white").place(x=285,y=10,width=100,height=25)
      
        #==============product detail frame======#
        Product_frame3=Frame(Product_frame1,bd=3,relief=RIDGE)
        Product_frame3.place(x=2,y=140,width=398,height=375)

        scrolly=Scrollbar(Product_frame3,orient=VERTICAL)
        scrollx=Scrollbar(Product_frame3,orient=HORIZONTAL)

        self.product_Table=ttk.Treeview(Product_frame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly,xscrollcommand=scrolly)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)
        self.product_Table.heading("pid",text="Pid")
        self.product_Table.heading("name",text="Name")
        self.product_Table.heading("price",text="Price")
        self.product_Table.heading("qty",text="QTY")
        self.product_Table.heading("status",text="Status")
        
        self.product_Table['show']= 'headings'     
        self.product_Table.column("pid",width=90)
        self.product_Table.column("name",width=100)
        self.product_Table.column("price",width=100)
        self.product_Table.column("qty",width=100)
        self.product_Table.column("status",width=100)
        self.product_Table.pack(fill=BOTH,expand=1)
        self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note=Label(Product_frame1,text="Note:Enter 0 Qty to remove product from cart",font=("times new roman",12),bg="white",fg="red").pack(side=BOTTOM,fill=X)

        #======Customerframe======#
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        Customerframe=Frame(self.root,relief=RIDGE,bd=3,bg="white")
        Customerframe.place(x=420,y=110,width=530,height=70) # previously x was 6+400 width 
        Ctitle=Label(Customerframe,text="Customer Details",font=("times new Roman",15),bg="grey").pack(side=TOP,fill=X)
        lbl_name=Label(Customerframe,text=" Name",font=("times new roman",15),bg="white").place(x=5,y=35)
        txt_name=Entry(Customerframe,textvariable=self.var_cname,font=("times new roman",15),bg="lightyellow").place(x=80,y=35,width=180)
        lbl_contact=Label(Customerframe,text=" Contact No",font=("times new roman",15),bg="white").place(x=270,y=35)
        txt_contact=Entry(Customerframe,textvariable=self.var_contact,font=("times new roman",15),bg="lightyellow").place(x=380,y=35,width=140)
       
        #=================Calucator-cart Frame=============================#
        cal_cart_frame=Frame(self.root,relief=RIDGE,bd=3,bg="white")
        cal_cart_frame.place(x=420,y=190,width=530,height=360)
      
        #============calculator frame===============================
        self.var_cal_input=StringVar()
        cal_frame=Frame(cal_cart_frame,relief=RIDGE,bd=9,bg="white")
        cal_frame.place(x=5,y=10,width=268,height=340)
        txt_cal_input=Entry(cal_frame,textvariable=self.var_cal_input,font=('arial',15,'bold'),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)

                #=====cal BUTTON============#
        btn_7=Button(cal_frame,text='7',font=('arial',15,'bold'),bd=5,width=4,command=lambda:self.get_input(7),pady=10,cursor='hand2').grid(row=1,column=0)
        btn_8=Button(cal_frame,text='8',font=('arial',15,'bold'),bd=5,width=4,pady=10,command=lambda:self.get_input(8),cursor='hand2').grid(row=1,column=1)
        btn_9=Button(cal_frame,text='9',font=('arial',15,'bold'),bd=5,width=4,pady=10,command=lambda:self.get_input(9),cursor='hand2').grid(row=1,column=2)
        btn_sum=Button(cal_frame,text='+',font=('arial',15,'bold'),bd=5,width=4,pady=10,command=lambda:self.get_input('+'),cursor='hand2').grid(row=1,column=3)


        btn_4=Button(cal_frame,text='4',font=('arial',15,'bold'),bd=5,width=4,pady=10,command=lambda:self.get_input(4),cursor='hand2').grid(row=2,column=0)
        btn_5=Button(cal_frame,text='5',font=('arial',15,'bold'),bd=5,width=4,pady=10,command=lambda:self.get_input(5),cursor='hand2').grid(row=2,column=1)
        btn_6=Button(cal_frame,text='6',font=('arial',15,'bold'),bd=5,width=4,pady=10,command=lambda:self.get_input(6),cursor='hand2').grid(row=2,column=2)
        btn_sub=Button(cal_frame,text='-',font=('arial',15,'bold'),bd=5,width=4,pady=10,command=lambda:self.get_input('-'),cursor='hand2').grid(row=2,column=3)

        btn_1=Button(cal_frame,text='1',font=('arial',15,'bold'),bd=5,width=4,pady=10,command=lambda:self.get_input(1),cursor='hand2').grid(row=3,column=0)
        btn_2=Button(cal_frame,text='2',font=('arial',15,'bold'),bd=5,width=4,pady=10,command=lambda:self.get_input(2),cursor='hand2').grid(row=3,column=1)
        btn_3=Button(cal_frame,text='3',font=('arial',15,'bold'),bd=5,width=4,pady=10,command=lambda:self.get_input(3),cursor='hand2').grid(row=3,column=2)
        btn_mul=Button(cal_frame,text='x',font=('arial',15,'bold'),bd=5,width=4,pady=10,command=lambda:self.get_input('*'),cursor='hand2').grid(row=3,column=3)

        btn_0=Button(cal_frame,text='0',font=('arial',15,'bold'),bd=5,width=4,pady=15,command=lambda:self.get_input(0),cursor='hand2').grid(row=4,column=0)
        btn_c=Button(cal_frame,text='C',font=('arial',15,'bold'),bd=5,width=4,pady=15,cursor='hand2',command=self.cal_clear).grid(row=4,column=1)
        btn_eq=Button(cal_frame,text='=',font=('arial',15,'bold'),bd=5,width=4,pady=15,cursor='hand2',command=self.perform_cal).grid(row=4,column=2)
        btn_div=Button(cal_frame,text='/',font=('arial',15,'bold'),bd=5,width=4,pady=15,command=lambda:self.get_input('/'),cursor='hand2').grid(row=4,column=3)



        #=======================cart-frame=======================#

        cart_frame=Frame(cal_cart_frame,bd=3,relief=RIDGE)
        cart_frame.place(x=280,y=8,width=245,height=342)
        self.Cart_title=Label(cart_frame,text="Cart \t total product:[0]",font=("times new Roman",15),bg="grey")
        self.Cart_title.pack(side = TOP,fill = X)

        scrolly=Scrollbar(cart_frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_frame,orient=HORIZONTAL)

        self.cart_Table=ttk.Treeview(cart_frame,columns=("pid","name","price","qty"),yscrollcommand=scrolly,xscrollcommand=scrolly)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.cart_Table.xview)
        scrolly.config(command=self.cart_Table.yview)
        self.cart_Table.heading("pid",text="Pid")
        self.cart_Table.heading("name",text="Name")
        self.cart_Table.heading("price",text="Price")
        self.cart_Table.heading("qty",text="QTY")
        
        self.cart_Table["show"]= "headings"     
        self.cart_Table.column("pid",width=40)
        self.cart_Table.column("name",width=100)
        self.cart_Table.column("price",width=40)
        self.cart_Table.column("qty",width=50)

        self.cart_Table.pack(fill=BOTH,expand=1)
        self.cart_Table.bind("<ButtonRelease-1>",self.get_data_cart)
        #============Add cart widgetsFrame================#
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_status=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
        Add_cartwidgetsframe=Frame(self.root,relief=RIDGE,bd=3,bg="white")
        Add_cartwidgetsframe.place(x=420,y=550,width=530,height=110)

        lbl_p_name=Label(Add_cartwidgetsframe,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(Add_cartwidgetsframe,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)

        lbl_p_price=Label(Add_cartwidgetsframe,text="Price per QTY",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_p_price=Entry(Add_cartwidgetsframe,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=230,y=35,width=150,height=22)
        
        lbl_p_qty=Label(Add_cartwidgetsframe,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_p_qty=Entry(Add_cartwidgetsframe,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=390,y=35,width=130,height=22)

        self.lbl_p_instock=Label(Add_cartwidgetsframe,text="In stock",font=("times new roman",15),bg="white")
        self.lbl_p_instock.place(x=5,y=70)

        btn_clear_cart=Button(Add_cartwidgetsframe,text="clear",command=self.clear_cart,cursor="hand2",font=("times new roman",15,"bold"),bg="lightgray").place(x=180,y=70,width=150,height=30)
        btn_update_cart=Button(Add_cartwidgetsframe,text="update",command = self.update_cart,cursor="hand2",font=("times new roman",15,"bold"),bg="orange").place(x=340,y=70,width=180,height=30)

        #=================Bill_class area===================#
        billFrame=Frame(self.root,bd=3, relief=RIDGE ,bg="white")
        billFrame.place(x=953,y=110,width=410,height=410)
        billarea_title=Label(billFrame,text="Customer bill area",font=("times new Roman",15),bg="black",fg = "white").pack(side=TOP,fill=X)
       
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        self.txt_bill_area=Text(billFrame,font=('goudy old stylr',12,'bold'),yscrollcommand=scrolly)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)
        #===================bill Buttons=============#
        bill_menu_Frame=Frame(self.root,bd=2, relief=RIDGE ,bg="white")
        bill_menu_Frame.place(x=953,y=520,width=410,height= 140)
        self.lbl_amt=Label(bill_menu_Frame,text='bill amount \n [0]',font=("goudy old style",15,"bold"),bg="#3f51b5")
        self.lbl_amt.place(x=2,y=5,width=120,height=70)

        self.lbl_discount=Label(bill_menu_Frame,text='discount \n 5%',font=("goudy old style",15,"bold"),bg="#8bc34a")
        self.lbl_discount.place(x=124,y=5,width=120,height=70)

        self.lbl_netpay=Label(bill_menu_Frame,text='Net Pay \n [0]',font=("goudy old style",15,"bold"),bg="#607d8b")
        self.lbl_netpay.place(x=246,y=5,width=120,height=70)

        btn_print=Button(bill_menu_Frame,text='print bill',command=self.print_bill,cursor="hand2",font=("goudy old style",15,"bold"),bg="red",fg = "white")
        btn_print.place(x=2,y=80,width=120,height=50)

        btn_clear_all=Button(bill_menu_Frame,text='clear bill',command = self.clear_all,cursor="hand2",font=("goudy old style",15,"bold"),bg="lightgreen")
        btn_clear_all.place(x=124,y=80,width=120,height=50)

        btn_generate=Button(bill_menu_Frame,cursor="hand2",command = self.generate_bill,text='generate bill',font=("goudy old style",15,"bold"),bg="purple")
        btn_generate.place(x=246,y=80,width=120,height=50)

        self.show()
        self.update_date_time()
       

    #=========================ALL FUNCTIONS======================#

    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)
    def cal_clear(self):
        self.var_cal_input.set('')
    def perform_cal(self):  
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))


#--------------------Get Data Function------------------------------------

    def get_data(self,ev):

        f = self.product_Table.focus()
        content = (self.product_Table.item(f)) 
        row = content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1]) 
        self.var_price.set(row[2])
        self.lbl_p_instock.config(text = f"In Stock [{str(row[3])}] ")
        self.var_stock.set(row[3])
        self.var_qty.set('1')


#--------------------Get Data Cart------------------------------------

    def get_data_cart(self,ev):

        f = self.cart_Table.focus()
        content = (self.cart_Table.item(f)) 
        row = content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1]) 
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.lbl_p_instock.config(text = f"In Stock [{str(row[4])}] ")
        self.var_stock.set(row[4])



 #--------------------Show Function------------------------------------

    def show(self):
        con = sqlite3.connect(database = r'test.db')
        cur = con.cursor()
        try:
         cur.execute("Select pid,name,price,qty,status from product where status = 'Active'")
         rows = cur.fetchall() 

         self.product_Table.delete(*self.product_Table.get_children())

         for row in rows:
             self.product_Table.insert('',END,values = row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent = self.root)

            

#--------------------Search Function------------------------------------

    def search(self):
        con = sqlite3.connect(database = r'test.db')
        cur = con.cursor()

        try:
            if self.var_search.get()=="Select":
              messagebox.showerror("Error","Select Search by Option",parent = self.root)

            elif self.var_search.get()=="":
              messagebox.showerror("Error","Search input required",parent = self.root)
            
            else:
              cur.execute("Select pid,name,price,qty,status from product where name LIKE '%"+self.var_search.get()+"%' and status ='Active'")
              rows = cur.fetchall() 

              if len(rows)!=0:
                self.product_Table.delete(*self.product_Table.get_children())
                for row in rows:
                    self.product_Table.insert('',END,values = row)
              else:
                  messagebox.showinfo("Error","No record found",parent = self.root)
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to:{str(ex)}",parent = self.root)


#----------------------------update cart fuction----------------

    def update_cart(self): 
        if self.var_pid.get() ==  '':
            messagebox.showerror("Error","Please select product is required",parent = self.root)
            
        elif self.var_qty.get() == '':
            messagebox.showerror("Error","Quantity is required",parent = self.root)
        
        elif int(self.var_qty.get()) > int(self.var_stock.get()):
            messagebox.showerror("Error","Invalid Quantity",parent = self.root)

        else:
            #price_cal = int((self.var_qty.get())) * float(self.var_price.get())
           # price_cal = float(price_cal)
            price_cal = self.var_price.get()
            cart_data = [self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get(),self.var_stock.get()]
            #  self.cart_list.append(cart_data)

        #-----------Update Cart-----------------------
            present = "no"
            index_= 0
            for row in self.cart_list:
                if self.var_pid.get() == row[0]:
                    present = "yes"
                    break
                index_ = index_+1
            print(index_,present)

            if present == "yes":
                print("I am here")
                op = messagebox.askyesno('Confirm',"Product already present\n Do you want to update | Remove",parent = self.root)          

                if op == True:
                    if self.var_qty.get() =="0":
                        self.cart_list.pop(index_)

                    else:
                       # self.cart_list[index_][2] = price_cal
                        self.cart_list[index_][3] = self.var_qty.get()
            else:
                self.cart_list.append(cart_data)
                print(self.cart_list)
            self.show_cart()
            self.bill_update()
    #-------------------------show_cart------------------

    def show_cart(self):
        
        try:
         self.cart_Table.delete(*self.cart_Table.get_children())
         for row in self.cart_list:
             self.cart_Table.insert('',END,values = row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent = self.root)


#-------------------------Bill Update-----------------

    def bill_update(self):
        self.bill_amt = 0
        self.net_pay = 0
        self.discount = 0
        for row in self.cart_list: 
            self.bill_amt = self.bill_amt + (float(row[2])*int(row[3]) ) 
        
        self.discount = (self.bill_amt*5)/100
        self.net_pay = self.bill_amt - self.discount
        self.lbl_amt.config(text = f'Bill Amount (Rs.) \n [{str(self.bill_amt)}]')
        self.lbl_netpay.config(text = f'Net Pay(Rs.) \n [{str(self.net_pay)}]')
        self.Cart_title.config(text= f"Cart \t total product:[{str(len(self.cart_list))}]")  


#------------------Generate Bill---------------------------

    def generate_bill(self):
        if self.var_cname.get() == '' or self.var_contact.get == '':
            messagebox.showerror('Error',f'Customer Details required',parent = self.root)
        elif len(self.cart_list) == 0:
            messagebox.showerror('Error',f'Please Add product required',parent = self.root)

        else:
            self.bill_top()
            self.bill_middle()
            self.bill_bottom()

            fp=open(f'bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showinfo('saved',"bill has been generated and saved in backend",parent=self.root)
            self.chk_print=1

#-------------Bill Top-----------------------

    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_temp=f'''
\t\tXYZ-Inventory
\t Phone No. 78915***** , Mumbai-400 001
{str("="*47)}
 Customer Name: {self.var_cname.get()}
 Ph no. :{self.var_contact.get()}
 Bill No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*47)}
 Product Name\t\t\tQTY\tPrice
{str("="*47)}
        '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)

#--------------Bill Middle-------------------------

    def bill_middle(self):
      con=sqlite3.connect(database=r'test.db')
      cur=con.cursor()
      try:
        for row in self.cart_list:
        # pid,name,price,qty,stock
            pid = row[0]
            name=row[1]
            qty = int(row[4]) - int(row[3])
            if int(row[3]) == int(row[4]):
                status = 'Inactive'
            if int(row[3]) != int(row[4]):
                status = 'Active'
            price=float(row[2])*int(row[3])
            price=str(price)
            self.txt_bill_area.insert(END,"\n "+name+"\t\t\t"+row[3]+"\tRs."+price)
        #--------------Update quantity of product---------------------
            cur.execute("Update product set qty=?,status = ? where pid = ?",(
                qty,
                status,
                pid))
            con.commit()
        con.close()
        self.show()  
      except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent = self.root)


#-----------------Bill Bottom-----------------------

    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*55)}
 Bill Amount\t\t\t\tRs.{self.bill_amt}
 Discount\t\t\t\tRs.{self.discount}
 Net Pay\t\t\t\tRs.{self.net_pay}
{str("="*55)}\n
        '''
        self.txt_bill_area.insert(END,bill_bottom_temp)

#------------------Print Bill---------------------

    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo('Print',"Please wait while printing",parent=self.root)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror('Print',"Please generate bill, to print the receipt",parent=self.root)
            
        
       
#-------------------Clear cart function-------------

    def clear_cart(self): #to be added as command in clear btn of billing
        self.var_pid.set("")
        self.var_pname.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.lbl_p_instock.config(text=f"In stock")
        self.var_stock.set("")

#-------------------Clear all function-------------


    def clear_all(self): #to be added as a command in clear all btn
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete('1.0',END)
        self.Cart_title.config(text=f"cart \t Total Product:[0]")
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()
        self.chk_print = 0


#-------------------Time--------------------

    
    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%D-%M-%Y")
        self.lbl_clock.config(text=f"Welcome to Inventory Management System \t\t Date:{str(date_) }\t\t time:{str(time_) }")
        self.lbl_clock.after(200,self.update_date_time)

#-----------------Logout--------------------------

    def logout(self):
        self.root.destroy()
        os.system("python login.py")
#----------------------Main-----------------------------

if __name__ == "__main__":
    root = Tk()
    obj = Bill_class(root)
    root.mainloop()