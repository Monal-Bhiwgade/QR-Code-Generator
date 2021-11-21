from tkinter import *
import qrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage

class Qr_Generator:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Generator || Developed By MONAL BHIWGADE ")
        self.root.resizable(False, False)

        title = Label(self.root, text="   Qr Code Genrator", font=("times new roman", 40), bg="#053246", fg="white",
                      anchor="w").place(x=0, y=0, relwidth=1)

        # =====>  Student Details Window  <======
        # =====>  Variables  <=====
        self.var_student_code = StringVar()
        self.var_student_name = StringVar()
        self.var_student_department = StringVar()
        self.var_student_designation = StringVar()

        Stud_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Stud_Frame.place(x=50, y=100, width=500, height=380)

        Stud_title = Label(Stud_Frame, text="Student Details", font=("goudy old style", 20), bg="#043256",
                          fg="white").place(x=0, y=0, relwidth=1)

        lbl_Stud_code = Label(Stud_Frame, text="Student ID", font=("times new roman", 15, "bold"), bg="white", ).place(
            x=20, y=60)
        lbl_name = Label(Stud_Frame, text="Name", font=("times new roman", 15, "bold"), bg="white", ).place(x=20, y=100)
        lbl_department = Label(Stud_Frame, text="Department", font=("times new roman", 15, "bold"), bg="white", ).place(
            x=20, y=140)
        lbl_designation = Label(Stud_Frame, text="Designation", font=("times new roman", 15, "bold"),
                                bg="white", ).place(x=20, y=180)

        txt_Stud_code = Entry(Stud_Frame, font=("times new roman", 15,), textvariable=self.var_student_code,
                             bg="light yellow", ).place(x=200, y=60)
        txt_name = Entry(Stud_Frame, font=("times new roman", 15,), textvariable=self.var_student_name,
                         bg="light yellow", ).place(x=200, y=100)
        txt_department = Entry(Stud_Frame, font=("times new roman", 15,), textvariable=self.var_student_department,
                               bg="light yellow", ).place(x=200, y=140)
        txt_designation = Entry(Stud_Frame, font=("times new roman", 15,), textvariable=self.var_student_designation,
                                bg="light yellow", ).place(x=200, y=180)

        btn_generate = Button(Stud_Frame, text="QR Generate", command=self.generate,
                              font=("times new roman", 18, "bold"), bg="#2196f3", fg="White").place(x=90, y=250,
                                                                                                    width=180,
                                                                                                    height=30)
        btn_clear = Button(Stud_Frame, text="Clear", command=self.clear, font=("times new roman", 18, "bold"),
                           bg="#607d8b", fg="White").place(x=282, y=250, width=120, height=30)

        self.msg = ""
        self.lbl_msg = Label(Stud_Frame, text=self.msg, font=("times new roman", 20,), bg="white", fg="green")
        self.lbl_msg.place(x=0, y=310, relwidth=1)

        # =====>  Student QR Frame  <======
        qr_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        qr_Frame.place(x=600, y=100, width=250, height=380)

        Stud_title = Label(qr_Frame, text="QR Code", font=("goudy old style", 20), bg="#043256",
                          fg="white").place(x=0, y=0, relwidth=1)

        self.qr_code = Label(qr_Frame, text=" No QR Code \nAvailable !!", font=("times new roman", 15), bg="#3f51b5",
                             fg="white", bd=1)
        self.qr_code.place(x=35, y=100, width=180, height=180)

    def clear(self):
        self.var_student_code.set("")
        self.var_student_name.set("")
        self.var_student_department.set("")
        self.var_student_designation.set("")
        self.msg = ""
        self.lbl_msg.config(text=self.msg)

    def generate(self):
        if self.var_student_code.get() == "" or self.var_student_department.get() == "" or self.var_student_name.get() == "" or self.var_student_designation.get() == "":
            self.msg = "All Fields are required !"
            self.lbl_msg.config(text=self.msg, fg="red")
        else:
            qr_data = (f"Student ID: {self.var_student_code.get()}\n Student Name:{self.var_student_name.get()}\n Department: {self.var_student_department.get()} \n Designation: {self.var_student_designation.get()}")
            qr_code = qrcode.make(qr_data)
            print(qr_code)
            qr_code = resizeimage.resize_cover(qr_code,[180,180])

            # =============>QR Code Image Update <===============
            self.im = ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)
            # =============> Updating Notification <===============
            self.msg = "QR Code Generated Successfully !"
            self.lbl_msg.config(text=self.msg, fg="green")


root = Tk()
obj = Qr_Generator(root)
root.mainloop()
