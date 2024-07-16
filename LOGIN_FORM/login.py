from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x800+0+0")
        self.root.title("SCUTU BIKE MANAGEMENT SYSTEM  LOGIN PANEL")
        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Sanjay Vishwakarma\OneDrive\Desktop\LOGIN_FORM\images\bikeimg.jpg")
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        
        img1=Image.open(r"C:\Users\Sanjay Vishwakarma\OneDrive\Desktop\LOGIN_FORM\images\userloginavtar.png")
        img1=img1.resize((100,100),Image.AFFINE)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0,)
        lblimg1.place(x=730,y=175,width=100,height=100)
        
        get_str=Label(frame,text="Get Started",font=('times new roman',20,"bold",),fg="white",bg="black")
        get_str.place(x=95,y=100)
        
        #label
        
        username_lbl=Label(frame,text="UserName",font=('times new roman',15,"bold",),fg="white",bg="black")
        username_lbl.place(x=130,y=155)
        
        self.txtuser=ttk.Entry(frame,font=('times new roman',15,'bold'))
        self.txtuser.place(x=40,y=180,width=270)
        
        password_lbl=Label(frame,text="Password",font=('times new roman',15,"bold",),fg="white",bg="black")
        password_lbl.place(x=130,y=225)
        
        self.txtpassword=ttk.Entry(frame,font=('times new roman',15,'bold'))
        self.txtpassword.place(x=40,y=250,width=270)
        
        ##########iconIMAGES#######################
        img2=Image.open(r"C:\Users\Sanjay Vishwakarma\OneDrive\Desktop\LOGIN_FORM\images\userloginavtar.png")
        img2=img2.resize((25,25),Image.AFFINE)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0,)
        lblimg2.place(x=712,y=325,width=25,height=25)
        
        img3=Image.open(r"C:\Users\Sanjay Vishwakarma\OneDrive\Desktop\LOGIN_FORM\images\userloginavtar.png")
        img3=img3.resize((25,25),Image.AFFINE)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0,)
        lblimg3.place(x=712,y=394,width=25,height=25)
        
        #loginbutton##########
        btn_login=Button(frame,command=self.login,text="Login",font=('times new roman',15,'bold'),bd=3,relief=RIDGE,fg='white',bg="orange",activeforeground="white",activebackground="orange")
        btn_login.place(x=110,y=300,width=120,height=35)
        
        #registerbutton
        btn_register=Button(frame,text="New User Register",font=('times new roman',10,'bold'),borderwidth=0,fg='white',bg="black",activeforeground="white",activebackground="black")
        btn_register.place(x=19,y=350,width=160)
        
        #forgetpassword
        btn_forget=Button(frame,text="Forget Password",font=('times new roman',10,'bold'),borderwidth=0,fg='white',bg="black",activeforeground="white",activebackground="black")
        btn_forget.place(x=15,y=370,width=160)
        
        
    def login(self):
        if self.txtuser.get() == "" or self.txtpassword.get() == "":
            messagebox.showerror("Error", "All Fields are Required")
        elif self.txtuser.get() == "sanjay" and self.txtpassword.get() == "sanjay12":
            messagebox.showinfo("Success", "Welcome to SCUTU LOGIN")
        else:
            messagebox.showerror("Invalid", "Invalid Username & Password")   
            
                 
               
if __name__=="__main__":
            root=Tk()
            app=Login_Window(root)
            root.mainloop()       

