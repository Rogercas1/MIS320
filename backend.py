from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Accessnegative:
    def __init__(self,root):
        self.root=root
        self.root.title("Access-Negative")
        self.root.geometry("1540x800+0+0")

        lbltitle = Label(self.root,bd=20,relief=RIDGE,text='Access-Negative', fg='red', bg='white',
                         font=('times new roman',50,'bold'))
        lbltitle.pack(side=TOP, fill=X)

        # Database
        Dataframe = Frame(self.root,bd=20, relief = RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=4000)
        DataframeLeft = LabelFrame(Dataframe,bd=10,relief = RIDGE, padx=10,
                                   font=('times new roman',12,'bold'),text = "UNIVERISTY INFORMATION")
        DataframeLeft.place(x=0, y=5, width=980,height=350)

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                   font=('times new roman', 12, 'bold'), text="Unknown")
        DataframeRight.place(x=990, y=5, width=460, height=350)

        # Buttons
        Buttonframe=Frame(self.root,bd=20, relief =RIDGE)
        Buttonframe.place(x=0,y=530, width=1530, height=70)

        # Details
        Detailframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailframe.place(x=0, y=600, width=1530, height=190)

        # Data to the left
        University_name = Label(DataframeLeft, font=('arial', 12, 'bold'), text="Name of University", padx=2, pady=6)
        University_name.grid(row=0, column=0, sticky=W)

        comUniversity_name = ttk.Combobox(DataframeLeft,font=('arial', 12, 'bold'), width = 33,  )
        comUniversity_name['values'] = ('Iowa State University', 'University of Iowa', 'University of Northern Iowa')
        comUniversity_name.grid(row=0,column=1)


        College_name = Label(DataframeLeft, font=('arial', 12, 'bold'), text="College Name", padx=2, pady=6)
        College_name.grid(row=1, column=0, sticky=W)
        txtCollege_Name = Entry(DataframeLeft, font=('arial', 12, 'bold'), width = 35 )
        txtCollege_Name.grid(row=1,column=1)

        Department_name = Label(DataframeLeft, font=('arial', 12, 'bold'), text="Department Name", padx=2, pady=6)
        Department_name.grid(row=2, column=0, sticky=W)
        txtDepartment_Name = Entry(DataframeLeft, font=('arial', 12, 'bold'), width=35)
        txtDepartment_Name.grid(row=2, column=1)

        Major_name = Label(DataframeLeft, font=('arial', 12, 'bold'), text="Major", padx=2, pady=6)
        Major_name.grid(row=3, column=0, sticky=W)
        txtMajor_name = Entry(DataframeLeft, font=('arial', 12, 'bold'), width=35)
        txtMajor_name.grid(row=3, column=1)

        Section_name = Label(DataframeLeft, font=('arial', 12, 'bold'), text="Section", padx=2, pady=6)
        Section_name.grid(row=4, column=0, sticky=W)
        txtSection_name = Entry(DataframeLeft, font=('arial', 12, 'bold'), width=35)
        txtSection_name.grid(row=4, column=1)

        Building_name = Label(DataframeLeft, font=('arial', 12, 'bold'), text="Building", padx=2, pady=6)
        Building_name.grid(row=5, column=0, sticky=W)
        txtBuilding_name = Entry(DataframeLeft, font=('arial', 12, 'bold'), width=35)
        txtBuilding_name.grid(row=5, column=1)

        Building_name = Label(DataframeLeft, font=('arial', 12, 'bold'), text="Building", padx=2, pady=6)
        Building_name.grid(row=5, column=0, sticky=W)
        txtBuilding_name = Entry(DataframeLeft, font=('arial', 12, 'bold'), width=35)
        txtBuilding_name.grid(row=5, column=1)





root = Tk()
ob = Accessnegative(root)
root.mainloop()
