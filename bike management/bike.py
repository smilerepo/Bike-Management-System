from tkinter import*
from tkinter import ttk , filedialog
from PIL import Image , ImageTk
import mysql.connector
from tkinter import messagebox
from tkcalendar import DateEntry


#admin and user ##########################################
# class Bike:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1530x7900+0+0")
#         self.root.title("SCUTU BIKE MANAGEMENT SYSTEM")

#         # Admin and User panels
#         self.admin_panel = None
#         self.user_panel = None

#         # Main Menu
#         menu = Menu(self.root)
#         self.root.config(menu=menu)

#         admin_menu = Menu(menu, tearoff=0)
#         menu.add_cascade(label="Admin", menu=admin_menu)
#         admin_menu.add_command(label="Admin Panel", command=self.open_admin_panel)

#         user_menu = Menu(menu, tearoff=0)
#         menu.add_cascade(label="User", menu=user_menu)
#         user_menu.add_command(label="User Panel", command=self.open_user_panel)

#     def open_admin_panel(self):
#         if self.admin_panel is None:
#             self.admin_panel = Toplevel(self.root)
#             self.admin_panel.title("Admin Panel")
#             self.admin_panel.geometry("1530x7900+0+0")
#             AdminPanel(self.admin_panel)

#     def open_user_panel(self):
#         if self.user_panel is None:
#             self.user_panel = Toplevel(self.root)
#             self.user_panel.title("User Panel")
#             self.user_panel.geometry("1530x7900+0+0")
#             UserPanel(self.user_panel)


# class AdminPanel:
#     def __init__(self, admin_root):
#         self.admin_root = admin_root
#         # Define and layout your admin panel widgets here (same as your original Bike class)


# class UserPanel:
#     def __init__(self, user_root):
#         self.user_root = user_root
#         # Define and layout your user panel widgets here
#         lbl_title = Label(self.user_root, text="SCUTU BIKE MANAGEMENT SYSTEM", font=('times new roman', 37, 'bold'), fg='darkorange', bg='black')
#         lbl_title.pack(side=TOP, fill=X)

#         user_frame = Frame(self.user_root, bd=2, relief=RIDGE, bg='white')
#         user_frame.place(x=0, y=50, width=1530, height=750)

#         # Add user-specific widgets and layout here
        
#  ###############################################################################################################
# import tkinter as tk
# from tkinter import messagebox


# # Function to show the user panel
# def show_user_panel():
#     user_panel = tk.Toplevel(root)
#     user_panel.title("User Panel")
#     user_panel.geometry("300x200")
#     tk.Label(user_panel, text="Welcome, User!").pack()
#     tk.Button(user_panel, text="View Profile", command=lambda: messagebox.showinfo("Profile", "User Profile Info")).pack()
#     tk.Button(user_panel, text="Logout", command=user_panel.destroy).pack()

# # Function to show the admin panel
# def show_admin_panel():
#     admin_panel = tk.Toplevel(root)
#     admin_panel.title("Admin Panel")
#     admin_panel.geometry("300x200")
#     tk.Label(admin_panel, text="Welcome, Admin!").pack()
#     tk.Button(admin_panel, text="Manage Users", command=lambda: messagebox.showinfo("Manage Users", "User Management")).pack()
#     tk.Button(admin_panel, text="Logout", command=admin_panel.destroy).pack()

# # Function to handle login
# def login():
#     username = username_entry.get()
#     password = password_entry.get()
#     if username == "admin" and password == "admin123":
#         show_admin_panel()
#     elif username == "user" and password == "user123":
#         show_user_panel()
#     else:
#         messagebox.showerror("Error", "Invalid credentials")

# # Main window
# root = tk.Tk()
# root.title("Login")
# root.geometry("300x150")

# tk.Label(root, text="Username").pack()
# username_entry = tk.Entry(root)
# username_entry.pack()

# tk.Label(root, text="Password").pack()
# password_entry = tk.Entry(root, show="*")
# password_entry.pack()

# tk.Button(root, text="Login", command=login).pack()

# root.mainloop()
#  ##################################################################################################       


# if __name__ == "__main__":
#     root = Tk()
#     app = Bike(root)
#     root.mainloop()




