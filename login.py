from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os
import smtplib  
import time
import email_pass


class Login:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Login Page")
        self.root.config(bg = "#fafafa")

        #-----------Image------------

        self.phone_image = ImageTk.PhotoImage(file = "images/phone.png") 
        self.lbl_phone_image = Label(self.root,image = self.phone_image,bd = 0).place(x =200,y =50)

        #-----------Frame 1------------ 

        login_frame = Frame(self.root,bd = 2,relief = RIDGE, bg = "White")
        login_frame.place(x = 650,y = 90,width = 350,height = 460)

        title = Label(login_frame,text = "Login Frame",font = ("Elephant",30,"bold"),bg = "white").place(x = 0,y = 30,relwidth = 1 )

        lbl_user = Label(login_frame,text = "Employee ID",font = ("Andalus",15),fg = "#767171",bg = "white").place(x = 50,y = 100 )
        self.employee_id= StringVar()
        self.password = StringVar()
        text_employee_id= Entry(login_frame,textvariable = self.employee_id,font = ("Times new Roman",15),bg = "#ECECEC").place(x = 50,y = 140,width = 250)

        lbl_pass = Label(login_frame,text = "Password",font = ("Andalus",15),fg = "#767171",bg = "white").place(x = 50,y = 190 )
        text_pass = Entry(login_frame,show = "*",textvariable = self.password,font = ("Times new Roman",15),bg = "#ECECEC").place(x = 50,y = 240,width = 250)

        btn_login = Button(login_frame,text = "Login",command = self.first_login,font = ("Arial Rounded MT Bold",15),bg = "#00B0F0",bd = 0,cursor = "hand2").place(x =50,y = 300,width = 250,height = 35)

        hr = Label(login_frame,bg = "lightgray").place(x= 50,y = 370,width = 250,height = 2)
        Or = Label(login_frame,text = "OR",fg = "lightgray",bg = "white",font = ("Times new Roman",15,"bold")).place(x= 150,y = 355)

        btn_forget = Button(login_frame,text = "Forget Password?",command = self.forget_window,font = ("Times new Roman",13),bg = "white",fg = "#00759E",bd = 0,activebackground = "white",activeforeground = "#00759E",cursor = "hand2").place(x =100,y = 390)
        
        
        
#---------------------------Login-------------------------------------
    def first_login(self):
        con = sqlite3.connect(database = r'test.db')
        cur = con.cursor()

        try:
            if self.employee_id.get() =="" or self.password.get() == "":
                messagebox.showerror("Error","All fields required",parent = self.root)
            else:

                cur.execute("Select utype from employee where eid =? AND pass = ?",(self.employee_id.get(),self.password.get()))
                user = cur.fetchone()

                if user == None:
                    messagebox.showerror("Error","Invalid Username/Password",parent = self.root)
                else:
                    if user[0] == "Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent = self.root)
        
#---------------------------Forget Password-------------------------------------

    def forget_window(self):
        con = sqlite3.connect(database = r'test.db')
        cur = con.cursor()

        try:
            if self.employee_id.get() == "":
                messagebox.showerror("Error","Employee ID required",parent = self.root)

            else:
                cur.execute("Select email from employee where eid =?",(self.employee_id.get(),))
                email = cur.fetchone()
                if email == None:
                    messagebox.showerror("Error","Invalid Employee ID",parent = self.root)
                else:

                    self.var_otp = StringVar()
                    self.var_new_pass = StringVar()
                    self.var_conf_pass = StringVar()

                    chk = self.sent_email(email[0])

                    if chk == 'f':
                        messagebox.showerror("Error","Connection error,Try again",parent = self.root)

                    else:
                        self.forget_wind = Toplevel(self.root)
                        self.forget_wind.title("Forget Password")
                        self.forget_wind.geometry("400x350+500+100")
                        self.forget_wind.focus_force()

                        title = Label(self.forget_wind,text = "RESET PASSWORD",font = ("Goudy old style",15,"bold"),bg= "#3f51b5",fg = "white").pack(side = TOP,fill = X)
                        lbl_reset = Label(self.forget_wind,text = "Enter OTP sent on Registered Email",font = ("Times new roman",15)).place(x = 20,y = 60)
                        text_reset = Entry(self.forget_wind,textvariable = self.var_otp,font = ("Times new roman",15)).place(x = 20,y = 100,width = 250,height = 30)
                        self.btn_reset = Button(self.forget_wind,command = self.validate_otp,text = "SUBMIT",font = ("Times new roman",15))
                        self.btn_reset.place(x = 280,y = 100,width = 100,height = 30)

                        lbl_new_pass = Label(self.forget_wind,text = "New Password",font = ("Times new roman",15)).place(x = 20,y = 160)
                        text_new_pass = Entry(self.forget_wind,textvariable = self.var_new_pass,font = ("Times new roman",15)).place(x = 20,y = 190,width = 250,height = 30)
                    
                        lbl_confirm_pass = Label(self.forget_wind,text = "Confirm Password",font = ("Times new roman",15)).place(x = 20,y = 255)
                        text_confirm_pass = Entry(self.forget_wind,textvariable = self.var_conf_pass,font = ("Times new roman",15)).place(x = 20,y = 255,width = 250,height = 30)
                    
                        self.btn_update = Button(self.forget_wind,command = self.update_password,text = "Update",state = DISABLED,font = ("Times new roman",15))
                        self.btn_update.place(x = 150,y = 300,width = 100,height = 30)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent = self.root)

#---------------------------OTP-------------------------------------

    def update_password(self):
        if self.var_new_pass.get()=="" or self.var_conf_pass.get()=="" :
            messagebox.showerror("Error","Password must be required",parent = self.forget_wind)

        elif self.var_new_pass.get()!= self.var_conf_pass.get():
            messagebox.showerror("Error","New and Confirm Password must be same",parent = self.forget_wind)

        else:
            con = sqlite3.connect(database = r'test.db')
            cur = con.cursor()

            try:
                cur.execute("Update employee SET pass= ? where eid = ?",(self.var_new_pass.get(),self.employee_id.get()))
                con.commit()
                messagebox.showinfo("Success","Password Updated succesfully",parent = self.forget_wind)
                self.forget_wind.destroy()
            except Exception as ex:
              messagebox.showerror("Error",f"Error due to:{str(ex)}",parent = self.root)

    def validate_otp(self):
        if int(self.otp) == int(self.var_otp.get()):
            self.btn_update.config(state = NORMAL)
            self.btn_reset.config(state = DISABLED)
        else:
            messagebox.showinfo("Error","Invalid OTP,Try again",parent = self.forget_wind)


    def sent_email(self, to_):
        s = smtplib.SMTP("smtp.gmail.com",587)
        s. starttls()
    
        email_ = email_pass.email_
        pass_ = email_pass.pass_
        
        s. login(email_,pass_)
        
        self.otp = int(time.strftime("%H%M%S"))+int(time.strftime("%S"))

        subject = "IMS RESET PASSWORD"
        msg = f"Dear Sir/Madam\n\n Your Reset OTP is: {str(self.otp)}\nwith regards by project team"

        msg= "Subject :{} to {}\n\n".format(subject,msg)
        s.sendmail(email_,to_,msg)

        chk = s.ehlo()

        if chk[0] == 250:
            return 's'
        else:
            return 'f'


if __name__ == "__main__":

    root = Tk()
    obj = Login(root)
    root.mainloop() 
