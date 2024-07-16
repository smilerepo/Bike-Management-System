from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register on Scutu ")
        self.root.geometry("1600x900+0+0")
        
        ###########variables#######################
        self.var_firstname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        
        #backgroundimage    
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Sanjay Vishwakarma\OneDrive\Desktop\LOGIN_FORM\images\green2.webp")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        ######leftimage########
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\Sanjay Vishwakarma\OneDrive\Desktop\LOGIN_FORM\images\scooobg1.png")
        bg1_lbl=Label(self.root,image=self.bg1)
        bg1_lbl.place(x=50,y=100,width=470,height=550)
        
        ##FRAME#############################
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        
        register_lbl=Label(frame,text="REGISTER HERE" ,font=("times new roman",20,"bold"),fg="green",bg="white")
        register_lbl.place(x=260,y=20)
        
        ############label and Entry########################################################
        
        ###row1################
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)
        
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_firstname,font=("times new roman",15))
        self.fname_entry.place(x=50,y=130,width=250)
        
        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        l_name.place(x=370,y=100)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)
        
        #####row2#######################################
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)
        
        ###############row3####################################
        security_Q=Label(frame,text="Select Security Question", font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your First Teacher Name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
        
        security_A=Label(frame,text="Select Answer", font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)
        
        #########row4##################################
        pswd=Label(frame,text="Password", font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)
        
        
        confirm_pswd=Label(frame,text="Confirm Passsword", font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)
        
        ####################checkbutton################
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text=" I Agree The Terms & Condition",font=("times new roman",10,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)
        
        #######################buttons##################
        img=Image.open(r"C:\Users\Sanjay Vishwakarma\OneDrive\Desktop\LOGIN_FORM\images\regist.png")
        img=img.resize((200,50),Image.AFFINE)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=80,y=420,width=200)
        
        img1=Image.open(r"C:\Users\Sanjay Vishwakarma\OneDrive\Desktop\LOGIN_FORM\images\loginbutton.png")
        img1=img1.resize((200,50),Image.AFFINE)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b2=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
        b2.place(x=360,y=420,width=200) 
        
        
        ############function declaration###############
        
    def register_data(self):
        if self.var_firstname.get()==""or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirm Password Must Be Same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree Our Terms And Condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="sanjay@a23",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email =%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already Register, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_firstname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get(),
                                                                                        self.var_confpass.get(),

                                                                                      ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")        
            
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
           
         
if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
        