#######################################################################################################
class Bike:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x7900+0+0")
        self.root.title("SCUTU BIKE MANAGEMENT SYSTEM")
        
        #variables
        self.var_1=StringVar()
        self.var_2=StringVar()
        self.var_3=StringVar()
        self.var_4=StringVar()
        self.var_5=StringVar()
        self.var_6=StringVar()
        self.var_7=StringVar()
        self.var_8=StringVar()
        self.var_9=StringVar()
        self.var_10=StringVar()
        self.var_11=StringVar()
        self.var_12=StringVar()
        self.var_13=StringVar()
        self.var_14=StringVar()
        self.var_15=StringVar()
        self.var_16=StringVar()

        
        
        lbl_title=Label(self.root,text="SCUTU BIKE MANAGEMENT SYSTEM",font=('times new roman',37,'bold'),fg='darkorange',bg='black')
        lbl_title.place(x=0,y=0,width=1530,height=50)
        
        # # logo
        # img_logo=Image.open('images/SCUTU logo.png')
        # img_logo=img_logo.resize((50,50),Image.BILINEAR)
        # self.photo_logo=ImageTk.PhotoImage(img_logo)
        
        # self.logo=Label(self.root,image=self.photo_logo)
        # self.logo.place(x=270,y=0,width=50,height=50)
        
        #image Frame
        upper_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        upper_frame.place(x=0,y=50,width=1530,height=160)
        
        # 1st
        img1=Image.open('images/scut1.jpg')
        img1=img1.resize((540,160),Image.BILINEAR)
        self.photo1=ImageTk.PhotoImage(img1)
         
        self.img_1=Label(upper_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=160)
        
                
        # # 2nd
        img2=Image.open('images/scut2.jpg')
        img2=img2.resize((540,160),Image.BILINEAR)
        self.photo2=ImageTk.PhotoImage(img2)
        
        self.img_2=Label(upper_frame,image=self.photo2)
        self.img_2.place(x=540,y=0,width=540,height=160)
        
        
        # #3rd
        img3=Image.open('images/scut3.jpg')
        img3=img3.resize((540,160),Image.BILINEAR)
        self.photo3=ImageTk.PhotoImage(img3)
        
        self.img_3=Label(upper_frame,image=self.photo3)
        self.img_3.place(x=1000,y=0,width=540,height=160)
        
        # Main Frame
        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='orange')
        main_frame.place(x=10,y=220,width=1500,height=560)
        
        # upper frame
        upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='grey',text='BIKE AND RIDER INFORMATION',font=('times new roman',11,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1480,height=270)
        
        # Labels and Entry Fill
        lbl_dep=Label(upper_frame,text='Bike Company',font=('arial',12,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)
        
        combo_gender=ttk.Combobox(upper_frame,textvariable=self.var_1,font=('arial',12,'bold'),width=17,state="readonly")
        combo_gender['value']=('Select Company','Begauss','OLA','TVS','SUZUKI')
        combo_gender.current(0)
        combo_gender.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #name
        lbl_Name=Label(upper_frame,text='Driver Name',font=('arial',12,'bold'),bg='white')
        lbl_Name.grid(row=0,column=2,padx=2,pady=7,sticky=W)
        
        txt_name=ttk.Entry(upper_frame,textvariable=self.var_3,font=('arial',11,'bold'),width=22)
        txt_name.grid(row=0,column=3,padx=2,pady=7)
        
        #BIke REgistration Number 
        lbl_BikeRegistNum=Label(upper_frame,text='Bike Regt. No.',font=('arial',12,'bold'),bg='white')
        lbl_BikeRegistNum.grid(row=1,column=0,padx=2,pady=7,sticky=W)
        
        txt_BikeRegistNum=ttk.Entry(upper_frame,textvariable=self.var_2,font=('arial',11,'bold'),width=22)
        txt_BikeRegistNum.grid(row=1,column=1,padx=2,pady=7, sticky=W)
        
        #Email
        lbl_Email=Label(upper_frame,text='Email ID',font=('arial',12,'bold'),bg='white')
        lbl_Email.grid(row=1,column=2,padx=2,pady=7,sticky=W)
        
        txt_Email=ttk.Entry(upper_frame,textvariable=self.var_9,font=('arial',11,'bold'),width=22)
        txt_Email.grid(row=1,column=3,padx=2,pady=7)
        
        #Initial Km Reading
        lbl_KmReading=Label(upper_frame,text='KM Reading',font=('arial',12,'bold'),bg='white')
        lbl_KmReading.grid(row=2,column=0,padx=2,pady=7,sticky=W)
        
        txt_KmReading=ttk.Entry(upper_frame,textvariable=self.var_11,font=('arial',11,'bold'),width=22)
        txt_KmReading.grid(row=2,column=1,padx=2,pady=7)
        
        #phonenumber
        lbl_Phone=Label(upper_frame,text='Phone No.',font=('arial',12,'bold'),bg='white')
        lbl_Phone.grid(row=2,column=2,padx=2,pady=7,sticky=W)
        
        txt_Phone=ttk.Entry(upper_frame,textvariable=self.var_5,font=('arial',11,'bold'),width=22)
        txt_Phone.grid(row=2,column=3,padx=2,pady=7)
        
        #gender
        lbl_gender=Label(upper_frame,text='Gender',font=('arial',12,'bold'),bg='white')
        lbl_gender.grid(row=3,column=2,padx=2,sticky=W)
        
        combo_gender=ttk.Combobox(upper_frame,textvariable=self.var_14,font=('arial',12,'bold'),width=17,state="readonly")
        combo_gender['value']=('Select Gender','Male','Female','Trans','Other')
        combo_gender.current(0)
        combo_gender.grid(row=3,column=3,padx=2,pady=10,sticky=W)
        
        #KYC
        # lbl_KYC=Label(upper_frame,text='KYC',font=('arial',12,'bold'),bg='white')
        # lbl_KYC.grid(row=4,column=2,padx=2,sticky=W)
        
        # combo_KYC=ttk.Combobox(upper_frame,font=('arial',12,'bold'),width=17,state="readonly")
        # combo_KYC['value']=('Choose','Adhar','PanCard','Driving Licence','Other')
        # combo_KYC.current(0)
        # combo_KYC.grid(row=4,column=3,padx=2,pady=10,sticky=W)
        
        # #kycdetail
        # lbl_kycdetail=Label(upper_frame,text='KYC Detail',font=('arial',12,'bold'),bg='white')
        # lbl_kycdetail.grid(row=5,column=2,padx=2,pady=7,sticky=W)
        
        # txt_kycdetail=ttk.Entry(upper_frame,font=('arial',11,'bold'),width=22)
        # txt_kycdetail.grid(row=5,column=3,padx=2,pady=7)
        
        self.var_com_search=StringVar()
        com_txt_kycdetail=ttk.Combobox(upper_frame,textvariable=self.var_15,state='readonly',
                                                        font=('arial',12,'bold'),width=18)
        com_txt_kycdetail['value']=('KYC Option','Adhar Card','Pan Card','Driving License')
        com_txt_kycdetail.current(0)
        com_txt_kycdetail.grid(row=4,column=2,padx=2,sticky=W)
        
        txt_kycdetail=ttk.Entry(upper_frame,textvariable=self.var_16,width=22,font=('arial',11,'bold'))
        txt_kycdetail.grid(row=4,column=3,padx=2,pady=7)
        
        #pickupdate
        lbl_Pickup=Label(upper_frame,text='Pickup Date',font=('arial',12,'bold'),bg='white')
        lbl_Pickup.grid(row=3,column=0,padx=2,pady=7,sticky=W)
        
        txt_Pickup=ttk.Entry(upper_frame,textvariable=self.var_11,font=('arial',11,'bold'),width=22)
        txt_Pickup= DateEntry(upper_frame, date_pattern='dd/mm/yyyy',width=26,padx=2,pady=7)
        txt_Pickup.grid(row=3,column=1,padx=2,pady=7)
         
        #dropdate
        lbl_Drop=Label(upper_frame,text='Drop Date',font=('arial',12,'bold'),bg='white')
        lbl_Drop.grid(row=4,column=0,padx=2,pady=7,sticky=W)
        
        txt_Drop=ttk.Entry(upper_frame,textvariable=self.var_12,font=('arial',11,'bold'),width=22)
        txt_Drop= DateEntry(upper_frame, date_pattern='dd/mm/yyyy',width=26,padx=2,pady=7)
        txt_Drop.grid(row=4,column=1,padx=2,pady=7)
        
        #securitydeposit
        lbl_security=Label(upper_frame,text='Security Deposit',font=('arial',12,'bold'),bg='white')
        lbl_security.grid(row=0,column=5,padx=2,sticky=W)
        
        combo_security=ttk.Combobox(upper_frame,textvariable=self.var_4,font=('arial',12,'bold'),width=17,state="readonly")
        combo_security['value']=('Choose Amount','Amount1','Amount2','Amount3','Enter Amount')
        combo_security.current(0)
        combo_security.grid(row=0,column=6,padx=2,pady=10,sticky=W)
        
        #modeofpayment
        lbl_mode=Label(upper_frame,text='Mode Of Payment',font=('arial',12,'bold'),bg='white')
        lbl_mode.grid(row=1,column=5,padx=2,sticky=W)
        
        combo_mode=ttk.Combobox(upper_frame,textvariable=self.var_7,font=('arial',12,'bold'),width=17,state="readonly")
        combo_mode['value']=('Choose Mode','Online','Cash','GPay','PhonePay')
        combo_mode.current(0)
        combo_mode.grid(row=1,column=6,padx=2,pady=10,sticky=W)
        
        #payment Reference Id 
        lbl_id=Label(upper_frame,text='Payment Ref.ID',font=('arial',12,'bold'),bg='white')
        lbl_id.grid(row=2,column=5,padx=2,pady=7,sticky=W)
        
        txt_id=ttk.Entry(upper_frame,font=('arial',11,'bold'),width=22)
        txt_id.grid(row=2,column=6,padx=2,pady=7)
        
        
        
        
        #rentamount
        lbl_amount=Label(upper_frame,text='Rent Amount',font=('arial',12,'bold'),bg='white')
        lbl_amount.grid(row=3,column=5,padx=2,pady=7,sticky=W)
        
        txt_amount=ttk.Entry(upper_frame,textvariable=self.var_6,font=('arial',11,'bold'),width=22)
        txt_amount.grid(row=3,column=6,padx=2,pady=7)
        
              
        #rentdate
        lbl_amount=Label(upper_frame,text='Rent Date',font=('arial',12,'bold'),bg='white')
        lbl_amount.grid(row=4,column=5,padx=2,pady=7,sticky=W)
        
        txt_amount=ttk.Entry(upper_frame,textvariable=self.var_13,font=('arial',11,'bold'),width=22)
        txt_amount= DateEntry(upper_frame, date_pattern='dd/mm/yyyy',width=26,padx=2,pady=7)
        txt_amount.grid(row=4,column=6,padx=2,pady=7)
       
        #hub details
        lbl_security=Label(upper_frame,text='Choose Hub',font=('arial',12,'bold'),bg='white')
        lbl_security.grid(row=5,column=0,padx=2,sticky=W)
        
        combo_security=ttk.Combobox(upper_frame,textvariable=self.var_4,font=('arial',12,'bold'),width=17,state="readonly")
        combo_security['value']=('Choose HUB','HUB1','HUB2','HUB3','HUB4')
        combo_security.current(0)
        combo_security.grid(row=5,column=1,padx=2,pady=10,sticky=W)
        
        #upload images
        # lbl_Image = Label(upper_frame, text='Upload Image ', font=('arial', 12, 'bold'), bg='white')
        # lbl_Image.grid(row=1, column=7, padx=2, pady=7, sticky=W)

       

        # btn_browse = Button(upper_frame, text='Upload Image 1', command=self.browse_image, font=('arial', 11, 'bold'), width=12)
        # self.image_path = StringVar()
        # txt_Image = ttk.Entry(upper_frame, textvariable=self.image_path, font=('arial', 11, 'bold'), width=17, state='readonly')
        # txt_Image.grid(row=0, column=7, padx=2, pady=7, sticky=W)
        # btn_browse.grid(row=0, column=8, padx=2, pady=7, sticky=W)
        
        
        # self.image_path = StringVar()
        # txt_Image = ttk.Entry(upper_frame, textvariable=self.image_path, font=('arial', 11, 'bold'), width=22, state='readonly')
        # txt_Image.grid(row=5, column=3, padx=2, pady=7, sticky=W)

        # btn_browse = Button(upper_frame, text='Upload Image 2', command=self.browse_image, font=('arial', 11, 'bold'), width=12)
        # btn_browse.grid(row=5, column=3, padx=2, pady=7, sticky=W)
        
        # self.image_path = StringVar()
        # txt_Image = ttk.Entry(upper_frame, textvariable=self.image_path, font=('arial', 11, 'bold'), width=22, state='readonly')
        # txt_Image.grid(row=5, column=4, padx=2, pady=7, sticky=W)

        # btn_browse = Button(upper_frame, text='Upload Image 3', command=self.browse_image, font=('arial', 11, 'bold'), width=12)
        # btn_browse.grid(row=5, column=4, padx=2, pady=7, sticky=W)
        
        # self.image_path = StringVar()
        # txt_Image = ttk.Entry(upper_frame, textvariable=self.image_path, font=('arial', 11, 'bold'), width=22, state='readonly')
        # txt_Image.grid(row=5, column=5, padx=2, pady=7, sticky=W)

        # btn_browse = Button(upper_frame, text='Upload Image 4', command=self.browse_image, font=('arial', 11, 'bold'), width=12)
        # btn_browse.grid(row=5, column=5, padx=2, pady=7, sticky=W)
        
               
        # #imageandbutton mask scooter image
        # img_mask=Image.open('images/SCUTU.jpeg')
        # img_mask=img_mask.resize((200,200),Image.BILINEAR)
        # self.photomask=ImageTk.PhotoImage(img_mask)
         
        # self.img_mask=Label(upper_frame,image=self.photomask)
        # self.img_mask.place(x=1100,y=20,width=200,height=200)
        
        #buttonFrame
        Button_Frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        Button_Frame.place(x=1290,y=10,width=170,height=210)
        
        #btmadd
        btn_add=Button(Button_Frame,text="SAVE",command=self.add_data,font=('arial',15,'bold'),width=13,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=1,pady=5)
        
        btn_update=Button(Button_Frame,text="UPDATE",font=('arial',15,'bold'),width=13,bg='blue',fg='white')
        btn_update.grid(row=1,column=0,padx=1,pady=5)
        
        btn_delete=Button(Button_Frame,text="DELETE",font=('arial',15,'bold'),width=13,bg='blue',fg='white')
        btn_delete.grid(row=2,column=0,padx=1,pady=5)
        
        btn_clear=Button(Button_Frame,text="CLEAR",font=('arial',15,'bold'),width=13,bg='blue',fg='white')
        btn_clear.grid(row=3,column=0,padx=1,pady=5)
        
        
        # downframe
        down_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='orange',text='BIKE AND RIDER INFORMATION TABLE',font=('times new roman',11,'bold'),fg='red')
        down_frame.place(x=10,y=280,width=1480,height=270)
        
        #searchframe
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text='SEARCH BIKE INFORMATION',font=('times new roman',11,'bold'),fg='red')
        search_frame.place(x=0,y=0,width=1470,height=60)
        
        search_by=Label(search_frame,text="SEARCH BY",font=('arial',15,'bold'),width=13,bg='green',fg='white')
        search_by.grid(row=0,column=0,padx=5,sticky=W)
        
        #search
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,state='readonly',
                                                        font=('arial',12,'bold'),width=18)
        com_txt_search['value']=('Select Option','Driver Name','Bike Registration No','Security Deposit','Gender')
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,padx=5,pady=10,sticky=W)
        
        txt_search=ttk.Entry(search_frame,width=22,font=('arial',11,'bold'))
        txt_search.grid(row=0,column=2,padx=5)
        
        btn_search=Button(search_frame,text="Search",font=('arial',11,'bold'),width=14,background="green",foreground="white")
        btn_search.grid(row=0,column=3,padx=5)
        
        
        btn_Showall=Button(search_frame,text="Show All",font=('arial',11,'bold'),width=14 ,foreground='white',background="green")
        btn_Showall.grid(row=0,column=4,padx=5)
        
        gogreen=Label(search_frame,text="Go Green",font=('Arial',30,'bold'),width=14 ,foreground='green',background="white")
        gogreen.place(x=910,y=0,width=600,height=30)
        
        img_logo_green=Image.open(r'images/charging.png')
        img_logo_green=img_logo_green.resize((25,25),Image.BILINEAR)
        self.photoimg_logo_green=ImageTk.PhotoImage(img_logo_green)
        
        self.logo=Label(search_frame,image=self.photoimg_logo_green)
        self.logo.place(x=1020,y=0,width=50,height=30)
        
        ##########################BIKE TABLE ######################################
        #tableframe
        table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=190) 
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL) 
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.Bike_table=ttk.Treeview(table_frame,columns=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Bike_table.xview)
        scroll_y.config(command=self.Bike_table.yview)
        
        self.Bike_table.heading('1',text='Bike Company')
        self.Bike_table.heading('2',text='Bike Regist No.')
        self.Bike_table.heading('3',text='Driver Name')
        self.Bike_table.heading('4',text='Security Deposit')
        self.Bike_table.heading('5',text='Phone No.')
        self.Bike_table.heading('6',text='Rent Amount')
        self.Bike_table.heading('7',text='Mode Of Payment')
        self.Bike_table.heading('8',text='Payment Referenc ID')
        self.Bike_table.heading('9',text='Email ID')
        self.Bike_table.heading('10',text='KM Reading')
        self.Bike_table.heading('11',text='Pickup Date')
        self.Bike_table.heading('12',text='Drop Date')
        self.Bike_table.heading('13',text='Rent Date')
        self.Bike_table.heading('14',text='Gender')
        self.Bike_table.heading('15',text='KYC Type')
        self.Bike_table.heading('16',text='KYC Id')
        self.Bike_table.heading('17',text='Choose Hub')
        
        self.Bike_table['show']='headings'
        
        self.Bike_table.column("1",width=100)
        self.Bike_table.column("2",width=100)
        self.Bike_table.column("3",width=100)
        self.Bike_table.column("4",width=100)
        self.Bike_table.column("5",width=100)
        self.Bike_table.column("6",width=100)
        self.Bike_table.column("7",width=100)
        self.Bike_table.column("8",width=100)
        self.Bike_table.column("9",width=100)
        self.Bike_table.column("10",width=100)
        self.Bike_table.column("11",width=100)
        self.Bike_table.column("12",width=100)
        self.Bike_table.column("13",width=100)
        self.Bike_table.column("14",width=100)
        self.Bike_table.column("15",width=100)
        self.Bike_table.column("16",width=100)
        self.Bike_table.column("17",width=100)
        
        
        self.Bike_table.pack(fill=BOTH,expand=1)
        
        self.fetch_data()
        
        
    ###########function Declaration###############
    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            self.image_path.set(file_path)
            with open(file_path, 'rb') as file:
                self.image_data = file.read()
    
    def add_data(self):
        if self.var_2.get()=='' or self.var_3.get()=='':
            messagebox.showerror('Error','All fields are Required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='sanjay@23',database='mydata')
                my_cursor=conn.cursor()
                my_cursor=conn.cursor('insert into scutubikemanagement(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                    
                    
                    
                                         
                                                                                                                                self.var_2.get(),
                                                                                                                                self.var_3.get(),
                                                                                                                                self.var_1.get(),                                                                                                                
                                                                                                                                self.var_4.get(),
                                                                                                                                self.var_5.get(),
                                                                                                                                self.var_6.get(),
                                                                                                                                self.var_7.get(),
                                                                                                                                self.var_8.get(),
                                                                                                                                self.var_9.get(),
                                                                                                                                self.var_10.get(),
                                                                                                                                self.var_11.get(),
                                                                                                                                self.var_12.get(),
                                                                                                                                self.var_13.get(),
                                                                                                                                self.var_14.get(),
                                                                                                                                self.var_15.get(),
                                                                                                                                self.var_16.get(),
                                                                                                                                self.var_17.get(), 
                                                                                                                            ))
                conn.commit()
                conn.close()
                messagebox.showinfo('Successfully Bike Has Been Added',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to {str(es)}', parent=self.root)
    
    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='sanjay@a23',database='mydata')
        my_cursor=conn.cursor()
        my_cursor.execute('Select * from scutubikemanagement')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.Bike_table(*self.Bike_table.get_children)
            for i in data:
                self.Bike_table.insert("",END,value=i)
            conn.commit
        conn.close()
               




               
                
                
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Bike(root)
    root.mainloop()