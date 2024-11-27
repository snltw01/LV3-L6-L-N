import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

class Register(tk.Tk):
    def __init__(self):
        super().__init__()
        image = Image.open('IMG/IMG.jpg').resize((100,100))
        self.tk_image = ImageTk.PhotoImage(image)
        self.title('Form Đăng Kí')
        self.geometry('700x700+100+100')
        self.nation=['Việt Nam','Hàn Quốc','Nhật Bản','Mỹ',"Trung Quốc","Lào","Nga"]
        self.Creat_widget()

    def Creat_widget(self):
        frame1=tk.Frame(self)
        frame1.pack()

        lb1=tk.Label(frame1, image=self.tk_image)
        lb1.grid(row=0,column=1,columnspan=3,padx=80)
        lb2=tk.Label(frame1,text='Form Đăng Kí')
        lb2.grid(row=1,column=1,columnspan=3,pady=25)

        lb3=tk.Label(frame1,text="Họ và tên")
        lb3.grid(row=2,column=0)

        en1=tk.Entry(frame1)
        en1.grid(row=2,column=1,padx=30,pady=20)

        lb4=tk.Label(frame1,text='Địa chỉ')
        lb4.grid(row=2,column=2)

        en2=tk.Entry(frame1)
        en2.grid(row=2,column=3,padx=30,pady=20)

        lb5=tk.Label(frame1,text="Ngày sinh")
        lb5.grid(row=3,column=0)
        
        en3=tk.Entry(frame1)
        en3.grid(row=3,column=1,padx=30,pady=20)

        lb6=tk.Label(frame1,text="Email")
        lb6.grid(row=3,column=2)

        en4=tk.Entry(frame1)
        en4.grid(row=3,column=3,padx=30,pady=20) 

        lb7=tk.Label(frame1,text="Quốc tịch")
        lb7.grid(row=4,column=0)
        
        combobox=ttk.Combobox(frame1,values=self.nation, state='readonly')
        combobox.grid(row=4,column=1,padx=30,pady=20)

        lb8=tk.Label(frame1,text="Số Điện thoại")
        lb8.grid(row=4,column=2)

        en5=tk.Entry(frame1)
        en5.grid(row=4,column=3,padx=30,pady=20)


Form1=Register()
Form1.mainloop()
