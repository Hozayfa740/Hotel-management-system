
from tkinter import *
import PIL.Image
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
from hotel import HotelManagementSystem

class login:
    def __init__(self,root):
        self.user_name = StringVar()
        self.password = StringVar()
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1550x800+0+0")
        img1 = Image.open("sm1.jpg")
        img1 = img1.resize((1550, 800), PIL.Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        Lbimage = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        Lbimage.place(x=0, y=0, width=1550, height=800)
        login_frame=Frame(self.root, bg="white")
        login_frame.place(x=550,y=160,height=300,width=500)

        title=Label(login_frame,text="Login Here",font=("Impact",20,"bold"),fg="#7AC5CD",padx=10,pady=2,bg="white")
        title.place(x=190,y=10)
        title2 = Label(login_frame, text="Accountant Employee Login Area", font=("Goudy old style", 11, "bold"), fg="#53868B", padx=10, pady=2,bg="white")
        title2.place(x=150, y=55)

        user = Label(login_frame, text="Username", font=("times new roman", 15, "bold"),
                       fg="#8B8970" )
        user.place(x=15,y=100)
        entry_user = ttk.Entry(login_frame, width=30,textvariable=self.user_name,
                             font=("times new roman", 15))
        entry_user.place(x=15, y=140)

        password = Label(login_frame, text="Password", font=("times new roman", 15, "bold"),
                     fg="#8B8970" )
        password.place(x=15, y=180)
        entry_password = ttk.Entry(login_frame, width=30,textvariable=self.password,
                               font=("times new roman", 15),show="*")
        entry_password.place(x=15, y=220)

        forget=Button(login_frame, text="Forget Password?", cursor="hand2",font=("times new roman", 10),
                       fg="#7AC5CD",bd=0,bg="white")
        forget.place(x=15, y=260)
        login = Button(self.root, text="Login", command=self.loginf,cursor="hand2",font=("times new roman", 15,"bold"),
                        bg="#7AC5CD",fg="white", bd=0,padx=20,pady=-1)
        login.place(x=770, y=445)
    def loginf(self):
        if self.user_name.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.user_name.get()!="smrity" or self.password.get()!="123":
            messagebox.showerror("Error","Invalid Username Or Password",parent=self.root)
            self.user_name.set("")
            self.password.set("")
        elif self.user_name.get()=="smrity" or self.password.get()=="123":
            self.new_window = Toplevel(self.root)
            self.app = HotelManagementSystem(self.new_window)
            self.user_name.set("")
            self.password.set("")





if __name__ == '__main__':
    root=Tk()
    obj=login(root)
    root.mainloop()