from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class details_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1300x550+228+250")

        #==========variables======
        self.var_floor = StringVar()
        self.var_room = StringVar()
        self.var_room_Type = StringVar()

        # =============title=========
        lbl_title = Label(self.root, text="ROOMBOOKING DETAILS", font=("times new roman", 18, "bold"),
                          bg="#D9D9D6", fg="black", bd=1, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1300, height=50)

        # =========logo==========
        img2 = Image.open("sm2.jpg")
        img2 = img2.resize((100, 50), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        Lbimage = Label(self.root, image=self.photoimg2, bd=2, relief=RIDGE)
        Lbimage.place(x=0, y=0, width=100, height=50)

        # =================label frame==========
        label_frameleft = LabelFrame(self.root, bd=4, relief=RIDGE, text="New Room Add",
                                     font=("times new roman", 15, "bold"), bg="white", fg="black")
        label_frameleft.place(x=5, y=50, width=540, height=350)

        #===========floor================
        lb1_floor = Label(label_frameleft, text="Floor No", font=("times new roman", 12, "bold"), padx=2, pady=4)
        lb1_floor.grid(row=0, column=0, sticky=W)
        entry_floor = ttk.Entry(label_frameleft, width=29, textvariable=self.var_floor,
                                font=("times new roman", 12, "bold"))
        entry_floor.grid(row=0, column=1, sticky=W)

        #======room no=============
        lb1_Room = Label(label_frameleft, text="Room No", font=("times new roman", 12, "bold"), padx=2, pady=4)
        lb1_Room.grid(row=1, column=0, sticky=W)
        entry_room = ttk.Entry(label_frameleft, width=29, textvariable=self.var_room,
                               font=("times new roman", 12, "bold"))
        entry_room.grid(row=1, column=1, sticky=W)

        #=======Room Type=========
        lb1_room_type = Label(label_frameleft, text="Room Type", font=("times new roman", 12, "bold"), padx=2, pady=4)
        lb1_room_type.grid(row=2, column=0, sticky=W)
        entry_room_typ = ttk.Entry(label_frameleft, width=29, textvariable=self.var_room_Type,
                                   font=("times new roman", 12, "bold"))
        entry_room_typ.grid(row=2, column=1, sticky=W)

        # ===============buttons=========
        btn_frame = Frame(label_frameleft, bd=1, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=412)

        btn_add = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 12, "bold"),
                         bg="#D9D9D6", fg="black", width=9)
        btn_add.grid(row=0, column=0, padx=1)

        btn_update = Button(btn_frame, text="Update", command=self.update, font=("arial", 12, "bold"),
                            bg="#D9D9D6", fg="black", width=9)
        btn_update.grid(row=0, column=1, padx=1)

        btn_delete = Button(btn_frame, text="Delete", command=self.deletef, font=("arial", 12, "bold"),
                            bg="#D9D9D6", fg="black", width=9)
        btn_delete.grid(row=0, column=2, padx=1)

        btn_reset = Button(btn_frame, text="Reset", command=self.reset, font=("arial", 12, "bold"),
                           bg="#D9D9D6", fg="black", width=10)
        btn_reset.grid(row=0, column=3, padx=1)

        #=========right frame==========
        label_frameright = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details",
                                      font=("times new roman", 15, "bold"), bg="white", fg="black")
        label_frameright.place(x=600, y=55, width=600, height=350)

        # ---------------show table----------#
        scroll_x = ttk.Scrollbar(label_frameright, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(label_frameright, orient=VERTICAL)
        self.cust_Details_Table = ttk.Treeview(label_frameright, columns=("Floor", "RoomNo", "RoomType"),
                                               xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.cust_Details_Table.xview)
        scroll_y.config(command=self.cust_Details_Table.yview)

        self.cust_Details_Table.heading("Floor", text="Floor")
        self.cust_Details_Table.heading("RoomNo", text="RoomNo")
        self.cust_Details_Table.heading("RoomType", text="RoomType")
        self.cust_Details_Table["show"] = "headings"
        self.cust_Details_Table.column("Floor", width=100)
        self.cust_Details_Table.column("RoomNo", width=100)
        self.cust_Details_Table.column("RoomType", width=100)
        self.cust_Details_Table.pack(fill=BOTH, expand=1)
        self.cust_Details_Table.bind("<ButtonRelease-1>", self.get_vale)

        self.fetch_data()

    # =================CRUD FUNCTIONS================

    def add_data(self):
        if self.var_room.get().strip() == "":
            messagebox.showerror("Hotel Management System", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="smrity",
                                               auth_plugin="mysql_native_password")
                my_cursor = conn.cursor(buffered=True)
                my_cursor.execute("INSERT INTO details (Floor, RoomNo, RoomType) VALUES (%s,%s,%s)", (
                    self.var_floor.get().strip(),
                    self.var_room.get().strip(),
                    self.var_room_Type.get().strip()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Hotel Management System", "New Room Added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="smrity",
                                           auth_plugin="mysql_native_password")
            my_cursor = conn.cursor(buffered=True)
            my_cursor.execute("SELECT * FROM details")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.cust_Details_Table.delete(*self.cust_Details_Table.get_children())
                for i in rows:
                    self.cust_Details_Table.insert("", END, values=(str(i[0]), str(i[1]), str(i[2])))
            conn.close()
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def get_vale(self, event=""):
        curser_row = self.cust_Details_Table.focus()
        content = self.cust_Details_Table.item(curser_row)
        row = content["values"]
        if row:
            self.var_floor.set(str(row[0]).strip())
            self.var_room.set(str(row[1]).strip())
            self.var_room_Type.set(str(row[2]).strip())

    def update(self):
        if self.var_room.get().strip() == "":
            messagebox.showerror("Hotel Management System", "Please enter room number", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="smrity",
                                               auth_plugin="mysql_native_password")
                my_cursor = conn.cursor(buffered=True)

                floor_val = self.var_floor.get().strip()
                room_val = self.var_room.get().strip()
                roomtype_val = self.var_room_Type.get().strip()

                my_cursor.execute("""
                    UPDATE details 
                    SET Floor=%s, RoomType=%s 
                    WHERE RoomNo=%s
                """, (
                    floor_val,
                    roomtype_val,
                    room_val
                ))
                conn.commit()

                if my_cursor.rowcount == 0:
                    messagebox.showwarning("Update Failed", f"No record found for RoomNo={room_val}", parent=self.root)
                else:
                    self.fetch_data()
                    messagebox.showinfo("Hotel Management System", "Room details updated successfully", parent=self.root)

                conn.close()
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def deletef(self):
        deletecheck = messagebox.askyesno("Hotel Management System", "Do you want to delete this room?", parent=self.root)
        if deletecheck:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="34632", database="smrity",
                                               auth_plugin="mysql_native_password")
                my_cursor = conn.cursor(buffered=True)
                my_cursor.execute("DELETE FROM details WHERE RoomNo=%s", (self.var_room.get().strip(),))
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def reset(self):
        self.var_floor.set("")
        self.var_room.set("")
        self.var_room_Type.set("")
        self.fetch_data()


if __name__ == '__main__':
    root = Tk()
    obj = details_win(root)
    root.mainloop()
